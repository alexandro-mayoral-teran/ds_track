# Lab 10.03 — Construir, explicar y ejecutar una consulta lazy

## Propósito y entradas

Practicar la [lección 10.03](../../../curriculum/10_polars_duckdb/03_polars_lazy_plans/README.md)
y distinguir el plan previsto de los resultados comprobados. Necesitas Python
con Polars 2.0.0; los [recorridos completos](../../../curriculum/10_polars_duckdb/03_polars_lazy_plans/recorridos.md)
explican el entorno y la ejecución. No necesitas entregas previas.

La [fuente CSV propia](../../../curriculum/10_polars_duckdb/03_polars_lazy_plans/muestra.csv)
contiene todos estos datos:

| ID textual | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Unidad crédito/corte; clave ID/fecha única. IDs de tres dígitos, fechas válidas
1900–2100, pesos enteros 0–2147483647, sin ausencias. Ante una incidencia se
rechaza toda la fuente. No modifiques este CSV ni resultados de prácticas previas.

## Actividad

1. Escribe a mano pares, conteos y sumas para septiembre ≥ 2000, septiembre
   ≥ 2001, octubre ≥ 0 y noviembre ≥ 2000.
2. Prepara una carpeta nueva con Parquet. Construye el plan de septiembre
   ≥ 2000 sin recoger todavía la salida. Compara `collect_schema()` de fuente
   y consulta, y explica por qué no conoces el número de filas solo con eso.
3. Examina los planes sin optimizar y optimizado. Señala fuente, filtros,
   proyección y orden; explica por qué el scan necesita tres columnas para
   devolver solo ID/saldo. Examina también el resumen por corte: ¿qué columna
   puede dejar de leer y por qué?
4. Ejecuta las cuatro selecciones, comprueba sus tipos y cada par contra CSV
   externo. Relee el resumen y contrasta 4500/4600 MXN. Explica por qué sumar
   cortes distintos no produce saldo a una fecha.
5. Crea un Parquet vacío con esquema explícito en otra carpeta nueva: compara
   selección vacía y resumen agrupado vacío. No elimines los tipos para lograrlo.
6. En una copia nueva del Parquet, cambia solo el saldo de `001` en septiembre
   de cero a `-1`. La consulta de octubre sigue devolviendo `003/2600`.
   Demuestra que la auditoría completa rechaza esa fuente.
7. Reinicia Python o usa otro proceso para verificar el Parquet original.
   Conserva scripts, planes y explicación en tu carpeta nueva bajo `output/`.

## Resultado y comprobación

| Escenario | Pares ID/saldo | Registros | Suma MXN |
| --- | --- | ---: | ---: |
| Septiembre ≥ 2000 | 002/2000, 003/2500 | 2 | 4500 |
| Septiembre ≥ 2001 | 003/2500 | 1 | 2500 |
| Octubre ≥ 0 | 001/100, 002/1900, 003/2600 | 3 | 4600 |
| Noviembre ≥ 2000 | Ninguno | 0 | 0 |

Fuente String/Date/Int32; selección String/Int32, incluso `(0, 2)`.
Resumen Date/UInt32/Int64: dos filas para la fuente completa; `(0, 3)` para
fuente vacía. La suma cero de una selección sin filas es un control, no una
fila inventada en un grupo inexistente. Los planes no se comparan como cadenas
literales: explica su significado y comprueba los valores materializados.

<details>
<summary>Solución razonada: preparación y consultas completas</summary>

Desde la raíz, en un script Python nuevo con el intérprete seleccionado:

```python
from datetime import date
from pathlib import Path
import sys
import polars as pl

modulos = Path("curriculum/10_polars_duckdb/03_polars_lazy_plans").resolve()
sys.path.insert(0, str(modulos))
from consultas_lazy import (
    ESQUEMA, abrir, preparar, seleccionar, resumir, ejecutar_verificado,
)

ruta = preparar("output/lazy_1003_lab")
entrada = abrir(ruta)
consulta = seleccionar(entrada, date(2026, 9, 30), 2000)
assert isinstance(consulta, pl.LazyFrame)
assert dict(entrada.collect_schema()) == ESQUEMA
assert dict(consulta.collect_schema()) == {"id_credito": pl.String, "saldo_mxn": pl.Int32}
print(consulta.explain(optimized=False))
print(consulta.explain())
print(resumir(entrada).explain())

for corte, minimo, pares in [
    (date(2026, 9, 30), 2000, [("002", 2000), ("003", 2500)]),
    (date(2026, 9, 30), 2001, [("003", 2500)]),
    (date(2026, 10, 31), 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    (date(2026, 11, 30), 2000, []),
]:
    entrega = ejecutar_verificado(ruta, corte=corte, minimo=minimo)
    assert entrega["seleccion"].rows() == pares
    assert entrega["control"]["registros"] == len(pares)
    assert entrega["control"]["saldo_mxn"] == sum(saldo for _, saldo in pares)
    assert entrega["resumen"]["saldo_mxn"].to_list() == [4500, 4600]
    print(entrega["control"])
```

El verificador no confía solo en estas sumas: reconstruye cada par desde CSV
con Python estándar y compara tipos y valores. El resumen necesita fecha/saldo;
la selección necesita además ID. El filtro de fecha no permite eliminar fecha
del scan aunque esa columna desaparezca de la salida.

</details>

<details>
<summary>Solución razonada: vacío, incidente fuera del filtro y evidencia</summary>

Continuación del bloque anterior. Cada caso conserva sus archivos originales.

```python
carpeta_vacia = Path("output/lazy_1003_lab_vacio")
carpeta_vacia.mkdir(parents=True, exist_ok=False)
fuente_vacia = carpeta_vacia / "vacio.csv"
fuente_vacia.write_text("id_credito,fecha_corte,saldo_mxn\n", encoding="utf-8")
ruta_vacia = preparar(carpeta_vacia / "parquet", fuente_vacia)
vacio = ejecutar_verificado(ruta_vacia, fuente_vacia)
assert vacio["seleccion"].shape == (0, 2)
assert vacio["resumen"].shape == (0, 3)
assert vacio["control"]["saldo_mxn"] == 0
assert vacio["resumen"].schema["saldo_mxn"] == pl.Int64

carpeta_error = Path("output/lazy_1003_lab_error")
carpeta_error.mkdir(parents=True, exist_ok=False)
original = pl.read_parquet(ruta)
alterada = original.with_columns(
    pl.when((pl.col("id_credito") == "001") & (pl.col("fecha_corte") == date(2026, 9, 30)))
    .then(pl.lit(-1, dtype=pl.Int32))
    .otherwise(pl.col("saldo_mxn"))
    .alias("saldo_mxn")
)
ruta_error = carpeta_error / "alterada.parquet"
alterada.write_parquet(ruta_error)
solo_consulta = seleccionar(abrir(ruta_error)).collect()
assert solo_consulta.rows() == [("003", 2600)]
try:
    ejecutar_verificado(ruta_error)
except ValueError as error:
    print("Rechazo esperado:", error)
else:
    raise AssertionError("La auditoria debio rechazar el saldo negativo")
assert pl.read_parquet(ruta).equals(original)

evidencia = ruta.parent / "evidencia"
evidencia.mkdir(exist_ok=False)
for nombre, plan in ejecutar_verificado(ruta)["planes"].items():
    (evidencia / f"{nombre}.txt").write_text(plan, encoding="utf-8")
```

`when(condición).then(valor).otherwise(otro)` es una expresión condicional
usada solo para fabricar el error en una copia: cambia esa fila y conserva
las demás. `lit` crea el literal -1 con tipo Int32. No limpia la fuente ni forma
parte de la consulta esencial. Un tipo correcto no demuestra saldo no negativo.

Para verificar desde otro proceso, conserva la carpeta y ejecuta con tu entorno
activo en la terminal del sistema:

```text
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_lab/muestra.parquet
```

Con uv usa `uv run --locked python -X utf8` en lugar de `python -X utf8`.
El comando no prepara ni sobrescribe archivos. Guardar los planes no sustituye
ejecutar ni conciliar. Escribe también tu explicación y las versiones usadas.

</details>

## Reflexión y evidencia

- ¿Qué lectura ya ocurrió si escribiste `read_parquet(...).lazy()`?
- ¿Qué diferencia hay entre conocer el esquema y conocer los valores?
- ¿Por qué el plan de la selección necesita fecha, pero la salida no la incluye?
- ¿Por qué `PROJECT 2/3` no significa «dos de cada tres filas»?
- ¿Qué error quedó oculto a la consulta de octubre? ¿Qué control lo detectó?
- ¿Qué falta medir antes de afirmar que el plan ahorra disco o RAM?

Entrega tu script, versiones, planes anotados, pares/resumen conciliados y el
rechazo esperado de la copia. Registra evidencia y dudas en
[PROGRESS.md](../../../PROGRESS.md). No publiques salidas ni entornos.
El proyecto `04_large_credit_dataset` y sus checkpoints siguen pendientes.

Siguiente: [10.04 — Tipos, faltantes y uniones](../../../curriculum/10_polars_duckdb/04_types_missing_joins/README.md).
Vuelve a la
[lección 10.03](../../../curriculum/10_polars_duckdb/03_polars_lazy_plans/README.md)
si quedan conceptos esenciales por explicar.

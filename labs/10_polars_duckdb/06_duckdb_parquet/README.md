# Lab 10.06 — Consultar y explicar SQL sobre Parquet

## Propósito y entradas

Practicar la [lección 10.06](../../../curriculum/10_polars_duckdb/06_duckdb_parquet/README.md)
con Python/DuckDB 2.0.0. Los [recorridos](../../../curriculum/10_polars_duckdb/06_duckdb_parquet/recorridos.md)
explican el entorno. No necesitas entregas previas ni completar la extensión
10.05. La fuente propia contiene exactamente estas filas:

| ID textual | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Unidad crédito/corte; clave ID/fecha única; ID de tres dígitos, fechas válidas
1900–2100 y saldos enteros 0–2147483647 sin ausencias. El
[CSV incluido](../../../curriculum/10_polars_duckdb/06_duckdb_parquet/muestra.csv)
se conserva intacto. Trabaja con carpetas nuevas bajo `output/`.

## Actividad

1. Responde a mano septiembre ≥ 2000, septiembre ≥ 2001, octubre ≥ 0 y
   noviembre ≥ 2000: pares, conteos y sumas.
2. Prepara Parquet completo y partes propias. Consulta cada representación
   por separado; no leas completo y partes juntos. Comprueba nombres/tipos,
   los pares y el resumen 4500/4600 MXN desde CSV externo.
3. Inspecciona EXPLAIN y EXPLAIN ANALYZE de octubre ≥ 2000. Señala fuente,
   proyecciones, filtros y filas estimadas/observadas. Explica cuál ejecutó
   realmente el SELECT y por qué no demuestra el contenido de cada importe.
4. Ejecuta los cuatro escenarios con parámetros. Conserva una selección vacía
   tipada; distingue agrupar una fuente vacía de sumar globalmente sin filas.
5. Duplica una fila de septiembre en una copia de sus partes. Muestra que la
   consulta directa de octubre todavía devuelve 003/2600, pero la auditoría
   completa rechaza el conjunto. Prueba también omitir una parte.
6. Altera dos saldos de septiembre a 2100/2400 en una copia. Aunque la suma
   siga siendo 4500, demuestra que el verificador compara valores por clave.
7. Reinicia Python o usa otro proceso para verificar los archivos originales.
   Guarda SQL/script, versiones, planes anotados y explicación.

## Resultado esperado

| Escenario | Pares ID/saldo | Registros | Suma MXN |
| --- | --- | ---: | ---: |
| Septiembre ≥ 2000 | 002/2000, 003/2500 | 2 | 4500 |
| Septiembre ≥ 2001 | 003/2500 | 1 | 2500 |
| Octubre ≥ 0 | 001/100, 002/1900, 003/2600 | 3 | 4600 |
| Noviembre ≥ 2000 | Ninguno | 0 | 0 |

Entrada VARCHAR/DATE/INTEGER; selección VARCHAR/INTEGER incluso vacía.
Resumen DATE/BIGINT/HUGEINT: septiembre tres/4500 y octubre tres/4600.
No se exige igualdad literal del plan, estimaciones exactas ni tiempos fijos.
Las métricas del perfil no acreditan I/O físico ni RAM acotada.

<details>
<summary>Solución razonada: ejecución y planes desde una fuente propia</summary>

Desde la raíz, en un script Python nuevo:

```python
from datetime import date
from pathlib import Path
import sys
import duckdb

modulos = Path("curriculum/10_polars_duckdb/06_duckdb_parquet").resolve()
sys.path.insert(0, str(modulos))
import consultas_duckdb as m

carpeta = Path("output/duckdb_1006_lab")
carpeta.mkdir(parents=True, exist_ok=False)
archivos = m.preparar(carpeta / "entrada")
for corte, minimo, pares in [
    (date(2026, 9, 30), 2000, [("002", 2000), ("003", 2500)]),
    (date(2026, 9, 30), 2001, [("003", 2500)]),
    (date(2026, 10, 31), 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    (date(2026, 11, 30), 2000, []),
]:
    completo = m.ejecutar(archivos["completo"], corte=corte, minimo=minimo)
    partes = m.ejecutar(archivos["partes"], corte=corte, minimo=minimo)
    assert completo["seleccion"] == partes["seleccion"] == pares
    assert completo["resumen"] == partes["resumen"]
    assert partes["control"]["saldo_mxn"] == sum(f[1] for f in pares)

entrega = m.ejecutar(archivos["partes"])
for nombre in ["plan", "analisis"]:
    texto = "\n".join(valor for _, valor in entrega[nombre])
    (carpeta / f"{nombre}.txt").write_text(texto, encoding="utf-8")
    print(texto)
```

El verificador audita todas las partes contra CSV antes del filtro, revisa cada
esquema y compara todos los valores. EXPLAIN ANALYZE y el SELECT posterior son
ejecuciones distintas. Los planes guardados no sustituyen la conciliación.

</details>

<details>
<summary>Solución razonada: vacío, duplicados fuera del filtro y saldos compensados</summary>

Continuación; se escriben copias nuevas, no los originales:

```python
fuente_vacia = carpeta / "vacio.csv"
fuente_vacia.write_text("id_credito,fecha_corte,saldo_mxn\n", encoding="utf-8")
vacios = m.preparar(carpeta / "entrada_vacia", fuente_vacia)
assert m.ejecutar(vacios["partes"], fuente_vacia)["resumen"] == []
with duckdb.connect(":memory:") as con:
    assert con.execute("SELECT COUNT(*), SUM(saldo_mxn) FROM read_parquet(?)",
                       [str(vacios["completo"])]).fetchall() == [(0, None)]

error_parte = carpeta / "septiembre_duplicado.parquet"
with duckdb.connect(":memory:") as con:
    con.execute("""COPY (
        SELECT * FROM read_parquet(?)
        UNION ALL
        SELECT * FROM read_parquet(?) LIMIT 4
    ) TO ? (FORMAT PARQUET)""",
    [str(archivos["partes"][0]), str(archivos["partes"][0]), str(error_parte)])
    lista_error = [str(error_parte), str(archivos["partes"][1])]
    sql = (modulos / "seleccion.sql").read_text(encoding="utf-8")
    assert con.execute(sql, [lista_error, date(2026, 10, 31), 2000]).fetchall() == [("003", 2600)]

for lista in [lista_error, [archivos["partes"][1]]]:
    try:
        m.ejecutar(lista)
    except ValueError:
        print("Rechazo esperado: duplicado o parte omitida")
    else:
        raise AssertionError("Debio rechazar el conjunto")

compensada = carpeta / "compensada.parquet"
with duckdb.connect(":memory:") as con:
    con.execute("""COPY (
        SELECT id_credito, fecha_corte,
            CASE WHEN fecha_corte = DATE '2026-09-30' AND id_credito = '002' THEN 2100
                 WHEN fecha_corte = DATE '2026-09-30' AND id_credito = '003' THEN 2400
                 ELSE saldo_mxn END AS saldo_mxn
        FROM read_parquet(?)
    ) TO ? (FORMAT PARQUET)""", [str(archivos["completo"]), str(compensada)])
try:
    m.ejecutar(compensada)
except ValueError:
    print("Rechazo esperado: valores compensados")
else:
    raise AssertionError("Debio rechazar valores distintos")
```

`UNION ALL` conserva repeticiones; limitamos a cuatro filas para fabricar un
lote incorrecto de septiembre. `CASE WHEN ... THEN ... ELSE ... END` fabrica
la copia compensada. Ninguna operación es una regla de limpieza. Los originales
y sus resultados se conservan. Un incidente fuera del filtro puede quedar
oculto al SELECT de octubre; la auditoría tiene otro alcance.

Para verificar en una sesión nueva, con el entorno activo, desde la terminal:

```text
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_lab/entrada/completo.parquet
```

Con uv usa `uv run --locked python -X utf8` en lugar de `python -X utf8`.
El comando no escribe entregas ni modifica bases; sí ejecuta SELECT para el perfil.

</details>

## Evidencia, reflexión y siguiente paso

Conserva script/SQL, versiones, planes anotados, pares/resumen y rechazos esperados.

- ¿Por qué una conexión nueva puede consultar el Parquet sin la tabla original?
- ¿Qué diferencia hay entre `.parquet`, `.duckdb` y una conexión en memoria?
- ¿Por qué describir el esquema no prueba unicidad ni ausencia de NULL?
- ¿Qué representa `~1 row` y qué aporta EXPLAIN ANALYZE?
- ¿Qué no detectaría comprobar solo el saldo de octubre?
- ¿Por qué la auditoría completa no es un benchmark de la consulta selectiva?

Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md).
El proyecto `04_large_credit_dataset` y sus checkpoints siguen pendientes.
Siguiente: [10.07 — DuckDB desde Python y R](../../../curriculum/10_polars_duckdb/07_duckdb_python_r/README.md).
Vuelve a la [lección](../../../curriculum/10_polars_duckdb/06_duckdb_parquet/README.md)
para revisar los conceptos antes de avanzar.

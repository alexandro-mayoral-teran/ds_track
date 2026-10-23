# Lab 10.04 — Conservar tipos, cobertura y cardinalidad

## Propósito y entradas

Practicar la [lección 10.04](../../../curriculum/10_polars_duckdb/04_types_missing_joins/README.md)
sin entregas de capítulos anteriores. Necesitas Python con Polars 2.0.0; el
contraste opcional usa pandas 2.3.3 y SQLite estándar. Usa los
[recorridos](../../../curriculum/10_polars_duckdb/04_types_missing_joins/recorridos.md)
para comprobar el intérprete. Puedes repartir la práctica en varias sesiones.

El [CSV de saldos](../../../curriculum/10_polars_duckdb/04_types_missing_joins/muestra.csv)
contiene exactamente:

| ID textual | Fecha de corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Unidad crédito/corte, clave ID/fecha única. ID de tres dígitos, fechas válidas
1900–2100 y pesos enteros 0–2147483647, sin ausencias. El
[catálogo](../../../curriculum/10_polars_duckdb/04_types_missing_joins/catalogo.csv)
tiene `001/Personal`, `002/ausencia`, `004/Vivienda`: clave ID única, no ausente,
y producto estable en ambos cortes. Solo su campo producto vacío significa
ausencia por contrato. No se imputan valores ni se eliminan duplicados.

## Actividad

1. Predice qué ocurre al convertir los textos `"0"`, `"2.5"`, `"error"`,
   `None` y `"2147483648"` a Int32 con `strict=False`. Conserva originales y
   separa ausencia inicial de conversión fallida. Explica el riesgo de convertir
   un flotante 3.9 a entero incluso con `strict=True`.
2. Para la muestra independiente de mediciones `[10.0, None, NaN, 0.0]`,
   comprueba filas, valores no null, null y NaN. Justifica por qué no son cuatro
   mediciones finitas. Para saldos opcionales `[None, None]`, compara suma del
   motor con una suma presentada solo si existe algún valor conocido.
3. Carga los CSV propios, revisa sus tipos y elabora un left join muchos-a-uno.
   Marca correspondencia antes de unir y distingue etiqueta pendiente de falta
   de catálogo. Comprueba los seis campos por crédito/corte.
4. Compara left/inner/semi/anti. Conserva totales por fecha y explica qué
   población responde cada salida. No llames «saldo total de cartera» a una
   suma de cortes distintos.
5. En una copia, repite `002` del catálogo. Muestra la multiplicación sin
   control y el rechazo con cardinalidad declarada. Repite `004`, que no se
   utiliza: demuestra que el validador completo también lo rechaza.
6. Comprueba fuente vacía con tipos y catálogo vacío por separado. Un catálogo
   vacío conserva seis saldos pero ninguna correspondencia; una fuente vacía
   no inventa observaciones a partir del catálogo.
7. Reinicia Python o usa otro proceso para ejecutar el verificador completo.
   Conserva evidencia en una carpeta nueva bajo `output/`.

## Resultado esperado y comprobación

| Resultado | Septiembre | Octubre |
| --- | ---: | ---: |
| Registros del left join | 3 | 3 |
| Saldo conservado MXN | 4500 | 4600 |
| Coincidencias con catálogo | 2 | 2 |
| Productos conocidos | 1 | 1 |
| Etiquetas pendientes pese a coincidir | 1 | 1 |
| Registros sin catálogo | 1 | 1 |

Left: seis filas; inner/semi: cuatro, saldos por corte 2000/2000 MXN;
anti: dos, 2500/2600 MXN. Los saldos de semi y anti reconstruyen 4500/4600,
sin perder registros ni multiplicarlos. Un duplicado derecho `002` sin control
produce ocho filas y 6500/6500; la unión validada lo rechaza.

La salida enriquecida tiene String/Date/Int32/String/Boolean/Boolean.
Producto puede ser null; saldo y banderas no. El resumen amplía saldo a Int64.
Comparar solo los totales no detecta un producto o bandera equivocados.

<details>
<summary>Solución razonada: conversiones, ausencias y cobertura</summary>

Ejecuta este bloque autónomo en Python:

```python
import math
import polars as pl

textos = pl.DataFrame({"original": ["0", "2.5", "error", None, "2147483648"]},
                      schema={"original": pl.String})
revision = textos.with_columns(
    pl.col("original").cast(pl.Int32, strict=False).alias("valor")
).with_columns(
    (pl.col("original").is_not_null() & pl.col("valor").is_null()).alias("fallo")
)
assert revision["valor"].to_list() == [0, None, None, None, None]
assert revision["fallo"].to_list() == [False, True, True, False, True]
assert pl.Series([3.9]).cast(pl.Int32, strict=True).to_list() == [3]

medidas = pl.DataFrame({"valor": [10.0, None, float("nan"), 0.0]},
                      schema={"valor": pl.Float64})
assert medidas.height == 4
assert medidas["valor"].count() == 3
assert medidas["valor"].null_count() == 1
assert medidas["valor"].is_nan().sum() == 1
assert math.isnan(medidas["valor"].sum())
assert medidas.filter(pl.col("valor").is_finite()).height == 2

opcionales = pl.DataFrame({"saldo": [None, None]}, schema={"saldo": pl.Int32})
control = opcionales.select(
    pl.len().alias("registros"),
    pl.col("saldo").count().alias("conocidos"),
    pl.col("saldo").cast(pl.Int64).sum().alias("suma_motor"),
    pl.when(pl.col("saldo").count() > 0)
    .then(pl.col("saldo").cast(pl.Int64).sum())
    .otherwise(pl.lit(None, dtype=pl.Int64)).alias("suma_observada"),
)
assert control.row(0) == (2, 0, 0, None)
```

La muestra monetaria principal exige saldos completos. Las muestras opcionales
son contratos distintos para estudiar faltantes; no autorizan modificar los
CSV de saldos. Un cero devuelto por sum no prueba que observamos un saldo cero.

</details>

<details>
<summary>Solución razonada: unión, cardinalidad y vacíos</summary>

Desde la raíz del repositorio, en un script nuevo:

```python
from pathlib import Path
import sys
import polars as pl

modulos = Path("curriculum/10_polars_duckdb/04_types_missing_joins").resolve()
sys.path.insert(0, str(modulos))
import semantica_polars as m

saldos = m.cargar_saldos()
catalogo = m.cargar_catalogo()
original = saldos.clone()
unida = m.enriquecer(saldos, catalogo)
m.comprobar_salida(unida)
resumen = m.resumir(unida)
m.comprobar_resumen(resumen)
assert saldos.equals(original)
assert resumen["saldo_mxn"].to_list() == [4500, 4600]
assert resumen["coincidencias"].to_list() == [2, 2]
assert resumen["productos_conocidos"].to_list() == [1, 1]

for modo, filas, totales in [
    ("left", 6, [4500, 4600]), ("inner", 4, [2000, 2000]),
    ("semi", 4, [2000, 2000]), ("anti", 2, [2500, 2600]),
]:
    vista = saldos.join(catalogo, on="id_credito", how=modo)
    assert vista.height == filas
    assert vista.group_by("fecha_corte").agg(
        pl.col("saldo_mxn").cast(pl.Int64).sum()
    ).sort("fecha_corte")["saldo_mxn"].to_list() == totales

for id_repetido in ["002", "004"]:
    duplicado = pl.concat([catalogo, catalogo.filter(pl.col("id_credito") == id_repetido)])
    if id_repetido == "002":
        assert saldos.join(duplicado, on="id_credito", how="left").height == 8
        try:
            saldos.join(duplicado, on="id_credito", how="left", validate="m:1")
        except pl.exceptions.ComputeError:
            print("Rechazo esperado de m:1")
        else:
            raise AssertionError("Debio rechazar duplicado utilizado")
    try:
        m.enriquecer(saldos, duplicado)
    except ValueError:
        print("Catalogo completo rechazado:", id_repetido)
    else:
        raise AssertionError("Debio rechazar incluso clave sin uso")

carpeta = Path("output/semantica_1004_lab")
carpeta.mkdir(parents=True, exist_ok=False)
fuente_vacia = carpeta / "saldos_vacios.csv"
fuente_vacia.write_text("id_credito,fecha_corte,saldo_mxn\n", encoding="utf-8")
catalogo_vacio = carpeta / "catalogo_vacio.csv"
catalogo_vacio.write_text("id_credito,producto\n", encoding="utf-8")
sin_saldos = m.ejecutar(fuente=fuente_vacia)
assert sin_saldos["unida"].shape == (0, 6)
assert sin_saldos["resumen"].shape == (0, 7)
sin_catalogo = m.ejecutar(catalogo=catalogo_vacio)
assert sin_catalogo["unida"].height == 6
assert sin_catalogo["resumen"]["coincidencias"].to_list() == [0, 0]
assert sin_catalogo["resumen"]["saldo_mxn"].to_list() == [4500, 4600]

unida.write_csv(carpeta / "union_revisada.csv")
resumen.write_csv(carpeta / "cobertura.csv")
```

En `002` existe correspondencia, pero su etiqueta es desconocida. En `003` no
hay correspondencia. El verificador mantiene la distinción con dos banderas.
Una columna null no basta para separar esos hechos. La salida vacía conserva
los mismos tipos; no se añaden filas de `004` mediante un left join.

Para contrastar desde una sesión nueva, usa tu entorno activo en la terminal:

```text
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

Con uv, sustituye `python -X utf8` por `uv run --locked python -X utf8`.
El argumento es una extensión: sin él se mantiene la referencia Python estándar.
El comando solo lee y comprueba; no escribe entregas ni modifica bases.

</details>

## Evidencia, reflexión y siguiente paso

Conserva tu script, versiones, diagnósticos, unión, cobertura y explicación
de los rechazos. Explica qué riesgo detecta cada control:

- ¿Por qué strict no garantiza preservar una fracción ni un identificador?
- ¿Qué diferencia hay entre contar filas y valores conocidos?
- ¿Por qué una etiqueta ausente no demuestra falta de correspondencia?
- ¿Por qué m:1 es adecuado aunque el ID se repita en dos cortes?
- ¿Qué cambia al elegir inner? ¿Qué demuestra y qué no demuestra la suma?
- ¿Qué política aplicarías antes de unir claves ausentes entre motores?

Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md).
El proyecto `04_large_credit_dataset` y sus checkpoints siguen pendientes.

Siguiente: [10.05 — Streaming y límites de memoria](../../../curriculum/10_polars_duckdb/README.md#05-streaming-y-limites-de-memoria),
extensión opcional todavía planificada. El siguiente esencial previsto es
[10.06 — DuckDB: SQL sobre Parquet](../../../curriculum/10_polars_duckdb/README.md#06-duckdb-sql-sobre-parquet),
también pendiente. Vuelve a la [lección](../../../curriculum/10_polars_duckdb/04_types_missing_joins/README.md)
si quedan conceptos por explicar.

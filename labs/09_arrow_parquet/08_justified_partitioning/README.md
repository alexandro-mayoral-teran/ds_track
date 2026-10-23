# Lab 09.08 — Particionar según una consulta

## Propósito y entradas

**Extensión opcional.** Practicar [09.08 — Particionamiento justificado](../../../curriculum/09_arrow_parquet/08_justified_partitioning/README.md).
Usa sus entornos locales; no requiere entregas anteriores ni instala paquetes.
Cada lenguaje crea sus propios archivos. Conserva originales y trabaja en
carpetas nuevas. Las soluciones se presentan después de las actividades.

## Actividad 1 — Una muestra completa

La muestra pequeña contiene `101/2026-09-30/0`, `102/2026-09-30/1500`,
`101/2026-10-31/100` y `102/2026-10-31/2000`: ID/fecha/saldo en MXN enteros,
clave ID/fecha y sin ausencias. Reproduce el bloque autónomo de la lección en
Python o R; no necesita CSV, TXT ni funciones del track.

1. Explica por qué hay cuatro observaciones, dos IDs y dos particiones.
2. Inspecciona un Parquet individual y el Dataset abierto con Hive. ¿De dónde
   sale `corte` y dónde se conserva la fecha original?
3. Consulta septiembre con saldo ≥ 0: `101/0`, `102/1500`.
4. Consulta octubre con saldo ≥ 101: solo `102/2000`.
5. Consulta noviembre: cero filas y las columnas ID/saldo conservadas.

<details>
<summary>Una solución razonada para la muestra pequeña</summary>

**Python**, después del bloque autónomo de la lección:

```python
casos = [
    (date(2026, 9, 30), 0, [("101", 0), ("102", 1500)]),
    (date(2026, 10, 31), 101, [("102", 2000)]),
    (date(2026, 11, 30), 0, []),
]
for corte, minimo, esperado in casos:
    filtro = ((ds.field("corte") == corte.isoformat()) &
              (ds.field("fecha_corte") == pa.scalar(corte)) &
              (ds.field("saldo_mxn") >= minimo))
    resultado = dataset.to_table(columns=["id_credito", "saldo_mxn"], filter=filtro)
    observado = sorted((f["id_credito"], f["saldo_mxn"]) for f in resultado.to_pylist())
    assert observado == esperado
    assert resultado.column_names == ["id_credito", "saldo_mxn"]
```

**R**, después de su bloque autónomo:

```r
fechas <- as.Date(c("2026-09-30", "2026-10-31", "2026-11-30"))
minimos <- c(0L, 101L, 0L)
ids <- list(c("101", "102"), "102", character())
saldos <- list(c(0L, 1500L), 2000L, integer())
for (i in seq_along(fechas)) {
  fecha_objetivo <- fechas[i]
  etiqueta <- format(fecha_objetivo, "%Y-%m-%d")
  minimo <- minimos[i]
  consulta <- dataset |>
    dplyr::filter(corte == etiqueta, fecha_corte == fecha_objetivo, saldo_mxn >= minimo) |>
    dplyr::select(id_credito, saldo_mxn)
  resultado <- dplyr::collect(consulta)
  resultado <- resultado[order(resultado$id_credito), ]
  stopifnot(identical(resultado$id_credito, ids[[i]]),
    identical(resultado$saldo_mxn, saldos[[i]]),
    identical(names(resultado), c("id_credito", "saldo_mxn")))
}
```

El cero de septiembre es conocido. La selección de noviembre no contiene
observaciones; no representa un saldo observado de cero para toda la cartera.
`fecha_objetivo` evita confundir un parámetro Date con la columna textual `corte`.

</details>

## Actividad 2 — Misma respuesta, distintas carpetas

Con las funciones y el preparador de la lección, reconstruye la base común
de 28 filas, 14 IDs y 29 000/31 800 MXN. Clave ID/fecha, tres columnas físicas
no anulables `string/date32/int32`. Usa `python_lab/` o `r_lab/` como destino.

1. Crea la comparación plana/particionada y audita ambas completas.
2. Consulta octubre ≥ 2800: cuatro IDs y 12 400 MXN; septiembre ≥ 2000:
   ocho IDs y 20 500 MXN. Compara cada ID/importe con CSV, no solo las sumas.
3. Describe los archivos candidatos por etiqueta para octubre y noviembre.
4. Intenta crear otra vez en el mismo destino: debe rechazarse sin cambiarlo.
5. En otra copia nueva del dataset particionado, duplica un archivo de septiembre.
   La consulta de octubre ≥ 2000 seguirá dando nueve filas/24 100 MXN; la
   auditoría completa debe rechazar el conjunto por claves repetidas.
6. Crea la demostración `por="clave"`: 28 carpetas/archivos de una fila.
   Contrasta con las dos particiones por corte y explica cuál responde a la pregunta.

<details>
<summary>Una solución razonada: consulta, copia alterada y rechazo</summary>

**Python**, desde la raíz de DS Track con su intérprete de estudio:

```python
from pathlib import Path
from datetime import date
import sys
import shutil
sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/08_justified_partitioning").resolve()))
import particiones as curso

compartida = Path("output/09_08_particiones").resolve()
destino = compartida / "python_lab"
print(curso.crear_comparacion(destino))
datos = destino / "por_corte/datos"
dataset = curso.abrir_particionado(datos)
for corte, minimo, filas, saldo in [
    (date(2026, 10, 31), 2800, 4, 12400), (date(2026, 9, 30), 2000, 8, 20500)]:
    resultado = curso.preparar_consulta(dataset, corte, minimo).to_table()
    assert curso.base.comprobar_consulta(resultado, corte, minimo) == {
        "registros": filas, "saldo_mxn": saldo}
print(curso.candidatos(dataset, date(2026, 10, 31)))
assert curso.candidatos(dataset, date(2026, 11, 30)) == []
try:
    curso.crear_comparacion(destino)
except FileExistsError:
    print("Destino conservado")
else:
    raise AssertionError("Se acepto un destino ocupado")

duplicado = compartida / "python_duplicado"
shutil.copytree(datos, duplicado)
septiembre = next((duplicado / "corte=2026-09-30").glob("*.parquet"))
shutil.copy2(septiembre, septiembre.with_name("copia_septiembre.parquet"))
resultado = curso.preparar_consulta(curso.abrir_particionado(duplicado)).to_table()
assert curso.base.comprobar_consulta(resultado) == {"registros": 9, "saldo_mxn": 24100}
try:
    curso.auditar_particionado(duplicado)
except ValueError as error:
    print(error)
else:
    raise AssertionError("La auditoria acepto duplicados")
print(curso.verificar_comparacion(destino))
```

**R**, desde la raíz del proyecto preparado, sin depender de la copia Python:

```r
source("particiones.R", encoding = "UTF-8")
compartida <- readLines("ruta_particiones_0908.txt", encoding = "UTF-8")
destino <- file.path(compartida, "r_lab")
print(crear_comparacion_r(destino))
f <- funciones_particiones()
datos <- file.path(destino, "por_corte/datos")
dataset <- abrir_particionado_r(datos)
fechas <- as.Date(c("2026-10-31", "2026-09-30"))
minimos <- c(2800L, 2000L)
filas <- c(4L, 8L)
saldos <- c(12400, 20500)
for (i in seq_along(fechas)) {
  resultado <- dplyr::collect(preparar_consulta_particion_r(dataset, fechas[i], minimos[i]))
  control <- f$comprobar_consulta_r(resultado, fechas[i], minimos[i])
  stopifnot(control$registros == filas[i], control$saldo_mxn == saldos[i])
}
print(candidatos_por_etiqueta_r(datos))
stopifnot(!length(candidatos_por_etiqueta_r(datos, as.Date("2026-11-30"))))
error <- tryCatch({crear_comparacion_r(destino); NULL}, error = function(e) e)
stopifnot(inherits(error, "error"))

duplicado <- file.path(compartida, "r_duplicado")
if (file.exists(duplicado)) stop("Elige una copia nueva")
stopifnot(dir.create(duplicado))
stopifnot(all(file.copy(list.dirs(datos, full.names = TRUE, recursive = FALSE),
  duplicado, recursive = TRUE)))
septiembre <- list.files(file.path(duplicado, "corte=2026-09-30"),
  pattern = "parquet$", full.names = TRUE)[1]
stopifnot(file.copy(septiembre, file.path(dirname(septiembre), "copia_septiembre.parquet")))
resultado <- dplyr::collect(preparar_consulta_particion_r(abrir_particionado_r(duplicado)))
stopifnot(f$comprobar_consulta_r(resultado)$saldo_mxn == 24100)
error <- tryCatch({auditar_particionado_r(duplicado); NULL}, error = function(e) e)
stopifnot(inherits(error, "error"))
print(conditionMessage(error))
print(verificar_comparacion_r(destino))
```

La copia de septiembre está fuera de la pregunta de octubre. Por eso una
consulta correcta puede coexistir con una fuente incorrecta. Ninguna ruta
deduplica para conseguir igualdad. Los originales se auditan de nuevo.
La demostración de 28 particiones está completa en la sección 8 de la lección;
puedes ejecutarla en otro destino con sufijo `_lab` para conservar lo anterior.

</details>

## Evidencia, comprobación y reflexión

Conserva scripts, árbol de carpetas, inventario, consulta y controles por clave,
rechazo del duplicado y explicación de la decisión. Reinicia cada sesión y
repite solo lectura: carga funciones/rutas, abre datasets, consulta y audita.
No vuelvas a escribir ni copiar carpetas. No publiques salidas personales en
el repositorio del curso.

- ¿Por qué la clave de una fila no es automáticamente una buena partición?
- ¿Qué falta saber para afirmar que se leyó menos o más rápido?
- ¿Qué pasaría si renombraras octubre como noviembre sin cambiar los archivos?
- ¿Por qué `error` al escribir no certifica claves únicas en lo ya guardado?
- ¿Por qué archivos con nombres distintos pueden repetir las mismas filas?
- ¿Qué diferencia hay entre un Parquet vacío con esquema y ninguna fuente?

No hay proyecto/checkpoint implementado asociado. Esta extensión no bloquea
el cierre esencial. Siguiente: [09.09 — Cierre del contrato compartido](../../../curriculum/09_arrow_parquet/README.md#09-cierre-del-contrato-compartido),
todavía planificada. Consulta los [pendientes de cierre](../../../docs/storage-closure.md).

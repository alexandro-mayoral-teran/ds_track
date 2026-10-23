# Lab 09.06 — Consultar una selección y auditar el conjunto

## Propósito y entradas

Practicar [09.06 — Lectura selectiva y datasets](../../../curriculum/09_arrow_parquet/06_selective_datasets/README.md)
con los entornos indicados allí. La primera práctica usa solo los cuatro
registros definidos en esta página y las APIs Arrow, sin CSV ni funciones
previas. La integración posterior usa el preparador de la lección: Python
desde la raíz de DS Track y R desde el proyecto renv, con la misma carpeta
compartida señalada por el TXT local. No necesitas entregas de otros capítulos.

## Primera práctica: una pregunta sobre cuatro filas

Dos créditos ficticios, dos cortes y saldo en pesos enteros:

| id_credito | fecha_corte | saldo_mxn |
| --- | --- | ---: |
| 101 | 2026-09-30 | 0 |
| 102 | 2026-09-30 | 1500 |
| 101 | 2026-10-31 | 100 |
| 102 | 2026-10-31 | 2000 |

Reproduce el bloque autónomo Python o R de la lección: crea estos datos y
dos archivos en una carpeta nueva. No requiere completar la otra ruta.
Después trabaja solo sobre esos archivos:

1. Consulta octubre con saldo ≥ 100. Antes de ejecutar, escribe qué IDs esperas.
2. Conserva ID y saldo: deben aparecer `101/100` y `102/2000`, suma 2100.
3. Cambia el umbral a 101: debe quedar solo `102/2000`.
4. Consulta septiembre con umbral cero: `101/0` y `102/1500`. Explica el cero.
5. Consulta noviembre con umbral cero: cero filas, dos columnas conservadas.
6. Reinicia la sesión y repite solo lectura. Identifica la línea que materializa.

<details>
<summary>Una solución razonada para la muestra pequeña</summary>

Después del bloque autónomo de creación de la lección, **Python**:

```python
casos = [
    (date(2026, 10, 31), 100, [("101", 100), ("102", 2000)]),
    (date(2026, 10, 31), 101, [("102", 2000)]),
    (date(2026, 9, 30), 0, [("101", 0), ("102", 1500)]),
    (date(2026, 11, 30), 0, []),
]
for corte, minimo, esperado in casos:
    filtro = ((ds.field("fecha_corte") == pa.scalar(corte)) &
              (ds.field("saldo_mxn") >= minimo))
    plan = dataset_mini.scanner(columns=["id_credito", "saldo_mxn"], filter=filtro)
    resultado = plan.to_table()  # Aquí reunimos el resultado en memoria.
    assert resultado.column_names == ["id_credito", "saldo_mxn"]
    observado = sorted((f["id_credito"], f["saldo_mxn"]) for f in resultado.to_pylist())
    assert observado == esperado
    print(corte, minimo, observado, sum(saldo for _, saldo in observado))
```

**R**, después de crear su propia muestra autónoma:

```r
cortes <- as.Date(c("2026-10-31", "2026-10-31", "2026-09-30", "2026-11-30"))
minimos <- c(100L, 101L, 0L, 0L)
ids <- list(c("101", "102"), "102", c("101", "102"), character())
saldos <- list(c(100L, 2000L), 2000L, c(0L, 1500L), integer())
for (i in seq_along(cortes)) {
  corte <- cortes[i]
  minimo <- minimos[i]
  plan <- dataset_mini |>
    dplyr::filter(fecha_corte == corte, saldo_mxn >= minimo) |>
    dplyr::select(id_credito, saldo_mxn)
  resultado <- dplyr::collect(plan)  # Aquí materializamos como tibble.
  resultado <- resultado[order(resultado$id_credito), ]
  stopifnot(identical(names(resultado), c("id_credito", "saldo_mxn")),
    identical(resultado$id_credito, ids[[i]]),
    identical(resultado$saldo_mxn, saldos[[i]]))
  print(resultado)
}
```

Se compara cada par ID/importe y se conserva la forma incluso sin filas.
El cero de septiembre pertenece a una observación existente; la selección
vacía de noviembre no describe un saldo observado de ese corte.
Para reiniciar, vuelve a importar las bibliotecas Python o carga el proyecto R,
define `carpeta_mini` con su ruta existente y abre `dataset_mini` como indica
la lección. No necesitas conservar `mini` en memoria ni volver a escribirlo.

</details>

## Integración: consulta y auditoría sobre la base común

Entrada reconstruida desde CSV: 28 filas, 14 créditos, dos cortes de 14 registros
con 29 000/31 800 MXN. Clave ID/fecha, esquema no anulable `string/date32/int32`;
saldo en pesos enteros no negativos. Se escriben dos partes de 14 filas en
`datos/`, sin particiones ni dependencias nuevas.

### Actividad

1. Crea un dataset nuevo en `python_lab/` y otro desde R en `r_lab/`.
2. Expresa las consultas antes de materializarlas y devuelve solo ID y saldo:
   octubre con saldo ≥ 2800; septiembre con saldo ≥ 2000; noviembre con saldo ≥ 0.
3. Compara cada ID/importe con la referencia CSV y explica estos resultados:
   cuatro filas/12 400 MXN; ocho/20 500; cero/0 en la selección vacía.
4. En cada lenguaje, copia su carpeta `datos/` en `duplicado_python/` o
   `duplicado_r/` y copia de nuevo su parte de septiembre dentro de ella.
   Conserva los originales; cada ruta puede ejecutarse por separado.
5. Consulta octubre con saldo ≥ 2000 en esa copia: debe seguir dando nueve
   filas y 24 100 MXN. Después ejecuta la auditoría completa en ambos lenguajes:
   debe rechazar el dataset. Explica por qué ambos resultados son coherentes.

Extensión opcional: cambia el umbral de octubre de 2800 a 2801. La fila de
2800 debe salir: quedan tres registros y 9600 MXN. La condición es inclusiva.

## Resultado y comprobación

- Plan de consulta y resultado materializado identificados por separado.
- Tres selecciones completas por clave, incluidas frontera y selección vacía.
- Dataset alterado rechazado por ambos auditores, aunque una consulta siga correcta.
- Entradas y carpetas originales intactas; lectura repetida tras reiniciar sesiones.

<details>
<summary>Una solución razonada</summary>

**Python**, en la raíz del repositorio y con el intérprete de estudio:

```python
from datetime import date
from pathlib import Path
import shutil
import sys
import pyarrow.parquet as pq

sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/06_selective_datasets").resolve()))
import consultas_dataset as curso

compartida = Path("output/09_06_datasets").resolve()
curso.crear_dataset(compartida / "python_lab")
datos = compartida / "python_lab/datos"
dataset = curso.abrir_dataset(datos)
casos = [
    (date(2026, 10, 31), 2800, 4, 12400),
    (date(2026, 9, 30), 2000, 8, 20500),
    (date(2026, 11, 30), 0, 0, 0),
]
for corte, minimo, filas, saldo in casos:
    plan = curso.preparar_consulta(dataset, corte, minimo)
    resultado = plan.to_table()
    control = curso.comprobar_consulta(resultado, corte, minimo)
    assert control == {"registros": filas, "saldo_mxn": saldo}
    print(corte, control)

duplicado = compartida / "duplicado_python"
shutil.copytree(datos, duplicado)
septiembre = pq.ParquetFile(datos / "parte_001.parquet").read()
assert set(septiembre["fecha_corte"].to_pylist()) == {date(2026, 9, 30)}
shutil.copy2(datos / "parte_001.parquet", duplicado / "copia_septiembre.parquet")
seleccion = curso.preparar_consulta(curso.abrir_dataset(duplicado)).to_table()
assert curso.comprobar_consulta(seleccion) == {"registros": 9, "saldo_mxn": 24100}
try:
    curso.verificar_dataset(duplicado)
except ValueError as error:
    print(error)
else:
    raise AssertionError("La auditoría aceptó registros repetidos")
```

El filtro de octubre no incluye ninguna de las filas añadidas de septiembre.
Por eso la selección coincide, pero el dataset completo contiene claves repetidas.
El auditor no deduplica ni elimina la copia para conseguir igualdad: la rechaza.

**R**, desde una sesión nueva en la raíz del proyecto de práctica:

```r
source("consultas_dataset.R", encoding = "UTF-8")
compartida <- readLines("ruta_dataset_0906.txt", encoding = "UTF-8")
crear_dataset_r(file.path(compartida, "r_lab"))
dataset <- abrir_dataset_r(file.path(compartida, "r_lab/datos"))
cortes <- as.Date(c("2026-10-31", "2026-09-30", "2026-11-30"))
minimos <- c(2800L, 2000L, 0L)
filas <- c(4L, 8L, 0L)
saldos <- c(12400, 20500, 0)
for (i in seq_along(cortes)) {
  plan <- preparar_consulta_r(dataset, cortes[i], minimos[i])
  resultado <- dplyr::collect(plan)
  control <- comprobar_consulta_r(resultado, cortes[i], minimos[i])
  stopifnot(control$registros == filas[i], control$saldo_mxn == saldos[i])
  print(control)
}

# R crea su propia copia; no depende de que hayas ejecutado Python.
datos <- file.path(compartida, "r_lab/datos")
duplicado <- file.path(compartida, "duplicado_r")
if (file.exists(duplicado)) stop("Elige una carpeta nueva")
stopifnot(dir.create(duplicado))
stopifnot(all(file.copy(list.files(datos, full.names = TRUE), duplicado)))
septiembre <- arrow::read_parquet(file.path(datos, "parte_001.parquet"))
stopifnot(all(septiembre$fecha_corte == as.Date("2026-09-30")))
stopifnot(file.copy(file.path(datos, "parte_001.parquet"),
  file.path(duplicado, "copia_septiembre.parquet")))
seleccion <- dplyr::collect(preparar_consulta_r(abrir_dataset_r(duplicado)))
stopifnot(comprobar_consulta_r(seleccion)$saldo_mxn == 24100)
error <- tryCatch({
  verificar_dataset_r(duplicado)
  NULL
}, error = function(e) e)
stopifnot(inherits(error, "error"))
print(conditionMessage(error))
print(verificar_dataset_r(file.path(compartida, "r_lab/datos")))
```

R usa su referencia reconstruida desde CSV y comprueba que su carpeta original
sigue válida. Cada ruta crea sus propias copias; como contraste adicional,
puedes abrir desde R la carpeta Python si ejecutaste ambas. `tryCatch()` y `try/except` permiten
inspeccionar el rechazo esperado; el recorrido falla si la auditoría lo acepta.

Al reiniciar, vuelve a importar/cargar las funciones, abre la carpeta existente
y prepara la consulta. **Omite crear y copiar carpetas**: son acciones de la
preparación, no parte de una verificación de solo lectura.

</details>

## Evidencia y reflexión

Conserva scripts, versiones, parámetros de consulta, selecciones comprobadas y
el mensaje del auditor. Registra qué operación materializó el resultado y por
qué no puedes inferir los bytes leídos a partir de su tamaño.

- ¿Qué columna necesita el filtro aunque no aparezca en la proyección?
- ¿Por qué una selección vacía no afirma que todo noviembre tenga saldo cero?
- ¿Qué parte del dataset quedó fuera de la consulta que parecía correcta?
- ¿Por qué la auditoría completa de este ejemplo no prueba ahorro de RAM?
- ¿Qué ocurriría si reunieras todos los lotes en una lista?

No hay proyecto/checkpoint implementado asociado. Después de comprobar y
explicar, continúa con [09.07 — Metadatos, row groups y compresión](../../../curriculum/09_arrow_parquet/README.md#07-metadatos-row-groups-y-compresion),
todavía planificada. Consulta los [pendientes de cierre](../../../docs/storage-closure.md).

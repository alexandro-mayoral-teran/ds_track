# Lab 09.07 — Explicar una decisión de almacenamiento

## Propósito y entradas

Practicar [09.07 — Metadatos, row groups y compresión](../../../curriculum/09_arrow_parquet/07_metadata_compression/README.md).
Usa sus entornos locales; no instala bibliotecas ni requiere entregas de otros
capítulos. Python y R pueden crear su práctica por separado. El detalle de
estadísticas/codificaciones se inspecciona con PyArrow; la interfaz R 25.0.1
permite consultar esquema y conteos y decodificar grupos.

Primero trabaja con cuatro filas definidas aquí: `101/2026-09-30/0`,
`102/2026-09-30/1500`, `101/2026-10-31/100`, `102/2026-10-31/2000`.
Cada triple es ID/fecha/saldo en pesos enteros; clave ID + fecha, sin ausencias.
El bloque autónomo completo de cada lenguaje está en la lección. No necesita
un CSV, un TXT ni funciones de capítulos previos.

## Actividad 1 — Cambiar los grupos conservando la tabla

1. Crea la muestra pequeña y su archivo de dos grupos como indica la lección.
2. Escribe **otro archivo** con cuatro filas por grupo, mismos tipos y valores,
   sin compresión ni diccionario y con estadísticas activadas.
3. Antes de inspeccionar, predice cuántos grupos tendrá cada archivo.
4. Compara todos los valores tras la relectura, no solo la suma.
5. Inspecciona las fechas mínima/máxima de cada grupo con PyArrow. Para buscar
   octubre, ¿qué grupo puede descartarse en el archivo de dos grupos? ¿Y en
   el de uno solo? Explica sin afirmar bytes físicamente leídos.

Resultado: dos grupos frente a uno; los dos archivos contienen las mismas
cuatro observaciones. El grupo de septiembre puede descartarse por fecha en
la primera disposición. El único grupo de la segunda sigue siendo candidato.

<details>
<summary>Una solución razonada: grupos y valores</summary>

**Python**, después del bloque autónomo de la lección:

```python
ruta4 = carpeta / "mini_grupo4.parquet"
with ruta4.open("xb") as archivo:
    pq.write_table(tabla, archivo, version="2.6", row_group_size=4,
                   compression="NONE", use_dictionary=False, write_statistics=True)
with pq.ParquetFile(ruta4) as lector4:
    assert lector4.metadata.num_row_groups == 1
    assert lector4.schema_arrow.equals(esquema, check_metadata=False)
    assert lector4.read().equals(tabla)

for archivo in (ruta, ruta4):
    with pq.ParquetFile(archivo) as lector:
        for i in range(lector.metadata.num_row_groups):
            estadisticas = lector.metadata.row_group(i).column(1).statistics
            assert estadisticas is not None and estadisticas.has_min_max
            print(archivo.name, i, estadisticas.min, estadisticas.max)
```

**R**, después de su bloque autónomo:

```r
ruta4 <- file.path(carpeta, "mini_grupo4.parquet")
if (file.exists(ruta4)) stop("Conserva el archivo existente")
arrow::write_parquet(tabla, ruta4, version = "2.6", chunk_size = 4L,
  compression = "uncompressed", use_dictionary = FALSE, write_statistics = TRUE)
lector4 <- arrow::ParquetFileReader$create(ruta4, mmap = FALSE)
stopifnot(lector4$num_row_groups == 1,
  lector4$GetSchema()$Equals(esquema, check_metadata = FALSE),
  identical(as.data.frame(lector4$ReadTable()), x))
lector4 <- NULL
```

En Python, los extremos de fecha son septiembre/septiembre y octubre/octubre
en los dos grupos. En el grupo único, son septiembre/octubre. Para ver los
metadatos del archivo escrito por R, abre su ruta real con `pq.ParquetFile()`
desde Python y usa el mismo bucle de inspección; no hace falta reescribirlo.
En R no calcules los extremos leyendo grupos para presentarlos como lectura
de estadísticas: sería decodificar valores.

</details>

## Actividad 2 — Estadísticas ausentes

Conservando la muestra pequeña, escribe un tercer archivo sin estadísticas,
dos filas por grupo y las demás opciones iguales. Comprueba que puede releerse
y que conserva los valores. Desde Python observa `statistics` de sus bloques.

Resultado: el archivo sigue siendo válido; que no haya estadísticas no
significa saldo cero ni ausencia de filas. No utilices sus extremos sin
comprobar disponibilidad.

<details>
<summary>Una solución razonada: escribir y comprobar la ausencia</summary>

**Python**:

```python
sin_stats = carpeta / "sin_estadisticas.parquet"
with sin_stats.open("xb") as archivo:
    pq.write_table(tabla, archivo, version="2.6", row_group_size=2,
                   compression="NONE", use_dictionary=False, write_statistics=False)
with pq.ParquetFile(sin_stats) as lector:
    assert lector.read().equals(tabla)
    for i in range(lector.metadata.num_row_groups):
        for j in range(lector.metadata.num_columns):
            assert lector.metadata.row_group(i).column(j).statistics is None
```

**R**:

```r
sin_stats <- file.path(carpeta, "sin_estadisticas.parquet")
if (file.exists(sin_stats)) stop("Conserva el archivo existente")
arrow::write_parquet(tabla, sin_stats, version = "2.6", chunk_size = 2L,
  compression = "uncompressed", use_dictionary = FALSE, write_statistics = FALSE)
stopifnot(identical(as.data.frame(arrow::read_parquet(sin_stats,
  as_data_frame = FALSE)), x))
```

El bucle Python puede inspeccionar también este archivo R. Desactivar
estadísticas no convierte los valores en nulos ni elimina columnas.

</details>

## Actividad 3 — Tamaño y tiempo con equivalencia comprobada

Prepara la base común con las funciones y el preparador de la lección. Entrada
incluida: 28 filas, 14 IDs, tres columnas `string/date32/int32` no anulables,
14 observaciones por corte y 29 000/31 800 MXN. Usa carpetas nuevas
`python_lab/` y `r_lab/`, nunca las entregas originales.

1. Ejecuta las cuatro variantes y tres repeticiones con los scripts incluidos.
2. Conserva tiempos crudos, orden, bytes, parámetros y versiones.
3. Compara base/Snappy y base/diccionario. Identifica qué cambia y qué queda fijo.
4. Comprueba dos grupos en base y cuatro en grupos7; los valores deben coincidir
   por ID/fecha en todos los archivos, no solo en uno de cada variante.
5. Examina códec/codificaciones reales de un archivo de cada variante usando
   PyArrow. Incluye también los cuatro escritos por R si sigues ambos recorridos.
6. Reinicia las sesiones y utiliza los verificadores de solo lectura.
7. Redacta una decisión de cuatro o cinco frases: equivalencia comprobada,
   observaciones de tamaño/tiempo, límites y qué medirías con una base mayor.

<details>
<summary>Una solución razonada: experimento y contraste</summary>

**Python**, desde la raíz de DS Track con el intérprete elegido:

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/07_metadata_compression").resolve()))
import metadatos_parquet as curso

compartida = Path("output/09_07_metadatos").resolve()
medidas = curso.crear_experimento(compartida / "python_lab")
assert len(medidas) == 12
print(curso.verificar_experimento(compartida / "python_lab"))
for nombre in curso.CONFIGURACIONES:
    detalle = curso.inspeccionar(compartida / "python_lab" / f"{nombre}_01.parquet")
    assert detalle["filas"] == 28
    assert detalle["grupos"] == (4 if nombre == "grupos7" else 2)
    print(nombre, detalle["bytes_archivo"])
    print([(c["columna"], c["codec"], c["codificaciones"]) for c in detalle["columnas"]])
```

**R**, desde la raíz del proyecto preparado, sin necesitar la carpeta Python:

```r
source("metadatos_parquet.R", encoding = "UTF-8")
compartida <- readLines("ruta_metadatos_0907.txt", encoding = "UTF-8")
medidas <- crear_experimento_r(file.path(compartida, "r_lab"))
stopifnot(nrow(medidas) == 12L)
print(verificar_experimento_r(file.path(compartida, "r_lab")))
for (nombre in configuraciones_metadatos()$configuracion) {
  detalle <- inspeccionar_metadatos_r(file.path(compartida, "r_lab",
    sprintf("%s_01.parquet", nombre)))
  stopifnot(detalle$filas == 28, detalle$grupos == if (nombre == "grupos7") 4 else 2)
  print(detalle)
}
```

El resumen debe conservar ambos cortes y los saldos conocidos. Para el
contraste detallado de cada archivo R, desde Python:

```python
for nombre in curso.CONFIGURACIONES:
    ruta_r = compartida / "r_lab" / f"{nombre}_01.parquet"
    print(curso.inspeccionar(ruta_r)["columnas"])
    print(curso.cartera.verificar_parquet(ruta_r))
```

Adapta `compartida` a la ruta que contiene el TXT R si es distinta.
Los tiempos reales de cada persona son parte de su evidencia; no existe un
ganador obligatorio. Un diccionario puede añadir costo en una muestra pequeña.
Una mediana R de cero puede reflejar la resolución del reloj. Ninguna de esas
observaciones permite concluir cómo se comportarán millones de registros.

Tras reiniciar, carga funciones y rutas y ejecuta **solo** los verificadores.
No repitas creación ni escritura: una ruta ocupada se conserva para revisión.

</details>

## Evidencia, comprobación y reflexión

Conserva scripts, archivos pequeños, mediciones crudas, notas del entorno y
una tabla comparativa. No versionas tus salidas de práctica en el repositorio
del curso. Registra tu evidencia y dudas en el mecanismo de estudio acordado.

- ¿Cuántos bloques de columna hay en dos grupos de tres columnas?
- ¿Por qué `INT32` no basta para distinguir fecha y saldo?
- ¿Puede un grupo con mínimo 100 y máximo 2000 no contener 1500?
- ¿Por qué usar diccionario con `UNCOMPRESSED` es coherente?
- ¿Qué dos factores cambian si comparas directamente Snappy con grupos7?
- ¿Qué quedó fuera de los intervalos medidos? ¿Por qué guardar el orden?
- ¿Por qué los bytes sin comprimir del bloque no son la RAM del proceso?
- ¿Qué demuestra la relectura y qué no puede autenticar de los tiempos pasados?

No hay proyecto/checkpoint implementado asociado. Después de comprobar y
explicar, continúa con [09.08 — Particionamiento justificado](../../../curriculum/09_arrow_parquet/08_justified_partitioning/README.md),
extensión disponible, o con el cierre esencial
[09.09](../../../curriculum/09_arrow_parquet/README.md#09-cierre-del-contrato-compartido),
también pendiente. Consulta los [pendientes de almacenamiento](../../../docs/storage-closure.md).

# 09 — Arrow y Parquet

## Propósito y prerrequisitos

Guardar, leer e intercambiar tablas entre Python y R con un contrato explícito.
Completa [08 — Visualización en R](../08_visualization_r/README.md) y reutiliza
los datos e indicadores conocidos del análisis anterior.

**Estado:** [09.01](01_csv_parquet_arrow/README.md) dispone de lección, scripts
de inspección, muestra CSV/Parquet y lab. [09.02](02_schemas_types/README.md)
añade contrato, evaluadores Python/R, casos de frontera y lab.
[09.03](03_python_read_write/README.md) incorpora PyArrow, conversión/relectura
Python, recorridos de entorno y lab. [09.04](04_r_read_write/README.md) añade
arrow en renv, ejemplos completos y escritura/relectura R con lab.
[09.05](05_python_r_exchange/README.md) añade intercambio en ambas direcciones,
muestra independiente y lab sin dependencias nuevas. [09.06](06_selective_datasets/README.md)
añade consultas sobre varios Parquet y auditoría separada con lab.
[09.07](07_metadata_compression/README.md) añade metadatos, grupos y comparación
controlada de compresión/codificación con lab, sin paquetes nuevos.
09.08–09.09 siguen planificadas; sus
enlaces internos describen el alcance. El [estado y pendientes de cierre](../../docs/storage-closure.md)
distingue material, práctica del estudiante e integración todavía pendiente.

El módulo es un puente entre lenguajes. La teoría se explica una vez; las prácticas
Python y R se presentan en apartados completos, seguidos de una comparación.
No se exige reticulate ni ejecutar ambos intérpretes en un mismo proceso.

## Qué problema resuelve cada componente

| Componente | Papel en el recorrido |
| --- | --- |
| CSV | Texto de intercambio sencillo; interpretar tipos forma parte de la lectura |
| Parquet | Formato de archivo columnar con esquema y opciones de compresión |
| Arrow | Representación columnar en memoria y bibliotecas para trabajar e intercambiar datos |
| PyArrow / arrow de R | Interfaces utilizadas en las prácticas Python y R |

Parquet y Arrow no son sinónimos. Un archivo Parquet puede leerse con distintos
motores; eso no garantiza que todos expongan idénticas clases o admitan todas
las características del formato. Conservaremos un contrato de tipos y unidades.
Arrow IPC/Feather y el intercambio en memoria serán ampliaciones, no requisitos.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [CSV, Parquet y Arrow](01_csv_parquet_arrow/README.md) | Esencial | Distinguir archivo, representación y biblioteca |
| 2 | [Esquemas y tipos entre lenguajes](02_schemas_types/README.md) | Esencial | Definir el contrato de una tabla compartida |
| 3 | [Leer y escribir desde Python](03_python_read_write/README.md) | Esencial | Convertir una muestra y comprobar su lectura |
| 4 | [Leer y escribir desde R](04_r_read_write/README.md) | Esencial | Repetir el recorrido con el mismo contrato |
| 5 | [Intercambio Python y R](05_python_r_exchange/README.md) | Práctica | Conciliar archivos escritos por el otro lenguaje |
| 6 | [Lectura selectiva y datasets](06_selective_datasets/README.md) | Esencial | Consultar columnas y filas de varios archivos |
| 7 | [Metadatos, row groups y compresión](07_metadata_compression/README.md) | Práctica | Explicar y medir una decisión de almacenamiento |
| 8 | [Particionamiento justificado](#08-particionamiento-justificado) | Extensión | Elegir particiones según una consulta y comprobarlas |
| 9 | [Cierre del contrato compartido](#09-cierre-del-contrato-compartido) | Práctica de cierre | Reconstruir datos e indicadores desde ambos lenguajes |

## Alcance de cada sección

<a id="01-csv-parquet-y-arrow"></a>

### 01 — CSV, Parquet y Arrow

- Texto frente a formato binario; filas, columnas, esquema, archivo y dataset.
  Diferenciar tamaño en disco de memoria utilizada después de leer.
- Disponible: [lección, scripts y muestra](01_csv_parquet_arrow/README.md) y
  [lab 09.01](../../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md).
  CSV/Parquet reales de 28 observaciones, 14 IDs y 29000/31800 MXN; tamaños y
  límites de inspección. Esencial con Python estándar/R base; lectura real
  PyArrow como evidencia y ampliación opcional, sin dependencias nuevas.
  Teoría de filas/columnas, lectura lógica/física, codificación frente a compresión
  y papel de Arrow en memoria; decisiones de uso sin anticipar benchmarks.

<a id="02-esquemas-y-tipos-entre-lenguajes"></a>

### 02 — Esquemas y tipos entre lenguajes

- Nombres, claves, tipos y nulabilidad; enteros, texto, fechas, marcas de tiempo,
  decimales y categorías. Distinguir esquema de reglas de negocio.
- Disponible: [lección, evaluadores y casos](02_schemas_types/README.md) y
  [lab 09.02](../../labs/09_arrow_parquet/02_schemas_types/README.md). Contrato de
  la base conocida y 23 casos separados; ausencia/vacío/cero, calendario, rango,
  precisión, centavos, timestamps y categorías. Python estándar/R base, sin
  instalar paquetes ni decodificar Parquet. Los factores de R y categorías de
  pandas requieren comprobación, no una equivalencia asumida.

<a id="03-leer-y-escribir-desde-python"></a>

### 03 — Leer y escribir desde Python

- pandas y PyArrow: convertir a una tabla Arrow, inspeccionar esquema y escribir
  Parquet. Leer de nuevo y decidir explícitamente el tratamiento del índice pandas.
- Disponible: [lección, módulo reutilizable y recorridos](03_python_read_write/README.md)
  y [lab 09.03](../../labs/09_arrow_parquet/03_python_read_write/README.md).
  PyArrow 21.0.0 declarado con lockfile real, pandas 2.3.3 conservado;
  esquema no anulable, índice omitido y comparación de todos los valores por
  clave tras relectura. Carpeta nueva y verificador de solo lectura; mismos
  28 registros y 29000/31800 MXN, sin modificar fuentes ni dependencias R.

<a id="04-leer-y-escribir-desde-r"></a>

### 04 — Leer y escribir desde R

- arrow::read_parquet/write_parquet; tabla en memoria frente a objeto Arrow.
  Revisar cómo se representan los tipos del contrato al entrar y salir de R.
- Disponible: [lección, funciones y preparador](04_r_read_write/README.md) y
  [lab 09.04](../../labs/09_arrow_parquet/04_r_read_write/README.md). Ejemplo
  pequeño completo y base común de 28 registros; esquema real no anulable y
  comparación por clave. Arrow 25.0.1/assertthat 0.2.1 en el mismo proyecto renv,
  respaldo 08.09 y restauración desde biblioteca vacía; registros anteriores
  conservados. No exige una entrega personal de Python ni reconstruir 07–08.

<a id="05-intercambio-python-y-r"></a>

### 05 — Intercambio Python y R

- Escribir en Python y leer en R; después escribir en R y leer en Python.
  Comparar datos por claves acordadas, no por orden accidental ni igualdad de bytes.
- Disponible: [lección, funciones y preparador](05_python_r_exchange/README.md) y
  [lab 09.05](../../labs/09_arrow_parquet/05_python_r_exchange/README.md). Base común
  conciliada en ambas direcciones y muestra de tres filas con acentos, vacío,
  ausencia y cero bajo otro contrato. Sesiones nuevas, tipos/nulabilidad y
  valores por clave; no exige entregas anteriores ni añade dependencias.

<a id="06-lectura-selectiva-y-datasets"></a>

### 06 — Lectura selectiva y datasets

- Proyección de columnas y filtros; Dataset/Scanner en Python y open_dataset con
  consultas dplyr en R. Diferenciar preparar una consulta de materializar resultados.
- Disponible: [lección, funciones y preparador](06_selective_datasets/README.md) y
  [lab 09.06](../../labs/09_arrow_parquet/06_selective_datasets/README.md). Ejemplo
  pequeño completo y base común en dos partes; esquemas de todos los archivos,
  auditoría completa separada y selección por clave desde CSV independiente.
  Octubre ≥ 2000: nueve registros y 24100 MXN. No acredita bytes omitidos,
  rendimiento ni RAM acotada; conserva fuentes/lockfiles sin paquetes nuevos.

<a id="07-metadatos-row-groups-y-compresion"></a>

### 07 — Metadatos, row groups y compresión

- Row groups, columnas, estadísticas y códecs; distinguir compresión de codificación
  y de particionamiento. Leer metadatos antes de modificar parámetros.
- Disponible: [lección, funciones y preparador](07_metadata_compression/README.md) y
  [lab 09.07](../../labs/09_arrow_parquet/07_metadata_compression/README.md).
  Ejemplos autónomos de cuatro filas y comparación de cuatro variantes de la
  base común, una modificación por comparación y tres repeticiones crudas.
  Esquema/valores por clave conservados, conteos/metadatos reales y tiempos
  separados de la validación. R expone esquema/conteos y lectura de grupos;
  PyArrow inspecciona también estadísticas/codificaciones de los archivos R.
  No acredita rendimiento general, I/O físico ni RAM; sin paquetes nuevos.

<a id="08-particionamiento-justificado"></a>

### 08 — Particionamiento justificado

- Carpetas por corte u otra clave de consulta, descubrimiento y pruning.
  Diferenciar particiones de archivos y row groups; evitar particiones excesivas.
- Práctica prevista: comparar una consulta de un corte con y sin particiones,
  revisar archivos generados y evitar duplicados al repetir una escritura.
  Evolución de esquemas y compactación quedan como profundización posterior.

<a id="09-cierre-del-contrato-compartido"></a>

### 09 — Cierre del contrato compartido

- Integrar conversión, lectura cruzada y consulta selectiva con reglas documentadas.
- Práctica prevista: reconstruir el Parquet y demostrar desde Python y R que
  conserva registros e indicadores. Particionar no es requisito del cierre esencial.

## Prácticas, proyecto y criterio de salida

Están disponibles los [labs 09.01](../../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md),
[09.02](../../labs/09_arrow_parquet/02_schemas_types/README.md),
[09.03](../../labs/09_arrow_parquet/03_python_read_write/README.md),
[09.04](../../labs/09_arrow_parquet/04_r_read_write/README.md),
[09.05](../../labs/09_arrow_parquet/05_python_r_exchange/README.md),
[09.06](../../labs/09_arrow_parquet/06_selective_datasets/README.md) y
[09.07](../../labs/09_arrow_parquet/07_metadata_compression/README.md).
09.08–09.09 siguen previstos, con 09.08 opcional. No se da el módulo por completo.
El cierre enlazará el análisis R con el proyecto previsto 04_large_credit_dataset,
registrado en [proyectos](../../projects/README.md), aún sin carpeta implementada.

Checkpoint de almacenamiento propuesto: CSV tipado, Parquet, contrato y comparación
Python/R (02–05 y 09). El checkpoint de lectura selectiva prepara el módulo 10
(06–07); particionamiento se añade solo con una pregunta que lo justifique.
Sus nombres se concretarán al desarrollar el proyecto.

Para avanzar, demuestra lectura y escritura en ambos lenguajes, explica el contrato
y concilia el resultado. Un esquema válido no comprueba claves únicas o cantidades
válidas por sí solo. Datasets distribuidos, almacenamiento en nube, Flight y
formatos de tablas con transacciones no son requisitos de este módulo.

## Continuidad y fuentes

Continúa con [10 — Polars y DuckDB](../10_polars_duckdb/README.md), reutilizando
los mismos archivos. Se conserva la numeración del track; R aplicado sigue pendiente.

- [Parquet: visión general](https://parquet.apache.org/docs/overview/) y
  [estructura del archivo](https://parquet.apache.org/docs/file-format/).
- [Parquet con PyArrow](https://arrow.apache.org/docs/python/parquet.html) y
  [datasets en Python](https://arrow.apache.org/docs/python/dataset.html).
- [Lectura/escritura en R](https://arrow.apache.org/docs/r/articles/read_write.html) y
  [datasets en R](https://arrow.apache.org/docs/r/articles/dataset.html).
- [Arrow en R for Data Science](https://r4ds.hadley.nz/arrow.html), como lectura abierta de apoyo.

09.01–09.02 se comprobaron con Python 3.12.12/R 4.6.1; la muestra y lectura de autoría de 09.01
utilizan PyArrow 21.0.0 ya existente, sin añadirlo durante esa introducción.
09.03 declara PyArrow 21.0.0 y conserva pandas 2.3.3; instalación y segunda
reconstrucción uv local con Python 3.12.12 comprobadas, sin cambios globales.
09.04 se comprueba con R 4.6.1/arrow 25.0.1 y renv 1.3.1, con segunda restauración
local; conserva 44 registros anteriores y añade arrow/assertthat.
09.05 comprueba ambas direcciones con esas versiones, conservando entornos,
fuentes y lockfiles; no incorpora dependencias.
09.06 usa las mismas versiones, con dplyr 1.2.1 en R; no modifica requisitos
ni lockfiles. Consultas y auditoría comprobadas desde procesos nuevos.
Versiones y capacidades de los recorridos por desarrollar se comprobarán al
implementarlos. Esta planificación no instala paquetes.
09.07 conserva esas versiones y lockfiles; compara archivos completos con
PyArrow 21.0.0/arrow 25.0.1, con sesiones nuevas y mediciones crudas locales.

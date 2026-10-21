# 09 — Arrow y Parquet

## Propósito y prerrequisitos

Guardar, leer e intercambiar tablas entre Python y R con un contrato explícito.
Completa [08 — Visualización en R](../08_visualization_r/README.md) y reutiliza
los datos e indicadores conocidos del análisis anterior.

**Estado:** [09.01](01_csv_parquet_arrow/README.md) dispone de lección, scripts
de inspección, muestra CSV/Parquet y lab. [09.02](02_schemas_types/README.md)
añade contrato, evaluadores Python/R, casos de frontera y lab.
[09.03](03_python_read_write/README.md) incorpora PyArrow, conversión/relectura
Python, recorridos de entorno y lab. 09.04–09.09 siguen planificadas; sus
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
| 4 | [Leer y escribir desde R](#04-leer-y-escribir-desde-r) | Esencial | Repetir el recorrido con el mismo contrato |
| 5 | [Intercambio Python y R](#05-intercambio-python-y-r) | Práctica | Conciliar archivos escritos por el otro lenguaje |
| 6 | [Lectura selectiva y datasets](#06-lectura-selectiva-y-datasets) | Esencial | Consultar columnas y filas de varios archivos |
| 7 | [Metadatos, row groups y compresión](#07-metadatos-row-groups-y-compresion) | Práctica | Explicar y medir una decisión de almacenamiento |
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
- Práctica prevista: repetir el ejemplo Python y comprobar precisión, texto y NA.
  El paquete arrow se incorporará al proyecto renv al desarrollar esta lección.

<a id="05-intercambio-python-y-r"></a>

### 05 — Intercambio Python y R

- Escribir en Python y leer en R; después escribir en R y leer en Python.
  Comparar datos por claves acordadas, no por orden accidental ni igualdad de bytes.
- Práctica prevista: verificar número de registros, unicidad, faltantes, tipos y
  totales. Revisar casos con acentos, fechas e identificadores; usar tolerancias
  explícitas si el contrato contiene valores de punto flotante.

<a id="06-lectura-selectiva-y-datasets"></a>

### 06 — Lectura selectiva y datasets

- Proyección de columnas y filtros; Dataset/Scanner en Python y open_dataset con
  consultas dplyr en R. Diferenciar preparar una consulta de materializar resultados.
- Práctica prevista: consultar varios cortes y recoger solo un resumen o resultado
  acotado. collect/to_table pueden materializar datos en memoria; revisar el volumen.
  La omisión física de datos depende del motor, filtro y metadatos disponibles.

<a id="07-metadatos-row-groups-y-compresion"></a>

### 07 — Metadatos, row groups y compresión

- Row groups, columnas, estadísticas y códecs; distinguir compresión de codificación
  y de particionamiento. Leer metadatos antes de modificar parámetros.
- Práctica prevista: comparar una muestra equivalente con dos configuraciones,
  midiendo tamaño y lectura sin alterar el indicador. No asumir que la opción
  más pequeña siempre será la más rápida.

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

Están disponibles los [labs 09.01](../../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md)
[09.02](../../labs/09_arrow_parquet/02_schemas_types/README.md) y
[09.03](../../labs/09_arrow_parquet/03_python_read_write/README.md).
09.04–09.09 siguen previstos, con 09.08 opcional. No se da el módulo por completo.
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
Versiones y capacidades de los recorridos por desarrollar se comprobarán al
implementarlos. Esta planificación no instala paquetes.

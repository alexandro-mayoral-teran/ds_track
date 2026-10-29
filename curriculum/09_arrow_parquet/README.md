# 09 — Arrow y Parquet

[Inicio](../../README.md) / [Módulos](../README.md) / **09 — Arrow y Parquet**

**Intercambia tablas entre Python y R conservando su contrato.**

[**Empezar por 09.01 →**](01_csv_parquet_arrow/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Guardar, leer y comprobar tablas con Arrow y Parquet. Distingue representación en memoria, archivo y tipos, y verifica cada valor antes de dar por válido el intercambio.

## Antes de empezar

Completa [08 — Visualización en R](../08_visualization_r/README.md). Reutiliza contratos e indicadores conocidos; los ejemplos presentan sus entradas y no exigen entregas personales anteriores. Las primeras secciones explican conceptos antes de introducir las dependencias de lectura/escritura.

## Qué vas a aprender

- Distinguir CSV, Parquet y Arrow y sus responsabilidades.
- Definir tipos, claves, unidades y reglas de ausencia.
- Escribir y releer datos en Python y R, comparando por clave.
- Separar auditoría completa y selección de datos.
- Reconstruir una entrega con referencia externa.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **09.01** · [CSV, Parquet y Arrow](01_csv_parquet_arrow/README.md) | [Lab 09.01](../../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md) | Distinguir archivo, representación y biblioteca |
| **09.02** · [Esquemas y tipos entre lenguajes](02_schemas_types/README.md) | [Lab 09.02](../../labs/09_arrow_parquet/02_schemas_types/README.md) | Definir el contrato de una tabla compartida |
| **09.03** · [Leer y escribir desde Python](03_python_read_write/README.md) | [Lab 09.03](../../labs/09_arrow_parquet/03_python_read_write/README.md) | Convertir una muestra y comprobar su lectura |
| **09.04** · [Leer y escribir desde R](04_r_read_write/README.md) | [Lab 09.04](../../labs/09_arrow_parquet/04_r_read_write/README.md) | Repetir el recorrido con el mismo contrato |
| **09.05** · [Intercambio Python y R](05_python_r_exchange/README.md) | [Lab 09.05](../../labs/09_arrow_parquet/05_python_r_exchange/README.md) | Conciliar archivos escritos por el otro lenguaje |
| **09.06** · [Lectura selectiva y datasets](06_selective_datasets/README.md) | [Lab 09.06](../../labs/09_arrow_parquet/06_selective_datasets/README.md) | Consultar columnas y filas de varios archivos |
| **09.07** · [Metadatos, row groups y compresión](07_metadata_compression/README.md) | [Lab 09.07](../../labs/09_arrow_parquet/07_metadata_compression/README.md) | Explicar y medir una decisión de almacenamiento |
| **09.08** · [Particionamiento justificado](08_justified_partitioning/README.md) — opcional | [Lab 09.08](../../labs/09_arrow_parquet/08_justified_partitioning/README.md) | Elegir particiones según una consulta y comprobarlas |
| **09.09** · [Cierre del contrato compartido](09_shared_contract_closure/README.md) | [Lab 09.09](../../labs/09_arrow_parquet/09_shared_contract_closure/README.md) | Reconstruir datos e indicadores desde ambos lenguajes |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

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
- Disponible: [lección, funciones y preparador](08_justified_partitioning/README.md) y
  [lab 09.08](../../labs/09_arrow_parquet/08_justified_partitioning/README.md).
  Muestra autónoma de cuatro filas y base común; organización plana/por corte,
  etiqueta auxiliar y tres columnas físicas conservadas. Misma selección de
  nueve IDs/24100 MXN, auditoría de etiquetas y claves, copias duplicadas
  rechazadas y 28 particiones excesivas contrastadas con dos cortes.
  Sin dependencias nuevas ni medición de I/O, rendimiento o RAM; evolución
  de esquemas y compactación quedan como profundización posterior.

<a id="09-cierre-del-contrato-compartido"></a>

### 09 — Cierre del contrato compartido

- Integrar conversión, lectura cruzada y consulta selectiva con reglas documentadas.
- Disponible: [lección, funciones y preparador](09_shared_contract_closure/README.md) y
  [lab 09.09](../../labs/09_arrow_parquet/09_shared_contract_closure/README.md).
  Fuente copiada/contrato, archivo completo/partes planas, resumen/selección,
  notas/huellas y verificadores de solo lectura. Reconstrucción desde CSV
  independiente y cruces Python/R con 28 registros, 29000/31800 MXN y nueve
  seleccionados/24100 MXN. Ejemplo autónomo, sesiones nuevas y alteraciones
  compensadas comprobadas; no exige entregas previas ni particiones.

</details>

## Cómo trabajar este módulo

La teoría es común y los recorridos Python/R se realizan por separado. No necesitas reticulate ni ambos intérpretes en un proceso. 09.08, particiones, es opcional; nube, Flight y formatos transaccionales no son requisitos. Un esquema válido no garantiza claves únicas o valores correctos.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

<a id="qué-problema-resuelve-cada-componente"></a>

<details>
<summary><strong>Qué problema resuelve cada componente</strong></summary>

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

</details>

Puedes separar cada práctica en contrato/predicción, lectura o escritura de
un caso y contraste por clave. Revisa el primer resultado antes de pasar al
intercambio o al dataset completo. Para pausar sin perder el estado, usa la
[pauta de reanudación](../../docs/learning-workflow.md#pausar-y-retomar-una-práctica).

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Fuente y contrato | Tipos, claves, unidades y ausencias |
| Archivos completos y partes | Relectura e intercambio entre lenguajes |
| Resultados y verificadores | Comparación por clave y reconstrucción desde referencia externa |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Demuestra escritura y lectura en ambos lenguajes, explica el contrato y concilia valores e indicadores. Distingue una validación de esquema de la comprobación de cada registro y conserva las entradas.

04_large_credit_dataset figura en [proyectos](../../projects/README.md), sin carpeta ni checkpoints implementados. Los [pendientes de almacenamiento](../../docs/storage-closure.md) separan material, práctica e integración.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoint de almacenamiento propuesto: CSV tipado, Parquet, contrato y comparación
Python/R (02–05 y 09). El checkpoint de lectura selectiva prepara el módulo 10
(06–07); particionamiento se añade solo con una pregunta que lo justifique.
Sus nombres se concretarán al desarrollar el proyecto.

</details>

<a id="continuidad-y-fuentes"></a>

## Siguiente paso

**Para empezar:** [lee 09.01](01_csv_parquet_arrow/README.md) y realiza su lab.

**Al cerrar:** continúa con [10 — Polars y DuckDB](../10_polars_duckdb/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

- [Parquet: visión general](https://parquet.apache.org/docs/overview/) y
  [estructura del archivo](https://parquet.apache.org/docs/file-format/).
- [Parquet con PyArrow](https://arrow.apache.org/docs/python/parquet.html) y
  [datasets en Python](https://arrow.apache.org/docs/python/dataset.html).
- [Lectura/escritura en R](https://arrow.apache.org/docs/r/articles/read_write.html) y
  [datasets en R](https://arrow.apache.org/docs/r/articles/dataset.html).
- [Arrow en R for Data Science](https://r4ds.hadley.nz/arrow.html), como lectura abierta de apoyo.

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_csv_parquet_arrow/README.md)

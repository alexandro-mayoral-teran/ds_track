# Estado y pendientes de almacenamiento — módulo 09

## Punto de reanudación

[09.01 — CSV, Parquet y Arrow](../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md)
y su [lab](../labs/09_arrow_parquet/01_csv_parquet_arrow/README.md) están disponibles.
Incluyen la muestra CSV/Parquet de 28 observaciones, inventario, evidencia de
lectura real y recorridos esenciales de solo lectura sin dependencias nuevas.
La introducción explica filas/columnas, selección lógica frente a lectura física,
codificación/compresión y condiciones del intercambio en memoria, con decisiones
de uso sin anticipar la práctica de datasets ni la medición de rendimiento.
El esencial distingue inspección de firma de decodificación Parquet; la opción
PyArrow es una ampliación de autoría. Esta introducción no implementa el lector arrow de R.

[09.02 — Esquemas y tipos entre lenguajes](../curriculum/09_arrow_parquet/02_schemas_types/README.md)
y su [lab](../labs/09_arrow_parquet/02_schemas_types/README.md) también están
disponibles: contrato de la base conocida, evaluadores Python estándar/R base
y 23 casos separados, sin nuevas dependencias. Se conservan originales y motivos;
se explican rango/precisión, dinero, fechas/instantes y categorías. Esta sección no realiza
lectura cruzada Parquet en ambos lenguajes.

[09.03 — Leer y escribir desde Python](../curriculum/09_arrow_parquet/03_python_read_write/README.md)
dispone de lección, recorridos completos de entorno, funciones/ejecutor/verificador
y [lab](../labs/09_arrow_parquet/03_python_read_write/README.md). PyArrow 21.0.0
declarado con lockfile real; pandas 2.3.3 y registros previos conservados.
Esquema no anulable, índice omitido, entrega nueva y relectura completa por clave
contra el CSV reconstruido, sin cambiar la muestra de 09.01 ni el entorno R.

[09.04 — Leer y escribir desde R](../curriculum/09_arrow_parquet/04_r_read_write/README.md)
y su [lab](../labs/09_arrow_parquet/04_r_read_write/README.md) están disponibles.
Ejemplo pequeño completo y base común; no se necesitan entregas personales Python
ni objetos de 07–08. Arrow 25.0.1/assertthat 0.2.1 se incorporan al mismo proyecto
renv con respaldo 08.09, 44 registros previos idénticos y segunda restauración
local desde biblioteca vacía. Lectura del esquema real antes de convertir,
valores por clave y entrega R verificada desde sesión nueva, conservando
28 registros y 29000/31800 MXN. Se lee la referencia escrita por Python;
la práctica completa del intercambio en ambas direcciones se desarrolla en 09.05.

[09.05 — Intercambio Python y R](../curriculum/09_arrow_parquet/05_python_r_exchange/README.md)
y su [lab](../labs/09_arrow_parquet/05_python_r_exchange/README.md) están disponibles.
Python escribe/R lee y R escribe/Python lee, sin depender de entregas anteriores
ni añadir paquetes. Conserva la base común y concilia esquema y valores por
clave; muestra independiente de tres filas con acentos, vacío/ausencia/cero y
otro contrato. Verificaciones desde procesos nuevos, fuentes/lockfiles intactos.

[09.06 — Lectura selectiva y datasets](../curriculum/09_arrow_parquet/06_selective_datasets/README.md)
y su [lab](../labs/09_arrow_parquet/06_selective_datasets/README.md) están disponibles.
Partes Parquet, Dataset/Scanner y dplyr, filtros/proyección y materialización;
auditoría completa separada de la selección. Mantiene la base común y concilia
nueve IDs/24100 MXN para octubre ≥ 2000, contra CSV independiente en cada lenguaje.
Ejemplo pequeño completo, sesiones nuevas y fuentes/lockfiles intactos; no
acredita bytes omitidos, rendimiento ni RAM acotada.
La ampliación didáctica presenta la tabla pequeña antes del código y ejemplos
iniciales con APIs Arrow directas, sin funciones ni archivos de capítulos
anteriores. El lab separa esa práctica de la integración con CSV; Python y R
crean sus propias copias alteradas y pueden ejecutarse por separado.

[09.07 — Metadatos, row groups y compresión](../curriculum/09_arrow_parquet/07_metadata_compression/README.md)
y su [lab](../labs/09_arrow_parquet/07_metadata_compression/README.md) están
disponibles: muestra autónoma de cuatro filas y base común con cuatro variantes
y tres repeticiones. Una modificación respecto de la base por comparación,
esquema/valores por clave conservados y tiempos separados de validación.
PyArrow inspecciona estadísticas/codificaciones/códecs, también de archivos R;
arrow R 25.0.1 expone esquema/conteos y lectura de grupos. Mediciones crudas,
sesiones nuevas y fronteras comprobadas, sin cambios de dependencias/lockfiles.
La muestra no acredita rendimiento general, I/O físico ni RAM acotada.

[09.08 — Particionamiento justificado](../curriculum/09_arrow_parquet/08_justified_partitioning/README.md)
y su [lab](../labs/09_arrow_parquet/08_justified_partitioning/README.md) están
disponibles como ampliación opcional. Ejemplos autónomos y base común en
organización plana/Hive; etiqueta auxiliar con tres columnas físicas conservadas.
Auditoría de rutas/valores y referencia CSV por clave; 28 particiones por clave
contrastadas con dos cortes. Repeticiones, etiquetas falsas, vacíos y lectura
cruzada comprobados sin cambiar dependencias ni lockfiles. No acredita I/O,
rendimiento ni RAM. Esta extensión no bloquea el cierre esencial.

[09.09 — Cierre del contrato compartido](../curriculum/09_arrow_parquet/09_shared_contract_closure/README.md)
y su [lab](../labs/09_arrow_parquet/09_shared_contract_closure/README.md) están
disponibles. Ambos escritores producen fuente/contrato, Parquet completo/partes
planas, resumen/selección y notas/huellas; ambos lectores reconstruyen la fuente
externa y verifican archivos/valores desde procesos nuevos. Mantiene 28 registros,
29000/31800 MXN y nueve seleccionados/24100 MXN. Copias con errores compensados
se rechazan aun actualizando huellas. Sin dependencias nuevas, entregas previas
ni requisito de particiones; no autentica sesiones históricas ni mide rendimiento.

**El desarrollo de las nueve secciones de 09 está cerrado.**
[10.01 — Pregunta, contrato y referencia](../curriculum/10_polars_duckdb/01_question_contract_reference/README.md)
y su [lab](../labs/10_polars_duckdb/01_question_contract_reference/README.md)
ya están disponibles: muestra autónoma, referencia Python estándar y contraste
opcional R base, sin motores nuevos. Se comprueba cada ID/importe, vacíos,
tipos, fronteras y escalas deterministas de 40/400 filas; no se mide rendimiento.
[10.02 — Polars: tablas y expresiones](../curriculum/10_polars_duckdb/02_polars_tables_expressions/README.md)
y su [lab](../labs/10_polars_duckdb/02_polars_tables_expressions/README.md)
ya están disponibles: DataFrame, expresiones y operaciones inmediatas, muestra
completa y conciliación independiente. Selección 003/2600 y resumen por corte
4500/4600 MXN, tipos explícitos y suma Int64 antes de agregar. Polars 2.0.0
declarado, instalación y segunda reconstrucción uv locales comprobadas;
registros previos del lockfile conservados, sin modificar Conda, renv ni globales.
[10.03 — Polars lazy y planes de consulta](../curriculum/10_polars_duckdb/03_polars_lazy_plans/README.md)
y su [lab](../labs/10_polars_duckdb/03_polars_lazy_plans/README.md) están disponibles:
ejemplos autónomos, Parquet nuevo, esquema, planes y ejecución real conciliada.
Auditoría completa separada de la selección, dependencias de columnas y límites
del plan; mismos seis registros y 4500/4600 MXN, sin dependencias nuevas.
[10.04 — Tipos, faltantes y uniones](../curriculum/10_polars_duckdb/04_types_missing_joins/README.md)
y su [lab](../labs/10_polars_duckdb/04_types_missing_joins/README.md) están disponibles:
conversiones con originales, null/NaN, cobertura y catálogo propio. Left m:1
conserva seis saldos y 4500/4600 MXN, separa coincidencia/etiqueta conocida;
contraste Python/pandas/SQLite sin dependencias nuevas.
[10.05 — Streaming y límites de memoria](../curriculum/10_polars_duckdb/05_streaming_memory/README.md)
y su [lab](../labs/10_polars_duckdb/05_streaming_memory/README.md) están disponibles
como extensión opcional: ejemplos autónomos de lotes/sink, plan físico y
observación del pico residente en procesos nuevos Windows. Fuente/pares
conciliados, vacío y fronteras; sin paquetes nuevos ni promesa de RAM acotada.
[10.06 — DuckDB: SQL sobre Parquet](../curriculum/10_polars_duckdb/06_duckdb_parquet/README.md)
y su [lab](../labs/10_polars_duckdb/06_duckdb_parquet/README.md) están disponibles:
SQL directo sobre completo/partes, esquema y valores por clave conciliados;
EXPLAIN/EXPLAIN ANALYZE, seis filas y 4500/4600 MXN. DuckDB 2.0.0 declarado,
instalación/reconstrucción uv local comprobadas; registros anteriores conservados.
[10.07 — DuckDB desde Python y R](../curriculum/10_polars_duckdb/07_duckdb_python_r/README.md)
y su [lab](../labs/10_polars_duckdb/07_duckdb_python_r/README.md) están disponibles:
misma consulta parametrizada, ejemplos autónomos y tipos/clases conciliados.
Python DuckDB 2.0.0 y R DuckDB 1.5.6/DBI 1.3.0; lectura cruzada, vacío y
recursos ante errores. renv con respaldo y segunda restauración local, 46
registros previos conservados; dbplyr/blob registrados por inferencia de renv.
[10.08 — Intercambio entre motores](../curriculum/10_polars_duckdb/08_engine_interchange/README.md)
y su [lab](../labs/10_polars_duckdb/08_engine_interchange/README.md) están disponibles:
ocho etapas pandas/Arrow/Polars/DuckDB, tipos lógicos/valores por clave y
materialización explícita. Muestra anulable independiente y ampliación R
Arrow/DBI, sin dependencias ni lockfiles nuevos. Vacíos, precisión y errores
comprobados; no acredita ausencia de copias, RAM ni rendimiento.
El siguiente desarrollo es [10.09 — Comparar tiempo y memoria](../curriculum/10_polars_duckdb/README.md#09-comparar-tiempo-y-memoria),
todavía planificada.
El estado y verificaciones de la sesión se registran en [PROGRESS.md](../PROGRESS.md),
sin duplicar aquí una bitácora. **El material disponible no acredita práctica
del estudiante ni implementa el proyecto integrador.**

## Desarrollo del material y siguiente módulo

09 no tiene secciones pendientes de autoría. El módulo 10 dispone de 10.01–10.08
(10.05 opcional); 10.09–10.10 siguen planificadas. Desarrollar 10.09 con contexto,
datos y resultados completos; mediciones crudas repetidas, límites de cada métrica
y resultados equivalentes antes de comparar. Distinguir preparación, ejecución,
recuperación/conversión y auditoría; definir hardware, hilos, caché y procesos.
Preservar fuentes y lockfiles anteriores. Conservar la distinción plan/ejecución;
no inferir I/O físico, RAM o rendimiento general a partir de planes o muestras pequeñas.

Conservar contratos, fuentes, verificadores y entregas de 09. Distinguir
preparación de entorno de exigir resultados personales anteriores. No modificar
lockfiles ni instalar Polars/DuckDB solo para planificar. Al incorporarlos,
comprobar entornos locales y resultados equivalentes. Mantener observaciones
crudas de 09.07 sin generalizar rendimiento a partir de 28 registros ni inferir
I/O físico o RAM de planes/candidatos.

PyArrow 21.0.0 se utilizó en un entorno de autoría ya existente para producir y
releer el ejemplo 09.01; no se añadió como dependencia durante esa introducción.
Desde 09.03 sí es dependencia declarada y comprobada del track, con instalación
y segunda reconstrucción uv local. Arrow de R ya está incorporado desde 09.04. No instalar por adelantado
Polars o DuckDB solo para planificar el recorrido.

## Qué falta para cerrar las prácticas y la integración

- Reunir evidencia propia del estudiante de 09.01–09.07 y 09.09, de 09.08 si
  se elige la ampliación y, más adelante, del proyecto. Material disponible no acredita aprendizaje.
- Revisar el cierre de [08](../curriculum/08_visualization_r/README.md): geometrías,
  escalas, población, exportación desde sesión nueva y conciliación con Python.
  Sus nueve secciones tienen material; no faltan lecciones de ese módulo.
- Los criterios y pendientes del cierre de 07 siguen en
  [tidyverse-closure.md](tidyverse-closure.md). El proyecto previsto
  `03_portfolio_analysis_r` continúa sin carpeta ni checkpoints activos.
- El proyecto previsto `04_large_credit_dataset` tampoco está implementado:
  definir producto, fuentes, contrato, rúbrica y checkpoints antes de crear su
  estructura o dar por cerrada la integración de 09/10. Consultar
  [proyectos](../projects/README.md).
- R aplicado, terminal avanzada y separación entre progreso del material y
  bitácoras personales siguen como decisiones de diseño. No renumerar 00–14
  ni presentar esas integraciones como realizadas.

## Comprobaciones requeridas al desarrollar lo siguiente

Conservar fuente y resultados anteriores; probar vacío, claves duplicadas,
faltantes, límites de enteros/decimales y fechas. Comparar por clave, sin depender
del orden accidental. Si se usa punto flotante, justificar tolerancias; no
imputar ni truncar para conseguir igualdad. Distinguir equivalencia de valores,
tipos lógicos, representación en cada lenguaje e igualdad binaria del archivo.

Revisar enlaces y navegación lección → lab → comprobación → evidencia → siguiente
lección; actualizar índices, arquitectura y progreso. Cuando se incorporen
dependencias, comprobar restauración desde otra biblioteca/entorno local sin
modificar los globales. Datos personales, bibliotecas y salidas de práctica
quedan fuera de Git. 10.09–10.10 y 11–14 conservan sus planes.

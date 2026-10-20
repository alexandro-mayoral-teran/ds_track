# Roadmap

El avance se mide por capacidades demostrables. Las duraciones son flexibles:
cada nivel se puede dividir en sesiones pequeñas y no es necesario completar
las extensiones para continuar.

El estado actual no se mantiene aquí, sino en [`PROGRESS.md`](PROGRESS.md), para
que este documento permanezca como una referencia estable del plan.

## Etiquetas de alcance

- **Esencial:** requisito para niveles posteriores.
- **Práctica:** consolida el tema mediante ejercicios.
- **Extensión:** tecnología alternativa o moderna.
- **Avanzado:** profundización que no bloquea el recorrido.

El [curriculum](curriculum/README.md) muestra el flujo numerado 00–14. La
numeración ordena el estudio; Streamlit (12) y Shiny (13) son dos rutas de
aplicación y basta elegir una antes del proyecto final (14).

## Nivel 0 — Entorno de aprendizaje

**Objetivo:** ejecutar y organizar material de forma reproducible.

- Práctica: distinguir Git (historial local) de GitHub (alojamiento y colaboración),
  y comprender repositorios, commits y la relación entre local y remoto.
- Esencial: archivos Markdown (`.md`), texto plano y vista renderizada;
  encabezados, listas, enlaces y bloques de código.
- Práctica: crear un README de perfil en GitHub con presentación, objetivos de
  aprendizaje y enlaces a evidencias.
- Extensión: Markdown para documentar contexto e instrucciones de IA;
  diferenciar estructura del documento y claridad de las instrucciones.
- Esencial: terminal, rutas y archivos en PowerShell y shells Unix.
- Esencial: distinguir sistema operativo, terminal, shell y comando.
- Práctica: actualizar el perfil desde la terminal con `clone`, `status`, `diff`,
  `add`, `commit` y `push`.
- Esencial: primer script Python y primer notebook con Jupyter.
- Esencial: conceptos de entorno y dependencias.
- Práctica: preparar un solo entorno con Conda, venv + pip o uv. Conda es el
  inicio recomendado si ya se utiliza Anaconda; los otros caminos son alternativas.
- Esencial: distinguir creación, activación, intérprete y kernel; comprobar
  qué Python ejecuta un script o notebook.
- Esencial: comprender qué conservan requirements.txt, environment.yml,
  pyproject.toml y uv.lock, y revisar la configuración del recorrido elegido.
- Extensión: explorar CSV con filtros de terminal y consultar otros gestores.

**Orden recomendado:** Git y GitHub → Markdown → perfil desde la web → terminal
y rutas → actualización del perfil con Git → primer script → entorno y
dependencias 05A (preparar entorno) → 05B (instalar y conservar dependencias)
→ primer notebook.

El [índice del nivel 0](curriculum/00_getting_started/README.md) enlaza las seis
lecciones y sus labs. Basta practicar el shell y gestor elegidos: no se requiere
dominar todos los comandos, completar los tres gestores ni resolver las extensiones.

**Primera evidencia:** un README con presentación y objetivos. En la práctica
con GitHub, publicarlo como perfil y explicar cómo actualizarlo conservando su
historial. Iconos, estadísticas y automatizaciones quedan como extensiones.

GitHub es una práctica recomendada: quien estudie desde un ZIP puede crear el
README localmente y continuar sin cuenta ni publicación.

**Criterio de salida:** escribir y previsualizar un documento Markdown, ejecutar
un script y un notebook desde un entorno limpio y explicar dónde están sus
dependencias. Si se realiza la práctica de GitHub, distinguir Git de GitHub y
demostrar una actualización del perfil mediante un commit y un push.

## Nivel 1 — Python fundamental

**Objetivo:** transformar datos sin depender todavía de una biblioteca tabular.

- Esencial: tipos y operaciones; listas y diccionarios para representar registros.
- Esencial: condiciones, ciclos y funciones pequeñas.
- Esencial: leer y escribir un CSV pequeño con la biblioteca estándar.
- Esencial: separar entrada, transformación y salida; detectar datos inválidos.
- Práctica: comprobar cantidades y totales con resultados conocidos y documentar
  las reglas aplicadas desde los primeros ejercicios.
- Práctica: módulos, excepciones y lectura de JSON cuando el ejercicio lo necesite.
- Extensión: comprensiones de iterables y otras formas de expresar un cálculo.

**Orden recomendado:** tipos → listas y diccionarios → condiciones y ciclos
→ funciones → archivos CSV → validación → resumen verificable.

**Criterio de salida:** leer registros sintéticos, aplicar reglas explícitas, conservar
rechazos y producir un resumen conciliado mediante funciones pequeñas y reutilizables.
El cierre inicial utiliza ventas ficticias; el dominio crediticio se incorpora en pandas.

## Nivel 2 — pandas

**Objetivo:** dominar el modelo mental de DataFrame y el análisis tabular.

El [plan de diez secciones](curriculum/02_pandas/README.md#orden-de-desarrollo)
ordena tablas → lectura → selección → tipos → calidad → texto/fechas → agrupación
→ uniones → reshape → análisis y primera gráfica. La
[primera lección](curriculum/02_pandas/01_series_dataframe/README.md) y
[lectura/exportación](curriculum/02_pandas/02_read_inspect_export/README.md) y
[selección/filtros](curriculum/02_pandas/03_select_filter_sort/README.md),
[tipos/cálculos](curriculum/02_pandas/04_types_calculated_columns/README.md),
[faltantes/duplicados/reglas](curriculum/02_pandas/05_missing_duplicates_rules/README.md),
[texto/fechas](curriculum/02_pandas/06_text_dates/README.md),
[agrupación/resumen](curriculum/02_pandas/07_group_summarize/README.md),
[combinación de tablas](curriculum/02_pandas/08_combine_tables/README.md),
[cambio de forma](curriculum/02_pandas/09_reshape_tables/README.md) y
[análisis y primera gráfica](curriculum/02_pandas/10_analysis_plot/README.md), con sus
labs, están disponibles. El material tiene diez lecciones; cerrar el aprendizaje
requiere evidencia de sus criterios, no solo disponibilidad de los archivos.

- Series, DataFrames, selección, filtrado y tipos.
- Faltantes, duplicados, fechas y texto.
- Esencial: agregaciones, `groupby`, `merge` y reshape.
- Extensión: ventanas y acumulados después de conciliar un resumen básico.
- Visualización inicial: una gráfica sencilla y una explicación de sus hallazgos.
- Matplotlib como base Python; Altair como profundización posterior de diseño
  declarativo e interacción, según la ruta de visualización prevista.
- Uso responsable de notebooks; comprobaciones de filas, llaves y totales antes
  y después de transformar o unir datos.

**Proyecto previsto (por implementar):** `01_clean_credit_data`.

**Criterio de salida:** limpiar una cartera en CSV y justificar cada regla de
calidad aplicada, presentar una gráfica e interpretar sus resultados.

## Nivel 3 — SQL y bases de datos

**Objetivo:** consultar y modelar datos persistentes.

El [plan de nueve secciones](curriculum/03_sql_databases/README.md#orden-de-desarrollo)
conecta modelo, consultas, carga, indicadores, joins, CTE, ventanas, transacciones
y conciliación con pandas. [Modelo relacional y SQLite](curriculum/03_sql_databases/01_relational_sqlite/README.md)
y [Primeras consultas](curriculum/03_sql_databases/02_first_queries/README.md)
y [Crear tablas y cargar datos](curriculum/03_sql_databases/03_create_load/README.md)
y [Agregaciones e indicadores](curriculum/03_sql_databases/04_aggregations/README.md)
y [Relacionar tablas con joins](curriculum/03_sql_databases/05_joins/README.md)
y [Subconsultas y CTE](curriculum/03_sql_databases/06_subqueries_cte/README.md)
y [Ventanas para comparar registros](curriculum/03_sql_databases/07_windows/README.md)
y [Escrituras y transacciones](curriculum/03_sql_databases/08_transactions/README.md)
y [Integración pandas y SQL](curriculum/03_sql_databases/09_pandas_sql/README.md)
con sus labs están disponibles. Las nueve secciones tienen material;
la finalización del aprendizaje requiere evidencia de los criterios.

- Esencial: modelo relacional, tablas, llaves, restricciones y normalización básica.
- Esencial: selección, filtros, agregaciones y joins con SQLite.
- Práctica: CTE, subconsultas y ventanas básicas para preguntas concretas.
- Esencial: comprender transacciones al escribir datos y verificar los indicadores.
- Avanzado: índices, planes de consulta y optimización cuando exista una limitación.
- Extensión: PostgreSQL después de dominar las operaciones en SQLite.

**Proyecto previsto (por implementar):** `02_credit_database`.

**Criterio de salida:** diseñar un modelo relacional y obtener indicadores de
cartera mediante consultas verificables.

**Checkpoint de integración:** integrar lo aprendido en un análisis pequeño: leer datos
con Python, limpiar con pandas, consultar indicadores en SQLite y explicar una
gráfica. Reutilizar los proyectos de limpieza y base de datos, sin crear un
proyecto adicional obligatorio. Conciliar al menos un indicador entre pandas
y SQL y conservar instrucciones de ejecución. Los niveles 04 y 05 ampliarán
su visualización y organización; ese análisis consolidado se reutiliza al pasar a R.

## Nivel 4 — Visualización en Python

**Objetivo:** comunicar un análisis conocido con gráficos justificables.

El [plan de nueve secciones](curriculum/04_visualization_python/README.md#orden-de-desarrollo)
parte de la pregunta, desarrolla Matplotlib y después Altair; la interacción es
opcional. Están disponibles
[04.01 — Pregunta y elección de gráfico](curriculum/04_visualization_python/01_question_chart/README.md),
[04.02 — Matplotlib: Figure y Axes](curriculum/04_visualization_python/02_figure_axes/README.md),
[04.03 — Comparaciones y evolución](curriculum/04_visualization_python/03_comparisons_evolution/README.md),
[04.04 — Distribuciones y relaciones](curriculum/04_visualization_python/04_distributions_relationships/README.md),
[04.05 — Escalas, etiquetas y accesibilidad](curriculum/04_visualization_python/05_scales_labels_accessibility/README.md),
[04.06 — Composición y exportación](curriculum/04_visualization_python/06_composition_export/README.md),
[04.07 — Altair: visualización declarativa](curriculum/04_visualization_python/07_altair_declarative/README.md),
[04.08 — Interacción con Altair (opcional)](curriculum/04_visualization_python/08_altair_interaction/README.md) y
[04.09 — Cierre visual del análisis](curriculum/04_visualization_python/09_visual_closure/README.md),
con sus labs. Las nueve secciones tienen material; interacción es opcional
y el cierre reconstruye figuras, indicadores conciliados e interpretación.
La finalización del aprendizaje requiere evidencia de sus criterios.

- Esencial: pregunta, gráfico adecuado, escalas, unidades, etiquetas y color accesible.
- Esencial: Matplotlib, Figure/Axes, barras, líneas y distribuciones.
- Práctica: composición, anotaciones y exportación.
- Práctica: Altair, marcas, codificaciones y tipos; interacción como extensión.

**Criterio de salida:** explicar un indicador de pandas/SQL mediante una figura,
justificar su representación y conservar el código que la reconstruye.

## Nivel 5 — Python aplicado

**Objetivo:** transformar un análisis de notebook en código reutilizable y verificable.

El [plan de once secciones](curriculum/05_python_applied/README.md#orden-de-desarrollo)
define un núcleo de módulos, configuración, errores, pruebas y contratos para
cerrar el análisis; clases, generadores, decoradores, medición y APIs amplían
ese núcleo. [05.01 — Del notebook a módulos](curriculum/05_python_applied/01_notebook_to_modules/README.md)
y [05.02 — Configuración y registro](curriculum/05_python_applied/02_configuration_logging/README.md)
y [05.03 — Errores y recursos](curriculum/05_python_applied/03_errors_resources/README.md)
y [05.04 — Pruebas de código y datos](curriculum/05_python_applied/04_testing/README.md)
disponen de lección y lab; 05.04 incluye pruebas unittest sobre el paquete compartido.
[05.05 — Tipos y contratos](curriculum/05_python_applied/05_types_contracts/README.md)
dispone de lección/lab, cobertura con contrato explícito y revisión sin exportar.
[05.06 — Clases, composición y dataclasses](curriculum/05_python_applied/06_classes_composition/README.md)
dispone de lección/lab opcionales, configuración por campos y composición sobre
la revisión existente.
[05.07 — Iteradores y generadores](curriculum/05_python_applied/07_iterators_generators/README.md)
dispone de lección/lab de extensión, consumo y lectura por lotes conciliada,
con límites de memoria explícitos.
[05.08 — Funciones como valores y decoradores](curriculum/05_python_applied/08_functions_decorators/README.md)
dispone de lección/lab de extensión y envoltura de registro con comportamiento
comprobado.
[05.09 — Medir antes de optimizar](curriculum/05_python_applied/09_measure_optimize/README.md)
dispone de lección/lab de extensión, tiempos repetidos, memoria trazada y perfiles;
compara alternativas equivalentes sin prometer una mejora universal.
[05.10 — Integración con APIs](curriculum/05_python_applied/10_api_integration/README.md)
dispone de lección/lab de extensión, respuestas locales, paginación acotada y
conciliación; transporte HTTPS probado con sustitutos, sin conexión obligatoria.
[05.11 — Cierre del proyecto Python](curriculum/05_python_applied/11_project_closure/README.md)
dispone de lección/lab, reconstrucción desde fuentes copiadas y verificación
de tablas y figura guardadas. Las once secciones tienen material disponible;
el aprendizaje se acredita mediante evidencias revisadas.

- Esencial: módulos, funciones, configuración, logging y comprobaciones.
- Práctica: anotaciones de tipos, clases, composición y dataclasses cuando aporten claridad.
- Práctica: iteradores y generadores; usar decoradores existentes.
- Extensión: crear decoradores, gestores de contexto y excepciones propias.
- Extensión: profiling, APIs y reintentos según necesidades del análisis.
- Avanzado: herencia, concurrencia y metaprogramación, sin bloquear el recorrido.

**Criterio de salida:** reorganizar el análisis conocido, separar entrada,
transformación y salida y comprobar que conserva sus indicadores y su figura.
Este cierre prepara el cambio de lenguaje a R; no exige dominar toda la POO.

## Nivel 6 — R fundamental

El [plan de nueve secciones](curriculum/06_r_foundations/README.md#orden-de-desarrollo)
introduce el modelo de R, funciones, archivos y renv antes de conciliar con Python.
[06.01 — R, editor, scripts y paquetes](curriculum/06_r_foundations/01_r_session/README.md)
dispone de lección, script y lab.
[06.02 — Objetos, vectores y tipos](curriculum/06_r_foundations/02_objects_vectors/README.md)
añade tipos/longitudes, coerción, operaciones vectorizadas y reciclaje con scripts y lab.
[06.03 — Seleccionar elementos](curriculum/06_r_foundations/03_subsetting/README.md)
dispone de lección/script/lab, correspondencia y contraste de operadores.
[06.04 — Lógica y valores faltantes](curriculum/06_r_foundations/04_logic_missing/README.md)
dispone de lección/script/lab: condiciones desconocidas, grupos conciliados,
any/all y resúmenes con cobertura. [06.05 — Listas y data frames](curriculum/06_r_foundations/05_lists_data_frames/README.md)
añade listas, tablas, selección con dimensiones conservadas y copia recalculada, con script y lab.
[06.06 — Funciones y control de flujo](curriculum/06_r_foundations/06_functions_control/README.md)
añade funciones reutilizables, decisiones con cobertura, ciclos y rechazos explícitos,
con scripts y lab.
[06.07 — Archivos y validación básica](curriculum/06_r_foundations/07_files_validation/README.md)
añade lectura textual, aceptados/rechazos conciliados y exportación comprobada,
con CSV propio, scripts y lab.
[06.08 — Proyectos y dependencias con renv](curriculum/06_r_foundations/08_projects_renv/README.md)
añade copia autocontenida, lockfile real, restauración y reconstrucción comprobada,
con preparador y lab.
[06.09 — Reproducir un resultado conocido](curriculum/06_r_foundations/09_known_result/README.md)
cierra con referencia Python independiente sobre el mismo contrato, comparación
de detalle/rechazos/indicadores y verificador de solo lectura. Las nueve secciones
tienen material; acreditar aprendizaje requiere evidencia de sus criterios.
Las referencias están en
[la guía de lecturas R](docs/r-reading-guide.md).

**Objetivo:** trasladar conceptos de análisis al ecosistema de R.

**Prerrequisito:** el análisis consolidado al finalizar el nivel 5. Reutilizar sus preguntas y
datos para aprender el modelo de R sobre un problema conocido.

- Vectores, listas, data frames, funciones y paquetes.
- Importación, transformación y conciliación básica; primera figura en el nivel 07.
- Proyectos reproducibles con `renv`.
- Equivalencias entre pandas y R.

**Criterio de salida:** reproducir en R un análisis conocido de Python sin
traducir mecánicamente cada línea.

## Nivel 7 — tidyverse y comunicación visual

El [plan de diez secciones](curriculum/07_tidyverse/README.md#orden-de-desarrollo)
conecta importación, transformación, calidad, relaciones, fechas y primera figura.
La [lección 07.01](curriculum/07_tidyverse/01_tibbles_import_pipes/README.md) y su
lab están disponibles: readr, tibble y pipe nativo sobre la cartera conocida,
con dependencias registradas en renv.
[07.02](curriculum/07_tidyverse/02_select_filter_sort/README.md) dispone de lección/lab
y script: columnas, condiciones con NA y orden con dplyr.
[07.03](curriculum/07_tidyverse/03_transform_columns/README.md) añade lección/lab,
conversión auditable e indicadores con mutate/if_else/case_when; conserva
el lockfile de 07.02.
[07.04](curriculum/07_tidyverse/04_missing_duplicates_quality/README.md) añade lección/lab,
reglas, claves y todos los motivos, con aceptados/rechazos reconstruidos sobre
44 registros. [07.05](curriculum/07_tidyverse/05_group_summarize/README.md)
añade lección/lab y resúmenes de los aceptados: agrupación, denominadores,
cobertura y conciliación con pandas sin nuevas dependencias.
[07.06](curriculum/07_tidyverse/06_join_tables/README.md) añade lección/lab,
uniones con cardinalidad y cobertura explícitas, catálogo estático y
conciliación pandas/SQLite; conserva los 29 aceptados y su saldo.
[07.07](curriculum/07_tidyverse/07_tidy_reshape/README.md) añade lección/lab,
pivot_longer/pivot_wider, claves únicas y distinción de ausencias; conserva
una proyección de 48 observaciones de dos cortes y sus indicadores. Incorpora
tidyr con lockfile/restauración local y respaldo, sin mezclar otras muestras.
[07.08](curriculum/07_tidyverse/08_text_categories_factors/README.md) añade lección/lab,
texto normalizado con reglas y origen conservado, pendientes y factores nominales
con niveles controlados. Incorpora forcats y declara stringr en el mismo proyecto.
[07.09](curriculum/07_tidyverse/09_dates_cutoffs/README.md) añade lección/lab,
fechas interpretadas con formato/calendario y motivos conservados, diferencias
en días, selección de períodos y comparación de 14 IDs comunes. Incorpora
lubridate con lockfile y respaldo.
[07.10](curriculum/07_tidyverse/10_first_plot_closure/README.md) cierra el material
con lección/lab, primera figura ggplot2, exportación y verificación de tablas
reconstruidas. Las diez secciones de 07 están disponibles; 08.01–08.02 tienen
lección, script y lab, 08.03–08.09 siguen planificadas y el proyecto integrador permanece pendiente. Consulta
[el cierre y pendientes](docs/tidyverse-closure.md) y
[la guía de lecturas R](docs/r-reading-guide.md).

**Objetivo:** realizar análisis expresivos y comunicar hallazgos.

- `dplyr`, `tidyr`, `stringr` y manejo de fechas.
- `ggplot2`, escalas, facetas y diseño de gráficas.
- Esencial: importación y exportación de archivos desde R.
- Extensión: acceso a SQL con DBI/RSQLite o dbplyr, reutilizando el nivel 03.

**Proyecto previsto (por implementar):** `03_portfolio_analysis_r`.

**Criterio de salida:** producir un análisis de cartera entendible por una
persona que no escribió el código.

## Nivel 8 — Visualización en R

El [plan de nueve secciones](curriculum/08_visualization_r/README.md#orden-de-desarrollo)
profundiza gramática, escalas, composición y exportación sobre el análisis conocido.
[08.01 — Pregunta y gramática de gráficos](curriculum/08_visualization_r/01_question_grammar/README.md)
tiene lección, script y lab; también
[08.02 — Geometrías y transformaciones estadísticas](curriculum/08_visualization_r/02_geometries_stats/README.md),
con figuras y cálculos comprobados. 08.03–08.09 siguen planificadas.
Las referencias abiertas están en [la guía de lecturas R](docs/r-reading-guide.md).

**Objetivo:** profundizar en ggplot2 sobre resultados ya conocidos.

- Esencial: estéticas, geometrías, escalas, etiquetas y facetas.
- Práctica: temas, anotaciones, composición y exportación.
- Práctica: comparar interpretaciones con las figuras del análisis Python.

**Criterio de salida:** construir y explicar una figura reproducible en R,
con indicadores conciliados y elección de representación justificada.

## Nivel 9 — Arrow y Parquet

**Objetivo:** comprender almacenamiento columnar y datasets mayores.

El [plan de nueve secciones](curriculum/09_arrow_parquet/README.md#orden-de-desarrollo)
presenta teoría común, esquemas, recorridos Python y R, intercambio en ambas
direcciones, lectura selectiva, metadatos y cierre. Particionamiento es opcional.
Las lecciones y labs están por desarrollar.

- Esencial: leer y escribir Parquet; comprender tipos, esquemas y almacenamiento columnar.
- Práctica: comparar CSV y Parquet en tamaño, tipos y lectura selectiva.
- Práctica: compresión, metadatos, row groups y pushdown con ejemplos pequeños.
- Extensión: particiones cuando las preguntas y el volumen las justifiquen.
- Avanzado: archivos pequeños y evolución de esquemas.
- Práctica: interoperabilidad entre Python, R y motores SQL.

**Criterio de salida:** convertir un CSV a Parquet bien tipado, comprobar que
conserva registros e indicadores al intercambiarlo entre Python y R en ambas
direcciones, y explicar el contrato. Particionar solo cuando
se pueda justificar; no es requisito para el primer ejercicio.

## Nivel 10 — Polars y DuckDB

**Objetivo:** procesar datos grandes en una sola máquina con criterio.

El [plan de diez secciones](curriculum/10_polars_duckdb/README.md#orden-de-desarrollo)
parte de un contrato conocido: expresiones y lazy en Polars, SQL sobre Parquet
con DuckDB, clientes Python/R, intercambio, mediciones y elección de herramienta.
Polars se enseña principalmente desde Python; su interfaz R y streaming son
ampliaciones opcionales. Las lecciones y labs están por desarrollar.

- Ejecución eager y lazy en Polars.
- Consultas SQL sobre Parquet con DuckDB.
- Extensión: procesamiento por lotes y cargas mayores que memoria, según recursos.
- Benchmarks frente a pandas: tiempo, memoria y legibilidad.

**Proyecto previsto (por implementar):** `04_large_credit_dataset`.

**Criterio de salida:** resolver el mismo problema con pandas, Polars y DuckDB,
y escoger una herramienta usando mediciones.

## Nivel 11 — Reportes reproducibles

El [plan de nueve secciones](curriculum/11_reporting_quarto/README.md#orden-de-desarrollo)
conecta documento, ejecución Python/R, evidencia, parámetros, caché y entrega.
HTML con un motor es esencial; PDF, dashboard y publicación son ampliaciones.
Las lecciones y labs están por desarrollar.

**Objetivo:** transformar análisis en productos consumibles.

Este nivel formaliza la comunicación iniciada con gráficas e interpretación en
pandas y tidyverse; no es la primera ocasión de explicar resultados.

- Narrativa, tablas, gráficas y parámetros.
- Esencial: Quarto con un motor elegido, Python/Jupyter o R/knitr.
- Esencial: HTML regenerable y revisado.
- Extensión: comparar el otro motor, PDF, dashboards y automatización de reportes.

**Proyecto previsto (por implementar):** `05_monthly_report`.

**Criterio de salida:** generar nuevamente un reporte completo partiendo de los
datos y el código, sin edición manual de resultados.

## Nivel 12 — Streamlit

El [plan de nueve secciones](curriculum/12_streamlit/README.md#orden-de-desarrollo)
introduce reejecución, widgets, funciones de datos, estado, caché, validación,
presentación, pruebas y entrega local.
Las lecciones y labs están por desarrollar.

**Objetivo:** convertir un análisis estable en una aplicación de datos Python.

- Esencial: inputs, tablas, gráficos y modelo de reejecución.
- Práctica: estado, caché y mensajes para entradas inválidas o filtros vacíos.
- Esencial: separar lógica de datos de la interfaz y comprobar indicadores.

**Criterio de salida:** crear un explorador con filtros y resultados verificables.
Es la ruta Python; se puede elegir en lugar de Shiny y pasar al proyecto final.
El proyecto/checkpoint específico se definirá al desarrollar este módulo.

## Nivel 13 — Shiny y fundamentos web

El [plan de diez secciones](curriculum/13_shiny_web/README.md#orden-de-desarrollo)
introduce web básica, UI/servidor, reactividad, filtros, eventos, validación,
presentación, módulos, pruebas y entrega local. Mastering Shiny apoya la ruta R.
Las lecciones y labs están por desarrollar.

**Objetivo:** convertir un análisis estable en una aplicación interactiva.

- Cliente, servidor, HTTP, HTML y CSS básicos.
- UI, servidor, estado y reactividad en Shiny.
- Inputs, outputs, validaciones y módulos.
- Lectura desde Parquet o una base de datos.

**Proyecto previsto (por implementar):** `06_shiny_portfolio_app`.

Streamlit ocupa el nivel 12. Elegir una de las dos aplicaciones; no exigir ambas.

**Criterio de salida:** construir un explorador de cartera con filtros y
mensajes de error comprensibles, sin mezclar la UI con las transformaciones.

## Nivel 14 — Proyecto reproducible

El [plan de nueve secciones](curriculum/14_reproducible_projects/README.md#orden-de-desarrollo)
consolida contrato, estructura, entornos, reprocesamiento, pruebas, trazabilidad,
productos y reconstrucción independiente. CI y despliegue son extensiones.
Las lecciones y labs están por desarrollar.

**Objetivo:** integrar el recorrido con prácticas de ingeniería.

La validación, documentación y separación de pasos se practican desde Python.
Aquí se profundiza en pruebas y automatización y se integran en un proyecto final.

- Código modular, configuración y logging.
- Pruebas unitarias, de integración y de calidad de datos.
- Pipelines idempotentes y reprocesamiento.
- Separación raw/clean/analytics.
- Secretos, PII y publicación segura.
- Automatización con Git como extensión.

**Criterio de salida:** reconstruir datos, métricas y producto final a partir de
instrucciones documentadas y datos sintéticos, incluyendo un reporte HTML y
una aplicación local elegida. Publicación en línea y CI no son requisitos.

## Temas estacionados

Se investigarán cuando resuelvan una limitación del recorrido:

- Orquestadores como Dagster o Prefect.
- Almacenamiento de objetos compatible con S3.
- dbt o SQLMesh.
- Apache Iceberg y conceptos lakehouse.
- Spark y procesamiento distribuido.
- APIs con Plumber o FastAPI.
- Terminal avanzada: filtros, redirecciones y automatización de datos, sin ubicación
  numerada o material desarrollado todavía.
- R aplicado después de visualización R: organización, pruebas y profundización;
  su integración numerada sigue pendiente y no modifica los niveles 09–14.

Estos temas no bloquean los módulos numerados. Las especializaciones avanzadas
de Python se tratarán dentro del nivel 05 cuando exista una necesidad concreta.

# Curriculum

El flujo está numerado por prerrequisitos. El nivel 00 tiene lecciones y labs;
el nivel 01 dispone de variables/tipos, listas/diccionarios, condiciones/ciclos,
funciones, archivos CSV y validación/resumen. Sus seis lecciones y labs están
disponibles. El módulo 02 tiene las diez lecciones de pandas y sus labs, incluido el cierre
con notebook y gráfica. SQL dispone de [sus nueve lecciones y labs](03_sql_databases/README.md),
incluido el [cierre de integración pandas/SQL](03_sql_databases/09_pandas_sql/README.md)
con indicadores y gráfica. Los módulos 04–05 tienen objetivos, prácticas y cierres propuestos,
todavía sin lecciones ejecutables ni labs.
Los módulos 06–08 tienen planes detallados de R fundamental, tidyverse y gráficos,
con [lecturas abiertas de apoyo](../docs/r-reading-guide.md). Los módulos 09–10
tienen planes detallados de almacenamiento compartido Python/R y procesamiento
con Polars/DuckDB. Los módulos 11–14 tienen planes de reportes, aplicaciones
alternativas y proyecto final. Todo el recorrido numerado tiene secciones definidas;
la planificación pendiente se implementará lección por lección.
El estado de desarrollo y las evidencias se registran en [PROGRESS.md](../PROGRESS.md).

| Nivel | Módulo | Resultado previsto |
| --- | --- | --- |
| 00 | [Entorno de aprendizaje](00_getting_started/) | Editar, ejecutar y comprobar scripts y notebooks |
| 01 | [Python fundamental](01_python_foundations/) | Transformar y validar registros con Python estándar |
| 02 | [pandas](02_pandas/) | Limpiar y resumir datos tabulares |
| 03 | [SQL y bases de datos](03_sql_databases/) | Modelar relaciones y consultar indicadores |
| 04 | [Visualización en Python](04_visualization_python/) | Comunicar resultados con Matplotlib y Altair |
| 05 | [Python aplicado](05_python_applied/) | Organizar un análisis en código reutilizable y verificable |
| 06 | [R fundamental](06_r_foundations/) | Reproducir un análisis conocido en R |
| 07 | [tidyverse](07_tidyverse/) | Transformar y preparar datos en R |
| 08 | [Visualización en R](08_visualization_r/) | Comunicar con ggplot2 y comparar representaciones |
| 09 | [Arrow y Parquet](09_arrow_parquet/) | Almacenar y comprobar datos columnares |
| 10 | [Polars y DuckDB](10_polars_duckdb/) | Procesar y comparar herramientas a mayor escala |
| 11 | [Reportes con Quarto](11_reporting_quarto/) | Generar un reporte reproducible |
| 12 | [Streamlit](12_streamlit/) | Construir una aplicación de datos en Python |
| 13 | [Shiny y fundamentos web](13_shiny_web/) | Construir una aplicación de datos en R |
| 14 | [Proyecto reproducible](14_reproducible_projects/) | Integrar datos, código, pruebas y producto final |

## Por qué este orden

1. **00–05: construir una base en Python.** Preparar herramientas, manipular datos
   con Python/pandas/SQL, comunicar un análisis y después organizar su código.
   Python aplicado usa un problema conocido: clases y decoradores no bloquean pandas.
2. **06–10: comparar ecosistemas y procesar más datos.** Reproducir el análisis
   en R, preparar tablas con tidyverse, profundizar en ggplot2 y después estudiar
   Parquet, Polars y DuckDB.
3. **11–14: entregar un producto.** Crear reportes, elegir una aplicación y
   cerrar con un proyecto reproducible.

Streamlit (12) y Shiny (13) son rutas de aplicación equivalentes en Python y R.
La numeración muestra ambas en el flujo, pero puedes elegir una y pasar al 14;
la otra queda para comparación posterior. ggplot2 básico aparece en tidyverse;
su diseño y composición se profundizan en el 08. Matplotlib básico aparece en
pandas; el 04 desarrolla visualización y Altair.

Dentro de Python aplicado, organización y validación son el núcleo; metaprogramación,
concurrencia y especializaciones no son requisitos para continuar a R.
Consulta [ROADMAP.md](../ROADMAP.md) para los criterios de salida y
[la arquitectura](../docs/architecture.md) para el diseño del material.

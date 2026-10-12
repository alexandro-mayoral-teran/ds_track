# Curriculum

Los módulos están ordenados por prerrequisitos. Cada directorio comienza con un
README que define objetivos y criterio de salida. El estado actual se mantiene
únicamente en [`PROGRESS.md`](../PROGRESS.md).

| Módulo | Resultado principal |
| --- | --- |
| [`00_getting_started`](00_getting_started/) | Entorno ejecutable |
| [`01_python_foundations`](01_python_foundations/) | Transformación con Python estándar |
| [`02_pandas`](02_pandas/) | Datos limpios, análisis y primera gráfica con Matplotlib |
| [`03_sql_databases`](03_sql_databases/) | Modelo y consultas relacionales |
| [`04_r_foundations`](04_r_foundations/) | Análisis básico equivalente en R |
| [`05_tidyverse`](05_tidyverse/) | Análisis y visualización con ggplot2 en R |
| [`06_arrow_parquet`](06_arrow_parquet/) | Dataset columnar bien diseñado |
| [`07_polars_duckdb`](07_polars_duckdb/) | Procesamiento local de mayor escala |
| [`08_reporting_quarto`](08_reporting_quarto/) | Reporte reproducible |
| [`09_shiny_web`](09_shiny_web/) | Aplicación interactiva: Shiny en R o ruta Streamlit en Python |
| [`10_reproducible_projects`](10_reproducible_projects/) | Pipeline probado y documentado |

## Rutas complementarias planificadas

Estas rutas tienen carpetas propias con su planificación. Sus lecciones y labs aún
no están desarrollados. No cambian la
numeración 00–10 ni son requisitos para comenzar pandas.

| Ruta | Cuándo se introduce | Contenido previsto |
| --- | --- | --- |
| [Python aplicado](python_applied/) | Después de pandas y SQL | Módulos, clases, composición, dataclasses, tipos, generadores, decoradores, pruebas, rendimiento y APIs |
| [Visualización en Python](visualization_python/) | Base con pandas; profundización después de un análisis estable | Matplotlib, diseño de gráficos y Altair declarativo e interactivo |
| [Visualización en R](visualization_r/) | R fundamental y tidyverse | ggplot2, estéticas, geometrías, escalas, facetas y comunicación |
| [Streamlit](streamlit/) | Después de análisis y gráficos verificables | Aplicación Python; alternativa al recorrido de Shiny del nivel 9 |

Se podrá elegir un ecosistema para cada producto y comparar el otro después.
La [arquitectura](../docs/architecture.md#rutas-de-profundización-previstas)
describe prerrequisitos y resultados esperados. El material se creará cuando
se desarrolle cada ruta, sin mantener carpetas vacías como si fueran lecciones.

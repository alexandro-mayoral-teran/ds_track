# Proyectos

Los proyectos integran módulos y producen un resultado compartible.

| Proyecto | Prerrequisitos | Producto |
| --- | --- | --- |
| `01_clean_credit_data` | Python, pandas | Dataset limpio y perfil de calidad |
| `02_credit_database` | SQL, modelado | Base relacional y consultas analíticas |
| `03_portfolio_analysis_r` | R, tidyverse | Análisis visual de cartera |
| `04_large_credit_dataset` | Parquet, Polars, DuckDB | Pipeline y benchmark local |
| `05_monthly_report` | Quarto | Reporte reproducible por corte |
| `06_shiny_portfolio_app` | Shiny, web básico | Explorador interactivo |

Los proyectos de la tabla son planes: se creará cada carpeta cuando se
implemente una práctica integradora con entradas, producto y criterios de salida.
El inicio o cierre del material de un módulo no activa por sí solo su proyecto.
Así se evita mantener esqueletos vacíos.

Las diez secciones de 07 ya tienen material y un cierre de práctica reproducible,
pero 03_portfolio_analysis_r y sus checkpoints siguen pendientes. Consulta los
[criterios y pendientes de 07](../docs/tidyverse-closure.md) antes de tratarlos
como entregas disponibles.

Las nueve secciones de 09 también tienen material, incluido un
[cierre de práctica verificable](../curriculum/09_arrow_parquet/09_shared_contract_closure/README.md).
Eso no implementa `04_large_credit_dataset` ni activa sus checkpoints; el módulo
10.01 ya tiene material de contrato/referencia y 10.02 de tablas/expresiones
Polars; 10.03 añade planes lazy y ejecución conciliada.
10.04 añade tipos, faltantes y uniones conciliadas con cobertura.
10.05 añade la extensión opcional de lotes/sink y memoria observada;
10.06–10.10 siguen planificadas. Esto no implementa el proyecto.
Consulta los [pendientes de almacenamiento](../docs/storage-closure.md).

Los módulos 04 y 05 amplían el análisis Python con figuras y código reutilizable;
los módulos 07 y 08 alimentan el análisis en R y sus figuras. Quarto ocupa el
nivel 11. La aplicación Shiny pertenece al 13; el nivel 12 ofrece Streamlit
como elección alternativa. Su proyecto o checkpoint se definirá al desarrollar
esa ruta, sin exigir construir dos aplicaciones para completar el nivel 14.

Los proyectos avanzarán mediante checkpoints enlazados a lecciones y labs. Las
reglas están en
[`docs/learning-workflow.md`](../docs/learning-workflow.md), y la estructura
inicial está en [`templates/project/`](../templates/project/).

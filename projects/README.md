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

Cada proyecto se creará cuando comience su módulo prerrequisito. Así se evita
mantener esqueletos vacíos y se permite que la arquitectura evolucione con el
aprendizaje.

Los proyectos avanzarán mediante checkpoints enlazados a lecciones y labs. Las
reglas están en
[`docs/learning-workflow.md`](../docs/learning-workflow.md), y la estructura
inicial está en [`templates/project/`](../templates/project/).

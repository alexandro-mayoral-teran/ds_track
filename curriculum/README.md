# Curriculum

[Inicio](../README.md) / **Recorrido de aprendizaje**

**Encuentra tu módulo y sigue una lección a la vez.**

El recorrido está numerado por prerrequisitos. Cada módulo reúne sus lecciones,
prácticas y criterios de salida; empieza por sus instrucciones y continúa con
el lab asociado.

[**Empezar por 00.01 →**](00_getting_started/01_github_profile/README.md) · [Módulos por etapa](#módulos-por-etapa) · [Cómo avanzar](#cómo-avanzar) · [Buscar un lab](../labs/README.md)

> **Estado del material:** 00–11 y [12.01–12.09](12_streamlit/README.md) están disponibles;
> [13.01–13.10](13_shiny_web/README.md) están disponibles; 14.01–14.09 tienen material de diseño, estructura, entornos, reprocesamiento, pruebas, trazabilidad, integración local y entrega opcional; la base de material del recorrido está disponible. Esto describe el contenido, no el aprendizaje de cada
> participante. Consulta el estado de proyectos y checkpoints por separado.

## Módulos por etapa

### 1 · Prepara y analiza — 00–05

Desde tus herramientas iniciales hasta un análisis organizado en código.

| Módulo | Aprenderás a… |
| --- | --- |
| **00** · [Entorno de aprendizaje](00_getting_started/README.md) | Documentar, ubicar archivos y ejecutar tu primer script y notebook |
| **01** · [Python fundamental](01_python_foundations/README.md) | Transformar y validar registros con Python estándar |
| **02** · [pandas](02_pandas/README.md) | Inspeccionar, transformar y resumir tablas |
| **03** · [SQL y bases de datos](03_sql_databases/README.md) | Modelar relaciones y consultar indicadores |
| **04** · [Visualización en Python](04_visualization_python/README.md) | Comunicar resultados con Matplotlib y Altair |
| **05** · [Python aplicado](05_python_applied/README.md) | Organizar un análisis en código reutilizable y verificable |

### 2 · Amplía tus herramientas — 06–10

Reproduce análisis en R y compara formas de almacenar y procesar datos.

| Módulo | Aprenderás a… |
| --- | --- |
| **06** · [R fundamental](06_r_foundations/README.md) | Trabajar con objetos, funciones y proyectos en R |
| **07** · [tidyverse](07_tidyverse/README.md) | Preparar, transformar y combinar tablas en R |
| **08** · [Visualización en R](08_visualization_r/README.md) | Diseñar y revisar figuras con ggplot2 |
| **09** · [Arrow y Parquet](09_arrow_parquet/README.md) | Almacenar e intercambiar datos conservando tipos y valores |
| **10** · [Polars y DuckDB](10_polars_duckdb/README.md) | Consultar datos y comparar herramientas con evidencia |

### 3 · Comunica e integra — 11–14

Entrega un reporte, elige una ruta de aplicación y después integra el trabajo.

| Módulo | Resultado previsto | Material |
| --- | --- | --- |
| **11** · [Reportes con Quarto](11_reporting_quarto/README.md) | Reporte reconstruible con datos, código y narrativa | Disponible |
| **12** · [Streamlit](12_streamlit/README.md) | Aplicación de datos en Python | 12.01–12.09 disponibles |
| **13** · [Shiny y fundamentos web](13_shiny_web/README.md) | Aplicación de datos en R | Diez secciones disponibles, incluida entrega local |
| **14** · [Proyecto reproducible](14_reproducible_projects/README.md) | Integración de datos, código, pruebas y producto final | 14.01–14.09 disponibles; 14.08 opcional; revisión final disponible |

> **Elige una aplicación:** Streamlit (12) y Shiny (13) son alternativas.
> Basta una antes del proyecto final (14); puedes estudiar la otra después.

## Cómo avanzar

1. Abre el **índice del módulo** y revisa su preparación y orden.
2. Lee una **lección** y predice el resultado antes de ejecutar sus ejemplos.
3. Realiza su **lab** en tu propia copia; usa las pistas cuando hagan falta.
4. **Comprueba y explica** el resultado con tu compañero.
5. Conserva **evidencia, dudas y siguiente paso** en tu nota personal.
6. Continúa con la **siguiente lección** cuando puedas justificar lo aprendido.

Una sesión puede cubrir solo un bloque. No necesitas abrir todas las lecciones
ni resolver ampliaciones opcionales para dar tu siguiente paso esencial.

| Si buscas… | Consulta… |
| --- | --- |
| El primer paso del recorrido | [00 — Entorno de aprendizaje](00_getting_started/README.md) |
| Una práctica concreta | [Índice de labs](../labs/README.md) |
| Una integración o checkpoint | [Proyectos y su estado](../projects/README.md) |
| Registrar tu primera evidencia | [Bitácora del módulo 00](../templates/learning-session/bitacora-00.md) |
| Capacidades y prerrequisitos detallados | [ROADMAP.md](../ROADMAP.md) |
| Qué material se desarrolló y qué sigue | [PROGRESS.md](../PROGRESS.md), registro editorial |

<a id="por-qué-este-orden"></a>

<details>
<summary><strong>Por qué este orden y qué es opcional</strong></summary>

Primero preparas herramientas y trabajas con Python, pandas y SQL. Después
comunicas resultados y organizas un análisis conocido antes de pasar a R.
R tiene su propio modelo de objetos y operaciones; no es una traducción línea
por línea de Python. Arrow/Parquet y los motores de consulta llegan después de
las bases de manipulación y validación.

Matplotlib básico aparece en pandas y se desarrolla en 04; ggplot2 comienza en
tidyverse y se profundiza en 08. En 05, organización y validación forman el
núcleo; las ampliaciones señaladas no son requisitos para continuar a R.
Cada índice indica qué es esencial, práctica, extensión u opcional.

Las razones de diseño del recorrido están en la
[arquitectura educativa](../docs/architecture.md). El detalle de desarrollo y las
comprobaciones anteriores se conserva en PROGRESS.md y en los índices de módulo,
sin repetirlo como introducción a este catálogo.

</details>

---

[← Inicio](../README.md) · [Primer módulo: 00](00_getting_started/README.md) · [Primera lección →](00_getting_started/01_github_profile/README.md)

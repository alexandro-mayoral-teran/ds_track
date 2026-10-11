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
- Práctica: `pip` para comprender el estándar de instalación.
- Extensión: `uv` para administrar el proyecto Python.
- Extensión: Git y GitHub para historial y publicación.

**Orden recomendado:** Git y GitHub → Markdown → perfil desde la web → terminal
y rutas → actualización del perfil con Git → primer script → entorno y
dependencias → primer notebook.

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

- Tipos, colecciones, control de flujo y funciones.
- Módulos, archivos, excepciones y comprensión de iterables.
- Lectura de CSV y JSON con la biblioteca estándar.
- Separación entre entrada, transformación y salida.

**Criterio de salida:** leer registros crediticios, validarlos y producir un
resumen mediante funciones pequeñas y reutilizables.

## Nivel 2 — pandas

**Objetivo:** dominar el modelo mental de DataFrame y el análisis tabular.

- Series, DataFrames, selección, filtrado y tipos.
- Faltantes, duplicados, fechas y texto.
- Agregaciones, `groupby`, `merge`, reshape y ventanas básicas.
- Visualización y uso responsable de notebooks.

**Proyecto asociado:** `01_clean_credit_data`.

**Criterio de salida:** limpiar una cartera en CSV y justificar cada regla de
calidad aplicada.

## Nivel 3 — SQL y bases de datos

**Objetivo:** consultar y modelar datos persistentes.

- Modelo relacional, tablas, llaves, restricciones y normalización.
- Consultas, joins, CTE, subconsultas y funciones de ventana.
- Índices, transacciones y planes de consulta.
- SQLite primero; PostgreSQL como extensión.

**Proyecto asociado:** `02_credit_database`.

**Criterio de salida:** diseñar un modelo relacional y obtener indicadores de
cartera mediante consultas verificables.

## Nivel 4 — R fundamental

**Objetivo:** trasladar conceptos de análisis al ecosistema de R.

- Vectores, listas, data frames, funciones y paquetes.
- Importación, transformación y visualización inicial.
- Proyectos reproducibles con `renv`.
- Equivalencias entre pandas y R.

**Criterio de salida:** reproducir en R un análisis conocido de Python sin
traducir mecánicamente cada línea.

## Nivel 5 — tidyverse y comunicación visual

**Objetivo:** realizar análisis expresivos y comunicar hallazgos.

- `dplyr`, `tidyr`, `stringr` y manejo de fechas.
- `ggplot2`, escalas, facetas y diseño de gráficas.
- Acceso a SQL y archivos desde R.

**Proyecto asociado:** `03_portfolio_analysis_r`.

**Criterio de salida:** producir un análisis de cartera entendible por una
persona que no escribió el código.

## Nivel 6 — Arrow y Parquet

**Objetivo:** comprender almacenamiento columnar y datasets mayores.

- Esquemas, tipos, compresión y metadatos.
- Row groups, particiones y estadísticas.
- Projection y predicate pushdown.
- Problema de archivos pequeños y evolución de esquemas.
- Interoperabilidad entre Python, R y motores SQL.

**Criterio de salida:** convertir CSV a un dataset Parquet bien tipado y
particionado, y explicar por qué se eligió ese diseño.

## Nivel 7 — Polars y DuckDB

**Objetivo:** procesar datos grandes en una sola máquina con criterio.

- Ejecución eager y lazy en Polars.
- Consultas SQL sobre Parquet con DuckDB.
- Procesamiento por lotes y cargas mayores que memoria.
- Benchmarks frente a pandas: tiempo, memoria y legibilidad.

**Proyecto asociado:** `04_large_credit_dataset`.

**Criterio de salida:** resolver el mismo problema con pandas, Polars y DuckDB,
y escoger una herramienta usando mediciones.

## Nivel 8 — Reportes reproducibles

**Objetivo:** transformar análisis en productos consumibles.

- Narrativa, tablas, gráficas y parámetros.
- Quarto con Python y R.
- Salidas HTML y PDF.
- Dashboards estáticos y automatización de reportes.

**Proyecto asociado:** `05_monthly_report`.

**Criterio de salida:** generar nuevamente un reporte completo partiendo de los
datos y el código, sin edición manual de resultados.

## Nivel 9 — Shiny y fundamentos web

**Objetivo:** convertir un análisis estable en una aplicación interactiva.

- Cliente, servidor, HTTP, HTML y CSS básicos.
- UI, servidor, estado y reactividad en Shiny.
- Inputs, outputs, validaciones y módulos.
- Lectura desde Parquet o una base de datos.

**Proyecto asociado:** `06_shiny_portfolio_app`.

**Criterio de salida:** construir un explorador de cartera con filtros y
mensajes de error comprensibles, sin mezclar la UI con las transformaciones.

## Nivel 10 — Proyecto reproducible

**Objetivo:** integrar el recorrido con prácticas de ingeniería.

- Código modular, configuración y logging.
- Pruebas unitarias, de integración y de calidad de datos.
- Pipelines idempotentes y reprocesamiento.
- Separación raw/clean/analytics.
- Secretos, PII y publicación segura.
- Automatización con Git como extensión.

**Criterio de salida:** reconstruir datos, métricas y producto final a partir de
instrucciones documentadas y datos sintéticos.

## Temas estacionados

Se investigarán después de completar los niveles esenciales:

- Orquestadores como Dagster o Prefect.
- Almacenamiento de objetos compatible con S3.
- dbt o SQLMesh.
- Apache Iceberg y conceptos lakehouse.
- Spark y procesamiento distribuido.
- APIs con Plumber o FastAPI.

Estar en esta lista no significa que el tema sea poco importante; significa que
todavía no resuelve una limitación encontrada durante la ruta principal.

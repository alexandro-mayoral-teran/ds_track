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

**Criterio de salida:** leer registros crediticios, validarlos y producir un
resumen mediante funciones pequeñas y reutilizables.

## Nivel 2 — pandas

**Objetivo:** dominar el modelo mental de DataFrame y el análisis tabular.

- Series, DataFrames, selección, filtrado y tipos.
- Faltantes, duplicados, fechas y texto.
- Agregaciones, `groupby`, `merge`, reshape y ventanas básicas.
- Visualización inicial: una gráfica sencilla y una explicación de sus hallazgos.
- Uso responsable de notebooks; comprobaciones de filas, llaves y totales antes
  y después de transformar o unir datos.

**Proyecto asociado:** `01_clean_credit_data`.

**Criterio de salida:** limpiar una cartera en CSV y justificar cada regla de
calidad aplicada, presentar una gráfica e interpretar sus resultados.

## Nivel 3 — SQL y bases de datos

**Objetivo:** consultar y modelar datos persistentes.

- Esencial: modelo relacional, tablas, llaves, restricciones y normalización básica.
- Esencial: selección, filtros, agregaciones y joins con SQLite.
- Práctica: CTE, subconsultas y ventanas básicas para preguntas concretas.
- Esencial: comprender transacciones al escribir datos y verificar los indicadores.
- Avanzado: índices, planes de consulta y optimización cuando exista una limitación.
- Extensión: PostgreSQL después de dominar las operaciones en SQLite.

**Proyecto asociado:** `02_credit_database`.

**Criterio de salida:** diseñar un modelo relacional y obtener indicadores de
cartera mediante consultas verificables.

**Cierre antes de R:** integrar lo aprendido en un análisis pequeño: leer datos
con Python, limpiar con pandas, consultar indicadores en SQLite y explicar una
gráfica. Reutilizar los proyectos de limpieza y base de datos, sin crear un
proyecto adicional obligatorio. Conciliar al menos un indicador entre pandas
y SQL y conservar instrucciones de ejecución.

## Nivel 4 — R fundamental

**Objetivo:** trasladar conceptos de análisis al ecosistema de R.

**Prerrequisito:** el análisis de cierre del nivel 3. Reutilizar sus preguntas y
datos para aprender el modelo de R sobre un problema conocido.

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

- Esencial: leer y escribir Parquet; comprender tipos, esquemas y almacenamiento columnar.
- Práctica: comparar CSV y Parquet en tamaño, tipos y lectura selectiva.
- Práctica: compresión, metadatos, row groups y pushdown con ejemplos pequeños.
- Extensión: particiones cuando las preguntas y el volumen las justifiquen.
- Avanzado: archivos pequeños y evolución de esquemas.
- Práctica: interoperabilidad entre Python, R y motores SQL.

**Criterio de salida:** convertir un CSV a Parquet bien tipado, comprobar que
conserva registros e indicadores y explicar el diseño. Particionar solo cuando
se pueda justificar; no es requisito para el primer ejercicio.

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

Este nivel formaliza la comunicación iniciada con gráficas e interpretación en
pandas y tidyverse; no es la primera ocasión de explicar resultados.

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

La validación, documentación y separación de pasos se practican desde Python.
Aquí se profundiza en pruebas y automatización y se integran en un proyecto final.

- Código modular, configuración y logging.
- Pruebas unitarias, de integración y de calidad de datos.
- Pipelines idempotentes y reprocesamiento.
- Separación raw/clean/analytics.
- Secretos, PII y publicación segura.
- Automatización con Git como extensión.

**Criterio de salida:** reconstruir datos, métricas y producto final a partir de
instrucciones documentadas y datos sintéticos.

## Temas estacionados

Las rutas previstas de **Python aplicado** y **visualización en Python y R**
se detallan en [la arquitectura](docs/architecture.md#rutas-de-profundización-previstas).
Incluyen clases, decoradores y robustez después de las bases, Matplotlib y
Altair para gráficos, ggplot2 para R y Streamlit como alternativa de aplicación
Python al recorrido de Shiny. Se incorporarán según sus prerrequisitos, sin
renumerar los niveles ni bloquear el avance a pandas.

Se investigarán después de completar los niveles esenciales:

- Orquestadores como Dagster o Prefect.
- Almacenamiento de objetos compatible con S3.
- dbt o SQLMesh.
- Apache Iceberg y conceptos lakehouse.
- Spark y procesamiento distribuido.
- APIs con Plumber o FastAPI.

Estar en esta lista no significa que el tema sea poco importante; significa que
todavía no resuelve una limitación encontrada durante la ruta principal.

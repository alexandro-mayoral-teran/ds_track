# 11 — Reportes con Quarto

## Propósito y prerrequisitos

Convertir el análisis conocido en un reporte que reúna contexto, tablas,
figuras e interpretación, y que pueda regenerarse sin editar resultados a mano.
Completa [10 — Polars y DuckDB](../10_polars_duckdb/README.md) como prerrequisito
conceptual. Las lecciones incluyen datos completos y no exigen entregas personales previas.

**Estado:** 11.01–11.06 disponibles con lecciones, datos, preparadores Python/R
y labs. 11.07–11.09 conservan su alcance previsto; sus lecciones y labs siguen pendientes.

La teoría del documento se explica una vez. Hay recorridos separados para
Python/Jupyter y R/knitr: elige un motor para el reporte esencial y compara el
otro como ampliación. No se exige mezclar ambos intérpretes en un documento.
Quarto se instala como herramienta; no sustituye Python, R o sus dependencias.
El [cierre 10.10](../10_polars_duckdb/10_closure_tool_choice/README.md) ya ofrece
tablas verificables, pregunta, método y límites como posible entrada del reporte.
La 11.01 empieza con una muestra propia pequeña y una preparación editorial;
no instala Quarto ni genera todavía un `.qmd` o HTML.
La 11.02 crea/renderiza HTML con Quarto 1.9.38 y conserva una secuencia de dos
pasos: preparación calculada Python/R y render de texto. Ejecución dentro del
documento con Jupyter/knitr ya está disponible en 11.03, con entornos comprobados.

## Orden de desarrollo

| Orden | Sección | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Reporte, fuente y renderizado](01_report_source_render/README.md) | Esencial disponible | Distinguir documento fuente y resultado generado |
| 2 | [Primer documento Quarto](02_first_document/README.md) | Esencial disponible | Crear un .qmd y renderizar HTML |
| 3 | [Ejecución con Python o R](03_execution_python_r/README.md) | Esencial disponible | Regenerar datos y resultados en el entorno correcto |
| 4 | [Tablas, figuras y referencias](04_tables_figures_references/README.md) | Esencial disponible | Relacionar evidencia y narrativa |
| 5 | [Parámetros y cortes](05_parameters_cutoffs/README.md) | Práctica disponible | Generar dos reportes desde una misma fuente |
| 6 | [Proyectos, caché y freeze](06_projects_cache_freeze/README.md) | Práctica disponible | Controlar cuándo se recalculan resultados |
| 7 | [Formatos y revisión visual](#07-formatos-y-revision-visual) | Práctica | Entregar HTML legible; PDF como ampliación |
| 8 | [Dashboard y distribución](#08-dashboard-y-distribucion) | Extensión | Organizar vistas sin exigir una app con servidor |
| 9 | [Cierre del reporte reproducible](#09-cierre-del-reporte-reproducible) | Práctica de cierre | Reconstruir y comprobar un reporte por corte |

## Alcance de cada sección

<a id="01-reporte-fuente-y-renderizado"></a>

### 01 — Reporte, fuente y renderizado

- Pregunta, público y estructura: contexto, método, hallazgos y límites.
  Fuente .qmd, entradas, archivos generados y diferencia con un notebook exploratorio.
- [Lección disponible](01_report_source_render/README.md), muestra propia de seis
  filas, preparadores Python estándar/R base y
  [lab 11.01](../../labs/11_reporting_quarto/01_report_source_render/README.md).
  Narrativa calculada: tres créditos, 6000/6300 MXN, +300 y 5% sobre septiembre.
  Cambio de entrada, base cero y distinción entre leer, regenerar y renderizar.

<a id="02-primer-documento-quarto"></a>

### 02 — Primer documento Quarto

- Markdown, encabezado YAML, título, formato y bloques de código; preview y render.
  Distinguir CLI Quarto de la extensión del editor.
- [Lección disponible](02_first_document/README.md), primer archivo completo,
  muestra propia, preparadores Python/R y
  [lab 11.02](../../labs/11_reporting_quarto/02_first_document/README.md).
  YAML/Markdown, código mostrado, render/preview, HTML con recursos incluidos y
  actualización en dos fases. Cifras calculadas antes del render; sin Jupyter/knitr aún.

<a id="03-ejecucion-con-python-o-r"></a>

### 03 — Ejecución con Python o R

- Python/Jupyter: kernel y entorno. R/knitr: proyecto, librería y renv.
  Reutilizar funciones y entradas del análisis en lugar de depender de una sesión previa.
- [Lección disponible](03_execution_python_r/README.md), CSV propio, funciones,
  documentos ejecutables, preparadores y
  [lab 11.03](../../labs/11_reporting_quarto/03_execution_python_r/README.md).
  Jupyter/Python o knitr/R, versiones fijadas, cálculo durante el render,
  comprobación del entorno real y detección de entradas/funciones ausentes.

<a id="04-tablas-figuras-y-referencias"></a>

### 04 — Tablas, figuras y referencias

- Tablas, captions, identificadores, referencias cruzadas, notas de fuente y
  cifras dentro del texto generadas desde resultados. Mostrar código solo cuando ayude.
- [Lección disponible](04_tables_figures_references/README.md), mínimo estático,
  CSV propio, reportes Python/R, preparadores y
  [lab 11.04](../../labs/11_reporting_quarto/04_tables_figures_references/README.md).
  Párrafo calculado, tabla/figura enlazadas, procedencia y cita bibliográfica;
  un mismo resultado, sin dependencias nuevas ni cambios de lockfiles.

<a id="05-parametros-y-cortes"></a>

### 05 — Parámetros y cortes

- Parámetros compatibles con el motor elegido y controles de corte/segmento.
  Nombres de salida explícitos y verificación del universo usado.
- [Lección disponible](05_parameters_cutoffs/README.md), mínimos autónomos, CSV
  de siete filas, funciones/reportes Python/R, YAML por corte, preparadores y
  [lab 11.05](../../labs/11_reporting_quarto/05_parameters_cutoffs/README.md).
  Dos reportes desde el mismo cálculo: septiembre 2/5000 MXN de 3/6000, octubre
  1/3300 de 4/7000, con mínimo de 2000 MXN. Parámetros efectivos visibles,
  selección vacía, frontera inclusiva y corte ausente distinguidos. Papermill
  2.7.0 declarado en notebooks; entorno R y sus metadatos conservados.

<a id="06-proyectos-cache-y-freeze"></a>

### 06 — Proyectos, caché y freeze

- _quarto.yml, rutas de proyecto, opciones de ejecución y resultados reutilizados.
  Diferenciar caché de ejecución y freeze; definir cuándo recalcular por cambios en datos.
- [Lección disponible](06_projects_cache_freeze/README.md), proyecto con rutas
  explícitas, CSV completo, reportes/preparadores Python/R y
  [lab 11.06](../../labs/11_reporting_quarto/06_projects_cache_freeze/README.md).
  Experimentos separados de caché y freeze; recálculo ante cambios de datos,
  documento, funciones y parámetros. Verificador de solo lectura por fila;
  jupyter-cache 1.0.1 en notebooks, sin nuevas dependencias R.

<a id="07-formatos-y-revision-visual"></a>

### 07 — Formatos y revisión visual

- HTML como formato esencial; navegación, tablas anchas, etiquetas y accesibilidad.
  PDF como extensión con su motor y dependencias adicionales explícitas.
- Práctica prevista: revisar el archivo final, corregir cortes o desbordamientos
  y comprobar que las cifras coinciden con las salidas verificadas.

<a id="08-dashboard-y-distribucion"></a>

### 08 — Dashboard y distribución

- Layout de dashboard con tarjetas, tablas y figuras precomputadas; distinguir
  interacción del navegador de una aplicación con ejecución de servidor.
- Práctica prevista: distribuir una salida local con sus recursos. Publicación
  en un servicio o sitio es opcional; no exige cuenta, despliegue ni datos privados.

<a id="09-cierre-del-reporte-reproducible"></a>

### 09 — Cierre del reporte reproducible

- Integrar código, parámetros, fuentes, dependencias y comprobaciones en un
  reporte regenerable, indicando qué archivos se producen.
- Práctica prevista: reconstruir un corte y verificar cifras, figuras y narrativa
  sin editar manualmente resultados. Basta un motor y una salida HTML para el cierre.

## Prácticas, proyecto y criterio de salida

Los labs [11.01](../../labs/11_reporting_quarto/01_report_source_render/README.md),
[11.02](../../labs/11_reporting_quarto/02_first_document/README.md),
[11.03](../../labs/11_reporting_quarto/03_execution_python_r/README.md),
[11.04](../../labs/11_reporting_quarto/04_tables_figures_references/README.md),
[11.05](../../labs/11_reporting_quarto/05_parameters_cutoffs/README.md) y
[11.06](../../labs/11_reporting_quarto/06_projects_cache_freeze/README.md)
están disponibles. Los labs 11.07–11.09 siguen previstos, con 11.08 opcional.
El proyecto previsto 05_monthly_report figura en [proyectos](../../projects/README.md),
sin carpeta ni checkpoints implementados.

Checkpoints propuestos: CP-01, documento y ejecución (01–03); CP-02, evidencia y
parámetros (04–05); CP-03, render actualizado y revisión final (06–07 y 09).
PDF, dashboards y publicación ampliarán el producto sin bloquear su cierre.

Podrás avanzar cuando otra persona pueda reconstruir el HTML con las mismas
entradas, y cuando sus cifras y referencias correspondan al corte declarado.
La comunicación comenzó en módulos anteriores; aquí se formaliza la entrega.

## Continuidad y referencias

Después elige [12 — Streamlit](../12_streamlit/README.md) para Python o
[13 — Shiny](../13_shiny_web/README.md) para R. Basta completar una aplicación
antes de [14 — Proyecto reproducible](../14_reproducible_projects/README.md).

Fuentes oficiales: [inicio](https://quarto.org/docs/get-started/),
[Python](https://quarto.org/docs/computations/python.html),
[R](https://quarto.org/docs/computations/r.html),
[opciones de ejecución](https://quarto.org/docs/computations/execution-options.html),
[parámetros](https://quarto.org/docs/computations/parameters.html),
[gestión de ejecución](https://quarto.org/docs/projects/code-execution.html),
[PDF](https://quarto.org/docs/output-formats/pdf-basics.html) y
[dashboards](https://quarto.org/docs/dashboards/).
Las versiones y requisitos se elegirán al implementar cada recorrido.

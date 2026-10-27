# 11 — Reportes con Quarto

[Inicio](../../README.md) / [Módulos](../README.md) / **11 — Reportes con Quarto**

**Reúne análisis y narrativa en un reporte que otra persona reconstruya.**

[**Empezar por 11.01 →**](01_report_source_render/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Convertir un análisis conocido en un reporte con contexto, tablas, figuras, interpretación y límites, regenerado desde fuentes y parámetros explícitos.

## Antes de empezar

Completa [10 — Polars y DuckDB](../10_polars_duckdb/README.md) como prerrequisito conceptual. Los ejemplos incluyen entradas completas sin exigir entregas personales previas. Quarto es una herramienta adicional; no sustituye Python o R ni sus dependencias.

## Qué vas a aprender

- Distinguir fuentes, ejecución y resultados generados.
- Combinar cifras, tablas, figuras y referencias del mismo análisis.
- Controlar parámetros, rutas, caché y recálculo.
- Revisar un HTML y reconstruir una entrega contra referencia externa.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **11.01** · [Reporte, fuente y renderizado](01_report_source_render/README.md) | [Lab 11.01](../../labs/11_reporting_quarto/01_report_source_render/README.md) | Distinguir documento fuente y resultado generado |
| **11.02** · [Primer documento Quarto](02_first_document/README.md) | [Lab 11.02](../../labs/11_reporting_quarto/02_first_document/README.md) | Crear un .qmd y renderizar HTML |
| **11.03** · [Ejecución con Python o R](03_execution_python_r/README.md) | [Lab 11.03](../../labs/11_reporting_quarto/03_execution_python_r/README.md) | Regenerar datos y resultados en el entorno correcto |
| **11.04** · [Tablas, figuras y referencias](04_tables_figures_references/README.md) | [Lab 11.04](../../labs/11_reporting_quarto/04_tables_figures_references/README.md) | Relacionar evidencia y narrativa |
| **11.05** · [Parámetros y cortes](05_parameters_cutoffs/README.md) | [Lab 11.05](../../labs/11_reporting_quarto/05_parameters_cutoffs/README.md) | Generar dos reportes desde una misma fuente |
| **11.06** · [Proyectos, caché y freeze](06_projects_cache_freeze/README.md) | [Lab 11.06](../../labs/11_reporting_quarto/06_projects_cache_freeze/README.md) | Controlar cuándo se recalculan resultados |
| **11.07** · [Formatos y revisión visual](07_formats_visual_review/README.md) | [Lab 11.07](../../labs/11_reporting_quarto/07_formats_visual_review/README.md) | Entregar HTML legible; PDF como ampliación |
| **11.08** · [Dashboard y distribución](08_dashboard_distribution/README.md) — opcional | [Lab 11.08](../../labs/11_reporting_quarto/08_dashboard_distribution/README.md) | Organizar vistas sin exigir una app con servidor |
| **11.09** · [Cierre del reporte reproducible](09_reproducible_report_closure/README.md) | [Lab 11.09](../../labs/11_reporting_quarto/09_reproducible_report_closure/README.md) | Reconstruir y comprobar un reporte por corte |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

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
- [Lección disponible](07_formats_visual_review/README.md) y
  [lab 11.07](../../labs/11_reporting_quarto/07_formats_visual_review/README.md),
  mínimo estático, reportes Python/R, CSS y verificador de solo lectura.
  Texto/tablas/barras conciliados; navegación, foco y tabla ancha comprobados
  en navegador a tres anchos. HTML esencial; PDF opcional con límite del
  entorno documentado, sin nuevas dependencias ni metadatos.

<a id="08-dashboard-y-distribucion"></a>

### 08 — Dashboard y distribución

- Layout de dashboard con tarjetas, tablas y figuras precomputadas; distinguir
  interacción del navegador de una aplicación con ejecución de servidor.
- [Lección disponible](08_dashboard_distribution/README.md) y
  [lab 11.08](../../labs/11_reporting_quarto/08_dashboard_distribution/README.md),
  mínimo, muestra completa, dashboards/preparadores Python/R y distribuidores.
  Tarjetas, tabla y figura conciliadas; pestañas en navegador sin servidor.
  Copia local con recursos incorporados, nota de lectura y destino protegido;
  revisión sin conexión, a tres anchos y con teclado, sin paquetes nuevos.
  Publicación en un servicio sigue siendo una ampliación no implementada.

<a id="09-cierre-del-reporte-reproducible"></a>

### 09 — Cierre del reporte reproducible

- Integrar código, parámetros, fuentes, dependencias y comprobaciones en un
  reporte regenerable, indicando qué archivos se producen.
- [Lección disponible](09_reproducible_report_closure/README.md) y
  [lab 11.09](../../labs/11_reporting_quarto/09_reproducible_report_closure/README.md):
  entrega completa, copia de solo fuentes y reconstrucción; referencia externa
  por clave, parámetros explícitos y texto/tablas/barras conciliados. Un motor
  y HTML bastan. Sin dependencias nuevas ni cambios de lockfiles.

</details>

## Cómo trabajar este módulo

Elige Python/Jupyter o R/knitr para el reporte esencial; el otro motor es ampliación. Un motor y HTML bastan. 11.08 es opcional; PDF, dashboards y publicación no bloquean el cierre. La ejecución se comprueba además desde una sesión nueva y con cambios deliberados de datos/parámetros.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Fuentes y parámetros | Qué entrada y corte se solicitaron |
| HTML, tablas y figuras | Coherencia de narrativa y valores |
| Entorno, instrucciones y referencia | Reconstrucción por otra persona y límites de las huellas |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Otra persona puede reconstruir el HTML con las mismas entradas y contrastar sus cifras y referencias. Explica los parámetros efectivos y detecta una discrepancia sin editar resultados manualmente.

05_monthly_report está previsto en [proyectos](../../projects/README.md), sin carpeta ni checkpoints implementados. Consulta [los criterios de cierre](../../docs/reporting-closure.md).

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, documento y ejecución (01–03); CP-02, evidencia y
parámetros (04–05); CP-03, render actualizado y revisión final (06–07 y 09).
PDF, dashboards y publicación ampliarán el producto sin bloquear su cierre.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 11.01](01_report_source_render/README.md) y realiza su lab.

Al cerrar, elige [12 — Streamlit](../12_streamlit/README.md) o [13 — Shiny](../13_shiny_web/README.md). Ambas rutas están planificadas; basta una antes de 14.

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Fuentes oficiales: [inicio](https://quarto.org/docs/get-started/),
[Python](https://quarto.org/docs/computations/python.html),
[R](https://quarto.org/docs/computations/r.html),
[opciones de ejecución](https://quarto.org/docs/computations/execution-options.html),
[parámetros](https://quarto.org/docs/computations/parameters.html),
[gestión de ejecución](https://quarto.org/docs/projects/code-execution.html),
[PDF](https://quarto.org/docs/output-formats/pdf-basics.html) y
[dashboards](https://quarto.org/docs/dashboards/).
Las versiones y requisitos se elegirán al implementar cada recorrido.

### Apoyos relacionados

- [cierre 10.10](../10_polars_duckdb/10_closure_tool_choice/README.md)
- [14 — Proyecto reproducible](../14_reproducible_projects/README.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_report_source_render/README.md)

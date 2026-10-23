# 11 — Reportes con Quarto

## Propósito y prerrequisitos

Convertir el análisis conocido en un reporte que reúna contexto, tablas,
figuras e interpretación, y que pueda regenerarse sin editar resultados a mano.
Completa [10 — Polars y DuckDB](../10_polars_duckdb/README.md) y reutiliza
sus datos e indicadores verificados.

**Estado:** nueve secciones planificadas; lecciones, ejemplos y labs por desarrollar.
Los enlaces internos describen el alcance previsto.

La teoría del documento se explica una vez. Habrá recorridos separados para
Python/Jupyter y R/knitr: elige un motor para el reporte esencial y compara el
otro como ampliación. No se exige mezclar ambos intérpretes en un documento.
Quarto se instala como herramienta; no sustituye Python, R o sus dependencias.
El [cierre 10.10](../10_polars_duckdb/10_closure_tool_choice/README.md) ya ofrece
tablas verificables, pregunta, método y límites como posible entrada del reporte.
Al desarrollar las lecciones se presentarán ejemplos completos sin exigir
entregas personales anteriores. Ese enlace no implementa aún las secciones de 11.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Reporte, fuente y renderizado](#01-reporte-fuente-y-renderizado) | Esencial | Distinguir documento fuente y resultado generado |
| 2 | [Primer documento Quarto](#02-primer-documento-quarto) | Esencial | Crear un .qmd y renderizar HTML |
| 3 | [Ejecución con Python o R](#03-ejecucion-con-python-o-r) | Esencial | Regenerar datos y resultados en el entorno correcto |
| 4 | [Tablas, figuras y referencias](#04-tablas-figuras-y-referencias) | Esencial | Relacionar evidencia y narrativa |
| 5 | [Parámetros y cortes](#05-parametros-y-cortes) | Práctica | Generar dos reportes desde una misma fuente |
| 6 | [Proyectos, caché y freeze](#06-proyectos-cache-y-freeze) | Práctica | Controlar cuándo se recalculan resultados |
| 7 | [Formatos y revisión visual](#07-formatos-y-revision-visual) | Práctica | Entregar HTML legible; PDF como ampliación |
| 8 | [Dashboard y distribución](#08-dashboard-y-distribucion) | Extensión | Organizar vistas sin exigir una app con servidor |
| 9 | [Cierre del reporte reproducible](#09-cierre-del-reporte-reproducible) | Práctica de cierre | Reconstruir y comprobar un reporte por corte |

## Alcance de cada sección

<a id="01-reporte-fuente-y-renderizado"></a>

### 01 — Reporte, fuente y renderizado

- Pregunta, público y estructura: contexto, método, hallazgos y límites.
  Fuente .qmd, entradas, archivos generados y diferencia con un notebook exploratorio.
- Práctica prevista: ordenar los resultados conocidos en una narrativa sin
  introducir otro análisis ni copiar indicadores manualmente.

<a id="02-primer-documento-quarto"></a>

### 02 — Primer documento Quarto

- Markdown, encabezado YAML, título, formato y bloques de código; preview y render.
  Distinguir CLI Quarto de la extensión del editor.
- Práctica prevista: un documento mínimo HTML con texto y resultado calculado;
  comprobar archivos y recursos necesarios para abrirlo en otro equipo.

<a id="03-ejecucion-con-python-o-r"></a>

### 03 — Ejecución con Python o R

- Python/Jupyter: kernel y entorno. R/knitr: proyecto, librería y renv.
  Reutilizar funciones y entradas del análisis en lugar de depender de una sesión previa.
- Práctica prevista: renderizar desde cero y detectar una dependencia o archivo
  faltante. Explicar qué se ejecutó; no ocultar una falla para conservar un reporte viejo.

<a id="04-tablas-figuras-y-referencias"></a>

### 04 — Tablas, figuras y referencias

- Tablas, captions, identificadores, referencias cruzadas, notas de fuente y
  cifras dentro del texto generadas desde resultados. Mostrar código solo cuando ayude.
- Práctica prevista: explicar un indicador y enlazar su tabla/figura, incluyendo
  unidades, corte, población y limitaciones de interpretación.

<a id="05-parametros-y-cortes"></a>

### 05 — Parámetros y cortes

- Parámetros compatibles con el motor elegido y controles de corte/segmento.
  Nombres de salida explícitos y verificación del universo usado.
- Práctica prevista: generar dos reportes con la misma fuente, conciliando sus
  indicadores con los datos de cada corte. La sintaxis se comprobará por motor.

<a id="06-proyectos-cache-y-freeze"></a>

### 06 — Proyectos, caché y freeze

- _quarto.yml, rutas de proyecto, opciones de ejecución y resultados reutilizados.
  Diferenciar caché de ejecución y freeze; definir cuándo recalcular por cambios en datos.
- Práctica prevista: cambiar una entrada y demostrar que el reporte publicado
  contiene el resultado actualizado. Un render exitoso con salidas reutilizadas
  no prueba que los datos se hayan vuelto a procesar.

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

Se prevén labs 11.01–11.09, con 11.08 opcional. Aún no existen.
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

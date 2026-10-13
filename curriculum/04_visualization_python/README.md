# 04 — Visualización en Python

## Propósito y prerrequisitos

Comunicar resultados ya comprobados: elegir una representación, construirla,
interpretarla y conservar el código que la produce. Reutilizar datos e indicadores
de [pandas](../02_pandas/README.md) y [SQL](../03_sql_databases/README.md).

**Estado:** [01 — Pregunta y elección de gráfico](01_question_chart/README.md)
y su lab están disponibles, con vistas comprobadas y práctica de justificación.
[02 — Matplotlib: Figure y Axes](02_figure_axes/README.md) y su lab también están disponibles.
[03 — Comparaciones y evolución](03_comparisons_evolution/README.md) y su lab están disponibles.
Las secciones 04–09 siguen planificadas; sus enlaces internos describen el alcance.

Pandas ya introduce una primera gráfica. Aquí profundizaremos primero con
Matplotlib y después con Altair. No repetiremos la limpieza para cada biblioteca.
Instalación y versiones se explicarán al introducir cada herramienta.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta y elección de gráfico](01_question_chart/README.md) | Esencial | Justificar una representación según la pregunta |
| 2 | [Matplotlib: Figure y Axes](02_figure_axes/README.md) | Esencial | Crear y guardar una figura desde código |
| 3 | [Comparaciones y evolución](03_comparisons_evolution/README.md) | Esencial | Construir barras y líneas con unidades |
| 4 | [Distribuciones y relaciones](#04-distribuciones-y-relaciones) | Esencial | Interpretar dispersión y variabilidad |
| 5 | [Escalas, etiquetas y accesibilidad](#05-escalas-etiquetas-y-accesibilidad) | Esencial | Revisar una figura que puede inducir a error |
| 6 | [Composición y exportación](#06-composicion-y-exportacion) | Práctica | Comparar vistas y producir una figura legible |
| 7 | [Altair: visualización declarativa](#07-altair-visualizacion-declarativa) | Práctica | Expresar datos, marcas y codificaciones |
| 8 | [Interacción con Altair](#08-interaccion-con-altair) | Extensión | Explorar un indicador con filtros o selección |
| 9 | [Cierre visual del análisis](#09-cierre-visual-del-analisis) | Práctica de cierre | Entregar figuras reconstruibles e interpretación |

## Alcance de cada sección

<a id="01-pregunta-y-eleccion-de-grafico"></a>

### 01 — Pregunta y elección de gráfico

- Comparar categorías, evolución, distribución y relación; identificar población,
  unidad de análisis y agregación. Distinguir observación de explicación causal.
- Práctica prevista: proponer gráficos para preguntas sobre saldo, cortes y segmentos,
  justificando la elección antes de escribir código.

<a id="02-matplotlib-figure-y-axes"></a>

### 02 — Matplotlib: Figure y Axes

- Figure como contenedor y Axes como área de representación; usar subplots y la
  interfaz de objetos para controlar una figura, sin depender del estado anterior.
- Práctica prevista: reconstruir la gráfica inicial, etiquetar y guardar la salida.

<a id="03-comparaciones-y-evolucion"></a>

### 03 — Comparaciones y evolución

- Barras, orden de categorías y líneas por fecha; valores absolutos frente a tasas.
- Práctica prevista: comparar segmentos y cortes, revisando períodos faltantes,
  denominadores y unidades antes de interpretar una tendencia.

<a id="04-distribuciones-y-relaciones"></a>

### 04 — Distribuciones y relaciones

- Histogramas, intervalos, boxplots y dispersión; distinguir resumen y detalle.
- Práctica prevista: describir variabilidad y casos extremos sin confundir
  correlación con causalidad ni eliminar observaciones por su apariencia.

<a id="05-escalas-etiquetas-y-accesibilidad"></a>

### 05 — Escalas, etiquetas y accesibilidad

- Límites de ejes, escala lineal/logarítmica y sus condiciones; bases de comparación.
  Títulos informativos, leyendas, formatos y paletas legibles.
- Práctica prevista: corregir una figura engañosa y explicar qué cambió. Usar
  señales adicionales al color y documentar incertidumbre o cobertura limitada.

<a id="06-composicion-y-exportacion"></a>

### 06 — Composición y exportación

- Vistas múltiples, ejes comparables, anotaciones y espacio para etiquetas.
  PNG/SVG, tamaño y resolución según el destino; cierre de figuras al generar varias.
- Práctica prevista: una figura para compartir con fuente, corte y comentario breve.

<a id="07-altair-visualizacion-declarativa"></a>

### 07 — Altair: visualización declarativa

- Chart, marcas y canales; tipos nominal, ordinal, cuantitativo y temporal.
  Diferenciar representar datos preparados de agregarlos dentro de la gráfica.
- Práctica prevista: representar el mismo indicador de Matplotlib y comprobar
  que ambas vistas muestran la misma población, agregación y unidades.

<a id="08-interaccion-con-altair"></a>

### 08 — Interacción con Altair

- Parámetros, selecciones, condiciones, filtros y tooltips con la API vigente.
- Práctica prevista: seleccionar un segmento y mantener explícito qué muestra
  el resultado. Revisar exportación y recursos necesarios para compartirlo.
  Esta ampliación no exige construir una aplicación Streamlit.

<a id="09-cierre-visual-del-analisis"></a>

### 09 — Cierre visual del análisis

- Integrar datos verificados, código de gráficos y una interpretación escrita.
- Práctica prevista: reconstruir al menos una figura estática, comparar una vista
  Altair y explicar hallazgo, población y límites. Interacción opcional.

## Prácticas, integración y criterio de salida

Se prevén labs 04.01–04.09; el 04.08 será opcional.
El [lab 04.01](../../labs/04_visualization_python/01_question_chart/README.md)
y el [lab 04.02](../../labs/04_visualization_python/02_figure_axes/README.md)
y el [lab 04.03](../../labs/04_visualization_python/03_comparisons_evolution/README.md)
están disponibles; 04.04–04.09 siguen pendientes.
Se ampliarán los productos previstos en [proyectos](../../projects/README.md)
01_clean_credit_data y 02_credit_database, sin crear un proyecto adicional obligatorio.

Checkpoint visual propuesto: conservar una tabla de indicadores conciliados,
una figura estática, una vista declarativa y una interpretación. El nombre del
checkpoint se concretará en esos proyectos al implementar el material.

Para avanzar debes justificar la representación, revisar escalas y unidades y
reconstruir la figura desde los datos. Diseñar interacción avanzada no es requisito.
Streamlit pertenece al módulo 12; estadística inferencial y modelado no se
presuponen para describir una muestra.

## Continuidad y referencias

Continúa con [05 — Python aplicado](../05_python_applied/README.md), reutilizando
este análisis para organizar su código.

La progresión se apoya en [Figure/Axes e interfaces de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html)
y en [parámetros e interacción de Altair](https://altair-viz.github.io/user_guide/interactions/parameters.html).
Consultar también [los canales de Altair](https://altair-viz.github.io/user_guide/encodings/index.html)
al desarrollar la representación declarativa.

# 04 — Visualización en Python

[Inicio](../../README.md) / [Módulos](../README.md) / **04 — Visualización en Python**

**Convierte resultados comprobados en gráficas que puedas explicar.**

[**Empezar por 04.01 →**](01_question_chart/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Elegir, construir, revisar e interpretar representaciones visuales sobre datos ya comprobados. Primero trabaja con Matplotlib y después con Altair, conservando la pregunta y los indicadores.

## Antes de empezar

Completa [03 — SQL](../03_sql_databases/README.md) y conserva las bases de [pandas](../02_pandas/README.md). Las lecciones explican las herramientas gráficas; no repitas toda la limpieza para cambiar de biblioteca.

## Qué vas a aprender

- Elegir una representación según pregunta, audiencia y unidad.
- Construir figuras con ejes, escalas y etiquetas coherentes.
- Contrastar la gráfica con tablas y datos de referencia.
- Exportar una figura y explicar sus límites.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **04.01** · [Pregunta y elección de gráfico](01_question_chart/README.md) | [Lab 04.01](../../labs/04_visualization_python/01_question_chart/README.md) | Justificar una representación según la pregunta |
| **04.02** · [Matplotlib: Figure y Axes](02_figure_axes/README.md) | [Lab 04.02](../../labs/04_visualization_python/02_figure_axes/README.md) | Crear y guardar una figura desde código |
| **04.03** · [Comparaciones y evolución](03_comparisons_evolution/README.md) | [Lab 04.03](../../labs/04_visualization_python/03_comparisons_evolution/README.md) | Construir barras y líneas con unidades |
| **04.04** · [Distribuciones y relaciones](04_distributions_relationships/README.md) | [Lab 04.04](../../labs/04_visualization_python/04_distributions_relationships/README.md) | Interpretar dispersión y variabilidad |
| **04.05** · [Escalas, etiquetas y accesibilidad](05_scales_labels_accessibility/README.md) | [Lab 04.05](../../labs/04_visualization_python/05_scales_labels_accessibility/README.md) | Revisar una figura que puede inducir a error |
| **04.06** · [Composición y exportación](06_composition_export/README.md) | [Lab 04.06](../../labs/04_visualization_python/06_composition_export/README.md) | Comparar vistas y producir una figura legible |
| **04.07** · [Altair: visualización declarativa](07_altair_declarative/README.md) | [Lab 04.07](../../labs/04_visualization_python/07_altair_declarative/README.md) | Expresar datos, marcas y codificaciones |
| **04.08** · [Interacción con Altair](08_altair_interaction/README.md) — opcional | [Lab 04.08](../../labs/04_visualization_python/08_altair_interaction/README.md) | Explorar un indicador con filtros o selección |
| **04.09** · [Cierre visual del análisis](09_visual_closure/README.md) | [Lab 04.09](../../labs/04_visualization_python/09_visual_closure/README.md) | Entregar figuras reconstruibles e interpretación |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

<a id="01-pregunta-y-eleccion-de-grafico"></a>

### 01 — Pregunta y elección de gráfico

- Comparar categorías, evolución, distribución y relación; identificar población,
  unidad de análisis y agregación. Distinguir observación de explicación causal.
- Práctica: proponer gráficos para preguntas sobre saldo, cortes y segmentos,
  justificando la elección antes de escribir código.

<a id="02-matplotlib-figure-y-axes"></a>

### 02 — Matplotlib: Figure y Axes

- Figure como contenedor y Axes como área de representación; usar subplots y la
  interfaz de objetos para controlar una figura, sin depender del estado anterior.
- Práctica: reconstruir la gráfica inicial, etiquetar y guardar la salida.

<a id="03-comparaciones-y-evolucion"></a>

### 03 — Comparaciones y evolución

- Barras, orden de categorías y líneas por fecha; valores absolutos frente a tasas.
- Práctica: comparar segmentos y cortes, revisando períodos faltantes,
  denominadores y unidades antes de interpretar una tendencia.

<a id="04-distribuciones-y-relaciones"></a>

### 04 — Distribuciones y relaciones

- Histogramas, intervalos, boxplots y dispersión; distinguir resumen y detalle.
- Práctica: describir variabilidad y casos extremos sin confundir
  correlación con causalidad ni eliminar observaciones por su apariencia.

<a id="05-escalas-etiquetas-y-accesibilidad"></a>

### 05 — Escalas, etiquetas y accesibilidad

- Límites de ejes, escala lineal/logarítmica y sus condiciones; bases de comparación.
  Títulos informativos, leyendas, formatos y paletas legibles.
- Práctica disponible: corregir una figura engañosa y explicar qué cambió. Usar
  señales adicionales al color y documentar incertidumbre o cobertura limitada.

<a id="06-composicion-y-exportacion"></a>

### 06 — Composición y exportación

- Vistas múltiples, ejes comparables, anotaciones y espacio para etiquetas.
  PNG/SVG, tamaño y resolución según el destino; cierre de figuras al generar varias.
- Práctica disponible: una figura para compartir con fuente, corte y comentario breve.

<a id="07-altair-visualizacion-declarativa"></a>

### 07 — Altair: visualización declarativa

- Chart, marcas y canales; tipos nominal, ordinal, cuantitativo y temporal.
  Diferenciar representar datos preparados de agregarlos dentro de la gráfica.
- Práctica disponible: representar el mismo indicador de Matplotlib y comprobar
  que ambas vistas muestran la misma población, agregación y unidades.

<a id="08-interaccion-con-altair"></a>

### 08 — Interacción con Altair

- Parámetros, selecciones, condiciones, filtros y tooltips con la API vigente.
- Práctica disponible: seleccionar un segmento y mantener explícito qué muestra
  el resultado. Revisar exportación y recursos necesarios para compartirlo.
  Esta ampliación no exige construir una aplicación Streamlit.

<a id="09-cierre-visual-del-analisis"></a>

### 09 — Cierre visual del análisis

- Integrar datos verificados, código de gráficos y una interpretación escrita.
- Práctica disponible: reconstruir al menos una figura estática, comparar una vista
  Altair y explicar hallazgo, población y límites. Interacción opcional.

</details>

## Cómo trabajar este módulo

Predice qué relación debe verse y contrasta valores, escalas y unidades después de dibujar. 04.08 es una ampliación opcional de interacción. Una app, inferencia estadística o modelado no son requisitos para describir la muestra.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Código y tablas de referencia | Datos y medidas efectivamente representados |
| Figuras y exportaciones | Escalas, leyendas, unidades y archivos legibles |
| Interpretación y revisión | Mensaje, decisiones visuales y límites |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-integración-y-criterio-de-salida"></a>

## Criterio de salida

Puedes justificar la representación, comprobar sus medidas y reconstruir una figura exportada desde los datos. El cierre 04.09 incluye figura estática, vista declarativa e interpretación; no exige interacción avanzada.

Se reutilizarán 01_clean_credit_data y 02_credit_database. No hay checkpoint de proyecto implementado ni se exige un proyecto adicional para cerrar las prácticas.

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 04.01](01_question_chart/README.md) y realiza su lab.

**Al cerrar:** continúa con [05 — Python aplicado](../05_python_applied/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

La progresión se apoya en [Figure/Axes e interfaces de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html)
y en [parámetros e interacción de Altair](https://altair-viz.github.io/user_guide/interactions/parameters.html).
Consultar también [los canales de Altair](https://altair-viz.github.io/user_guide/encodings/index.html)
al desarrollar la representación declarativa.

### Apoyos relacionados

- [proyectos](../../projects/README.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_question_chart/README.md)

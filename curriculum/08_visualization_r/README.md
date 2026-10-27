# 08 — Visualización en R

[Inicio](../../README.md) / [Módulos](../README.md) / **08 — Visualización en R**

**Diseña figuras en R y verifica qué representan.**

[**Empezar por 08.01 →**](01_question_grammar/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Profundizar en ggplot2 sobre tablas e indicadores comprobados, conectando pregunta, representación e interpretación sin repetir la limpieza en cada figura.

## Antes de empezar

Completa [07 — tidyverse](../07_tidyverse/README.md), incluida [su primera figura](../07_tidyverse/10_first_plot_closure/README.md). Usa las bibliotecas locales y los preparadores indicados, conservando entregas anteriores.

## Qué vas a aprender

- Relacionar datos, mapeos, capas y estadísticas.
- Elegir geometrías, escalas, facetas y composición.
- Revisar etiquetas, color y alternativas textuales.
- Exportar figuras y contrastarlas con su referencia numérica.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **08.01** · [Pregunta y gramática de gráficos](01_question_grammar/README.md) | [Lab 08.01](../../labs/08_visualization_r/01_question_grammar/README.md) | Explicar datos, estéticas y capas de una figura |
| **08.02** · [Geometrías y transformaciones estadísticas](02_geometries_stats/README.md) | [Lab 08.02](../../labs/08_visualization_r/02_geometries_stats/README.md) | Elegir una geometría y verificar qué agrega |
| **08.03** · [Mapear y fijar estéticas](03_aesthetic_mapping/README.md) | [Lab 08.03](../../labs/08_visualization_r/03_aesthetic_mapping/README.md) | Distinguir variables de estilos constantes |
| **08.04** · [Escalas y coordenadas](04_scales_coordinates/README.md) | [Lab 08.04](../../labs/08_visualization_r/04_scales_coordinates/README.md) | Justificar límites, transformaciones y unidades |
| **08.05** · [Facetas y comparación entre grupos](05_facets_groups/README.md) | [Lab 08.05](../../labs/08_visualization_r/05_facets_groups/README.md) | Comparar segmentos con escalas explícitas |
| **08.06** · [Etiquetas, temas y accesibilidad](06_labels_themes_accessibility/README.md) | [Lab 08.06](../../labs/08_visualization_r/06_labels_themes_accessibility/README.md) | Comunicar población, hallazgo y límites |
| **08.07** · [Componer figuras](07_compose_figures/README.md) | [Lab 08.07](../../labs/08_visualization_r/07_compose_figures/README.md) | Reunir vistas sin perder contexto |
| **08.08** · [Exportación reproducible](08_reproducible_export/README.md) — opcional | [Lab 08.08](../../labs/08_visualization_r/08_reproducible_export/README.md) | Producir archivos legibles desde código |
| **08.09** · [Cierre visual y comparación con Python](09_visual_comparison/README.md) | [Lab 08.09](../../labs/08_visualization_r/09_visual_comparison/README.md) | Explicar indicadores equivalentes en dos ecosistemas |

<a id="alcance-de-cada-sección"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

<a id="01-pregunta-y-gramatica-de-graficos"></a>

### 01 — Pregunta y gramática de gráficos

- Revisar unidad de análisis, corte y población; ggplot, datos, aes, capas y objeto
  de gráfico. Construir por partes la figura inicial del módulo 07.
- Disponible: [lección y script](01_question_grammar/README.md) y
  [lab 08.01](../../labs/08_visualization_r/01_question_grammar/README.md).
  Reconstrucción por partes, unidad original/resumida, herencia, conteo frente
  a saldo y explicación de población/límites, sin dependencias nuevas.

<a id="02-geometrias-y-transformaciones-estadisticas"></a>

### 02 — Geometrías y transformaciones estadísticas

- Barras, líneas, puntos, histogramas y boxplots según la pregunta; datos de entrada
  frente a cálculos de la geometría. Diferenciar geom_bar de geom_col.
- Disponible: [lección, script y figuras](02_geometries_stats/README.md) y
  [lab 08.02](../../labs/08_visualization_r/02_geometries_stats/README.md).
  Identidad/conteo, líneas/puntos, intervalos y cajas sobre los mismos 14 IDs,
  con frecuencias/cuartiles comprobados. Sin dependencias nuevas; proporciones
  y huecos temporales como ampliaciones. Suavizados no son requisito.

<a id="03-mapear-y-fijar-esteticas"></a>

### 03 — Mapear y fijar estéticas

- Dentro de aes se vinculan variables; fuera se establecen propiedades constantes.
  Color, relleno, tamaño, forma y agrupación de líneas.
- Disponible: [lección, script y figura](03_aesthetic_mapping/README.md) y
  [lab 08.03](../../labs/08_visualization_r/03_aesthetic_mapping/README.md).
  Propiedades constantes/mapeos, leyendas, relleno/borde, formas/tamaño y
  agrupación por ID con mapeos locales. Misma base de 14 IDs, sin dependencias nuevas.

<a id="04-escalas-y-coordenadas"></a>

### 04 — Escalas y coordenadas

- Escalas continuas, discretas y temporales; ejes, transformaciones y unidades.
  Diferenciar limitar una escala de ampliar una vista con coordenadas.
- Disponible: [lección, script y figuras](04_scales_coordinates/README.md) y
  [lab 08.04](../../labs/08_visualization_r/04_scales_coordinates/README.md).
  Unidades, marcas/etiquetas, censura frente a zoom, fechas, log10 sobre positivos
  y proporción fija; misma fuente/lockfile, sin dependencias nuevas.

<a id="05-facetas-y-comparacion-entre-grupos"></a>

### 05 — Facetas y comparación entre grupos

- facet_wrap/facet_grid, escalas compartidas o libres y categorías ausentes.
- Disponible: [lección, script y figuras](05_facets_groups/README.md) y
  [lab 08.05](../../labs/08_visualization_r/05_facets_groups/README.md).
  Wrap/grid, escalas compartidas/libres, integrantes y denominadores, capas
  repetidas y categorías sin registros; misma fuente/lockfile, sin dependencias nuevas.

<a id="06-etiquetas-temas-y-accesibilidad"></a>

### 06 — Etiquetas, temas y accesibilidad

- labs, anotaciones, themes y leyendas; títulos informativos, corte y fuente.
  Contraste, señales adicionales al color y categorías con orden justificado.
- Disponible: [lección, script y figuras](06_labels_themes_accessibility/README.md) y
  [lab 08.06](../../labs/08_visualization_r/06_labels_themes_accessibility/README.md).
  Mensaje, anotaciones, temas locales, señales adicionales al color y descripción
  alternativa con tabla; mismos datos/lockfile, sin nuevas dependencias.

<a id="07-componer-figuras"></a>

### 07 — Componer figuras

- Combinar vistas con una herramienta como patchwork cuando aporte claridad;
  mantener escalas, unidades y leyendas comparables.
- Disponible: [lección, script y figuras](07_compose_figures/README.md) y
  [lab 08.07](../../labs/08_visualization_r/07_compose_figures/README.md).
  Resumen/detalle, disposición, guías y ejes explícitos; patchwork 1.3.2 añadido
  al mismo proyecto renv con respaldo y lockfile, registros previos conservados.

<a id="08-exportacion-reproducible"></a>

### 08 — Exportación reproducible

- ggsave con objeto explícito, dimensiones, formato y resolución según el destino.
  Diferenciar salida PNG/SVG/PDF y comprobar etiquetas en el archivo final.
- Disponible: [lección, script y figura](08_reproducible_export/README.md) y
  [lab 08.08](../../labs/08_visualization_r/08_reproducible_export/README.md).
  PNG esencial, dimensiones/resolución, pares/resumen y configuración; verificador
  de solo lectura y reconstrucción en otra carpeta. SVG/PDF opcionales con
  dispositivos incluidos en R, sin dependencias nuevas. Quarto se introduce en 11.

<a id="09-cierre-visual-y-comparacion-con-python"></a>

### 09 — Cierre visual y comparación con Python

- Comparar indicadores, población y corte antes de comparar apariencia con
  Matplotlib/Altair. No se exige reproducir exactamente el estilo del otro ecosistema.
- Disponible: [lección, scripts R/Python y figuras](09_visual_comparison/README.md)
  y [lab 08.09](../../labs/08_visualization_r/09_visual_comparison/README.md).
  Reconstrucción independiente de la fuente, seis tablas conciliadas, pares,
  cambio relativo y cobertura. Reutiliza la entrega de 07.10, sin nuevas
  dependencias; el proyecto integrador no se acredita.

</details>

## Cómo trabajar este módulo

Trabaja en scripts dentro del IDE y compara las figuras con sus tablas. Después verifica desde una sesión nueva. 08.08 es ampliación de exportación; diseñar extensiones de ggplot2 o una app no es requisito. R aplicado sigue siendo una consideración de diseño: no añade un módulo ni renumera 09–14.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Código y tablas | Datos y estadísticas representados |
| Figuras y exportaciones | Unidades, escalas, etiquetas y legibilidad |
| Interpretación y contraste | Diferencias y límites frente a la referencia |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-integración-y-criterio-de-salida"></a>

## Criterio de salida

Justifica geometría y escalas, comprueba medidas y reconstruye una figura exportada con interpretación. Los controles numéricos acompañan la revisión visual; no la sustituyen ni certifican accesibilidad completa.

Se ampliará 03_portfolio_analysis_r con un checkpoint visual, aún sin implementar. La integración numerada de R aplicado continúa pendiente.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Se sigue considerando **R aplicado** después de este módulo, para organizar
código, pruebas y dependencias antes de Parquet. Su integración y numeración
continúan pendientes: la planificación actual no añade un nivel ni renumera 09–14.
Los objetos avanzados y desarrollo de paquetes quedan como profundización.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 08.01](01_question_grammar/README.md) y realiza su lab.

**Al cerrar:** continúa con [09 — Arrow y Parquet](../09_arrow_parquet/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Para iniciar: [Data visualization de R4DS segunda edición](https://r4ds.hadley.nz/data-visualize.html)
y [documentación de ggplot2](https://ggplot2.tidyverse.org/reference/).
El libro [ggplot2: Elegant Graphics for Data Analysis](https://ggplot2-book.org/)
apoya la gramática; su capítulo de capas advierte que es un borrador y no es
lectura obligatoria. La lección 08.01 enlaza las funciones comprobadas.
La lección 08.08 contrasta [la referencia de ggsave](https://ggplot2.tidyverse.org/reference/ggsave.html).
Consulta la [guía de libros abiertos](../../docs/r-reading-guide.md) para las
lecturas iniciales y de profundización.

### Apoyos relacionados

- [proyectos](../../projects/README.md)
- [arquitectura de R aplicado](../../docs/architecture.md#r-aplicado-consideración-para-el-próximo-ajuste)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_question_grammar/README.md)

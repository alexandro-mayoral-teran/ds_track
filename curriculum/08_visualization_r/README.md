# 08 — Visualización en R

## Propósito y prerrequisitos

Profundizar en ggplot2 sobre tablas e indicadores ya comprobados en
[07 — tidyverse](../07_tidyverse/README.md), cuyas diez secciones tienen material.
Se reutiliza la primera figura disponible en
[07.10](../07_tidyverse/10_first_plot_closure/README.md) y se
compara con el análisis Python; no se repite toda la limpieza para aprender gráficos.

**Estado:** [08.01](01_question_grammar/README.md) y
[08.02](02_geometries_stats/README.md) disponen de lección, script y lab.
08.03–08.09 siguen planificadas; sus enlaces internos describen el alcance.

La pregunta, la representación y la interpretación guían el recorrido. El libro
abierto de ggplot2 aporta la gramática de gráficos; su tercera edición en línea
está en desarrollo. Las APIs y dependencias se comprobarán al crear cada lección.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta y gramática de gráficos](01_question_grammar/README.md) | Esencial | Explicar datos, estéticas y capas de una figura |
| 2 | [Geometrías y transformaciones estadísticas](02_geometries_stats/README.md) | Esencial | Elegir una geometría y verificar qué agrega |
| 3 | [Mapear y fijar estéticas](#03-mapear-y-fijar-esteticas) | Esencial | Distinguir variables de estilos constantes |
| 4 | [Escalas y coordenadas](#04-escalas-y-coordenadas) | Esencial | Justificar límites, transformaciones y unidades |
| 5 | [Facetas y comparación entre grupos](#05-facetas-y-comparacion-entre-grupos) | Práctica | Comparar segmentos con escalas explícitas |
| 6 | [Etiquetas, temas y accesibilidad](#06-etiquetas-temas-y-accesibilidad) | Esencial | Comunicar población, hallazgo y límites |
| 7 | [Componer figuras](#07-componer-figuras) | Práctica | Reunir vistas sin perder contexto |
| 8 | [Exportación reproducible](#08-exportacion-reproducible) | Esencial | Producir archivos legibles desde código |
| 9 | [Cierre visual y comparación con Python](#09-cierre-visual-y-comparacion-con-python) | Práctica de cierre | Explicar indicadores equivalentes en dos ecosistemas |

## Alcance de cada sección

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
- Práctica prevista: corregir una leyenda accidental y verificar que cada línea
  representa el grupo esperado.

<a id="04-escalas-y-coordenadas"></a>

### 04 — Escalas y coordenadas

- Escalas continuas, discretas y temporales; ejes, transformaciones y unidades.
  Diferenciar limitar una escala de ampliar una vista con coordenadas.
- Práctica prevista: comprobar si cambiar límites excluye observaciones y altera
  un cálculo estadístico; justificar una comparación legible.

<a id="05-facetas-y-comparacion-entre-grupos"></a>

### 05 — Facetas y comparación entre grupos

- facet_wrap/facet_grid, escalas compartidas o libres y categorías ausentes.
- Práctica prevista: comparar el mismo indicador entre segmentos, conservando
  denominadores y haciendo visibles grupos sin datos.

<a id="06-etiquetas-temas-y-accesibilidad"></a>

### 06 — Etiquetas, temas y accesibilidad

- labs, anotaciones, themes y leyendas; títulos informativos, corte y fuente.
  Contraste, señales adicionales al color y categorías con orden justificado.
- Práctica prevista: mejorar una figura y escribir una interpretación que distinga
  datos observados, cobertura e incertidumbre de afirmaciones causales.

<a id="07-componer-figuras"></a>

### 07 — Componer figuras

- Combinar vistas con una herramienta como patchwork cuando aporte claridad;
  mantener escalas, unidades y leyendas comparables.
- Práctica prevista: detalle y resumen en una misma composición. La biblioteca
  adicional se incorporará al renv del proyecto solo al implementar esta sección.

<a id="08-exportacion-reproducible"></a>

### 08 — Exportación reproducible

- ggsave con objeto explícito, dimensiones, formato y resolución según el destino.
  Diferenciar salida PNG/SVG/PDF y comprobar etiquetas en el archivo final.
- Práctica prevista: regenerar la figura desde una sesión nueva y conservar su
  tabla fuente y configuración. El reporte Quarto se introduce en el nivel 11.

<a id="09-cierre-visual-y-comparacion-con-python"></a>

### 09 — Cierre visual y comparación con Python

- Comparar indicadores, población y corte antes de comparar apariencia con
  Matplotlib/Altair. No se exige reproducir exactamente el estilo del otro ecosistema.
- Práctica prevista: entregar una figura reconstruible, tabla conciliada y
  comentario con hallazgo y límites, ampliando el proyecto R conocido.

## Prácticas, integración y criterio de salida

Los labs [08.01](../../labs/08_visualization_r/01_question_grammar/README.md) y
[08.02](../../labs/08_visualization_r/02_geometries_stats/README.md) están
disponibles; 08.03–08.09 siguen previstos. Se ampliará el proyecto previsto
03_portfolio_analysis_r, registrado en [proyectos](../../projects/README.md),
con un checkpoint visual cuyo nombre se definirá al implementarlo.

Puedes avanzar cuando justifiques geometría y escalas, compruebes las medidas
representadas y reconstruyas una figura exportada con interpretación. Diseñar
extensiones de ggplot2 o una app interactiva no es requisito; Shiny ocupa el 13.

Se sigue considerando **R aplicado** después de este módulo, para organizar
código, pruebas y dependencias antes de Parquet. Su integración y numeración
continúan pendientes: la planificación actual no añade un nivel ni renumera 09–14.
Los objetos avanzados y desarrollo de paquetes quedan como profundización.

## Continuidad y referencias

Por ahora, el siguiente módulo numerado es [09 — Arrow y Parquet](../09_arrow_parquet/README.md).
Consulta la [arquitectura de R aplicado](../../docs/architecture.md#r-aplicado-consideración-para-el-próximo-ajuste)
para la consideración pendiente.

Para iniciar: [Data visualization de R4DS segunda edición](https://r4ds.hadley.nz/data-visualize.html)
y [documentación de ggplot2](https://ggplot2.tidyverse.org/reference/).
El libro [ggplot2: Elegant Graphics for Data Analysis](https://ggplot2-book.org/)
apoya la gramática; su capítulo de capas advierte que es un borrador y no es
lectura obligatoria. La lección 08.01 enlaza las funciones comprobadas.
Para exportar se verificará [la referencia de ggsave](https://ggplot2.tidyverse.org/reference/ggsave.html).
Consulta la [guía de libros abiertos](../../docs/r-reading-guide.md) para las
lecturas iniciales y de profundización.

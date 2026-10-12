# 08 — Visualización en R

## Propósito y prerrequisitos

Profundizar en ggplot2 sobre tablas e indicadores ya comprobados en
[07 — tidyverse](../07_tidyverse/README.md). Se reutiliza su primera figura y se
compara con el análisis Python; no se repite toda la limpieza para aprender gráficos.

**Estado:** nueve secciones planificadas; lecciones y labs por desarrollar.
Los enlaces internos describen el alcance, no material ejecutable.

La pregunta, la representación y la interpretación guían el recorrido. El libro
abierto de ggplot2 aporta la gramática de gráficos; su tercera edición en línea
está en desarrollo. Las APIs y dependencias se comprobarán al crear cada lección.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta y gramática de gráficos](#01-pregunta-y-gramatica-de-graficos) | Esencial | Explicar datos, estéticas y capas de una figura |
| 2 | [Geometrías y transformaciones estadísticas](#02-geometrias-y-transformaciones-estadisticas) | Esencial | Elegir una geometría y verificar qué agrega |
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
- Práctica prevista: describir qué aporta cada capa y qué pregunta responde.

<a id="02-geometrias-y-transformaciones-estadisticas"></a>

### 02 — Geometrías y transformaciones estadísticas

- Barras, líneas, puntos, histogramas y boxplots según la pregunta; datos de entrada
  frente a cálculos de la geometría. Diferenciar geom_bar de geom_col.
- Práctica prevista: contrastar conteos con saldos ya agregados y comprobarlos
  contra la tabla. Bandas o suavizados requieren explicar su método y límites.

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

Se prevén labs 08.01–08.09; todavía no existen. Se ampliará el proyecto previsto
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

Fuente principal: [ggplot2: Elegant Graphics for Data Analysis](https://ggplot2-book.org/),
con lectura de [construcción por capas](https://ggplot2-book.org/layers).
Para exportar se verificará [la referencia de ggsave](https://ggplot2.tidyverse.org/reference/ggsave.html).
Consulta la [guía de libros abiertos](../../docs/r-reading-guide.md) para las
lecturas iniciales y de profundización.

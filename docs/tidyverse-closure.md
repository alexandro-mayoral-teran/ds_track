# Cierre de 07 — tidyverse y pendientes

## Qué está disponible

Las diez secciones de [07 — tidyverse](../curriculum/07_tidyverse/README.md)
tienen lección, práctica asociada y código ejecutable. El cierre
[07.10](../curriculum/07_tidyverse/10_first_plot_closure/README.md) reconstruye
desde el CSV original la validación de 07.09, conserva aceptados/rechazos y
motivos, compara una base común y genera la primera figura con ggplot2.

Se mantiene el mismo proyecto renv: metadatos anteriores respaldados, lockfile
real, biblioteca local y restauración comprobada. Las salidas de práctica y las
bibliotecas permanecen locales. La primera gráfica no exige notebook, Quarto,
acceso a una base remota ni publicación web.

**Esto cierra el desarrollo del material de 07, no acredita aprendizaje ni
completa el track.** El avance real y las verificaciones de autoría están en
[PROGRESS.md](../PROGRESS.md). Este documento conserva los criterios de cierre
y el alcance pendiente, no una bitácora adicional.

## Qué falta para cerrar la práctica del estudiante

| Evidencia por reunir | Comprobación |
| --- | --- |
| Script propio y contrato explicado | Fuente, unidad, reglas y claves identificadas sin depender del workspace |
| Auditoría de calidad | 48 = 36 aceptados + 12 rechazos; originales y motivos conservados |
| Población comparable | 14 IDs comunes, cuatro sin pareja por corte; cobertura 14/18 por fecha |
| Tablas y figura coherentes | 29000/31800 MXN, cambio +2800; CSV releídos y PNG legible con base cero |
| Reconstrucción completa | Reiniciar R, ejecutar el script y verificar la entrega desde el CSV original |
| Interpretación y reflexión | Denominador de 9.66%, alcance descriptivo, límites y dudas pendientes |

Usar el [lab 07.10](../labs/07_tidyverse/10_first_plot_closure/README.md), revisar
la explicación con quien acompaña y registrar evidencia real. Una sesión puede
cubrir parte del cierre. Consultar material o ejecutar el script de referencia
no basta para marcar una competencia como adquirida.

## Qué falta desarrollar después

| Pendiente | Alcance y condición para darlo por implementado |
| --- | --- |
| Criterio de salida de 08 | Las nueve secciones tienen lección/scripts y lab. Revisar evidencia de geometrías, escalas, indicadores, reconstrucción y explicación; disponer del material no acredita las prácticas del estudiante. |
| Proyecto 03_portfolio_analysis_r | No tiene carpeta ni checkpoints activos. Antes de crearlos, definir producto, entradas, contrato y rúbrica; enlazar las lecciones y evidencias efectivamente exigidas. |
| Checkpoints propuestos de 07 | Importación/contrato, calidad, indicadores/relaciones y categorías/cortes/figura. Son propuestas para el proyecto, no entregas ya habilitadas. |
| Revisión del recorrido IDE anterior | 07.01–07.10 ya priorizan IDE. Revisar con el usuario las lecciones anteriores que aún necesiten adaptación, conservando terminal como apoyo cuando corresponda. |
| Decisiones de estructura | Integración numerada de R aplicado, terminal avanzada y separación entre avance del material y bitácoras personales: resolver antes de cambiar numeración o referencias. |
| Resto del track | Las nueve secciones de 09 y las diez de 10 tienen material; 11–14 conservan planes. Consultar [cierre de almacenamiento](storage-closure.md); el proyecto integrador y la práctica siguen pendientes. Cerrar el material no acredita aprendizaje. |

[08.01 — Pregunta y gramática de gráficos](../curriculum/08_visualization_r/01_question_grammar/README.md)
ya reutiliza la figura, datos y población explícita de 07.10 para estudiar sus
capas sin repetir toda la limpieza. [08.02](../curriculum/08_visualization_r/02_geometries_stats/README.md)
amplía geometrías y estadísticas sobre la misma base común.
[08.03](../curriculum/08_visualization_r/03_aesthetic_mapping/README.md) distingue
mapeos, propiedades constantes y agrupación por ID.
[08.04](../curriculum/08_visualization_r/04_scales_coordinates/README.md) amplía
unidades, límites, zoom y transformaciones.
[08.05](../curriculum/08_visualization_r/05_facets_groups/README.md) añade paneles
por segmento/corte, escalas y cobertura explícitas.
[08.06](../curriculum/08_visualization_r/06_labels_themes_accessibility/README.md)
añade mensaje, etiquetas, temas locales y señales alternativas al color.
[08.07](../curriculum/08_visualization_r/07_compose_figures/README.md) reúne
resumen/detalle con contexto, ejes y guías explícitos.
[08.09](../curriculum/08_visualization_r/09_visual_comparison/README.md) añade
cierre visual y contraste independiente de registros, pares y saldos con Python.
[08.08 — Exportación reproducible](../curriculum/08_visualization_r/08_reproducible_export/README.md)
añade dimensiones, resolución y comprobación de archivos. Las nueve secciones
tienen material; revisar el criterio global y la evidencia antes de avanzar al
[lección 09.01 — CSV, Parquet y Arrow](../curriculum/09_arrow_parquet/01_csv_parquet_arrow/README.md),
ya disponible. Los [pendientes de almacenamiento](storage-closure.md) distinguen
la introducción del cierre completo. Instalar dependencias
adicionales solo cuando una práctica implementada las requiera.

Para el proyecto integrador, consultar el [índice de proyectos](../projects/README.md)
y el [flujo de aprendizaje](learning-workflow.md). Publicación, PDF, una segunda
aplicación o temas avanzados no se añaden como requisitos implícitos del cierre.

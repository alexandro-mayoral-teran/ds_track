# Lecturas abiertas para el recorrido de R

Estas referencias se pueden consultar en línea sin comprar un libro. Se usarán
para fundamentar lecciones y preparar ejemplos propios de DS Track; no hace
falta leerlas completas para avanzar. La planificación adapta su orden al
análisis ya aprendido con Python.

## Libros y papel dentro del track

| Referencia | Autoría | Uso previsto |
| --- | --- | --- |
| [R for Data Science, segunda edición](https://r4ds.hadley.nz/) | Hadley Wickham, Mine Çetinkaya-Rundel y Garrett Grolemund | Base para importar, transformar y comunicar datos en 06–08 |
| [Advanced R, segunda edición](https://adv-r.hadley.nz/) | Hadley Wickham | Consultas sobre estructuras y funciones en 06; profundización posterior |
| [ggplot2: Elegant Graphics for Data Analysis, tercera edición en línea](https://ggplot2-book.org/) | Hadley Wickham, Danielle Navarro y Thomas Lin Pedersen | Gramática, capas, escalas y comunicación visual en 08 |
| [R Packages, segunda edición](https://r-pkgs.org/) | Hadley Wickham y Jennifer Bryan | Referencia futura para organizar, documentar y comprobar paquetes |

La tercera edición en línea del libro de ggplot2 está en desarrollo. Al crear
una lección se comprobará la documentación de la versión instalada, especialmente
si un ejemplo del libro utiliza una API diferente.

## Por dónde leer según el módulo

### 06 — R fundamental

Comienza con el [manual introductorio oficial de R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)
y consulta [selección de estructuras en Advanced R](https://adv-r.hadley.nz/subsetting.html)
para entender las diferencias entre [, [[ y $. Advanced R es apoyo para preguntas
concretas; no se exige dominar entornos, evaluación o sistemas de objetos.

Para dependencias, utiliza la [introducción oficial a renv](https://rstudio.github.io/renv/articles/renv.html).
Un entorno de evaluación de R y una librería de paquetes de renv son conceptos
diferentes; no se equiparan a los entornos virtuales de Python.

### 07 — tidyverse

En R for Data Science, consulta [transformación](https://r4ds.hadley.nz/data-transform.html),
[datos ordenados](https://r4ds.hadley.nz/data-tidy.html) y
[uniones](https://r4ds.hadley.nz/joins.html). Después utiliza los capítulos de
[factores](https://r4ds.hadley.nz/factors.html) y
[fechas](https://r4ds.hadley.nz/datetimes.html) para las preguntas del proyecto.
El libro se consulta por necesidad; su índice no es una lista obligatoria del curso.

### 08 — Visualización en R

Profundiza en [construcción de una figura por capas](https://ggplot2-book.org/layers)
y utiliza el índice del libro de ggplot2 para escalas, facetas, temas y composición.
La [documentación de ggplot2](https://ggplot2.tidyverse.org/) complementa los conceptos
con la API vigente y los parámetros de cada función.

### Futuro R aplicado

Advanced R y R Packages servirán para organización, funciones, pruebas,
documentación y diseño de paquetes cuando esos temas respondan a una necesidad.
Su ubicación en el track sigue pendiente; no se exige crear un paquete antes de
tidyverse, ggplot2 o Parquet.

## Apoyo en español

[R para Ciencia de Datos](https://es.r4ds.hadley.nz/) ofrece la traducción
comunitaria de la primera edición de R for Data Science. Puede ayudar con el
vocabulario, pero su organización y algunos ejemplos difieren de la segunda
edición. No mezclar instrucciones de versiones sin comprobarlas; DS Track
explicará cada concepto en español y verificará las APIs al desarrollar el material.

## Aplicar una lectura

1. Plantea una pregunta concreta del ejercicio.
2. Lee el apartado correspondiente y consulta los nombres que no entiendas.
3. Prueba la idea en una muestra pequeña del track.
4. Comprueba registros, tipos e indicadores; explica el resultado.
5. Anota la referencia y la decisión tomada antes de continuar.

Los planes detallados están en [R fundamental](../curriculum/06_r_foundations/README.md),
[tidyverse](../curriculum/07_tidyverse/README.md) y
[visualización en R](../curriculum/08_visualization_r/README.md).

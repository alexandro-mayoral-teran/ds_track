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
| [Mastering Shiny](https://mastering-shiny.org/) | Hadley Wickham | Aplicaciones reactivas y organización en el módulo 13 |

La tercera edición en línea del libro de ggplot2 está en desarrollo. Al crear
una lección se comprobará la documentación de la versión instalada, especialmente
si un ejemplo del libro utiliza una API diferente.

## Por dónde leer según el módulo

### 06 — R fundamental

La [lección 06.01](../curriculum/06_r_foundations/01_r_session/README.md) utiliza
[Workflow: basics](https://r4ds.hadley.nz/workflow-basics.html),
[Workflow: scripts and projects](https://r4ds.hadley.nz/workflow-scripts.html) y
[Workflow: getting help](https://r4ds.hadley.nz/workflow-help.html) de R4DS segunda
edición. Se adaptan sus ideas a una venta propia y se verifican source, Rscript,
sessionInfo y paquetes con la documentación oficial y R 4.6.1 local.
No se traslada la instalación inicial de tidyverse del libro a esta primera
práctica: utiliza paquetes incluidos. Renv se desarrolla en 06.08.

La [lección 06.02](../curriculum/06_r_foundations/02_objects_vectors/README.md)
consulta [vectores de Advanced R](https://adv-r.hadley.nz/vectors-chap.html), de
Hadley Wickham, para relacionar tipo común, longitud y coerción. No exige estudiar
todo el capítulo. Contrasta c, typeof/class, as.integer y aritmética con la ayuda
oficial y R 4.6.1 local; en particular, distingue reciclaje base silencioso de
validación de datos y de reglas más estrictas de otros paquetes.

La [lección 06.03](../curriculum/06_r_foundations/03_subsetting/README.md) toma
[selección en Advanced R](https://adv-r.hadley.nz/subsetting.html) como consulta
puntual y contrasta Extract/names con R 4.6.1. Distingue el objeto seleccionado,
el contenedor y su contenido; anticipa solo una lista mínima y deja la selección
de tablas para 06.05. drop con una matriz es ampliación opcional.

La [lección 06.04](../curriculum/06_r_foundations/04_logic_missing/README.md) consulta
[Logical vectors de R4DS segunda edición](https://r4ds.hadley.nz/logicals.html),
de Wickham, Çetinkaya-Rundel y Grolemund. Usa ejemplos propios de ventas en R base,
sin requerir dplyr. Contrasta operadores, NA/is.na, any/all y na.rm con la ayuda
oficial y R 4.6.1: cumplimiento, incumplimiento conocido y pendiente son grupos
distintos; una suma observada requiere declarar cobertura. Vacío, todos faltantes,
cero, NULL y NaN se comparan antes de automatizar decisiones en 06.06.

La [lección 06.05](../curriculum/06_r_foundations/05_lists_data_frames/README.md)
consulta listas y data frames de [Advanced R](https://adv-r.hadley.nz/vectors-chap.html),
de Hadley Wickham, y su capítulo de selección. Usa ventas propias y R base;
contrasta construcción, reciclaje, extracción y dimensiones con la ayuda instalada
de R 4.6.1. Algunos pasajes del libro describen conversión automática de texto a
factor: el valor predeterminado de stringsAsFactors es FALSE desde R 4.0.0, según
la documentación oficial. Matrices son comparación opcional; tibble queda para 07.
Consulta de estas referencias: 2026-10-17.

La [lección 06.06](../curriculum/06_r_foundations/06_functions_control/README.md)
consulta [Functions de R4DS segunda edición](https://r4ds.hadley.nz/functions.html),
de Wickham, Çetinkaya-Rundel y Grolemund, y los capítulos de
[funciones](https://adv-r.hadley.nz/functions.html) y
[control de flujo](https://adv-r.hadley.nz/control-flow.html) de Advanced R,
de Wickham. Adapta ideas a las ventas propias con R base: entradas explícitas,
retorno y alcance local, validación, decisiones con cobertura y repetición segura.
Contrasta if/for/stop/seq_along/tryCatch con ayuda instalada de R 4.6.1;
no exige tidyverse, evaluación avanzada o sistemas de condiciones propios.
Consulta de estas referencias: 2026-10-17.

La [lección 06.07](../curriculum/06_r_foundations/07_files_validation/README.md)
consulta [Data import de R4DS segunda edición](https://r4ds.hadley.nz/data-import.html),
de Wickham, Çetinkaya-Rundel y Grolemund, sobre columnas, tipos y faltantes.
Adapta el problema a R base y un CSV propio: texto conservado, reglas por registro,
rechazos conciliados y exportación/relectura. read.csv/write.csv/count.fields y
codificación contrastados con ayuda de R 4.6.1. El capítulo usa readr; sus APIs
no se intercambian con las de R base ni se instalan por anticipado. UTF-8 del
archivo y locale de la sesión se distinguen; una entrega parcial no se considera
comprobada. Consulta: 2026-10-17.

La [lección 06.08](../curriculum/06_r_foundations/08_projects_renv/README.md)
consulta [Workflow: scripts and projects de R4DS](https://r4ds.hadley.nz/workflow-scripts.html),
de Wickham, Çetinkaya-Rundel y Grolemund, y la
[introducción a renv](https://rstudio.github.io/renv/articles/renv.html), de Kevin
Ushey y Hadley Wickham. Contrasta init, snapshot explícito, restore, status y
rutas con renv 1.3.1; withr 3.0.3 proporciona una dependencia pequeña para
presentación temporal. Lockfile y activador generados realmente, restauración en
copias independientes y ejecución comprobadas con R 4.6.1. No confunde paquetes,
intérprete y estado de consola ni exige tidyverse por anticipado. Consulta: 2026-10-17.

La [lección 06.09](../curriculum/06_r_foundations/09_known_result/README.md)
retoma [Workflow: scripts and projects de R4DS](https://r4ds.hadley.nz/workflow-scripts.html),
de Wickham, Çetinkaya-Rundel y Grolemund, para reconstruir desde archivos.
El cierre compara implementaciones propias de Python/R sobre el mismo contrato:
identidad, rechazos, faltantes, conteos e importes con tolerancia explícita.
Documentación de comparación/huellas en R y csv/math/hashlib en Python contrastada;
R 4.6.1 y Python 3.12.12 comprobados. Se conserva el lockfile de 06.08 y no se
adelanta ggplot2 ni se confunde material completo con aprendizaje acreditado.
Consulta: 2026-10-17.

Comienza con el [manual introductorio oficial de R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)
y consulta [selección de estructuras en Advanced R](https://adv-r.hadley.nz/subsetting.html)
para entender las diferencias entre [, [[ y $. Advanced R es apoyo para preguntas
concretas; no se exige dominar entornos, evaluación o sistemas de objetos.

Para dependencias, utiliza la [introducción oficial a renv](https://rstudio.github.io/renv/articles/renv.html).
Un entorno de evaluación de R y una librería de paquetes de renv son conceptos
diferentes; no se equiparan a los entornos virtuales de Python.

### 07 — tidyverse

La [lección 07.01](../curriculum/07_tidyverse/01_tibbles_import_pipes/README.md)
consulta Data import de R4DS segunda edición, de Wickham, Çetinkaya-Rundel y
Grolemund, y las referencias oficiales de readr/tibble/pipe. Usa ejemplos propios
sobre el CSV de pandas 02.02; comprueba tipos, problemas y extracción con R 4.6.1,
readr 2.2.0 y tibble 3.3.1. El proyecto renv se extiende con un lockfile realmente
restaurado; no exige el metapaquete tidyverse. Consulta: 2026-10-17.

En R for Data Science, consulta [transformación](https://r4ds.hadley.nz/data-transform.html),
[datos ordenados](https://r4ds.hadley.nz/data-tidy.html) y
[uniones](https://r4ds.hadley.nz/joins.html). Después utiliza los capítulos de
[factores](https://r4ds.hadley.nz/factors.html) y
[fechas](https://r4ds.hadley.nz/datetimes.html) para las preguntas del proyecto.
El libro se consulta por necesidad; su índice no es una lista obligatoria del curso.

La [lección 07.02](../curriculum/07_tidyverse/02_select_filter_sort/README.md)
retoma Data transformation de R4DS (Wickham, Çetinkaya-Rundel y Grolemund) y las
referencias oficiales select/rename/filter/arrange. Ejemplos propios sobre la
cartera conocida; selección, lógica de tres valores, pendientes, empates y
vacío comprobados con R 4.6.1/dplyr 1.2.1. Contrasta pandas/SQLite bajo la misma
pregunta y conserva las dependencias previas de renv. Consulta: 2026-10-17.

La [lección 07.03](../curriculum/07_tidyverse/03_transform_columns/README.md)
consulta Numbers y Logical vectors de R4DS segunda edición, de Wickham,
Çetinkaya-Rundel y Grolemund, junto con mutate/if_else/case_when de dplyr y
parse_double/problemas de readr. Se contrasta con ayuda instalada y ejemplos
propios: conservación del origen, tipos y prioridad, conversiones incompatibles
y denominadores. R 4.6.1/dplyr 1.2.1/readr 2.2.0; sin paquetes nuevos. Reutiliza
40 filas de pandas 02.04 y concilia todas sus columnas. Consulta: 2026-10-17.

La [lección 07.04](../curriculum/07_tidyverse/04_missing_duplicates_quality/README.md)
consulta Missing values de R4DS segunda edición (Wickham, Çetinkaya-Rundel y
Grolemund), distinct/coalesce/bind_rows de dplyr y duplicated/rowSums de R.
Ejemplos propios sobre los 44 registros de pandas 02.05: ausencia frente a
combinación ausente, claves, motivos múltiples y partición reconstruida.
R 4.6.1/dplyr 1.2.1 existentes, sin dependencias nuevas; casos de frontera y
comparación exacta de trabajo, partes y banderas con pandas. Revisión: 2026-10-18.

### 08 — Visualización en R

Profundiza en [construcción de una figura por capas](https://ggplot2-book.org/layers)
y utiliza el índice del libro de ggplot2 para escalas, facetas, temas y composición.
La [documentación de ggplot2](https://ggplot2.tidyverse.org/) complementa los conceptos
con la API vigente y los parámetros de cada función.

### 09 — Arrow y Parquet

Para continuar después de ggplot2, el [capítulo Arrow de R for Data Science](https://r4ds.hadley.nz/arrow.html)
apoya la parte R del [módulo 09](../curriculum/09_arrow_parquet/README.md).
El track añade una práctica de intercambio Python/R y controles de tipos e indicadores.

### 11 — Reportes y 13 — Shiny

El [capítulo Quarto de R for Data Science](https://r4ds.hadley.nz/quarto.html)
apoya el recorrido R del módulo 11. Para la aplicación del 13, consulta
[Mastering Shiny](https://mastering-shiny.org/) y
[reactividad básica](https://mastering-shiny.org/basic-reactivity.html).
La documentación oficial complementa los libros para verificar APIs al implementar.

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

Consulta 06.01: 2026-10-15. No se presume que todos los libros estén desactualizados:
se contrasta la función o el flujo concreto con la versión usada. Las páginas web
de R-patched/R-devel y los libros en desarrollo pueden describir otras versiones;
la ayuda instalada permite comprobar lo que realmente está disponible.

## Aplicar una lectura

1. Plantea una pregunta concreta del ejercicio.
2. Lee el apartado correspondiente y consulta los nombres que no entiendas.
3. Prueba la idea en una muestra pequeña del track.
4. Comprueba registros, tipos e indicadores; explica el resultado.
5. Anota la referencia y la decisión tomada antes de continuar.

Los planes detallados están en [R fundamental](../curriculum/06_r_foundations/README.md),
[tidyverse](../curriculum/07_tidyverse/README.md) y
[visualización en R](../curriculum/08_visualization_r/README.md).

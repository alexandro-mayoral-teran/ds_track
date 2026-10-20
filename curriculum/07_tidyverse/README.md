# 07 — tidyverse

## Propósito y prerrequisitos

Transformar tablas de manera expresiva y comprobable con dplyr, tidyr y paquetes
relacionados. Completa [R fundamental](../06_r_foundations/README.md) y reutiliza
sus datos y proyecto renv; no se crea un entorno independiente por cada ejercicio.
El [cierre 06.09](../06_r_foundations/09_known_result/README.md) está disponible
con conciliación Python/R.

**Estado:** 07.01–07.06 disponen de lecciones, scripts y labs; 07.01–07.02
tienen lockfiles y 07.03–07.06 reutilizan el de 07.02. 07.07–07.10
siguen planificadas. Los enlaces internos describen el alcance pendiente.

Usaremos la misma cartera sintética e indicadores conocidos de pandas/SQL.
La primera figura con ggplot2 aparece aquí; el módulo 08 profundiza su diseño.
R for Data Science inspira contenidos, pero adaptamos su orden a los prerrequisitos
ya trabajados en DS Track, sin exigir leer el libro completo.

## Orden de desarrollo

| Orden | Sección | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Tibbles, importación y pipes](01_tibbles_import_pipes/README.md) | Esencial | Cargar una tabla y leer una secuencia de pasos |
| 2 | [Seleccionar, filtrar y ordenar](02_select_filter_sort/README.md) | Esencial | Obtener un subconjunto verificable |
| 3 | [Transformar columnas](03_transform_columns/README.md) | Esencial | Calcular indicadores con reglas explícitas |
| 4 | [Faltantes, duplicados y calidad](04_missing_duplicates_quality/README.md) | Esencial | Conservar aceptados y rechazos con motivos |
| 5 | [Agrupar y resumir](05_group_summarize/README.md) | Esencial | Conciliar medidas y denominadores |
| 6 | [Unir tablas](06_join_tables/README.md) | Esencial | Detectar relaciones que multiplican registros |
| 7 | [Datos ordenados y reshape](#07-datos-ordenados-y-reshape) | Práctica | Cambiar formato preservando indicadores |
| 8 | [Texto, categorías y factores](#08-texto-categorias-y-factores) | Esencial | Normalizar categorías y controlar su orden |
| 9 | [Fechas y cortes](#09-fechas-y-cortes) | Esencial | Comparar períodos con fechas interpretadas |
| 10 | [Primera figura y cierre del análisis](#10-primera-figura-y-cierre-del-analisis) | Práctica de cierre | Reconstruir tablas e interpretar un gráfico |

## Alcance de cada sección

<a id="01-tibbles-importacion-y-pipes"></a>

### 01 — Tibbles, importación y pipes

Disponible: [lección 07.01](01_tibbles_import_pipes/README.md) y
[lab 07.01](../../labs/07_tidyverse/01_tibbles_import_pipes/README.md).
Tibble frente a data.frame, tipos/problemas de readr y pipe nativo. Reutiliza las
seis observaciones de pandas 02.02 con diccionario, controles 6 × 5 y 6000 MXN.
Extiende el mismo proyecto renv de 06.09 con respaldo de metadatos y lockfile
comprobado: readr 2.2.0/tibble 3.3.1; no exige todo tidyverse ni dplyr todavía.
Recorrido principal en RStudio/IDE: preparación desde R, scripts por bloques,
inspección y reinicio con ejecución completa. Rscript es una alternativa opcional.

<a id="02-seleccionar-filtrar-y-ordenar"></a>

### 02 — Seleccionar, filtrar y ordenar

Disponible: [lección 07.02](02_select_filter_sort/README.md) y
[lab 07.02](../../labs/07_tidyverse/02_select_filter_sort/README.md).
select/rename/filter/arrange, lógica de tres valores, pendientes, desempates y
vacíos con esquema. Mismo CSV que 07.01 y pandas 02.03: 002/003/006, 2750 MXN,
partición 3/2/1. Extiende el proyecto desde R con dplyr 1.2.1/lockfile; recorrido
IDE y comparación de significado con pandas/SQL, sin exportar ni modificar la fuente.

<a id="03-transformar-columnas"></a>

### 03 — Transformar columnas

Disponible: [lección 07.03](03_transform_columns/README.md) y
[lab 07.03](../../labs/07_tidyverse/03_transform_columns/README.md).
mutate, if_else/case_when y prioridades; conversión auditable sin truncar ni
imputar cero. Empieza con seis observaciones y retoma las 40 filas de pandas 02.04:
40 × 15, 36 restas/35 porcentajes evaluables y 211150 MXN en la base conciliada.
Conserva textos y marcas, fuente y dependencias de 07.02; preparación y práctica
desde el IDE sin reinstalar. across permanece como ampliación posterior.

<a id="04-faltantes-duplicados-y-calidad"></a>

### 04 — Faltantes, duplicados y calidad

Disponible: [lección 07.04](04_missing_duplicates_quality/README.md) y
[lab 07.04](../../labs/07_tidyverse/04_missing_duplicates_quality/README.md).
Ausencia explícita frente a observación ausente, claves compuestas, duplicated
y distinct, reglas y motivos múltiples. Reutiliza 44 registros de pandas 02.05:
29 aceptados/15 rechazados, 19 incidencias; partición reconstruida y saldo
interpretable con cobertura. Sin imputar ni elegir una versión repetida;
preparación desde R y recorrido IDE, sin dependencias nuevas.

<a id="05-agrupar-y-resumir"></a>

### 05 — Agrupar y resumir

Disponible: [lección 07.05](05_group_summarize/README.md) y
[lab 07.05](../../labs/07_tidyverse/05_group_summarize/README.md).
group_by/summarise/n, estado de agrupación y ungroup; cobertura, denominadores,
ceros, desconocidos y vacío. Resume los 29 aceptados de 07.04: cuatro grupos,
177250 MXN y 18 atrasos ≥ 30, con conciliación pandas sobre la misma población.
Muestra mínima independiente para faltantes; factores como ampliación opcional.
Preparación desde R, mismo proyecto/lockfile y sin dependencias nuevas.

<a id="06-unir-tablas"></a>

### 06 — Unir tablas

Disponible: [lección 07.06](06_join_tables/README.md) y
[lab 07.06](../../labs/07_tidyverse/06_join_tables/README.md).
left_join/inner_join y semi_join/anti_join; claves, relationship y na_matches,
cardinalidad frente a cobertura. Catálogo estático sobre los 29 aceptados:
19 coincidencias/10 sin catálogo, 177250 MXN conservados; seis etiquetas
desconocidas y una clave sin uso distinguidas. Multiplicación, claves compuestas
y NA demostrados; conciliación pandas/SQLite. Mismo proyecto, sin paquetes nuevos.

<a id="07-datos-ordenados-y-reshape"></a>

### 07 — Datos ordenados y reshape

- Una variable por columna y una observación por fila; pivot_longer/pivot_wider.
  Definir claves antes de reorganizar y distinguir reshape de agregación.
- Práctica prevista: comparar cortes en formatos largo y ancho, detectando
  combinaciones repetidas o ausentes que afectan el resultado.

<a id="08-texto-categorias-y-factores"></a>

### 08 — Texto, categorías y factores

- stringr para espacios y patrones sencillos; factores y forcats para niveles
  y orden. Los patrones avanzados se amplían después de un caso básico.
- Práctica prevista: normalizar un segmento sin colapsar categorías distintas,
  revisar niveles desconocidos y ordenar categorías para una figura.

<a id="09-fechas-y-cortes"></a>

### 09 — Fechas y cortes

- lubridate, parseo y fechas inválidas; fechas frente a instantes, períodos y zonas
  horarias solo cuando el origen incluya horas.
- Práctica prevista: seleccionar cortes y calcular una diferencia temporal con
  unidades definidas, conciliando el período con Python.

<a id="10-primera-figura-y-cierre-del-analisis"></a>

### 10 — Primera figura y cierre del análisis

- ggplot, aes y una geometría de barras o líneas; títulos, unidades y ggsave.
  Distinguir contar registros de graficar un indicador ya agregado.
- Práctica prevista: reconstruir limpieza, indicadores y figura desde una sesión
  nueva, comparar con pandas/SQL y explicar el hallazgo sin atribuir causalidad.

## Prácticas, proyecto y criterio de salida

Los labs 07.01–07.06 están disponibles; 07.07–07.10 siguen previstos. El proyecto previsto
03_portfolio_analysis_r, registrado en [proyectos](../../projects/README.md),
todavía no tiene carpeta ni checkpoints implementados.

Checkpoints propuestos: CP-01, importación y contrato (01–03); CP-02, calidad
(04); CP-03, indicadores y relaciones (05–07); CP-04, categorías, cortes y
primera figura (08–10). Se concretarán al desarrollar el proyecto.

El cierre requiere tablas reproducibles, reglas justificadas, conteos e indicadores
conciliados y una gráfica explicada. DBI/RSQLite y consultas remotas con dbplyr
son extensiones para reutilizar el conocimiento SQL, no requisitos de instalación
inicial. Arrow y Parquet se desarrollan en 09; Quarto en 11 y Shiny en 13.

## Continuidad y referencias

Después del cierre, continúa con [08 — Visualización en R](../08_visualization_r/README.md).

Lecturas de R for Data Science: [transformación](https://r4ds.hadley.nz/data-transform.html),
[datos ordenados](https://r4ds.hadley.nz/data-tidy.html),
[uniones](https://r4ds.hadley.nz/joins.html),
[factores](https://r4ds.hadley.nz/factors.html) y
[fechas](https://r4ds.hadley.nz/datetimes.html).
Para controles vigentes se consultará [la referencia de joins de dplyr](https://dplyr.tidyverse.org/reference/mutate-joins.html).
Los libros y su uso por nivel están en la [guía de lecturas](../../docs/r-reading-guide.md).

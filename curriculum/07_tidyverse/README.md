# 07 — tidyverse

## Propósito y prerrequisitos

Transformar tablas de manera expresiva y comprobable con dplyr, tidyr y paquetes
relacionados. Completa [R fundamental](../06_r_foundations/README.md) y reutiliza
sus datos y proyecto renv; no se crea un entorno independiente por cada ejercicio.
El [cierre 06.09](../06_r_foundations/09_known_result/README.md) está disponible
con conciliación Python/R.

**Estado:** 07.01 dispone de lección, scripts, lockfile y lab; 07.02–07.10
siguen planificadas. Los enlaces internos describen el alcance pendiente.

Usaremos la misma cartera sintética e indicadores conocidos de pandas/SQL.
La primera figura con ggplot2 aparece aquí; el módulo 08 profundiza su diseño.
R for Data Science inspira contenidos, pero adaptamos su orden a los prerrequisitos
ya trabajados en DS Track, sin exigir leer el libro completo.

## Orden de desarrollo

| Orden | Sección | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Tibbles, importación y pipes](01_tibbles_import_pipes/README.md) | Esencial | Cargar una tabla y leer una secuencia de pasos |
| 2 | [Seleccionar, filtrar y ordenar](#02-seleccionar-filtrar-y-ordenar) | Esencial | Obtener un subconjunto verificable |
| 3 | [Transformar columnas](#03-transformar-columnas) | Esencial | Calcular indicadores con reglas explícitas |
| 4 | [Faltantes, duplicados y calidad](#04-faltantes-duplicados-y-calidad) | Esencial | Conservar aceptados y rechazos con motivos |
| 5 | [Agrupar y resumir](#05-agrupar-y-resumir) | Esencial | Conciliar medidas y denominadores |
| 6 | [Unir tablas](#06-unir-tablas) | Esencial | Detectar relaciones que multiplican registros |
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

<a id="02-seleccionar-filtrar-y-ordenar"></a>

### 02 — Seleccionar, filtrar y ordenar

- select, rename, filter y arrange; condiciones y comportamiento ante NA.
- Práctica prevista: comparar una selección con pandas/SQL, incluso cuando no
  hay coincidencias. Los nombres de fila no sustituyen identificadores de origen.

<a id="03-transformar-columnas"></a>

### 03 — Transformar columnas

- mutate, operaciones vectorizadas, if_else y case_when; conversiones explícitas.
- Práctica prevista: crear una clasificación con fronteras conocidas y registrar
  conversiones fallidas. across se ofrece como ampliación tras dominar un campo.

<a id="04-faltantes-duplicados-y-calidad"></a>

### 04 — Faltantes, duplicados y calidad

- is.na, distinct, claves y reglas; separar faltante explícito de combinación
  ausente. Reemplazar o eliminar solo con una decisión justificada.
- Práctica prevista: detalle de aceptados/rechazos y conteos conciliados;
  no usar distinct para ocultar problemas en una unión.

<a id="05-agrupar-y-resumir"></a>

### 05 — Agrupar y resumir

- group_by, summarise, n y medidas sobre grupos; estado de agrupación y ungroup.
  Revisar denominadores, sumas de valores desconocidos y grupos vacíos.
- Práctica prevista: conciliar saldo y registros por segmento con un corte conocido.
  Acumulados y funciones de ventana quedan como ampliación de esa pregunta.

<a id="06-unir-tablas"></a>

### 06 — Unir tablas

- left_join/inner_join, claves explícitas y cardinalidad; semi_join y anti_join
  para detectar coincidencias y ausencias. Verificar controles de relaciones en
  la versión de dplyr elegida y decidir cómo tratar claves faltantes.
- Práctica prevista: agregar un catálogo sin inflar el saldo; comparar con el join SQL.

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

El lab 07.01 está disponible; 07.02–07.10 siguen previstos. El proyecto previsto
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

# 07 — tidyverse

[Inicio](../../README.md) / [Módulos](../README.md) / **07 — tidyverse**

**Transforma tablas en R sin perder sus claves, cobertura o significado.**

[**Empezar por 07.01 →**](01_tibbles_import_pipes/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 10 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Preparar, transformar y combinar tablas con dplyr, tidyr y paquetes relacionados, contrastando reglas e indicadores con resultados conocidos.

## Antes de empezar

Completa [06 — R fundamental](../06_r_foundations/README.md), incluido [06.09](../06_r_foundations/09_known_result/README.md). Reutiliza su proyecto renv y sigue los preparadores con respaldos; no crees un entorno nuevo por cada ejercicio.

## Qué vas a aprender

- Importar e inspeccionar tablas preservando tipos y unidades.
- Seleccionar, transformar y validar registros.
- Resumir, unir y cambiar la forma sin alterar indicadores.
- Trabajar con categorías y fechas explícitas.
- Reconstruir un resultado y explicar una primera figura.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **07.01** · [Tibbles, importación y pipes](01_tibbles_import_pipes/README.md) | [Lab 07.01](../../labs/07_tidyverse/01_tibbles_import_pipes/README.md) | Cargar una tabla y leer una secuencia de pasos |
| **07.02** · [Seleccionar, filtrar y ordenar](02_select_filter_sort/README.md) | [Lab 07.02](../../labs/07_tidyverse/02_select_filter_sort/README.md) | Obtener un subconjunto verificable |
| **07.03** · [Transformar columnas](03_transform_columns/README.md) | [Lab 07.03](../../labs/07_tidyverse/03_transform_columns/README.md) | Calcular indicadores con reglas explícitas |
| **07.04** · [Faltantes, duplicados y calidad](04_missing_duplicates_quality/README.md) | [Lab 07.04](../../labs/07_tidyverse/04_missing_duplicates_quality/README.md) | Conservar aceptados y rechazos con motivos |
| **07.05** · [Agrupar y resumir](05_group_summarize/README.md) | [Lab 07.05](../../labs/07_tidyverse/05_group_summarize/README.md) | Conciliar medidas y denominadores |
| **07.06** · [Unir tablas](06_join_tables/README.md) | [Lab 07.06](../../labs/07_tidyverse/06_join_tables/README.md) | Detectar relaciones que multiplican registros |
| **07.07** · [Datos ordenados y reshape](07_tidy_reshape/README.md) | [Lab 07.07](../../labs/07_tidyverse/07_tidy_reshape/README.md) | Cambiar formato preservando indicadores |
| **07.08** · [Texto, categorías y factores](08_text_categories_factors/README.md) | [Lab 07.08](../../labs/07_tidyverse/08_text_categories_factors/README.md) | Normalizar categorías y controlar su orden |
| **07.09** · [Fechas y cortes](09_dates_cutoffs/README.md) | [Lab 07.09](../../labs/07_tidyverse/09_dates_cutoffs/README.md) | Comparar períodos con fechas interpretadas |
| **07.10** · [Primera figura y cierre del análisis](10_first_plot_closure/README.md) | [Lab 07.10](../../labs/07_tidyverse/10_first_plot_closure/README.md) | Reconstruir tablas e interpretar un gráfico |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

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

Disponible: [lección 07.07](07_tidy_reshape/README.md) y
[lab 07.07](../../labs/07_tidyverse/07_tidy_reshape/README.md).
pivot_wider/pivot_longer, claves de celda, tipos y NA explícito frente a combinación
ausente. Reutiliza las 48 observaciones de pandas 02.07: proyección 48 × 3,
ancho 24 × 3 y vuelta exacta; inventario de claves para huecos de combinación.
Saldos 47200/46700 MXN y cobertura 21/24 por corte, conciliados con pandas.
Mismo proyecto renv, respaldo 07.06 y lockfile real con tidyr 1.3.2.

<a id="08-texto-categorias-y-factores"></a>

### 08 — Texto, categorías y factores

Disponible: [lección 07.08](08_text_categories_factors/README.md) y
[lab 07.08](../../labs/07_tidyverse/08_text_categories_factors/README.md).
stringr para espacios, minúsculas y patrones sencillos; equivalencias exactas
con origen conservado. Muestra de pandas 02.06: 48 registros, 45 segmentos
reconocidos y tres pendientes; fechas/IDs sin validar. Factores estrictos,
niveles nominales, orden manual/por medida y grupos vacíos sin alterar importes.
Stringr directo y forcats 1.0.1 en el mismo proyecto con respaldo y lockfile real.

<a id="09-fechas-y-cortes"></a>

### 09 — Fechas y cortes

Disponible: [lección 07.09](09_dates_cutoffs/README.md) y
[lab 07.09](../../labs/07_tidyverse/09_dates_cutoffs/README.md).
Fechas ISO, calendario/rango, diferencias en días, relaciones y claves normalizadas.
Reutiliza la fuente de 07.08: 48 = 36 aceptados + 12 rechazados, motivos conservados;
18 aceptados por corte y 14 IDs comunes con diferencia 2800 MXN. Intervalos con
fin exclusivo y población explícita, conciliados con pandas/datetime. Lubridate
1.9.5 en el mismo proyecto renv, con respaldo y restauración local real.

<a id="10-primera-figura-y-cierre-del-analisis"></a>

### 10 — Primera figura y cierre del análisis

Disponible: [lección 07.10](10_first_plot_closure/README.md) y
[lab 07.10](../../labs/07_tidyverse/10_first_plot_closure/README.md).
Reconstruye 07.09 desde el CSV original: 48 = 36 + 12, 14 IDs comunes y saldos
29000/31800 MXN. ggplot/aes/geom_col frente a conteo con geom_bar, etiquetas,
unidades y exportación explícita. Tablas, RDS y PNG en destino nuevo; verificación
de entrega desde sesión nueva y contraste pandas/SQLite. ggplot2 4.0.3 con
lockfile y respaldo 07.09, restauración local y límites descriptivos explícitos.

</details>

## Cómo trabajar este módulo

En el IDE, abre el proyecto, edita scripts y compara resultados por bloques; después comprueba una sesión nueva. Las dependencias se incorporan por sección. No instales todo tidyverse por anticipado. SQL remoto con dbplyr y DBI/RSQLite son ampliaciones; Arrow y Quarto se estudian después.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Tablas y reglas | Tipos, particiones, claves y cobertura |
| Código y resúmenes | Filas e indicadores conciliados |
| Figura y entrega | Reconstrucción e interpretación del cierre |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Puedes reconstruir tablas con reglas justificadas, conciliar conteos e indicadores y explicar una gráfica. Otra persona debe poder seguir las instrucciones del cierre con las entradas declaradas.

03_portfolio_analysis_r está previsto en [proyectos](../../projects/README.md); carpeta y checkpoints siguen pendientes. Consulta también [el cierre tidyverse](../../docs/tidyverse-closure.md).

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, importación y contrato (01–03); CP-02, calidad
(04); CP-03, indicadores y relaciones (05–07); CP-04, categorías, cortes y
primera figura (08–10). Se concretarán al desarrollar el proyecto.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 07.01](01_tibbles_import_pipes/README.md) y realiza su lab.

**Al cerrar:** continúa con [08 — Visualización en R](../08_visualization_r/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Lecturas de R for Data Science: [transformación](https://r4ds.hadley.nz/data-transform.html),
[datos ordenados](https://r4ds.hadley.nz/data-tidy.html),
[uniones](https://r4ds.hadley.nz/joins.html),
[factores](https://r4ds.hadley.nz/factors.html) y
[fechas](https://r4ds.hadley.nz/datetimes.html).
Para controles vigentes se consultará [la referencia de joins de dplyr](https://dplyr.tidyverse.org/reference/mutate-joins.html).
Los libros y su uso por nivel están en la [guía de lecturas](../../docs/r-reading-guide.md).

### Apoyos relacionados

- [08.01 — Pregunta y gramática de gráficos](../08_visualization_r/01_question_grammar/README.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_tibbles_import_pipes/README.md)

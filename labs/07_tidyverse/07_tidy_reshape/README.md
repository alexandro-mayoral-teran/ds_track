# Lab 07.07 — Cambiar de forma conservando claves y faltantes

## Propósito, entradas y resultado

Practica la [lección 07.07](../../../curriculum/07_tidyverse/07_tidy_reshape/README.md)
en el mismo proyecto RStudio/IDE. Prepara los archivos y restaura el lockfile
de la lección una vez: tidyr se añade a la biblioteca local, con respaldo de
metadatos anteriores. No inicialices otro proyecto renv ni cambies Conda.

La entrada es datos/cartera_formas.csv: copia de la muestra de 48 observaciones
de pandas 02.07, distinta de los 29 aceptados de 07.04–07.06. Conserva esas
fuentes y resultados. Entrega output/mis_formas.R con ancho, claves presentes,
recuperado y controles, además de una explicación de lo conservado. No se pide
exportar, graficar ni crear un checkpoint integrador, todavía pendiente.

## 1. Anticipar unidades y forma

Escribe la clave de cada fila larga y ancha y la clave de una celda de saldo.
¿Qué columnas recuperarás y cuáles no? ¿Cuántas filas esperas antes y después?

<details>
<summary>Comprobar el razonamiento</summary>

Largo: ID/corte; ancho: ID; celda: ID más el corte que dio nombre a la columna.
La proyección conserva ID, corte y saldo; segmento/atraso siguen en fuente,
pero no se reconstruyen desde ella. Esperamos 48 × 3 → 24 × 3 → 48 × 3.
Los cortes son etiquetas de texto, sin convertirlas todavía a fechas de R.

</details>

## 2. Leer y seleccionar sin modificar la fuente

Abre la práctica, reinicia R y comprueba getwd() en Console. Crea el script
en el editor manteniendo la raíz de la práctica como directorio:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_formas.R", encoding = "UTF-8")
ruta <- "datos/cartera_formas.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_fuente_formas(ruta)
original <- fuente
largo <- fuente |> dplyr::select(id_credito, corte = fecha_corte, saldo_mxn)
claves_presentes <- largo |> dplyr::select(id_credito, corte)
```

Inspecciona tipos, claves, cortes y saldos faltantes. Explica por qué este
contrato permite NA sin modificar los rechazos del ejercicio anterior.

<details>
<summary>Comprobación posible</summary>

```r
validar_proyeccion(largo)
stopifnot(identical(dim(fuente), c(48L, 5L)), is.integer(largo$saldo_mxn),
          length(unique(largo$id_credito)) == 24L,
          sum(is.na(largo$saldo_mxn)) == 6L)
```

Es otra población y otro contrato analítico. No hay que ejecutar evaluar_calidad
de 07.04 sobre esta fuente ni reemplazar los datos anteriores.

</details>

## 3. Ensanchar y volver a largo

Escribe pivot_wider declarando id_cols, names_from y values_from; añade el
prefijo saldo_ y ordena por ID. Luego escribe pivot_longer sobre las dos
columnas de saldo, conserva NA y compara con las funciones reutilizables:

```r
ancho <- largo_a_ancho(largo)
recuperado <- recuperar_saldos(ancho, claves_presentes)
comprobar_formas(largo, ancho, claves_presentes, recuperado)
```

<details>
<summary>Una solución razonada</summary>

```r
propio <- largo |>
  tidyr::pivot_wider(id_cols = id_credito, names_from = corte,
                     values_from = saldo_mxn, names_prefix = "saldo_", names_sort = TRUE) |>
  dplyr::arrange(id_credito)
vuelta <- propio |>
  tidyr::pivot_longer(cols = dplyr::all_of(columnas_ancho[-1]), names_to = "corte",
                      names_prefix = "saldo_", values_to = "saldo_mxn",
                      values_ptypes = list(saldo_mxn = integer()), values_drop_na = FALSE) |>
  dplyr::arrange(id_credito, corte)
stopifnot(identical(as.list(propio), as.list(ancho)),
          identical(as.list(vuelta), as.list(recuperado)),
          identical(dim(ancho), c(24L, 3L)), nrow(recuperado) == 48L)
```

Aquí todas las combinaciones existen, por eso la rejilla coincide con el
detalle recuperado. all_of selecciona los nombres exactos del vector; el
prefijo se retira al volver a largo. No se agregan ni rellenan cantidades.

</details>

Comprueba controles por corte: registros, saldos conocidos y suma observada.
Explica por qué no basta comparar una suma de los dos cortes juntos.

<details>
<summary>Cifras y límites</summary>

```r
controles <- control_por_corte(recuperado)
stopifnot(identical(controles$registros, c(24L, 24L)),
          identical(controles$conocidos, c(21L, 21L)),
          identical(controles$saldo_observado_mxn, c(47200, 46700)))
```

Cobertura 21/24 = 87.5 % en cada corte. Son sumas observadas, no saldos
completos. Trasladar un saldo entre créditos o cortes podría conservar una
suma global y cambiar los datos. La comparación completa revisa cada clave,
tipo, valor y NA; los indicadores son un control adicional.

</details>

## 4. Distinguir ausencia de observación y saldo desconocido

Reproduce la muestra mini de la sección 6 de la lección y su inventario.
Predice cuántas filas tendrá la rejilla y cuántas deben recuperarse.

<details>
<summary>Solución y comprobaciones</summary>

```r
mini <- tibble::tibble(
  id_credito = c("A", "A", "B", "C"),
  corte = c("2026-09-30", "2026-10-31", "2026-09-30", "2026-10-31"),
  saldo_mxn = c(100L, 80L, NA_integer_, 0L)
)
mini_claves <- mini |> dplyr::select(id_credito, corte)
mini_ancho <- largo_a_ancho(mini)
mini_rejilla <- ancho_a_rejilla(mini_ancho)
mini_recuperado <- recuperar_saldos(mini_ancho, mini_claves)
comprobar_formas(mini, mini_ancho, mini_claves, mini_recuperado)
stopifnot(nrow(mini_rejilla) == 6L, nrow(mini_recuperado) == 4L,
          sum(is.na(mini_recuperado$saldo_mxn)) == 1L,
          mini_recuperado$saldo_mxn[mini_recuperado$id_credito == "C"] == 0L)
```

B/septiembre tenía un saldo desconocido; B/octubre y C/septiembre no tenían
observaciones. Solo el inventario permite distinguir los tres NA del ancho.
El cero de C/octubre sí fue observado. Sin inventario no puedes reconstruir
la misma población basándote únicamente en si el saldo es NA.

</details>

Reproduce también el ensayo con values_drop_na = TRUE y values_fill = 0L
de la lección. Explica qué fila real se pierde y qué hueco se rellena. Déjalos
en objetos separados; no sustituyas mini_recuperado por esos ensayos.

## 5. Rechazar ambigüedades y probar vacío

En otro bloque, crea repetido añadiendo mini[1, ] con bind_rows. La función
debe detenerse antes de pivotar: misma clave, aunque el importe sea igual.
Este bloque produce **error esperado** y queda fuera del script correcto:

```r
# ERROR ESPERADO: ejecutar por separado.
repetido <- dplyr::bind_rows(mini, mini[1, ])
largo_a_ancho(repetido)
```

No utilices values_fn = sum ni distinct para ocultar la repetición. Explica
la diferencia entre resumir registros legítimos y reorganizar saldos únicos.
En el recorrido correcto comprueba una proyección vacía y el esquema estable:

```r
vacio <- largo[0, ]
vacio_ancho <- largo_a_ancho(vacio)
vacio_claves <- vacio |> dplyr::select(id_credito, corte)
vacio_recuperado <- recuperar_saldos(vacio_ancho, vacio_claves)
comprobar_formas(vacio, vacio_ancho, vacio_claves, vacio_recuperado)
stopifnot(nrow(vacio_ancho) == 0L, identical(names(vacio_ancho), columnas_ancho),
          is.integer(vacio_recuperado$saldo_mxn))
```

No hay observaciones; el esquema mantiene las dos columnas acordadas sin
crear créditos. Vacío, todos los saldos NA y todos los saldos cero son tres
situaciones distintas.

## 6. Reiniciar y conservar evidencia

Guarda output/mis_formas.R con carga, proyección, inventario, cambio de forma,
casos mini/vacío y comprobaciones correctas. Guarda aparte el error esperado.
Usa Session > Restart R, sin recuperar objetos anteriores, y ejecuta desde
Console en la raíz de la práctica:

```r
source("output/mis_formas.R", encoding = "UTF-8")
source("cambiar_forma.R", encoding = "UTF-8")
stopifnot(identical(fuente, original), identical(huella, tools::md5sum(ruta)))
```

También puedes usar Source desde el editor. Conserva script, versiones,
metadatos respaldados, formas, inventario y controles por corte. output/ y
las bibliotecas están ignorados; no los agregues con fuerza al repositorio.

Responde con tus palabras:

1. ¿Qué distingue ordenar filas de tener datos ordenados?
2. ¿Qué forma necesita tu pregunta y qué representa cada fila?
3. ¿Por qué una celda requiere ID más corte, y no solo ID?
4. ¿Qué información se pierde al guardar solo el ancho sin inventario?
5. ¿Por qué values_fill y values_drop_na necesitan una regla explícita?
6. ¿Por qué conservar las sumas no demuestra una vuelta correcta?

Puedes avanzar cuando reconstruyas los tres campos, conserves claves/NA/tipos
y expliques cobertura y límites desde una sesión nueva. Registra evidencia y
dudas en [PROGRESS.md](../../../PROGRESS.md); disponer del material no acredita
aprendizaje. No hay checkpoint integrador implementado asociado.

Siguiente: [07.08 — Texto, categorías y factores](../../../curriculum/07_tidyverse/08_text_categories_factors/README.md). Volver a la [lección 07.07](../../../curriculum/07_tidyverse/07_tidy_reshape/README.md).

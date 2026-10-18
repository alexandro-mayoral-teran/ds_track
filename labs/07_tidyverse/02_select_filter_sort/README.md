# Lab 07.02 — Obtener un subconjunto verificable

## Propósito, entradas y resultado

Practica la [lección 07.02](../../../curriculum/07_tidyverse/02_select_filter_sort/README.md)
en RStudio o tu IDE. Recibes las seis observaciones de cartera de 07.01, su
lector y el script de comprobación. Completa primero la preparación de 07.02
y restaura su lockfile en el **mismo proyecto**, sin repetir preparadores.

Entrega un script propio y una explicación que relacione cada verbo con
filas, columnas o nombres. Debe producir una selección ordenada, conservar
pendientes, resolver empates y comprobar una selección vacía. No se pide
exportación, gráficos ni un checkpoint integrador, todavía pendiente.

Puedes dividir el lab en dos sesiones: selección/condiciones y orden/vacíos.
El recorrido completo se realiza desde el IDE; no necesitas Terminal.

## 1. Anticipar antes de ejecutar

Escribe la pregunta: saldo ≥ 500 MXN **y** atraso ≥ 5 días. Con el CSV y su
diccionario, predice los identificadores que cumplen, no cumplen o quedan
pendientes. Indica qué filas cambian si sustituyes Y por O. No calcules una
conclusión de riesgo: estas reglas solo delimitan el subconjunto del ejercicio.

<details>
<summary>Comprobar el razonamiento</summary>

Cumplen 002, 003 y 006. No cumplen 001 y 004. En 005 el saldo cumple, pero
no se conoce el atraso: pendiente. Son 3 + 2 + 1 = 6. Con O entran 001, 002,
003, 005 y 006: cinco filas; TRUE | NA es TRUE. 004 no cumple ninguna.

</details>

## 2. Construir el script propio

Abre el mismo proyecto de práctica y comprueba getwd() en Console. Crea
output/mi_seleccion.R con File > New File > R Script; conserva como directorio
la raíz de la práctica. Empieza con:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_importacion.R", encoding = "UTF-8")
cartera <- leer_cartera("datos/cartera_demo.csv")
comprobar_muestra(cartera)
original <- cartera
```

Ejecuta por bloques con Run. Observa cartera en Environment y su visor; deja
las comprobaciones en el script. Usa filter para las condiciones confirmadas,
select para conservar id_credito/segmento/saldo_mxn/dias_atraso y arrange para
saldo descendente e identificador ascendente. Muestra el resultado con print.

<details>
<summary>Una solución posible</summary>

anyNA pregunta si hay algún faltante; al negarlo con ! comprobamos que todos
los saldos del subconjunto están presentes antes de sumar.

```r
seleccion <- cartera |>
  dplyr::filter(saldo_mxn >= 500, dias_atraso >= 5) |>
  dplyr::select(id_credito, segmento, saldo_mxn, dias_atraso) |>
  dplyr::arrange(dplyr::desc(saldo_mxn), id_credito)
print(seleccion, n = 6, width = Inf)
stopifnot(identical(seleccion$id_credito, c("002", "003", "006")),
          identical(seleccion$saldo_mxn, c(1500, 750, 500)),
          identical(dim(seleccion), c(3L, 4L)),
          !anyNA(seleccion$saldo_mxn), sum(seleccion$saldo_mxn) == 2750)
```

El subtotal de 2750 MXN corresponde a tres saldos conocidos de tres seleccionados.
No es el total de 6000 MXN de la muestra. En 006, saldo = 500 y atraso = 5
están incluidos porque la pregunta usa ≥. La identidad procede de la columna,
no de que una fila se imprima como 1, 2 o 3.

</details>

## 3. Separar negación y desconocimiento

Construye no_cumplen y pendientes sobre la condición completa. Comprueba claves
y que los tres grupos reúnen las seis filas sin intersecciones. Después crea
una selección con O y explica por qué 005 entra aunque tenga un faltante.

<details>
<summary>Solución razonada</summary>

```r
no_cumplen <- cartera |>
  dplyr::filter(!(saldo_mxn >= 500 & dias_atraso >= 5))
pendientes <- cartera |>
  dplyr::filter(is.na(saldo_mxn >= 500 & dias_atraso >= 5))
alternativa_o <- cartera |>
  dplyr::filter((saldo_mxn >= 500) | (dias_atraso >= 5))
stopifnot(identical(no_cumplen$id_credito, c("001", "004")),
          identical(pendientes$id_credito, "005"),
          nrow(seleccion) + nrow(no_cumplen) + nrow(pendientes) == 6L,
          identical(alternativa_o$id_credito, c("001", "002", "003", "005", "006")))
```

Las claves esperadas son distintas y reúnen 001–006: no basta comprobar solo
la suma de conteos. !NA no se vuelve TRUE, por lo que negar el filtro no
incluye la pendiente. No cambiamos los datos; formulamos tres preguntas.

</details>

## 4. Renombrar y reconocer una secuencia inválida

Crea presentacion cambiando saldo_mxn a saldo_pesos con rename. Comprueba que
seleccion conserva el nombre original y que ambas columnas tienen los mismos
valores. Después lee esta secuencia: ¿por qué fallará?

```r
# Error esperado: ejecutar aparte, no dejarlo en el script de reconstruccion.
cartera |>
  dplyr::select(id_credito, saldo_mxn) |>
  dplyr::filter(dias_atraso >= 5)
```

<details>
<summary>Solución y diagnóstico</summary>

`%in%` comprueba pertenencia: aquí pregunta si un texto está entre los nombres
de columnas, como en el [comparador de 06.09](../../../curriculum/06_r_foundations/09_known_result/README.md).

```r
presentacion <- seleccion |> dplyr::rename(saldo_pesos = saldo_mxn)
stopifnot("saldo_mxn" %in% names(seleccion),
          "saldo_pesos" %in% names(presentacion),
          identical(presentacion$saldo_pesos, seleccion$saldo_mxn))
```

En la secuencia errónea, select retiró dias_atraso antes de que
filter la necesitara. Filtra primero o conserva esa columna hasta utilizarla.
Renombrar no convierte moneda ni recalcula saldos. No edites la fuente para
resolver un error de secuencia.

</details>

## 5. Empates, faltantes de orden y vacío

Construye esta tabla pequeña adicional en memoria. No reemplaces cartera:

```r
empates <- tibble::tibble(
  id_credito = c("B02", "B01", "B03", "B04"),
  saldo_mxn = c(500, 500, 750, NA_real_)
)
```

Ordena por saldo descendente e ID ascendente. Predice dónde queda B04 y qué
resuelve el segundo criterio. En la cartera original, pregunta por saldo > 10000,
selecciona las mismas cuatro columnas y ordena. Comprueba tamaño, nombres y
tipos aunque no haya coincidencias; no intentes extraer un primer crédito.

<details>
<summary>Una solución posible</summary>

```r
empates_ordenados <- empates |>
  dplyr::arrange(dplyr::desc(saldo_mxn), id_credito)
stopifnot(identical(empates_ordenados$id_credito, c("B03", "B01", "B02", "B04")))
vacia <- cartera |>
  dplyr::filter(saldo_mxn > 10000) |>
  dplyr::select(id_credito, segmento, saldo_mxn, dias_atraso) |>
  dplyr::arrange(dplyr::desc(saldo_mxn), id_credito)
stopifnot(identical(dim(vacia), c(0L, 4L)),
          identical(names(vacia), names(seleccion)),
          identical(vapply(vacia, typeof, character(1)),
                    vapply(seleccion, typeof, character(1))),
          identical(cartera, original))
```

B03 tiene el mayor saldo; B01 precede a B02 en el empate de 500; el saldo
desconocido B04 queda al final en esta tabla local. La ausencia de coincidencias
es una respuesta válida que conserva el esquema. No informa un saldo observado
de cero. Una variante con saldo ≥ 5000 también queda vacía en esta muestra.

</details>

## 6. Reconstruir, comparar y registrar

Guarda el script propio con los bloques correctos; mantén el error deliberado
en otro archivo o ejecútalo aparte. Usa Session > Restart R, abre la misma
práctica y comprueba que no se restauran objetos de un workspace anterior.
Ejecuta en Console desde la raíz de la práctica:

```r
source("output/mi_seleccion.R", encoding = "UTF-8")
source("seleccionar_cartera.R", encoding = "UTF-8")
```

También puedes usar Source sobre el archivo abierto, manteniendo ese directorio.
Ambos scripts deben reconstruir la carga y pasar los controles; limpiar el texto
de Console no sustituye reiniciar R. La ejecución del script incluido compara
la huella del CSV antes/después y comprueba que el objeto original se conservó.

Compara la selección con [pandas 02.03](../../../curriculum/02_pandas/03_select_filter_sort/README.md):
misma fuente, corte, umbrales y orden; mismas claves 002/003/006 y 2750 MXN.
No necesitas ejecutar Python o SQL para completar este lab. Explica cómo SELECT,
WHERE y ORDER BY expresan la misma pregunta; la lección incluye la equivalencia.

Conserva como evidencia el script, versiones, claves/valores esperados, grupos
3/2/1 y tus explicaciones de NA, empate y vacío. output/ queda ignorado; no
agregues bibliotecas o resultados de práctica con fuerza a Git.

Preguntas de reflexión:

1. ¿Qué verbo cambia columnas, cuál filas y cuál solo su orden?
2. ¿Por qué 005 no está entre quienes no cumplen ni entre los confirmados?
3. ¿Por qué ordenar por saldo no basta para expresar cómo resolver empates?
4. ¿Qué demuestra comprobar claves además de contar filas?
5. ¿Qué se perdió al quitar una columna antes de necesitarla?

Puedes avanzar cuando reconstruyas desde una sesión nueva, justifiques las
filas, distingas NA de cero y compruebes el vacío sin alterar la fuente.
Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md); la disponibilidad
del material no acredita el aprendizaje. No hay checkpoint integrador implementado.

Siguiente: [07.03 — Transformar columnas](../../../curriculum/07_tidyverse/03_transform_columns/README.md),
con lección y lab disponibles. Volver a la [lección 07.02](../../../curriculum/07_tidyverse/02_select_filter_sort/README.md).

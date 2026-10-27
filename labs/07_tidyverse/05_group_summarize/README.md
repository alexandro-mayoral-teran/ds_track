# Lab 07.05 — Indicadores por grupo con denominadores explícitos

## Propósito, entradas y resultado

Practica la [lección 07.05](../../../curriculum/07_tidyverse/05_group_summarize/README.md)
en el mismo proyecto RStudio/IDE. Prepara sus dos archivos una sola vez según
la lección. Usa el CSV de 44 registros de 07.04 y conserva sus rechazos.
No necesitas nuevos paquetes ni otra muestra de cartera.

Entrega output/mi_resumen.R, los controles ejecutados desde una sesión nueva y
una explicación de población, unidades y denominadores. La muestra mini se crea
en memoria y se identifica por separado. No se pide exportar datos ni producir
una figura. El proyecto/checkpoint integrador sigue pendiente.

## 1. Anticipar la forma

Antes de ejecutar, escribe la clave del detalle, la del resumen y qué filas
formarán la población. ¿Qué cambiaría al incluir rechazados o varios cortes?

<details>
<summary>Comprobar el razonamiento</summary>

Detalle: ID/corte. Resumen: corte/segmento. Población principal: 29 aceptados,
no las 44 entradas. Habrá cuatro grupos en el único corte 2026-09-30. Los
rechazos siguen disponibles con motivos; incluirlos cambiaría el contrato.
En varios cortes contaríamos observaciones crédito/corte; un mismo crédito
podría contarse más de una vez. El saldo siempre necesita una fecha de referencia.

</details>

## 2. Reconstruir la base

Abre la práctica, reinicia R y comprueba getwd() en Console. Crea el script
en el editor manteniendo la raíz del proyecto como directorio. Ejecuta por bloques:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_resumen.R", encoding = "UTF-8")
ruta <- "datos/cartera_calidad.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_conversion(ruta)
original <- fuente
revision <- evaluar_calidad(fuente)
detalle <- revision$aceptados
detalle_original <- detalle
```

Explica las advertencias de conversión conocidas. Comprueba 29 aceptados,
15 rechazados y unicidad de ID/corte antes de obtener indicadores.

<details>
<summary>Una comprobación posible</summary>

```r
stopifnot(nrow(detalle) == 29L, nrow(revision$rechazados) == 15L,
          !anyNA(detalle[c("id_credito", "fecha_corte")]),
          !anyDuplicated(detalle[c("id_credito", "fecha_corte")]))
```

No se usa distinct para hacer desaparecer una repetición. Las reglas de
07.04 ya apartaron todas las apariciones de las claves repetidas.

</details>

## 3. Resumir y conciliar

Escribe primero un group_by/summarise con n(), suma de saldo y conteo de
atrasos conocidos; pide una salida sin agrupación. Después usa la función
de la lección y compara tus cifras. Inspecciona las doce columnas:

```r
resumen <- resumir_grupos(detalle)
comprobar_resumen(detalle, resumen)
print(resumen, width = Inf)
```

<details>
<summary>Solución razonada y cifras esperadas</summary>

```r
propio <- detalle |>
  dplyr::group_by(fecha_corte, segmento) |>
  dplyr::summarise(
    registros = dplyr::n(),
    saldo_observado_mxn = suma_observada(saldo_mxn),
    atrasos_conocidos = sum(!is.na(dias_atraso)),
    .groups = "drop"
  ) |>
  dplyr::arrange(fecha_corte, segmento)
stopifnot(identical(propio$registros, c(8L, 5L, 10L, 6L)),
          identical(propio$saldo_observado_mxn, c(47000, 35250, 57000, 38000)),
          identical(propio$registros, resumen$registros),
          sum(resumen$registros) == 29L,
          sum(resumen$saldo_observado_mxn) == 177250,
          sum(resumen$atrasos_30_confirmados) == 18L,
          length(dplyr::group_vars(resumen)) == 0L)
```

En orden comercio/consumo/educacion/servicios, los confirmados ≥ 30 son 5/3/6/4.
Todos los campos requeridos están presentes en aceptados, por eso ambas
coberturas son 100 %. No concluyas lo mismo sobre la entrada de 44 registros.

</details>

## 4. Elegir el denominador

Calcula la tasa global y el promedio de saldo del conjunto a partir de las
bases del resumen. Contrástalos con la media simple de tasas y promedios de
los cuatro segmentos. Explica por qué esa media simple responde otra pregunta.

<details>
<summary>Solución razonada</summary>

```r
tasa_global <- sum(resumen$atrasos_30_confirmados) /
  sum(resumen$atrasos_conocidos) * 100
promedio_global <- sum(resumen$saldo_observado_mxn) / sum(resumen$saldos_conocidos)
stopifnot(abs(tasa_global - 18 / 29 * 100) < 1e-10,
          abs(promedio_global - 177250 / 29) < 1e-10)
print(c(tasa_global = tasa_global,
        media_tasas = mean(resumen$atraso_30_pct_conocidos)))
print(c(promedio_global = promedio_global,
        media_promedios = mean(resumen$saldo_promedio_conocido_mxn)))
```

La tasa conjunta es aproximadamente 62.07 % y el promedio 6112.07 MXN.
La media simple asigna igual peso a los cuatro segmentos, aunque tengan
8, 5, 10 y 6 registros. La tasa conjunta pondera por evaluaciones conocidas;
el promedio de saldo, por saldos conocidos. No redondees antes de comprobar.

</details>

Reproduce la demostración de dos cortes de la sección 5 de la lección.
Antes de ejecutar mutate, anticipa su denominador consultando group_vars.
Comprueba que ungroup cambia de porcentajes por corte a porcentajes globales.

## 5. Distinguir cero, desconocido y sin registros

Copia al script la definición de mini de la sección 6 de la lección. Calcula
mini_resumen por separado. Explica qué sabemos del saldo en a, b y c, y qué
significa el grupo NA. Comprueba la tabla vacía. Los factores son opcionales.

<details>
<summary>Comprobación y explicación</summary>

```r
mini <- tibble::tibble(
  id_credito = c("M1", "M2", "M3", "M4", "M5", "M6"),
  fecha_corte = rep("2026-09-30", 6),
  segmento = c("a", "a", "b", "b", "c", NA_character_),
  saldo_mxn = c(100L, NA_integer_, 0L, NA_integer_, NA_integer_, 50L),
  dias_atraso = c(30L, NA_integer_, 0L, 60L, NA_integer_, 30L)
)
mini_resumen <- resumir_grupos(mini)
comprobar_resumen(mini, mini_resumen)
stopifnot(nrow(mini_resumen) == 4L,
          sum(mini_resumen$registros) == 6L,
          sum(mini_resumen$saldos_conocidos) == 3L,
          sum(mini_resumen$atrasos_conocidos) == 4L,
          suma_observada(mini_resumen$saldo_observado_mxn) == 150,
          sum(mini_resumen$atrasos_30_confirmados) == 3L,
          nrow(resumir_grupos(mini[0, ])) == 0L)
```

a tiene 100 observados en un saldo conocido de dos filas, no un total completo.
b tiene un cero observado y otro saldo desconocido. c existe pero no tiene
cantidades conocidas: suma NA, cobertura cero y tasa NA. M6 se conserva en
el grupo de segmento NA; .drop no sirve para excluir esa clave ausente.
La tasa conjunta es 3/4 = 75 %, con cobertura de atraso 4/6 ≈ 66.67 %.
Una categoría de texto sin ninguna fila no aparece como grupo.

</details>

En un bloque aislado, cambia dos sumas del resumen conservando su total.
Este bloque debe producir **error esperado**; mantenlo fuera del script correcto:

```r
alterado <- resumen
alterado$saldo_observado_mxn[1:2] <- alterado$saldo_observado_mxn[1:2] + c(10, -10)
stopifnot(sum(alterado$saldo_observado_mxn) == sum(resumen$saldo_observado_mxn))
comprobar_resumen(detalle, alterado)
```

La suma global pasó, pero las cifras de comercio y consumo dejaron de corresponder
al detalle. No cambies el detalle para justificar el resumen alterado.

## 6. Reiniciar, explicar y conservar evidencia

Guarda output/mi_resumen.R con carga, agrupación, cálculos, muestra mini y
comprobaciones correctas. Conserva aparte el ensayo que debe fallar. Usa
Session > Restart R sin recuperar el workspace anterior. En Console, desde
la raíz de la práctica:

```r
source("output/mi_resumen.R", encoding = "UTF-8")
source("resumir_cartera.R", encoding = "UTF-8")
stopifnot(identical(fuente, original), identical(detalle, detalle_original),
          identical(huella, tools::md5sum(ruta)))
```

También puedes usar Source desde el editor. Conserva script, versiones,
cuatro grupos, conciliación 29/177250/18 y mini con su cobertura. output/
está ignorado; no agregues con fuerza resultados ni bibliotecas al repositorio.

Responde con tus palabras:

1. ¿Por qué n() no siempre es el denominador de una tasa?
2. ¿Qué diferencia hay entre agrupar y resumir? ¿Qué detalle se pierde?
3. ¿Cómo puede una agrupación persistente cambiar un porcentaje?
4. ¿Por qué cero casos confirmados no garantiza una tasa cero?
5. ¿Qué detectó comparar por grupo que no detectó la suma global?
6. ¿Por qué 100 % de cobertura entre aceptados no describe toda la entrada?

Puedes avanzar cuando reconstruyas y expliques las cifras, el estado de
agrupación y los casos NA/cero/vacío. Registra evidencia y dudas en
tu bitácora personal junto a la práctica; la disponibilidad del material no acredita
aprendizaje. No hay checkpoint integrador implementado asociado.

Siguiente: [07.06 — Unir tablas](../../../curriculum/07_tidyverse/06_join_tables/README.md). Volver a la [lección 07.05](../../../curriculum/07_tidyverse/05_group_summarize/README.md).

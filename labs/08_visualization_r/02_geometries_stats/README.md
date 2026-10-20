# Lab 08.02 — Geometrías y transformaciones estadísticas

## Propósito y entradas

Elegir una geometría, anticipar qué calcula y comprobar el resultado. Lee
primero la [lección 08.02](../../../curriculum/08_visualization_r/02_geometries_stats/README.md).
Usa el mismo proyecto renv de 07.10/08.01 y conserva su fuente, funciones,
lockfile y entregas. No hay instalaciones ni nuevas fuentes principales.

En RStudio o tu IDE, crea `output/mi_geometrias_lab.R`. Trabaja en Console de R
con la raíz del proyecto como directorio, no desde Terminal. Ten disponible
`output/mi_geometrias.R`, construido durante la lección. El lab no requiere
guardar figuras en disco: sí inspeccionarlas y explicar sus tablas.

## Actividad esencial

1. Sin ejecutar, elige tabla y geometría para: suma por fecha, cantidad de
   créditos por fecha, concentración de saldos en septiembre, relación entre
   saldos del mismo ID y distribución por corte. Escribe la unidad de cada eje.
2. Reconstruye el recorrido desde el CSV. Justifica 2 filas resumidas, 14 pares
   y 28 observaciones. Predice y luego comprueba 29000/31800 MXN con `geom_col`,
   1/1 con conteo del resumen y 14/14 con conteo del detalle.
3. Revisa línea y dispersión: identifica los dos cortes realmente observados y
   el ID de dos puntos. Explica por qué el trazo no son observaciones diarias
   y por qué la alineación de los pares no demuestra causas.
4. Cambia **solo los bordes** del histograma de septiembre a 1000, 2000, 3000
   y 4000. Anticipa dónde cae 2000 con cierre derecho. Comprueba las nuevas
   frecuencias con `hist` y la tabla de la capa. Justifica qué cambió y qué se
   conserva. Mantén 14 créditos, no mezcles fechas ni alteres saldos.
5. Comprueba los cuartiles de septiembre y octubre en las cajas de la lección.
   Calcula IQR, límites de referencia y bigotes de septiembre. Explica por qué
   no debes hacer esas cajas con solo los dos totales.
6. En una **muestra didáctica independiente** de cinco saldos, 100, 110, 120,
   130 y 1000 MXN, calcula Q1/mediana/Q3 tipo 7, límites y bigotes. Dibuja caja
   más todos los puntos. Identifica el valor exterior sin borrarlo ni cambiar
   las reglas de aceptación de la cartera principal.
7. Guarda, reinicia R y ejecuta el script completo desde sesión nueva. Reúne
   las comprobaciones y escribe una explicación por cada geometría, incluyendo
   lo que oculta o no permite concluir. Anota una duda o corrección real.

## Resultados y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Tablas principales | 2 resumen / 14 pares / 28 detalle; 14 por corte |
| Sumas y conteos | 29000/31800 MXN; resumen contado 1/1; detalle contado 14/14 |
| Histograma con 1000 MXN de ancho | Frecuencias 7, 5, 2; suma 14; cierre derecho |
| Caja septiembre | Q1 1475; mediana 2050; Q3 2575; bigotes 1100/3200 |
| Caja octubre | Q1 1675; mediana 2250; Q3 2775; bigotes 1300/3400 |
| Muestra independiente | Q1 110; mediana 120; Q3 130; IQR 20; límites 80/160; bigotes 100/130; exterior 1000 conservado |
| Reconstrucción | Fuente intacta; cifras reproducidas sin workspace anterior |

La suma de frecuencias no basta: comprueba bordes, cierre y cada intervalo.
Tampoco basta igualar medianas: revisa cuartiles, bigotes y valores exteriores.
En la muestra independiente el bigote superior es 130, **no 160**, porque 160
es un límite calculado, no una observación. No se exige demostrar inferencia
estadística ni ajustar un modelo.

## Pistas

<details>
<summary>Ver pistas para las comprobaciones</summary>

Usa el detalle de septiembre, no la tabla de sumas. Para el histograma conserva
`closed = "right"` y en `hist`, `right = TRUE, include.lowest = TRUE`.
Compara `layer_data(..., 1)$count` con `$counts` de la referencia.
Para los bigotes, calcula Q1/Q3 e identifica los valores dentro de los límites.
La caja más puntos puede usar `outlier.shape = NA`: se oculta el símbolo
duplicado de la caja, mientras la otra capa conserva todos los puntos.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

Guarda el recorrido completo de la lección como `output/mi_geometrias.R`.
El [script de referencia](../../../curriculum/08_visualization_r/02_geometries_stats/explorar_geometrias.R)
puede servir para contrastarlo; no dependas de objetos dejados por otra sesión.
En `output/mi_geometrias_lab.R`:

```r
source("output/mi_geometrias.R", encoding = "UTF-8")
bordes_lab <- c(1000, 2000, 3000, 4000)
referencia_lab <- graphics::hist(septiembre$saldo_mxn, breaks = bordes_lab,
  right = TRUE, include.lowest = TRUE, plot = FALSE)
histograma_lab <- ggplot2::ggplot(septiembre, ggplot2::aes(saldo_mxn)) +
  ggplot2::geom_histogram(breaks = bordes_lab, closed = "right",
                          fill = "#246A86", colour = "white") +
  ggplot2::scale_x_continuous(breaks = bordes_lab) +
  ggplot2::labs(title = "Septiembre: intervalos de 1000 MXN",
    subtitle = "Los mismos 14 IDs; cierre derecho",
    x = "Saldo por crédito (MXN)", y = "Créditos por intervalo") +
  ggplot2::theme_minimal(base_size = 12)
print(histograma_lab)
stopifnot(identical(referencia_lab$counts, c(7L, 5L, 2L)),
          identical(ggplot2::layer_data(histograma_lab, 1)$count,
                    as.double(referencia_lab$counts)),
          sum(referencia_lab$counts) == nrow(septiembre))

q <- stats::quantile(septiembre$saldo_mxn, c(0.25, 0.5, 0.75), type = 7, names = FALSE)
iqr <- q[3] - q[1]
limites <- c(q[1] - 1.5 * iqr, q[3] + 1.5 * iqr)
dentro <- septiembre$saldo_mxn >= limites[1] & septiembre$saldo_mxn <= limites[2]
bigotes <- range(septiembre$saldo_mxn[dentro])
stopifnot(identical(q, c(1475, 2050, 2575)), iqr == 1100,
          identical(limites, c(-175, 4225)),
          identical(as.double(bigotes), c(1100, 3200)))
print(limites)
print(bigotes)
```

El cambio de 500 a 1000 MXN por intervalo junta grupos: 4 + 3 = 7,
3 + 2 = 5, y 2 en el último. No se perdieron créditos ni cambió la suma de
sus saldos. Una caja resume posiciones de la distribución; no muestra el
saldo total ni los cambios por ID. Esas preguntas requieren otras tablas.

```r
mini <- tibble::tibble(grupo = "Ejemplo independiente",
                      saldo_mxn = c(100, 110, 120, 130, 1000))
q_mini <- stats::quantile(mini$saldo_mxn, c(0.25, 0.5, 0.75), type = 7, names = FALSE)
iqr_mini <- q_mini[3] - q_mini[1]
limites_mini <- c(q_mini[1] - 1.5 * iqr_mini, q_mini[3] + 1.5 * iqr_mini)
interior <- mini$saldo_mxn >= limites_mini[1] & mini$saldo_mxn <= limites_mini[2]
bigotes_mini <- range(mini$saldo_mxn[interior])
exteriores <- mini$saldo_mxn[!interior]
caja_mini <- ggplot2::ggplot(mini, ggplot2::aes(grupo, saldo_mxn)) +
  ggplot2::geom_boxplot(coef = 1.5, quantile.type = 7, outlier.shape = NA) +
  ggplot2::geom_point(position = ggplot2::position_jitter(width = 0.06, height = 0, seed = 802)) +
  ggplot2::labs(title = "Un valor exterior conservado",
    x = NULL, y = "Saldo por observación (MXN)") +
  ggplot2::theme_minimal(base_size = 12)
print(caja_mini)
calculado_mini <- ggplot2::layer_data(caja_mini, 1)
stopifnot(identical(q_mini, c(110, 120, 130)),
          identical(limites_mini, c(80, 160)),
          identical(bigotes_mini, c(100, 130)), identical(exteriores, 1000),
          calculado_mini$ymin == 100, calculado_mini$ymax == 130,
          identical(calculado_mini$outliers[[1]], 1000),
          nrow(ggplot2::layer_data(caja_mini, 2)) == 5L,
          identical(huella, tools::md5sum(ruta)))
```

`range` obtiene mínimo y máximo de las observaciones interiores. Con `!interior`
seleccionamos las exteriores para inspeccionarlas, sin eliminarlas de `mini`.
La regla gráfica no prueba que 1000 sea un error. La interpretación necesita
contexto o una regla de calidad independiente.

Guarda, reinicia R y ejecuta desde la raíz de la práctica, en Console:

```r
source("output/mi_geometrias_lab.R", encoding = "UTF-8")
```

</details>

## Ampliaciones opcionales

No bloquean avanzar. La primera explora un denominador explícito; la segunda
usa otra muestra mínima para distinguir hueco y ausencia de fila.

<details>
<summary>Proporción por intervalo en un solo corte y grupo</summary>

Después de reconstruir el recorrido esencial:

```r
proporciones <- ggplot2::ggplot(septiembre,
  ggplot2::aes(saldo_mxn, y = ggplot2::after_stat(count / sum(count)))) +
  ggplot2::geom_histogram(breaks = bordes, closed = "right") +
  ggplot2::labs(x = "Saldo por crédito (MXN)", y = "Proporción de los 14 créditos")
print(proporciones)
altura <- ggplot2::layer_data(proporciones, 1)$y
stopifnot(isTRUE(all.equal(altura, c(4, 3, 3, 2, 2) / 14)),
          abs(sum(altura) - 1) < 1e-12)
```

`count` aparece después del cálculo de intervalos, por eso usamos `after_stat`.
El denominador suma las frecuencias de esta única población sin facetas ni
grupos adicionales: 14. Las alturas son proporciones, no porcentajes ni densidad.
Con paneles, agrupaciones o pesos habría que revisar el denominador y el cálculo;
no trasladar esta expresión automáticamente. Con intervalos de anchura desigual
también habría que revisar el significado de las áreas.
[Referencia de evaluación](https://ggplot2.tidyverse.org/reference/aes_eval.html).

</details>

<details>
<summary>Una observación ausente no equivale a una fila inexistente</summary>

Esta muestra es independiente; no agrega un corte a la cartera de 07.10:

```r
serie_mini <- tibble::tibble(
  fecha = as.Date(c("2026-09-30", "2026-10-31", "2026-11-30")),
  valor = c(100, NA_real_, 120)
)
conocidos <- serie_mini[!is.na(serie_mini$valor),]
hueco <- ggplot2::ggplot(serie_mini, ggplot2::aes(fecha, valor, group = 1)) +
  ggplot2::geom_line() + ggplot2::geom_point(data = conocidos) +
  ggplot2::scale_x_date(breaks = serie_mini$fecha, date_labels = "%Y-%m-%d") +
  ggplot2::labs(title = "Octubre explícitamente ausente", x = "Fecha", y = "Valor de ejemplo")
sin_fila <- ggplot2::ggplot(conocidos, ggplot2::aes(fecha, valor, group = 1)) +
  ggplot2::geom_line() + ggplot2::geom_point() +
  ggplot2::scale_x_date(breaks = serie_mini$fecha, date_labels = "%Y-%m-%d") +
  ggplot2::labs(title = "Octubre no tiene fila", x = "Fecha", y = "Valor de ejemplo")
print(hueco)
print(sin_fila)
stopifnot(nrow(serie_mini) == 3L, sum(is.na(serie_mini$valor)) == 1L)
```

En el primer gráfico el NA interior interrumpe el trazo; los dos puntos
conocidos siguen visibles porque su capa recibe `conocidos`. En el segundo
aparece una conexión septiembre/noviembre. Ninguno demuestra el valor de octubre.
Eliminar filas NA antes de dibujar puede ocultar el hueco; imputar cero
inventaría una medición. El caso de NA interior no necesariamente genera aviso:
la ausencia de advertencias no demuestra completitud.
[Referencia de líneas y ausencias](https://ggplot2.tidyverse.org/reference/geom_path.html).

</details>

## Evidencia, reflexión y salida

Conserva script, tabla de elección por pregunta, comprobaciones numéricas y
notas de revisión visual. Registra dudas y evidencia real según
[PROGRESS.md](../../../PROGRESS.md). No hay checkpoint ni proyecto integrador
activo; ejecutar la referencia no acredita por sí solo aprendizaje.

- ¿Qué cambia entre contar el resumen y contar el detalle?
- ¿Qué orden usa una línea y qué emparejamiento necesita una dispersión?
- ¿Qué información pierde el histograma sobre cada ID y qué depende de sus bordes?
- ¿Qué distingue límite, bigote y punto exterior? ¿Cuál es el criterio para borrar un dato?
- ¿Por qué dos cajas similares no demuestran cambios similares por crédito?
- ¿Qué tabla revisarías antes de afirmar que la suma de octubre aumentó por una causa concreta?

Cierra cuando puedas reconstruir y justificar esos puntos. Siguiente:
[08.03 — Mapear y fijar estéticas](../../../curriculum/08_visualization_r/README.md#03-mapear-y-fijar-esteticas),
todavía planificada. Volver a la [lección 08.02](../../../curriculum/08_visualization_r/02_geometries_stats/README.md).

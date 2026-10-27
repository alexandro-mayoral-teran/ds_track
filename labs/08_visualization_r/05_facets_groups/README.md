# Lab 08.05 — Facetas y comparación entre grupos

## Propósito y entradas

Comparar grupos con paneles y explicar qué filas, medidas y escalas recibe cada
uno. Lee la [lección 08.05](../../../curriculum/08_visualization_r/05_facets_groups/README.md)
y conserva tu script `output/mi_facetas.R`. Usa el mismo proyecto renv de 07.10,
sin cambiar fuentes, reglas de aceptación, funciones previas o lockfile.

Abre el proyecto en RStudio o tu IDE. Crea `output/mi_facetas_lab.R`, eligiendo
otro nombre si ya existe trabajo. Ejecuta por bloques en Console de R desde la
raíz del proyecto; no dependas del workspace de una sesión anterior. No se
necesitan instalaciones ni una entrega nueva exportada.

## Actividad esencial

1. Predice cuántas filas, paneles, capas, barras y textos tendrá `por_segmento`.
   Explica qué representa una fila de `detalle` y una de `resumen_segmentos`.
   Justifica por qué tener los mismos 14 IDs globales no basta para asegurar
   integrantes iguales por segmento si un ID cambia de categoría.
2. Reconstruye la lección y comprueba 28 observaciones, ocho sumas y los grupos
   de cuatro/cuatro/tres/tres créditos por corte. Concílialos con 14 y con
   29000/31800 MXN. Explica los denominadores de `proporcion_creditos`.
3. Contrasta escalas fijas/libres de las barras. En la cuadrícula de cajas,
   cambia a `scales = "free_y"`: predice cuántas escalas verticales habrá y qué
   paneles compartirán una. Comprueba que siguen ocho cajas y 28 puntos.
4. Construye un gráfico de barras por segmento y añade etiquetas desde
   `cierre$datos_figura`, que tiene los totales globales y **no tiene segmento**.
   Usa `inherit.aes = FALSE` y declara x/y/label. Predice dónde aparecerán las
   cifras y si esa opción impide repetirlas. Inspecciona la capa y corrige la
   tabla de etiquetas para informar créditos del segmento/corte correspondiente.
5. En una copia, invierte el orden de las filas resumidas. Comprueba que cada
   suma sigue en su segmento y fecha. No compares solo el total general ni los
   códigos numéricos de panel entre gráficos.
6. Usa la muestra independiente A/B/C de la lección. Construye una cuadrícula
   **solo con puntos de `demo`, sin la capa de inventario**. Compara `drop = TRUE`
   y `drop = FALSE`; predice el número de paneles. Explica por qué B/Oct puede
   seguir vacío y C desaparecer, sin convertir ningún saldo en cero.
7. Contrasta esa cuadrícula con `sin_registros`, cuyos textos sí incluyen las
   seis combinaciones del inventario. Señala cero observado, saldo NA y celdas
   sin registro. Explica por qué seis paneles no equivalen a seis mediciones.
8. Guarda, reinicia R y ejecuta el script completo. Conserva predicciones,
   comprobaciones, notas de revisión visual y una corrección propia.

## Resultados y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Base principal | 14 IDs comunes, 28 observaciones; segmento estable por ID |
| Barras por segmento | Ocho filas resumidas, cuatro paneles, dos capas, ocho barras y ocho textos |
| Importes por segmento Sep/Oct | comercio 7600/8400; consumo 9200/10000; educacion 5800/6400; servicios 6400/7000 MXN |
| Denominadores | 4/14, 4/14, 3/14 y 3/14 por corte; no tasas sobre 18 ni sobre 48 |
| Cuadrícula con y libre | Ocho paneles, cuatro escalas y; los dos cortes del segmento comparten una |
| Etiquetas incorrectas | Ocho textos con «n = 14» repetidos por falta de segmento |
| Etiquetas corregidas | Dos «n = 4» por panel de comercio/consumo y dos «n = 3» por educacion/servicios |
| Demo solo puntos | `drop = TRUE`: cuatro paneles; `drop = FALSE`: seis; tres filas de origen en ambos |
| Estados independientes | Dos saldos conocidos, uno NA y tres combinaciones sin registro |
| Conservación | CSV intacto, sumas/IDs conservados y reconstrucción desde sesión nueva |

Las ocho etiquetas incorrectas son el resultado de repetir dos filas globales
en cuatro paneles. Su cantidad coincide con la de las etiquetas correctas:
contarlas no basta. Hay que revisar a qué clave y medida corresponde cada una.

## Pistas

<details>
<summary>Ver pistas después de formular tus predicciones</summary>

La tabla de etiquetas debe conservar `segmento` y `corte`. Herencia de mapeos y
asignación de facetas son mecanismos distintos. Reutiliza la relación PANEL →
segmento de la lección para revisar valores y textos. Los factores mantienen
el orden al invertir filas; cambiar niveles modifica la presentación.

Para estudiar `drop`, evita usar la capa de inventario: esa capa ya contiene C
y ambas fechas. `drop = FALSE` conserva niveles del factor que ninguna fila
utiliza; no modifica `demo`. La cuadrícula cruza los valores retenidos de las
dos dimensiones, de modo que una celda vacía no implica una fila con saldo cero.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar la actividad</summary>

Empieza tu script con la reconstrucción de la lección:

```r
source("output/mi_facetas.R", encoding = "UTF-8")
totales_lab <- resumen_segmentos |> dplyr::group_by(corte) |>
  dplyr::summarise(creditos = sum(creditos), saldo_mxn = sum(saldo_mxn),
    proporcion = sum(proporcion_creditos), .groups = "drop")
stopifnot(identical(totales_lab$creditos, c(14L, 14L)),
          identical(totales_lab$saldo_mxn, c(29000, 31800)),
          all(abs(totales_lab$proporcion - 1) < 1e-12))
cuadricula_libre <- cuadricula + ggplot2::facet_grid(
  rows = ggplot2::vars(segmento), cols = ggplot2::vars(corte), scales = "free_y") +
  ggplot2::labs(title = "Escala vertical compartida dentro de cada segmento",
    subtitle = "Cuatro rangos y; los dos cortes de cada fila comparten uno")
diseno_libre <- ggplot2::ggplot_build(cuadricula_libre)$layout$layout
stopifnot(nrow(diseno_libre) == 8L,
          length(unique(diseno_libre$SCALE_Y)) == 4L,
          all(table(diseno_libre$SCALE_Y) == 2L),
          nrow(ggplot2::layer_data(cuadricula_libre, 1)) == 8L,
          nrow(ggplot2::layer_data(cuadricula_libre, 2)) == 28L)
print(cuadricula_libre)
```

Los segmentos tienen los mismos integrantes entre fechas en esta muestra.
La escala libre por fila permite comparar septiembre/octubre dentro del
segmento; exige leer ejes para comparar segmentos. No cambió ningún saldo.

Ahora el caso incorrecto y su corrección:

```r
globales <- cierre$datos_figura |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = levels(detalle$corte))
)
etiquetas_globales <- base_segmentos +
  ggplot2::facet_wrap(ggplot2::vars(segmento), ncol = 2) +
  ggplot2::geom_text(data = globales,
    ggplot2::aes(corte, saldo_mxn, label = paste0("n = ", creditos)),
    inherit.aes = FALSE, vjust = -0.5, size = 3.5) +
  ggplot2::labs(title = "Caso incorrecto: etiquetas globales repetidas")
textos_mal <- ggplot2::layer_data(etiquetas_globales, 2)
stopifnot(nrow(textos_mal) == 8L, all(textos_mal$label == "n = 14"))
print(etiquetas_globales)
etiquetas_correctas <- base_segmentos +
  ggplot2::facet_wrap(ggplot2::vars(segmento), ncol = 2) +
  ggplot2::geom_text(data = resumen_segmentos,
    ggplot2::aes(corte, saldo_mxn, label = paste0("n = ", creditos)),
    inherit.aes = FALSE, vjust = -0.5, size = 3.5) +
  ggplot2::labs(title = "Etiquetas por segmento y corte")
textos_bien <- ggplot2::layer_data(etiquetas_correctas, 2) |> tibble::as_tibble()
mapa_textos <- ggplot2::ggplot_build(etiquetas_correctas)$layout$layout
texto_observado <- textos_bien |> dplyr::select(PANEL, x, y, label) |>
  dplyr::left_join(mapa_textos |> dplyr::select(PANEL, segmento),
    by = "PANEL", relationship = "many-to-one") |>
  dplyr::transmute(segmento = as.character(segmento),
    corte = levels(detalle$corte)[as.integer(x)], saldo_mxn = y, etiqueta = label) |>
  dplyr::arrange(segmento, corte)
texto_esperado <- resumen_segmentos |> dplyr::transmute(
  segmento = as.character(segmento), corte = as.character(corte), saldo_mxn,
  etiqueta = paste0("n = ", creditos)) |> dplyr::arrange(segmento, corte)
stopifnot(identical(texto_observado, texto_esperado))
print(etiquetas_correctas)
```

La tabla global carece de `segmento`; las dos etiquetas participan en los
cuatro paneles y además amplían el rango hasta los totales globales. La
corrección conserva las claves de faceta. `inherit.aes = FALSE` aparece en
ambos: esa opción no era la causa ni la solución de la repetición.

```r
invertido <- resumen_segmentos[nrow(resumen_segmentos):1, ]
figura_invertida <- ggplot2::ggplot(invertido, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col() + ggplot2::facet_wrap(ggplot2::vars(segmento), ncol = 2)
ci <- ggplot2::layer_data(figura_invertida, 1) |> tibble::as_tibble()
pi <- ggplot2::ggplot_build(figura_invertida)$layout$layout
resultado_invertido <- ci |> dplyr::select(PANEL, x, y) |>
  dplyr::left_join(pi |> dplyr::select(PANEL, segmento),
    by = "PANEL", relationship = "many-to-one") |>
  dplyr::transmute(segmento = as.character(segmento),
    corte = levels(detalle$corte)[as.integer(x)], saldo_mxn = y) |>
  dplyr::arrange(segmento, corte)
stopifnot(identical(resultado_invertido, esperado))
base_demo <- ggplot2::ggplot(demo, ggplot2::aes(x = 1, y = saldo_mxn)) +
  ggplot2::geom_point(size = 3)
con_drop <- base_demo + ggplot2::facet_grid(
  rows = ggplot2::vars(segmento), cols = ggplot2::vars(corte), drop = TRUE)
sin_drop <- base_demo + ggplot2::facet_grid(
  rows = ggplot2::vars(segmento), cols = ggplot2::vars(corte), drop = FALSE)
stopifnot(nrow(ggplot2::ggplot_build(con_drop)$layout$layout) == 4L,
          nrow(ggplot2::ggplot_build(sin_drop)$layout$layout) == 6L,
          nrow(demo) == 3L, sum(is.na(demo$saldo_mxn)) == 1L,
          sum(demo$saldo_mxn == 0, na.rm = TRUE) == 1L,
          identical(huella, tools::md5sum(ruta)))
print(con_drop)
print(sin_drop)
print(sin_registros)
```

`na.rm = TRUE` se usa aquí solo al **contar ceros conocidos**; no sustituye
el saldo NA ni elimina su fila. La cuenta de ausentes se revisa aparte.
Sin C quedan A/B × Sep/Oct, cuatro paneles; B/Oct sigue vacío porque la
cuadrícula cruza filas y columnas. Con los niveles conservados son seis.
Los avisos por el punto con saldo NA son esperados y no implican borrar su origen.

Guarda, reinicia R con Session > Restart R y ejecuta en Console:

```r
source("output/mi_facetas_lab.R", encoding = "UTF-8")
```

Si usaste otros nombres, ajusta los `source`. El
[script de referencia](../../../curriculum/08_visualization_r/05_facets_groups/explorar_facetas.R)
sirve para contrastar la lección; tu evidencia incluye la explicación de las
decisiones, además de las aserciones.

</details>

## Extensión opcional — Combinaciones y niveles

Con la misma `base_demo`, compara `facet_wrap(vars(segmento, corte))` con la
cuadrícula. Con `drop = TRUE`, wrap tendrá tres paneles de combinaciones
observadas; la cuadrícula tendrá cuatro por el cruce A/B × Sep/Oct. Con
`drop = FALSE`, ambos pueden conservar las seis combinaciones de niveles.
No uses la capa de inventario para este contraste: sus seis filas harían
presentes todas esas combinaciones para formar paneles.

## Evidencia, reflexión y salida

Conserva script propio, predicciones, comprobaciones por claves y notas de
inspección visual. Registra evidencia real y dudas según
tu bitácora personal junto a la práctica. No hay proyecto integrador ni checkpoint
activo; ejecutar una referencia no acredita aprendizaje.

- ¿Por qué cuatro paneles pueden contener solo dos capas y ocho barras?
- ¿Qué población y denominador declara tu comparación?
- ¿Cuándo elegirías un eje compartido y cuándo un rango propio por panel?
- ¿Por qué una capa con dos filas puede producir ocho etiquetas?
- ¿Qué información adicional necesitas para interpretar un panel vacío?
- ¿Cómo detectarías un cambio de segmento sin ocultarlo en un resumen global?

Cierra cuando puedas reconstruir y justificar esas decisiones. Siguiente:
[08.06 — Etiquetas, temas y accesibilidad](../../../curriculum/08_visualization_r/06_labels_themes_accessibility/README.md),
ya disponible. Volver a la [lección 08.05](../../../curriculum/08_visualization_r/05_facets_groups/README.md).

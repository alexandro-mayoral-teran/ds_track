# Lab 08.01 — Pregunta y gramática de gráficos

## Propósito y entradas

Explicar y reconstruir una figura por componentes. Lee primero la
[lección 08.01](../../../curriculum/08_visualization_r/01_question_grammar/README.md).
Usa el mismo proyecto renv de 07.10, sus funciones y `datos/cartera_texto.csv`.
No hay datos ni paquetes nuevos; conserva fuente, rechazos y entregas anteriores.

En RStudio o tu IDE crea `output/mi_gramatica_lab.R`. Mantén como directorio
la raíz de la práctica y ejecuta en Console de R, por bloques. Puedes repartir
la actividad en dos sesiones: construcción y luego reconstrucción/explicación.

## Actividad

1. Escribe antes de dibujar la pregunta, unidad original, unidad de la tabla
   representada, fechas, población y medida. Explica por qué los saldos
   39900/41500 responden una pregunta distinta de 29000/31800 MXN.
2. Reconstruye `cierre` desde la fuente con los pasos de la lección. Comprueba
   48 = 36 + 12; 14 pares; ocho registros sin pareja. Prepara `datos` conservando
   `saldo_mxn` numérico y agregando `corte`/`etiqueta` para presentación.
3. Antes de cada `print`, predice qué aparecerá: objeto sin geometría; barras;
   barras con textos. Guarda tres objetos distintos. Explica de dónde obtiene
   cada capa sus datos, posiciones y, si corresponde, etiquetas.
4. Añade contexto y tema sin cambiar tabla ni mapeos de posición. Incluye MXN,
   fechas, 14 IDs, cobertura 14/18 y un límite descriptivo. Cuenta capas y
   marcas por separado. Revisa legibilidad en Plots.
5. Construye aparte el conteo de filas por corte con `geom_bar`, sin mapear y.
   Predice 1/1 y justifica por qué no son cantidades de créditos ni de MXN.
6. Haz una variante con **una sola etiqueta**, la de octubre: conserva ambas
   barras y pasa a `geom_text` una tabla filtrada a octubre. No filtres el
   gráfico completo. Explica qué cambió y qué heredó esa capa. La selección
   con `filter` se estudió en [07.02](../../../curriculum/07_tidyverse/02_select_filter_sort/README.md).
7. Guarda, reinicia R y ejecuta tu script completo. Registra una interpretación
   con cambio absoluto, denominador de la variación y cobertura; incluye una
   duda o corrección. No requiere una nueva exportación.

## Resultado y comprobación

| Evidencia | Resultado esperado |
| --- | --- |
| Contrato escrito | Crédito/corte original; fila resumida por corte de los mismos 14 IDs |
| Barras de saldo | 29000 y 31800 MXN; origen cero; dos fechas identificadas |
| Texto por fila | `29 000` y `31 800`; dos capas y cuatro marcas en total |
| Variante | Dos barras y una etiqueta en octubre; dos capas y tres marcas |
| Conteo separado | 1/1 filas de la tabla resumida; no interpretar como saldo |
| Reconstrucción | Mismos resultados desde sesión nueva, fuente intacta |
| Explicación | +2800 MXN; +9.66% sobre 29000; cobertura 14/18 por corte; sin inferir causas |

Compara también los nombres de las fechas y la ubicación de las etiquetas:
conservar dos alturas no detecta un intercambio de sus nombres. Una figura
legible no sustituye comprobar su tabla, y un conteo de capas no certifica sus
valores ni su interpretación.

## Pistas

<details>
<summary>Ver pistas de construcción y herencia</summary>

Usa `p0` para datos/mapeos, `p1` para barras y `p2` para barras/textos.
En la variante, comienza de nuevo desde `p1`: si partes de `p2`, conservarás
también las dos etiquetas anteriores. El argumento nombrado `data =` de
`geom_text` cambia la tabla de esa capa; no cambia la tabla de las barras.
Las columnas requeridas por los mapeos heredados deben seguir disponibles.

</details>

## Solución razonada

<details>
<summary>Ver una solución después de intentar el lab</summary>

Al inicio de tu script copia los bloques de reconstrucción y preparación de
`datos` de la lección, incluidas las comprobaciones y la huella de la fuente.
Después construye:

```r
p0 <- ggplot2::ggplot(datos, ggplot2::aes(x = corte, y = saldo_mxn))
p1 <- p0 + ggplot2::geom_col(fill = "#246A86", width = 0.6)
p2 <- p1 + ggplot2::geom_text(
  ggplot2::aes(label = etiqueta), vjust = -0.5, size = 4.5
)
print(p0)
print(p1)
print(p2)

# Componente compartido: escala y contexto, sin agregar capas de datos.
contexto <- list(
  ggplot2::scale_y_continuous(
    limits = c(0, NA), expand = ggplot2::expansion(mult = c(0, 0.12)),
    labels = function(x) format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
  ),
  ggplot2::labs(
    title = "Saldo de los mismos créditos en dos cortes",
    subtitle = "Base común: 14 IDs aceptados en ambas fechas",
    x = "Fecha de corte", y = "Saldo observado (MXN)",
    caption = "Datos sintéticos. Base común: 14/18 por corte; no explica causas."
  ),
  ggplot2::theme_minimal(base_size = 12)
)
figura_lab <- p2 + contexto
print(figura_lab)
```

`list` reúne componentes para reutilizarlos: al sumarla a un ggplot, se agregan
sus elementos en orden. Es una comodidad, no una teoría esencial nueva; puedes
repetir esas tres llamadas con `+` como en la lección. Las listas se estudiaron
en [06.05](../../../curriculum/06_r_foundations/05_lists_data_frames/README.md).
La [referencia de adición](https://ggplot2.tidyverse.org/reference/gg-add.html)
documenta su uso con componentes.

```r
conteo_lab <- ggplot2::ggplot(datos, ggplot2::aes(x = corte)) +
  ggplot2::geom_bar() +
  ggplot2::labs(title = "Filas de la tabla resumida por corte", y = "Filas (no MXN)")
print(conteo_lab)

octubre <- datos |> dplyr::filter(fecha_corte == as.Date("2026-10-31"))
variante <- p1 + ggplot2::geom_text(
  data = octubre, mapping = ggplot2::aes(label = etiqueta),
  vjust = -0.5, size = 4.5
) + contexto
print(variante)
stopifnot(nrow(octubre) == 1L, octubre$saldo_mxn == 31800,
          length(p0$layers) == 0L, length(p1$layers) == 1L,
          length(figura_lab$layers) == 2L, length(variante$layers) == 2L,
          identical(datos$saldo_mxn, c(29000, 31800)),
          identical(huella, tools::md5sum(ruta)))
```

`geom_text(data = octubre, ...)` hereda los mapeos x/y, pero los evalúa sobre
su propia tabla, que conserva `corte` y `saldo_mxn`. Solo añade `label`. Las
barras siguen usando las dos filas de `datos`. La referencia de
[geom_text](https://ggplot2.tidyverse.org/reference/geom_text.html) documenta
datos y herencia por capa. Filtrar `datos` antes de crear `p0` eliminaría la
barra de septiembre y cambiaría la comparación.

No exportes dentro del script de reconstrucción. Guarda y reinicia R; desde
la raíz de la práctica, en Console, ejecuta:

```r
source("output/mi_gramatica_lab.R", encoding = "UTF-8")
```

La diferencia 31800 − 29000 es 2800 MXN; dividirla entre 29000 produce el
9.66%. El 14/18 describe cobertura de IDs aceptados, no variación de saldo.
Si usaras todos los aceptados por corte, el cambio sería 1600 MXN sobre una
población que cambia; no debes presentar esa cifra como la de los mismos IDs.

</details>

## Reflexión, evidencia y salida

- ¿Cuál es la unidad de una fila original y cuál la de una fila de `datos`?
- ¿Por qué hay dos capas, aunque la figura completa tiene cuatro marcas?
- ¿Qué cambia al sumar `labs`? ¿Cambiar el nombre del eje convierte la unidad?
- ¿Qué hereda la capa de octubre y qué tabla usa para resolver esos mapeos?
- ¿Por qué contar filas resumidas no recupera el número de créditos?
- ¿Cómo distinguirías ausencia de base común de un saldo observado cero?
- ¿Qué no puedes conocer sobre el mes intermedio ni sobre las causas?

Conserva script, contrato escrito, revisión visual y explicación de cuatro a
seis frases. Registra la evidencia y dudas reales según
[PROGRESS.md](../../../PROGRESS.md), sin marcar aprendizaje por la existencia
de una solución. No hay proyecto integrador ni checkpoint activo todavía.

Continúa cuando puedas reconstruir y explicar tus decisiones. Siguiente:
[08.02 — Geometrías y transformaciones estadísticas](../../../curriculum/08_visualization_r/02_geometries_stats/README.md),
ya disponible. Volver a la [lección 08.01](../../../curriculum/08_visualization_r/01_question_grammar/README.md).

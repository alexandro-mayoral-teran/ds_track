# Mismo proyecto renv de 07.10; ejecutar desde su raiz en el IDE.
# Guardar una copia propia como output/mi_comunicacion.R; no instala ni exporta.
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
cierre <- construir_cierre(fuente)
comprobar_cierre(fuente, cierre)
formato_mxn <- function(x) format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
datos <- cierre$datos_figura |> dplyr::arrange(fecha_corte) |>
  dplyr::mutate(
    corte = factor(format(fecha_corte, "%Y-%m-%d"),
      levels = c("2026-09-30", "2026-10-31")),
    etiqueta = formato_mxn(saldo_mxn)
  )
inicial <- datos$saldo_mxn[1]
final <- datos$saldo_mxn[2]
diferencia <- final - inicial
variacion_pct <- if (inicial == 0) NA_real_ else 100 * diferencia / inicial
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(cierre$comunes) == 14L, nrow(cierre$sin_pareja) == 8L,
          identical(datos$saldo_mxn, c(29000, 31800)), diferencia == 2800,
          all(datos$creditos == 14L), all(datos$aceptados_corte == 18L))
titulo <- paste("El saldo observado aumenta", formato_mxn(diferencia), "MXN")
nota_fuente <- paste(
  "Datos sintéticos DS Track; CSV y reglas de aceptación de 07.10.",
  "Base común: 14 de 18 aceptados por corte; cuatro sin pareja por fecha.",
  "Comparación descriptiva: no identifica causas ni representa todos los aceptados.", sep = "\n"
)
print(datos, width = Inf)
print(variacion_pct)

base <- ggplot2::ggplot(datos, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col(fill = "#246A86", width = 0.6)
rotulado <- base +
  ggplot2::geom_text(ggplot2::aes(label = etiqueta), vjust = -0.5,
    colour = "#222222", size = 11, size.unit = "pt") +
  ggplot2::scale_y_continuous(limits = c(0, NA), labels = formato_mxn,
    expand = ggplot2::expansion(mult = c(0, 0.25))) +
  ggplot2::scale_x_discrete(labels = c(
    "2026-09-30" = "30 sep 2026", "2026-10-31" = "31 oct 2026")) +
  ggplot2::labs(title = titulo,
    subtitle = "Los mismos 14 IDs aceptados en ambas fechas",
    x = "Fecha de corte", y = "Saldo observado (MXN)", caption = nota_fuente)
print(rotulado)

con_tema <- rotulado + ggplot2::theme_minimal(base_size = 12, base_family = "sans")
tema_lectura <- ggplot2::theme(
  plot.title = ggplot2::element_text(face = "bold", size = 15),
  plot.caption = ggplot2::element_text(hjust = 0, size = 9, lineheight = 1.1),
  axis.text = ggplot2::element_text(colour = "#222222", size = 10),
  panel.grid.major.x = ggplot2::element_blank(),
  panel.grid.major.y = ggplot2::element_line(colour = "#D9D9D9", linewidth = 0.3),
  panel.grid.minor = ggplot2::element_blank(),
  plot.background = ggplot2::element_rect(fill = "white", colour = NA),
  plot.margin = ggplot2::margin(12, 14, 12, 12),
  legend.position = "bottom"
)
legible <- con_tema + tema_lectura
print(legible)

mensaje_pct <- if (is.na(variacion_pct)) {
  "Porcentaje no definido: base inicial cero"
} else {
  paste0("+", formatC(variacion_pct, format = "f", digits = 2, decimal.mark = "."),
         "% sobre septiembre")
}
nota_octubre <- datos |> dplyr::filter(fecha_corte == max(fecha_corte)) |>
  dplyr::mutate(posicion_nota = saldo_mxn + 5000, mensaje = mensaje_pct)
comunicada <- legible + ggplot2::geom_label(data = nota_octubre,
  ggplot2::aes(x = corte, y = posicion_nota, label = mensaje),
  inherit.aes = FALSE, colour = "#222222", fill = "white",
  size = 10, size.unit = "pt", linewidth = 0.3)
con_nota <- comunicada + ggplot2::annotate("text", x = "2026-09-30", y = 37000,
  label = "Datos sintéticos", colour = "#222222", size = 10, size.unit = "pt")
print(comunicada)
print(con_nota)

etiquetas_fecha <- c("2026-09-30" = "30 sep 2026", "2026-10-31" = "31 oct 2026")
paleta <- c("2026-09-30" = "#246A86", "2026-10-31" = "#A34E12")
formas <- c("2026-09-30" = 16, "2026-10-31" = 17)
base_puntos <- ggplot2::ggplot(datos, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_line(ggplot2::aes(group = 1), colour = "#68747A", linewidth = 0.7) +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 3.5) +
  ggplot2::geom_text(ggplot2::aes(label = etiqueta), vjust = -1,
    colour = "#222222", size = 11, size.unit = "pt") +
  ggplot2::scale_x_discrete(labels = etiquetas_fecha) +
  ggplot2::scale_y_continuous(limits = c(0, NA), labels = formato_mxn,
    expand = ggplot2::expansion(mult = c(0, 0.18))) +
  ggplot2::labs(title = "Dos observaciones del saldo común",
    subtitle = "Las fechas se identifican mediante posiciones, formas y textos",
    x = "Fecha de corte", y = "Saldo observado (MXN)", caption = nota_fuente) +
  ggplot2::theme_minimal(base_size = 12, base_family = "sans") + tema_lectura
con_senales <- base_puntos +
  ggplot2::scale_colour_manual(name = "Fecha de corte", values = paleta, labels = etiquetas_fecha) +
  ggplot2::scale_shape_manual(name = "Fecha de corte", values = formas, labels = etiquetas_fecha)
sin_color <- base_puntos +
  ggplot2::scale_colour_manual(name = "Fecha de corte",
    values = c("2026-09-30" = "#222222", "2026-10-31" = "#222222"), labels = etiquetas_fecha) +
  ggplot2::scale_shape_manual(name = "Fecha de corte", values = formas, labels = etiquetas_fecha) +
  ggplot2::labs(subtitle = "Prueba con color único: las formas y fechas conservan el significado")
print(con_senales)
print(sin_color)

descripcion <- paste(
  "Gráfico de dos barras desde cero. Saldo observado de los mismos 14 IDs aceptados:",
  paste0("30 de septiembre de 2026, ", formato_mxn(inicial), " MXN;"),
  paste0("31 de octubre, ", formato_mxn(final), " MXN."),
  paste0("Diferencia de ", formato_mxn(diferencia), " MXN; ",
    if (is.na(variacion_pct)) mensaje_pct else paste("aproximadamente", mensaje_pct), "."),
  "Datos sintéticos; cobertura de 14 de 18 aceptados por corte. No identifica causas."
)
comunicada <- comunicada + ggplot2::labs(alt = descripcion)
texto_alternativo <- ggplot2::get_alt_text(comunicada)
tabla_lectura <- datos |> dplyr::select(fecha_corte, creditos, saldo_mxn, aceptados_corte)
stopifnot(identical(texto_alternativo, descripcion),
          identical(ggplot2::get_labs(comunicada)$title, titulo))
cat(texto_alternativo, "\n")
print(tabla_lectura)

columnas_barra <- c("x", "y", "ymin", "ymax")
stopifnot(identical(ggplot2::layer_data(base, 1)[columnas_barra],
                    ggplot2::layer_data(comunicada, 1)[columnas_barra]),
          identical(ggplot2::layer_data(rotulado, 2)$label, datos$etiqueta),
          nrow(ggplot2::layer_data(comunicada, 3)) == 1L,
          identical(ggplot2::layer_data(con_senales, 2)$y,
                    ggplot2::layer_data(sin_color, 2)$y),
          length(unique(ggplot2::layer_data(sin_color, 2)$colour)) == 1L,
          length(unique(ggplot2::layer_data(sin_color, 2)$shape)) == 2L,
          identical(huella, tools::md5sum(ruta)))

cat("Comunicacion comprobada; fuente intacta.\n")

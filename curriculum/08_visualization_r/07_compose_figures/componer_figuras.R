# Mismo proyecto renv de 08.07; ejecutar desde su raiz en el IDE.
# Guardar una copia propia como output/mi_composicion.R; no instala ni exporta.
# La vista anidada de tres graficos es una ampliacion opcional.
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
library(patchwork)
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
cierre <- construir_cierre(fuente)
comprobar_cierre(fuente, cierre)
fechas <- cierre$datos_figura$fecha_corte
resumen <- cierre$datos_figura |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = format(fechas, "%Y-%m-%d"))
)
detalle <- cierre$resultado$aceptados |>
  dplyr::filter(fecha_corte %in% fechas) |>
  dplyr::semi_join(cierre$comunes, by = "id_credito", na_matches = "never") |>
  dplyr::select(id_credito, fecha_corte, saldo_mxn) |>
  dplyr::mutate(corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = levels(resumen$corte)))
control <- detalle |> dplyr::group_by(fecha_corte) |>
  dplyr::summarise(creditos = dplyr::n(), saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop")
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(cierre$comunes) == 14L, nrow(detalle) == 28L,
          !anyNA(detalle), anyDuplicated(detalle[c("id_credito", "fecha_corte")]) == 0L,
          identical(control$creditos, c(14L, 14L)),
          identical(control$saldo_mxn, c(29000, 31800)),
          identical(control$saldo_mxn, resumen$saldo_mxn))
print(control)

paleta <- c("2026-09-30" = "#246A86", "2026-10-31" = "#A34E12")
formas <- c("2026-09-30" = 16, "2026-10-31" = 17)
rotulos_fecha <- c("2026-09-30" = "30 sep 2026", "2026-10-31" = "31 oct 2026")
formato_mxn <- function(x) format(x, big.mark = " ", scientific = FALSE, trim = TRUE)
tema_vista <- ggplot2::theme_minimal(base_size = 12, base_family = "sans") +
  ggplot2::theme(panel.grid.minor = ggplot2::element_blank(),
    panel.grid.major.x = ggplot2::element_blank(),
    axis.text = ggplot2::element_text(colour = "#222222"),
    plot.title = ggplot2::element_text(size = 12, face = "bold"))
escala_color <- ggplot2::scale_colour_manual(name = "Fecha de corte", values = paleta, labels = rotulos_fecha)
escala_forma <- ggplot2::scale_shape_manual(name = "Fecha de corte", values = formas, labels = rotulos_fecha)
p_resumen <- ggplot2::ggplot(resumen, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_line(ggplot2::aes(group = 1), colour = "#68747A", linewidth = 0.7) +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 3) +
  ggplot2::geom_text(ggplot2::aes(label = formato_mxn(saldo_mxn)),
    vjust = -1, size = 10, size.unit = "pt") +
  escala_color + escala_forma +
  ggplot2::scale_x_discrete(labels = c("2026-09-30" = "Sep", "2026-10-31" = "Oct")) +
  ggplot2::scale_y_continuous(limits = c(0, NA), labels = formato_mxn,
    expand = ggplot2::expansion(mult = c(0, 0.15))) +
  ggplot2::labs(title = "Saldo total de la base común", x = "Corte de 2026",
    y = "Saldo total observado (MXN)") + tema_vista
p_detalle <- ggplot2::ggplot(detalle, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_line(ggplot2::aes(group = id_credito), colour = "#68747A", linewidth = 0.6) +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 3) +
  escala_color + escala_forma +
  ggplot2::scale_x_discrete(labels = c("2026-09-30" = "Sep", "2026-10-31" = "Oct")) +
  ggplot2::scale_y_continuous(limits = c(0, NA), labels = formato_mxn,
    expand = ggplot2::expansion(mult = c(0, 0.15))) +
  ggplot2::labs(title = "Dos observaciones por crédito", x = "Corte de 2026",
    y = "Saldo por crédito (MXN)") + tema_vista
print(p_resumen)
print(p_detalle)

en_fila <- patchwork::wrap_plots(p_resumen, p_detalle,
  ncol = 2, widths = c(1, 1.4), guides = "collect", axes = "keep", axis_titles = "keep")
anotacion <- patchwork::plot_annotation(
  title = "El saldo común aumenta 2 800 MXN entre dos cortes",
  subtitle = "Los mismos 14 IDs: resumen y detalle con medidas explícitas",
  caption = paste(
    "Datos sintéticos DS Track. Base común: 14/18 aceptados por fecha; cuatro sin pareja por corte.",
    "A: dos sumas (29 000/31 800 MXN). B: 28 observaciones, 14 pares; los tramos no son mediciones diarias.",
    "Comparación descriptiva: no representa todos los aceptados ni identifica causas.", sep = "\n"
  ),
  tag_levels = "A",
  theme = ggplot2::theme(plot.title = ggplot2::element_text(face = "bold", size = 15),
    plot.caption = ggplot2::element_text(hjust = 0, size = 9),
    plot.background = ggplot2::element_rect(fill = "white", colour = NA))
)
composicion <- (en_fila + anotacion) & ggplot2::theme(legend.position = "bottom")
print(composicion)

en_columna <- patchwork::wrap_plots(p_resumen, p_detalle,
  ncol = 1, heights = c(1, 1.4), guides = "collect", axes = "keep", axis_titles = "keep")
vertical <- (en_columna + anotacion) & ggplot2::theme(legend.position = "bottom")
print(vertical)

p_pares <- ggplot2::ggplot(cierre$comunes, ggplot2::aes(saldo_sep, saldo_oct)) +
  ggplot2::geom_abline(intercept = 0, slope = 1, linetype = "dashed", colour = "#68747A") +
  ggplot2::geom_point(colour = "#246A86", size = 2.5) +
  ggplot2::coord_fixed(ratio = 1, xlim = c(0, 3600), ylim = c(0, 3600), expand = FALSE) +
  ggplot2::labs(title = "Saldos emparejados por ID", x = "Septiembre (MXN)", y = "Octubre (MXN)") +
  tema_vista
anidada <- ((p_resumen / (p_detalle | p_pares)) +
  patchwork::plot_layout(heights = c(1, 1.4), guides = "collect") +
  patchwork::plot_annotation(title = "Resumen, observaciones y pares de la misma base",
    caption = "Datos sintéticos; 14 IDs comunes y cobertura 14/18 por fecha.\nLa diagonal de C es igualdad, no una regresión ni una explicación causal.",
    tag_levels = "A")) & ggplot2::theme(legend.position = "bottom")
print(anidada)

stopifnot(inherits(composicion, "patchwork"),
          length(composicion) == 2L,
          identical(ggplot2::layer_data(composicion[[1]], 2)$y, c(29000, 31800)),
          nrow(ggplot2::layer_data(composicion[[2]], 2)) == 28L,
          length(unique(ggplot2::layer_data(composicion[[2]], 1)$group)) == 14L,
          all(cierre$comunes$saldo_oct - cierre$comunes$saldo_sep == 200L),
          identical(huella, tools::md5sum(ruta)))
descripcion_conjunto <- paste(
  "Dos vistas de los mismos 14 IDs aceptados en septiembre y octubre de 2026.",
  "A muestra saldo total de 29 000 y 31 800 MXN, diferencia +2 800.",
  "B conserva 28 observaciones y conecta los dos saldos de cada crédito; cada par aumenta 200 MXN.",
  "Las vistas tienen ejes de agregación diferente. Datos sintéticos, cobertura 14/18 por fecha; sin interpretación causal."
)
cat(descripcion_conjunto, "\n")
print(control)

cat("Composicion comprobada; fuente intacta.\n")

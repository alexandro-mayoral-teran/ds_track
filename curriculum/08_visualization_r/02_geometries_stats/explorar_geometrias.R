# Mismo proyecto renv de 07.10/08.01; ejecutar desde su raiz en el IDE.
# No instala, exporta ni modifica entradas. Guardar como output/mi_geometrias.R.
if (!file.exists("R/funciones_cierre.R") || !file.exists(".Rprofile")) {
  stop("Abre el proyecto preparado para 07.10 y manten su raiz como directorio.")
}
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
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(cierre$comunes) == 14L, nrow(cierre$sin_pareja) == 8L,
          nrow(cierre$fuera_cortes) == 0L,
          identical(cierre$datos_figura$saldo_mxn, c(29000, 31800)))

# Resumen: dos filas. Pares: 14 filas. Detalle: 28 observaciones credito/corte.
resumen <- cierre$datos_figura |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"),
                 levels = c("2026-09-30", "2026-10-31"))
)
pares <- cierre$comunes
detalle <- dplyr::bind_rows(
  pares |> dplyr::select(id_credito, saldo_mxn = saldo_sep) |>
    dplyr::mutate(fecha_corte = as.Date("2026-09-30")),
  pares |> dplyr::select(id_credito, saldo_mxn = saldo_oct) |>
    dplyr::mutate(fecha_corte = as.Date("2026-10-31"))
) |> dplyr::mutate(
  corte = factor(format(fecha_corte, "%Y-%m-%d"), levels = levels(resumen$corte))
)
control_detalle <- detalle |> dplyr::group_by(fecha_corte) |>
  dplyr::summarise(creditos = dplyr::n(), saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop")
stopifnot(nrow(detalle) == 28L, !anyNA(detalle),
          anyDuplicated(detalle[c("id_credito", "fecha_corte")]) == 0L,
          identical(control_detalle$creditos, c(14L, 14L)),
          identical(control_detalle$saldo_mxn, resumen$saldo_mxn))
print(control_detalle)

# Identidad: usa alturas ya calculadas. Conteo: calcula cantidad de filas.
barras <- ggplot2::ggplot(resumen, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_col(fill = "#246A86", width = 0.6) +
  ggplot2::labs(title = "Saldo de los mismos 14 créditos",
                 x = "Fecha de corte", y = "Saldo observado (MXN)") +
  ggplot2::theme_minimal(base_size = 12)
conteo_resumen <- ggplot2::ggplot(resumen, ggplot2::aes(corte)) + ggplot2::geom_bar()
conteo_detalle <- ggplot2::ggplot(detalle, ggplot2::aes(corte)) + ggplot2::geom_bar()
print(barras)
print(conteo_resumen)
print(conteo_detalle)

# Linea: conecta dos observaciones temporales de una sola serie.
linea <- ggplot2::ggplot(resumen, ggplot2::aes(fecha_corte, saldo_mxn, group = 1)) +
  ggplot2::geom_line(linewidth = 0.8, colour = "#246A86") +
  ggplot2::geom_point(size = 3, colour = "#246A86") +
  ggplot2::scale_x_date(breaks = resumen$fecha_corte, date_labels = "%Y-%m-%d") +
  ggplot2::labs(title = "Dos cortes observados de los mismos 14 créditos",
    x = "Fecha de corte", y = "Saldo observado (MXN)",
    caption = "Datos sintéticos. Base común: 14/18 por corte.\nEl tramo no son mediciones diarias.") +
  ggplot2::theme_minimal(base_size = 12)
print(linea)

# Dispersion: cada fila contiene los dos saldos del mismo ID.
dispersion <- ggplot2::ggplot(pares, ggplot2::aes(saldo_sep, saldo_oct)) +
  ggplot2::geom_point(size = 3, colour = "#246A86") +
  ggplot2::labs(title = "Saldos por crédito en dos fechas",
    subtitle = "14 pares; cada punto corresponde al mismo ID",
    x = "Saldo septiembre (MXN)", y = "Saldo octubre (MXN)",
    caption = "Datos sintéticos: todos los pares aumentan 200 MXN.\nEsta relación construida no demuestra una causa.") +
  ggplot2::theme_minimal(base_size = 12)
print(dispersion)
stopifnot(all(pares$saldo_oct - pares$saldo_sep == 200L))

# Histograma de un solo corte, con bordes y cierre explicitos.
septiembre <- detalle |> dplyr::filter(fecha_corte == as.Date("2026-09-30"))
bordes <- seq(1000, 3500, by = 500)
frecuencias <- graphics::hist(septiembre$saldo_mxn, breaks = bordes,
  right = TRUE, include.lowest = TRUE, plot = FALSE)
stopifnot(identical(frecuencias$counts, c(4L, 3L, 3L, 2L, 2L)),
          sum(frecuencias$counts) == 14L)
histograma <- ggplot2::ggplot(septiembre, ggplot2::aes(saldo_mxn)) +
  ggplot2::geom_histogram(breaks = bordes, closed = "right",
                          fill = "#246A86", colour = "white") +
  ggplot2::scale_x_continuous(breaks = bordes) +
  ggplot2::labs(title = "Distribución del saldo en septiembre",
    subtitle = "Los mismos 14 IDs de la comparación; intervalos de 500 MXN",
    x = "Saldo por crédito (MXN)", y = "Créditos por intervalo",
    caption = "Datos sintéticos. Suma de frecuencias: 14.\nNo se representan sumas de saldo.") +
  ggplot2::theme_minimal(base_size = 12)
print(histograma)
print(frecuencias$counts)

# Caja: cuantiles tipo 7 y bigotes 1.5 IQR; los puntos conservan el detalle.
cuartiles <- detalle |> dplyr::group_by(corte) |>
  dplyr::summarise(n = dplyr::n(),
    q1 = stats::quantile(saldo_mxn, 0.25, type = 7, names = FALSE),
    mediana = stats::median(saldo_mxn),
    q3 = stats::quantile(saldo_mxn, 0.75, type = 7, names = FALSE),
    .groups = "drop")
cajas <- ggplot2::ggplot(detalle, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_boxplot(coef = 1.5, quantile.type = 7,
                        outlier.shape = NA, fill = "#D9EBF2", width = 0.5) +
  ggplot2::geom_point(position = ggplot2::position_jitter(width = 0.08, height = 0, seed = 802),
                       size = 2, colour = "#246A86") +
  ggplot2::labs(title = "Distribución del saldo de los mismos 14 créditos",
    subtitle = "Caja por fecha y 14 observaciones por corte",
    x = "Fecha de corte", y = "Saldo por crédito (MXN)",
    caption = "Datos sintéticos. Puntos desplazados solo horizontalmente.\nLas cajas no muestran el emparejamiento por ID.") +
  ggplot2::theme_minimal(base_size = 12)
print(cajas)
print(cuartiles)

# Inspeccion de la estadistica de cada capa, sin modificar sus datos internos.
calculado_hist <- ggplot2::layer_data(histograma, 1)
calculado_caja <- ggplot2::layer_data(cajas, 1)
stopifnot(identical(ggplot2::layer_data(barras, 1)$y, c(29000, 31800)),
          identical(ggplot2::layer_data(conteo_resumen, 1)$count, c(1, 1)),
          identical(ggplot2::layer_data(conteo_detalle, 1)$count, c(14, 14)),
          identical(calculado_hist$count, as.double(frecuencias$counts)),
          identical(calculado_caja$lower, cuartiles$q1),
          identical(calculado_caja$middle, cuartiles$mediana),
          identical(calculado_caja$upper, cuartiles$q3),
          identical(huella, tools::md5sum(ruta)))
print(calculado_hist[c("xmin", "xmax", "count")])
print(calculado_caja[c("ymin", "lower", "middle", "upper", "ymax")])
print(utils::packageVersion("ggplot2"))
cat("Geometrias comprobadas; fuente intacta, sin nuevas dependencias ni exportacion.\n")

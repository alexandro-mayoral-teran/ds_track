# Ejecutar desde la raiz del mismo proyecto renv de 07.10, en el IDE.
# Guardar una copia propia como output/mi_esteticas.R; no instala ni exporta.
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
control <- detalle |> dplyr::group_by(fecha_corte) |>
  dplyr::summarise(creditos = dplyr::n(),
    saldo_mxn = sum(as.double(saldo_mxn)), .groups = "drop")
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          nrow(pares) == 14L, nrow(detalle) == 28L,
          nrow(cierre$sin_pareja) == 8L,
          !anyNA(detalle), anyDuplicated(detalle[c("id_credito", "fecha_corte")]) == 0L,
          identical(control$creditos, c(14L, 14L)),
          identical(control$saldo_mxn, c(29000, 31800)))
print(control)

base_barras <- ggplot2::ggplot(resumen, ggplot2::aes(corte, saldo_mxn))
fijas <- base_barras +
  ggplot2::geom_col(fill = "#246A86", colour = "#183C4A", width = 0.6) +
  ggplot2::labs(title = "Saldo de los mismos 14 créditos",
    subtitle = "Relleno constante; la fecha se lee en el eje",
    x = "Fecha de corte", y = "Saldo observado (MXN)") +
  ggplot2::theme_minimal(base_size = 12)
print(fijas)

mapeadas <- base_barras +
  ggplot2::geom_col(ggplot2::aes(fill = corte), width = 0.6) +
  ggplot2::labs(title = "Saldo de los mismos 14 créditos",
    subtitle = "El relleno representa la fecha, además del eje",
    x = "Fecha de corte", y = "Saldo observado (MXN)", fill = "Fecha de corte") +
  ggplot2::theme_minimal(base_size = 12)
print(mapeadas)

paleta <- c("2026-09-30" = "#246A86", "2026-10-31" = "#A34E12")
manual <- mapeadas + ggplot2::scale_fill_manual(values = paleta) +
  ggplot2::theme(legend.position = "bottom")
print(manual)

accidental <- base_barras + ggplot2::geom_col(ggplot2::aes(fill = "red"))
rojas <- base_barras + ggplot2::geom_col(fill = "red")
print(accidental)
print(rojas)

puntos <- ggplot2::ggplot(detalle, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_point(ggplot2::aes(fill = corte), shape = 21,
    colour = "#183C4A", size = 3, stroke = 0.7) +
  ggplot2::scale_fill_manual(values = paleta) +
  ggplot2::labs(title = "Saldo por crédito y fecha",
    subtitle = "28 observaciones de 14 IDs; puntos coincidentes pueden superponerse",
    x = "Fecha de corte", y = "Saldo por crédito (MXN)", fill = "Fecha de corte") +
  ggplot2::theme_minimal(base_size = 12)
print(puntos)

doble_senal <- ggplot2::ggplot(detalle, ggplot2::aes(corte, saldo_mxn)) +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 3) +
  ggplot2::labs(colour = "Fecha de corte", shape = "Fecha de corte",
    x = "Fecha de corte", y = "Saldo por crédito (MXN)")
tamano <- ggplot2::ggplot(pares, ggplot2::aes(saldo_sep, saldo_oct)) +
  ggplot2::geom_point(ggplot2::aes(size = saldo_sep), colour = "#246A86") +
  ggplot2::labs(size = "Saldo septiembre (MXN)",
    x = "Saldo septiembre (MXN)", y = "Saldo octubre (MXN)")
print(doble_senal)
print(tamano)

trayectorias <- ggplot2::ggplot(detalle,
    ggplot2::aes(fecha_corte, saldo_mxn)) +
  ggplot2::geom_line(ggplot2::aes(group = id_credito),
    colour = "#68747A", linewidth = 0.6, alpha = 0.6) +
  ggplot2::geom_point(ggplot2::aes(colour = corte, shape = corte), size = 2.8) +
  ggplot2::scale_colour_manual(values = paleta) +
  ggplot2::scale_x_date(breaks = resumen$fecha_corte, date_labels = "%Y-%m-%d") +
  ggplot2::labs(title = "Dos observaciones por crédito",
    subtitle = "14 grupos por ID; color y forma de puntos indican la fecha",
    x = "Fecha de corte", y = "Saldo por crédito (MXN)",
    colour = "Fecha de corte", shape = "Fecha de corte",
    caption = "Datos sintéticos. Base común: 14/18 por corte.\nLos tramos no son mediciones diarias ni explican causas.") +
  ggplot2::theme_minimal(base_size = 12)
print(trayectorias)

capa_fija <- ggplot2::layer_data(fijas, 1)
capa_manual <- ggplot2::layer_data(manual, 1)
lineas <- ggplot2::layer_data(trayectorias, 1)
grupos <- split(lineas, lineas$group)
firma <- function(x, y) paste(x, y, sep = "/")
pares_dibujados <- vapply(grupos, function(g) {
  g <- g[order(g$x), ]
  stopifnot(nrow(g) == 2L,
            identical(g$x, as.numeric(resumen$fecha_corte)))
  firma(g$y[1], g$y[2])
}, character(1))
stopifnot(identical(capa_fija$y, c(29000, 31800)),
          identical(capa_manual$y, capa_fija$y),
          all(capa_fija$fill == "#246A86"),
          identical(capa_manual$fill, unname(paleta[as.character(resumen$corte)])),
          length(grupos) == 14L,
          identical(sort(unname(pares_dibujados)),
                    sort(firma(pares$saldo_sep, pares$saldo_oct))),
          nrow(ggplot2::layer_data(trayectorias, 2)) == 28L,
          identical(huella, tools::md5sum(ruta)))
print(table(lineas$group))

cat("Esteticas comprobadas; fuente intacta.\n")

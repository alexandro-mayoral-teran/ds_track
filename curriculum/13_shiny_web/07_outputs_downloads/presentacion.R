# Requiere cartera.R; no consulta archivos ni entradas de Shiny al definir.
exigir_exportable <- function(consulta) {
  if (is.null(consulta) || nrow(consulta$universo) == 0L) stop("No hay consulta con universo para exportar.")
  validar_cartera(consulta$seleccion)
  invisible(TRUE)
}

crear_grafica <- function(consulta) {
  exigir_exportable(consulta)
  datos <- consulta$seleccion
  if (nrow(datos) == 0L) stop("No hay filas para graficar.")
  techo <- max(1, datos$saldo_mxn) * 1.15
  ggplot2::ggplot(datos, ggplot2::aes(x = id_credito, y = saldo_mxn)) +
    ggplot2::geom_col(fill = "#27648C", width = 0.65) +
    ggplot2::geom_text(ggplot2::aes(label = format(saldo_mxn, scientific = FALSE, trim = TRUE)), vjust = -0.4) +
    ggplot2::scale_y_continuous(limits = c(0, techo), expand = ggplot2::expansion(mult = 0)) +
    ggplot2::labs(title = "Saldo de los creditos seleccionados", subtitle = paste("Corte aplicado:", consulta$filtros$corte),
                  x = "Credito", y = "Saldo (MXN)") +
    ggplot2::theme_minimal(base_size = 12)
}

descripcion_grafica <- function(consulta) {
  exigir_exportable(consulta)
  if (nrow(consulta$seleccion) == 0L) return("Seleccion vacia: no hay barras para mostrar.")
  paste0("Saldo en MXN por credito, corte aplicado ", consulta$filtros$corte, ": ",
    paste(paste0(consulta$seleccion$id_credito, " = ", format(consulta$seleccion$saldo_mxn, scientific = FALSE, trim = TRUE)), collapse = "; "), ".")
}

crear_contexto <- function(consulta) {
  exigir_exportable(consulta)
  f <- consulta$filtros; m <- consulta$indicadores
  data.frame(corte = f$corte,
    segmentos = if (length(f$segmentos) == 0L) "ninguno" else paste(f$segmentos, collapse = "|"),
    minimo_mxn = f$minimo_mxn, regla = "saldo_mxn >= minimo_mxn",
    creditos_universo = nrow(consulta$universo), saldo_universo_mxn = sum(as.numeric(consulta$universo$saldo_mxn)),
    creditos_seleccion = m$cantidad, saldo_seleccion_mxn = m$saldo_mxn, porcentaje_creditos = m$porcentaje_creditos,
    stringsAsFactors = FALSE)
}

escribir_seleccion <- function(consulta, archivo) {
  exigir_exportable(consulta)
  utils::write.csv(consulta$seleccion, archivo, row.names = FALSE, fileEncoding = "UTF-8", na = "")
}

escribir_contexto <- function(consulta, archivo) {
  utils::write.csv(crear_contexto(consulta), archivo, row.names = FALSE, fileEncoding = "UTF-8", na = "")
}

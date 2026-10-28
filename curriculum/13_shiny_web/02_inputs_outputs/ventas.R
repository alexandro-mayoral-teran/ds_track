# Muestra sintetica conocida: funciones sin Shiny ni trabajo al importar.
crear_ventas <- function() {
  ventas <- data.frame(
    venta_id = c("V001", "V002", "V003", "V004"),
    unidades = c(4L, 2L, 0L, 3L),
    precio_mxn = c(75L, 120L, 50L, 40L),
    stringsAsFactors = FALSE
  )
  ventas$importe_mxn <- ventas$unidades * ventas$precio_mxn
  ventas
}

consultar_venta <- function(ventas, clave) {
  # Un control de lista no sustituye la comprobacion del valor recibido.
  opciones <- c("todas", ventas$venta_id)
  if (!is.character(clave) || length(clave) != 1L || is.na(clave) || !clave %in% opciones) {
    stop("La venta debe ser una clave conocida o 'todas'.")
  }
  if (identical(clave, "todas")) return(ventas)
  ventas[ventas$venta_id == clave, , drop = FALSE]
}

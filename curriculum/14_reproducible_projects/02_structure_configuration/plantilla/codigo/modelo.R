# Solo define funciones. R base; no activa renv, instala ni escribe archivos.
fecha_contrato <- function(x) {
  valor <- tryCatch(as.Date(x, "%Y-%m-%d"), error = function(e) as.Date(NA))
  is.character(x) && length(x) == 1L && !is.na(x) &&
    grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", x) && !is.na(valor) &&
    format(valor, "%Y-%m-%d") == x && x >= "1900-01-01" && x <= "2100-12-31"
}
leer_contrato <- function(ruta) {
  read.csv(ruta, colClasses = "character", check.names = FALSE, row.names = NULL,
    na.strings = NULL, fileEncoding = "UTF-8", fill = FALSE, blank.lines.skip = FALSE)
}
resolver_contrato <- function(datos, corte, segmentos, minimo) {
  columnas <- c("ids", "saldos_mxn", "creditos_universo", "creditos_seleccion", "saldo_universo_mxn", "saldo_seleccion_mxn", "porcentaje_creditos")
  salida <- setNames(rep("", length(columnas)), columnas)
  segs <- if (segmentos == "ninguno") character() else strsplit(segmentos, "|", fixed = TRUE)[[1]]
  valido <- fecha_contrato(corte) && grepl("^(0|[1-9][0-9]{0,6})$", minimo) &&
    as.numeric(minimo) <= 1000000 && segmentos %in% c("ninguno", "comercio", "servicios", "comercio|servicios", "servicios|comercio")
  if (!valido) return(c(estado = "rechazo", salida))
  universo <- datos[datos$fecha_corte == corte, , drop = FALSE]
  if (nrow(universo) == 0L) return(c(estado = "sin_universo", salida))
  seleccion <- universo[universo$segmento %in% segs & universo$saldo_mxn >= as.numeric(minimo), , drop = FALSE]
  seleccion <- seleccion[order(seleccion$id_credito), , drop = FALSE]
  c(estado = if (nrow(seleccion) > 0L) "ok" else "vacio", ids = paste(seleccion$id_credito, collapse = "|"),
    saldos_mxn = paste(format(seleccion$saldo_mxn, scientific = FALSE, trim = TRUE), collapse = "|"),
    creditos_universo = as.character(nrow(universo)), creditos_seleccion = as.character(nrow(seleccion)),
    saldo_universo_mxn = format(sum(universo$saldo_mxn), scientific = FALSE, trim = TRUE),
    saldo_seleccion_mxn = format(sum(seleccion$saldo_mxn), scientific = FALSE, trim = TRUE),
    porcentaje_creditos = as.character(100 * nrow(seleccion) / nrow(universo)))
}
leer_fuente_modelo <- function(ruta) {
  datos <- leer_contrato(ruta)
  stopifnot(identical(names(datos), c("id_credito", "segmento", "fecha_corte", "saldo_mxn")),
    nrow(datos) <= 10000L, !anyNA(datos), all(grepl("^[0-9]{3}$", datos$id_credito)),
    all(datos$segmento %in% c("comercio", "servicios")),
    all(grepl("^(0|[1-9][0-9]{0,6})$", datos$saldo_mxn)),
    !anyDuplicated(datos[c("id_credito", "fecha_corte")]))
  stopifnot(all(vapply(unique(datos$fecha_corte), fecha_contrato, logical(1))))
  datos$saldo_mxn <- as.numeric(datos$saldo_mxn)
  stopifnot(all(is.finite(datos$saldo_mxn)), all(datos$saldo_mxn <= 1000000))
  datos
}

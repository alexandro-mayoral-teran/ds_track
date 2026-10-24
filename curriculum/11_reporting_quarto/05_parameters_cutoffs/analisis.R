# Funciones R base; validacion del lote completo antes del filtro de fecha.
analizar <- function(origen, fecha_corte, minimo_mxn) {
  if (!is.character(fecha_corte) || length(fecha_corte) != 1L || is.na(fecha_corte) ||
      !grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha_corte)) stop("fecha_corte debe ser texto ISO YYYY-MM-DD")
  fecha <- as.Date(fecha_corte, format = "%Y-%m-%d")
  if (is.na(fecha) || format(fecha, "%Y-%m-%d") != fecha_corte ||
      fecha < as.Date("1900-01-01") || fecha > as.Date("2100-12-31")) stop("Calendario o rango de fecha invalido")
  if (!is.numeric(minimo_mxn) || length(minimo_mxn) != 1L || is.na(minimo_mxn) ||
      !is.finite(minimo_mxn) || minimo_mxn < 0 || minimo_mxn > 1000000 ||
      minimo_mxn != floor(minimo_mxn)) stop("minimo_mxn debe ser numerico entero entre 0 y 1000000")
  minimo <- as.integer(minimo_mxn)
  fechas <- c("2026-09-30", "2026-10-31")
  esperadas <- c(as.vector(outer(c("001", "002", "003"), fechas, paste, sep = "|")), "004|2026-10-31")
  d <- read.csv(origen, colClasses = "character", check.names = FALSE,
                na.strings = NULL, strip.white = FALSE)
  if (!identical(names(d), c("credito_id", "fecha_corte", "saldo_mxn")) ||
      nrow(d) != 7L || anyNA(d)) stop("Columnas o cobertura distintas del contrato")
  claves <- paste(d$credito_id, d$fecha_corte, sep = "|")
  if (anyDuplicated(claves) || !setequal(claves, esperadas) ||
      any(!grepl("^(0|[1-9][0-9]{0,6})$", d$saldo_mxn))) stop("Clave o saldo invalido/repetido en la fuente completa")
  d$saldo <- as.integer(d$saldo_mxn)
  if (any(d$saldo > 1000000L)) stop("Saldo excede 1000000 MXN")
  if (!fecha_corte %in% fechas) stop("Corte no disponible: no se interpreta como universo vacio")
  filas <- d[d$fecha_corte == fecha_corte, c("credito_id", "saldo")]
  filas <- filas[order(filas$credito_id), , drop = FALSE]
  filas$cumple <- filas$saldo >= minimo
  seleccion <- filas[filas$cumple, , drop = FALSE]
  ids <- if (nrow(seleccion)) paste(seleccion$credito_id, collapse = ", ") else "ninguno"
  list(fecha = fecha_corte, minimo = minimo, filas = filas, universo_n = nrow(filas),
       universo_mxn = sum(filas$saldo), seleccion_n = nrow(seleccion),
       seleccion_mxn = sum(seleccion$saldo),
       proporcion = paste0(formatC(100 * nrow(seleccion) / nrow(filas), format = "f", digits = 2, decimal.mark = "."), "%"),
       ids = ids)
}

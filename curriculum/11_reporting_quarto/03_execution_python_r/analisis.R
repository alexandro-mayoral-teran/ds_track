# R base; no depende de objetos calculados en la sesión interactiva.
analizar <- function(origen) {
  ids <- c("001", "002", "003")
  fechas <- c("2026-09-30", "2026-10-31")
  d <- read.csv(origen, colClasses = "character", check.names = FALSE,
                na.strings = NULL, strip.white = FALSE)
  if (!identical(names(d), c("credito_id", "fecha_corte", "saldo_mxn")) ||
      nrow(d) != 6L || anyNA(d)) stop("Columnas o cobertura distintas del contrato")
  claves <- paste(d$credito_id, d$fecha_corte, sep = "|")
  esperadas <- as.vector(outer(ids, fechas, paste, sep = "|"))
  if (anyDuplicated(claves) || !setequal(claves, esperadas) ||
      any(!grepl("^(0|[1-9][0-9]{0,6})$", d$saldo_mxn))) stop("Clave o saldo inválido/repetido")
  saldos <- as.integer(d$saldo_mxn)
  if (any(saldos > 1000000L)) stop("Saldo excede 1000000 MXN")
  a <- saldos[match(paste(ids, fechas[1], sep = "|"), claves)]
  b <- saldos[match(paste(ids, fechas[2], sep = "|"), claves)]
  inicial <- sum(a)
  final <- sum(b)
  tasa <- if (inicial == 0) "no definida (base inicial cero)" else
    paste0(formatC(100 * (final - inicial) / inicial, format = "f", digits = 2,
                  decimal.mark = "."), "%")
  list(septiembre = inicial, octubre = final, diferencia = final - inicial,
       tasa = tasa, pares = data.frame(credito_id = ids, septiembre = a, octubre = b))
}

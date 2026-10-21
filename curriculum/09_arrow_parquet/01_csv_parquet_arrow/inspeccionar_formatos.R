# Solo define funciones; biblioteca base de R, sin inicializar renv ni exportar.
leer_observaciones <- function(ruta) {
  x <- utils::read.csv(ruta, colClasses = "character", check.names = FALSE,
    na.strings = NULL, strip.white = FALSE, blank.lines.skip = FALSE,
    fill = FALSE, fileEncoding = "UTF-8", stringsAsFactors = FALSE)
  stopifnot(identical(names(x), c("id_credito", "fecha_corte", "saldo_mxn")), !anyNA(x),
    all(grepl("^[0-9]{3}$", x$id_credito)),
    all(grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", x$fecha_corte)),
    all(substr(x$fecha_corte, 1, 4) >= "1900" & substr(x$fecha_corte, 1, 4) <= "2100"),
    all(grepl("^[0-9]+$", x$saldo_mxn)))
  fecha <- as.Date(x$fecha_corte, format = "%Y-%m-%d")
  saldo <- as.double(x$saldo_mxn)
  stopifnot(!anyNA(fecha), identical(format(fecha, "%Y-%m-%d"), x$fecha_corte),
    all(is.finite(saldo)), all(saldo <= .Machine$integer.max))
  x$fecha_corte <- fecha
  x$saldo_mxn <- as.integer(saldo)
  stopifnot(!anyDuplicated(x[c("id_credito", "fecha_corte")]))
  x
}

inspeccionar_formatos <- function(carpeta = "curriculum/09_arrow_parquet/01_csv_parquet_arrow/datos") {
  x <- leer_observaciones(file.path(carpeta, "base_comun.csv"))
  cortes <- as.Date(c("2026-09-30", "2026-10-31"))
  cantidades <- vapply(seq_along(cortes), function(i) sum(x$fecha_corte == cortes[i]), integer(1))
  saldos <- vapply(seq_along(cortes), function(i) sum(as.double(x$saldo_mxn[x$fecha_corte == cortes[i]])), double(1))
  stopifnot(nrow(x) == 28L, length(unique(x$id_credito)) == 14L,
    identical(cantidades, c(14L, 14L)), identical(saldos, c(29000, 31800)))
  inventario <- utils::read.csv(file.path(carpeta, "inventario.csv"), colClasses = "character",
    check.names = FALSE, na.strings = NULL, fileEncoding = "UTF-8")
  stopifnot(identical(names(inventario), c("archivo", "filas", "columnas", "bytes", "md5")),
    identical(inventario$archivo, c("base_comun.csv", "base_comun.parquet")),
    all(inventario$filas == "28"), all(inventario$columnas == "3"))
  rutas <- file.path(carpeta, inventario$archivo)
  stopifnot(identical(as.double(inventario$bytes), as.double(file.info(rutas)$size)),
    identical(inventario$md5, unname(tools::md5sum(rutas))))
  conexion <- file(rutas[2], "rb")
  on.exit(close(conexion))
  inicio <- readBin(conexion, "raw", n = 4L)
  seek(conexion, where = -4, origin = "end")
  final <- readBin(conexion, "raw", n = 4L)
  stopifnot(identical(rawToChar(inicio), "PAR1"), identical(rawToChar(final), "PAR1"))
  list(observaciones = x,
    resumen = data.frame(fecha_corte = cortes, registros = cantidades, saldo_mxn = saldos),
    inventario = inventario, alcance = "CSV interpretado; Parquet sin decodificar")
}

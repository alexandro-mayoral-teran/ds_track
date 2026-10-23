# source() define funciones; no instala, no abre conexiones ni lee datos.
fuente_1007 <- function() "datos/muestra_1007.csv"
leer_1007 <- function(fuente = fuente_1007()) {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  x <- e$evaluar_contrato(e$leer_textos_contrato(fuente, e$columnas_contrato))
  if (any(!x$diagnostico$aceptado)) stop("CSV externo fuera del contrato")
  # Limite conservador: referencia R base suma doubles exactos solo en esta cota.
  if (nrow(x$tipados) > floor(2^53 / 2147483647)) stop("Referencia fuera de la cota exacta")
  x$tipados
}

parametros_1007 <- function(corte, minimo, pagina = 2L) {
  dias <- if (identical(class(corte), "Date")) as.numeric(corte) else NA_real_
  if (length(dias) != 1L || is.na(dias) || !is.finite(dias) || dias != floor(dias) ||
      corte < as.Date("1900-01-01") || corte > as.Date("2100-12-31")) stop("corte debe ser Date valido")
  if (!is.integer(minimo) || length(minimo) != 1L || is.na(minimo) || minimo < 0L) stop("minimo debe ser integer no negativo")
  if (!is.integer(pagina) || length(pagina) != 1L || is.na(pagina) || pagina < 1L) stop("pagina debe ser integer positivo")
}

sql_1007 <- function(nombre) paste(readLines(file.path("SQL", nombre), encoding = "UTF-8"), collapse = "\n")
abrir_1007 <- function() DBI::dbConnect(duckdb::duckdb(shared_home = FALSE), dbdir = ":memory:")

preparar_1007 <- function(destino, fuente = fuente_1007()) {
  filas <- leer_1007(fuente)
  if (length(destino) != 1L || is.na(destino) || !nzchar(destino) || file.exists(destino)) stop("Destino debe ser carpeta nueva")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear destino")
  archivo <- file.path(normalizePath(destino, winslash = "/"), "completo.parquet")
  con <- abrir_1007()
  on.exit(DBI::dbDisconnect(con, shutdown = TRUE), add = TRUE)
  DBI::dbWriteTable(con, "saldos", filas,
    field.types = c(id_credito = "VARCHAR", fecha_corte = "DATE", saldo_mxn = "INTEGER"))
  DBI::dbExecute(con, "COPY saldos TO ? (FORMAT PARQUET, COMPRESSION ZSTD)", params = list(archivo))
  archivo
}

auditar_1007 <- function(con, archivo, fuente = fuente_1007()) {
  if (length(archivo) != 1L || !file.exists(archivo)) stop("Indica un archivo existente")
  esperado <- leer_1007(fuente)
  d <- DBI::dbGetQuery(con, "DESCRIBE SELECT * FROM read_parquet(?)", params = list(archivo))
  if (!identical(d$column_name, c("id_credito", "fecha_corte", "saldo_mxn")) ||
      !identical(d$column_type, c("VARCHAR", "DATE", "INTEGER"))) stop("Esquema Parquet distinto")
  x <- DBI::dbGetQuery(con, "SELECT * FROM read_parquet(?) ORDER BY id_credito,fecha_corte", params = list(archivo))
  esperado <- esperado[order(esperado$id_credito, esperado$fecha_corte), , drop = FALSE]
  rownames(esperado) <- NULL
  if (!identical(x, esperado)) stop("Entrada distinta del CSV externo por clave/valor")
  invisible(esperado)
}

recuperar_1007 <- function(con, sql, parametros, pagina) {
  # DESCRIBE comprueba tipos SQL; dbColumnInfo antes de fetch puede ser unknown en este cliente.
  d <- DBI::dbGetQuery(con, paste("DESCRIBE", sql), params = parametros)
  if (!identical(d$column_name, c("id_credito", "saldo_mxn")) ||
      !identical(d$column_type, c("VARCHAR", "INTEGER"))) stop("Esquema de seleccion distinto")
  res <- DBI::dbSendQuery(con, sql)
  on.exit(DBI::dbClearResult(res), add = TRUE)
  DBI::dbBind(res, parametros)
  salida <- DBI::dbFetch(res, n = 0)
  repeat {
    bloque <- DBI::dbFetch(res, n = pagina)
    if (!nrow(bloque)) break
    salida <- rbind(salida, bloque)
  }
  salida
}

ejecutar_1007 <- function(archivo, fuente = fuente_1007(), corte = as.Date("2026-10-31"), minimo = 2000L, pagina = 2L) {
  parametros_1007(corte, minimo, pagina)
  con <- abrir_1007()
  on.exit(DBI::dbDisconnect(con, shutdown = TRUE), add = TRUE)
  filas <- auditar_1007(con, archivo, fuente)
  seleccion <- recuperar_1007(con, sql_1007("seleccion_1007.sql"), list(archivo, corte, minimo), pagina)
  esperado <- filas[filas$fecha_corte == corte & filas$saldo_mxn >= minimo, c("id_credito", "saldo_mxn"), drop = FALSE]
  esperado <- esperado[order(esperado$id_credito), , drop = FALSE]
  rownames(esperado) <- NULL
  if (!identical(seleccion, esperado)) stop("Seleccion distinta por clave/valor")
  resumen <- DBI::dbGetQuery(con, sql_1007("resumen_1007.sql"), params = list(archivo))
  cortes <- sort(unique(filas$fecha_corte))
  texto <- function(x) format(x, scientific = FALSE, trim = TRUE)
  esperado_r <- data.frame(fecha_corte = cortes,
    registros_texto = vapply(seq_along(cortes), function(i) texto(sum(filas$fecha_corte == cortes[i])), character(1)),
    saldo_texto = vapply(seq_along(cortes), function(i) texto(sum(as.double(filas$saldo_mxn[filas$fecha_corte == cortes[i]]))), character(1)))
  if (!identical(resumen, esperado_r)) stop("Resumen distinto de referencia R base")
  list(seleccion = seleccion, resumen = resumen,
    control = c(registros = nrow(seleccion), saldo_mxn = sum(as.double(seleccion$saldo_mxn))),
    version = DBI::dbGetQuery(con, "SELECT version() AS version")$version)
}

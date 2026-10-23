# Extension R: source() solo define. Proyecto renv preparado con Arrow/DBI/DuckDB.
ejecutar_1008_r <- function(fuente = "datos/muestra_1008.csv",
    corte = as.Date("2026-10-31"), minimo = 2000L) {
  # Funciones del proyecto, no entregas de otra practica.
  e <- new.env(parent = globalenv())
  sys.source("R/clientes_1007.R", envir = e)
  e$parametros_1007(corte, minimo)
  filas <- e$leer_1007(fuente)
  esquema <- arrow::schema(id_credito = arrow::utf8(),
    fecha_corte = arrow::date32(), saldo_mxn = arrow::int32())
  entrada <- arrow::arrow_table(filas, schema = esquema)
  con <- e$abrir_1007()
  on.exit(DBI::dbDisconnect(con, shutdown = TRUE), add = TRUE)
  duckdb::duckdb_register_arrow(con, "entrada", entrada)
  on.exit(duckdb::duckdb_unregister_arrow(con, "entrada"), add = TRUE, after = FALSE)
  tipos <- DBI::dbGetQuery(con, "DESCRIBE SELECT * FROM entrada")
  if (!identical(tipos$column_type, c("VARCHAR", "DATE", "INTEGER"))) stop("Tipos SQL incompatibles")
  nativa <- DBI::dbGetQuery(con, "SELECT * FROM entrada ORDER BY id_credito,fecha_corte")
  esperada <- filas[order(filas$id_credito, filas$fecha_corte), , drop = FALSE]
  rownames(esperada) <- NULL
  # Antes de volver a Arrow: comprobar clases y cada valor nativo.
  if (!identical(nativa, esperada)) stop("Cambio de clases/valores en DBI")
  vuelta <- arrow::arrow_table(nativa, schema = esquema)
  if (!vuelta$schema$Equals(esquema, check_metadata = FALSE) ||
      !identical(as.data.frame(vuelta), esperada)) stop("Cambio de tipos/valores al volver a Arrow")
  seleccion <- DBI::dbGetQuery(con,
    "SELECT id_credito,saldo_mxn FROM entrada WHERE fecha_corte=CAST(? AS DATE)
     AND saldo_mxn>=? ORDER BY id_credito", params = list(corte, minimo))
  objetivo <- esperada[esperada$fecha_corte == corte & esperada$saldo_mxn >= minimo,
    c("id_credito", "saldo_mxn"), drop = FALSE]
  rownames(objetivo) <- NULL
  if (!identical(seleccion, objetivo)) stop("Seleccion distinta")
  list(seleccion = seleccion, esquema = vuelta$schema,
    resumen = data.frame(fecha_corte = sort(unique(filas$fecha_corte)),
      saldo_mxn = vapply(sort(unique(filas$fecha_corte)),
        function(corte_actual) sum(as.double(filas$saldo_mxn[filas$fecha_corte == corte_actual])), double(1))),
    version = DBI::dbGetQuery(con, "SELECT version() AS version")$version)
}

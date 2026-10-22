# Desde la raiz del proyecto renv de 09.04. source() no lee ni escribe datos.
funciones_cartera_cruce <- function() {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  e
}

esquema_muestra_cruce <- function() {
  arrow::schema(
    arrow::field("id_prueba", arrow::utf8(), nullable = FALSE),
    arrow::field("fecha", arrow::date32(), nullable = FALSE),
    arrow::field("etiqueta", arrow::utf8(), nullable = TRUE),
    arrow::field("importe", arrow::int32(), nullable = TRUE)
  )
}

construir_muestra_cruce <- function() {
  x <- data.frame(id_prueba = c("A", "B", "C"),
    fecha = as.Date(c("2024-02-29", "2026-09-30", "2026-10-31")),
    etiqueta = c("Crédito ágil", "", NA_character_),
    importe = c(0L, NA_integer_, 10L))
  tabla <- arrow::arrow_table(x, schema = esquema_muestra_cruce())
  tabla$metadata <- NULL
  tabla
}

comparar_muestra_cruce <- function(observada) {
  if (!inherits(observada, "Table") ||
      !observada$schema$Equals(esquema_muestra_cruce(), check_metadata = FALSE)) {
    stop("Esquema distinto en la muestra de intercambio")
  }
  x <- as.data.frame(observada)
  if (anyNA(x$id_prueba) || anyNA(x$fecha)) stop("ID/fecha ausentes en la muestra")
  x <- x[order(x$id_prueba), , drop = FALSE]
  rownames(x) <- NULL
  if (!identical(x, as.data.frame(construir_muestra_cruce()))) {
    stop("Claves o valores distintos en la muestra de intercambio")
  }
  list(registros = 3L, importes_conocidos = 2L, suma_observada = 10L)
}

leer_desde_python <- function(carpeta, ruta_csv = "datos/base_comun_0904.csv") {
  # Se comprueban ambos archivos antes de devolver exito. No se escriben notas.
  funciones <- funciones_cartera_cruce()
  resumen <- funciones$verificar_parquet_r(file.path(carpeta, "base_comun.parquet"), ruta_csv)
  ruta <- file.path(carpeta, "muestra.parquet")
  if (!file.exists(ruta) || dir.exists(ruta)) stop("Falta el archivo muestra.parquet")
  muestra <- comparar_muestra_cruce(arrow::read_parquet(ruta, as_data_frame = FALSE))
  list(cartera = resumen, muestra = muestra)
}

escribir_desde_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  funciones <- funciones_cartera_cruce()
  funciones$crear_entrega_r(destino, ruta_csv)
  arrow::write_parquet(construir_muestra_cruce(), file.path(destino, "muestra.parquet"),
    version = "2.6", compression = "snappy")
  # Relectura propia: el paso siguiente sera leer esta carpeta desde Python.
  leer_desde_python(destino, ruta_csv)
}

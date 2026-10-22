# source() define funciones sin leer datos, instalar ni escribir entregas.
funciones_cartera_dataset <- function() {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  e
}

archivos_dataset_r <- function(carpeta) {
  if (!is.character(carpeta) || length(carpeta) != 1L || is.na(carpeta) || !dir.exists(carpeta)) {
    stop("Se requiere la carpeta datos del dataset")
  }
  archivos <- sort(list.files(carpeta, full.names = TRUE, all.files = TRUE, no.. = TRUE))
  if (!length(archivos) || any(dir.exists(archivos)) ||
      any(!grepl("\\.parquet$", archivos, ignore.case = TRUE))) {
    stop("Se exige al menos un Parquet y ninguna otra entrada en datos")
  }
  if (anyDuplicated(normalizePath(archivos, winslash = "/", mustWork = TRUE))) {
    stop("Una misma ruta de archivo aparece repetida")
  }
  archivos
}

abrir_dataset_r <- function(carpeta) {
  archivos <- archivos_dataset_r(carpeta)
  funciones <- funciones_cartera_dataset()
  for (ruta in archivos) {
    esquema <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)$GetSchema()
    if (!esquema$Equals(funciones$esquema_cartera(), check_metadata = FALSE)) {
      stop("Esquema distinto en ", basename(ruta))
    }
  }
  dataset <- arrow::open_dataset(archivos, format = "parquet", unify_schemas = TRUE,
    partitioning = NULL)
  if (!dataset$schema$Equals(funciones$esquema_cartera(), check_metadata = FALSE)) {
    stop("Esquema del dataset distinto")
  }
  dataset
}

verificar_dataset_r <- function(carpeta, ruta_csv = "datos/base_comun_0904.csv") {
  # Auditoria completa de esta muestra pequena, separada de la consulta selectiva.
  funciones <- funciones_cartera_dataset()
  esperada <- funciones$crear_tabla_cartera(funciones$cargar_cartera(ruta_csv))
  observada <- arrow::as_arrow_table(abrir_dataset_r(carpeta))
  funciones$comparar_carteras(esperada, observada)
  funciones$resumir_cartera(observada)
}

escribir_partes_r <- function(tabla, destino, filas_por_archivo = 14L) {
  funciones <- funciones_cartera_dataset()
  x <- funciones$validar_tabla_cartera(tabla)
  if (!is.integer(filas_por_archivo) || length(filas_por_archivo) != 1L ||
      is.na(filas_por_archivo) || filas_por_archivo <= 0L) stop("Indica un entero positivo con L")
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino)) stop("Indica una carpeta NUEVA")
  if (!arrow::codec_is_available("snappy")) stop("Esta instalacion no incluye Snappy")
  if (!dir.create(file.path(destino, "datos"), recursive = TRUE)) stop("No se pudo crear el destino")
  grupos <- split(seq_len(nrow(x)), ceiling(seq_len(nrow(x)) / filas_por_archivo))
  if (!length(grupos)) grupos <- list(integer())
  inventario <- data.frame(archivo = sprintf("parte_%03d.parquet", seq_along(grupos)),
    registros = lengths(grupos))
  for (i in seq_along(grupos)) {
    parte <- funciones$crear_tabla_cartera(x[grupos[[i]], , drop = FALSE])
    arrow::write_parquet(parte, file.path(destino, "datos", inventario$archivo[i]),
      version = "2.6", compression = "snappy")
  }
  funciones$comparar_carteras(tabla, arrow::as_arrow_table(abrir_dataset_r(file.path(destino, "datos"))))
  utils::write.csv(inventario, file.path(destino, "inventario.csv"), row.names = FALSE,
    fileEncoding = "UTF-8")
  inventario
}

crear_dataset_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  funciones <- funciones_cartera_dataset()
  tabla <- funciones$crear_tabla_cartera(funciones$cargar_cartera(ruta_csv))
  escribir_partes_r(tabla, destino)
  verificar_dataset_r(file.path(destino, "datos"), ruta_csv)
}

parametros_consulta_r <- function(corte, minimo) {
  if (!identical(class(corte), "Date") || length(corte) != 1L || is.na(corte) ||
      !is.finite(as.numeric(corte)) || as.numeric(corte) != floor(as.numeric(corte)) ||
      corte < as.Date("1900-01-01") || corte > as.Date("2100-12-31")) {
    stop("corte debe ser Date entre 1900 y 2100, sin fracciones")
  }
  if (!is.integer(minimo) || length(minimo) != 1L || is.na(minimo) || minimo < 0L) {
    stop("minimo debe ser entero no negativo con L dentro de int32")
  }
  invisible(TRUE)
}

preparar_consulta_r <- function(dataset, corte = as.Date("2026-10-31"), minimo = 2000L) {
  parametros_consulta_r(corte, minimo)
  funciones <- funciones_cartera_dataset()
  if (!inherits(dataset, "Dataset") ||
      !dataset$schema$Equals(funciones$esquema_cartera(), check_metadata = FALSE)) {
    stop("Se requiere Dataset con el esquema de cartera")
  }
  # corte/minimo son escalares locales, no columnas. No ejecutar collect() aqui.
  dataset |>
    dplyr::filter(fecha_corte == corte, saldo_mxn >= minimo) |>
    dplyr::select(id_credito, saldo_mxn)
}

referencia_consulta_r <- function(corte, minimo, ruta_csv = "datos/base_comun_0904.csv") {
  parametros_consulta_r(corte, minimo)
  funciones <- funciones_cartera_dataset()
  x <- funciones$cargar_cartera(ruta_csv)
  x <- x[x$fecha_corte == corte & x$saldo_mxn >= minimo, c("id_credito", "saldo_mxn"), drop = FALSE]
  x <- x[order(x$id_credito), , drop = FALSE]
  rownames(x) <- NULL
  x
}

comprobar_consulta_r <- function(resultado, corte = as.Date("2026-10-31"), minimo = 2000L,
    ruta_csv = "datos/base_comun_0904.csv") {
  if (!is.data.frame(resultado) || !identical(names(resultado), c("id_credito", "saldo_mxn")) ||
      !identical(class(resultado$id_credito), "character") ||
      !identical(class(resultado$saldo_mxn), "integer") || anyNA(resultado)) {
    stop("Se exige la proyeccion character/integer sin NA")
  }
  x <- as.data.frame(resultado)
  x <- x[order(x$id_credito), , drop = FALSE]
  rownames(x) <- NULL
  if (!identical(x, referencia_consulta_r(corte, minimo, ruta_csv))) {
    stop("Seleccion distinta del CSV, aunque coincidan sus sumas")
  }
  list(registros = nrow(x), saldo_mxn = sum(as.double(x$saldo_mxn)))
}

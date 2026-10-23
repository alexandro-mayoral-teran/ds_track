# Desde la raiz de DS Track: añade un script y una ruta, sin instalar paquetes.
preparar_practica_metadatos <- function(destino,
    carpeta_metadatos = file.path(getwd(), "output/09_07_metadatos")) {
  valido <- function(x) is.character(x) && length(x) == 1L && !is.na(x) && nzchar(x)
  if (!valido(destino) || !valido(carpeta_metadatos)) stop("Indica rutas como texto unico")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!dir.exists(destino)) stop("El proyecto debe ser una carpeta")
  origen <- "curriculum/09_arrow_parquet/07_metadata_compression/metadatos_parquet.R"
  previo <- "curriculum/09_arrow_parquet/04_r_read_write"
  locales <- c("DESCRIPTION", "renv.lock", "R/intercambio_parquet.R", "R/contrato_0902.R",
    "datos/base_comun_0904.csv")
  originales <- c(file.path(previo, c("DESCRIPTION", "renv.lock", "intercambio_parquet.R")),
    "curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R",
    "curriculum/09_arrow_parquet/01_csv_parquet_arrow/datos/base_comun.csv")
  if (!all(file.exists(c(origen, originales)))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(locales, ".Rprofile", "renv/activate.R"))))) {
    stop("Falta el proyecto preparado de 09.04; no se requieren sus entregas")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, locales))),
                 unname(tools::md5sum(originales)))) stop("Fuentes/metadatos personalizados: revisar sin sobrescribir")
  nuevas <- file.path(destino, c("metadatos_parquet.R", "ruta_metadatos_0907.txt"))
  if (any(file.exists(nuevas))) stop("Script o ruta ocupados: conserva tu preparacion")
  carpeta_metadatos <- normalizePath(carpeta_metadatos, winslash = "/", mustWork = FALSE)
  if (!grepl("^(/|[A-Za-z]:[/\\\\])", carpeta_metadatos)) {
    carpeta_metadatos <- file.path(normalizePath(getwd(), winslash = "/"), carpeta_metadatos)
  }
  if (!file.copy(origen, nuevas[1])) stop("No se pudo copiar el script")
  writeLines(enc2utf8(carpeta_metadatos), nuevas[2], useBytes = TRUE)
  cat("09.07 preparada sin cambiar fuentes, metadatos, biblioteca ni entregas.\n")
  invisible(destino)
}

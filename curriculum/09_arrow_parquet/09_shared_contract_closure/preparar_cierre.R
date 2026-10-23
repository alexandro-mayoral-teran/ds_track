# Desde la raiz de DS Track: añade scripts y una ruta, sin instalar paquetes.
preparar_practica_cierre <- function(destino,
    carpeta_cierre = file.path(getwd(), "output/09_09_cierre")) {
  valido <- function(x) is.character(x) && length(x) == 1L && !is.na(x) && nzchar(x)
  if (!valido(destino) || !valido(carpeta_cierre)) stop("Indica rutas como texto unico")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!dir.exists(destino)) stop("El proyecto debe ser una carpeta")
  origen <- "curriculum/09_arrow_parquet/09_shared_contract_closure/cierre_contrato.R"
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
  auxiliar <- "curriculum/09_arrow_parquet/06_selective_datasets/consultas_dataset.R"
  if (!file.exists(auxiliar)) stop("Falta el modulo de consultas incluido")
  nuevas <- file.path(destino, c("cierre_contrato.R", "ruta_cierre_0909.txt", "R/consultas_cierre_0909.R"))
  if (any(file.exists(nuevas))) stop("Script o ruta ocupados: conserva tu preparacion")
  carpeta_cierre <- normalizePath(carpeta_cierre, winslash = "/", mustWork = FALSE)
  if (!grepl("^(/|[A-Za-z]:[/\\\\])", carpeta_cierre)) {
    carpeta_cierre <- file.path(normalizePath(getwd(), winslash = "/"), carpeta_cierre)
  }
  if (!file.copy(origen, nuevas[1])) stop("No se pudo copiar el script")
  if (!file.copy(auxiliar, nuevas[3])) stop("No se pudo copiar el modulo compartido")
  writeLines(enc2utf8(carpeta_cierre), nuevas[2], useBytes = TRUE)
  cat("09.09 preparada sin cambiar fuentes, metadatos, biblioteca ni entregas.\n")
  invisible(destino)
}

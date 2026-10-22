# Desde la raiz de DS Track; solo copia el script y una ruta local compartida.
preparar_practica_dataset <- function(destino,
    carpeta_dataset = file.path(getwd(), "output/09_06_datasets")) {
  valido <- function(x) is.character(x) && length(x) == 1L && !is.na(x) && nzchar(x)
  if (!valido(destino) || !valido(carpeta_dataset)) stop("Indica rutas como texto unico")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!dir.exists(destino)) stop("El proyecto debe ser una carpeta")
  origen <- "curriculum/09_arrow_parquet/06_selective_datasets/consultas_dataset.R"
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
                 unname(tools::md5sum(originales)))) {
    stop("Fuentes o metadatos personalizados; revisa diferencias sin sobrescribirlos")
  }
  nuevas <- file.path(destino, c("consultas_dataset.R", "ruta_dataset_0906.txt"))
  if (any(file.exists(nuevas))) stop("Script o ruta local ocupados; conserva tu preparacion")
  # Hace absoluta la ruta aunque la carpeta de intercambio todavia no exista.
  carpeta_dataset <- normalizePath(carpeta_dataset, winslash = "/", mustWork = FALSE)
  if (!grepl("^(/|[A-Za-z]:[/\\\\])", carpeta_dataset)) {
    carpeta_dataset <- file.path(normalizePath(getwd(), winslash = "/"), carpeta_dataset)
  }
  if (!file.copy(origen, nuevas[1])) stop("No se pudo copiar el script")
  writeLines(enc2utf8(carpeta_dataset), nuevas[2], useBytes = TRUE)
  cat("09.06 preparada sin cambiar fuentes, metadatos, biblioteca ni entregas.\n")
  cat("La ruta personal solo queda en ruta_dataset_0906.txt dentro de tu copia local.\n")
  invisible(destino)
}

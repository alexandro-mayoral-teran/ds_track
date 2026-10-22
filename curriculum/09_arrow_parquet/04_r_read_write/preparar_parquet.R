# Desde la raiz de DS Track; no instala ni activa renv al hacer source().
preparar_practica_parquet <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica la carpeta de tu proyecto renv existente")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!dir.exists(destino)) stop("El destino debe ser una carpeta")
  base <- "curriculum/09_arrow_parquet/04_r_read_write"
  previo <- "curriculum/08_visualization_r/07_compose_figures"
  origenes <- c(file.path(base, c("DESCRIPTION", "renv.lock", "intercambio_parquet.R",
    "ejecutar_parquet.R")),
    "curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R",
    "curriculum/09_arrow_parquet/02_schemas_types/casos_contrato.csv",
    file.path("curriculum/09_arrow_parquet/01_csv_parquet_arrow/datos",
      c("base_comun.csv", "base_comun.parquet")))
  relativas <- c("DESCRIPTION", "renv.lock", "R/intercambio_parquet.R",
    "ejecutar_parquet.R", "R/contrato_0902.R", "datos/casos_contrato_0904.csv",
    "datos/base_comun_0904.csv", "datos/referencia_python_0904.parquet")
  anteriores <- file.path(previo, c("DESCRIPTION", "renv.lock"))
  if (!all(file.exists(c(origenes, anteriores)))) stop("Ejecuta desde la raiz de DS Track")
  requisitos <- file.path(destino, c(".Rprofile", "renv/activate.R", "restaurar.R",
    "DESCRIPTION", "renv.lock"))
  if (!all(file.exists(requisitos)) || !all(dir.exists(file.path(destino, c("R", "datos"))))) {
    stop("Falta el proyecto renv preparado; revisa 06.08 y la actualizacion de 08.07")
  }
  respaldo <- file.path(destino, "respaldo_08_09")
  if (file.exists(respaldo) || any(file.exists(file.path(destino, relativas[-(1:2)])))) {
    stop("Respaldo o archivos de 09.04 ocupados; conserva y revisa antes de repetir")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, relativas[1:2]))),
                 unname(tools::md5sum(anteriores)))) {
    stop("Metadatos distintos de 08.07-08.09; revisa personalizaciones sin sobrescribirlas")
  }
  if (!dir.create(respaldo)) stop("No se pudo crear el respaldo")
  for (nombre in relativas[1:2]) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) {
      stop("Respaldo parcial; conserva la carpeta y revisa")
    }
  }
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial; conserva el respaldo y revisa antes de repetir")
    }
  }
  cat("09.04 preparada sin instalar. Respaldo de metadatos en respaldo_08_09/.\n")
  cat("Abre el mismo proyecto, reinicia R y ejecuta source(\"restaurar.R\").\n")
  invisible(destino)
}

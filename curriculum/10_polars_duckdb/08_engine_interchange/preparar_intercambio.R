# Desde la raiz de DS Track; sin instalar ni modificar metadatos.
preparar_practica_intercambio <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica el proyecto renv existente")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/10_polars_duckdb/08_engine_interchange"
  previo <- "curriculum/10_polars_duckdb/07_duckdb_python_r"
  nombres <- c("DESCRIPTION", "renv.lock")
  if (!all(file.exists(file.path(destino, c(nombres, ".Rprofile", "R/clientes_1007.R", "R/contrato_0902.R"))))) stop("Falta proyecto 10.07 preparado")
  if (!identical(unname(tools::md5sum(file.path(destino, nombres))),
      unname(tools::md5sum(file.path(previo, nombres))))) stop("Metadatos distintos: revisar sin sobrescribir")
  originales <- file.path(base, c("intercambio.R", "ejecutar_intercambio.R", "muestra.csv"))
  nuevas <- file.path(destino, c("R/intercambio_1008.R", "ejecutar_intercambio.R", "datos/muestra_1008.csv"))
  if (!all(file.exists(originales)) || any(file.exists(nuevas))) stop("Origen ausente o destinos ocupados")
  if (!all(file.copy(originales, nuevas, overwrite = FALSE))) stop("Copia parcial: conservar y revisar")
  cat("10.08 copiada sin instalar ni modificar DESCRIPTION/renv.lock.\n")
  invisible(destino)
}

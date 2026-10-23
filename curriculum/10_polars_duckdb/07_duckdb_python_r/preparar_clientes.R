# Desde la raiz de DS Track; source() solo define esta funcion. No instala.
preparar_practica_clientes <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica el proyecto renv existente")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/10_polars_duckdb/07_duckdb_python_r"
  previo <- "curriculum/09_arrow_parquet/04_r_read_write"
  antiguas <- file.path(previo, c("DESCRIPTION", "renv.lock"))
  archivos <- c("DESCRIPTION", "renv.lock", "clientes.R", "ejecutar_clientes.R",
    "muestra.csv", "seleccion.sql", "resumen.sql")
  origenes <- c(file.path(base, archivos), "curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R")
  relativas <- c("DESCRIPTION", "renv.lock", "R/clientes_1007.R", "ejecutar_clientes.R",
    "datos/muestra_1007.csv", "SQL/seleccion_1007.sql", "SQL/resumen_1007.sql", "R/contrato_0902.R")
  if (!all(file.exists(c(origenes, antiguas)))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", "restaurar.R", "DESCRIPTION", "renv.lock"))))) stop("Falta proyecto renv preparado")
  if (!identical(unname(tools::md5sum(file.path(destino, c("DESCRIPTION", "renv.lock")))),
                 unname(tools::md5sum(antiguas)))) stop("Metadatos personalizados o ya ampliados: revisar sin sobrescribir")
  respaldo <- file.path(destino, "respaldo_09_09")
  if (file.exists(respaldo) || any(file.exists(file.path(destino, relativas[3:7])))) stop("Respaldo o archivos 10.07 ocupados")
  validador <- file.path(destino, relativas[8])
  if (file.exists(validador) && !identical(unname(tools::md5sum(validador)), unname(tools::md5sum(origenes[8])))) stop("Validador personalizado: revisar")
  if (!dir.create(respaldo)) stop("No se pudo crear respaldo")
  for (nombre in c("DESCRIPTION", "renv.lock")) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) stop("Respaldo parcial: conservar y revisar")
  }
  for (carpeta in c("R", "datos", "SQL")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(origenes)) {
    if (i == 8L && file.exists(validador)) next
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = i <= 2L)) stop("Preparacion parcial: conservar respaldo y revisar")
  }
  cat("10.07 preparada sin instalar; respaldo en respaldo_09_09/.\n")
  cat("Abre el mismo proyecto, reinicia R y ejecuta source(\"restaurar.R\").\n")
  invisible(destino)
}

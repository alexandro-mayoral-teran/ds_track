# Desde la raiz de DS Track; source() solo define, no instala ni activa renv.
preparar_ejecucion <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/03_execution_python_r"
  previo <- "curriculum/10_polars_duckdb/07_duckdb_python_r"
  nombres <- c("DESCRIPTION", "renv.lock", "analisis.R", "cartera.csv", "reporte_r.qmd", "ejecucion_1103.Rproj")
  relativas <- c("DESCRIPTION", "renv.lock", "R/analisis_1103.R",
                 "datos/cartera_1103.csv", "reporte_1103.qmd", "ejecucion_1103.Rproj")
  origenes <- file.path(base, nombres)
  if (!all(file.exists(c(origenes, file.path(previo, nombres[1:2]))))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", "restaurar.R", nombres[1:2]))))) {
    stop("Falta el proyecto renv preparado")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, nombres[1:2]))),
                 unname(tools::md5sum(file.path(previo, nombres[1:2]))))) {
    stop("Metadatos personalizados o ya ampliados: revisar sin sobrescribir")
  }
  respaldo <- file.path(destino, "respaldo_10_07")
  if (file.exists(respaldo) || any(file.exists(file.path(destino, relativas[3:6])))) {
    stop("Respaldo o archivos 11.03 ocupados")
  }
  if (!dir.create(respaldo)) stop("No se pudo crear respaldo")
  for (n in nombres[1:2]) {
    if (!file.copy(file.path(destino, n), file.path(respaldo, n))) stop("Respaldo parcial: conservar y revisar")
  }
  for (carpeta in c("R", "datos")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial: conservar respaldo y revisar")
    }
  }
  cat("11.03 preparada; abre el mismo proyecto, reinicia R y ejecuta source('restaurar.R').\n")
  invisible(destino)
}

# Alternativa sin entregas previas: proyecto nuevo con la misma configuración renv.
crear_entorno_ejecucion <- function(destino) {
  base <- "curriculum/11_reporting_quarto/03_execution_python_r"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  origenes <- c(file.path(plantilla, c(".Rprofile", "restaurar.R", "renv/activate.R", "renv/settings.json")),
               file.path(base, c("DESCRIPTION", "renv.lock", "analisis.R", "cartera.csv", "reporte_r.qmd", "ejecucion_1103.Rproj")))
  relativas <- c(".Rprofile", "restaurar.R", "renv/activate.R", "renv/settings.json",
                 "DESCRIPTION", "renv.lock", "R/analisis_1103.R", "datos/cartera_1103.csv", "reporte_1103.qmd", "ejecucion_1103.Rproj")
  if (!all(file.exists(origenes))) stop("Ejecuta desde la raiz de DS Track")
  if (file.exists(destino)) stop("El destino ya existe: conservar y elegir otro")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  for (carpeta in c("renv", "R", "datos")) dir.create(file.path(destino, carpeta))
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]))) {
      stop("Copia parcial: conservar y revisar")
    }
  }
  cat("Proyecto nuevo preparado sin instalar; abre su carpeta y ejecuta source('restaurar.R').\n")
  invisible(destino)
}

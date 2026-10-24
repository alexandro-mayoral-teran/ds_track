# Desde la raiz de DS Track. Carga funciones sin instalar ni activar renv.
preparar_evidencia <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/04_tables_figures_references"
  previo <- "curriculum/11_reporting_quarto/03_execution_python_r"
  origenes <- c(file.path(base, c("cartera.csv", "reporte_r.qmd", "referencias.bib")),
               file.path(previo, "analisis.R"))
  relativas <- c("datos/cartera_1104.csv", "reporte_1104.qmd", "referencias_1104.bib", "R/analisis_1104.R")
  if (!all(file.exists(origenes))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", "DESCRIPTION", "renv.lock"))))) {
    stop("Falta el proyecto renv preparado")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, c("DESCRIPTION", "renv.lock")))),
                 unname(tools::md5sum(file.path(previo, c("DESCRIPTION", "renv.lock")))))) {
    stop("Metadatos distintos de 11.03: revisar sin sobrescribir")
  }
  if (any(file.exists(file.path(destino, relativas)))) stop("Archivos de 11.04 ocupados")
  for (carpeta in c("R", "datos")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]))) stop("Copia parcial: conservar y revisar")
  }
  cat("11.04 preparada sin cambiar metadatos ni instalar paquetes.\n")
  invisible(destino)
}

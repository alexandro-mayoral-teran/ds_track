# Desde la raiz de DS Track; solo copia fuentes, sin instalar ni renderizar.
preparar_proyecto_quarto <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/06_projects_cache_freeze"
  previo <- "curriculum/11_reporting_quarto/03_execution_python_r"
  fuentes <- c(file.path(base, c("_quarto.yml", "cartera.csv", "reporte_r.qmd", "octubre.yml")),
               "curriculum/11_reporting_quarto/05_parameters_cutoffs/analisis.R")
  relativas <- c("_quarto.yml", "datos/cartera_1106.csv", "informes/reporte_1106.qmd",
                 "octubre_1106.yml", "R/analisis_1106.R")
  if (!all(file.exists(fuentes))) stop("Ejecuta desde la raiz de DS Track")
  metadatos <- c("DESCRIPTION", "renv.lock")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", metadatos))))) {
    stop("Falta proyecto renv preparado")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, metadatos))),
                 unname(tools::md5sum(file.path(previo, metadatos))))) {
    stop("Metadatos personalizados: revisar sin sobrescribir")
  }
  if (any(file.exists(file.path(destino, relativas)))) stop("Configuracion o archivos de 11.06 ocupados")
  for (carpeta in c("datos", "informes", "R")) {
    dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  }
  for (i in seq_along(fuentes)) {
    if (!file.copy(fuentes[i], file.path(destino, relativas[i]))) stop("Copia parcial: conservar y revisar")
  }
  cat("Proyecto Quarto preparado; fuentes y metadatos previos conservados.\n")
  invisible(destino)
}

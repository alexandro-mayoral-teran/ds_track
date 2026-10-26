# Desde la raiz de DS Track: agrega 11.07 sin cambiar metadatos ni configuracion Quarto.
preparar_revision <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/07_formats_visual_review"
  previo <- "curriculum/11_reporting_quarto/03_execution_python_r"
  fuentes <- c(file.path(base, c("cartera.csv", "reporte_r.qmd", "estilos.css", "minimo.qmd")),
               file.path(previo, "analisis.R"))
  relativas <- c("datos/cartera_1107.csv", "reporte_1107.qmd", "estilos_1107.css",
                 "minimo_1107.qmd", "R/analisis_1107.R")
  metadatos <- c("DESCRIPTION", "renv.lock")
  if (!all(file.exists(fuentes))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", metadatos))))) {
    stop("Falta el proyecto renv preparado")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, metadatos))),
                 unname(tools::md5sum(file.path(previo, metadatos))))) {
    stop("Metadatos personalizados: revisar sin sobrescribir")
  }
  if (any(file.exists(file.path(destino, relativas)))) stop("Archivos de 11.07 ocupados")
  for (carpeta in c("R", "datos")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(fuentes)) {
    if (!file.copy(fuentes[i], file.path(destino, relativas[i]))) stop("Copia parcial: conservar y revisar")
  }
  cat("11.07 preparada sin instalar ni modificar configuracion o metadatos previos.\n")
  invisible(destino)
}

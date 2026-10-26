# Desde la raiz de DS Track; conserva configuracion, bibliotecas y fuentes previas.
preparar_dashboard <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/08_dashboard_distribution"
  previo <- "curriculum/11_reporting_quarto/03_execution_python_r"
  fuentes <- c(file.path(base, c("cartera.csv", "dashboard_r.qmd", "estilos.css", "minimo.qmd")),
               file.path(previo, "analisis.R"))
  relativas <- c("datos/cartera_1108.csv", "dashboard_1108.qmd", "estilos_1108.css",
                 "minimo_1108.qmd", "R/analisis_1108.R")
  metadatos <- c("DESCRIPTION", "renv.lock")
  if (!all(file.exists(fuentes))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", metadatos))))) {
    stop("Falta proyecto renv preparado")
  }
  if (!identical(unname(tools::md5sum(file.path(destino, metadatos))),
                 unname(tools::md5sum(file.path(previo, metadatos))))) {
    stop("Metadatos personalizados: revisar sin sobrescribir")
  }
  if (any(file.exists(file.path(destino, relativas)))) stop("Archivos de 11.08 ocupados")
  for (carpeta in c("R", "datos")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(fuentes)) {
    if (!file.copy(fuentes[i], file.path(destino, relativas[i]))) stop("Copia parcial: conservar y revisar")
  }
  cat("11.08 preparada sin instalar ni cambiar metadatos.\n")
  invisible(destino)
}

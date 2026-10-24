# Desde la raiz de DS Track; no instala ni modifica metadatos renv.
preparar_parametros <- function(destino) {
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/11_reporting_quarto/05_parameters_cutoffs"
  previo <- "curriculum/11_reporting_quarto/03_execution_python_r"
  nombres <- c("cartera.csv", "analisis.R", "reporte_r.qmd", "septiembre.yml", "octubre.yml")
  relativas <- c("datos/cartera_1105.csv", "R/analisis_1105.R", "reporte_1105.qmd", "septiembre_1105.yml", "octubre_1105.yml")
  if (!all(file.exists(file.path(base, nombres)))) stop("Ejecuta desde la raiz de DS Track")
  if (!all(file.exists(file.path(destino, c(".Rprofile", "renv/activate.R", "DESCRIPTION", "renv.lock"))))) stop("Falta proyecto renv preparado")
  if (!identical(unname(tools::md5sum(file.path(destino, c("DESCRIPTION", "renv.lock")))),
                 unname(tools::md5sum(file.path(previo, c("DESCRIPTION", "renv.lock")))))) stop("Metadatos personalizados: revisar sin sobrescribir")
  if (any(file.exists(file.path(destino, relativas)))) stop("Archivos de 11.05 ocupados")
  for (carpeta in c("R", "datos")) dir.create(file.path(destino, carpeta), showWarnings = FALSE)
  for (i in seq_along(nombres)) {
    if (!file.copy(file.path(base, nombres[i]), file.path(destino, relativas[i]))) stop("Copia parcial: conservar y revisar")
  }
  cat("11.05 preparada sin modificar metadatos ni instalar paquetes.\n")
  invisible(destino)
}

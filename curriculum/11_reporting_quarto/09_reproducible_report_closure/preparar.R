# Ejecutar source() desde la raiz del curso; crea solo fuentes y metadatos locales.
preparar_cierre <- function(destino) {
  base <- "curriculum/11_reporting_quarto/09_reproducible_report_closure"
  entorno <- "curriculum/11_reporting_quarto/03_execution_python_r"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  comunes <- c("_quarto.yml", "cartera.csv", "parametros.json", "estilos.css", "verificar.py", "copiar_fuentes.py", "construir.R")
  fuentes <- c(file.path(base, comunes), file.path(base, c("reporte_r.qmd", "LEEME_fuentes.md")),
               "curriculum/11_reporting_quarto/05_parameters_cutoffs/analisis.R",
               file.path(plantilla, c(".Rprofile", "restaurar.R", "renv/activate.R", "renv/settings.json")),
               file.path(entorno, c("DESCRIPTION", "renv.lock", "ejecucion_1103.Rproj")))
  relativas <- c(comunes, "reporte.qmd", "README.md", "analisis.R", ".Rprofile", "restaurar.R",
                 "renv/activate.R", "renv/settings.json", "DESCRIPTION", "renv.lock", "cierre.Rproj")
  if (!all(file.exists(fuentes))) stop("Ejecuta desde la raiz de DS Track")
  if (file.exists(destino)) stop("Destino ocupado: conservar y elegir otro")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear destino")
  dir.create(file.path(destino, "renv"))
  for (i in seq_along(fuentes)) {
    if (!file.copy(fuentes[i], file.path(destino, relativas[i]))) stop("Copia parcial: conservar e investigar")
  }
  cat("Copia R nueva preparada. Abrir cierre.Rproj y restaurar biblioteca local.\n")
  invisible(destino)
}

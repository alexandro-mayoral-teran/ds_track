# Desde la raiz del repositorio. source() solo define la funcion; no instala.
preparar_primera_app <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una carpeta nueva para la practica.")
  }
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- "curriculum/13_shiny_web/01_web_first_app"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  propios <- c("app.R", "minimo.R", "DESCRIPTION", "renv.lock", "shiny_1301.Rproj",
               "restaurar.R", "iniciar.R", "comprobar_app.R")
  compartidos <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(base, propios), file.path(plantilla, compartidos))
  relativas <- c(propios, compartidos)
  if (!all(file.exists(origenes))) stop("Faltan fuentes; ejecuta desde la raiz de DS Track.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino.")
  if (!dir.create(file.path(destino, "renv"))) stop("Copia parcial: conservar y revisar.")
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
      stop("Copia parcial: conservarla y revisar el mensaje.")
    }
  }
  cat("Proyecto preparado sin instalar. Abre shiny_1301.Rproj y lee los recorridos de 13.01.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

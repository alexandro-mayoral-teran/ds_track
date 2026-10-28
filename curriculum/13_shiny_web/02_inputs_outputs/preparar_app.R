# Desde la raiz del repo; source() solo define, no instala ni inicia la app.
preparar_entradas_salidas <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una carpeta nueva para la practica.")
  }
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- "curriculum/13_shiny_web/02_inputs_outputs"
  anterior <- "curriculum/13_shiny_web/01_web_first_app"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  propios <- c("app.R", "minimo.R", "ventas.R", "comprobar_app.R")
  reutilizados <- c("DESCRIPTION", "renv.lock", "shiny_1301.Rproj", "restaurar.R", "iniciar.R")
  configuracion <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(base, propios), file.path(anterior, reutilizados), file.path(plantilla, configuracion))
  relativas <- c(propios, "DESCRIPTION", "renv.lock", "shiny_1302.Rproj", "restaurar.R", "iniciar.R", configuracion)
  if (!all(file.exists(origenes))) stop("Faltan fuentes; ejecuta desde la raiz de DS Track.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino.")
  if (!dir.create(file.path(destino, "renv"))) stop("Copia parcial: conservar y revisar.")
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
      stop("Copia parcial: conservarla y revisar el mensaje.")
    }
  }
  cat("13.02 preparada sin instalar; abre shiny_1302.Rproj y sigue los recorridos.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

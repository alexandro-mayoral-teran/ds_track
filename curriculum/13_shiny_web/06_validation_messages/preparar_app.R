# Desde la raiz del repo; source solo define la funcion.
preparar_validacion_mensajes <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica una carpeta nueva.")
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- "curriculum/13_shiny_web/06_validation_messages"
  anterior <- "curriculum/13_shiny_web/01_web_first_app"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  propios <- c("app.R", "minimo.R", "validacion.R", "comprobar_app.R")
  metadatos <- c("DESCRIPTION", "renv.lock", "shiny_1301.Rproj", "restaurar.R", "iniciar.R")
  configuracion <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(base, propios), "curriculum/13_shiny_web/04_shared_filters/cartera.R",
    "curriculum/13_shiny_web/05_events_session/consulta.R", "curriculum/12_streamlit/03_data_interface/cartera.csv",
    file.path(anterior, metadatos), file.path(plantilla, configuracion))
  relativas <- c(propios, "cartera.R", "consulta.R", "cartera.csv", "DESCRIPTION", "renv.lock", "shiny_1306.Rproj", "restaurar.R", "iniciar.R", configuracion)
  if (!all(file.exists(origenes))) stop("Faltan fuentes; ejecuta desde la raiz del repo.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear la copia.")
  if (!dir.create(file.path(destino, "renv"))) stop("Copia parcial: conservar y revisar.")
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) stop("Copia parcial: conservar y revisar.")
  }
  cat("13.06 preparada sin instalar; abre shiny_1306.Rproj y sigue recorridos.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

# Ejecutar desde la raiz del repo. Solo copia; no instala ni inicia.
preparar_pruebas_flujo <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica una carpeta nueva.")
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- "curriculum/13_shiny_web/09_tests_flow"
  modulos <- "curriculum/13_shiny_web/08_organization_modules"
  primera <- "curriculum/13_shiny_web/01_web_first_app"
  salidas <- "curriculum/13_shiny_web/07_outputs_downloads"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  propios <- c("minimo.R", "pruebas_minimo.R", "pruebas_funciones.R", "pruebas_servidor.R", "ejecutar_pruebas.R")
  reutilizados <- c("curriculum/13_shiny_web/04_shared_filters/cartera.R", "curriculum/13_shiny_web/05_events_session/consulta.R",
    "curriculum/13_shiny_web/06_validation_messages/validacion.R", file.path(salidas, "presentacion.R"),
    "curriculum/12_streamlit/03_data_interface/cartera.csv", file.path(salidas, c("DESCRIPTION", "renv.lock")))
  configuracion <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(base, propios), file.path(modulos, c("app.R", "consulta_module.R")), reutilizados,
    file.path(primera, c("shiny_1301.Rproj", "restaurar.R", "iniciar.R")), file.path(plantilla, configuracion))
  relativas <- c(propios, "app.R", "consulta_module.R", "cartera.R", "consulta.R", "validacion.R", "presentacion.R", "cartera.csv", "DESCRIPTION", "renv.lock",
    "shiny_1309.Rproj", "restaurar.R", "iniciar.R", configuracion)
  if (!all(file.exists(origenes))) stop("Faltan fuentes; ejecuta desde la raiz del repo.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear la copia.")
  if (!dir.create(file.path(destino, "renv"))) stop("Copia parcial: conservar y revisar.")
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) stop("Copia parcial: conservar y revisar.")
  }
  cat("13.09 preparada: veinte archivos, sin instalar. Sigue recorridos.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

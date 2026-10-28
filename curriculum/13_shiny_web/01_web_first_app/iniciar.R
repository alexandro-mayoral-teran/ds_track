# source() define la funcion; iniciar_app() mantiene R ocupado hasta detenerla.
iniciar_app <- function(archivo = "app.R", puerto = NULL, abrir = interactive()) {
  if (!is.character(archivo) || length(archivo) != 1L || is.na(archivo) ||
      !archivo %in% c("minimo.R", "app.R")) stop("Elige minimo.R o app.R.")
  if (!all(file.exists(c(".Rprofile", "renv/activate.R", archivo)))) {
    stop("Abre primero la carpeta preparada; no ejecutes la fuente aislada del curso.")
  }
  source(".Rprofile")
  shiny::runApp(appDir = archivo, host = "127.0.0.1", port = puerto, launch.browser = abrir)
}

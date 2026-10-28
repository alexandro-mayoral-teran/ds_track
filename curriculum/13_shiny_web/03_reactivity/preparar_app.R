# Ejecutar desde la raiz del repo. Solo define la funcion; no restaura ni arranca.
preparar_reactividad <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una carpeta nueva para la practica.")
  }
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- "curriculum/13_shiny_web/03_reactivity"
  anterior <- "curriculum/13_shiny_web/01_web_first_app"
  plantilla <- "curriculum/06_r_foundations/08_projects_renv/plantilla"
  propios <- c("app.R", "minimo.R", "comprobar_app.R")
  reutilizados <- c("DESCRIPTION", "renv.lock", "shiny_1301.Rproj", "restaurar.R", "iniciar.R")
  configuracion <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(base, propios), "curriculum/13_shiny_web/02_inputs_outputs/ventas.R",
               file.path(anterior, reutilizados), file.path(plantilla, configuracion))
  relativas <- c(propios, "ventas.R", "DESCRIPTION", "renv.lock", "shiny_1303.Rproj",
                 "restaurar.R", "iniciar.R", configuracion)
  if (!all(file.exists(origenes))) stop("Faltan fuentes; ejecuta desde la raiz de DS Track.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino.")
  if (!dir.create(file.path(destino, "renv"))) stop("Copia parcial: conservar y revisar.")
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
      stop("Copia parcial: conservarla y revisar el mensaje.")
    }
  }
  cat("13.03 preparada sin instalar; abre shiny_1303.Rproj y sigue recorridos.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

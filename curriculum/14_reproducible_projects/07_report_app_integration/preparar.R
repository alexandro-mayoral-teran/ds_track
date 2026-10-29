# Dos preparadores equivalentes si se elige la misma app; ninguno instala.
preparar_integracion <- function(destino, repo = ".", app = "shiny") {
  if (!is.character(app) || length(app) != 1L || is.na(app) || !app %in% c("streamlit", "shiny")) stop("Elegir una app.")
  base <- file.path(repo, "curriculum/14_reproducible_projects/07_report_app_integration")
  e <- new.env(parent = globalenv())
  source(file.path(repo, "curriculum/14_reproducible_projects/06_traceability_recovery/preparar.R"), local = e, encoding = "UTF-8")
  e$preparar_trazabilidad(destino, repo)
  for (p in c("pipeline.py", "pipeline.R", "LEEME.md")) {
    if (!file.copy(file.path(base, "plantilla", p), file.path(destino, p), overwrite = TRUE)) stop("Copia parcial.")
  }
  nuevas <- c("integracion.py", "integracion.R", ".renvignore", "interfaz/python/app.py", "interfaz/python/pyproject.toml", "interfaz/python/uv.lock", "interfaz/python/.python-version", "interfaz/r/app.R")
  copiar <- function(origen, relativa) {
    final <- file.path(destino, relativa)
    if (!dir.exists(dirname(final))) dir.create(dirname(final), recursive = TRUE)
    if (!file.copy(origen, final, overwrite = FALSE)) stop("Copia parcial: conservar.")
  }
  for (p in nuevas) copiar(file.path(base, "plantilla", p), p)
  shiny <- file.path(repo, "curriculum/13_shiny_web/01_web_first_app")
  for (p in c("DESCRIPTION", "renv.lock", "restaurar.R", "iniciar.R")) copiar(file.path(shiny, p), paste0("interfaz/r/", p))
  renv <- file.path(repo, "curriculum/06_r_foundations/08_projects_renv/plantilla")
  for (p in c(".Rprofile", "renv/activate.R", "renv/settings.json")) copiar(file.path(renv, p), paste0("interfaz/r/", p))
  copiar(file.path(shiny, "shiny_1301.Rproj"), "interfaz/r/interfaz_1407.Rproj")
  if (!file.rename(file.path(destino, "producto_1406.Rproj"), file.path(destino, "producto_1407.Rproj"))) stop("No se pudo nombrar proyecto.")
  original <- utils::read.csv(file.path(destino, "config/consulta.csv"), colClasses = "character")
  casos <- list(octubre = list(), septiembre = list(corte = "2026-09-30"), vacio = list(segmentos = "servicios", minimo_texto = "1901"), sinuniverso = list(corte = "2026-11-30"))
  for (nombre in names(casos)) {
    cfg <- original
    cambios <- c(list(app = app, salida = paste0("salidas/", nombre, "_integrado")), casos[[nombre]])
    for (k in names(cambios)) cfg$valor[cfg$clave == k] <- cambios[[k]]
    final <- file.path(destino, "config", paste0(nombre, ".csv"))
    if (file.exists(final)) stop("Configuracion ocupada.")
    con <- file(final, "wb")
    tryCatch(write.table(cfg, con, sep = ",", quote = FALSE, row.names = FALSE, eol = "\n"), finally = close(con))
  }
  cat("53 fuentes; lee LEEME.md. Ruta elegida:", app, "\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

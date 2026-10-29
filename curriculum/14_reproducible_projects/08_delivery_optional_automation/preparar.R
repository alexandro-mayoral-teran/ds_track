# Crea otra copia; no restaura entornos ni inicia aplicaciones.
preparar_entrega <- function(destino, repo = ".", app = "shiny") {
  e <- new.env(parent = globalenv())
  source(file.path(repo, "curriculum/14_reproducible_projects/07_report_app_integration/preparar.R"), local = e, encoding = "UTF-8")
  e$preparar_integracion(destino, repo, app)
  base <- file.path(repo, "curriculum/14_reproducible_projects/08_delivery_optional_automation/plantilla")
  for (p in c("pipeline.py", "pipeline.R", "LEEME.md")) {
    if (!file.copy(file.path(base, p), file.path(destino, p), overwrite = TRUE)) stop("Copia parcial: conservar.")
  }
  for (p in c("entrega.py", "entrega.R", "reconstruir.py", "reconstruir.R", "catalogo.csv", "CI_EJEMPLO.yml", "LEEME_ENTREGA.md")) {
    if (!file.copy(file.path(base, p), file.path(destino, p), overwrite = FALSE)) stop("Copia parcial: conservar.")
  }
  if (!file.rename(file.path(destino, "producto_1407.Rproj"), file.path(destino, "producto_1408.Rproj"))) stop("No se pudo nombrar proyecto.")
  cat("60 fuentes; lee LEEME.md. No se instalaron paquetes ni se habilito CI.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

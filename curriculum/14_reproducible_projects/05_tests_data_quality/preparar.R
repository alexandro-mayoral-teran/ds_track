# Copia nueva de las fuentes 14.04 y pruebas, sin instalar paquetes.
preparar_pruebas <- function(destino, repo = ".") {
  base <- file.path(repo, "curriculum/14_reproducible_projects/05_tests_data_quality")
  e <- new.env(parent = globalenv())
  source(file.path(repo, "curriculum/14_reproducible_projects/04_pipeline_reprocessing/preparar.R"), local = e, encoding = "UTF-8")
  e$preparar_pipeline(destino, repo)
  for (p in c("pruebas.py", "pruebas.R", "referencia/calidad.csv")) {
    if (!file.copy(file.path(base, "plantilla", p), file.path(destino, p), overwrite = FALSE)) stop("Copia parcial: revisar.")
  }
  if (!file.copy(file.path(base, "plantilla/LEEME.md"), file.path(destino, "LEEME.md"), overwrite = TRUE)) stop("Copia parcial: revisar.")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  stopifnot(normalizePath(file.path(destino, "producto_1404.Rproj"), winslash = "/", mustWork = TRUE) == paste0(destino, "/producto_1404.Rproj"))
  if (!file.rename(file.path(destino, "producto_1404.Rproj"), file.path(destino, "producto_1405.Rproj"))) stop("No se pudo nombrar proyecto nuevo.")
  cat("31 fuentes finales; lee LEEME.md.\n")
  invisible(destino)
}

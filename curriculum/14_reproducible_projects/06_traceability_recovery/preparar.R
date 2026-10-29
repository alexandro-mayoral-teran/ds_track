# Ejecutar desde la raiz del repositorio; no restaura ni instala.
preparar_trazabilidad <- function(destino, repo = ".") {
  base <- file.path(repo, "curriculum/14_reproducible_projects/06_traceability_recovery")
  e <- new.env(parent = globalenv())
  source(file.path(repo, "curriculum/14_reproducible_projects/05_tests_data_quality/preparar.R"), local = e, encoding = "UTF-8")
  e$preparar_pruebas(destino, repo)
  for (p in c("trazar.py", "trazar.R")) {
    if (!file.copy(file.path(base, "plantilla", p), file.path(destino, p), overwrite = FALSE)) stop("Copia parcial: revisar.")
  }
  if (!file.copy(file.path(base, "plantilla/LEEME.md"), file.path(destino, "LEEME.md"), overwrite = TRUE)) stop("Copia parcial: revisar.")
  if (!file.rename(file.path(destino, "producto_1405.Rproj"), file.path(destino, "producto_1406.Rproj"))) stop("No se pudo nombrar proyecto nuevo.")
  cat("33 fuentes finales; lee LEEME.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

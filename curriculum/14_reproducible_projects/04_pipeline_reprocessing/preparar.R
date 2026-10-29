# Preparar desde consola R con raiz del repositorio explicita.
preparar_pipeline <- function(destino, repo = ".") {
  base <- file.path(repo, "curriculum/14_reproducible_projects/04_pipeline_reprocessing")
  e <- new.env(parent = globalenv())
  source(file.path(repo, "curriculum/14_reproducible_projects/03_reconstructible_environments/preparar.R"), local = e, encoding = "UTF-8")
  e$preparar_entornos(destino, repo)
  # La copia recien creada contiene fuentes anteriores; se adaptan solo estas seis.
  propias <- c("LEEME.md", "ejecutar.py", "ejecutar.R", "codigo/configuracion.py", "codigo/configuracion.R", "salidas/LEEME.md")
  for (p in propias) if (!file.copy(file.path(base, "plantilla", p), file.path(destino, p), overwrite = TRUE)) stop("Copia parcial: revisar.")
  for (p in c("pipeline.py", "pipeline.R")) if (!file.copy(file.path(base, "plantilla", p), file.path(destino, p), overwrite = FALSE)) stop("Copia parcial: revisar.")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  stopifnot(normalizePath(file.path(destino, "producto_1403.Rproj"), winslash = "/", mustWork = TRUE) == paste0(destino, "/producto_1403.Rproj"))
  if (!file.rename(file.path(destino, "producto_1403.Rproj"), file.path(destino, "producto_1404.Rproj"))) stop("No se pudo nombrar el proyecto nuevo.")
  cat("28 fuentes finales, sin instalar paquetes; lee LEEME.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

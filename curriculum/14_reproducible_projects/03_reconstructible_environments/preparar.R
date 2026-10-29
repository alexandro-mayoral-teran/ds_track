# Solo define y copia; desde raiz del repo o con repo explicito.
preparar_entornos <- function(destino, repo = ".") {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica carpeta nueva.")
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- file.path(repo, "curriculum/14_reproducible_projects/03_reconstructible_environments")
  previa <- file.path(repo, "curriculum/14_reproducible_projects/02_structure_configuration/plantilla")
  contrato <- file.path(repo, "curriculum/14_reproducible_projects/01_product_question_contract")
  plantilla <- file.path(repo, "curriculum/06_r_foundations/08_projects_renv/plantilla")
  anteriores <- c("revisar.py", "revisar.R", "config/consulta.csv", "codigo/modelo.py", "codigo/modelo.R", "codigo/configuracion.py", "codigo/configuracion.R", "salidas/LEEME.md")
  propios <- c("LEEME.md", "ejecutar.py", "ejecutar.R", "entorno.csv")
  python <- c("pyproject.toml", "uv.lock", ".python-version"); r <- c("DESCRIPTION", "renv.lock", "restaurar.R")
  perfiles <- c(".Rprofile", "renv/activate.R", "renv/settings.json")
  origenes <- c(file.path(previa, anteriores), file.path(contrato, c("ESPECIFICACION.md", "plantilla_contrato.md", "cartera.csv", "criterios.csv")), file.path(base, propios),
    file.path(base, "entorno_python", python), file.path(base, "entorno_r", r), file.path(plantilla, perfiles), file.path(repo,"curriculum/13_shiny_web/01_web_first_app/shiny_1301.Rproj"))
  relativas <- c(anteriores, "docs/ESPECIFICACION.md", "docs/plantilla_contrato.md", "datos/entrada/cartera.csv", "referencia/criterios.csv", propios, python, r, perfiles, "producto_1403.Rproj")
  if (length(origenes) != 26L || !all(file.exists(origenes))) stop("Faltan fuentes del curso.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear carpeta.")
  for (i in seq_along(origenes)) {
    final <- file.path(destino, relativas[i]); padre <- dirname(final)
    if (!dir.exists(padre) && !dir.create(padre, recursive = TRUE)) stop("Copia parcial: conservar y revisar.")
    if (!file.copy(origenes[i], final, overwrite = FALSE)) stop("Copia parcial: conservar y revisar.")
  }
  cat("26 fuentes copiadas, sin instalar; lee LEEME.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

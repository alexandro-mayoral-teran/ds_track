# Desde la raiz del repo o con repo explicito; solo define y copia archivos.
preparar_estructura <- function(destino, repo = ".") {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica un destino nuevo.")
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  base <- file.path(repo, "curriculum/14_reproducible_projects/02_structure_configuration/plantilla")
  previa <- file.path(repo, "curriculum/14_reproducible_projects/01_product_question_contract")
  propios <- c("LEEME.md", "revisar.py", "revisar.R", "config/consulta.csv", "codigo/modelo.py", "codigo/modelo.R", "codigo/configuracion.py", "codigo/configuracion.R", "salidas/LEEME.md")
  anteriores <- c("ESPECIFICACION.md", "plantilla_contrato.md", "cartera.csv", "criterios.csv")
  relativas <- c(propios, "docs/ESPECIFICACION.md", "docs/plantilla_contrato.md", "datos/entrada/cartera.csv", "referencia/criterios.csv")
  origenes <- c(file.path(base, propios), file.path(previa, anteriores))
  if (!all(file.exists(origenes))) stop("Faltan fuentes; revisa la raiz del repo.")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear carpeta.")
  for (i in seq_along(origenes)) {
    padre <- dirname(file.path(destino, relativas[i]))
    if (!dir.exists(padre) && !dir.create(padre, recursive = TRUE)) stop("Copia parcial: conservar y revisar.")
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) stop("Copia parcial: conservar y revisar.")
  }
  cat("13 archivos copiados, sin instalar; lee LEEME.md.\n")
  invisible(normalizePath(destino, winslash = "/", mustWork = TRUE))
}

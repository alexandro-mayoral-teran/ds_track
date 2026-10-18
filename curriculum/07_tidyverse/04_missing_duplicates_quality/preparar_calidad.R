# Desde la raiz de DS Track: source() solo define la funcion.
preparar_calidad <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/07_tidyverse/04_missing_duplicates_quality"
  requisitos <- file.path(destino, c(".Rprofile", "renv.lock", "DESCRIPTION",
                                    "transformar_cartera.R", "R/funciones_transformacion.R",
                                    "datos/cartera_conversion.csv"))
  if (!all(file.exists(requisitos))) { stop("Completa la preparacion de 07.03 primero.") }
  origenes <- c(file.path(base, c("funciones_calidad.R", "revisar_calidad.R")),
                "curriculum/02_pandas/05_missing_duplicates_rules/cartera_calidad.csv")
  relativas <- c("R/funciones_calidad.R", "revisar_calidad.R", "datos/cartera_calidad.csv")
  if (!all(file.exists(origenes))) { stop("Ejecuta desde la raiz de DS Track; faltan fuentes.") }
  if (any(file.exists(file.path(destino, relativas)))) {
    stop("Ya hay archivos en el destino; conserva tu trabajo y revisa.")
  }
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
      stop("Copia parcial; conserva la carpeta y revisa antes de repetir.")
    }
  }
  cat("07.04 preparada; sin cambios en metadatos ni paquetes.\n")
  invisible(destino)
}

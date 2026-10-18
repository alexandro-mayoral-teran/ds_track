# Desde la raiz de DS Track: source() solo define la funcion.
preparar_transformacion <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/07_tidyverse/03_transform_columns"
  requisitos <- file.path(destino, c(".Rprofile", "renv.lock", "DESCRIPTION",
                                    "seleccionar_cartera.R", "R/funciones_importacion.R",
                                    "datos/cartera_demo.csv"))
  if (!all(file.exists(requisitos))) { stop("Completa la preparacion de 07.02 primero.") }
  origenes <- c(file.path(base, c("funciones_transformacion.R", "transformar_cartera.R")),
                "curriculum/02_pandas/04_types_calculated_columns/cartera_conversion.csv")
  relativas <- c("R/funciones_transformacion.R", "transformar_cartera.R",
                 "datos/cartera_conversion.csv")
  if (!all(file.exists(origenes))) { stop("Ejecuta desde la raiz de DS Track; faltan fuentes.") }
  if (any(file.exists(file.path(destino, relativas)))) {
    stop("Ya hay archivos en el destino; conserva tu trabajo y revisa.")
  }
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
      stop("Copia parcial; conserva la carpeta y revisa antes de repetir.")
    }
  }
  cat("07.03 preparada; sin cambios en DESCRIPTION, renv.lock o paquetes.\n")
  invisible(destino)
}

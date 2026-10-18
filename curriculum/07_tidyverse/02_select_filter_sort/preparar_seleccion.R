# Desde la raiz de DS Track: source() solo define esta funcion.
preparar_seleccion <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/07_tidyverse/02_select_filter_sort"
  requisitos <- file.path(destino, c(".Rprofile", "renv.lock", "DESCRIPTION",
                                    "renv/activate.R", "R/funciones_importacion.R",
                                    "importar_cartera.R", "datos/cartera_demo.csv"))
  if (!all(file.exists(requisitos))) { stop("Completa la preparacion de 07.01 primero.") }
  nombres <- c("DESCRIPTION", "renv.lock", "seleccionar_cartera.R")
  origenes <- file.path(base, nombres)
  respaldo <- file.path(destino, "respaldo_07_01")
  if (!all(file.exists(origenes))) { stop("Ejecuta desde la raiz de DS Track; faltan fuentes.") }
  if (file.exists(respaldo) || file.exists(file.path(destino, nombres[3]))) {
    stop("Ya hay respaldo o script en el destino; conserva tu trabajo y revisa.")
  }
  if (!dir.create(respaldo)) { stop("No se pudo crear el respaldo.") }
  for (nombre in nombres[1:2]) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) {
      stop("Respaldo parcial; conserva la carpeta y revisa.")
    }
  }
  for (i in seq_along(nombres)) {
    if (!file.copy(origenes[i], file.path(destino, nombres[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial; revisa el respaldo antes de continuar.")
    }
  }
  cat("07.02 preparada sin instalar. Metadatos anteriores en respaldo_07_01/.\n")
  cat("Abre de nuevo tu proyecto y ejecuta source(\"restaurar.R\") desde R.\n")
  invisible(destino)
}

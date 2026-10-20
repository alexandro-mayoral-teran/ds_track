# Desde la raiz de DS Track: source() solo define la funcion; no instala.
preparar_practica_cierre <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/07_tidyverse/10_first_plot_closure"
  requisitos <- file.path(destino, c(".Rprofile", "renv.lock", "DESCRIPTION", "restaurar.R",
                                    "renv/activate.R", "R/funciones_calidad.R",
                                    "R/funciones_texto.R", "R/funciones_fechas.R", "revisar_fechas.R", "datos/cartera_texto.csv"))
  if (!all(file.exists(requisitos))) { stop("Completa la preparacion de 07.09 primero.") }
  relativas <- c("DESCRIPTION", "renv.lock", "R/funciones_cierre.R", "cerrar_analisis.R", "verificar_cierre.R")
  origenes <- file.path(base, c("DESCRIPTION", "renv.lock", "funciones_cierre.R", "cerrar_analisis.R", "verificar_cierre.R"))
  respaldo <- file.path(destino, "respaldo_07_09")
  if (!all(file.exists(origenes))) { stop("Ejecuta desde la raiz de DS Track; faltan fuentes.") }
  if (file.exists(respaldo) || any(file.exists(file.path(destino, relativas[-c(1, 2)])))) {
    stop("Ya hay respaldo o archivos de 07.10; conserva tu trabajo y revisa.")
  }
  if (!dir.create(respaldo)) { stop("No se pudo crear el respaldo.") }
  for (nombre in relativas[1:2]) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) {
      stop("Respaldo parcial; conserva la carpeta y revisa.")
    }
  }
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial; conserva el respaldo y revisa antes de repetir.")
    }
  }
  cat("07.10 preparada sin instalar; metadatos previos en respaldo_07_09/.\n")
  cat("Abre el mismo proyecto y ejecuta source(\"restaurar.R\") si falta sincronizar.\n")
  invisible(destino)
}

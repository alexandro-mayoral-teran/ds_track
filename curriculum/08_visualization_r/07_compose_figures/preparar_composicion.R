# Desde la raiz de DS Track: source() define la funcion; no instala paquetes.
preparar_practica_composicion <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!dir.exists(destino)) { stop("El destino debe ser una carpeta de practica.") }
  base <- "curriculum/08_visualization_r/07_compose_figures"
  previo <- "curriculum/07_tidyverse/10_first_plot_closure"
  requisitos <- file.path(destino, c(".Rprofile", "DESCRIPTION", "renv.lock", "restaurar.R",
    "renv/activate.R", "R/funciones_calidad.R", "R/funciones_texto.R",
    "R/funciones_fechas.R", "R/funciones_cierre.R", "datos/cartera_texto.csv"))
  nombres <- c("DESCRIPTION", "renv.lock", "componer_figuras.R")
  origenes <- file.path(base, nombres)
  metadatos_previos <- file.path(previo, nombres[1:2])
  if (!all(file.exists(c(origenes, metadatos_previos)))) {
    stop("Ejecuta desde la raiz de DS Track; faltan fuentes de preparacion.")
  }
  if (!all(file.exists(requisitos))) { stop("Completa la practica de 07.10 primero.") }
  respaldo <- file.path(destino, "respaldo_08_06")
  if (file.exists(respaldo) || file.exists(file.path(destino, nombres[3]))) {
    stop("Ya hay respaldo o script de 08.07; conserva el trabajo y revisa.")
  }
  actuales <- unname(tools::md5sum(file.path(destino, nombres[1:2])))
  esperados <- unname(tools::md5sum(metadatos_previos))
  if (!identical(actuales, esperados)) {
    stop("Los metadatos difieren de 07.10/08.06; revisa tus cambios antes de preparar.")
  }
  if (!dir.create(respaldo)) { stop("No se pudo crear el respaldo.") }
  for (nombre in nombres[1:2]) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) {
      stop("Respaldo parcial; conserva la carpeta y revisa antes de continuar.")
    }
  }
  for (i in seq_along(nombres)) {
    if (!file.copy(origenes[i], file.path(destino, nombres[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial; conserva el respaldo y revisa antes de repetir.")
    }
  }
  cat("08.07 preparada sin instalar; metadatos anteriores en respaldo_08_06/.\n")
  cat("Abre el mismo proyecto, reinicia R y ejecuta source(\"restaurar.R\").\n")
  invisible(destino)
}

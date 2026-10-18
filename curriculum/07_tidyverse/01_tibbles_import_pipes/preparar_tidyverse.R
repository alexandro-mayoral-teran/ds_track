# Desde la raiz de DS Track: source() define la funcion, sin copiar ni instalar.
preparar_tidyverse <- function(destino) {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) {
    stop("Indica una ruta de carpeta existente como texto.")
  }
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  base <- "curriculum/07_tidyverse/01_tibbles_import_pipes"
  requisitos <- file.path(destino, c(".Rprofile", "renv.lock", "DESCRIPTION",
                                    "renv/activate.R", "ejecutar_cierre.R", "R", "datos"))
  if (!all(file.exists(requisitos))) { stop("Falta la estructura de la practica 06.09.") }
  origenes <- c(file.path(base, c("DESCRIPTION", "renv.lock", "funciones_importacion.R",
                                 "importar_cartera.R")),
                "curriculum/02_pandas/02_read_inspect_export/cartera_demo.csv")
  relativas <- c("DESCRIPTION", "renv.lock", "R/funciones_importacion.R",
                 "importar_cartera.R", "datos/cartera_demo.csv")
  nuevas <- file.path(destino, relativas[3:5])
  respaldo <- file.path(destino, "respaldo_06_09")
  if (!all(file.exists(origenes))) { stop("Faltan fuentes; ejecuta desde la raiz de DS Track.") }
  if (dir.exists(respaldo) || any(file.exists(nuevas))) {
    stop("Ya hay material de 07.01 o archivos propios en esos destinos; conserva y revisa.")
  }
  if (!dir.create(respaldo)) { stop("No se pudo crear el respaldo de metadatos.") }
  for (nombre in c("DESCRIPTION", "renv.lock")) {
    if (!file.copy(file.path(destino, nombre), file.path(respaldo, nombre))) {
      stop("Respaldo parcial; revisa antes de continuar.")
    }
  }
  for (i in seq_along(origenes)) {
    if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = i <= 2L)) {
      stop("Preparacion parcial; conserva la carpeta y revisa el respaldo.")
    }
  }
  cat("07.01 preparada. Metadatos anteriores en respaldo_06_09/.\n")
  cat("Activa y restaura desde esta carpeta, sin reinicializar renv:\n", destino, "\n")
  invisible(destino)
}

# Alternativa por terminal; no se ejecuta al cargar el archivo con source().
if (sys.nframe() == 0L) {
  args <- commandArgs(trailingOnly = TRUE)
  if (length(args) != 1L) { stop("Indica la carpeta existente de tu proyecto 06.09.") }
  preparar_tidyverse(args[1])
}

# Solo trabaja con archivos de esta copia, desde su raiz.
if (!requireNamespace("renv", quietly = TRUE) || is.null(renv::project())) {
  stop("Activa el proyecto con ejecutar.R antes de analizar.")
}
if (!identical(normalizePath(renv::project()), normalizePath(getwd()))) {
  stop("El proyecto activo no coincide con la carpeta del analisis.")
}
if (!requireNamespace("withr", quietly = TRUE)) {
  stop("Falta withr; restaura el proyecto antes de analizar.")
}
source("R/funciones_ventas.R", encoding = "UTF-8")
source("R/funciones_archivos.R", encoding = "UTF-8")
argumentos <- commandArgs(trailingOnly = TRUE)
if (length(argumentos) > 1L) { stop("Indica como maximo una carpeta nueva de salida.") }
destino <- "output/primera_revision"
if (length(argumentos) == 1L) { destino <- argumentos[1] }
crudos <- leer_ventas("datos/ventas_entrada.csv")
revision <- validar_registros(crudos)
resumen <- resumir_importes(revision$aceptados$importe_mxn)
carpeta <- exportar_revision(revision, resumen, destino)

# withr aplica digits solo durante esta presentacion; no redondea los datos.
digitos_antes <- getOption("digits")
cat("Resumen mostrado con cuatro cifras significativas:\n")
withr::with_options(list(digits = 4), print(resumen))
if (!identical(getOption("digits"), digitos_antes)) {
  stop("La opcion de presentacion no se restauro.")
}
# Evidencia de ejecucion: util para diagnosticar, no sustituye el lockfile.
writeLines(capture.output(utils::sessionInfo()), file.path(carpeta, "sesion.txt"))
cat("Entrega creada, sin redondear los importes guardados:\n")
print(carpeta)
print(revision$controles)
print(utils::packageVersion("withr"))

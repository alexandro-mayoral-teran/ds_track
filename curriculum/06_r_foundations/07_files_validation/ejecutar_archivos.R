# Ejecutar desde la raiz; argumentos opcionales: entrada.csv carpeta_nueva.
source("curriculum/06_r_foundations/06_functions_control/funciones_ventas.R",
       encoding = "UTF-8")
source("curriculum/06_r_foundations/07_files_validation/funciones_archivos.R",
       encoding = "UTF-8")
argumentos <- commandArgs(trailingOnly = TRUE)
if (length(argumentos) == 0L) {
  entrada <- "curriculum/06_r_foundations/07_files_validation/ventas_entrada.csv"
  destino <- "curriculum/06_r_foundations/07_files_validation/output/primera_revision"
} else if (length(argumentos) == 2L) {
  entrada <- argumentos[1]
  destino <- argumentos[2]
} else {
  stop("Indica entrada y destino juntos, o ejecuta sin argumentos.")
}
crudos <- leer_ventas(entrada)
revision <- validar_registros(crudos)
resumen <- resumir_importes(revision$aceptados$importe_mxn)
# Validar y resumir terminan antes de crear la salida.
carpeta <- exportar_revision(revision, resumen, destino)

# Volver a leer conserva texto; solo los campos numericos se convierten.
releidos <- read.csv(file.path(carpeta, "aceptados.csv"), colClasses = "character",
                      na.strings = character(0), check.names = FALSE,
                      fileEncoding = "UTF-8")
importe_texto <- releidos$importe_mxn
importe_texto[importe_texto == "NA"] <- NA_character_
# write.csv puede usar notacion cientifica: se relee su formato, no el de entrada.
importes_releidos <- tryCatch(as.double(importe_texto),
                              warning = function(w) { stop(conditionMessage(w)) })
if (!identical(names(releidos), names(revision$aceptados)) ||
    nrow(releidos) != nrow(revision$aceptados) ||
    !identical(releidos$id_venta, revision$aceptados$id_venta) ||
    !identical(releidos$nota, revision$aceptados$nota) ||
    !isTRUE(all.equal(importes_releidos, revision$aceptados$importe_mxn, tolerance = 1e-12))) {
  stop("La relectura no conserva estructura, identidad o importes esperados.")
}
resumen_releido <- resumir_importes(importes_releidos)
if (!isTRUE(all.equal(resumen_releido, resumen, tolerance = 1e-12))) {
  stop("Los indicadores releidos no coinciden con los calculados.")
}
cat("Carpeta de revision creada:\n")
print(carpeta)
cat("Conteos de entrada, aceptados y rechazos:\n")
print(revision$controles)
cat("Resumen de aceptados; el total completo permanece desconocido:\n")
print(resumen)
cat("Relectura de identidad, notas, importes e indicadores comprobada.\n")
print(R.version.string)
print(utils::sessionInfo())

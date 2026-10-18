# Desde la raiz de la copia preparada para 06.09.
if (!file.exists("renv/activate.R") || !file.exists("R/comparar_resultados.R")) {
  stop("Ejecuta desde la raiz de la copia de cierre preparada.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el proyecto antes de analizar.") }
source("R/funciones_ventas.R", encoding = "UTF-8")
source("R/funciones_archivos.R", encoding = "UTF-8")
source("R/comparar_resultados.R", encoding = "UTF-8")
argumentos <- commandArgs(trailingOnly = TRUE)
entrada <- "datos/ventas_entrada.csv"
referencia <- "output/referencia_python"
destino <- "output/cierre_r"
if (length(argumentos) == 3L) {
  entrada <- argumentos[1]; referencia <- argumentos[2]; destino <- argumentos[3]
} else if (length(argumentos) != 0L) {
  stop("Indica entrada, referencia y destino juntos, o ejecuta sin argumentos.")
}
huella <- unname(tools::md5sum(entrada))
revision <- validar_registros(leer_ventas(entrada))
resumen <- resumir_importes(revision$aceptados$importe_mxn)
memoria <- comparar_con_python(tablas_revision(revision, resumen), referencia, entrada)
# Comparar precede a escribir; un desacuerdo no crea la entrega R.
carpeta <- exportar_revision(revision, resumen, destino)
guardados <- comparar_con_python(leer_entrega_cierre(carpeta), referencia, entrada)
if (!identical(huella, unname(tools::md5sum(entrada)))) { stop("La fuente cambio durante el cierre.") }
memoria$etapa <- "memoria"
guardados$etapa <- "csv_guardado"
pruebas <- rbind(memoria, guardados)
writeLines(capture.output(utils::sessionInfo()), file.path(carpeta, "sesion_r.txt"))
# Informe al final; no hace atomica la carpeta ni acredita aprendizaje.
write.csv(pruebas, file.path(carpeta, "conciliacion.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
cat("Cierre conciliado con Python. Controles comprobados:\n")
print(nrow(pruebas)) # 72 para este esquema.
withr::with_options(list(digits = 4), print(resumen))
print(carpeta)

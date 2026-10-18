# Solo lectura, desde la copia preparada. No activa ni instala paquetes externos.
source("R/funciones_ventas.R", encoding = "UTF-8")
source("R/funciones_archivos.R", encoding = "UTF-8")
source("R/comparar_resultados.R", encoding = "UTF-8")
argumentos <- commandArgs(trailingOnly = TRUE)
entrada <- "datos/ventas_entrada.csv"
referencia <- "output/referencia_python"
entrega <- "output/cierre_r"
if (length(argumentos) == 3L) {
  entrada <- argumentos[1]; referencia <- argumentos[2]; entrega <- argumentos[3]
} else if (length(argumentos) != 0L) {
  stop("Indica entrada, referencia y entrega juntos, o ejecuta sin argumentos.")
}
requeridos <- file.path(entrega, c("aceptados.csv", "rechazos.csv", "controles.csv",
                                  "resumen.csv", "sesion_r.txt", "conciliacion.csv"))
if (!all(file.exists(requeridos) & !dir.exists(requeridos))) {
  stop("Entrega incompleta: faltan tablas, sesion o informe final.")
}
revision <- validar_registros(leer_ventas(entrada))
resumen <- resumir_importes(revision$aceptados$importe_mxn)
a <- comparar_con_python(tablas_revision(revision, resumen), referencia, entrada)
b <- comparar_con_python(leer_entrega_cierre(entrega), referencia, entrada)
cat("Verificacion de solo lectura: controles correctos sobre recalculo y CSV guardados.\n")
print(nrow(a) + nrow(b))
print(R.version.string)

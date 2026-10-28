# Desde la copia preparada, con su entorno restaurado. No inicia HTTP.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
library(shiny)
for (archivo in c("cartera.R", "consulta.R", "validacion.R", "presentacion.R", "consulta_module.R")) {
  source(archivo, encoding = "UTF-8")
}
for (archivo in c("pruebas_minimo.R", "pruebas_funciones.R", "pruebas_servidor.R")) {
  cat("Ejecutando ", archivo, "\n", sep = "")
  source(archivo, encoding = "UTF-8")
}
cat("OK conjunto esencial. Falta complementar con la lista de navegador del lab.\n")

# Desde la copia preparada. Activar puede preparar renv si aun no esta instalado.
if (!file.exists("renv.lock") || !file.exists("R/funciones_ventas.R")) {
  stop("Ejecuta desde la raiz del proyecto preparado.")
}
source(".Rprofile")
estado <- renv::status()
if (!isTRUE(estado$synchronized)) {
  stop("Revisa renv::status() y restaura antes de ejecutar el analisis.")
}
source("analisis.R", encoding = "UTF-8")

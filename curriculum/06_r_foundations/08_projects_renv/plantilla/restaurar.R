# Rscript --vanilla restaurar.R, desde la raiz de la copia preparada.
if (!file.exists("renv.lock") || !file.exists("renv/activate.R")) {
  stop("Falta el proyecto preparado; revisa la carpeta actual.")
}
# --vanilla omite perfiles automaticos; activamos expresamente el del proyecto.
source(".Rprofile")
# Restaura las versiones registradas; puede descargar e instalar localmente.
renv::restore(prompt = FALSE)
estado <- renv::status()
if (!isTRUE(estado$synchronized)) { stop("El proyecto sigue sin sincronizar.") }
print(R.version.string)
print(.libPaths())
print(utils::packageVersion("renv"))
print(utils::packageVersion("withr"))

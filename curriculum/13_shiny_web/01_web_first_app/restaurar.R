# Desde la raiz de la copia preparada; restaurar puede descargar paquetes locales.
if (!all(file.exists(c("DESCRIPTION", "renv.lock", ".Rprofile", "renv/activate.R")))) {
  stop("Falta el proyecto preparado; revisa la carpeta actual.")
}
source(".Rprofile")
renv::restore(prompt = FALSE)
estado <- renv::status()
if (!isTRUE(estado$synchronized)) stop("El proyecto no esta sincronizado; revisar sin ocultar el error.")
cat(R.version.string, "\n")
print(.libPaths())
cat("shiny ", as.character(utils::packageVersion("shiny")), "\n", sep = "")
cat("renv ", as.character(utils::packageVersion("renv")), "\n", sep = "")

# Desde la raiz de la copia; puede descargar solo renv en la biblioteca local.
esperado <- utils::read.csv("entorno.csv", colClasses = "character", na.strings = NULL)
if (!identical(as.character(getRversion()), esperado$valor[esperado$clave == "r"])) stop("Version R distinta de la declarada; revisar antes de restaurar.")
source(".Rprofile")
renv::restore(prompt = FALSE)
if (!isTRUE(renv::status()$synchronized)) stop("Biblioteca y lockfile no sincronizados.")
cat("R ", getRversion() |> as.character(), "; renv ", as.character(utils::packageVersion("renv")), "\n", sep = "")
print(.libPaths())

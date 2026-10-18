# Desde la raiz del proyecto renv que ya utilizas, despues de preparar 07.01.
if (!file.exists("R/funciones_importacion.R") || !file.exists(".Rprofile")) {
  stop("Ejecuta desde la raiz de la practica preparada.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile antes de continuar.") }
source("R/funciones_importacion.R")
ruta <- "datos/cartera_demo.csv"
huella <- tools::md5sum(ruta)

cartera <- leer_cartera(ruta)
comprobar_muestra(cartera)
print(cartera, n = 6, width = Inf)
print(vapply(cartera, typeof, character(1)))

# El pipe nativo pasa cada resultado al primer argumento de la llamada siguiente.
vista <- cartera |> head(2)
stopifnot(identical(vista, head(cartera, 2)), nrow(cartera) == 6L)
print(vista)
cat("Filas en la vista:", cartera |> head(2) |> nrow(), "\n")
cat("Saldo conocido: 6000 MXN; cobertura: 6/6. Atraso desconocido: 1/6.\n")
stopifnot(identical(huella, tools::md5sum(ruta)))
print(R.version.string)
print(vapply(c("readr", "tibble", "withr", "renv"),
             function(p) as.character(utils::packageVersion(p)), character(1)))
# Sin exportacion ni limpieza: imprime controles y deja la fuente intacta.

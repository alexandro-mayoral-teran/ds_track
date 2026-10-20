# En la raiz de la practica: bloques en el IDE o source completo tras reiniciar R.
if (!file.exists("R/funciones_formas.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.07.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile de 07.07 desde R.") }
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_formas.R", encoding = "UTF-8")
ruta <- "datos/cartera_formas.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_fuente_formas(ruta)
original <- fuente
largo <- fuente |> dplyr::select(id_credito, corte = fecha_corte, saldo_mxn)
claves_presentes <- largo |> dplyr::select(id_credito, corte)
ancho <- largo_a_ancho(largo)
recuperado <- recuperar_saldos(ancho, claves_presentes)
comprobar_formas(largo, ancho, claves_presentes, recuperado)
controles <- control_por_corte(recuperado)
stopifnot(identical(dim(largo), c(48L, 3L)), identical(dim(ancho), c(24L, 3L)),
          identical(controles$registros, c(24L, 24L)),
          identical(controles$conocidos, c(21L, 21L)),
          identical(controles$saldo_observado_mxn, c(47200, 46700)),
          sum(is.na(recuperado$saldo_mxn)) == 6L,
          identical(fuente, original), identical(huella, tools::md5sum(ruta)))
print(ancho, n = 24, width = Inf)
print(controles, width = Inf)
cat("48 observaciones -> 24 filas anchas -> 48 recuperadas; seis saldos NA conservados.\n")
cat("Saldos por corte: 47200 y 46700 MXN, cada uno con cobertura 21/24.\n")
print(R.version.string)
print(utils::packageVersion("tidyr"))
# No agrega ni exporta: conserva una proyeccion de tres campos, no las cinco columnas fuente.

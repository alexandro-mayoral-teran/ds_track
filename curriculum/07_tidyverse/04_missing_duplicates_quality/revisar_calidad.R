# En la raiz de la practica: ejecutar bloques en el IDE o source() completo.
if (!file.exists("R/funciones_calidad.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.04.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Comprueba el entorno de 07.02.") }
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
ruta <- "datos/cartera_calidad.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_conversion(ruta)
original <- fuente
revision <- evaluar_calidad(fuente)
trabajo <- revision$trabajo
aceptados <- revision$aceptados
rechazados <- revision$rechazados
banderas <- revision$banderas

stopifnot(
  identical(dim(trabajo), c(44L, 12L)),
  nrow(aceptados) == 29L, nrow(rechazados) == 15L,
  identical(dim(banderas), c(44L, 15L)),
  sum(as.matrix(banderas)) == 19L,
  identical(rechazados$numero_registro,
            c(1L, 2L, 5L, 9L, 14L, 18L, 21L, 23L, 31L, 33L, 38L, 41L, 42L, 43L, 44L)),
  identical(revision$controles$saldo_observado_mxn, c(234900, 177250, 57650)),
  identical(revision$controles$saldos_conocidos, c(42L, 29L, 13L)),
  identical(revision$controles$saldos_sin_interpretar, c(2L, 0L, 2L)),
  identical(fuente, original), identical(huella, tools::md5sum(ruta))
)
print(revision$controles, width = Inf)
print(rechazados |> dplyr::select(numero_registro, id_credito, motivos), n = 15, width = Inf)
cat("44 = 29 aceptados + 15 rechazados; 19 incumplimientos, no 19 filas.\n")
cat("Saldo interpretable de registros de entrada: 234900 = 177250 + 57650 MXN.\n")
cat("Incluye repeticiones y negativos en la entrada; 2 saldos siguen sin interpretar.\n")
print(R.version.string)
print(utils::packageVersion("dplyr"))
# Advertencias de parseo esperadas y motivos conservados. No exporta ni imputa.

# Ejecutar en la raiz del mismo proyecto renv preparado para 07.10.
if (!file.exists("R/funciones_cierre.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.10.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile de 07.10 desde R.") }
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
cierre <- construir_cierre(fuente)
comprobar_cierre(fuente, cierre)
stopifnot(identical(cierre$resultado$controles$registros, c(48L,36L,12L)),
          identical(cierre$datos_figura$creditos, c(14L,14L)),
          identical(cierre$datos_figura$saldo_mxn, c(29000,31800)),
          identical(cierre$datos_figura$aceptados_corte, c(18L,18L)),
          nrow(cierre$sin_pareja) == 8L, nrow(cierre$fuera_cortes) == 0L,
          sum(cierre$comunes$diferencia_mxn) == 2800,
          identical(huella, tools::md5sum(ruta)))
print(cierre$resultado$controles, width = Inf)
print(cierre$resumen_cortes, width = Inf)
print(cierre$datos_figura, width = Inf)
figura <- crear_figura_cierre(cierre)
print(figura) # En el IDE aparece en Plots; dentro de una funcion, print es necesario.
cat("Base comun: 29000 -> 31800 MXN; +2800 MXN (+9.66% sobre septiembre).\n")
cat("18 aceptados por corte, 14 IDs comunes; no atribuye causas ni representa todos los creditos.\n")
print(utils::packageVersion("ggplot2"))
# No exporta por source: elige una carpeta nueva con exportar_cierre(cierre, ...).

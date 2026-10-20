# En la raiz de la practica: bloques en el IDE o source completo tras reiniciar R.
if (!file.exists("R/funciones_fechas.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.09.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile de 07.09 desde R.") }
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
original <- fuente
resultado <- preparar_fechas(fuente)
comprobar_fechas(fuente, resultado)
trabajo <- resultado$trabajo
aceptados <- resultado$aceptados
rechazados <- resultado$rechazados
septiembre <- seleccionar_periodo(aceptados, lubridate::ymd("2026-09-01"), lubridate::ymd("2026-10-01"))
octubre <- seleccionar_periodo(aceptados, lubridate::ymd("2026-10-01"), lubridate::ymd("2026-11-01"))
resumen <- resumir_cortes_fechas(aceptados)
comparables <- dplyr::inner_join(
  septiembre |> dplyr::select(id_credito, saldo_sep = saldo_mxn),
  octubre |> dplyr::select(id_credito, saldo_oct = saldo_mxn),
  by = "id_credito", relationship = "one-to-one", na_matches = "never"
) |> dplyr::mutate(diferencia_mxn = as.double(saldo_oct) - saldo_sep)
stopifnot(identical(dim(trabajo), c(48L, 15L)),
          identical(resultado$controles$registros, c(48L, 36L, 12L)),
          identical(resultado$controles$saldo_observado_mxn, c(112800, 81400, 31400)),
          sum(as.matrix(resultado$banderas)) == 12L,
          identical(rechazados$numero_registro, c(5L,9L,12L,14L,18L,23L,30L,33L,43L,44L,47L,48L)),
          identical(resumen$registros, c(18L, 18L)),
          identical(resumen$saldo_observado_mxn, c(39900, 41500)),
          nrow(comparables) == 14L, sum(comparables$saldo_sep) == 29000,
          sum(comparables$saldo_oct) == 31800, sum(comparables$diferencia_mxn) == 2800,
          identical(fuente, original), identical(huella, tools::md5sum(ruta)))
print(resultado$controles, width = Inf)
print(resumen, width = Inf)
print(rechazados |> dplyr::select(numero_registro, motivos), n = 12, width = Inf)
cat("48 = 36 aceptados + 12 rechazados bajo el contrato declarado.\n")
cat("14 IDs comunes: 29000 -> 31800 MXN; diferencia 2800 sobre la misma base.\n")
print(R.version.string)
print(utils::packageVersion("lubridate"))
# Advertencia de fecha imposible visible; conserva origen y motivos. No exporta ni grafica.

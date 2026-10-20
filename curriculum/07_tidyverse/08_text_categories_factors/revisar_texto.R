# En la raiz de la practica: ejecutar bloques o source completo desde el IDE.
if (!file.exists("R/funciones_texto.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.08.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile de 07.08 desde R.") }
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
original <- fuente
resultado <- preparar_segmentos(fuente)
comprobar_segmentos(fuente, resultado)
trabajo <- resultado$trabajo
reconocidos <- resultado$reconocidos
pendientes <- resultado$pendientes
resumen <- resultado$resumen
stopifnot(identical(dim(trabajo), c(48L, 10L)),
          identical(resultado$controles$registros, c(48L, 45L, 3L)),
          identical(resultado$controles$saldo_observado_mxn, c(112800, 105800, 7000)),
          identical(pendientes$numero_registro, c(5L, 9L, 48L)),
          sum(trabajo$estado_segmento == "ausente") == 2L,
          sum(trabajo$estado_segmento == "fuera_catalogo") == 1L,
          sum(trabajo$texto_modificado) == 46L,
          identical(resumen$registros, c(10L, 12L, 12L, 11L)),
          identical(resumen$saldo_observado_mxn, c(23000, 27600, 28800, 26400)),
          identical(fuente, original), identical(huella, tools::md5sum(ruta)))
print(resultado$controles, width = Inf)
print(resumen, width = Inf)
print(pendientes |> dplyr::select(numero_registro, segmento, segmento_normalizado,
                                  estado_segmento, saldo_mxn), width = Inf)
cat("48 = 45 reconocidos + 3 pendientes SOLO de segmento; las fechas e IDs no se validaron.\n")
cat("112800 = 105800 + 7000 MXN de registros de entrada; no es saldo a una fecha unica.\n")
print(R.version.string)
print(utils::packageVersion("stringr"))
print(utils::packageVersion("forcats"))
# Sin exportar ni graficar; no acredita aceptacion completa de registros.

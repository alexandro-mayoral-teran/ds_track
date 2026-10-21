# Desde la raiz del mismo proyecto renv. source() define la funcion; no exporta.
# Copia este archivo desde el editor, sin reemplazar una copia propia existente.
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")

cerrar_visual <- function(destino) {
  ruta <- "datos/cartera_texto.csv"
  huella <- tools::md5sum(ruta)
  fuente <- leer_texto_segmentos(ruta)
  cierre <- construir_cierre(fuente)
  comprobar_cierre(fuente, cierre)
  # Valores conocidos de esta muestra: no convertir un cambio de fuente en exito.
  stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
            nrow(cierre$comunes) == 14L,
            identical(cierre$datos_figura$saldo_mxn, c(29000, 31800)),
            identical(cierre$datos_figura$aceptados_corte, c(18L, 18L)))
  datos <- cierre$datos_figura
  inicial <- datos$saldo_mxn[1]
  diferencia <- diff(datos$saldo_mxn)
  cambio <- if (inicial == 0) NA_real_ else 100 * diferencia / inicial
  print(datos)
  cat(sprintf("Diferencia: %.0f MXN; cambio relativo: %.2f%% del saldo inicial.\n",
              diferencia, cambio))
  # Reutiliza la entrega comprobada de 07.10: siete CSV, RDS, PNG y sesion.
  exportar_cierre(cierre, destino)
  comprobar_entrega(fuente, destino)
  stopifnot(identical(huella, tools::md5sum(ruta)))
  invisible(cierre)
}

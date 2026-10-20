# Ejecutar por bloques o con source desde la raiz de la practica en el IDE.
if (!file.exists("R/funciones_resumen.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.05.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Comprueba el entorno de 07.02.") }
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_resumen.R", encoding = "UTF-8")
ruta <- "datos/cartera_calidad.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_conversion(ruta)
original <- fuente
revision <- evaluar_calidad(fuente)
detalle <- revision$aceptados
detalle_original <- detalle
resumen <- resumir_grupos(detalle)
comprobar_resumen(detalle, resumen)
stopifnot(nrow(fuente) == 44L, nrow(detalle) == 29L,
          nrow(revision$rechazados) == 15L,
          identical(resumen$segmento, c("comercio", "consumo", "educacion", "servicios")),
          identical(resumen$registros, c(8L, 5L, 10L, 6L)),
          identical(resumen$saldo_observado_mxn, c(47000, 35250, 57000, 38000)),
          identical(resumen$atrasos_30_confirmados, c(5L, 3L, 6L, 4L)),
          sum(resumen$saldo_observado_mxn) == 177250,
          all(resumen$cobertura_saldo_pct == 100),
          all(resumen$cobertura_atraso_pct == 100),
          identical(detalle, detalle_original), identical(fuente, original),
          identical(huella, tools::md5sum(ruta)))
print(resumen, width = Inf)
cat("Base: 29 aceptados de 44 registros; 15 rechazos conservados.\n")
cat("Saldo de aceptados: 177250 MXN, cobertura 29/29.\n")
print(R.version.string)
print(utils::packageVersion("dplyr"))
# Advertencias de conversion de 07.04 visibles; no exporta ni modifica entradas.

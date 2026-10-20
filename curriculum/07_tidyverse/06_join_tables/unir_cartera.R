# En la raiz de la practica: ejecutar bloques o source completo en el IDE.
if (!file.exists("R/funciones_uniones.R") || !file.exists(".Rprofile")) {
  stop("Abre la practica preparada para 07.06.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Comprueba el entorno de 07.02.") }
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_resumen.R", encoding = "UTF-8")
source("R/funciones_uniones.R", encoding = "UTF-8")
rutas <- c("datos/cartera_calidad.csv", "datos/catalogo_etiquetas.csv")
huellas <- tools::md5sum(rutas)
fuente <- leer_texto_conversion(rutas[1])
original <- fuente
revision <- evaluar_calidad(fuente)
detalle <- revision$aceptados
detalle_original <- detalle
catalogo <- leer_catalogo(rutas[2])
catalogo_original <- catalogo
resultado <- unir_catalogo(detalle, catalogo)
comprobar_union(detalle, catalogo, resultado)
ampliado <- resultado$ampliado
stopifnot(nrow(fuente) == 44L, nrow(revision$rechazados) == 15L,
          identical(dim(ampliado), c(29L, 14L)),
          identical(resultado$controles$registros, c(29L, 19L, 10L)),
          identical(resultado$controles$saldo_observado_mxn, c(177250, 120250, 57000)),
          identical(resultado$catalogo_sin_uso$segmento, "salud"),
          sum(ampliado$en_catalogo & is.na(ampliado$etiqueta_segmento)) == 6L,
          identical(as.list(resumir_grupos(ampliado)), as.list(resumir_grupos(detalle))),
          identical(detalle, detalle_original), identical(catalogo, catalogo_original),
          identical(fuente, original), identical(huellas, tools::md5sum(rutas)))
print(resultado$controles, width = Inf)
print(ampliado |> dplyr::select(numero_registro, id_credito, segmento,
                                etiqueta_segmento, en_catalogo), n = 29, width = Inf)
cat("29 filas y 177250 MXN conservados; 19 coincidencias y 10 sin catalogo.\n")
cat("6 coincidencias tienen etiqueta desconocida; salud queda sin uso.\n")
print(R.version.string)
print(utils::packageVersion("dplyr"))
# Advertencias de conversion de 07.04 visibles. No exporta ni modifica fuentes.

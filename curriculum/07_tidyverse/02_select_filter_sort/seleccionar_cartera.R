# Abrir en el proyecto de practica; ejecutar por bloques o con Source.
if (!file.exists("R/funciones_importacion.R") || !file.exists(".Rprofile")) {
  stop("Abre la carpeta de practica preparada, no la raiz de DS Track.")
}
source(".Rprofile")
if (!isTRUE(renv::status()$synchronized)) { stop("Restaura el lockfile antes de continuar.") }
source("R/funciones_importacion.R", encoding = "UTF-8")
ruta <- "datos/cartera_demo.csv"
huella <- tools::md5sum(ruta)
cartera <- leer_cartera(ruta)
comprobar_muestra(cartera)
original <- cartera

# La condicion completa tiene tres estados. No rellenamos datos faltantes.
confirmados <- cartera |> dplyr::filter(saldo_mxn >= 500, dias_atraso >= 5)
no_cumplen <- cartera |> dplyr::filter(!(saldo_mxn >= 500 & dias_atraso >= 5))
pendientes <- cartera |> dplyr::filter(is.na(saldo_mxn >= 500 & dias_atraso >= 5))

# Filtrar antes de retirar columnas necesarias. Desempate explicito por clave.
seleccion <- confirmados |>
  dplyr::select(id_credito, segmento, saldo_mxn, dias_atraso) |>
  dplyr::arrange(dplyr::desc(saldo_mxn), id_credito)
presentacion <- seleccion |> dplyr::rename(saldo_pesos = saldo_mxn)
sin_coincidencias <- cartera |>
  dplyr::filter(saldo_mxn > 10000) |>
  dplyr::select(id_credito, segmento, saldo_mxn, dias_atraso) |>
  dplyr::arrange(dplyr::desc(saldo_mxn), id_credito)

stopifnot(
  identical(seleccion$id_credito, c("002", "003", "006")),
  identical(seleccion$saldo_mxn, c(1500, 750, 500)),
  identical(seleccion$dias_atraso, c(10L, 45L, 5L)),
  identical(names(seleccion), c("id_credito", "segmento", "saldo_mxn", "dias_atraso")),
  sum(seleccion$saldo_mxn) == 2750,
  !anyNA(seleccion$saldo_mxn),
  identical(no_cumplen$id_credito, c("001", "004")),
  identical(pendientes$id_credito, "005"),
  nrow(confirmados) + nrow(no_cumplen) + nrow(pendientes) == nrow(cartera),
  identical(dim(sin_coincidencias), c(0L, 4L)),
  identical(names(sin_coincidencias), names(seleccion)),
  identical(vapply(sin_coincidencias, typeof, character(1)),
            vapply(seleccion, typeof, character(1))),
  identical(cartera, original), identical(huella, tools::md5sum(ruta))
)
cat("Pregunta: saldo >= 500 MXN y atraso >= 5 dias.\n")
print(seleccion, n = 6, width = Inf)
cat("6 filas = 3 confirmadas + 2 no cumplen + 1 pendiente.\n")
cat("Subtotal seleccionado: 2750 MXN; saldo conocido en 3/3.\n")
print(pendientes, n = 6, width = Inf)
print(presentacion, n = 6, width = Inf)
print(sin_coincidencias)
print(R.version.string)
print(utils::packageVersion("dplyr"))
# No exporta ni sobrescribe la fuente. No atribuye riesgo a estas condiciones.

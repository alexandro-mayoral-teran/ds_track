# Autoría opcional; usa CSV temporal, no modifica cartera.csv ni monta UI.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("cartera.R", encoding = "UTF-8")
source("validacion.R", encoding = "UTF-8")
for (texto in c("", " ", "-1", "+1", "01", "1.0", "1900.5", "1e3", "1,000", "1000001")) {
  stopifnot(!revisar_filtros("2026-09-30", c("comercio", "servicios"), texto)$ok)
}
for (texto in c("0", "1", "1900", "2000", "1000000")) {
  stopifnot(revisar_filtros("2026-09-30", NULL, texto)$ok)
}
stopifnot(!revisar_filtros("2026-02-30", character(), "0")$ok,
          !revisar_filtros("2026-09-30", "otro", "0")$ok,
          !revisar_filtros("2026-09-30", character(), NA_character_)$ok)
fallo_salida <- function(expr, patron) {
  error <- tryCatch({ force(expr); NULL }, error = identity)
  stopifnot(inherits(error, "shiny.silent.error"), grepl(patron, conditionMessage(error), fixed = TRUE))
}
celdas <- function(html) {
  trimws(gsub("</?td[^>]*>", "", regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]], perl = TRUE))
}
local({
  ruta <- tempfile(fileext = ".csv"); on.exit(unlink(ruta))
  original <- readLines("cartera.csv", encoding = "UTF-8")
  writeLines(original, ruta, useBytes = TRUE)
  entorno <- new.env(parent = globalenv())
  app <- source("app.R", local = entorno, encoding = "UTF-8")$value
  lector <- entorno$leer_fuente_segura
  entorno$leer_fuente_segura <- function(...) lector(ruta)
  shiny::testServer(app$serverFuncSource(), {
    session$setInputs(aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30",
      segmentos = c("comercio", "servicios"), minimo_texto = "2000", mostrar_tabla = TRUE)
    fallo_salida(output$resumen, "")
    session$setInputs(aplicar = 1L)
    stopifnot(identical(output$resumen, "Creditos seleccionados: 2; saldo seleccionado: 4500 MXN."),
      identical(output$cobertura, "Cobertura: 2 de 3 creditos del corte (66.67%)."),
      identical(celdas(output$tabla), c("002", "servicios", "2026-09-30", "2000", "003", "comercio", "2026-09-30", "2500")))
    anterior <- estado()$consulta
    session$setInputs(minimo_texto = "1900.5")
    stopifnot(identical(estado()$consulta, anterior))
    session$setInputs(aplicar = 2L)
    stopifnot(identical(estado()$consulta, anterior), estado()$tipo == "rechazo", grepl("No se aplico", output$aviso))
    session$setInputs(minimo_texto = "0", segmentos = "comercio", aplicar = 3L)
    stopifnot(identical(output$resumen, "Creditos seleccionados: 2; saldo seleccionado: 2500 MXN."),
      identical(celdas(output$tabla), c("001", "comercio", "2026-09-30", "0", "003", "comercio", "2026-09-30", "2500")))
    session$setInputs(segmentos = NULL, aplicar = 4L)
    stopifnot(estado()$tipo == "vacio", identical(output$resumen, "Creditos seleccionados: 0; saldo seleccionado: 0 MXN."),
      identical(output$cobertura, "Cobertura: 0 de 3 creditos del corte (0.00%)."))
    fallo_salida(output$tabla, "No hay filas seleccionadas")
    session$setInputs(corte = "2026-11-30", segmentos = "comercio", aplicar = 5L)
    stopifnot(estado()$tipo == "sin_universo")
    fallo_salida(output$resumen, ""); fallo_salida(output$cobertura, "")
    session$setInputs(corte = "2026-10-31", segmentos = c("comercio", "servicios"), minimo_texto = "2000", aplicar = 6L)
    stopifnot(identical(output$resumen, "Creditos seleccionados: 1; saldo seleccionado: 2600 MXN."))
    unlink(ruta); session$setInputs(aplicar = 7L)
    stopifnot(estado()$tipo == "fuente", is.null(estado()$consulta))
    fallo_salida(output$resumen, ""); fallo_salida(output$tabla, "")
    writeLines(c(original, original[length(original)]), ruta, useBytes = TRUE)
    session$setInputs(corte = "2026-09-30", aplicar = 8L)
    stopifnot(estado()$tipo == "fuente"); fallo_salida(output$cobertura, "")
    writeLines(original[1], ruta, useBytes = TRUE); session$setInputs(aplicar = 9L)
    stopifnot(estado()$tipo == "sin_universo"); fallo_salida(output$resumen, "")
    writeLines(original, ruta, useBytes = TRUE); session$setInputs(aplicar = 10L)
    stopifnot(identical(output$resumen, "Creditos seleccionados: 2; saldo seleccionado: 4500 MXN."))
    entorno$crear_consulta <- function(...) stop("Fallo deliberado de autoria")
    session$setInputs(aplicar = 11L)
    stopifnot(estado()$tipo == "error", is.null(estado()$consulta)); fallo_salida(output$resumen, "")
  })
})
minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(minimo$serverFuncSource(), {
  session$setInputs(minimo = "0")
  stopifnot(identical(output$valor, "Minimo valido: 0 MXN."), length(celdas(output$tabla)) == 6L)
  session$setInputs(minimo = ""); fallo_salida(output$valor, "Escribe un minimo")
  session$setInputs(minimo = "1.5"); fallo_salida(output$tabla, "Usa digitos")
  session$setInputs(minimo = "2501"); fallo_salida(output$tabla, "No hay coincidencias")
  session$setInputs(minimo = "2000"); stopifnot(length(celdas(output$tabla)) == 4L)
})
cat("Entradas, rechazo, cero/vacio/sin universo, fuente ausente/invalida/vacia, recuperacion y error inesperado: OK. UI por separado.\n")

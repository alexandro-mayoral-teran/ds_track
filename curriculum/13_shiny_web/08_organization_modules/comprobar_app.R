# Autoría opcional: no monta UI; navegador y descargas reales se revisan aparte.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
library(shiny)
for (archivo in c("cartera.R", "consulta.R", "validacion.R", "presentacion.R", "consulta_module.R")) {
  source(archivo, encoding = "UTF-8")
}
stopifnot(identical(NS("izquierda")("corte"), "izquierda-corte"))
celdas <- function(html) {
  trimws(gsub("</?td[^>]*>", "", regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]], perl = TRUE))
}
fijar <- function(sesion, id, ...) {
  valores <- list(...); names(valores) <- paste0(id, "-", names(valores))
  do.call(sesion$setInputs, valores)
}
local({
  ruta <- tempfile(fileext = ".csv"); on.exit(unlink(ruta))
  original <- readLines("cartera.csv", encoding = "UTF-8"); writeLines(original, ruta, useBytes = TRUE)
  entorno <- new.env(parent = globalenv())
  app <- source("app.R", local = entorno, encoding = "UTF-8")$value
  html <- htmltools::renderTags(entorno$ui)$html
  ids <- regmatches(html, gregexpr('(?<= id=")[^"]+', html, perl = TRUE))[[1]]
  stopifnot(!anyDuplicated(ids), all(c("izquierda-corte", "derecha-corte", "comparacion") %in% ids))
  servidor <- entorno$consultaServer
  entorno$consultaServer <- function(id, ...) servidor(id, ruta = ruta)
  testServer(app$serverFuncSource(), {
    for (id in c("izquierda", "derecha")) fijar(session, id,
      aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30",
      segmentos = c("comercio", "servicios"), minimo_texto = "2000", mostrar_tabla = TRUE)
    stopifnot(is.null(a$estado()$consulta), is.null(b$estado()$consulta))
    fijar(session, "derecha", corte = "2026-10-31", aplicar = 1L)
    b_guardada <- b$estado()
    stopifnot(identical(b_guardada$consulta$indicadores$saldo_mxn, 2600), is.null(a$estado()$consulta))
    casos <- list(list("2026-09-30", c("comercio", "servicios"), "2000", c("002", "003"), c(2000, 2500)),
      list("2026-10-31", c("comercio", "servicios"), "2000", "003", 2600),
      list("2026-09-30", "comercio", "0", c("001", "003"), c(0, 2500)),
      list("2026-09-30", "comercio", "1", "003", 2500),
      list("2026-10-31", "servicios", "1900", "002", 1900),
      list("2026-10-31", "servicios", "1901", character(), numeric()),
      list("2026-09-30", NULL, "0", character(), numeric()))
    for (i in seq_along(casos)) {
      caso <- casos[[i]]; anterior <- a$estado()
      fijar(session, "izquierda", corte = caso[[1]], segmentos = caso[[2]], minimo_texto = caso[[3]])
      stopifnot(identical(a$estado(), anterior), identical(b$estado(), b_guardada))
      fijar(session, "izquierda", aplicar = i)
      q <- a$estado()$consulta
      stopifnot(identical(q$seleccion$id_credito, caso[[4]]), identical(q$seleccion$saldo_mxn, caso[[5]]),
        q$indicadores$saldo_mxn == sum(caso[[5]]), nrow(q$universo) == 3L, identical(b$estado(), b_guardada))
      stopifnot(grepl("izquierda-csv_seleccion", output[["izquierda-descargas"]]$html, fixed = TRUE),
        grepl("derecha-csv_contexto", output[["derecha-descargas"]]$html, fixed = TRUE))
    }
    stopifnot(grepl("B: 1 creditos / 2600", output$comparacion, fixed = TRUE))
    anterior <- a$estado()$consulta
    fijar(session, "izquierda", minimo_texto = "1900.5", aplicar = 8L)
    stopifnot(identical(a$estado()$consulta, anterior), identical(b$estado(), b_guardada))
    fijar(session, "izquierda", corte = "2026-11-30", minimo_texto = "0", aplicar = 9L)
    stopifnot(a$estado()$tipo == "sin_universo", identical(b$estado(), b_guardada))
    writeLines(c(original, original[length(original)]), ruta, useBytes = TRUE)
    fijar(session, "izquierda", corte = "2026-09-30", aplicar = 10L)
    stopifnot(a$estado()$tipo == "fuente", identical(b$estado(), b_guardada))
    unlink(ruta); fijar(session, "izquierda", aplicar = 11L)
    stopifnot(a$estado()$tipo == "fuente", identical(b$estado(), b_guardada))
    stopifnot(grepl(basename(ruta), a$estado()$mensaje, fixed = TRUE))
    fijar(session, "derecha", aplicar = 2L)
    stopifnot(b$estado()$tipo == "fuente")
    writeLines(original, ruta, useBytes = TRUE)
    fijar(session, "izquierda", corte = "2026-09-30", segmentos = c("comercio", "servicios"), minimo_texto = "2000", aplicar = 12L)
    stopifnot(identical(a$estado()$consulta$indicadores$saldo_mxn, 4500), b$estado()$tipo == "fuente")
  })
})
entorno_min <- new.env(parent = globalenv())
minimo <- source("minimo.R", local = entorno_min, encoding = "UTF-8")$value
testServer(entorno_min$numeroServer, {
  session$setInputs(guardar = structure(0L, class = "shinyActionButtonValue"), numero = 2)
  stopifnot(is.null(guardado()))
  session$setInputs(numero = 3, guardar = 1L)
  stopifnot(identical(output$resultado, "Guardado: 3; doble: 6."))
  session$setInputs(numero = 7)
  stopifnot(identical(output$resultado, "Guardado: 3; doble: 6."))
})
testServer(minimo$serverFuncSource(), {
  for (id in c("uno", "dos")) fijar(session, id, guardar = structure(0L, class = "shinyActionButtonValue"), numero = 2)
  fijar(session, "uno", numero = 0, guardar = 1L)
  stopifnot(a() == 0, is.null(b()))
  fijar(session, "dos", numero = 7, guardar = 1L)
  stopifnot(a() == 0, b() == 7, identical(output$lectura_padre, "Padre: A=0; B=7."))
})
cat("Modulo local y dos instancias: siete consultas, API del padre, rechazo/bloqueo/recuperacion y namespace dinamico OK. UI por separado.\n")

# Autoría opcional: archivos temporales, ggplot_build y servidor; navegador aparte.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("cartera.R", encoding = "UTF-8"); source("consulta.R", encoding = "UTF-8")
source("presentacion.R", encoding = "UTF-8")
referencia <- data.frame(id_credito = rep(c("001", "002", "003"), 2),
  segmento = rep(c("comercio", "servicios", "comercio"), 2),
  fecha_corte = rep(c("2026-09-30", "2026-10-31"), each = 3), saldo_mxn = c(0, 2000, 2500, 100, 1900, 2600))
stopifnot(identical(leer_cartera(), referencia))
todos <- c("comercio", "servicios")
casos <- list(list("2026-09-30", todos, 2000, c("002", "003"), c(2000, 2500)),
  list("2026-10-31", todos, 2000, "003", 2600),
  list("2026-09-30", "comercio", 0, c("001", "003"), c(0, 2500)),
  list("2026-09-30", "comercio", 1, "003", 2500),
  list("2026-10-31", "servicios", 1900, "002", 1900),
  list("2026-10-31", "servicios", 1901, character(), numeric()),
  list("2026-09-30", character(), 0, character(), numeric()))
local({
  ruta <- tempfile(fileext = ".csv"); on.exit(unlink(ruta))
  for (caso in casos) {
    q <- crear_consulta(referencia, list(corte = caso[[1]], segmentos = caso[[2]], minimo_mxn = caso[[3]]))
    ref <- referencia[referencia$fecha_corte == caso[[1]] & referencia$id_credito %in% caso[[4]], , drop = FALSE]
    rownames(ref) <- NULL
    stopifnot(identical(q$seleccion, ref))
    escribir_seleccion(q, ruta)
    encabezado <- names(utils::read.csv(ruta, nrows = 0, check.names = FALSE, row.names = NULL))
    stopifnot(identical(encabezado, names(ref))) # No permitir un indice extra inferido como row.names.
    releido <- utils::read.csv(ruta, colClasses = c("character", "character", "character", "numeric"), check.names = FALSE)
    stopifnot(identical(releido, ref))
    escribir_contexto(q, ruta); contexto <- utils::read.csv(ruta, colClasses = "character", check.names = FALSE)
    stopifnot(contexto$corte == caso[[1]], as.numeric(contexto$minimo_mxn) == caso[[3]],
      as.numeric(contexto$creditos_universo) == 3, as.numeric(contexto$creditos_seleccion) == length(caso[[4]]),
      as.numeric(contexto$saldo_seleccion_mxn) == sum(caso[[5]]))
    if (nrow(ref) > 0L) {
      p <- crear_grafica(q); construido <- ggplot2::ggplot_build(p)
      stopifnot(identical(p$data, ref), identical(as.numeric(construido$data[[1]]$y), caso[[5]]),
        identical(as.character(construido$layout$panel_params[[1]]$x$get_labels()), caso[[4]]),
        identical(as.numeric(construido$data[[2]]$label), caso[[5]]), grepl(caso[[1]], descripcion_grafica(q), fixed = TRUE))
    } else stopifnot(inherits(try(crear_grafica(q), silent = TRUE), "try-error"))
  }
  # Una fila cero: escala valida, etiqueta 0 y no confundir con vacio.
  cero <- referencia[1, , drop = FALSE]
  q <- crear_consulta(cero, list(corte = "2026-09-30", segmentos = "comercio", minimo_mxn = 0))
  stopifnot(ggplot2::ggplot_build(crear_grafica(q))$data[[1]]$y == 0)
  ausente <- crear_consulta(referencia, list(corte = "2026-11-30", segmentos = todos, minimo_mxn = 0))
  stopifnot(inherits(try(escribir_seleccion(ausente, ruta), silent = TRUE), "try-error"),
    inherits(try(escribir_contexto(NULL, ruta), silent = TRUE), "try-error"))
})
app <- source("app.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(app$serverFuncSource(), {
  session$setInputs(aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30", segmentos = todos, minimo_texto = "2000", mostrar_tabla = TRUE)
  stopifnot(grepl("Descargas no disponibles", output$descargas$html, fixed = TRUE))
  session$setInputs(aplicar = 1L)
  consulta <- estado()$consulta
  stopifnot(grepl("csv_seleccion", output$descargas$html, fixed = TRUE))
  session$setInputs(corte = "2026-10-31")
  stopifnot(identical(estado()$consulta, consulta))
  session$setInputs(mostrar_tabla = FALSE)
  stopifnot(identical(estado()$consulta, consulta), grepl("csv_seleccion", output$descargas$html, fixed = TRUE))
  session$setInputs(aplicar = 2L)
  stopifnot(identical(output$resumen, "Creditos seleccionados: 1; saldo seleccionado: 2600 MXN."))
  session$setInputs(segmentos = NULL, aplicar = 3L)
  stopifnot(estado()$tipo == "vacio", grepl("csv_seleccion", output$descargas$html, fixed = TRUE))
  session$setInputs(corte = "2026-11-30", aplicar = 4L)
  stopifnot(grepl("Descargas no disponibles", output$descargas$html, fixed = TRUE))
})
cat("Siete consultas, grafica/etiquetas/alt, CSV releidos, contexto, cero/vacio y descargas por estado: OK. Navegador por separado.\n")

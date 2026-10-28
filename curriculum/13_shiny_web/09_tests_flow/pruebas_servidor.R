# Requiere las funciones y Shiny. Solo modifica un CSV temporal propio.
local({
  ruta <- tempfile(fileext = ".csv")
  on.exit(unlink(ruta))
  original <- readLines("cartera.csv", encoding = "UTF-8")
  writeLines(original, ruta, useBytes = TRUE)
  testServer(consultaServer, args = list(ruta = ruta), {
    session$setInputs(aplicar = structure(0L, class = "shinyActionButtonValue"),
      corte = "2026-09-30", segmentos = c("comercio", "servicios"),
      minimo_texto = "2000", mostrar_tabla = TRUE)
    stopifnot("Inicio sin consulta" = is.null(estado()$consulta))
    session$setInputs(aplicar = 1L)
    guardada <- estado()$consulta
    stopifnot("Septiembre" = identical(guardada$indicadores$saldo_mxn, 4500),
      "Salida septiembre" = identical(output$resumen, "Creditos seleccionados: 2; saldo seleccionado: 4500 MXN."))
    session$setInputs(corte = "2026-10-31")
    stopifnot("Editar no aplica" = identical(estado()$consulta, guardada),
      "Salida conserva consulta" = identical(output$resumen, "Creditos seleccionados: 2; saldo seleccionado: 4500 MXN."),
      "Avisa borrador" = grepl("pendientes", output$pendiente, fixed = TRUE))
    session$setInputs(aplicar = 2L)
    stopifnot("Octubre actualizado" = identical(estado()$consulta$indicadores$saldo_mxn, 2600),
      "Salida octubre" = identical(output$resumen, "Creditos seleccionados: 1; saldo seleccionado: 2600 MXN."))
    guardada <- estado()$consulta
    session$setInputs(mostrar_tabla = FALSE)
    stopifnot("Presentacion no altera datos" = identical(estado()$consulta, guardada))
    session$setInputs(minimo_texto = "1.5", aplicar = 3L)
    stopifnot("Rechazo conserva instantanea" = identical(estado()$consulta, guardada), estado()$tipo == "rechazo")
    session$setInputs(segmentos = character(), minimo_texto = "0", aplicar = 4L)
    stopifnot("Vacio sobre universo" = estado()$tipo == "vacio",
      identical(estado()$consulta$indicadores$saldo_mxn, 0),
      identical(estado()$consulta$indicadores$porcentaje_creditos, 0))
    session$setInputs(corte = "2026-11-30", aplicar = 5L)
    stopifnot("Sin universo no es cero por ciento" = estado()$tipo == "sin_universo",
      is.na(estado()$consulta$indicadores$porcentaje_creditos))
    writeLines(c(original, original[7]), ruta, useBytes = TRUE)
    session$setInputs(corte = "2026-09-30", segmentos = "comercio", aplicar = 6L)
    stopifnot("Duplicado de octubre bloquea septiembre" = estado()$tipo == "fuente", is.null(estado()$consulta))
    unlink(ruta); session$setInputs(aplicar = 7L)
    stopifnot("Ausencia bloquea" = estado()$tipo == "fuente", is.null(estado()$consulta))
    writeLines(original, ruta, useBytes = TRUE)
    session$setInputs(minimo_texto = "0", aplicar = 8L)
    stopifnot("Recuperacion con cero conocido" = estado()$tipo == "ok",
      identical(estado()$consulta$seleccion$id_credito, c("001", "003")),
      identical(estado()$consulta$seleccion$saldo_mxn, c(0, 2500)))
  })
  # Cada invocacion crea otra sesion simulada; no hereda consulta aplicada.
  testServer(consultaServer, args = list(ruta = ruta), {
    session$setInputs(corte = "2026-09-30", segmentos = "comercio", minimo_texto = "0")
    stopifnot("Sesion nueva" = is.null(estado()$consulta))
  })
})
local({
  # App real de 13.08 sin cambios. La UI se inspecciona, no se monta en navegador.
  entorno <- new.env(parent = globalenv())
  app <- source("app.R", local = entorno, encoding = "UTF-8")$value
  html <- htmltools::renderTags(entorno$ui)$html
  ids <- regmatches(html, gregexpr('(?<= id=")[^"]+', html, perl = TRUE))[[1]]
  stopifnot(!anyDuplicated(ids), all(c("izquierda-corte", "derecha-corte", "comparacion") %in% ids))
  fijar <- function(sesion, id, ...) {
    valores <- list(...); names(valores) <- paste0(id, "-", names(valores))
    do.call(sesion$setInputs, valores)
  }
  testServer(app, {
    for (id in c("izquierda", "derecha")) fijar(session, id,
      aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30",
      segmentos = c("comercio", "servicios"), minimo_texto = "2000", mostrar_tabla = TRUE)
    stopifnot(is.null(a$estado()$consulta), is.null(b$estado()$consulta))
    fijar(session, "izquierda", aplicar = 1L)
    guardada <- a$estado()
    fijar(session, "derecha", corte = "2026-10-31", aplicar = 1L)
    stopifnot("Instancias independientes" = identical(a$estado(), guardada),
      "API derecha" = identical(b$estado()$consulta$indicadores$saldo_mxn, 2600),
      "Padre" = identical(output$comparacion, "A: 2 creditos / 4500 MXN; B: 1 creditos / 2600 MXN. Cada consulta conserva su corte y denominador."),
      "Namespace dinamico A" = grepl("izquierda-csv_seleccion", output[["izquierda-descargas"]]$html, fixed = TRUE),
      "Namespace dinamico B" = grepl("derecha-csv_contexto", output[["derecha-descargas"]]$html, fixed = TRUE))
  })
})
cat("OK servidor: inicio, editar/aplicar, rechazo, vacio, bloqueo y recuperacion.\n")

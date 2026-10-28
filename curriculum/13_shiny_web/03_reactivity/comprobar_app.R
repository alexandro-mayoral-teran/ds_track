# Apoyo opcional de autoria. No monta la UI ni sustituye navegador/IDE (13.09).
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("ventas.R", encoding = "UTF-8")
esperadas <- data.frame(
  venta_id = c("V001", "V002", "V003", "V004"), unidades = c(4L, 2L, 0L, 3L),
  precio_mxn = c(75L, 120L, 50L, 40L), importe_mxn = c(300L, 240L, 0L, 120L),
  stringsAsFactors = FALSE
)
stopifnot(identical(crear_ventas(), esperadas))
entorno <- new.env(parent = globalenv())
app <- source("app.R", local = entorno, encoding = "UTF-8")$value
# Instrumentacion no reactiva y solo de prueba; cuenta la funcion de datos real.
original <- entorno$consultar_venta
llamadas <- 0L
entorno$consultar_venta <- function(ventas, clave) {
  llamadas <<- llamadas + 1L
  original(ventas, clave)
}
celdas <- function(html) {
  if (is.null(html)) return(character())
  etiquetas <- regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]]
  trimws(gsub("</?td[^>]*>", "", etiquetas, perl = TRUE))
}
shiny::testServer(app$serverFuncSource(), {
  session$setInputs(venta_elegida = "todas", mostrar_detalle = TRUE, nota = "Inicio")
  for (clave in c("todas", "V001", "V002", "V003", "V004")) {
    session$setInputs(venta_elegida = clave)
    ref <- if (clave == "todas") esperadas else esperadas[esperadas$venta_id == clave, , drop = FALSE]
    texto <- paste0("Ventas consultadas: ", nrow(ref), "; importe consultado ", sum(ref$importe_mxn), " MXN.")
    stopifnot(identical(output$resumen_venta, texto))
    valores <- unlist(lapply(seq_len(nrow(ref)), function(i) as.character(unlist(ref[i, ], use.names = FALSE))), use.names = FALSE)
    stopifnot(identical(celdas(output$detalle_venta), valores))
    antes <- llamadas
    # Dos lecturas adicionales del mismo reactive no repiten la funcion.
    stopifnot(identical(consulta(), ref), identical(consulta(), ref), llamadas == antes)
    session$setInputs(nota = paste0("Nota ", clave))
    stopifnot(identical(output$eco, paste0("Nota: Nota ", clave)), llamadas == antes)
    session$setInputs(mostrar_detalle = FALSE)
    stopifnot(length(celdas(output$detalle_venta)) == 0L, identical(output$resumen_venta, texto), llamadas == antes)
    session$setInputs(mostrar_detalle = TRUE)
    stopifnot(identical(celdas(output$detalle_venta), valores), llamadas == antes)
  }
  antes <- llamadas
  session$setInputs(venta_elegida = "V003")
  stopifnot(identical(output$resumen_venta, "Ventas consultadas: 1; importe consultado 0 MXN."), llamadas == antes + 1L)
})

# Sesion nueva: el reactive no reutiliza la cache de la sesion anterior.
antes <- llamadas
shiny::testServer(app$serverFuncSource(), {
  session$setInputs(venta_elegida = "V003", mostrar_detalle = TRUE)
  stopifnot(identical(output$resumen_venta, "Ventas consultadas: 1; importe consultado 0 MXN."))
})
stopifnot(llamadas == antes + 1L)

minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(minimo$serverFuncSource(), {
  session$setInputs(numero = 2, mostrar = TRUE, nota = "Inicio")
  for (n in c(0, 2, 3, 10)) {
    session$setInputs(numero = n)
    stopifnot(identical(output$resultado, paste0("Doble: ", n * 2)))
  }
  session$setInputs(mostrar = FALSE)
  stopifnot(identical(output$resultado, "Consulta desactivada."))
  session$setInputs(numero = 7, nota = "Oculto")
  stopifnot(identical(output$resultado, "Consulta desactivada."), identical(output$eco, "Nota: Oculto"))
  session$setInputs(mostrar = TRUE)
  stopifnot(identical(output$resultado, "Doble: 14"))
})

# Sonda sin outputs: demanda manual para separar invalidacion de ejecucion.
# isolate es solo instrumentacion aqui; no se introduce como solucion de la app.
ejecuciones <- 0L
shiny::testServer(function(input, output, session) {
  doble <- shiny::reactive({ ejecuciones <<- ejecuciones + 1L; input$numero * 2 })
  rama <- shiny::reactive({ if (isTRUE(input$mostrar)) doble() else -1 })
}, {
  session$setInputs(numero = 2, mostrar = TRUE)
  stopifnot(ejecuciones == 0L)
  stopifnot(shiny::isolate(rama()) == 4, ejecuciones == 1L)
  stopifnot(shiny::isolate(rama()) == 4, ejecuciones == 1L)
  session$setInputs(numero = 3)
  stopifnot(ejecuciones == 1L) # Invalidado; nadie ha pedido el resultado nuevo.
  stopifnot(shiny::isolate(rama()) == 6, ejecuciones == 2L)
  session$setInputs(mostrar = FALSE)
  stopifnot(shiny::isolate(rama()) == -1, ejecuciones == 2L)
  session$setInputs(numero = 8)
  stopifnot(shiny::isolate(rama()) == -1, ejecuciones == 2L)
  session$setInputs(mostrar = TRUE)
  stopifnot(shiny::isolate(rama()) == 16, ejecuciones == 3L)
})
cat("Cinco consultas por campo, cache por sesion, ramas, minimo e invalidacion sin demanda: OK. UI por separado.\n")

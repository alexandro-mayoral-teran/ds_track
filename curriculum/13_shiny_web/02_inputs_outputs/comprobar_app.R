# Apoyo de autoria, no leccion de pruebas 13.09 ni sustituto del navegador/IDE.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("ventas.R", encoding = "UTF-8")

esperadas <- data.frame(
  venta_id = c("V001", "V002", "V003", "V004"), unidades = c(4L, 2L, 0L, 3L),
  precio_mxn = c(75L, 120L, 50L, 40L), importe_mxn = c(300L, 240L, 0L, 120L),
  stringsAsFactors = FALSE
)
ventas_base <- crear_ventas()
stopifnot(identical(ventas_base, esperadas))
stopifnot(identical(consultar_venta(ventas_base, "todas"), esperadas))
for (i in seq_len(4L)) {
  stopifnot(identical(consultar_venta(ventas_base, esperadas$venta_id[i]), esperadas[i, , drop = FALSE]))
}
for (clave in list(NULL, NA_character_, "", "V999", 1, c("V001", "V002"))) {
  stopifnot(inherits(try(consultar_venta(ventas_base, clave), silent = TRUE), "try-error"))
}
consulta <- consultar_venta(ventas_base, "V001")
consulta$importe_mxn <- 999L
stopifnot(identical(ventas_base, esperadas))

celdas <- function(html) {
  if (is.null(html)) return(character())
  etiquetas <- regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]]
  trimws(gsub("</?td[^>]*>", "", etiquetas, perl = TRUE))
}

app <- source("app.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
stopifnot(inherits(app, "shiny.appobj"))
shiny::testServer(app$serverFuncSource(), {
  # testServer no monta la UI: hay que indicar los valores de entrada.
  session$flushReact()
  stopifnot(!nzchar(paste(output$resumen_venta, collapse = "")), length(celdas(output$detalle_venta)) == 0L)
  for (clave in c("todas", "V001", "V002", "V003", "V004")) {
    session$setInputs(venta_elegida = clave, mostrar_detalle = TRUE)
    indices <- if (clave == "todas") 1:4 else match(clave, esperadas$venta_id)
    referencia <- esperadas[indices, , drop = FALSE]
    texto <- paste0("Valor recibido: ", clave, ". Ventas consultadas: ", nrow(referencia),
                    "; importe consultado ", sum(referencia$importe_mxn), " MXN.")
    stopifnot(identical(output$resumen_venta, texto))
    valores <- unlist(lapply(seq_len(nrow(referencia)), function(i) as.character(unlist(referencia[i, ], use.names = FALSE))), use.names = FALSE)
    stopifnot(identical(celdas(output$detalle_venta), valores))
    session$setInputs(mostrar_detalle = FALSE)
    stopifnot(identical(output$resumen_venta, texto), length(celdas(output$detalle_venta)) == 0L)
    session$setInputs(mostrar_detalle = TRUE)
    stopifnot(identical(celdas(output$detalle_venta), valores))
  }
})

minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(minimo$serverFuncSource(), {
  for (texto in c("Ventas", "Otra nota", "", "<b>ventas</b>")) {
    session$setInputs(mensaje = texto)
    stopifnot(identical(output$eco, paste0("Texto recibido: ", texto)))
  }
})
cat("Funciones, cinco consultas, ocultar/recuperar y eco de texto: OK. Revisar UI/navegador por separado.\n")

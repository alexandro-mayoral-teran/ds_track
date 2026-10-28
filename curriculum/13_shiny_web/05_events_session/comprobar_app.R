# Apoyo de autoria: fija entradas, no monta UI. Tema de pruebas: 13.09.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("cartera.R", encoding = "UTF-8")
source("consulta.R", encoding = "UTF-8")
referencia <- data.frame(id_credito = rep(c("001", "002", "003"), 2),
  segmento = rep(c("comercio", "servicios", "comercio"), 2),
  fecha_corte = rep(c("2026-09-30", "2026-10-31"), each = 3), saldo_mxn = c(0, 2000, 2500, 100, 1900, 2600))
stopifnot(identical(leer_cartera(), referencia))
todos <- c("comercio", "servicios")
casos <- list(
  list("2026-09-30", todos, 2000, c("002", "003"), 4500),
  list("2026-10-31", todos, 2000, "003", 2600),
  list("2026-09-30", "comercio", 0, c("001", "003"), 2500),
  list("2026-09-30", "comercio", 1, "003", 2500),
  list("2026-10-31", "servicios", 1900, "002", 1900),
  list("2026-10-31", "servicios", 1901, character(), 0),
  list("2026-09-30", character(), 0, character(), 0)
)
celdas <- function(html) {
  if (is.null(html)) return(character())
  trimws(gsub("</?td[^>]*>", "", regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]], perl = TRUE))
}
entorno <- new.env(parent = globalenv())
app <- source("app.R", local = entorno, encoding = "UTF-8")$value
shiny::testServer(app$serverFuncSource(), {
  # testServer no obtiene estos valores de la UI: dar 0 con la clase real del boton.
  session$setInputs(aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30", segmentos = todos, minimo_mxn = 2000, mostrar_tabla = TRUE)
  stopifnot(is.null(aplicada()), identical(output$contexto, "Consulta aplicada: ninguna."))
  for (i in seq_along(casos)) {
    caso <- casos[[i]]
    anterior <- aplicada()
    contexto_anterior <- output$contexto
    session$setInputs(corte = caso[[1]], segmentos = if (length(caso[[2]]) == 0L) NULL else caso[[2]], minimo_mxn = caso[[3]])
    stopifnot(identical(aplicada(), anterior)) # Editar no aplica.
    stopifnot(identical(output$contexto, contexto_anterior))
    session$setInputs(aplicar = i)
    esperado <- referencia[referencia$fecha_corte == caso[[1]] & referencia$id_credito %in% caso[[4]], , drop = FALSE]
    guardada <- aplicada()
    stopifnot(identical(guardada$seleccion$id_credito, caso[[4]]), guardada$indicadores$saldo_mxn == caso[[5]])
    valores <- unlist(lapply(seq_len(nrow(esperado)), function(j) as.character(unlist(esperado[j, ], use.names = FALSE))), use.names = FALSE)
    if (length(valores) == 0L) valores <- character()
    stopifnot(identical(celdas(output$tabla), valores))
    stopifnot(identical(output$resumen, paste0("Creditos seleccionados: ", length(caso[[4]]), "; saldo seleccionado: ", caso[[5]], " MXN.")))
    porcentaje <- formatC(100 * length(caso[[4]]) / 3, format = "f", digits = 2, decimal.mark = ".")
    stopifnot(identical(output$cobertura, paste0("Cobertura: ", length(caso[[4]]), " de 3 creditos del corte (", porcentaje, "%).")))
    stopifnot(identical(output$estado, "Borrador: coincide con la consulta aplicada."))
    session$setInputs(mostrar_tabla = FALSE)
    stopifnot(identical(aplicada(), guardada), length(celdas(output$tabla)) == 0L)
    session$setInputs(mostrar_tabla = TRUE)
    stopifnot(identical(aplicada(), guardada), identical(celdas(output$tabla), valores))
  }
  anterior <- aplicada()
  session$setInputs(minimo_mxn = 1900.5, aplicar = 8L)
  stopifnot(identical(aplicada(), anterior), grepl("No se aplico:", output$aviso, fixed = TRUE))
  session$setInputs(minimo_mxn = 0, aplicar = 9L)
  stopifnot(identical(output$aviso, "Consulta aplicada. Puedes preparar otro borrador."))
  guardada <- aplicada()
  session$setInputs(aplicar = 10L) # Misma consulta: accion nueva, contenido igual.
  stopifnot(identical(aplicada(), guardada))
})
shiny::testServer(app$serverFuncSource(), {
  session$setInputs(aplicar = structure(0L, class = "shinyActionButtonValue"), corte = "2026-09-30", segmentos = todos, minimo_mxn = 2000)
  stopifnot(is.null(aplicada()), identical(output$resumen, "Pulsa Aplicar filtros para consultar."))
})
minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(minimo$serverFuncSource(), {
  session$setInputs(guardar = structure(0L, class = "shinyActionButtonValue"), numero = 2)
  stopifnot(identical(output$resultado, "Sin numero guardado."))
  session$setInputs(numero = 3)
  stopifnot(is.null(guardado()))
  session$setInputs(guardar = 1L)
  stopifnot(identical(output$resultado, "Guardado: 3; doble: 6."))
  session$setInputs(numero = 7)
  stopifnot(identical(output$resultado, "Guardado: 3; doble: 6."))
  session$setInputs(guardar = 2L)
  stopifnot(identical(output$resultado, "Guardado: 7; doble: 14."))
  session$setInputs(numero = 0, guardar = 3L)
  stopifnot(identical(output$resultado, "Guardado: 0; doble: 0."))
})
cat("Siete consultas por campo, borrador/aplicacion, rechazo sin reemplazo, sesion nueva y minimo: OK. UI por separado.\n")

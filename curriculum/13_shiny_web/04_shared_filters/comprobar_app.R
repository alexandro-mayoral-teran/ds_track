# Apoyo de autoria; no monta la UI ni reemplaza navegador/IDE. Pruebas como tema: 13.09.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
source("cartera.R", encoding = "UTF-8")
referencia <- data.frame(id_credito = rep(c("001", "002", "003"), 2),
  segmento = rep(c("comercio", "servicios", "comercio"), 2),
  fecha_corte = rep(c("2026-09-30", "2026-10-31"), each = 3),
  saldo_mxn = c(0, 2000, 2500, 100, 1900, 2600), stringsAsFactors = FALSE)
stopifnot(identical(leer_cartera(), referencia))
todos <- c("comercio", "servicios")
# Corte, segmentos, minimo, IDs esperados, suma esperada (expectativas explicitas).
casos <- list(
  list("2026-09-30", todos, 2000, c("002", "003"), 4500),
  list("2026-10-31", todos, 2000, "003", 2600),
  list("2026-09-30", todos, 0, c("001", "002", "003"), 4500),
  list("2026-10-31", todos, 0, c("001", "002", "003"), 4600),
  list("2026-09-30", "comercio", 0, c("001", "003"), 2500),
  list("2026-09-30", "comercio", 1, "003", 2500),
  list("2026-10-31", "servicios", 1900, "002", 1900),
  list("2026-10-31", "servicios", 1901, character(), 0),
  list("2026-09-30", todos, 2500, "003", 2500),
  list("2026-09-30", todos, 2501, character(), 0),
  list("2026-09-30", character(), 0, character(), 0),
  list("2026-10-31", todos, 1000000, character(), 0)
)
for (caso in casos) {
  universo <- seleccionar_corte(referencia, caso[[1]])
  seleccion <- filtrar_seleccion(universo, caso[[2]], caso[[3]])
  stopifnot(identical(seleccion$id_credito, caso[[4]]))
  medidas <- resumir_seleccion(seleccion, nrow(universo))
  stopifnot(medidas$cantidad == length(caso[[4]]), medidas$saldo_mxn == caso[[5]],
            medidas$porcentaje_creditos == 100 * length(caso[[4]]) / 3)
}
vacio <- referencia[FALSE, , drop = FALSE]
stopifnot(identical(seleccionar_corte(referencia, "2026-11-30"), vacio),
          is.na(resumir_seleccion(vacio, 0)$porcentaje_creditos))
antes <- referencia
filas <- filtrar_seleccion(seleccionar_corte(referencia, "2026-09-30"), todos, 0)
filas$saldo_mxn[1] <- 99
stopifnot(identical(referencia, antes))
falla <- function(expr) stopifnot(inherits(try(force(expr), silent = TRUE), "try-error"))
for (minimo in list(NA_real_, Inf, -1, 0.5, 1000001, "2000", TRUE, numeric(), c(0, 1))) {
  falla(filtrar_seleccion(vacio, todos, minimo))
}
for (segmentos in list(NULL, NA_character_, "otro", c("comercio", "comercio"), 1)) {
  falla(filtrar_seleccion(vacio, segmentos, 0))
}
for (fecha in c("2026-02-30", "2026-2-01", "1899-12-31", "2101-01-01")) falla(seleccionar_corte(referencia, fecha))
falla(seleccionar_corte(rbind(referencia, referencia[6, ]), "2026-09-30"))
alterada <- referencia; alterada$saldo_mxn[6] <- NA_real_
falla(seleccionar_corte(alterada, "2026-09-30")) # Incidencia fuera del corte solicitado.
falla(resumir_seleccion(referencia, 6)) # Dos cortes no forman un denominador de creditos a una fecha.

celdas <- function(html) {
  if (is.null(html)) return(character())
  trimws(gsub("</?td[^>]*>", "", regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]], perl = TRUE))
}
entorno <- new.env(parent = globalenv())
app <- source("app.R", local = entorno, encoding = "UTF-8")$value
llamadas <- 0L; original <- entorno$filtrar_seleccion
entorno$filtrar_seleccion <- function(...) { llamadas <<- llamadas + 1L; original(...) }
shiny::testServer(app$serverFuncSource(), {
  for (caso in casos) {
    session$setInputs(corte = caso[[1]], segmentos = if (length(caso[[2]]) == 0) NULL else caso[[2]],
                     minimo_mxn = caso[[3]], mostrar_tabla = TRUE)
    stopifnot(identical(output$resumen, paste0("Creditos seleccionados: ", length(caso[[4]]), "; saldo seleccionado: ", caso[[5]], " MXN.")))
    porcentaje <- formatC(100 * length(caso[[4]]) / 3, format = "f", digits = 2, decimal.mark = ".")
    stopifnot(identical(output$cobertura, paste0("Cobertura: ", length(caso[[4]]), " de 3 creditos del corte (", porcentaje, "%).")))
    ref <- referencia[referencia$fecha_corte == caso[[1]] & referencia$id_credito %in% caso[[4]], , drop = FALSE]
    valores <- unlist(lapply(seq_len(nrow(ref)), function(i) as.character(unlist(ref[i, ], use.names = FALSE))), use.names = FALSE)
    if (length(valores) == 0L) valores <- character()
    stopifnot(identical(celdas(output$tabla), valores))
    numero <- llamadas
    session$setInputs(mostrar_tabla = FALSE)
    stopifnot(length(celdas(output$tabla)) == 0L, llamadas == numero)
    session$setInputs(mostrar_tabla = TRUE)
    stopifnot(identical(celdas(output$tabla), valores), llamadas == numero)
  }
})
minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
shiny::testServer(minimo$serverFuncSource(), {
  for (caso in list(c(2000, 2, 4500), c(2001, 1, 2500), c(0, 3, 4500), c(2501, 0, 0))) {
    session$setInputs(minimo = caso[1])
    stopifnot(identical(output$resumen, paste0(caso[2], " creditos; ", caso[3], " MXN.")))
  }
})
cat("Doce escenarios por clave/campo, fronteras, fuente completa, cache y minimo: OK. UI por separado.\n")

# Apoyo opcional de autoria. No instala, abre navegador ni certifica el IDE.
if (!file.exists(".Rprofile")) stop("Ejecuta desde la copia preparada.")
source(".Rprofile")
app <- source("app.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
stopifnot(inherits(app, "shiny.appobj"))
minimo <- source("minimo.R", local = new.env(parent = globalenv()), encoding = "UTF-8")$value
stopifnot(inherits(minimo, "shiny.appobj"))

# Oraculo explicito: filas y valores manuales, no otra llamada al mismo calculo.
servidor <- app$serverFuncSource()
shiny::testServer(servidor, {
  session$flushReact()
  stopifnot(identical(output$resumen_ventas, "4 ventas; total 660 MXN."))
  html <- output$detalle_ventas
  celdas <- regmatches(html, gregexpr("<td[^>]*>[^<]*</td>", html, perl = TRUE))[[1]]
  valores <- trimws(gsub("</?td[^>]*>", "", celdas, perl = TRUE))
  stopifnot(identical(valores, c("V001", "4", "75", "300", "V002", "2", "120", "240",
                               "V003", "0", "50", "0", "V004", "3", "40", "120")))
})

entorno <- new.env(parent = globalenv())
invisible(source("app.R", local = entorno, encoding = "UTF-8"))
esperado <- data.frame(
  venta_id = c("V001", "V002", "V003", "V004"), unidades = c(4L, 2L, 0L, 3L),
  precio_mxn = c(75L, 120L, 50L, 40L), importe_mxn = c(300L, 240L, 0L, 120L),
  stringsAsFactors = FALSE
)
stopifnot(identical(entorno$ventas, esperado))
cat("Objetos app, resumen y cuatro filas de referencia: OK. Revisar navegador por separado.\n")

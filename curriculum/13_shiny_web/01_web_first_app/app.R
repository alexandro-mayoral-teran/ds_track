# Ventas sinteticas incluidas: no lee ni escribe archivos de datos personales.
library(shiny)

# Preparacion al cargar esta app en el proceso R. Se consulta, no se modifica por sesion.
ventas <- data.frame(
  venta_id = c("V001", "V002", "V003", "V004"),
  unidades = c(4L, 2L, 0L, 3L),
  precio_mxn = c(75L, 120L, 50L, 40L),
  stringsAsFactors = FALSE
)
ventas$importe_mxn <- ventas$unidades * ventas$precio_mxn
cat("[13.01] Preparacion: 4 ventas; total ", sum(ventas$importe_mxn), " MXN.\n", sep = "")

ui <- fluidPage(
  title = "DS Track - primera app Shiny",
  h1("Ventas: una primera app Shiny"),
  p("Cuatro ventas ficticias. Cada fila es una venta; los importes se expresan en pesos mexicanos."),
  h2("Resultado calculado en R"),
  textOutput("resumen_ventas"),
  h2("Detalle de las cuatro ventas"),
  tableOutput("detalle_ventas"),
  p("La venta V003 tiene cero unidades conocido: sigue incluida en las cuatro filas."),
  p("Esta app aun no tiene filtros. Recargar crea otra sesion; detener el proceso R interrumpe la conexion."),
  lang = "es"
)

server <- function(input, output, session) {
  cat("[13.01] Sesion abierta: se define el comportamiento de sus salidas.\n")
  output$resumen_ventas <- renderText({
    cat("[13.01] Calculo de resumen para una salida.\n")
    paste0(nrow(ventas), " ventas; total ", sum(ventas$importe_mxn), " MXN.")
  })
  output$detalle_ventas <- renderTable({
    # Cambian etiquetas de presentacion, no los datos de ventas.
    setNames(ventas, c("Venta", "Unidades", "Precio (MXN)", "Importe (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
}

shinyApp(ui = ui, server = server)

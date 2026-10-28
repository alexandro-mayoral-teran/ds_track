library(shiny)
source("ventas.R", local = TRUE, encoding = "UTF-8")

# Datos de 13.01 conservados; ninguna sesion modifica esta tabla.
ventas <- crear_ventas()
opciones_venta <- c("Todas las ventas" = "todas", setNames(ventas$venta_id, ventas$venta_id))

ui <- fluidPage(
  title = "DS Track - entradas y salidas",
  h1("Consultar una venta"),
  p("Cuatro ventas ficticias de referencia: 660 MXN en total. El selector consulta una venta o las cuatro."),
  selectInput("venta_elegida", "Venta para consultar", choices = opciones_venta,
              selected = "todas", multiple = FALSE, selectize = FALSE),
  checkboxInput("mostrar_detalle", "Mostrar detalle de la consulta", value = TRUE),
  h2("Resultado de la consulta"),
  textOutput("resumen_venta"),
  tableOutput("detalle_venta"),
  p("Ocultar el detalle no cambia la consulta ni su importe. V003 es una venta con cero conocido."),
  p("Los cambios de estos controles actualizan las salidas sin un boton de envio."),
  lang = "es"
)

server <- function(input, output, session) {
  output$resumen_venta <- renderText({
    if (is.null(input$venta_elegida)) return(NULL)
    consulta <- consultar_venta(ventas, input$venta_elegida)
    paste0("Valor recibido: ", input$venta_elegida, ". Ventas consultadas: ", nrow(consulta),
           "; importe consultado ", sum(consulta$importe_mxn), " MXN.")
  })

  output$detalle_venta <- renderTable({
    if (is.null(input$venta_elegida) || !isTRUE(input$mostrar_detalle)) return(NULL)
    consulta <- consultar_venta(ventas, input$venta_elegida)
    setNames(consulta, c("Venta", "Unidades", "Precio (MXN)", "Importe (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
}

shinyApp(ui = ui, server = server)

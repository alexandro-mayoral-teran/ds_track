library(shiny)
source("ventas.R", local = TRUE, encoding = "UTF-8")

# Fuente inmutable compartida; la expresion reactiva nace dentro de cada sesion.
ventas <- crear_ventas()
opciones <- c("Todas las ventas" = "todas", setNames(ventas$venta_id, ventas$venta_id))
ui <- fluidPage(
  title = "DS Track - modelo de reactividad",
  h1("Una consulta, dos salidas"),
  p("Cuatro ventas ficticias: 300, 240, 0 y 120 MXN; total 660 MXN."),
  selectInput("venta_elegida", "Venta para consultar", choices = opciones,
              selected = "todas", selectize = FALSE),
  checkboxInput("mostrar_detalle", "Mostrar detalle de la consulta", value = TRUE),
  textInput("nota", "Nota independiente", value = "Mi prediccion"),
  h2("Resultado"),
  textOutput("resumen_venta"),
  tableOutput("detalle_venta"),
  textOutput("eco"),
  p("La nota no modifica la consulta. Ocultar el detalle conserva el resumen y la venta elegida."),
  p("La consola R muestra [consulta], [resumen], [detalle] y [observador]. Su orden no es un contrato."),
  lang = "es"
)

server <- function(input, output, session) {
  consulta <- reactive({
    if (is.null(input$venta_elegida)) return(NULL)
    message("[consulta] venta=", input$venta_elegida)
    consultar_venta(ventas, input$venta_elegida)
  }, label = "consulta")

  output$resumen_venta <- renderText({
    message("[resumen] solicitar consulta")
    datos <- consulta()
    if (is.null(datos)) return(NULL)
    paste0("Ventas consultadas: ", nrow(datos), "; importe consultado ",
           sum(datos$importe_mxn), " MXN.")
  })
  output$detalle_venta <- renderTable({
    message("[detalle] evaluar rama")
    if (!isTRUE(input$mostrar_detalle)) return(NULL)
    datos <- consulta()
    if (is.null(datos)) return(NULL)
    setNames(datos, c("Venta", "Unidades", "Precio (MXN)", "Importe (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
  output$eco <- renderText({ paste0("Nota: ", input$nota) })

  # Efecto de diagnostico, sin asignar datos ni producir un valor para las salidas.
  observe({
    message("[observador] detalle=", isTRUE(input$mostrar_detalle))
  }, label = "aviso_detalle")
}

shinyApp(ui, server)

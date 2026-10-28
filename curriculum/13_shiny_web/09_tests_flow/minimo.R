library(shiny)

dobleUI <- function(id) {
  ns <- NS(id)
  tagList(numericInput(ns("numero"), "Numero entero (0 a 10)", 3, min = 0, max = 10, step = 1),
    textInput(ns("nota"), "Nota independiente", ""),
    textOutput(ns("resultado")), textOutput(ns("eco")))
}

dobleServer <- function(id) {
  moduleServer(id, function(input, output, session) {
    doble <- reactive({
      req(is.numeric(input$numero), length(input$numero) == 1L,
        is.finite(input$numero), input$numero >= 0, input$numero <= 10,
        input$numero == floor(input$numero))
      message("[doble] calcular numero=", input$numero)
      input$numero * 2
    }, label = "doble didactico")
    output$resultado <- renderText({ paste0("Doble: ", doble(), ".") })
    output$eco <- renderText({ paste0("Nota: ", input$nota) })
    list(doble = doble)
  })
}

ui <- fluidPage(lang = "es", titlePanel("13.09: observar y comprobar"), dobleUI("ejemplo"))
server <- function(input, output, session) { a <- dobleServer("ejemplo") }
shinyApp(ui, server)

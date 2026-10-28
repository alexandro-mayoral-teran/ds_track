library(shiny)

ui <- fluidPage(
  h1("Una entrada y una salida"),
  textInput("mensaje", "Mensaje del ejemplo", value = "Ventas"),
  textOutput("eco"),
  p("Escribe un texto de ejemplo. No necesitas introducir datos personales."),
  lang = "es"
)

server <- function(input, output, session) {
  output$eco <- renderText({
    if (is.null(input$mensaje)) return(NULL)
    paste0("Texto recibido: ", input$mensaje)
  })
}

shinyApp(ui = ui, server = server)

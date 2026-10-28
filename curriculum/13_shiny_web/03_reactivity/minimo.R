library(shiny)

ui <- fluidPage(
  title = "DS Track - numero y doble",
  h1("Numero y doble"),
  numericInput("numero", "Numero del ejemplo", value = 2, min = 0, max = 10, step = 1),
  checkboxInput("mostrar", "Consultar el doble", value = TRUE),
  textOutput("resultado"),
  textInput("nota", "Nota independiente", value = "Mi prediccion"),
  textOutput("eco"),
  p("Observa las marcas [doble] y [resultado] en la consola R. Desmarca, cambia el numero y vuelve a marcar."),
  lang = "es"
)

server <- function(input, output, session) {
  doble <- reactive({
    if (is.null(input$numero)) return(NULL)
    message("[doble] numero=", input$numero)
    2 * input$numero
  }, label = "doble")

  output$resultado <- renderText({
    message("[resultado] evaluar rama")
    # La rama desmarcada termina ANTES de leer doble().
    if (!isTRUE(input$mostrar)) return("Consulta desactivada.")
    valor <- doble()
    if (is.null(valor)) return(NULL)
    paste0("Doble: ", valor)
  })
  output$eco <- renderText({ paste0("Nota: ", input$nota) })
}

shinyApp(ui, server)

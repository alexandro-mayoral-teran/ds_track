library(shiny)
ui <- fluidPage(
  title = "DS Track - guardar un numero",
  h1("Un numero editado y uno guardado"),
  numericInput("numero", "Numero del borrador", value = 2, min = 0, max = 10, step = 1),
  actionButton("guardar", "Guardar numero"),
  textOutput("borrador"), textOutput("resultado"), lang = "es"
)
server <- function(input, output, session) {
  guardado <- reactiveVal(NULL)
  bindEvent(observe({
    numero <- input$numero
    if (length(numero) != 1L || is.na(numero) || !is.finite(numero) || numero < 0 || numero > 10 || numero != floor(numero)) return(invisible(NULL))
    guardado(numero)
  }), input$guardar, ignoreNULL = TRUE, ignoreInit = TRUE)
  output$borrador <- renderText({ paste0("Borrador: ", input$numero) })
  output$resultado <- renderText({
    valor <- guardado()
    if (is.null(valor)) return("Sin numero guardado.")
    paste0("Guardado: ", valor, "; doble: ", valor * 2, ".")
  })
}
shinyApp(ui, server)

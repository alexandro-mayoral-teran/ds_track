library(shiny)
# Mini muestra completa: un solo corte, dos salidas y ningun archivo externo.
datos <- data.frame(credito = c("001", "002", "003"), saldo_mxn = c(0, 2000, 2500))
ui <- fluidPage(
  title = "DS Track - una seleccion",
  h1("Una seleccion para dos salidas"),
  numericInput("minimo", "Saldo minimo incluido", value = 2000, min = 0, max = 1000000, step = 1),
  textOutput("resumen"), tableOutput("tabla"), lang = "es"
)
server <- function(input, output, session) {
  seleccion <- reactive({
    if (is.null(input$minimo)) return(NULL)
    datos[datos$saldo_mxn >= input$minimo, , drop = FALSE]
  })
  output$resumen <- renderText({
    filas <- seleccion()
    if (is.null(filas)) return(NULL)
    paste0(nrow(filas), " creditos; ", sum(filas$saldo_mxn), " MXN.")
  })
  output$tabla <- renderTable({ seleccion() }, rownames = FALSE, digits = 0)
}
shinyApp(ui, server)

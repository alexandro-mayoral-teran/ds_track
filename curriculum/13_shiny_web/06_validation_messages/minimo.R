library(shiny)
datos <- data.frame(credito = c("001", "002", "003"), saldo_mxn = c(0, 2000, 2500))
ui <- fluidPage(title = "DS Track - req validate need", h1("Requerir y explicar"),
  textInput("minimo", "Saldo minimo (texto)", value = "2000"),
  textOutput("valor"), tableOutput("tabla"), lang = "es")
server <- function(input, output, session) {
  minimo <- reactive({
    req(!is.null(input$minimo)) # Inicio transitorio, sin mensaje de error.
    validate(need(nzchar(input$minimo), "Escribe un minimo; 0 incluye el saldo cero."),
             need(grepl("^(0|[1-9][0-9]*)$", input$minimo), "Usa digitos enteros sin signos, espacios ni decimales."))
    valor <- as.numeric(input$minimo)
    validate(need(is.finite(valor) && valor <= 1000000, "Usa de 0 a 1000000 MXN."))
    valor
  })
  output$valor <- renderText({ paste0("Minimo valido: ", minimo(), " MXN.") })
  output$tabla <- renderTable({
    seleccion <- datos[datos$saldo_mxn >= minimo(), , drop = FALSE]
    validate(need(nrow(seleccion) > 0L, "No hay coincidencias; baja el minimo."))
    seleccion
  }, rownames = FALSE, digits = 0)
}
shinyApp(ui, server)

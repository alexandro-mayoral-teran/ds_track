library(shiny)
numeroUI <- function(id, titulo) {
  ns <- NS(id)
  tagList(h2(titulo), numericInput(ns("numero"), "Numero del borrador", 2, min = 0, max = 10, step = 1),
    actionButton(ns("guardar"), "Guardar numero"), textOutput(ns("resultado")))
}
numeroServer <- function(id) {
  moduleServer(id, function(input, output, session) {
    guardado <- reactiveVal(NULL)
    bindEvent(observe({
      n <- input$numero
      if (length(n) != 1L || is.na(n) || !is.finite(n) || n < 0 || n > 10 || n != floor(n)) return(invisible(NULL))
      guardado(n)
    }), input$guardar, ignoreNULL = TRUE, ignoreInit = TRUE)
    output$resultado <- renderText({
      valor <- guardado()
      if (is.null(valor)) return("Sin numero guardado.")
      paste0("Guardado: ", valor, "; doble: ", valor * 2, ".")
    })
    reactive(guardado())
  })
}
ui <- fluidPage(title = "DS Track - dos instancias", h1("Reutilizar sin mezclar"),
  numeroUI("uno", "Numero A"), numeroUI("dos", "Numero B"), textOutput("lectura_padre"), lang = "es")
server <- function(input, output, session) {
  a <- numeroServer("uno"); b <- numeroServer("dos")
  output$lectura_padre <- renderText({
    izquierda <- a(); derecha <- b()
    paste0("Padre: A=", if (is.null(izquierda)) "sin guardar" else izquierda,
      "; B=", if (is.null(derecha)) "sin guardar" else derecha, ".")
  })
}
shinyApp(ui, server)

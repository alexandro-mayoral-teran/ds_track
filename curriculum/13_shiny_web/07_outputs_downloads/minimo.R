library(shiny)
datos <- data.frame(credito = c("001", "002", "003"), saldo_mxn = c(0, 2000, 2500))
ui <- fluidPage(title = "DS Track - primera descarga", h1("Una tabla y su CSV"),
  tableOutput("tabla"), downloadButton("csv", "Descargar CSV del minimo"), lang = "es")
server <- function(input, output, session) {
  output$tabla <- renderTable({ datos }, rownames = FALSE, digits = 0)
  output$csv <- downloadHandler(filename = "creditos_minimo.csv",
    content = function(file) { utils::write.csv(datos, file, row.names = FALSE, fileEncoding = "UTF-8") },
    contentType = "text/csv; charset=utf-8")
}
shinyApp(ui, server)

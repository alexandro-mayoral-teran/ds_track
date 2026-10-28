library(shiny)
for (archivo in c("cartera.R", "consulta.R", "validacion.R", "presentacion.R", "consulta_module.R")) {
  source(archivo, local = TRUE, encoding = "UTF-8")
}
ui <- fluidPage(title = "DS Track - organizacion y modulos",
  h1("Dos consultas con el mismo modulo"),
  p("Cada panel tiene borrador y consulta aplicada propios. Ambos leen la misma fuente al aplicar, sin modificarla."),
  textOutput("comparacion"),
  fluidRow(column(6, consultaUI("izquierda", "Consulta A")),
           column(6, consultaUI("derecha", "Consulta B"))),
  lang = "es")
server <- function(input, output, session) {
  a <- consultaServer("izquierda", ruta = "cartera.csv")
  b <- consultaServer("derecha", ruta = "cartera.csv")
  output$comparacion <- renderText({
    izquierda <- a$estado()$consulta; derecha <- b$estado()$consulta
    if (is.null(izquierda) || is.null(derecha) || nrow(izquierda$universo) == 0L || nrow(derecha$universo) == 0L) {
      return("Aplica ambas consultas con universo para comparar sus selecciones.")
    }
    paste0("A: ", izquierda$indicadores$cantidad, " creditos / ", izquierda$indicadores$saldo_mxn,
      " MXN; B: ", derecha$indicadores$cantidad, " creditos / ", derecha$indicadores$saldo_mxn,
      " MXN. Cada consulta conserva su corte y denominador.")
  })
}
shinyApp(ui, server)

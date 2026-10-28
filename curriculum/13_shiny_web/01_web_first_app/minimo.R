# Una app completa sin controles: primero reconocer UI, servidor y objeto app.
library(shiny)

ui <- fluidPage(
  h1("Mi primera app Shiny"),
  p("Esta pagina se presenta en el navegador; el proceso R mantiene la app activa."),
  lang = "es"
)

server <- function(input, output, session) {
  # No hay calculos ni salidas dinamicas en este primer minimo.
}

shinyApp(ui = ui, server = server)

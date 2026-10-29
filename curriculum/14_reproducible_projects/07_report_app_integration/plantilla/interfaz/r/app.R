# Ejecutar desde interfaz/r con su biblioteca renv local.
if (as.character(getRversion()) != "4.6.1" || as.character(utils::packageVersion("shiny")) != "1.14.0") stop("Usa R 4.6.1 y Shiny 1.14.0 declarados para esta interfaz.")
raiz_producto <- normalizePath("../..", winslash = "/", mustWork = TRUE)
source(file.path(raiz_producto, "integracion.R"), encoding = "UTF-8")
opciones <- c("Octubre" = "config/octubre.csv", "Septiembre" = "config/septiembre.csv",
  "Selección vacía" = "config/vacio.csv", "Sin universo" = "config/sinuniverso.csv")
ui <- shiny::fluidPage(
  shiny::tags$head(shiny::tags$style("body{max-width:960px;margin:auto;padding:20px}table{border-collapse:collapse}td,th{padding:8px;border:1px solid #aaa}section{overflow-wrap:anywhere}")),
  shiny::titlePanel("Cartera: reporte y app conciliados"),
  shiny::p("Elige una configuración y pulsa Comprobar entrega. El borrador no cambia la consulta aplicada."),
  shiny::selectInput("config", "Configuración de la entrega", opciones, selectize = FALSE),
  shiny::actionButton("comprobar", "Comprobar entrega"),
  shiny::uiOutput("aviso"), shiny::uiOutput("vista"),
  shiny::p("Sin caché de cálculo ni vigilancia del disco. Pulsa de nuevo para comprobar cambios. No hay autenticidad por MD5."))
server <- function(input, output, session) {
  aplicada <- shiny::reactiveVal(NULL)
  aviso <- shiny::reactiveVal("Todavía no hay consulta aplicada.")
  shiny::bindEvent(shiny::observe({
    tryCatch({
      p <- cargar_integracion(raiz_producto, input$config, "shiny")
      aplicada(p); aviso("")
    }, error = function(error) {
      aplicada(NULL); aviso(paste("Comprobación rechazada:", conditionMessage(error)))
    })
  }), input$comprobar, ignoreInit = TRUE)
  output$aviso <- shiny::renderUI({
    if (nzchar(aviso())) return(shiny::p(role = "alert", aviso()))
    p <- aplicada()
    if (!is.null(p) && input$config != p$config) shiny::p("Borrador distinto: se conserva la configuración aplicada que aparece abajo.")
  })
  output$vista <- shiny::renderUI({
    p <- aplicada()
    if (!is.null(p)) shiny::HTML(vista_integracion(p))
  })
}
shiny::shinyApp(ui, server)

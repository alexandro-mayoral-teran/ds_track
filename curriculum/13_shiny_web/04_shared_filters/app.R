library(shiny)
source("cartera.R", local = TRUE, encoding = "UTF-8")
cartera <- leer_cartera("cartera.csv")
cortes <- sort(unique(cartera$fecha_corte))

ui <- fluidPage(
  title = "DS Track - filtros compartidos",
  h1("Explorar un corte de cartera"),
  p("Datos ficticios: tres creditos en dos cortes. Tabla e indicadores usan la misma seleccion."),
  selectInput("corte", "Fecha de corte", choices = cortes, selected = "2026-09-30", selectize = FALSE),
  checkboxGroupInput("segmentos", "Segmentos incluidos", choices = c("Comercio" = "comercio", "Servicios" = "servicios"),
                     selected = c("comercio", "servicios")),
  numericInput("minimo_mxn", "Saldo minimo (MXN, incluido)", value = 2000, min = 0, max = 1000000, step = 1),
  checkboxInput("mostrar_tabla", "Mostrar tabla", value = TRUE),
  h2("Seleccion e indicadores"),
  textOutput("contexto"),
  textOutput("resumen"),
  textOutput("cobertura"),
  tableOutput("tabla"),
  p("Ningun segmento marcado selecciona cero filas. Ocultar la tabla no cambia los indicadores."),
  lang = "es"
)

server <- function(input, output, session) {
  universo <- reactive({
    if (is.null(input$corte)) return(NULL)
    seleccionar_corte(cartera, input$corte)
  }, label = "universo_del_corte")

  seleccion <- reactive({
    datos <- universo()
    if (is.null(datos) || is.null(input$minimo_mxn)) return(NULL)
    # Un grupo de casillas sin marcar llega como NULL; aqui significa ninguno.
    segmentos <- if (is.null(input$segmentos)) character() else input$segmentos
    message("[seleccion] corte=", input$corte, "; minimo=", input$minimo_mxn)
    filtrar_seleccion(datos, segmentos, input$minimo_mxn)
  }, label = "seleccion_compartida")

  indicadores <- reactive({
    datos <- seleccion()
    if (is.null(datos)) return(NULL)
    resumir_seleccion(datos, nrow(universo()))
  }, label = "indicadores_compartidos")

  output$contexto <- renderText({
    if (is.null(input$corte) || is.null(input$minimo_mxn)) return(NULL)
    etiquetas <- if (length(input$segmentos) == 0L) "ninguno" else paste(sort(input$segmentos), collapse = ", ")
    paste0("Corte: ", input$corte, ". Segmentos: ", etiquetas, ". Saldo minimo: ", input$minimo_mxn, " MXN (>=).")
  })
  output$resumen <- renderText({
    valores <- indicadores()
    if (is.null(valores)) return(NULL)
    paste0("Creditos seleccionados: ", valores$cantidad, "; saldo seleccionado: ", valores$saldo_mxn, " MXN.")
  })
  output$cobertura <- renderText({
    valores <- indicadores()
    if (is.null(valores)) return(NULL)
    if (is.na(valores$porcentaje_creditos)) return("Cobertura: sin universo en ese corte.")
    paste0("Cobertura: ", valores$cantidad, " de ", nrow(universo()), " creditos del corte (",
           formatC(valores$porcentaje_creditos, format = "f", digits = 2, decimal.mark = "."), "%).")
  })
  output$tabla <- renderTable({
    if (!isTRUE(input$mostrar_tabla)) return(NULL)
    datos <- seleccion()
    if (is.null(datos)) return(NULL)
    setNames(datos, c("Credito", "Segmento", "Corte", "Saldo (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
}

shinyApp(ui, server)

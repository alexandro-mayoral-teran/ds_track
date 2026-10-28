library(shiny)
source("cartera.R", local = TRUE, encoding = "UTF-8")
source("consulta.R", local = TRUE, encoding = "UTF-8")
cartera <- leer_cartera("cartera.csv") # Fuente inmutable; no contiene elecciones de usuarios.
ui <- fluidPage(
  title = "DS Track - eventos y sesion",
  h1("Editar y aplicar filtros"),
  p("Cartera ficticia: tres creditos por corte. Editar controles prepara un borrador; Aplicar filtros cambia la consulta."),
  selectInput("corte", "Fecha de corte (borrador)", choices = sort(unique(cartera$fecha_corte)), selected = "2026-09-30", selectize = FALSE),
  checkboxGroupInput("segmentos", "Segmentos del borrador", choices = c("Comercio" = "comercio", "Servicios" = "servicios"), selected = c("comercio", "servicios")),
  numericInput("minimo_mxn", "Saldo minimo del borrador (MXN, incluido)", value = 2000, min = 0, max = 1000000, step = 1),
  actionButton("aplicar", "Aplicar filtros"),
  textOutput("estado"), textOutput("aviso"),
  checkboxInput("mostrar_tabla", "Mostrar tabla", value = TRUE),
  h2("Consulta aplicada"),
  textOutput("contexto"), textOutput("resumen"), textOutput("cobertura"), tableOutput("tabla"),
  p("Ningun segmento marcado selecciona cero filas. Otra sesion tiene su propia consulta; recargar comienza sin consulta aplicada."),
  lang = "es"
)
server <- function(input, output, session) {
  # Estos objetos se crean de nuevo para CADA sesion.
  aplicada <- reactiveVal(NULL, label = "consulta_aplicada")
  aviso <- reactiveVal("Aun no aplicas filtros.")
  borrador <- reactive({
    list(corte = input$corte,
         segmentos = sort(if (is.null(input$segmentos)) character() else input$segmentos),
         minimo_mxn = input$minimo_mxn)
  })
  bindEvent(observe({
    # bindEvent aisla estas lecturas: solo el boton dispara la accion.
    nueva <- tryCatch(crear_consulta(cartera, borrador()), error = function(error) {
      aviso(paste0("No se aplico: ", conditionMessage(error), " Revisa el borrador y vuelve a aplicar."))
      NULL
    })
    if (is.null(nueva)) return(invisible(NULL))
    aplicada(nueva) # Un unico reemplazo, DESPUES de calcular/validar todo.
    aviso("Consulta aplicada. Puedes preparar otro borrador.")
    message("[aplicar] consulta completa guardada en esta sesion")
  }), input$aplicar, ignoreNULL = TRUE, ignoreInit = TRUE)

  output$estado <- renderText({
    guardada <- aplicada()
    if (is.null(guardada)) return("Borrador: sin consulta aplicada.")
    if (identical(borrador(), guardada$filtros)) "Borrador: coincide con la consulta aplicada." else "Borrador: cambios pendientes de aplicar."
  })
  output$aviso <- renderText({ aviso() })
  output$contexto <- renderText({
    guardada <- aplicada()
    if (is.null(guardada)) return("Consulta aplicada: ninguna.")
    f <- guardada$filtros
    segmentos <- if (length(f$segmentos) == 0) "ninguno" else paste(f$segmentos, collapse = ", ")
    paste0("Corte aplicado: ", f$corte, ". Segmentos: ", segmentos, ". Saldo minimo: ", f$minimo_mxn, " MXN (>=).")
  })
  output$resumen <- renderText({
    guardada <- aplicada()
    if (is.null(guardada)) return("Pulsa Aplicar filtros para consultar.")
    m <- guardada$indicadores
    paste0("Creditos seleccionados: ", m$cantidad, "; saldo seleccionado: ", m$saldo_mxn, " MXN.")
  })
  output$cobertura <- renderText({
    guardada <- aplicada()
    if (is.null(guardada)) return(NULL)
    m <- guardada$indicadores
    if (is.na(m$porcentaje_creditos)) return("Cobertura: sin universo en ese corte.")
    paste0("Cobertura: ", m$cantidad, " de ", nrow(guardada$universo), " creditos del corte (",
      formatC(m$porcentaje_creditos, format = "f", digits = 2, decimal.mark = "."), "%).")
  })
  output$tabla <- renderTable({
    if (!isTRUE(input$mostrar_tabla)) return(NULL)
    guardada <- aplicada()
    if (is.null(guardada)) return(NULL)
    setNames(guardada$seleccion, c("Credito", "Segmento", "Corte", "Saldo (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
}
shinyApp(ui, server)

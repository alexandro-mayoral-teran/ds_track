library(shiny)
source("cartera.R", local = TRUE, encoding = "UTF-8")
source("consulta.R", local = TRUE, encoding = "UTF-8")
source("validacion.R", local = TRUE, encoding = "UTF-8")
# No leemos aqui: la interfaz debe abrir incluso si falta el archivo.
ui <- fluidPage(
  title = "DS Track - validacion y mensajes", h1("Consultar con mensajes claros"),
  p("Los controles son un borrador. Cada aplicacion relee y valida toda la fuente antes de consultar."),
  selectInput("corte", "Fecha de corte (borrador)", choices = c("Septiembre" = "2026-09-30", "Octubre" = "2026-10-31", "Noviembre (sin registros de referencia)" = "2026-11-30"), selected = "2026-09-30", selectize = FALSE),
  checkboxGroupInput("segmentos", "Segmentos del borrador", choices = c("Comercio" = "comercio", "Servicios" = "servicios"), selected = c("comercio", "servicios")),
  textInput("minimo_texto", "Saldo minimo del borrador (texto en MXN)", value = "2000"),
  actionButton("aplicar", "Aplicar filtros"),
  textOutput("aviso"), textOutput("pendiente"),
  checkboxInput("mostrar_tabla", "Mostrar tabla", value = TRUE),
  h2("Ultima consulta aplicada"), textOutput("contexto"),
  textOutput("resumen"), textOutput("cobertura"), tableOutput("tabla"),
  p("Ningun segmento selecciona cero filas. Fuente ausente o invalida retira cifras al aplicar; cambiar archivos sin aplicar no actualiza la pagina."),
  lang = "es"
)
server <- function(input, output, session) {
  estado <- reactiveVal(list(tipo = "inicio", consulta = NULL, mensaje = "Pulsa Aplicar filtros para consultar."))
  borrador <- reactive({ revisar_filtros(input$corte, input$segmentos, input$minimo_texto) })
  bindEvent(observe({
    fuente <- leer_fuente_segura("cartera.csv")
    if (!fuente$ok) {
      message("[fuente] ", fuente$diagnostico)
      estado(list(tipo = "fuente", consulta = NULL, mensaje = fuente$mensaje))
      return(invisible(NULL))
    }
    revisado <- borrador()
    if (!revisado$ok) {
      estado(list(tipo = "rechazo", consulta = estado()$consulta,
        mensaje = paste0("No se aplico. ", revisado$mensaje, " Corrige y vuelve a aplicar. La consulta anterior, si existe, se conserva.")))
      return(invisible(NULL))
    }
    nueva <- tryCatch(crear_consulta(fuente$datos, revisado$filtros), error = function(error) {
      message("[calculo inesperado] ", conditionMessage(error)); NULL
    })
    if (is.null(nueva)) {
      estado(list(tipo = "error", consulta = NULL, mensaje = "Error inesperado al calcular. Se retiraron las cifras; revisa la consola R antes de volver a aplicar."))
      return(invisible(NULL))
    }
    if (nrow(nueva$universo) == 0L) {
      tipo <- "sin_universo"
      mensaje <- "Sin universo: el corte aplicado no tiene registros en la fuente validada. Elige otro corte y aplica; no se publica porcentaje."
    } else if (nrow(nueva$seleccion) == 0L) {
      tipo <- "vacio"
      mensaje <- "Seleccion vacia sobre un universo existente. Puedes incluir segmentos o bajar el minimo y volver a aplicar."
    } else {
      tipo <- "ok"; mensaje <- "Consulta aplicada con fuente validada."
    }
    estado(list(tipo = tipo, consulta = nueva, mensaje = mensaje))
  }), input$aplicar, ignoreNULL = TRUE, ignoreInit = TRUE)

  disponible <- reactive({
    actual <- estado()
    # El aviso general ya explica la causa; FALSE evita repetirla en cada salida.
    validate(need(!is.null(actual$consulta), FALSE))
    validate(need(nrow(actual$consulta$universo) > 0L, FALSE))
    actual$consulta
  })
  output$aviso <- renderText({ estado()$mensaje })
  output$pendiente <- renderText({
    actual <- estado()$consulta; editado <- borrador()
    if (is.null(actual)) return("Borrador: sin consulta aplicada disponible.")
    if (editado$ok && identical(editado$filtros, actual$filtros)) "Borrador: coincide con la consulta aplicada." else "Borrador: cambios pendientes de aplicar."
  })
  output$contexto <- renderText({
    actual <- estado()$consulta
    if (is.null(actual)) return("Consulta aplicada disponible: ninguna.")
    f <- actual$filtros; segmentos <- if (length(f$segmentos) == 0L) "ninguno" else paste(f$segmentos, collapse = ", ")
    paste0("Corte aplicado: ", f$corte, ". Segmentos: ", segmentos, ". Saldo minimo: ", f$minimo_mxn, " MXN (>=).")
  })
  output$resumen <- renderText({
    m <- disponible()$indicadores
    paste0("Creditos seleccionados: ", m$cantidad, "; saldo seleccionado: ", m$saldo_mxn, " MXN.")
  })
  output$cobertura <- renderText({
    actual <- disponible(); m <- actual$indicadores
    paste0("Cobertura: ", m$cantidad, " de ", nrow(actual$universo), " creditos del corte (",
      formatC(m$porcentaje_creditos, format = "f", digits = 2, decimal.mark = "."), "%).")
  })
  output$tabla <- renderTable({
    req(isTRUE(input$mostrar_tabla)) # Solo controla presentacion; no valida datos.
    datos <- disponible()$seleccion
    validate(need(nrow(datos) > 0L, "No hay filas seleccionadas. Incluye segmentos o baja el minimo y aplica."))
    setNames(datos, c("Credito", "Segmento", "Corte", "Saldo (MXN)"))
  }, rownames = FALSE, digits = 0, striped = TRUE)
}
shinyApp(ui, server)

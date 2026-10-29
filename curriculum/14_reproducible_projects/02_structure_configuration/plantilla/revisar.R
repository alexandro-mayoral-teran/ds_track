# Cargar este archivo define una funcion; la raiz del proyecto es explicita.
revisar_proyecto <- function(raiz, archivo = "config/consulta.csv") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  entorno <- new.env(parent = globalenv())
  source(file.path(raiz, "codigo", "modelo.R"), local = entorno, encoding = "UTF-8")
  source(file.path(raiz, "codigo", "configuracion.R"), local = entorno, encoding = "UTF-8")
  config <- entorno$leer_configuracion(raiz, archivo)
  datos <- entorno$leer_fuente_modelo(config$entrada_resuelta)
  resultado <- entorno$resolver_contrato(datos, config$corte, config$segmentos, config$minimo_texto)
  for (clave in c("version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida")) cat(clave, ": ", config[[clave]], "\n", sep = "")
  for (clave in names(resultado)) cat(clave, ": ", resultado[[clave]], "\n", sep = "")
  cat("Solo revision: no inicia app/reporte ni crea/reserva el destino de salida.\n")
  invisible(resultado)
}

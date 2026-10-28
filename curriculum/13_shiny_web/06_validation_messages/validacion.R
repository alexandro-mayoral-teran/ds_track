# Funciones corrientes. Requieren cartera.R; no leen al hacer source.
revisar_filtros <- function(corte, segmentos, minimo_texto) {
  rechazo <- function(mensaje) list(ok = FALSE, mensaje = mensaje)
  if (!is.character(minimo_texto) || length(minimo_texto) != 1L || is.na(minimo_texto) || !nzchar(minimo_texto)) {
    return(rechazo("Escribe el saldo minimo en pesos enteros; usa 0 si no quieres excluir saldos por importe."))
  }
  if (!grepl("^(0|[1-9][0-9]*)$", minimo_texto)) {
    return(rechazo("Minimo invalido: usa digitos sin signos, espacios, decimales ni ceros iniciales (salvo 0)."))
  }
  minimo <- as.numeric(minimo_texto)
  if (!is.finite(minimo) || minimo > 1000000) return(rechazo("Minimo fuera de rango: usa de 0 a 1000000 MXN."))
  fecha_valida <- tryCatch({ validar_fecha(corte); TRUE }, error = function(e) FALSE)
  if (!fecha_valida) return(rechazo("Selecciona una fecha de corte valida en formato YYYY-MM-DD."))
  if (is.null(segmentos)) segmentos <- character()
  if (!is.character(segmentos) || anyNA(segmentos) || anyDuplicated(segmentos) ||
      any(!segmentos %in% c("comercio", "servicios"))) return(rechazo("Selecciona segmentos conocidos, sin repetir."))
  list(ok = TRUE, filtros = list(corte = corte, segmentos = sort(segmentos), minimo_mxn = minimo))
}

leer_fuente_segura <- function(ruta = "cartera.csv") {
  if (!file.exists(ruta)) return(list(ok = FALSE,
    mensaje = "No se encuentra cartera.csv. Recupera la copia de la fuente y vuelve a aplicar.",
    diagnostico = paste("Archivo ausente:", ruta)))
  tryCatch(list(ok = TRUE, datos = leer_cartera(ruta)), error = function(error) {
    list(ok = FALSE, mensaje = "La fuente no se puede usar: revisa el contrato y el diagnostico en la consola R; corrige la copia y vuelve a aplicar.",
         diagnostico = conditionMessage(error))
  })
}

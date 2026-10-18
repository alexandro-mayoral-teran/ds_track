# Solo definiciones. Comparacion semantica: no exige CSV de bytes identicos.
esquemas_cierre <- list(
  aceptados = list(numericas = c("fila_origen", "unidades", "precio_mxn", "importe_mxn"),
                   exactas = "fila_origen"),
  rechazos = list(numericas = "fila_origen", exactas = "fila_origen"),
  controles = list(numericas = c("n_entrada", "n_aceptados", "n_rechazados"),
                   exactas = c("n_entrada", "n_aceptados", "n_rechazados")),
  resumen = list(numericas = c("n_registros", "n_conocidos", "n_faltantes", "cobertura_pct",
                               "suma_observada_mxn", "media_observada_mxn", "total_mxn",
                               "n_cumplen", "n_no_cumplen", "n_pendientes"),
                 exactas = c("n_registros", "n_conocidos", "n_faltantes",
                              "n_cumplen", "n_no_cumplen", "n_pendientes"))
)

leer_tabla_cierre <- function(ruta) {
  return(tryCatch(
    read.csv(ruta, colClasses = "character", na.strings = character(0),
             check.names = FALSE, row.names = NULL, fill = FALSE,
             blank.lines.skip = FALSE, fileEncoding = "UTF-8"),
    warning = function(w) { stop(conditionMessage(w)) }
  ))
}

numero_exportado <- function(texto, exacto = FALSE) {
  ausente <- texto == "NA"
  texto_numero <- texto
  texto_numero[ausente] <- NA_character_
  valor <- tryCatch(as.double(texto_numero),
                    warning = function(w) { stop(conditionMessage(w)) })
  if (any(is.nan(valor)) || !identical(is.na(valor), ausente) ||
      any(!is.na(valor) & !is.finite(valor))) {
    stop("Numero exportado incompatible o faltante sin marcador NA.")
  }
  if (exacto && (any(ausente) || any(!grepl("^[0-9]+$", texto)))) {
    stop("Los conteos y posiciones deben ser enteros decimales conocidos.")
  }
  return(valor)
}

comparar_tabla <- function(actual, referencia, esquema, nombre) {
  if (!identical(names(actual), names(referencia))) {
    stop(paste("Esquema diferente en", nombre))
  }
  if (nrow(actual) != nrow(referencia)) { stop(paste("Filas diferentes en", nombre)) }
  for (campo in names(actual)) {
    if (campo %in% esquema$numericas) {
      exacto <- campo %in% esquema$exactas
      valor_ref <- numero_exportado(referencia[[campo]], exacto)
      valor_actual <- actual[[campo]]
      if (!is.numeric(valor_actual) || any(is.nan(valor_actual)) ||
          any(!is.na(valor_actual) & !is.finite(valor_actual)) ||
          !identical(is.na(valor_actual), is.na(valor_ref))) {
        stop(paste("Tipo, finitud o faltantes diferentes en", nombre, campo))
      }
      if (exacto) {
        coincide <- all(valor_actual == valor_ref)
      } else {
        coincide <- all(abs(valor_actual - valor_ref) <= 1e-9, na.rm = TRUE)
      }
    } else {
      coincide <- identical(actual[[campo]], referencia[[campo]])
    }
    if (!coincide) { stop(paste("Valores diferentes en", nombre, campo)) }
  }
  return(data.frame(tabla = nombre, control = c("esquema", "n_filas", names(actual)),
                     correcto = TRUE, stringsAsFactors = FALSE))
}

tablas_revision <- function(revision, resumen) {
  return(list(aceptados = revision$aceptados, rechazos = revision$rechazos,
               controles = revision$controles, resumen = as.data.frame(resumen)))
}

comparar_con_python <- function(tablas, carpeta_python, entrada) {
  contexto <- leer_tabla_cierre(file.path(carpeta_python, "contexto.csv"))
  if (!identical(names(contexto), c("contrato", "md5_entrada", "umbral", "python")) ||
      nrow(contexto) != 1L) { stop("Contexto Python incompatible.") }
  if (contexto$contrato != "ventas-06-09-v1" || contexto$umbral != "200") {
    stop("Contrato o umbral distintos de los usados por R.")
  }
  if (!identical(contexto$md5_entrada, unname(tools::md5sum(entrada)))) {
    stop("La referencia Python corresponde a otra fuente o a una version anterior.")
  }
  pruebas <- data.frame(tabla = "contexto", control = c("contrato", "umbral", "fuente"),
                         correcto = TRUE, stringsAsFactors = FALSE)
  if (!identical(names(tablas), names(esquemas_cierre))) { stop("Faltan tablas del cierre.") }
  for (nombre in names(esquemas_cierre)) {
    referencia <- leer_tabla_cierre(file.path(carpeta_python, paste0(nombre, ".csv")))
    prueba <- comparar_tabla(tablas[[nombre]], referencia, esquemas_cierre[[nombre]], nombre)
    pruebas <- rbind(pruebas, prueba)
  }
  return(pruebas)
}

leer_entrega_cierre <- function(carpeta) {
  tablas <- list()
  for (nombre in names(esquemas_cierre)) {
    tabla <- leer_tabla_cierre(file.path(carpeta, paste0(nombre, ".csv")))
    esquema <- esquemas_cierre[[nombre]]
    if (!all(esquema$numericas %in% names(tabla))) { stop("Faltan columnas numericas.") }
    for (campo in esquema$numericas) {
      tabla[[campo]] <- numero_exportado(tabla[[campo]], campo %in% esquema$exactas)
    }
    tablas[[nombre]] <- tabla
  }
  return(tablas)
}

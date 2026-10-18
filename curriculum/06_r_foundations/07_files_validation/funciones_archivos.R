# 06.07 - Definiciones sin lectura ni escritura al cargar el archivo.
leer_ventas <- function(ruta) {
  if (!file.exists(ruta) || dir.exists(ruta)) {
    stop("La entrada debe ser un archivo existente.")
  }
  # Este contrato requiere cuatro campos y un registro por linea fisica.
  # count.fields respeta las comillas de un campo que contiene una coma.
  campos <- count.fields(ruta, sep = ",", quote = "\"", comment.char = "",
                         blank.lines.skip = FALSE)
  if (length(campos) == 0L || anyNA(campos) || any(campos != 4L)) {
    stop("CSV incompatible: se esperan cuatro campos y un registro por linea.")
  }
  # Un aviso del lector tampoco permite continuar con una tabla parcial.
  crudos <- tryCatch(
    read.csv(ruta, header = TRUE, sep = ",", dec = ".", quote = "\"",
             colClasses = "character", na.strings = character(0),
             stringsAsFactors = FALSE, check.names = FALSE, row.names = NULL,
             strip.white = FALSE, fill = FALSE, blank.lines.skip = FALSE,
             comment.char = "", fileEncoding = "UTF-8"),
    warning = function(w) { stop(conditionMessage(w)) }
  )
  esperadas <- c("id_venta", "unidades", "precio_mxn", "nota")
  if (!identical(names(crudos), esperadas)) {
    stop("Las columnas o su orden no coinciden con el contrato.")
  }
  return(crudos)
}

# Solo texto decimal no negativo, sin signo ni exponente. Faltantes: "" y "NA".
convertir_numeros <- function(texto) {
  if (!is.character(texto) || anyNA(texto)) {
    stop("La conversion requiere texto conservado, sin NA de R.")
  }
  faltante <- texto == "" | texto == "NA"
  formato <- grepl("^[0-9]+([.][0-9]+)?$", texto)
  valores <- rep(NA_real_, length(texto))
  convertir <- !faltante & formato
  valores[convertir] <- as.double(texto[convertir])
  invalido <- !faltante & (!formato | !is.finite(valores))
  valores[invalido] <- NA_real_
  return(list(valores = valores, invalido = invalido, faltante = faltante))
}

validar_registros <- function(crudos) {
  esperadas <- c("id_venta", "unidades", "precio_mxn", "nota")
  if (!is.data.frame(crudos) || !identical(names(crudos), esperadas)) {
    stop("Se requiere la tabla textual de leer_ventas.")
  }
  for (nombre in esperadas) {
    if (!is.character(crudos[[nombre]]) || anyNA(crudos[[nombre]])) {
      stop("Las columnas deben conservar texto sin NA de R.")
    }
  }
  unidades <- convertir_numeros(crudos$unidades)
  precios <- convertir_numeros(crudos$precio_mxn)
  id_valido <- grepl("^V[0-9]{3}$", crudos$id_venta)
  repetido <- duplicated(crudos$id_venta) | duplicated(crudos$id_venta, fromLast = TRUE)
  importes <- unidades$valores * precios$valores
  producto_invalido <- !is.na(importes) & !is.finite(importes)
  motivos <- rep("", nrow(crudos))
  for (i in seq_len(nrow(crudos))) {
    razones <- character(0)
    if (!id_valido[i]) { razones <- c(razones, "id_invalido") }
    if (id_valido[i] && repetido[i]) { razones <- c(razones, "id_repetido") }
    if (unidades$invalido[i]) { razones <- c(razones, "unidades_invalidas") }
    if (precios$invalido[i]) { razones <- c(razones, "precio_invalido") }
    if (producto_invalido[i]) { razones <- c(razones, "importe_no_finito") }
    motivos[i] <- paste(razones, collapse = ";")
  }
  aceptada <- motivos == ""
  filas <- seq_len(nrow(crudos))
  tipados <- data.frame(fila_origen = filas, id_venta = crudos$id_venta,
                        unidades = unidades$valores, precio_mxn = precios$valores,
                        importe_mxn = importes, nota = crudos$nota,
                        stringsAsFactors = FALSE)
  aceptados <- tipados[aceptada, , drop = FALSE]
  rechazos <- data.frame(fila_origen = filas[!aceptada],
                         crudos[!aceptada, , drop = FALSE],
                         motivo = motivos[!aceptada], stringsAsFactors = FALSE)
  controles <- data.frame(n_entrada = nrow(crudos), n_aceptados = nrow(aceptados),
                          n_rechazados = nrow(rechazos))
  if (controles$n_aceptados + controles$n_rechazados != controles$n_entrada) {
    stop("Los conteos no concilian con la entrada.")
  }
  return(list(aceptados = aceptados, rechazos = rechazos, controles = controles))
}

# Exige una carpeta nueva. Una falla de escritura puede dejar entrega parcial.
exportar_revision <- function(revision, resumen, destino) {
  if (file.exists(destino) || dir.exists(destino)) {
    stop("El destino ya existe; elige otra carpeta para conservar la entrega.")
  }
  if (!dir.create(destino, recursive = TRUE)) {
    stop("No se pudo crear la carpeta de salida.")
  }
  write.csv(revision$aceptados, file.path(destino, "aceptados.csv"),
            row.names = FALSE, na = "NA", fileEncoding = "UTF-8")
  write.csv(revision$rechazos, file.path(destino, "rechazos.csv"),
            row.names = FALSE, na = "NA", fileEncoding = "UTF-8")
  write.csv(revision$controles, file.path(destino, "controles.csv"),
            row.names = FALSE, fileEncoding = "UTF-8")
  write.csv(as.data.frame(resumen), file.path(destino, "resumen.csv"),
            row.names = FALSE, na = "NA", fileEncoding = "UTF-8")
  return(destino)
}

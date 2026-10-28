# Funciones R corrientes: no cargan Shiny, no leen al hacer source y no mutan datos.
validar_fecha <- function(fecha) {
  if (!is.character(fecha) || length(fecha) != 1L || is.na(fecha) ||
      !grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha)) stop("Fecha: usa YYYY-MM-DD.")
  valor <- as.Date(fecha, format = "%Y-%m-%d")
  if (is.na(valor) || format(valor, "%Y-%m-%d") != fecha || fecha < "1900-01-01" || fecha > "2100-12-31") {
    stop("Fecha inexistente o fuera de 1900-2100.")
  }
  invisible(TRUE)
}

validar_cartera <- function(datos) {
  columnas <- c("id_credito", "segmento", "fecha_corte", "saldo_mxn")
  if (!is.data.frame(datos) || !identical(names(datos), columnas) || nrow(datos) > 10000L) {
    stop("Cartera: cuatro columnas en orden y hasta 10000 registros.")
  }
  if (!all(vapply(datos[1:3], is.character, logical(1))) || anyNA(datos) ||
      !is.numeric(datos$saldo_mxn) || any(!is.finite(datos$saldo_mxn)) ||
      any(datos$saldo_mxn < 0 | datos$saldo_mxn > 1000000 | datos$saldo_mxn != floor(datos$saldo_mxn))) {
    stop("Tipos, ausencias o saldo fuera del contrato.")
  }
  if (any(!grepl("^[0-9]{3}$", datos$id_credito)) ||
      any(!datos$segmento %in% c("comercio", "servicios"))) stop("ID o segmento fuera del contrato.")
  for (fecha in unique(datos$fecha_corte)) validar_fecha(fecha)
  if (anyDuplicated(datos[c("id_credito", "fecha_corte")])) stop("Clave ID/corte repetida.")
  invisible(TRUE)
}

leer_cartera <- function(ruta = "cartera.csv") {
  texto <- utils::read.csv(ruta, colClasses = "character", check.names = FALSE, row.names = NULL,
    na.strings = NULL, fileEncoding = "UTF-8", fill = FALSE, blank.lines.skip = FALSE)
  if (!identical(names(texto), c("id_credito", "segmento", "fecha_corte", "saldo_mxn"))) stop("Encabezado incorrecto.")
  if (anyNA(texto) || any(!grepl("^(0|[1-9][0-9]*)$", texto$saldo_mxn))) stop("Saldo: texto entero sin signos ni decimales.")
  texto$saldo_mxn <- as.numeric(texto$saldo_mxn)
  validar_cartera(texto) # Toda la fuente, antes de cualquier filtro.
  texto
}

seleccionar_corte <- function(datos, corte) {
  validar_cartera(datos)
  validar_fecha(corte)
  resultado <- datos[datos$fecha_corte == corte, , drop = FALSE]
  resultado <- resultado[order(resultado$id_credito), , drop = FALSE]
  rownames(resultado) <- NULL
  resultado
}

filtrar_seleccion <- function(universo, segmentos, minimo_mxn) {
  validar_cartera(universo)
  if (length(unique(universo$fecha_corte)) > 1L) stop("Selecciona un solo corte antes de filtrar.")
  if (!is.character(segmentos) || anyNA(segmentos) || anyDuplicated(segmentos) ||
      any(!segmentos %in% c("comercio", "servicios"))) stop("Segmentos: etiquetas conocidas, sin repetir.")
  if (!is.numeric(minimo_mxn) || length(minimo_mxn) != 1L || is.na(minimo_mxn) ||
      !is.finite(minimo_mxn) || minimo_mxn < 0 || minimo_mxn > 1000000 || minimo_mxn != floor(minimo_mxn)) {
    stop("Minimo: entero de 0 a 1000000 MXN.")
  }
  resultado <- universo[universo$segmento %in% segmentos & universo$saldo_mxn >= minimo_mxn, , drop = FALSE]
  resultado <- resultado[order(resultado$id_credito), , drop = FALSE]
  rownames(resultado) <- NULL
  resultado
}

resumir_seleccion <- function(seleccion, cantidad_universo) {
  validar_cartera(seleccion)
  if (length(unique(seleccion$fecha_corte)) > 1L) stop("El resumen requiere un solo corte.")
  if (!is.numeric(cantidad_universo) || length(cantidad_universo) != 1L ||
      is.na(cantidad_universo) || !is.finite(cantidad_universo) ||
      cantidad_universo < nrow(seleccion) || cantidad_universo > 10000 || cantidad_universo != floor(cantidad_universo)) {
    stop("Denominador incompatible con la seleccion.")
  }
  cantidad <- nrow(seleccion)
  list(cantidad = cantidad, saldo_mxn = sum(as.numeric(seleccion$saldo_mxn)),
       porcentaje_creditos = if (cantidad_universo == 0) NA_real_ else 100 * cantidad / cantidad_universo)
}

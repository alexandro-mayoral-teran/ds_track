# 06.06 - Funciones reutilizables. Cargar este archivo solo define funciones.
# Contrato de esta practica: vectores numericos ordinarios, sin dimensiones,
# no negativos; NA permitido, NaN e infinitos rechazados. Sin conversion a numero.
validar_numeros <- function(x) {
  if (!is.numeric(x) || !is.null(dim(x))) {
    stop("Se requiere un vector numerico sin dimensiones.")
  }
  if (any(is.nan(x)) || any(!is.na(x) & !is.finite(x))) {
    stop("No se permiten NaN ni infinitos.")
  }
  if (any(x < 0, na.rm = TRUE)) {
    stop("No se permiten valores negativos.")
  }
  return(x)
}

# Longitudes iguales: se prohibe el reciclaje de precios en este contrato.
# Cada posicion debe representar la misma venta en ambos argumentos.
calcular_importes <- function(unidades, precio_mxn) {
  unidades <- validar_numeros(unidades)
  precio_mxn <- validar_numeros(precio_mxn)
  if (length(unidades) != length(precio_mxn)) {
    stop("Unidades y precios deben tener la misma longitud.")
  }
  # as.double evita desbordamiento de multiplicacion entre enteros R.
  importes <- as.double(unidades) * as.double(precio_mxn)
  if (any(!is.na(importes) & !is.finite(importes))) {
    stop("El producto excede el rango numerico disponible.")
  }
  return(importes)
}

# Devuelve datos; no imprime, no modifica entradas ni escribe archivos.
# Sin registros o sin valores conocidos, suma/media/total se informan como NA.
resumir_importes <- function(importes, umbral = 200) {
  importes <- validar_numeros(importes)
  umbral <- validar_numeros(umbral)
  if (length(umbral) != 1L || any(is.na(umbral))) {
    stop("El umbral debe ser un numero conocido de longitud uno.")
  }
  n_registros <- length(importes)
  n_conocidos <- sum(!is.na(importes))
  n_faltantes <- sum(is.na(importes))
  cobertura_pct <- NA_real_
  suma_observada_mxn <- NA_real_
  media_observada_mxn <- NA_real_
  total_mxn <- NA_real_
  if (n_registros > 0L) {
    cobertura_pct <- 100 * n_conocidos / n_registros
  }
  if (n_conocidos > 0L) {
    suma_observada_mxn <- sum(importes, na.rm = TRUE)
    if (!is.finite(suma_observada_mxn)) {
      stop("La suma excede el rango numerico disponible.")
    }
    media_observada_mxn <- mean(importes, na.rm = TRUE)
  }
  if (n_registros > 0L && n_conocidos == n_registros) {
    total_mxn <- suma_observada_mxn
  }
  condicion <- importes >= umbral
  conocida <- !is.na(condicion)
  return(list(
    n_registros = n_registros,
    n_conocidos = n_conocidos,
    n_faltantes = n_faltantes,
    cobertura_pct = cobertura_pct,
    suma_observada_mxn = suma_observada_mxn,
    media_observada_mxn = media_observada_mxn,
    total_mxn = total_mxn,
    n_cumplen = sum(conocida & condicion),
    n_no_cumplen = sum(conocida & !condicion),
    n_pendientes = sum(!conocida)
  ))
}

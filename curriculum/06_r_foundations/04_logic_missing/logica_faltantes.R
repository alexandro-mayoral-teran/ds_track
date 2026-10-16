# 06.04 - Logica y valores faltantes. Ejecutar desde una sesion nueva.
# Las primeras cuatro ventas conservan los valores de 06.02 y 06.03.
id_venta <- c("V001", "V002", "V003", "V004", "V005", "V006")
unidades <- c(4L, 2L, 0L, 3L, NA, 2L)
precio_mxn <- c(75, 120, 50, 40, 100, NA)
importe_mxn <- unidades * precio_mxn

cat("Importes por posicion (MXN):\n")
print(importe_mxn) # 300 240 0 120 NA NA

# Una comparacion conserva una respuesta por venta, incluidos los desconocidos.
cumple_umbral <- importe_mxn >= 200
conocida <- !is.na(cumple_umbral)
cumplen <- conocida & cumple_umbral
no_cumplen <- conocida & !cumple_umbral
pendientes <- is.na(cumple_umbral)

cat("Condicion importe >= 200:\n")
print(cumple_umbral)
cat("Cumplen:\n")
print(id_venta[cumplen])
cat("No cumplen con importe conocido:\n")
print(id_venta[no_cumplen])
cat("Pendientes de informacion:\n")
print(id_venta[pendientes])
cat("Conteos: cumplen, no cumplen, pendientes y total:\n")
print(c(sum(cumplen), sum(no_cumplen), sum(pendientes), length(id_venta)))

# Se informa cobertura antes de interpretar la suma parcial.
importe_conocido <- !is.na(importe_mxn)
n_conocidos <- sum(importe_conocido)
n_faltantes <- sum(!importe_conocido)
cobertura_pct <- 100 * n_conocidos / length(importe_mxn)
suma_observada_mxn <- sum(importe_mxn, na.rm = TRUE)
media_observada_mxn <- mean(importe_mxn, na.rm = TRUE)
cat("Importes conocidos y faltantes:\n")
print(c(n_conocidos, n_faltantes))
cat("Cobertura porcentual:\n")
print(cobertura_pct)
cat("Suma observada (MXN); el total de las seis ventas es desconocido:\n")
print(suma_observada_mxn)
cat("Media de los cuatro importes observados (MXN):\n")
print(media_observada_mxn)

# & y | operan por posicion; && y || combinan condiciones de longitud uno.
cat("Hay registros y todos tienen importe conocido:\n")
print(length(importe_mxn) > 0L && all(importe_conocido)) # FALSE
cat("Existe un cumplimiento confirmado; todas las ventas cumplen:\n")
print(c(any(cumple_umbral), all(cumple_umbral))) # TRUE FALSE

# Casos pequenos: cero observado, faltante, resultado indefinido y ausencia.
cat("is.na de cero, NA_real_ y NaN:\n")
print(is.na(c(0, NA_real_, NaN))) # FALSE TRUE TRUE
cat("is.nan de NA_real_ y NaN; longitud de NULL:\n")
print(is.nan(c(NA_real_, NaN))) # FALSE TRUE
print(length(NULL)) # 0

# Este cero es la suma del conjunto vacio tras omitir NA, no un total observado.
solo_faltantes <- c(NA_real_, NA_real_)
cat("Solo faltantes: conocidos, suma con na.rm y media con na.rm:\n")
print(c(sum(!is.na(solo_faltantes)), sum(solo_faltantes, na.rm = TRUE),
        mean(solo_faltantes, na.rm = TRUE))) # 0 0 NaN
cat("Vector vacio: longitud, any y all:\n")
print(length(numeric(0))) # 0
print(c(any(logical(0)), all(logical(0)))) # FALSE TRUE

cat("Version y sesion:\n")
print(R.version.string)
print(utils::sessionInfo())

# 06.05 - Listas y data frames. Ejecutar en una sesion nueva.
# Cada componente de una lista conserva su objeto y su longitud.
ficha <- list(id_venta = "V001", unidades = 4L, precio_mxn = 75,
              notas = c("Venta ficticia", "Precio confirmado"))
cat("Lista y contenido de un componente:\n")
str(ficha)
str(ficha["unidades"])
str(ficha[["unidades"]])

# Muestra nueva: conserva valores y orden de las seis ventas de 06.04.
id_venta <- c("V001", "V002", "V003", "V004", "V005", "V006")
unidades <- c(4L, 2L, 0L, 3L, NA, 2L)
precio_mxn <- c(75, 120, 50, 40, 100, NA)
cat("Longitudes de las entradas; revisar tambien correspondencia:\n")
print(c(length(id_venta), length(unidades), length(precio_mxn)))
ventas <- data.frame(id_venta = id_venta, unidades = unidades,
                     precio_mxn = precio_mxn, stringsAsFactors = FALSE)
ventas$importe_mxn <- ventas$unidades * ventas$precio_mxn
cat("Tabla, tipos y dimensiones:\n")
print(ventas)
str(ventas)
print(names(ventas))
print(c(nrow(ventas), ncol(ventas), length(ventas))) # 6 4 4

cat("Vector frente a tabla de una columna:\n")
columna <- ventas[["importe_mxn"]]
tabla_columna <- ventas[, "importe_mxn", drop = FALSE]
str(columna)
str(tabla_columna)
print(ventas[c(4, 1), c("id_venta", "importe_mxn"), drop = FALSE])

# Mascaras completas, sin NA, calculadas desde la misma tabla.
condicion <- ventas$importe_mxn >= 200
conocida <- !is.na(condicion)
altas <- ventas[conocida & condicion, , drop = FALSE]
bajas <- ventas[conocida & !condicion, , drop = FALSE]
pendientes <- ventas[is.na(condicion), , drop = FALSE]
cat("Cumplen, no cumplen y pendientes:\n")
print(altas)
print(bajas)
print(pendientes)
print(c(nrow(altas), nrow(bajas), nrow(pendientes))) # 2 2 2
sin_coincidencias <- ventas[ventas$id_venta == "V999", , drop = FALSE]
cat("Dimensiones de consulta vacia:\n")
print(dim(sin_coincidencias)) # 0 4
cat("Conocidos, faltantes, cobertura, suma y media observadas:\n")
print(c(sum(!is.na(ventas$importe_mxn)), sum(is.na(ventas$importe_mxn)),
        100 * sum(!is.na(ventas$importe_mxn)) / nrow(ventas),
        sum(ventas$importe_mxn, na.rm = TRUE),
        mean(ventas$importe_mxn, na.rm = TRUE)))

# Confirmacion didactica en copia; recalcular el importe es un paso distinto.
ventas_confirmadas <- ventas
fila_v005 <- ventas_confirmadas$id_venta == "V005"
cat("Registros que se van a confirmar:\n")
print(sum(fila_v005)) # 1
ventas_confirmadas$unidades[fila_v005] <- 1L
ventas_confirmadas$importe_mxn <- ventas_confirmadas$unidades * ventas_confirmadas$precio_mxn
cat("Variante V005 y original conservado:\n")
print(ventas_confirmadas[fila_v005, , drop = FALSE])
print(ventas[ventas$id_venta == "V005", , drop = FALSE])
print(c(sum(!is.na(ventas_confirmadas$importe_mxn)),
        sum(ventas_confirmadas$importe_mxn, na.rm = TRUE),
        mean(ventas_confirmadas$importe_mxn, na.rm = TRUE))) # 5 760 152

# Demostracion incorrecta aislada: no usar como fuente del resumen.
mal_reciclada <- data.frame(id_venta = id_venta, unidades = unidades,
                            precio_mxn = c(75, 120))
cat("Precios INCORRECTOS por reciclaje silencioso:\n")
print(mal_reciclada$precio_mxn)
cat("Version y sesion:\n")
print(R.version.string)
print(utils::sessionInfo())

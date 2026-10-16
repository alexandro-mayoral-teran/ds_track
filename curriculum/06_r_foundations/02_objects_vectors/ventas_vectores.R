# 06.02: cuatro ventas ficticias. Cada posicion representa la misma venta
# en todos los vectores; todavia no se leen tablas ni se hacen uniones.
id_venta <- c("V001", "V002", "V003", "V004")
unidades <- c(4L, 2L, 0L, 3L)
precio_mxn <- c(75, 120, 50, 40)

# Los vectores tienen cuatro elementos; la multiplicacion es por posicion.
print("Longitudes: identificadores, unidades, precios")
print(length(id_venta))
print(length(unidades))
print(length(precio_mxn))
importe_mxn <- unidades * precio_mxn
total_mxn <- sum(importe_mxn)
print("Importes por venta (MXN):")
print(importe_mxn)  # 300 240 0 120
print("Total de las cuatro ventas (MXN):")
print(total_mxn)    # 660; cero unidades sigue siendo una observacion.

print("Tipo y clase de unidades:")
print(typeof(unidades))  # integer
print(class(unidades))   # integer
print("Tipo y clase de precios:")
print(typeof(precio_mxn)) # double, aunque los valores se impriman sin decimales.
print(class(precio_mxn))  # numeric

# Un unico factor se aplica deliberadamente a todas las ventas.
factor_cobro <- 0.9
importe_con_descuento_mxn <- importe_mxn * factor_cobro
print("Importes con descuento del 10 por ciento (MXN):")
print(importe_con_descuento_mxn)  # 270 216 0 108
print("Total con descuento (MXN):")
print(sum(importe_con_descuento_mxn))  # 594

# Diagnosticar no instala paquetes ni guarda objetos entre sesiones.
print(R.version.string)
print(utils::sessionInfo())

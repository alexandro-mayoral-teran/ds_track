# 06.02: demostraciones DELIBERADAMENTE incorrectas como analisis de ventas.
# No son una segunda fuente de resultados aceptados. El aviso esperado no
# detiene necesariamente Rscript: codigo 0 no equivale a datos correctos.
unidades <- c(4L, 2L, 0L, 3L)

# Dos precios para cuatro ventas: R repite 75, 120, 75, 120 sin avisar.
precios_incompletos <- c(75, 120)
importe_reciclado_mxn <- unidades * precios_incompletos
print("Reciclaje completo sin aviso; estos NO son los importes correctos:")
print(importe_reciclado_mxn)  # 300 240 0 360; total 900 en lugar de 660.
print(sum(importe_reciclado_mxn))

# Tres precios para cuatro ventas: R empieza otra vuelta, ahora con un aviso.
precios_tres <- c(75, 120, 50)
importe_parcial_mxn <- unidades * precios_tres
print("Reciclaje parcial con aviso; tampoco es un resultado aceptado:")
print(importe_parcial_mxn)    # 300 240 0 225

# Combinar numero y texto elige un tipo comun character para todo el vector.
precios_mezclados <- c(75, "120")
print("Mezcla de numero y texto:")
print(precios_mezclados)
print(typeof(precios_mezclados))  # character

# Convertir no significa validar: se pierde la parte decimal sin redondear.
precios_decimales <- c(75.9, 120.1)
precios_truncados <- as.integer(precios_decimales)
print("Conversion con perdida de decimales; originales conservados:")
print(precios_decimales)
print(precios_truncados)         # 75 120, sin aviso en este caso.

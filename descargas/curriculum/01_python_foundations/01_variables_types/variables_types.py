"""Interpreta campos ficticios de texto y calcula una venta."""

# Entradas: simulan texto recibido desde un archivo.
producto = "cuaderno"
unidades_texto = "3"
precio_unitario_texto = "40"

# Conversión y cálculo.
unidades = int(unidades_texto)
precio_unitario_mxn = int(precio_unitario_texto)
importe_mxn = unidades * precio_unitario_mxn
alcanza_umbral = importe_mxn >= 100

# Salida con valores, tipos y una comparación.
print(f"{unidades} unidades de {producto}: {importe_mxn} MXN")
print(f"Tipo de la entrada: {type(unidades_texto).__name__}")
print(f"Tipo después de convertir: {type(unidades).__name__}")
print(f"¿Importe de al menos 100 MXN?: {alcanza_umbral}")

"""Representa ventas ficticias como una lista de registros."""

ventas = [
    {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
    {"producto": "lapiz", "unidades": 5, "precio_unitario_mxn": 10},
    {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
]

# Acceso por posición y después por nombre de campo.
primera_venta = ventas[0]
importe_mxn = primera_venta["unidades"] * primera_venta["precio_unitario_mxn"]
print(f"Registros iniciales: {len(ventas)}")
print(f"Primer producto: {primera_venta['producto']}")
print(f"Importe de la primera venta: {importe_mxn} MXN")

# Agrega un registro sin sustituir la lista por el resultado de append.
ventas.append({"producto": "rotulador", "unidades": 2, "precio_unitario_mxn": 15})
print(f"Registros después de agregar: {len(ventas)}")

# Copia un registro con campos simples, dejando intacto el original.
copia = primera_venta.copy()
copia["unidades"] = 4
print(f"Unidades del original: {primera_venta['unidades']}")
print(f"Unidades de la copia: {copia['unidades']}")
print(f"Región del primer registro: {primera_venta.get('region', 'sin dato')}")

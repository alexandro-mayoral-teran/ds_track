"""Clasifica y resume una colección de ventas ficticias."""

ventas = [
    {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
    {"producto": "lapiz", "unidades": 5, "precio_unitario_mxn": 10},
    {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
]
umbral_mxn = 50

# Inicializa una sola vez antes de recorrer.
cantidad_revisada = 0
total_general_mxn = 0
seleccionadas = []
total_seleccionado_mxn = 0

for venta in ventas:
    importe_mxn = venta["unidades"] * venta["precio_unitario_mxn"]
    cantidad_revisada += 1
    total_general_mxn += importe_mxn

    # El orden de estas condiciones define las categorías.
    if importe_mxn >= 80:
        categoria = "alto"
    elif importe_mxn >= 50:
        categoria = "medio"
    else:
        categoria = "bajo"
    print(f"{venta['producto']}: {importe_mxn} MXN, categoría {categoria}")

    # Construye la selección sin agregar campos al registro original.
    if importe_mxn >= umbral_mxn:
        registro = venta.copy()
        registro["importe_mxn"] = importe_mxn
        seleccionadas.append(registro)
        total_seleccionado_mxn += importe_mxn

print(f"Registros revisados: {cantidad_revisada}")
print(f"Total general: {total_general_mxn} MXN")
print(f"Registros con importe de al menos {umbral_mxn} MXN: {len(seleccionadas)}")
print(f"Total seleccionado: {total_seleccionado_mxn} MXN")

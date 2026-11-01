"""Separa cálculos, filtros y presentación de ventas ficticias."""


def calcular_importe(unidades, precio_unitario_mxn):
    """Calcula el importe con entradas numéricas ya preparadas."""
    return unidades * precio_unitario_mxn


def seleccionar_ventas(ventas, umbral_mxn=50):
    """Devuelve copias de las ventas cuyo importe alcanza el umbral."""
    seleccionadas = []
    for venta in ventas:
        importe_mxn = calcular_importe(venta["unidades"], venta["precio_unitario_mxn"])
        if importe_mxn >= umbral_mxn:
            registro = venta.copy()
            registro["importe_mxn"] = importe_mxn
            seleccionadas.append(registro)
    return seleccionadas


def resumir_ventas(ventas):
    """Devuelve cantidad y total, sin modificar registros ni imprimir."""
    total_mxn = 0
    for venta in ventas:
        total_mxn += calcular_importe(venta["unidades"], venta["precio_unitario_mxn"])
    return {"cantidad": len(ventas), "total_mxn": total_mxn}


def main():
    """Prepara entradas, llama a las transformaciones y muestra resultados."""
    ventas = [
        {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
        {"producto": "lapiz", "unidades": 5, "precio_unitario_mxn": 10},
        {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
    ]
    resumen_general = resumir_ventas(ventas)
    seleccionadas = seleccionar_ventas(ventas, umbral_mxn=50)
    resumen_seleccionado = resumir_ventas(seleccionadas)

    print(f"Registros generales: {resumen_general['cantidad']}")
    print(f"Total general: {resumen_general['total_mxn']} MXN")
    print(f"Registros seleccionados: {resumen_seleccionado['cantidad']}")
    print(f"Total seleccionado: {resumen_seleccionado['total_mxn']} MXN")


if __name__ == "__main__":
    main()

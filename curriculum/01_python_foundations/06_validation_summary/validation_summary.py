"""Valida ventas ficticias y conserva resultados y motivos de rechazo."""

import csv
from pathlib import Path


CAMPOS_ENTRADA = ["producto", "unidades", "precio_unitario_mxn"]
CAMPOS_VALIDOS = CAMPOS_ENTRADA + ["importe_mxn"]
CAMPOS_RECHAZADOS = ["registro"] + CAMPOS_ENTRADA + ["motivo"]
CAMPOS_RESUMEN = ["producto", "registros", "unidades", "importe_mxn"]


def leer_csv(ruta):
    """Detiene la lectura si no se puede interpretar la estructura acordada."""
    registros = []
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo, strict=True)
        if lector.fieldnames != CAMPOS_ENTRADA:
            raise ValueError(f"Encabezado esperado: {CAMPOS_ENTRADA}")
        for fila in lector:
            if None in fila or None in fila.values():
                raise ValueError("Hay un registro con campos sobrantes o faltantes.")
            registros.append(fila)
    return registros


def validar_venta(fila):
    """Recibe campos de texto; devuelve una venta o los motivos de rechazo."""
    errores = []
    producto = fila["producto"].strip()
    if producto == "":
        errores.append("producto vacío")

    # Capturar solo la conversión esperada; no ocultar otros errores del programa.
    unidades = None
    try:
        unidades = int(fila["unidades"])
    except ValueError:
        errores.append("unidades no es un entero")
    if unidades is not None and unidades <= 0:
        errores.append("unidades debe ser mayor que 0")

    precio = None
    try:
        precio = int(fila["precio_unitario_mxn"])
    except ValueError:
        errores.append("precio no es un entero")
    if precio is not None and precio < 0:
        errores.append("precio debe ser mayor o igual que 0")

    if errores:
        return {"venta": None, "errores": errores}

    venta = {
        "producto": producto,
        "unidades": unidades,
        "precio_unitario_mxn": precio,
        "importe_mxn": unidades * precio,
    }
    return {"venta": venta, "errores": []}


def separar_registros(registros):
    """Conserva cada entrada en una de dos colecciones, sin modificarla."""
    validos = []
    rechazados = []
    for numero, fila in enumerate(registros, start=1):
        resultado = validar_venta(fila)
        if resultado["errores"]:
            rechazado = {
                "registro": numero,
                "producto": fila["producto"],
                "unidades": fila["unidades"],
                "precio_unitario_mxn": fila["precio_unitario_mxn"],
                "motivo": "; ".join(resultado["errores"]),
            }
            rechazados.append(rechazado)
        else:
            validos.append(resultado["venta"])
    return {"validos": validos, "rechazados": rechazados}


def resumir_ventas(ventas):
    """Agrupa por producto y acumula registros, unidades e importe."""
    por_producto = {}
    for venta in ventas:
        producto = venta["producto"]
        if producto not in por_producto:
            por_producto[producto] = {
                "producto": producto, "registros": 0, "unidades": 0, "importe_mxn": 0
            }
        grupo = por_producto[producto]
        grupo["registros"] += 1
        grupo["unidades"] += venta["unidades"]
        grupo["importe_mxn"] += venta["importe_mxn"]
    return list(por_producto.values())


def comprobar_resultado(entradas, validos, rechazados, resumen):
    """Comprueba conteo e indicadores antes de escribir resultados."""
    if len(entradas) != len(validos) + len(rechazados):
        raise ValueError("No se conserva la cantidad de registros de entrada.")
    total_registros = 0
    total_unidades = 0
    total_mxn = 0
    for venta in validos:
        total_unidades += venta["unidades"]
        total_mxn += venta["importe_mxn"]
    unidades_resumen = 0
    importe_resumen = 0
    for grupo in resumen:
        total_registros += grupo["registros"]
        unidades_resumen += grupo["unidades"]
        importe_resumen += grupo["importe_mxn"]
    if (total_registros != len(validos)
            or unidades_resumen != total_unidades
            or importe_resumen != total_mxn):
        raise ValueError("El resumen no concilia con las ventas válidas.")
    return {"unidades": total_unidades, "importe_mxn": total_mxn}


def escribir_csv(ruta, campos, registros):
    """Reemplaza una salida generada; escribe encabezado incluso sin registros."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(registros)


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "ventas_revision.csv"
    salida = carpeta / "output"
    registros = leer_csv(entrada)
    resultado = separar_registros(registros)
    validos = resultado["validos"]
    rechazados = resultado["rechazados"]
    resumen = resumir_ventas(validos)
    control = comprobar_resultado(registros, validos, rechazados, resumen)

    escribir_csv(salida / "ventas_validas.csv", CAMPOS_VALIDOS, validos)
    escribir_csv(salida / "ventas_rechazadas.csv", CAMPOS_RECHAZADOS, rechazados)
    escribir_csv(salida / "resumen_productos.csv", CAMPOS_RESUMEN, resumen)
    print(f"Registros de entrada: {len(registros)}")
    print(f"Válidos: {len(validos)} | Rechazados: {len(rechazados)}")
    print(f"Unidades válidas: {control['unidades']}")
    print(f"Importe válido: {control['importe_mxn']} MXN")
    print("Conteo y resumen conciliados. Revisa los tres CSV en output.")


if __name__ == "__main__":
    main()

"""Lee ventas ficticias, convierte campos y escribe un CSV con importes."""

import csv
from pathlib import Path


CAMPOS_ENTRADA = ["producto", "unidades", "precio_unitario_mxn"]
CAMPOS_SALIDA = ["producto", "unidades", "precio_unitario_mxn", "importe_mxn"]


def leer_csv(ruta):
    """Lee un CSV UTF-8, con o sin BOM, con el encabezado esperado."""
    registros = []
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo, delimiter=",", strict=True)
        if lector.fieldnames != CAMPOS_ENTRADA:
            raise ValueError(f"Encabezado esperado: {CAMPOS_ENTRADA}")
        for fila in lector:
            if None in fila or None in fila.values():
                raise ValueError("La fila no tiene la cantidad de campos esperada.")
            registros.append(fila)
    return registros


def preparar_ventas(registros):
    """Convierte campos enteros y agrega importes sin modificar las entradas."""
    ventas = []
    for fila in registros:
        unidades = int(fila["unidades"])
        precio_unitario_mxn = int(fila["precio_unitario_mxn"])
        venta = {
            "producto": fila["producto"],
            "unidades": unidades,
            "precio_unitario_mxn": precio_unitario_mxn,
            "importe_mxn": unidades * precio_unitario_mxn,
        }
        ventas.append(venta)
    return ventas


def escribir_csv(ruta, ventas):
    """Escribe encabezado y registros; reemplaza la salida si ya existe."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_SALIDA, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(ventas)


def main():
    """Separa lectura, transformación, escritura y presentación."""
    carpeta_leccion = Path(__file__).resolve().parent
    ruta_entrada = carpeta_leccion / "ventas_entrada.csv"
    ruta_salida = carpeta_leccion / "output" / "ventas_con_importe.csv"

    registros = leer_csv(ruta_entrada)
    ventas = preparar_ventas(registros)
    escribir_csv(ruta_salida, ventas)

    total_mxn = 0
    for venta in ventas:
        total_mxn += venta["importe_mxn"]
    print(f"Registros leídos: {len(registros)}")
    print(f"Registros escritos: {len(ventas)}")
    print(f"Total calculado: {total_mxn} MXN")
    print(f"Salida: {ruta_salida.name} en la carpeta output de esta lección")


if __name__ == "__main__":
    main()

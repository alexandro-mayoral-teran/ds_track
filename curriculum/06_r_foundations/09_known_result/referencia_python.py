"""Referencia independiente para el contrato de ventas de 06.07, sin pandas."""

import argparse
import csv
import hashlib
import io
import math
import platform
import re
from pathlib import Path


CONTRATO = "ventas-06-09-v1"
UMBRAL = 200
ENTRADA = ["id_venta", "unidades", "precio_mxn", "nota"]
ACEPTADOS = ["fila_origen", "id_venta", "unidades", "precio_mxn", "importe_mxn", "nota"]
RECHAZOS = ["fila_origen"] + ENTRADA + ["motivo"]


def leer_entrada(ruta):
    """Un registro por línea; rechaza estructura ambigua antes de exportar."""
    texto = ruta.read_bytes().decode("utf-8")
    if not texto or not texto.endswith("\n"):
        raise ValueError("CSV vacío o sin salto de línea final.")
    filas = []
    for linea in io.StringIO(texto, newline=None):
        registros = list(csv.reader([linea], strict=True))
        if len(registros) != 1 or len(registros[0]) != 4:
            raise ValueError("Se esperan cuatro campos y un registro por línea.")
        filas.append(registros[0])
    if filas[0] != ENTRADA:
        raise ValueError("Cabecera incompatible con el contrato.")
    return [dict(zip(ENTRADA, valores)) for valores in filas[1:]]


def numero(texto):
    """Devuelve (valor o None, inválido); no confunde ausencia con error."""
    if texto in ("", "NA"):
        return None, False
    if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", texto) is None:
        return None, True
    valor = float(texto)
    return (valor, False) if math.isfinite(valor) else (None, True)


def analizar(filas):
    """Cuenta claves primero; valida después sin elegir un duplicado arbitrario."""
    frecuencias = {}
    for fila in filas:
        identificador = fila["id_venta"]
        frecuencias[identificador] = frecuencias.get(identificador, 0) + 1
    aceptados, rechazos = [], []
    for posicion, fila in enumerate(filas, start=1):
        motivos = []
        id_valido = re.fullmatch(r"V[0-9]{3}", fila["id_venta"]) is not None
        if not id_valido:
            motivos.append("id_invalido")
        if id_valido and frecuencias[fila["id_venta"]] > 1:
            motivos.append("id_repetido")
        unidades, unidades_invalidas = numero(fila["unidades"])
        precio, precio_invalido = numero(fila["precio_mxn"])
        if unidades_invalidas:
            motivos.append("unidades_invalidas")
        if precio_invalido:
            motivos.append("precio_invalido")
        importe = None
        if unidades is not None and precio is not None:
            importe = unidades * precio
            if not math.isfinite(importe):
                motivos.append("importe_no_finito")
        if motivos:
            rechazos.append({"fila_origen": posicion, **fila, "motivo": ";".join(motivos)})
        else:
            aceptados.append({
                "fila_origen": posicion, "id_venta": fila["id_venta"],
                "unidades": unidades, "precio_mxn": precio,
                "importe_mxn": importe, "nota": fila["nota"],
            })
    conocidos = [fila["importe_mxn"] for fila in aceptados if fila["importe_mxn"] is not None]
    n = len(aceptados)
    suma = math.fsum(conocidos) if conocidos else None
    if suma is not None and not math.isfinite(suma):
        raise ValueError("La suma excede el rango numérico disponible.")
    resumen = {
        "n_registros": n,
        "n_conocidos": len(conocidos),
        "n_faltantes": n - len(conocidos),
        "cobertura_pct": 100 * len(conocidos) / n if n else None,
        "suma_observada_mxn": suma,
        "media_observada_mxn": suma / len(conocidos) if conocidos else None,
        "total_mxn": suma if n and len(conocidos) == n else None,
        "n_cumplen": sum(importe >= UMBRAL for importe in conocidos),
        "n_no_cumplen": sum(importe < UMBRAL for importe in conocidos),
        "n_pendientes": n - len(conocidos),
    }
    controles = {"n_entrada": len(filas), "n_aceptados": n, "n_rechazados": len(rechazos)}
    if n + len(rechazos) != len(filas):
        raise ValueError("Los conteos no concilian.")
    return aceptados, rechazos, controles, resumen


def escribir(ruta, campos, filas):
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, lineterminator="\n")
        escritor.writeheader()
        for fila in filas:
            escritor.writerow({campo: "NA" if fila[campo] is None else fila[campo] for campo in campos})


def generar(entrada, destino):
    if destino.exists():
        raise FileExistsError("El destino ya existe; conserva esa referencia y elige otro.")
    huella_antes = hashlib.md5(entrada.read_bytes()).hexdigest()
    filas = leer_entrada(entrada)
    aceptados, rechazos, controles, resumen = analizar(filas)
    if hashlib.md5(entrada.read_bytes()).hexdigest() != huella_antes:
        raise ValueError("La fuente cambió durante el cálculo.")
    destino.mkdir(parents=True, exist_ok=False)
    escribir(destino / "aceptados.csv", ACEPTADOS, aceptados)
    escribir(destino / "rechazos.csv", RECHAZOS, rechazos)
    escribir(destino / "controles.csv", list(controles), [controles])
    escribir(destino / "resumen.csv", list(resumen), [resumen])
    # Metadatos al final: no convierten varias escrituras en una transacción.
    contexto = {"contrato": CONTRATO, "md5_entrada": huella_antes,
                "umbral": UMBRAL, "python": platform.python_version()}
    escribir(destino / "contexto.csv", list(contexto), [contexto])
    print(f"Referencia Python creada: {controles}")
    print(f"Suma observada: {resumen['suma_observada_mxn']}; total: {resumen['total_mxn']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path)
    parser.add_argument("destino", type=Path)
    argumentos = parser.parse_args()
    generar(argumentos.entrada, argumentos.destino)


if __name__ == "__main__":
    main()

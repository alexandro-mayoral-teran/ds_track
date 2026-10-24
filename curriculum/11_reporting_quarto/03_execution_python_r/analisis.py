"""Contrato pequeño y cálculo puro desde CSV para el reporte 11.03."""
import csv
import re
from pathlib import Path


def analizar(origen: Path) -> dict:
    ids = ["001", "002", "003"]
    fechas = ["2026-09-30", "2026-10-31"]
    esperadas = {(i, f) for i in ids for f in fechas}
    with origen.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["credito_id", "fecha_corte", "saldo_mxn"]:
            raise ValueError("Columnas distintas del contrato")
        valores = {}
        for fila in lector:
            clave = (fila["credito_id"], fila["fecha_corte"])
            texto = fila["saldo_mxn"]
            if (None in fila or clave not in esperadas or clave in valores
                    or texto is None or re.fullmatch(r"0|[1-9][0-9]{0,6}", texto) is None):
                raise ValueError("Clave o saldo inválido/repetido")
            saldo = int(texto)
            if saldo > 1_000_000:
                raise ValueError("Saldo excede 1000000 MXN")
            valores[clave] = saldo
    if set(valores) != esperadas:
        raise ValueError("Se requieren tres créditos en ambos cortes")
    pares = [(i, valores[i, fechas[0]], valores[i, fechas[1]]) for i in ids]
    a, b = (sum(valores[i, f] for i in ids) for f in fechas)
    tasa = f"{100 * (b-a) / a:.2f}%" if a != 0 else "no definida (base inicial cero)"
    return {"septiembre": a, "octubre": b, "diferencia": b-a, "tasa": tasa, "pares": pares}

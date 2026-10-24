"""Validar parámetros y la fuente completa antes de seleccionar el corte."""
import csv
from datetime import date
from pathlib import Path
import re


def analizar(origen: Path, fecha_corte, minimo_mxn) -> dict:
    if type(fecha_corte) is not str or re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha_corte) is None:
        raise ValueError("fecha_corte debe ser texto ISO YYYY-MM-DD")
    fecha = date.fromisoformat(fecha_corte)
    if not 1900 <= fecha.year <= 2100:
        raise ValueError("fecha_corte fuera de 1900–2100")
    if (type(minimo_mxn) not in (int, float) or not 0 <= minimo_mxn <= 1_000_000
            or int(minimo_mxn) != minimo_mxn):
        raise ValueError("minimo_mxn debe ser numérico entero entre 0 y 1000000, no texto/booleano")
    minimo = int(minimo_mxn)
    fechas = ["2026-09-30", "2026-10-31"]
    esperadas = {(i, f) for i in ["001", "002", "003"] for f in fechas} | {("004", fechas[1])}
    valores = {}
    with origen.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["credito_id", "fecha_corte", "saldo_mxn"]:
            raise ValueError("Columnas distintas del contrato")
        for fila in lector:
            clave = (fila["credito_id"], fila["fecha_corte"])
            texto = fila["saldo_mxn"]
            if (None in fila or clave not in esperadas or clave in valores or texto is None
                    or re.fullmatch(r"0|[1-9][0-9]{0,6}", texto) is None):
                raise ValueError("Clave o saldo inválido/repetido en la fuente completa")
            saldo = int(texto)
            if saldo > 1_000_000:
                raise ValueError("Saldo excede 1000000 MXN")
            valores[clave] = saldo
    if set(valores) != esperadas:
        raise ValueError("Se requieren las siete observaciones del contrato")
    if fecha_corte not in fechas:
        raise ValueError("Corte no disponible: no se interpreta como un universo vacío")
    filas = [(i, saldo, saldo >= minimo) for (i, f), saldo in sorted(valores.items()) if f == fecha_corte]
    seleccion = [(i, s) for i, s, cumple in filas if cumple]
    n = len(filas)
    return {"fecha": fecha_corte, "minimo": minimo, "filas": filas,
            "universo_n": n, "universo_mxn": sum(s for _, s, _ in filas),
            "seleccion_n": len(seleccion), "seleccion_mxn": sum(s for _, s in seleccion),
            "proporcion": f"{100 * len(seleccion) / n:.2f}%",
            "ids": ", ".join(i for i, _ in seleccion) or "ninguno"}

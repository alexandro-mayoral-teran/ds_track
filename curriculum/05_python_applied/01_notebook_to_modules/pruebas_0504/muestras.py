"""Entradas pequeñas propias: resultados calculables sin ejecutar el análisis."""

import csv
from pathlib import Path

import pandas as pd

CUT = "2026-10-31"
CREDITS = [
    ["001", "C01", "comercio"], ["002", "C02", "comercio"],
    ["003", "C03", "comercio"], ["004", "C04", "consumo"],
    ["005", "C05", "educacion"],
]
CUTS = [
    ["001", CUT, "0", "0"], ["002", CUT, "1", "30"],
    ["003", CUT, "", ""], ["004", CUT, "10", "31"],
    ["005", CUT, "", ""], ["001", "2026-09-30", "900", "0"],
]


def detail_fixture():
    """Tabla tipada para probar transformación sin depender del lector CSV."""
    return pd.DataFrame({
        "id_credito": pd.Series(["001", "002", "003", "004", "005", "001"], dtype="string"),
        "fecha_corte": pd.Series([CUT] * 5 + ["2026-09-30"], dtype="string"),
        "saldo_mxn": pd.Series([0, 1, pd.NA, 10, pd.NA, 900], dtype="Int64"),
        "dias_atraso": pd.Series([0, 30, pd.NA, 31, pd.NA, 0], dtype="Int64"),
        "segmento": pd.Series(["comercio"] * 3 + ["consumo", "educacion", "comercio"], dtype="string"),
    })


def write_sources(folder, cuts=None, credits=None):
    """Escribir solo dentro del directorio temporal recibido por cada prueba."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    specifications = [
        ("cortes.csv", ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"],
         CUTS if cuts is None else cuts),
        ("creditos.csv", ["id_credito", "id_cliente", "segmento"],
         CREDITS if credits is None else credits),
    ]
    for name, columns, rows in specifications:
        with (folder / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(columns)
            writer.writerows(rows)
    return folder

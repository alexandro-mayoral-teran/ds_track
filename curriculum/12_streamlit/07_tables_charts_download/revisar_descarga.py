"""Releer CSV/contexto con biblioteca estándar; no verifica la fuente histórica."""

import argparse
import csv
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path


def revisar(ruta_csv, ruta_contexto):
    contenido = Path(ruta_csv).read_bytes()
    contexto = json.loads(Path(ruta_contexto).read_text(encoding="utf-8"))
    if not isinstance(contexto, dict) or not all(isinstance(contexto.get(k), dict) for k in ("filtros", "universo", "indicadores")):
        raise ValueError("El contexto necesita filtros, universo e indicadores.")
    lector = csv.DictReader(StringIO(contenido.decode("utf-8")), strict=True)
    filas = list(lector)
    if lector.fieldnames != ["id_credito", "segmento", "fecha_corte", "saldo_mxn"]:
        raise ValueError("Encabezado CSV inesperado.")
    if lector.fieldnames != contexto["columnas_csv"]:
        raise ValueError("Las columnas no coinciden con el contexto.")
    if sha256(contenido).hexdigest() != contexto["sha256_csv"]:
        raise ValueError("El CSV no corresponde a la huella del contexto.")
    if len(filas) != contexto["filas_csv"] or len(filas) != contexto["indicadores"]["cantidad"]:
        raise ValueError("No coincide el número de filas.")
    saldo = sum(int(f["saldo_mxn"]) for f in filas)
    if saldo != contexto["indicadores"]["saldo_mxn"]:
        raise ValueError("No coincide la suma seleccionada.")
    return filas, contexto


def main():
    parser = argparse.ArgumentParser(description="Releer un par CSV/JSON descargado; no modifica archivos.")
    parser.add_argument("csv", type=Path)
    parser.add_argument("contexto", type=Path)
    args = parser.parse_args()
    try:
        filas, contexto = revisar(args.csv, args.contexto)
    except (OSError, UnicodeError, csv.Error, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    print("Filtros:", contexto["filtros"])
    print("Universo:", contexto["universo"])
    print("Filas:", len(filas), "Saldo seleccionado (MXN):", contexto["indicadores"]["saldo_mxn"])
    for fila in filas:
        print(fila)
    print("Huella, filas y suma coherentes. Contrasta cada valor con tu referencia de estudio.")


if __name__ == "__main__":
    main()

"""Otro consumidor de las mismas funciones: terminal → parámetros → JSON."""

import argparse
import csv
import json
from pathlib import Path

from cartera import SEGMENTOS, analizar, leer_cartera
from configuracion import CORTE_INICIAL, MINIMO_INICIAL, RUTA_DATOS


def main():
    parser = argparse.ArgumentParser(description="Analizar cartera sin abrir Streamlit.")
    parser.add_argument("--fuente", type=Path, default=RUTA_DATOS)
    parser.add_argument("--corte", default=CORTE_INICIAL)
    parser.add_argument("--minimo", type=int, default=MINIMO_INICIAL)
    parser.add_argument("--segmentos", nargs="*", choices=SEGMENTOS, default=list(SEGMENTOS))
    args = parser.parse_args()
    try:
        resultado = analizar(leer_cartera(args.fuente), args.corte, args.segmentos, args.minimo)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.error(str(error))  # Termina con código 2; no imprime un JSON de éxito.
    print(json.dumps(resultado, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()

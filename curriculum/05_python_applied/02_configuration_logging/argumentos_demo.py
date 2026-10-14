"""Reconocer argumentos y ayuda, sin leer fuentes ni crear una entrega."""

import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--cut", default="2026-10-31", help="Fecha del ejemplo")
    parser.add_argument("--dpi", type=int, default=160, help="Entero del ejemplo")
    args = parser.parse_args(argv)
    print(f"Fecha recibida: {args.cut}")
    print(f"Resolución recibida: {args.dpi} (tipo: {type(args.dpi).__name__})")
    print("Esta demostración solo interpreta argumentos; no valida datos ni exporta.")


if __name__ == "__main__":
    main()

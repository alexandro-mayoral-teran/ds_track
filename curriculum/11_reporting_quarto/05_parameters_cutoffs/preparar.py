"""Copiar fuentes de 11.05 a una carpeta nueva; no instala ni renderiza."""
import argparse
from pathlib import Path
import shutil


def preparar(destino: Path) -> None:
    base = Path(__file__).resolve().parent
    nombres = ["cartera.csv", "analisis.py", "reporte_python.qmd", "septiembre.yml", "octubre.yml"]
    if not all((base / n).is_file() for n in nombres):
        raise FileNotFoundError("Faltan fuentes de 11.05")
    destino.mkdir(parents=True, exist_ok=False)
    for nombre in nombres:
        shutil.copyfile(base / nombre, destino / nombre)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

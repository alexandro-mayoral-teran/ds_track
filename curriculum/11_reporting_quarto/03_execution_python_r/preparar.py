"""Copiar fuentes Python de 11.03 a una carpeta nueva; no renderiza ni instala."""
import argparse
from pathlib import Path
import shutil


def preparar(destino: Path) -> None:
    base = Path(__file__).resolve().parent
    archivos = ["cartera.csv", "analisis.py", "reporte_python.qmd"]
    if not all((base / a).is_file() for a in archivos):
        raise FileNotFoundError("Faltan fuentes de 11.03")
    destino.mkdir(parents=True, exist_ok=False)
    for a in archivos:
        shutil.copyfile(base / a, destino / a)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

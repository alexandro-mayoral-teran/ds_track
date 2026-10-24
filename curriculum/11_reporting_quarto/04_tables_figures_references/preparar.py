"""Fuentes completas para 11.04, en carpeta nueva; no instala ni renderiza."""
import argparse
from pathlib import Path
import shutil


def preparar(destino: Path) -> None:
    base = Path(__file__).resolve().parent
    origenes = [base / "cartera.csv", base / "reporte_python.qmd", base / "referencias.bib",
                base.parent / "03_execution_python_r" / "analisis.py"]
    if not all(p.is_file() for p in origenes):
        raise FileNotFoundError("Faltan fuentes de la práctica")
    destino.mkdir(parents=True, exist_ok=False)
    for origen in origenes:
        shutil.copyfile(origen, destino / origen.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

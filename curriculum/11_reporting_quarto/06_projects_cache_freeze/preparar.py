"""Preparar un proyecto Quarto Python nuevo; no instala ni renderiza."""
import argparse
from pathlib import Path
import shutil


def preparar(destino: Path) -> None:
    base = Path(__file__).resolve().parent
    fuentes = {
        base / "_quarto.yml": "_quarto.yml",
        base / "cartera.csv": "datos/cartera.csv",
        base / "reporte_python.qmd": "informes/reporte_1106.qmd",
        base / "octubre.yml": "octubre.yml",
        base.parent / "05_parameters_cutoffs/analisis.py": "funciones/analisis.py",
    }
    if not all(p.is_file() for p in fuentes):
        raise FileNotFoundError("Faltan fuentes de 11.06 o funciones de 11.05")
    destino.mkdir(parents=True, exist_ok=False)
    for origen, relativa in fuentes.items():
        salida = destino / relativa
        salida.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origen, salida)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

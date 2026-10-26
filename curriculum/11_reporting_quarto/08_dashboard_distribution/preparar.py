"""Preparar fuentes del dashboard 11.08 en un destino nuevo, sin renderizar."""
import argparse
from pathlib import Path
import shutil


def preparar(destino: Path) -> None:
    base = Path(__file__).resolve().parent
    fuentes = {base / n: n for n in ["cartera.csv", "dashboard_python.qmd", "estilos.css", "minimo.qmd"]}
    fuentes[base.parent / "03_execution_python_r/analisis.py"] = "analisis.py"
    if not all(p.is_file() for p in fuentes):
        raise FileNotFoundError("Faltan fuentes de 11.08 o funciones de 11.03")
    destino.mkdir(parents=True, exist_ok=False)
    for origen, nombre in fuentes.items():
        shutil.copyfile(origen, destino / nombre)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

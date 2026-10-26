"""Crear una copia Python 11.09 completa, sin instalar ni construir resultados."""
import argparse
from pathlib import Path
import shutil


def preparar(destino):
    base = Path(__file__).resolve().parent
    repo = base.parents[2]
    fuentes = {base / n: n for n in ["_quarto.yml", "cartera.csv", "parametros.json", "estilos.css", "verificar.py", "copiar_fuentes.py", "construir.py"]}
    fuentes.update({base / "reporte_python.qmd": "reporte.qmd", base / "LEEME_fuentes.md": "README.md",
                    base.parent / "05_parameters_cutoffs/analisis.py": "analisis.py",
                    repo / "pyproject.toml": "pyproject.toml", repo / "uv.lock": "uv.lock"})
    if not all(p.is_file() for p in fuentes):
        raise FileNotFoundError("Faltan fuentes de 11.09 o configuración del curso")
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    for origen, nombre in fuentes.items():
        shutil.copyfile(origen, destino / nombre)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    preparar(parser.parse_args().destino)

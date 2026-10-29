"""Reúne 60 fuentes en carpeta nueva. No instala, ejecuta ni activa CI."""
from pathlib import Path
import argparse
import csv
import runpy
import shutil

BASE = Path(__file__).resolve().parent
EXTRAS = ("entrega.py", "entrega.R", "reconstruir.py", "reconstruir.R", "catalogo.csv", "CI_EJEMPLO.yml", "LEEME_ENTREGA.md")


def fuentes():
    anterior = runpy.run_path(str(BASE.parent / "07_report_app_integration/preparar.py"))
    propias = {"pipeline.py", "pipeline.R", "LEEME.md"}
    pares = [(BASE / "plantilla" / r if r in propias else p,
              "producto_1408.Rproj" if r == "producto_1407.Rproj" else r) for p, r in anterior["fuentes"]()]
    return pares + [(BASE / "plantilla" / r, r) for r in EXTRAS]


def preparar(destino, app="streamlit"):
    if app not in ("streamlit", "shiny"):
        raise ValueError("Elegir streamlit o shiny")
    destino = Path(destino).absolute()
    if destino.exists() or destino.is_symlink():
        raise ValueError("Destino ocupado; conservar y elegir otro")
    pares = fuentes()
    if not all(p.is_file() for p, _ in pares):
        raise ValueError("Faltan fuentes")
    destino.mkdir(parents=True, exist_ok=False)
    for origen, relativa in pares:
        final = destino / relativa; final.parent.mkdir(parents=True, exist_ok=True)
        with origen.open("rb") as entrada, final.open("xb") as salida:
            shutil.copyfileobj(entrada, salida)
    anterior = runpy.run_path(str(BASE.parent / "07_report_app_integration/preparar.py"))
    anterior["configuraciones"](destino, app)
    print("60 fuentes; lee LEEME.md. No se instalaron paquetes ni se habilito CI.")
    return destino


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("destino")
    p.add_argument("--app", choices=["streamlit", "shiny"], default="streamlit")
    a = p.parse_args(); preparar(a.destino, a.app)

"""Prepara 31 fuentes en carpeta nueva; no copia entornos ni resultados."""
from pathlib import Path
import runpy
import argparse
import shutil
BASE = Path(__file__).resolve().parent

def fuentes():
    anteriores = runpy.run_path(str(BASE.parent / "04_pipeline_reprocessing/preparar.py"))["fuentes"]()
    pares = [(BASE / "plantilla/LEEME.md" if r == "LEEME.md" else p, "producto_1405.Rproj" if r == "producto_1404.Rproj" else r) for p, r in anteriores]
    return pares + [(BASE / "plantilla" / r, r) for r in ("pruebas.py", "pruebas.R", "referencia/calidad.csv")]

def preparar(destino):
    destino = Path(destino).absolute()
    if destino.exists() or destino.is_symlink(): raise ValueError("El destino existe; elegir otra carpeta")
    pares = fuentes()
    if len(pares) != 31 or not all(p.is_file() for p, _ in pares): raise ValueError("Faltan fuentes")
    destino.mkdir(parents=True, exist_ok=False)
    for p, r in pares:
        final = destino / r; final.parent.mkdir(parents=True, exist_ok=True)
        with p.open("rb") as entrada, final.open("xb") as salida: shutil.copyfileobj(entrada, salida)
    print("31 fuentes copiadas; lee LEEME.md antes de restaurar.")
    return destino

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("destino")
    preparar(p.parse_args().destino)

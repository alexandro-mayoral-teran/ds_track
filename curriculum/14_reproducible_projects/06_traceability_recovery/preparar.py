"""Prepara 33 fuentes en carpeta nueva; conserva el pipeline y las pruebas 14.05."""
from pathlib import Path
import argparse
import runpy
import shutil

BASE = Path(__file__).resolve().parent


def fuentes():
    anteriores = runpy.run_path(str(BASE.parent / "05_tests_data_quality/preparar.py"))["fuentes"]()
    pares = [(BASE / "plantilla/LEEME.md" if r == "LEEME.md" else p,
              "producto_1406.Rproj" if r == "producto_1405.Rproj" else r)
             for p, r in anteriores]
    return pares + [(BASE / "plantilla" / r, r) for r in ("trazar.py", "trazar.R")]


def preparar(destino):
    destino = Path(destino).absolute()
    if destino.exists() or destino.is_symlink():
        raise ValueError("El destino existe; elegir otra carpeta")
    pares = fuentes()
    if len(pares) != 33 or not all(p.is_file() for p, _ in pares):
        raise ValueError("Faltan fuentes")
    destino.mkdir(parents=True, exist_ok=False)
    for origen, relativa in pares:
        final = destino / relativa
        final.parent.mkdir(parents=True, exist_ok=True)
        with origen.open("rb") as entrada, final.open("xb") as salida:
            shutil.copyfileobj(entrada, salida)
    print("33 fuentes copiadas; lee LEEME.md antes de restaurar.")
    return destino


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("destino")
    preparar(p.parse_args().destino)

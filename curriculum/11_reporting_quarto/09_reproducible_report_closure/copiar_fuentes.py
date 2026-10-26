"""Copiar solo fuentes a un destino nuevo; no verifica ni construye resultados."""
import argparse
from pathlib import Path
import shutil
from verificar import fuentes


def copiar(origen, destino, motor):
    origen, destino = Path(origen), Path(destino)
    nombres = fuentes(motor)
    if not all((origen / n).is_file() for n in nombres):
        raise FileNotFoundError("Faltan fuentes de la entrega")
    destino.mkdir(parents=True, exist_ok=False)
    for n in nombres:
        (destino / n).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origen / n, destino / n)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("origen", type=Path)
    p.add_argument("destino", type=Path)
    p.add_argument("--motor", choices=["python", "r"], required=True)
    a = p.parse_args()
    copiar(a.origen, a.destino, a.motor)

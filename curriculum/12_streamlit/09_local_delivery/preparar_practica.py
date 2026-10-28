"""Reúne fuentes existentes y metadatos para una práctica nueva de 12.09."""

import argparse
import importlib.util
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent
RAIZ = BASE.parents[2]


def preparar(destino):
    fuentes = [(BASE / "entrega.py", "entrega.py"),
               (BASE / "LEEME.md", "README.md"),
               (RAIZ / "pyproject.toml", "pyproject.toml"),
               (RAIZ / "uv.lock", "uv.lock")]
    for fuente, _ in fuentes:
        if not fuente.is_file():
            raise FileNotFoundError(f"Falta una fuente: {fuente}")
    ruta = BASE.parent / "08_app_testing" / "preparar_practica.py"
    spec = importlib.util.spec_from_file_location("preparador_1208", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    destino = modulo.preparar(destino)
    for fuente, nombre in fuentes:
        shutil.copyfile(fuente, destino / nombre)
    return destino


def main():
    parser = argparse.ArgumentParser(description="Crear una práctica NUEVA para 12.09.")
    parser.add_argument("destino", type=Path)
    args = parser.parse_args()
    try:
        destino = preparar(args.destino)
    except OSError as error:
        parser.error(str(error))
    print(f"Práctica preparada en: {destino}")
    print("Continúa con entrega.py crear; no se inició un servidor ni se instaló nada.")


if __name__ == "__main__":
    main()

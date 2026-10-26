"""Preparar una copia personal 02.01; no instala paquetes ni ejecuta el notebook."""
import argparse
import json
from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parents[2]
CATALOGO = REPO / "portal/sesiones.json"


def catalogo():
    datos = json.loads(CATALOGO.read_text(encoding="utf-8"))
    for ruta in [datos["leccion"], datos["lab"], *datos["practica"].values(), *datos["consulta"]]:
        path = (REPO / ruta).resolve()
        if not path.is_relative_to(REPO) or not path.is_file():
            raise ValueError(f"Fuente fuera del repositorio o inexistente: {ruta}")
    return datos


def preparar(destino):
    datos = catalogo()
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    for nombre, ruta in datos["practica"].items():
        if Path(nombre).name != nombre:
            raise ValueError("El nombre de una descarga debe ser un archivo simple")
        shutil.copyfile(REPO / ruta, destino / nombre)
    print(f"Copia personal preparada: {destino.resolve()}")
    print("Abre ABRIR.md y selecciona el kernel de tu entorno de estudio.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("destino", type=Path)
    preparar(p.parse_args().destino)

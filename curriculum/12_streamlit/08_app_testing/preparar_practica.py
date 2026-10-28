"""Reutiliza las fuentes de 12.07 y añade los ejemplos de pruebas de 12.08."""

import argparse
import importlib.util
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent


def preparar(destino):
    """Crea un destino nuevo; no instala, arranca servidores ni ejecuta pruebas."""
    anteriores = BASE.parent / "07_tables_charts_download" / "preparar_practica.py"
    especificacion = importlib.util.spec_from_file_location("preparador_1207", anteriores)
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    fuentes = [BASE / nombre for nombre in
               ("minimo_pruebas.py", "pruebas_modelo.py", "pruebas_app.py")]
    for fuente in fuentes + [BASE / "minimo.py"]:
        if not fuente.is_file():
            raise FileNotFoundError(f"Falta una fuente: {fuente}")
    destino = modulo.preparar(destino)
    # El mínimo de esta sección sustituye solo al mínimo de la copia recién creada.
    shutil.copyfile(BASE / "minimo.py", destino / "minimo.py")
    for fuente in fuentes:
        shutil.copyfile(fuente, destino / fuente.name)
    return destino


def main():
    parser = argparse.ArgumentParser(description="Crear una copia NUEVA para 12.08.")
    parser.add_argument("destino", type=Path)
    args = parser.parse_args()
    try:
        destino = preparar(args.destino)
    except OSError as error:
        parser.error(str(error))
    print(f"Práctica preparada en: {destino}")
    print("Continúa con minimo_pruebas.py; no se inició ningún servidor.")


if __name__ == "__main__":
    main()

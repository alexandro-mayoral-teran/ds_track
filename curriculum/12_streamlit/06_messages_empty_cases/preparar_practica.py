"""Crea una copia nueva con el modelo de 12.03 y las interfaces de 12.06."""

import argparse
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent
MODELO = BASE.parent / "03_data_interface"


def preparar(destino):
    """No ejecuta apps, instala paquetes, sobrescribe ni modifica las fuentes."""
    destino = Path(destino).resolve()
    fuentes = [MODELO / nombre for nombre in
               ("cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py")]
    fuentes += [BASE.parent / "05_data_resource_cache" / "cache_analisis.py"]
    fuentes += [BASE / nombre for nombre in ("app.py", "entradas.py", "minimo.py")]
    for fuente in fuentes:
        if not fuente.is_file():
            raise FileNotFoundError(f"Falta una fuente del repositorio: {fuente}")
    destino.mkdir(parents=True, exist_ok=False)
    for fuente in fuentes:
        shutil.copyfile(fuente, destino / fuente.name)
    return destino


def main():
    parser = argparse.ArgumentParser(description="Preparar una carpeta NUEVA para el lab 12.06.")
    parser.add_argument("destino", type=Path, help="Carpeta que todavía no existe.")
    args = parser.parse_args()
    try:
        destino = preparar(args.destino)
    except OSError as error:
        parser.error(str(error))
    print(f"Práctica preparada en: {destino}")
    print("No se inició el servidor. Continúa con los recorridos de la lección 12.06.")


if __name__ == "__main__":
    main()

"""Copia explicita de 13 archivos, sin instalar ni ejecutar el producto."""
from pathlib import Path
import shutil
import argparse

BASE = Path(__file__).resolve().parent
PREVIA = BASE.parent / "01_product_question_contract"
PROPIOS = ["LEEME.md", "revisar.py", "revisar.R", "config/consulta.csv",
    "codigo/modelo.py", "codigo/modelo.R", "codigo/configuracion.py", "codigo/configuracion.R", "salidas/LEEME.md"]
PREVIOS = {"ESPECIFICACION.md": "docs/ESPECIFICACION.md", "plantilla_contrato.md": "docs/plantilla_contrato.md",
    "cartera.csv": "datos/entrada/cartera.csv", "criterios.csv": "referencia/criterios.csv"}

def preparar(destino):
    destino = Path(destino).absolute()
    if destino.exists() or destino.is_symlink():
        raise ValueError("El destino existe; conservarlo y elegir otro")
    fuentes = [(BASE / "plantilla" / p, p) for p in PROPIOS] + [(PREVIA / a, b) for a, b in PREVIOS.items()]
    if not all(a.is_file() for a, _ in fuentes):
        raise ValueError("Faltan fuentes de la seccion")
    destino.mkdir(parents=True, exist_ok=False)
    for fuente, relativa in fuentes:
        final = destino / relativa
        final.parent.mkdir(parents=True, exist_ok=True)
        with fuente.open("rb") as entrada, final.open("xb") as salida:
            shutil.copyfileobj(entrada, salida)
    print(f"13 archivos copiados en {destino}. Sin instalar; lee LEEME.md.")
    return destino

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino")
    preparar(parser.parse_args().destino)

"""Prepara 26 fuentes en carpeta nueva; no copia entornos ni instala paquetes."""
from pathlib import Path
import shutil
import argparse
BASE = Path(__file__).resolve().parent
REPO = BASE.parents[2]

def fuentes():
    previa = BASE.parent / "02_structure_configuration" / "plantilla"
    contrato = BASE.parent / "01_product_question_contract"
    pares = [(previa / p, p) for p in ["revisar.py", "revisar.R", "config/consulta.csv", "codigo/modelo.py", "codigo/modelo.R", "codigo/configuracion.py", "codigo/configuracion.R", "salidas/LEEME.md"]]
    pares += [(contrato / a, b) for a, b in {"ESPECIFICACION.md":"docs/ESPECIFICACION.md", "plantilla_contrato.md":"docs/plantilla_contrato.md", "cartera.csv":"datos/entrada/cartera.csv", "criterios.csv":"referencia/criterios.csv"}.items()]
    pares += [(BASE / p, p) for p in ["LEEME.md", "ejecutar.py", "ejecutar.R", "entorno.csv"]]
    pares += [(BASE / "entorno_python" / p, p) for p in ["pyproject.toml", "uv.lock", ".python-version"]]
    pares += [(BASE / "entorno_r" / p, p) for p in ["DESCRIPTION", "renv.lock", "restaurar.R"]]
    plantilla = REPO / "curriculum/06_r_foundations/08_projects_renv/plantilla"
    pares += [(plantilla / p, p) for p in [".Rprofile", "renv/activate.R", "renv/settings.json"]]
    pares += [(REPO / "curriculum/13_shiny_web/01_web_first_app/shiny_1301.Rproj", "producto_1403.Rproj")]
    return pares

def preparar(destino):
    destino = Path(destino).absolute()
    if destino.exists() or destino.is_symlink(): raise ValueError("El destino existe; conservarlo y elegir otro")
    pares = fuentes()
    if len(pares) != 26 or not all(p.is_file() for p, _ in pares): raise ValueError("Faltan fuentes del curso")
    destino.mkdir(parents=True, exist_ok=False)
    for fuente, relativa in pares:
        final = destino / relativa; final.parent.mkdir(parents=True, exist_ok=True)
        with fuente.open("rb") as entrada, final.open("xb") as salida: shutil.copyfileobj(entrada, salida)
    print(f"26 fuentes en {destino}. No se instalaron paquetes; lee LEEME.md.")
    return destino

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("destino")
    preparar(parser.parse_args().destino)

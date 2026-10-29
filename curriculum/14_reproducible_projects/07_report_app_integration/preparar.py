"""Prepara el producto y sus dos interfaces en carpeta nueva; no instala."""
from pathlib import Path
import argparse
import csv
import runpy
import shutil

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[2]


def fuentes():
    anteriores = runpy.run_path(str(BASE.parent / "06_traceability_recovery/preparar.py"))["fuentes"]()
    propias = {"pipeline.py", "pipeline.R", "LEEME.md"}
    pares = [(BASE / "plantilla" / r if r in propias else p,
              "producto_1407.Rproj" if r == "producto_1406.Rproj" else r) for p, r in anteriores]
    nuevas = ["integracion.py", "integracion.R", ".renvignore", "interfaz/python/app.py", "interfaz/python/pyproject.toml", "interfaz/python/uv.lock", "interfaz/python/.python-version", "interfaz/r/app.R"]
    pares += [(BASE / "plantilla" / r, r) for r in nuevas]
    shiny = REPO / "curriculum/13_shiny_web/01_web_first_app"
    pares += [(shiny / r, "interfaz/r/" + r) for r in ["DESCRIPTION", "renv.lock", "restaurar.R", "iniciar.R"]]
    renv = REPO / "curriculum/06_r_foundations/08_projects_renv/plantilla"
    pares += [(renv / r, "interfaz/r/" + r) for r in [".Rprofile", "renv/activate.R", "renv/settings.json"]]
    pares += [(shiny / "shiny_1301.Rproj", "interfaz/r/interfaz_1407.Rproj")]
    return pares


def configuraciones(destino, app):
    with (destino / "config/consulta.csv").open(encoding="utf-8", newline="") as f:
        original = {f["clave"]: f["valor"] for f in csv.DictReader(f)}
    casos = {"octubre": {}, "septiembre": {"corte": "2026-09-30"},
             "vacio": {"segmentos": "servicios", "minimo_texto": "1901"}, "sinuniverso": {"corte": "2026-11-30"}}
    for nombre, cambios in casos.items():
        cfg = dict(original, app=app, salida="salidas/" + nombre + "_integrado", **cambios)
        with (destino / "config" / (nombre + ".csv")).open("x", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n"); w.writerow(["clave", "valor"]); w.writerows(cfg.items())


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
    configuraciones(destino, app)
    print(len(pares) + 4, "fuentes; lee LEEME.md. Ruta elegida:", app)
    return destino


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("destino")
    p.add_argument("--app", choices=["streamlit", "shiny"], default="streamlit")
    a = p.parse_args(); preparar(a.destino, a.app)

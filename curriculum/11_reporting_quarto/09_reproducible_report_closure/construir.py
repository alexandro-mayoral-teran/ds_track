"""Construir una entrega nueva desde su raíz; no reemplaza resultados anteriores."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from verificar import leer_parametros, leer_csv, huellas, verificar


def construir(quarto):
    raiz = Path(__file__).resolve().parent
    if Path.cwd().resolve() != raiz:
        raise ValueError("Ejecuta desde la raíz de la copia preparada")
    if any((raiz / n).exists() for n in ["salida", "reporte.html", "huellas.json", "render.log", "comando.txt"]):
        raise FileExistsError("Entrega iniciada u ocupada: conservar y preparar otra copia")
    p = leer_parametros(raiz / "parametros.json")
    leer_csv(raiz / "cartera.csv")
    version = subprocess.check_output([quarto, "--version"], text=True).strip()
    argumentos = ["render", "reporte.qmd", "--to", "html", "--execute-params", "parametros.json", "--cache-refresh"]
    (raiz / "comando.txt").write_text("Quarto " + version + "\nquarto " + " ".join(argumentos) + "\n", encoding="utf-8")
    env = {**os.environ, "QUARTO_PYTHON": sys.executable}
    with (raiz / "render.log").open("w", encoding="utf-8") as log:
        proceso = subprocess.run([quarto, *argumentos], env=env, stdout=log, stderr=subprocess.STDOUT)
    if proceso.returncode:
        raise RuntimeError("Falló el render; conserva render.log y la copia parcial")
    (raiz / "huellas.json").write_text(json.dumps(huellas(raiz, "python"), indent=2), encoding="utf-8")
    verificar(raiz, raiz / "cartera.csv", p["fecha_corte"], p["minimo_mxn"])
    print("Construcción comprobada contra su entrada local. Contrastar después con referencia externa.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quarto", default="quarto")
    construir(parser.parse_args().quarto)

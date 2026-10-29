"""Reconstrucción explícita después de revisar las fuentes y restaurar la raíz."""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys
from ejecutar import RAIZ, verificar_entorno
from trazar import trazar
from integracion import generar, renderizar
from modelo import leer


def reconstruir(quarto=None):
    verificar_entorno()
    ejecutable = quarto or shutil.which("quarto")
    if not ejecutable:
        candidato = Path("C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe")
        ejecutable = str(candidato) if candidato.is_file() else None
    if not ejecutable or not Path(ejecutable).is_file():
        raise ValueError("Quarto existente requerido; indicar --quarto")
    casos = ("octubre", "septiembre", "vacio")
    for caso in casos:
        for ruta in (RAIZ / "salidas" / (caso + "_integrado"), RAIZ / "reportes" / caso,
                     RAIZ / "intentos" / ("recon_" + caso)):
            if ruta.exists() or ruta.is_symlink():
                raise ValueError("Reconstruccion ocupada o parcial; conservar y usar otra copia nueva")
    subprocess.run([sys.executable, "pruebas.py"], cwd=RAIZ, check=True)
    for caso in casos:
        archivo = "config/" + caso + ".csv"
        _, filas = leer(RAIZ / archivo)
        app = {f["clave"]: f["valor"] for f in filas}["app"]
        if app != "streamlit":
            raise ValueError("Esta ruta reconstruye Python/Streamlit; elige R para Shiny")
        trazar("recon_" + caso, archivo)
        generar(caso, archivo, app)
        renderizar(caso, archivo, app, ejecutable)
    print("Tres consultas y tres HTML reconstruidos. La app se inicia por separado.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--quarto")
    reconstruir(p.parse_args().quarto)

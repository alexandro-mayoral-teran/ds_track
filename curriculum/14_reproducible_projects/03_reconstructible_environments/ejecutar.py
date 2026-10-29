"""Consulta de 14.02 + evidencia nueva del entorno. No genera reporte/app."""
from pathlib import Path
import sys
import platform
import site
import hashlib
import csv
import shutil
import subprocess
import argparse
from datetime import datetime, timezone
sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parent
from revisar import revisar
from modelo import leer

def ejecutar(evidencia, archivo="config/consulta.csv"):
    columnas, filas = leer(RAIZ / "entorno.csv")
    claves = {"esquema", "python", "r", "dependencias_python", "dependencias_r"}
    if columnas != ["clave", "valor"] or len(filas) != 5 or {f["clave"] for f in filas} != claves:
        raise ValueError("Declaracion de entorno incompatible")
    declarado = {f["clave"]: f["valor"] for f in filas}
    if declarado["esquema"] != "1403-v1" or declarado["dependencias_python"] != "ninguna_externa":
        raise ValueError("Esquema/dependencias no implementados")
    if platform.python_version() != declarado["python"]:
        raise ValueError("Version Python distinta de la declarada")
    if sys.prefix == sys.base_prefix or Path(sys.prefix).resolve() != (RAIZ / ".venv").resolve() or site.ENABLE_USER_SITE:
        raise ValueError("Usa el Python de .venv de esta copia, sin paquetes de usuario")
    if "include-system-site-packages = false" not in (Path(sys.prefix) / "pyvenv.cfg").read_text().lower():
        raise ValueError("No se admite incluir paquetes del entorno base")
    import re
    if not re.fullmatch(r"evidencia/[a-z][a-z0-9_-]{0,39}\.csv", evidencia):
        raise ValueError("Evidencia: evidencia/nombre_nuevo.csv")
    destino = RAIZ / evidencia
    if destino.exists() or destino.is_symlink():
        raise ValueError("La evidencia existe; conservarla y elegir otro nombre")
    if destino.parent.exists() and (destino.parent.resolve() != RAIZ / "evidencia"):
        raise ValueError("Carpeta de evidencia enlazada a otro lugar")
    resultado = revisar(archivo)
    columnas, filas_config = leer(RAIZ / archivo)
    config = {f["clave"]: f["valor"] for f in filas_config}
    registro = {"esquema": "1403-v1", "fecha_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": "python", "version": platform.python_version(), "ejecutable": sys.executable,
        "raiz": str(RAIZ), "entorno_local": sys.prefix, "sistema": platform.platform(),
        "dependencias_calculo": "biblioteca_estandar", "paquetes_usuario": str(site.ENABLE_USER_SITE)}
    quarto = shutil.which("quarto")
    registro["quarto_ruta"] = quarto or "no_disponible_en_PATH"
    if quarto:
        p = subprocess.run([quarto, "--version"], capture_output=True, text=True, timeout=15)
        registro["quarto_version"] = p.stdout.strip() if p.returncode == 0 else "error_al_consultar"
    else:
        registro["quarto_version"] = "no_consultada"
    for clave, valor in config.items():
        registro["config." + clave] = valor
    for clave, valor in resultado.items():
        registro["resultado." + clave] = valor
    for clave, ruta in {"entrada": RAIZ / config["entrada"], "config": RAIZ / archivo,
        "declaracion": RAIZ / "entorno.csv", "lockfile": RAIZ / "uv.lock"}.items():
        registro["md5." + clave] = hashlib.md5(ruta.read_bytes()).hexdigest()
    destino.parent.mkdir(exist_ok=True)
    with destino.open("x", encoding="utf-8", newline="") as salida:
        escritor = csv.writer(salida); escritor.writerow(["clave", "valor"]); escritor.writerows(registro.items())
    print(f"Evidencia nueva: {destino}. No autentica sesiones pasadas.")
    return resultado

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidencia")
    parser.add_argument("--config", default="config/consulta.csv")
    args = parser.parse_args()
    ejecutar(args.evidencia, args.config)

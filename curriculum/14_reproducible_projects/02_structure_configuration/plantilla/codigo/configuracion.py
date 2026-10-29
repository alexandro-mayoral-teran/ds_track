"""Configuracion explicita; importar no lee ni escribe archivos."""
from pathlib import Path
import re
from modelo import leer, fecha_valida

CLAVES = {"version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida"}

def relativa(texto):
    partes = texto.split("/")
    if not re.fullmatch(r"[A-Za-z0-9_-]+(/[A-Za-z0-9_. -]+)+", texto) or any(p in (".", "..") or p.endswith((".", " ")) for p in partes):
        raise ValueError("Ruta: usa componentes relativos con /, sin . ni ..")
    return Path(*partes)

def existente(raiz, texto):
    ruta = (raiz / relativa(texto)).resolve(strict=True)
    if not ruta.is_relative_to(raiz) or not ruta.is_file():
        raise ValueError("Archivo fuera del proyecto o no regular")
    return ruta

def leer_configuracion(raiz, archivo="config/consulta.csv"):
    raiz = Path(raiz).resolve(strict=True)
    if not raiz.is_dir():
        raise ValueError("Indica una carpeta de proyecto")
    if not archivo.startswith("config/") or not archivo.endswith(".csv"):
        raise ValueError("Configuracion: archivo CSV dentro de config/")
    columnas, filas = leer(existente(raiz, archivo))
    if columnas != ["clave", "valor"] or {f["clave"] for f in filas} != CLAVES or len(filas) != len(CLAVES):
        raise ValueError("Configuracion: claves exactas, sin ausencias, extras ni repeticiones")
    config = {f["clave"]: f["valor"] for f in filas}
    if config["version_reglas"] != "1401-v1":
        raise ValueError("Version de reglas no implementada")
    if not fecha_valida(config["corte"]) or config["segmentos"] not in ("ninguno", "comercio", "servicios", "comercio|servicios", "servicios|comercio"):
        raise ValueError("Corte o segmentos invalidos")
    minimo = config["minimo_texto"]
    if not re.fullmatch(r"0|[1-9][0-9]{0,6}", minimo) or int(minimo) > 1000000:
        raise ValueError("Minimo: entero canonico 0..1000000")
    if config["app"] not in ("streamlit", "shiny"):
        raise ValueError("Elige una app: streamlit o shiny")
    if not config["entrada"].startswith("datos/entrada/") or not config["entrada"].endswith(".csv"):
        raise ValueError("Entrada: CSV dentro de datos/entrada/")
    entrada = existente(raiz, config["entrada"])
    if not re.fullmatch(r"salidas/[a-z][a-z0-9_-]{0,39}", config["salida"]):
        raise ValueError("Salida: salidas/nombre_simple")
    padre = (raiz / "salidas").resolve(strict=True)
    if not padre.is_relative_to(raiz) or not padre.is_dir():
        raise ValueError("Carpeta salidas fuera del proyecto o ausente")
    salida = padre / config["salida"].split("/")[1]
    if salida.exists() or salida.is_symlink():
        raise ValueError("Salida ocupada: elegir otro nombre; no se sobrescribe")
    return dict(config, raiz=raiz, entrada_resuelta=entrada, salida_resuelta=salida)

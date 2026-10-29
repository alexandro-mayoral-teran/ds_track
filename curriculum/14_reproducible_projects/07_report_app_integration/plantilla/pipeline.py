"""14.07: cálculo compartido; construir o comprobar una entrega inmutable de una consulta."""
from pathlib import Path
import argparse
import csv
import hashlib
import tempfile
from ejecutar import RAIZ, verificar_entorno
from configuracion import leer_configuracion
from modelo import cargar_fuente, resolver, leer


def md5(ruta):
    return hashlib.md5(Path(ruta).read_bytes()).hexdigest()


def escribir(ruta, tabla):
    with ruta.open("x", encoding="utf-8", newline="") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerows(tabla)


def comprobar(carpeta, tablas):
    nombres = set(tablas) | {"COMPLETO.csv"}
    if not carpeta.is_dir() or {p.name for p in carpeta.iterdir()} != nombres:
        raise ValueError("Entrega incompleta o con archivos extra; conservar y usar otro destino")
    for nombre, esperado in tablas.items():
        ruta = carpeta / nombre
        if ruta.is_symlink() or not ruta.is_file():
            raise ValueError("Archivo de entrega no regular")
        columnas, filas = leer(ruta)
        actual = [columnas] + [[f[c] for c in columnas] for f in filas]
        if actual != esperado:
            raise ValueError("La entrega difiere del calculo actual: " + nombre)
    marca = carpeta / "COMPLETO.csv"
    if marca.is_symlink() or not marca.is_file():
        raise ValueError("Marca no regular")
    columnas, filas = leer(marca)
    if columnas != ["archivo", "md5"] or filas != [
        {"archivo": n, "md5": md5(carpeta / n)} for n in tablas
    ]:
        raise ValueError("Marca o huellas incorrectas")


def tablas_esperadas(archivo="config/consulta.csv"):
    cfg = leer_configuracion(RAIZ, archivo, permitir_existente=True)
    destino = cfg["salida_resuelta"]
    if destino.exists() and destino.resolve() != destino:
        raise ValueError("Destino enlazado")
    datos = cargar_fuente(cfg["entrada_resuelta"])
    resultado = resolver(datos, cfg["corte"], cfg["segmentos"], cfg["minimo_texto"])
    if resultado["estado"] not in ("ok", "vacio"):
        raise ValueError("Consulta sin universo o invalida: no se publica una entrega")
    campos = ["id_credito", "segmento", "fecha_corte", "saldo_mxn"]
    ids = set(resultado["ids"].split("|")) if resultado["ids"] else set()
    seleccion = sorted((f for f in datos if f["fecha_corte"] == cfg["corte"] and f["id_credito"] in ids), key=lambda f: f["id_credito"])
    contexto = {k: cfg[k] for k in ("version_reglas", "corte", "segmentos", "minimo_texto", "app")}
    contexto.update({k: v for k, v in resultado.items() if k not in ("ids", "saldos_mxn")})
    contexto["porcentaje_creditos"] = format(float(resultado["porcentaje_creditos"]), ".15g")
    insumos = {"esquema": "1404-v1", "motor": "python", "version_reglas": cfg["version_reglas"]}
    for nombre, ruta in {"entrada": cfg["entrada_resuelta"], "config": RAIZ / archivo,
                         "modelo": RAIZ / "codigo/modelo.py", "pipeline": RAIZ / "pipeline.py",
                         "configuracion": RAIZ / "codigo/configuracion.py"}.items():
        insumos["md5." + nombre] = md5(ruta)
    tablas = {
        "seleccion.csv": [campos] + [[f[c] for c in campos] for f in seleccion],
        "contexto.csv": [list(contexto), list(contexto.values())],
        "insumos.csv": [["clave", "valor"]] + [[k, v] for k, v in insumos.items()],
    }
    return cfg, tablas


def pipeline(archivo="config/consulta.csv", simular_fallo=False):
    verificar_entorno()
    cfg, tablas = tablas_esperadas(archivo)
    destino = cfg["salida_resuelta"]
    if destino.exists():
        comprobar(destino, tablas)
        print("Reutilizada y comprobada:", destino)
        return "reutilizada"
    temporal = Path(tempfile.mkdtemp(prefix=".pendiente-", dir=destino.parent))
    print("Preparando:", temporal)
    escribir(temporal / "seleccion.csv", tablas["seleccion.csv"])
    if simular_fallo:
        raise RuntimeError("Fallo didactico: temporal conservado, sin entrega final")
    for nombre in ("contexto.csv", "insumos.csv"):
        escribir(temporal / nombre, tablas[nombre])
    escribir(temporal / "COMPLETO.csv", [["archivo", "md5"]] + [[n, md5(temporal / n)] for n in tablas])
    comprobar(temporal, tablas)
    if destino.exists():
        raise ValueError("Destino ocupado durante la ejecucion; temporal conservado")
    temporal.rename(destino)
    print("Creada y comprobada:", destino)
    return "creada"


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default="config/consulta.csv")
    p.add_argument("--simular-fallo", action="store_true")
    a = p.parse_args()
    pipeline(a.config, a.simular_fallo)

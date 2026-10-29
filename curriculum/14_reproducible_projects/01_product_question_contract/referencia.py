"""Aritmetica independiente para revisar el contrato 14.01; solo lee e imprime.

No genera reporte/app ni valida el argumento humano de la especificacion.
"""
import csv
from datetime import date
from pathlib import Path
import re
import math

BASE = Path(__file__).resolve().parent
COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn"]
MEDIDAS = ["ids", "saldos_mxn", "creditos_universo", "creditos_seleccion", "saldo_universo_mxn", "saldo_seleccion_mxn", "porcentaje_creditos"]

def leer(ruta):
    with Path(ruta).open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.reader(archivo, strict=True)
        columnas = next(lector, [])
        valores = list(lector)
        if any(len(f) != len(columnas) for f in valores):
            raise ValueError("Fila con ancho distinto del encabezado")
        return columnas, [dict(zip(columnas, f)) for f in valores]

def fecha_valida(texto):
    try:
        return bool(re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", texto)) and date.fromisoformat(texto).isoformat() == texto and "1900-01-01" <= texto <= "2100-12-31"
    except ValueError:
        return False

def cargar_fuente(ruta):
    columnas, filas = leer(ruta)
    if columnas != COLUMNAS or len(filas) > 10000:
        raise ValueError("Fuente: esquema o cantidad fuera del contrato")
    claves = set()
    for f in filas:
        if not re.fullmatch(r"[0-9]{3}", f["id_credito"]) or f["segmento"] not in ("comercio", "servicios") or not fecha_valida(f["fecha_corte"]):
            raise ValueError("Fuente: ID, segmento o fecha invalida")
        if not re.fullmatch(r"0|[1-9][0-9]{0,6}", f["saldo_mxn"]) or int(f["saldo_mxn"]) > 1000000:
            raise ValueError("Fuente: saldo invalido")
        clave = f["id_credito"], f["fecha_corte"]
        if clave in claves:
            raise ValueError("Fuente: clave repetida")
        claves.add(clave)
    return filas

def resolver(filas, corte, segmentos, minimo):
    salida = dict.fromkeys(MEDIDAS, "")
    segs = [] if segmentos == "ninguno" else segmentos.split("|")
    valido = fecha_valida(corte) and bool(re.fullmatch(r"0|[1-9][0-9]{0,6}", minimo))
    valido = valido and int(minimo) <= 1000000 and len(segs) == len(set(segs)) and all(s in ("comercio", "servicios") for s in segs)
    if not valido:
        return dict(estado="rechazo", **salida)
    universo = [f for f in filas if f["fecha_corte"] == corte]
    if not universo:
        return dict(estado="sin_universo", **salida)
    seleccion = sorted((f for f in universo if f["segmento"] in segs and int(f["saldo_mxn"]) >= int(minimo)), key=lambda f: f["id_credito"])
    return dict(estado="ok" if seleccion else "vacio", ids="|".join(f["id_credito"] for f in seleccion),
        saldos_mxn="|".join(f["saldo_mxn"] for f in seleccion),
        creditos_universo=str(len(universo)), creditos_seleccion=str(len(seleccion)),
        saldo_universo_mxn=str(sum(int(f["saldo_mxn"]) for f in universo)),
        saldo_seleccion_mxn=str(sum(int(f["saldo_mxn"]) for f in seleccion)),
        porcentaje_creditos=str(100 * len(seleccion) / len(universo)))

def comprobar(carpeta=BASE):
    carpeta = Path(carpeta)
    filas = cargar_fuente(carpeta / "cartera.csv") # Toda la fuente antes de filtrar.
    columnas, casos = leer(carpeta / "criterios.csv")
    if columnas != ["caso", "corte", "segmentos", "minimo_texto", "estado", *MEDIDAS] or not casos:
        raise ValueError("Criterios: esquema o lista vacia")
    if any(not f["caso"] for f in casos) or len({f["caso"] for f in casos}) != len(casos):
        raise ValueError("Criterios: nombres ausentes o repetidos")
    for caso in casos:
        real = resolver(filas, caso["corte"], caso["segmentos"], caso["minimo_texto"])
        for clave, valor in real.items():
            esperado = caso[clave]
            igual = math.isclose(float(valor), float(esperado), rel_tol=1e-12) if clave == "porcentaje_creditos" and valor and esperado else valor == esperado
            if not igual:
                raise ValueError(f"{caso['caso']}: {clave}; esperado={esperado!r}, calculado={valor!r}")
        print(f"OK {caso['caso']}: {real['estado']} IDs={real['ids'] or '(ninguno/publicacion ausente)'}")
    print(f"{len(casos)} criterios numericos conciliados. La especificacion requiere revision humana.")
    return len(casos)

if __name__ == "__main__":
    comprobar()

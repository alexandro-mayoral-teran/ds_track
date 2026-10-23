"""Referencia de consulta con Python estandar; no importa motores tabulares.

Importar no lee datos ni escribe. Las reglas existentes se reutilizan sin pedir
entregas de otros capitulos. Comparar resultados no mide rendimiento.
"""

import argparse
import csv
from datetime import date
import importlib.util
import json
from pathlib import Path
import re

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
COMUN = CARPETA.parents[1] / "09_arrow_parquet/01_csv_parquet_arrow/datos/base_comun.csv"
_spec = importlib.util.spec_from_file_location("reglas_1001",
    CARPETA.parents[1] / "09_arrow_parquet/02_schemas_types/contrato_tabla.py")
reglas = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reglas)


def cargar_filas(ruta=FUENTE):
    """Rechaza el lote completo ante una incidencia; no limpia ni filtra errores."""
    evaluadas = reglas.evaluar_contrato(reglas.leer_textos(ruta, reglas.COLUMNAS))
    fallos = [(i, f["motivos"]) for i, f in enumerate(evaluadas, 1) if not f["aceptado"]]
    if fallos:
        raise ValueError(f"Fuente fuera del contrato (fila, motivos): {fallos}")
    return [dict(id_credito=f["original"]["id_credito"], fecha_corte=f["fecha"],
                 saldo_mxn=f["saldo"]) for f in evaluadas]


def validar_parametros(corte, minimo):
    if type(corte) is not date or not date(1900, 1, 1) <= corte <= date(2100, 12, 31):
        raise ValueError("corte debe ser date entre 1900 y 2100, sin hora")
    if type(minimo) is not int or not 0 <= minimo <= reglas.MAXIMO:
        raise ValueError("minimo debe ser entero no negativo dentro de int32")


def construir_referencia(ruta=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    validar_parametros(corte, minimo)
    filas = cargar_filas(ruta)
    seleccion = []
    for fila in filas:
        if fila["fecha_corte"] == corte and fila["saldo_mxn"] >= minimo:
            seleccion.append(dict(id_credito=fila["id_credito"], saldo_mxn=fila["saldo_mxn"]))
    seleccion.sort(key=lambda f: f["id_credito"])
    return dict(seleccion=seleccion, control=dict(corte=corte.isoformat(), minimo_mxn=minimo,
        registros=len(seleccion), saldo_mxn=sum(f["saldo_mxn"] for f in seleccion)),
        fuente=dict(registros=len(filas), ids=len({f["id_credito"] for f in filas})))


def comprobar_seleccion(observada, ruta=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    """Adaptador de registros Python nativos; no sustituye inspeccionar el esquema del motor."""
    if type(observada) is not list:
        raise ValueError("Se requiere una lista de registros nativos")
    for f in observada:
        if (type(f) is not dict or set(f) != {"id_credito", "saldo_mxn"} or
                type(f["id_credito"]) is not str or not re.fullmatch(r"[0-9]{3}", f["id_credito"]) or
                type(f["saldo_mxn"]) is not int or not 0 <= f["saldo_mxn"] <= reglas.MAXIMO):
            raise ValueError("Salida distinta de ID textual/saldo entero sin ausencias")
    referencia = construir_referencia(ruta, corte, minimo)
    if sorted(observada, key=lambda f: f["id_credito"]) != referencia["seleccion"]:
        raise ValueError("Pares ID/importe distintos, aunque coincidan conteos y sumas")
    return referencia["control"]


def generar_escala(destino, creditos=20):
    """Dos cortes, IDs nuevos y formula fija; no repite claves ni usa azar."""
    if type(creditos) is not int or not 1 <= creditos <= 999:
        raise ValueError("creditos debe ser entero entre 1 y 999 (IDs de tres digitos)")
    destino = Path(destino)
    # El padre debe existir; nunca sobreescribir una muestra anterior.
    with destino.open("x", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=reglas.COLUMNAS)
        escritor.writeheader()
        for mes, corte in enumerate(["2026-09-30", "2026-10-31"]):
            for j in range(creditos):
                escritor.writerow(dict(id_credito=f"{j + 1:03d}", fecha_corte=corte,
                    saldo_mxn=(j * 137 + mes * 83) % 5001))
    return construir_referencia(destino)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    parser.add_argument("--generar", type=Path, help="CSV NUEVO; padre existente")
    parser.add_argument("--creditos", type=int, default=20)
    args = parser.parse_args()
    if args.generar is not None:
        generar_escala(args.generar, args.creditos)
    ruta = args.generar if args.generar is not None else args.fuente
    print(json.dumps(construir_referencia(ruta, args.corte, args.minimo), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

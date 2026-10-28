"""Lectura y análisis reutilizables, sin Streamlit ni trabajo al importar."""

import csv
from datetime import date
import re

COLUMNAS = ("id_credito", "segmento", "fecha_corte", "saldo_mxn")
SEGMENTOS = ("comercio", "servicios")
MAXIMO_MXN = 1_000_000


def validar_fecha(valor):
    """Contrato didáctico: ISO real, años 1900–2100, sin normalizar textos."""
    if not isinstance(valor, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", valor):
        raise ValueError("Fecha: se requiere YYYY-MM-DD.")
    fecha = date.fromisoformat(valor)
    if not 1900 <= fecha.year <= 2100:
        raise ValueError("Fecha fuera de 1900–2100.")


def validar_importe(valor):
    if type(valor) is not int or not 0 <= valor <= MAXIMO_MXN:
        raise ValueError("Importe: entero de 0 a 1000000 MXN; bool no es importe.")


def validar_cartera(filas):
    """Revisa TODA la entrada, incluso filas que un filtro no mostraría."""
    if not isinstance(filas, list):
        raise ValueError("La cartera debe ser una lista de registros.")
    claves = set()
    for numero, fila in enumerate(filas, start=1):
        if not isinstance(fila, dict) or set(fila) != set(COLUMNAS):
            raise ValueError(f"Registro {numero}: columnas incorrectas.")
        identificador = fila["id_credito"]
        if not isinstance(identificador, str) or not re.fullmatch(r"[0-9]{3}", identificador):
            raise ValueError(f"Registro {numero}: ID de tres dígitos.")
        validar_fecha(fila["fecha_corte"])
        if fila["segmento"] not in SEGMENTOS:
            raise ValueError(f"Registro {numero}: segmento desconocido.")
        validar_importe(fila["saldo_mxn"])
        clave = (identificador, fila["fecha_corte"])
        if clave in claves:
            raise ValueError(f"Registro {numero}: clave ID/corte repetida.")
        claves.add(clave)


def leer_cartera(ruta):
    """Lee UTF-8, convierte saldos tras revisar su forma y valida el conjunto."""
    filas = []
    with open(ruta, encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo, strict=True)
        if lector.fieldnames != list(COLUMNAS):
            raise ValueError("Encabezado: se requieren las cuatro columnas en su orden.")
        for fila in lector:
            if set(fila) != set(COLUMNAS) or any(v is None for v in fila.values()):
                raise ValueError(f"Línea {lector.line_num}: número de campos incorrecto.")
            if not re.fullmatch(r"0|[1-9][0-9]*", fila["saldo_mxn"]):
                raise ValueError(f"Línea {lector.line_num}: saldo entero sin signos ni decimales.")
            fila["saldo_mxn"] = int(fila["saldo_mxn"])
            filas.append(fila)
    validar_cartera(filas)
    return filas


def analizar(filas, corte, segmentos, minimo_mxn):
    """Calcula sin leer, imprimir ni modificar la entrada; devuelve datos simples."""
    validar_cartera(filas)
    validar_fecha(corte)
    validar_importe(minimo_mxn)
    if not isinstance(segmentos, (list, tuple)) or any(s not in SEGMENTOS for s in segmentos):
        raise ValueError("Segmentos: lista o tupla con etiquetas conocidas; [] selecciona ninguno.")
    if len(segmentos) != len(set(segmentos)):
        raise ValueError("Segmentos repetidos.")
    universo = [fila for fila in filas if fila["fecha_corte"] == corte]
    seleccion = [dict(fila) for fila in universo
                 if fila["segmento"] in segmentos and fila["saldo_mxn"] >= minimo_mxn]
    seleccion.sort(key=lambda fila: fila["id_credito"])
    cantidad = len(seleccion)
    return {
        "corte": corte,
        "segmentos": list(segmentos),
        "minimo_mxn": minimo_mxn,
        "universo": {"cantidad": len(universo), "saldo_mxn": sum(f["saldo_mxn"] for f in universo)},
        "seleccion": seleccion,
        "indicadores": {
            "cantidad": cantidad,
            "saldo_mxn": sum(f["saldo_mxn"] for f in seleccion),
            "porcentaje_creditos": cantidad / len(universo) * 100 if universo else None,
        },
    }

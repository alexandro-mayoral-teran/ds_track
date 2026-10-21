"""Contrato didactico de solo lectura: Python estandar, sin lector Parquet."""

import csv
from collections import Counter
from datetime import date
from pathlib import Path
import re

COLUMNAS = ["id_credito", "fecha_corte", "saldo_mxn"]
CARPETA = Path(__file__).resolve().parent
MAXIMO = 2147483647


def leer_textos(ruta, columnas):
    """Conserva vacios y el marcador literal de ausencia antes de interpretar."""
    with Path(ruta).open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != columnas:
            raise ValueError("Nombres u orden de columnas distintos")
        filas = list(lector)
    if any(None in fila or None in fila.values() for fila in filas):
        raise ValueError("Cantidad de campos distinta")
    return filas


def evaluar_contrato(filas):
    """Evalua entradas textuales; conserva originales y todos los motivos.

    La ausencia se representa por el texto reservado \\N solo en estos casos.
    No normaliza espacios, no redondea y no infiere unidades.
    """
    resultados = []
    for original in filas:
        if list(original) != COLUMNAS or any(type(v) is not str for v in original.values()):
            raise ValueError("Se requieren las tres columnas textuales en orden")
        motivos = []
        identificador, texto_fecha, texto_saldo = original.values()
        id_valido = bool(re.fullmatch(r"[0-9]{3}", identificador))
        if identificador == r"\N":
            motivos.append("id_ausente")
        elif not id_valido:
            motivos.append("id_forma")

        fecha = None
        if texto_fecha == r"\N":
            motivos.append("fecha_ausente")
        elif not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", texto_fecha):
            motivos.append("fecha_forma")
        else:
            try:
                fecha = date.fromisoformat(texto_fecha)
            except ValueError:
                motivos.append("fecha_calendario")
            else:
                if not 1900 <= fecha.year <= 2100:
                    motivos.append("fecha_rango")

        saldo = None
        if texto_saldo == r"\N":
            motivos.append("saldo_ausente")
        elif not re.fullmatch(r"-?[0-9]+", texto_saldo):
            motivos.append("saldo_forma")
        else:
            # Compara magnitud textual antes de convertir: sin perdida por float.
            negativo = texto_saldo.startswith("-")
            digitos = texto_saldo.lstrip("-").lstrip("0") or "0"
            if len(digitos) > 10 or (len(digitos) == 10 and digitos > str(MAXIMO)):
                motivos.append("saldo_rango")
            else:
                saldo = int(digitos) * (-1 if negativo else 1)
            if negativo and digitos != "0":
                motivos.append("saldo_negativo")

        # Una clave completa se revisa aunque el saldo de esa fila sea invalido.
        clave = (identificador, fecha) if id_valido and fecha is not None else None
        resultados.append(dict(original=original.copy(), fecha=fecha, saldo=saldo,
                               clave=clave, motivos=motivos))
    frecuencias = Counter(r["clave"] for r in resultados if r["clave"] is not None)
    for r in resultados:
        if r["clave"] is not None and frecuencias[r["clave"]] > 1:
            r["motivos"].append("clave_repetida")
        r["aceptado"] = not r["motivos"]
    return resultados


def comprobar_contrato(carpeta=CARPETA):
    carpeta = Path(carpeta)
    ruta_base = carpeta.parent / "01_csv_parquet_arrow" / "datos" / "base_comun.csv"
    base = evaluar_contrato(leer_textos(ruta_base, COLUMNAS))
    if not all(r["aceptado"] for r in base):
        raise ValueError("La base conocida incumple el contrato")
    conteos = Counter(r["fecha"].isoformat() for r in base)
    saldos = {c: sum(r["saldo"] for r in base if r["fecha"].isoformat() == c)
              for c in sorted(conteos)}
    if (len(base) != 28 or len({r["original"]["id_credito"] for r in base}) != 14
            or conteos != {"2026-09-30": 14, "2026-10-31": 14}
            or saldos != {"2026-09-30": 29000, "2026-10-31": 31800}):
        raise ValueError("La base conocida cambio")
    casos = leer_textos(carpeta / "casos_contrato.csv",
                        ["caso", *COLUMNAS, "motivos_esperados"])
    evaluados = evaluar_contrato([{k: f[k] for k in COLUMNAS} for f in casos])
    for caso, resultado in zip(casos, evaluados):
        if "|".join(resultado["motivos"]) != caso["motivos_esperados"]:
            raise ValueError("Motivos distintos para " + caso["caso"])
    return dict(base=base, saldos_mxn=saldos, casos=casos, evaluados=evaluados)


if __name__ == "__main__":
    resultado = comprobar_contrato()
    print("Base: 28 observaciones, 14 IDs; saldos MXN:", resultado["saldos_mxn"])
    for caso, fila in zip(resultado["casos"], resultado["evaluados"]):
        print(caso["caso"] + ": " + ("|".join(fila["motivos"]) or "aceptado"))
    print("Casos separados:", len(resultado["casos"]), "; aceptados:",
          sum(r["aceptado"] for r in resultado["evaluados"]))
    print("Solo lectura CSV; no decodifica Parquet ni instala paquetes.")

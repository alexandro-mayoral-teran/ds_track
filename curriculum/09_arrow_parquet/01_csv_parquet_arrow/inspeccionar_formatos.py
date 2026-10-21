"""Inspeccion de solo lectura. Esencial: biblioteca estandar; PyArrow opcional."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

COLUMNAS = ["id_credito", "fecha_corte", "saldo_mxn"]
CARPETA = Path(__file__).resolve().parent / "datos"


def leer_csv(ruta):
    with Path(ruta).open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != COLUMNAS:
            raise ValueError("Cabecera distinta de la muestra")
        observaciones = []
        for fila in lector:
            if None in fila or None in fila.values():
                raise ValueError("Registro con cantidad de campos distinta")
            if not re.fullmatch(r"[0-9]{3}", fila["id_credito"]):
                raise ValueError("Conserva el ID como texto de tres digitos")
            texto = fila["fecha_corte"]
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", texto):
                raise ValueError("Se requiere fecha ISO explicita")
            fecha = date.fromisoformat(texto)
            if not 1900 <= fecha.year <= 2100:
                raise ValueError("Fecha fuera del rango didactico")
            saldo = fila["saldo_mxn"]
            if not re.fullmatch(r"[0-9]+", saldo) or int(saldo) > 2147483647:
                raise ValueError("Saldo fuera del contrato de esta muestra")
            observaciones.append(dict(id_credito=fila["id_credito"],
                                       fecha_corte=fecha, saldo_mxn=int(saldo)))
    claves = [(f["id_credito"], f["fecha_corte"]) for f in observaciones]
    if len(set(claves)) != len(claves):
        raise ValueError("Clave ID/corte repetida")
    return observaciones


def inspeccionar(carpeta=CARPETA):
    carpeta = Path(carpeta)
    filas = leer_csv(carpeta / "base_comun.csv")
    conteos = Counter(f["fecha_corte"].isoformat() for f in filas)
    saldos = {corte: sum(f["saldo_mxn"] for f in filas if f["fecha_corte"].isoformat() == corte)
              for corte in sorted(conteos)}
    ids = {f["id_credito"] for f in filas}
    if len(ids) != 14 or conteos != {"2026-09-30": 14, "2026-10-31": 14} or saldos != {
            "2026-09-30": 29000, "2026-10-31": 31800}:
        raise ValueError("La muestra no reproduce los valores conocidos")
    with (carpeta / "inventario.csv").open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["archivo", "filas", "columnas", "bytes", "md5"]:
            raise ValueError("Inventario con cabecera distinta")
        inventario = list(lector)
    if [f["archivo"] for f in inventario] != ["base_comun.csv", "base_comun.parquet"]:
        raise ValueError("Inventario con archivos distintos")
    for entrada in inventario:
        contenido = (carpeta / entrada["archivo"]).read_bytes()
        if (len(contenido) != int(entrada["bytes"]) or
                hashlib.md5(contenido).hexdigest() != entrada["md5"] or
                entrada["filas"] != "28" or entrada["columnas"] != "3"):
            raise ValueError("Archivo distinto del inventario de referencia")
    with (carpeta / "base_comun.parquet").open("rb") as archivo:
        inicio = archivo.read(4)
        archivo.seek(-4, 2)
        final = archivo.read(4)
    if inicio != b"PAR1" or final != b"PAR1":
        raise ValueError("Firma distinta de la muestra Parquet sin cifrar")
    # Esto NO decodifica Parquet: contrasta inventario, firma y analisis del CSV.
    return dict(registros=len(filas), ids=len(ids), saldos_mxn=saldos,
                archivos=inventario, alcance="CSV interpretado; Parquet sin decodificar")


def verificar_parquet(carpeta=CARPETA):
    """Ampliacion de autoría; requiere PyArrow ya disponible en el entorno elegido."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    carpeta = Path(carpeta)
    inspeccionar(carpeta)
    esperado = leer_csv(carpeta / "base_comun.csv")
    archivo = pq.ParquetFile(carpeta / "base_comun.parquet")
    tabla = archivo.read()
    esquema = pa.schema([
        pa.field("id_credito", pa.string(), nullable=False),
        pa.field("fecha_corte", pa.date32(), nullable=False),
        pa.field("saldo_mxn", pa.int32(), nullable=False),
    ])
    clave = lambda f: (f["fecha_corte"], f["id_credito"])
    if not tabla.schema.equals(esquema) or sorted(tabla.to_pylist(), key=clave) != sorted(esperado, key=clave):
        raise ValueError("Parquet no conserva el esquema o los valores por clave")
    return dict(pyarrow=pa.__version__, filas=archivo.metadata.num_rows,
                columnas=archivo.metadata.num_columns, grupos_filas=archivo.metadata.num_row_groups,
                esquema=str(tabla.schema), buffers_logicos_bytes=tabla.nbytes,
                alcance="Parquet decodificado y conciliado con el CSV; no mide RAM del proceso")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--carpeta", type=Path, default=CARPETA)
    parser.add_argument("--verificar-parquet", action="store_true")
    args = parser.parse_args()
    funcion = verificar_parquet if args.verificar_parquet else inspeccionar
    print(json.dumps(funcion(args.carpeta), ensure_ascii=False, indent=2))

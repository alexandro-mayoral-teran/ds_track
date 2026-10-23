"""Particiones Hive con etiqueta auxiliar: consultas y auditoria separadas.

Importar no escribe. Los archivos conservan las tres columnas del contrato.
"""

import argparse
import csv
from datetime import date
import importlib.util
import json
from pathlib import Path
import re

import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "dataset_0908", CARPETA.parent / "06_selective_datasets/consultas_dataset.py")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
cartera = base.cartera
FUENTE = cartera.FUENTE


def campo_particion(por):
    if por not in ("corte", "clave"):
        raise ValueError("por debe ser corte o clave")
    return por


def etiquetas(tabla, por):
    campo_particion(por)
    filas = cartera.validar_tabla(tabla)
    return [(f["id_credito"] + "_" if por == "clave" else "") +
            f["fecha_corte"].isoformat() for f in filas]


def archivos_particionados(carpeta, por="corte"):
    """Inspecciona arbol y todos los esquemas reales, sin decodificar valores."""
    campo_particion(por)
    carpeta = Path(carpeta)
    if not carpeta.is_dir() or carpeta.is_symlink():
        raise ValueError("Indica la carpeta datos del dataset")
    entradas = sorted(carpeta.iterdir())
    archivos = []
    if (len(entradas) == 1 and entradas[0].name == "vacio.parquet" and
            entradas[0].is_file() and not entradas[0].is_symlink()):
        archivos = entradas
    else:
        for p in entradas:
            patron = r"clave=\d{3}_\d{4}-\d{2}-\d{2}" if por == "clave" else r"corte=\d{4}-\d{2}-\d{2}"
            if not p.is_dir() or p.is_symlink() or not re.fullmatch(patron, p.name):
                raise ValueError("Arbol inesperado: una carpeta Hive por etiqueta")
            valor = p.name.split("=", 1)[1]
            if por == "clave" and not re.fullmatch(r"\d{3}_\d{4}-\d{2}-\d{2}", valor):
                raise ValueError("Clave de particion invalida")
            fecha = date.fromisoformat(valor[-10:])
            if not date(1900, 1, 1) <= fecha <= date(2100, 12, 31):
                raise ValueError("Fecha de carpeta fuera del contrato")
            partes = sorted(p.iterdir())
            if not partes or any(not f.is_file() or f.is_symlink() or f.suffix != ".parquet" for f in partes):
                raise ValueError("Cada particion debe contener solo archivos Parquet")
            archivos.extend(partes)
    if not archivos:
        raise ValueError("Dataset sin archivos: falta un esquema comprobable")
    for ruta in archivos:
        with pq.ParquetFile(ruta) as lector:
            if not lector.schema_arrow.equals(cartera.ESQUEMA, check_metadata=False):
                raise ValueError(f"Esquema fisico distinto en {ruta.name}")
            if ruta.name == "vacio.parquet" and ruta.parent == carpeta and lector.metadata.num_rows:
                raise ValueError("El archivo vacio contiene registros")
    return archivos


def abrir_particionado(carpeta, por="corte"):
    archivos_particionados(carpeta, por)
    particion = ds.partitioning(pa.schema([(por, pa.string())]), flavor="hive")
    return ds.dataset(carpeta, format="parquet", partitioning=particion)


def inventario(carpeta, por="corte"):
    carpeta = Path(carpeta)
    filas = []
    for ruta in archivos_particionados(carpeta, por):
        with pq.ParquetFile(ruta) as lector:
            filas.append(dict(archivo=ruta.relative_to(carpeta).as_posix(),
                registros=lector.metadata.num_rows, grupos=lector.metadata.num_row_groups,
                bytes_archivo=ruta.stat().st_size))
    return filas


def auditar_particionado(carpeta, ruta_csv=FUENTE, por="corte"):
    """Auditoria completa en memoria: ruta contra cada fila, luego CSV por clave."""
    carpeta = Path(carpeta)
    for ruta in archivos_particionados(carpeta, por):
        with pq.ParquetFile(ruta) as lector:
            tabla = lector.read()
        valores = etiquetas(tabla, por)
        if valores and any(v != ruta.parent.name.split("=", 1)[1] for v in valores):
            raise ValueError("Etiqueta de carpeta distinta de los valores fisicos")
    observada = abrir_particionado(carpeta, por).to_table(columns=cartera.COLUMNAS)
    esperada = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    cartera.comparar_tablas(esperada, observada)
    return cartera.resumir(observada)


def escribir_particionado(tabla, destino, por="corte"):
    valores = etiquetas(tabla, por)
    if not pa.Codec.is_available("snappy"):
        raise ValueError("Snappy no disponible")
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    datos = destino / "datos"
    datos.mkdir()
    if tabla.num_rows:
        ampliada = tabla.append_column(pa.field(por, pa.string(), nullable=False), pa.array(valores))
        formato = ds.ParquetFileFormat()
        ds.write_dataset(ampliada, datos, format=formato,
            file_options=formato.make_write_options(compression="snappy", version="2.6"),
            partitioning=ds.partitioning(pa.schema([(por, pa.string())]), flavor="hive"),
            basename_template="parte-{i}.parquet", existing_data_behavior="error",
            use_threads=False)
    else:
        # Sin valores no hay carpetas que descubrir: conservar un Parquet vacio.
        with (datos / "vacio.parquet").open("xb") as archivo:
            pq.write_table(tabla, archivo, compression="snappy", version="2.6")
    cartera.comparar_tablas(tabla, abrir_particionado(datos, por).to_table(columns=cartera.COLUMNAS))
    filas = inventario(datos, por)
    with (destino / "inventario.csv").open("x", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]))
        escritor.writeheader()
        escritor.writerows(filas)
    return filas


def preparar_consulta(dataset, corte=date(2026, 10, 31), minimo=2000):
    base.parametros_consulta(corte, minimo)
    # La etiqueta permite descartar particiones; la fecha fisica tambien se exige.
    filtro = ((ds.field("corte") == corte.isoformat()) &
              (ds.field("fecha_corte") == pa.scalar(corte)) & (ds.field("saldo_mxn") >= minimo))
    return dataset.scanner(columns=base.PROYECCION, filter=filtro)


def candidatos(dataset, corte=date(2026, 10, 31)):
    base.parametros_consulta(corte, 0)
    # Solo expresion de particion: no mide lecturas fisicas ni descarta por saldo.
    return sorted(f.path for f in dataset.get_fragments(filter=ds.field("corte") == corte.isoformat()))


def crear_comparacion(destino, ruta_csv=FUENTE):
    tabla = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    base.escribir_partes(tabla, destino / "plano", filas_por_archivo=14)
    escribir_particionado(tabla, destino / "por_corte")
    return verificar_comparacion(destino, ruta_csv)


def verificar_comparacion(destino, ruta_csv=FUENTE):
    destino = Path(destino)
    a = base.verificar_dataset(destino / "plano/datos", ruta_csv)
    b = auditar_particionado(destino / "por_corte/datos", ruta_csv)
    if a != b:
        raise ValueError("Resumenes distintos")
    return b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    accion = parser.add_mutually_exclusive_group(required=True)
    accion.add_argument("--crear", type=Path)
    accion.add_argument("--verificar", type=Path)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    args = parser.parse_args()
    print(json.dumps((crear_comparacion(args.crear, args.fuente) if args.crear is not None else
                      verificar_comparacion(args.verificar, args.fuente)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

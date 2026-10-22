"""Partes Parquet, auditoria completa y consultas selectivas separadas.

Importar no lee datos ni crea salidas. Sin dependencias nuevas respecto a 09.03.
"""

import argparse
import csv
from datetime import date
import importlib.util
import json
from pathlib import Path

import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "cartera_0903", CARPETA.parent / "03_python_read_write/intercambio_python.py")
cartera = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cartera)
FUENTE = cartera.FUENTE
PROYECCION = ["id_credito", "saldo_mxn"]


def archivos_dataset(carpeta):
    """Carpeta plana: ninguna entrada se omite silenciosamente."""
    carpeta = Path(carpeta)
    if not carpeta.is_dir():
        raise ValueError("Se requiere la carpeta datos del dataset")
    archivos = sorted(carpeta.iterdir())
    if not archivos or any(not p.is_file() or p.suffix.lower() != ".parquet" for p in archivos):
        raise ValueError("Se exige al menos un Parquet y ninguna otra entrada en datos")
    if len({p.resolve() for p in archivos}) != len(archivos):
        raise ValueError("Una misma ruta de archivo aparece repetida")
    return archivos


def abrir_dataset(carpeta):
    """Comprueba esquemas de TODOS los archivos; no valida sus filas."""
    archivos = archivos_dataset(carpeta)
    for ruta in archivos:
        with pq.ParquetFile(ruta) as lector:
            if not lector.schema_arrow.equals(cartera.ESQUEMA, check_metadata=False):
                raise ValueError(f"Esquema distinto en {ruta.name}")
    dataset = ds.dataset([str(p) for p in archivos], format="parquet", partitioning=None)
    if not dataset.schema.equals(cartera.ESQUEMA, check_metadata=False):
        raise ValueError("Esquema del dataset distinto")
    return dataset


def verificar_dataset(carpeta, ruta_csv=FUENTE):
    """Auditoria completa, deliberadamente en memoria para esta muestra pequena."""
    esperada = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    observada = abrir_dataset(carpeta).to_table()
    cartera.comparar_tablas(esperada, observada)
    return cartera.resumir(observada)


def escribir_partes(tabla, destino, filas_por_archivo=14):
    """Escribe partes nuevas sin carpetas de particion; el vacio conserva esquema."""
    cartera.validar_tabla(tabla)
    if type(filas_por_archivo) is not int or filas_por_archivo <= 0:
        raise ValueError("filas_por_archivo debe ser entero positivo")
    if not pa.Codec.is_available("snappy"):
        raise ValueError("Esta instalacion no incluye Snappy")
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    datos = destino / "datos"
    datos.mkdir()
    inventario = []
    for i, inicio in enumerate(range(0, tabla.num_rows, filas_por_archivo) or [0], 1):
        parte = tabla.slice(inicio, filas_por_archivo)
        nombre = f"parte_{i:03d}.parquet"
        with (datos / nombre).open("xb") as archivo:
            pq.write_table(parte, archivo, version="2.6", compression="snappy")
        inventario.append(dict(archivo=nombre, registros=parte.num_rows))
    # La relectura no depende del inventario; las notas no acreditan integridad.
    cartera.comparar_tablas(tabla, abrir_dataset(datos).to_table())
    with (destino / "inventario.csv").open("x", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["archivo", "registros"])
        escritor.writeheader()
        escritor.writerows(inventario)
    return inventario


def crear_dataset(destino, ruta_csv=FUENTE):
    tabla = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    escribir_partes(tabla, destino)
    return verificar_dataset(Path(destino) / "datos", ruta_csv)


def parametros_consulta(corte, minimo):
    if type(corte) is not date or not date(1900, 1, 1) <= corte <= date(2100, 12, 31):
        raise ValueError("corte debe ser date entre 1900 y 2100, sin hora")
    if type(minimo) is not int or not 0 <= minimo <= 2147483647:
        raise ValueError("minimo debe ser entero no negativo dentro de int32")


def preparar_consulta(dataset, corte=date(2026, 10, 31), minimo=2000):
    """Devuelve Scanner: aun no materializa el resultado completo."""
    parametros_consulta(corte, minimo)
    if not isinstance(dataset, ds.Dataset) or not dataset.schema.equals(
            cartera.ESQUEMA, check_metadata=False):
        raise ValueError("Se requiere Dataset con el esquema de cartera")
    filtro = ((ds.field("fecha_corte") == pa.scalar(corte, type=pa.date32())) &
              (ds.field("saldo_mxn") >= minimo))
    return dataset.scanner(columns=PROYECCION, filter=filtro)


def referencia_consulta(corte, minimo, ruta_csv=FUENTE):
    """CSV validado y recorrido Python, sin ejecutar filtros Arrow o pandas."""
    parametros_consulta(corte, minimo)
    filas = cartera._exigir_reglas(cartera._contrato.leer_textos(ruta_csv, cartera.COLUMNAS))
    return sorted([dict(id_credito=f["original"]["id_credito"], saldo_mxn=f["saldo"])
                   for f in filas if f["fecha"] == corte and f["saldo"] >= minimo],
                  key=lambda f: f["id_credito"])


def comprobar_consulta(resultado, corte=date(2026, 10, 31), minimo=2000, ruta_csv=FUENTE):
    """Comprueba SOLO la seleccion; no certifica filas/columnas excluidas."""
    esquema = pa.schema([cartera.ESQUEMA.field(n) for n in PROYECCION])
    if not isinstance(resultado, pa.Table) or not resultado.schema.equals(esquema, check_metadata=False):
        raise ValueError("Esquema proyectado distinto")
    resultado.validate(full=True)
    if any(c.null_count for c in resultado.columns):
        raise ValueError("Ausencias en la seleccion")
    if sorted(resultado.to_pylist(), key=lambda f: f["id_credito"]) != referencia_consulta(
            corte, minimo, ruta_csv):
        raise ValueError("Seleccion distinta del CSV, aunque coincidan sus sumas")
    return dict(registros=resultado.num_rows,
                saldo_mxn=sum(f["saldo_mxn"] for f in resultado.to_pylist()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    acciones = parser.add_mutually_exclusive_group(required=True)
    acciones.add_argument("--crear", type=Path, help="Carpeta NUEVA para partes e inventario")
    acciones.add_argument("--verificar", type=Path, help="Carpeta datos: auditoria completa de lectura")
    acciones.add_argument("--consultar", type=Path, help="Carpeta datos: seleccion de lectura")
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    if args.crear is not None:
        resultado = crear_dataset(args.crear, args.fuente)
    elif args.verificar is not None:
        resultado = verificar_dataset(args.verificar, args.fuente)
    else:
        seleccion = preparar_consulta(abrir_dataset(args.consultar), args.corte, args.minimo).to_table()
        resultado = comprobar_consulta(seleccion, args.corte, args.minimo, args.fuente)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

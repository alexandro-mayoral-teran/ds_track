"""Entrega reconstruible y verificador de solo lectura, interoperables con R.

Importar no crea salidas. La referencia se reconstruye del CSV externo a la entrega.
"""

import argparse
import csv
from datetime import date
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import shutil

import pyarrow as pa
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "dataset_cierre_0909", CARPETA.parent / "06_selective_datasets/consultas_dataset.py")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
cartera = base.cartera
FUENTE = cartera.FUENTE
CORTE = date(2026, 10, 31)
MINIMO = 2000
CONTRATO = [
    dict(regla="columnas", valor="id_credito|fecha_corte|saldo_mxn"),
    dict(regla="tipos_arrow", valor="string|date32|int32"),
    dict(regla="nulabilidad", valor="false|false|false"),
    dict(regla="clave", valor="id_credito|fecha_corte"),
    dict(regla="id", valor="tres digitos textuales"),
    dict(regla="fechas", valor="1900-01-01 a 2100-12-31; calendario valido"),
    dict(regla="saldo", valor="MXN; entero entre 0 y 2147483647"),
    dict(regla="duplicados", valor="rechazar; no deduplicar"),
]
NOTAS_FIJAS = dict(version_parquet="2.6", compresion="snappy",
                   fecha_consulta=CORTE.isoformat(), minimo_mxn=str(MINIMO))


def escribir_csv(ruta, columnas, filas):
    with Path(ruta).open("x", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(filas)


def leer_csv(ruta, columnas):
    with Path(ruta).open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != columnas:
            raise ValueError(f"Columnas CSV distintas en {Path(ruta).name}")
        filas = list(lector)
    if any(set(f) != set(columnas) or any(v is None for v in f.values()) for f in filas):
        raise ValueError("CSV con campos faltantes o adicionales")
    return filas


def comparar_csv(ruta, columnas, esperadas):
    observadas = leer_csv(ruta, columnas)
    textos = [{k: str(f[k]) for k in columnas} for f in esperadas]
    clave = lambda f: tuple(f[k] for k in columnas)
    if sorted(observadas, key=clave) != sorted(textos, key=clave):
        raise ValueError(f"Valores CSV distintos en {Path(ruta).name}")


def huellas(destino):
    """MD5 solo para cambios accidentales; no es prueba de autenticidad."""
    destino = Path(destino)
    return [dict(archivo=p.relative_to(destino).as_posix(), bytes=p.stat().st_size,
                 md5=hashlib.md5(p.read_bytes(), usedforsecurity=False).hexdigest())
            for p in sorted(destino.rglob("*")) if p.is_file() and p != destino / "huellas.csv"]


def resumen_csv(tabla):
    return cartera.resumir(tabla)["cortes"]


def verificar_entrega(destino, ruta_csv=FUENTE):
    """Reconstruye referencia, revisa arbol/notas/huellas y decodifica todos los datos."""
    destino = Path(destino)
    esperada = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    nombres = {"entrada.csv", "tabla.parquet", "dataset", "resumen.csv", "seleccion.csv",
               "contrato.csv", "sesion.csv", "huellas.csv"}
    if not destino.is_dir() or {p.name for p in destino.iterdir()} != nombres:
        raise ValueError("Entrega incompleta o con entradas adicionales")
    if {p.name for p in (destino / "dataset").iterdir()} != {"datos", "inventario.csv"}:
        raise ValueError("Estructura de dataset distinta")
    # No se utilizan rutas procedentes del manifiesto para abrir otros archivos.
    comparar_csv(destino / "huellas.csv", ["archivo", "bytes", "md5"], huellas(destino))
    if (destino / "entrada.csv").read_bytes() != Path(ruta_csv).read_bytes():
        raise ValueError("La copia de entrada no coincide con la fuente externa")
    comparar_csv(destino / "contrato.csv", ["regla", "valor"], CONTRATO)
    notas = leer_csv(destino / "sesion.csv", ["campo", "valor"])
    sesion = {f["campo"]: f["valor"] for f in notas}
    if (len(sesion) != len(notas) or set(sesion) != set(NOTAS_FIJAS) |
            {"escritor", "version_lenguaje", "version_arrow"} or
            sesion["escritor"] not in ("Python", "R") or
            not sesion["version_lenguaje"] or not sesion["version_arrow"] or
            any(sesion[k] != v for k, v in NOTAS_FIJAS.items())):
        raise ValueError("Notas de sesion inconsistentes")
    # Esquema real antes de comparar, sin imponerlo al lector.
    with pq.ParquetFile(destino / "tabla.parquet") as lector:
        cartera.comparar_tablas(esperada, lector.read())
    base.verificar_dataset(destino / "dataset/datos", ruta_csv)
    partes = base.archivos_dataset(destino / "dataset/datos")
    cantidad = max(1, (esperada.num_rows + 13) // 14)
    if [p.name for p in partes] != [f"parte_{i:03d}.parquet" for i in range(1, cantidad + 1)]:
        raise ValueError("Partes distintas del plan de escritura")
    inventario = []
    for p in partes:
        with pq.ParquetFile(p) as lector:
            inventario.append(dict(archivo=p.name, registros=lector.metadata.num_rows))
    if any(f["registros"] > 14 for f in inventario):
        raise ValueError("Una parte supera las 14 filas del plan")
    comparar_csv(destino / "dataset/inventario.csv", ["archivo", "registros"], inventario)
    comparar_csv(destino / "resumen.csv", ["fecha_corte", "registros", "saldo_mxn"],
                  resumen_csv(esperada))
    seleccion = base.preparar_consulta(base.abrir_dataset(destino / "dataset/datos"), CORTE, MINIMO).to_table()
    control = base.comprobar_consulta(seleccion, CORTE, MINIMO, ruta_csv)
    comparar_csv(destino / "seleccion.csv", base.PROYECCION,
                  base.referencia_consulta(CORTE, MINIMO, ruta_csv))
    return dict(cartera=cartera.resumir(esperada), seleccion=control)


def crear_entrega(destino, ruta_csv=FUENTE):
    tabla = cartera.crear_tabla(cartera.cargar_dataframe(ruta_csv))
    if not pa.Codec.is_available("snappy"):
        raise ValueError("Snappy no disponible")
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(ruta_csv, destino / "entrada.csv")
    with (destino / "tabla.parquet").open("xb") as archivo:
        pq.write_table(tabla, archivo, version="2.6", compression="snappy")
    base.escribir_partes(tabla, destino / "dataset", filas_por_archivo=14)
    escribir_csv(destino / "resumen.csv", ["fecha_corte", "registros", "saldo_mxn"], resumen_csv(tabla))
    seleccion = base.preparar_consulta(base.abrir_dataset(destino / "dataset/datos"), CORTE, MINIMO).to_table()
    base.comprobar_consulta(seleccion, CORTE, MINIMO, ruta_csv)
    escribir_csv(destino / "seleccion.csv", base.PROYECCION, seleccion.sort_by("id_credito").to_pylist())
    escribir_csv(destino / "contrato.csv", ["regla", "valor"], CONTRATO)
    sesion = dict(escritor="Python", version_lenguaje=platform.python_version(),
                  version_arrow=pa.__version__, **NOTAS_FIJAS)
    escribir_csv(destino / "sesion.csv", ["campo", "valor"],
                  [dict(campo=k, valor=v) for k, v in sesion.items()])
    escribir_csv(destino / "huellas.csv", ["archivo", "bytes", "md5"], huellas(destino))
    return verificar_entrega(destino, ruta_csv)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    accion = parser.add_mutually_exclusive_group(required=True)
    accion.add_argument("--crear", type=Path)
    accion.add_argument("--verificar", type=Path)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    args = parser.parse_args()
    resultado = (crear_entrega(args.crear, args.fuente) if args.crear is not None else
                 verificar_entrega(args.verificar, args.fuente))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

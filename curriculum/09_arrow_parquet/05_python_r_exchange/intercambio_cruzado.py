"""Escribir desde Python y verificar una carpeta escrita desde R, sin instalar.

Las reglas de cartera se reutilizan de 09.03/09.02. Importar no crea entregas.
"""

import argparse
from datetime import date
import importlib.util
import json
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "escritor_0903", CARPETA.parent / "03_python_read_write/intercambio_python.py")
cartera = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cartera)
FUENTE = cartera.FUENTE


def esquema_muestra():
    """Contrato independiente: texto e importe admiten ausencias, ID/fecha no."""
    return pa.schema([
        pa.field("id_prueba", pa.string(), nullable=False),
        pa.field("fecha", pa.date32(), nullable=False),
        pa.field("etiqueta", pa.string(), nullable=True),
        pa.field("importe", pa.int32(), nullable=True),
    ])


def construir_muestra():
    """Tres observaciones completas en el codigo; no son registros de cartera."""
    return pa.Table.from_pylist([
        dict(id_prueba="A", fecha=date(2024, 2, 29), etiqueta="Crédito ágil", importe=0),
        dict(id_prueba="B", fecha=date(2026, 9, 30), etiqueta="", importe=None),
        dict(id_prueba="C", fecha=date(2026, 10, 31), etiqueta=None, importe=10),
    ], schema=esquema_muestra())


def comparar_muestra(observada):
    """Esquema y cada valor por ID; acepta reordenacion, rechaza cambios/duplicados."""
    if not isinstance(observada, pa.Table) or not observada.schema.equals(
            esquema_muestra(), check_metadata=False):
        raise ValueError("Esquema distinto en la muestra de intercambio")
    observada.validate(full=True)
    filas = observada.to_pylist()
    if any(f["id_prueba"] is None or f["fecha"] is None for f in filas):
        raise ValueError("ID/fecha ausentes en la muestra")
    if sorted(filas, key=lambda f: f["id_prueba"]) != construir_muestra().to_pylist():
        raise ValueError("Claves o valores distintos en la muestra de intercambio")
    return dict(registros=3, importes_conocidos=2, suma_observada=10)


def leer_desde_r(carpeta, ruta_csv=FUENTE):
    """Verifica ambos Parquet contra referencias reconstruidas; solo lectura."""
    carpeta = Path(carpeta)
    resumen = cartera.verificar_parquet(carpeta / "base_comun.parquet", ruta_csv)
    ruta = carpeta / "muestra.parquet"
    if not ruta.is_file():
        raise ValueError("Falta el archivo muestra.parquet")
    muestra = comparar_muestra(pq.ParquetFile(ruta).read())
    return dict(cartera=resumen, muestra=muestra)


def escribir_desde_python(destino, ruta_csv=FUENTE):
    """Crea otra entrega: base con escritor 09.03 y muestra independiente.

    Una falla deja carpeta parcial. La relectura propia no acredita lectura R.
    """
    destino = Path(destino)
    cartera.crear_entrega(destino, ruta_csv)
    with (destino / "muestra.parquet").open("xb") as archivo:
        pq.write_table(construir_muestra(), archivo, version="2.6", compression="snappy")
    # Misma comprobacion, aqui sobre el archivo propio; despues debe leer R.
    return leer_desde_r(destino, ruta_csv)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    acciones = parser.add_mutually_exclusive_group(required=True)
    acciones.add_argument("--escribir", type=Path, help="Carpeta NUEVA para los dos Parquet")
    acciones.add_argument("--leer", type=Path, help="Carpeta escrita por R; solo lectura")
    parser.add_argument("--fuente", type=Path, default=FUENTE, help="CSV de referencia")
    args = parser.parse_args()
    resultado = (escribir_desde_python(args.escribir, args.fuente) if args.escribir is not None
                 else leer_desde_r(args.leer, args.fuente))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

"""Extension opcional: lotes, sink y comprobacion separada de la consulta.

Importar no lee datos ni escribe. La auditoria completa usa memoria y no forma
parte de una demostracion de RAM acotada. Cada destino debe ser nuevo.
"""

import argparse
from datetime import date
import importlib.util
import json
from pathlib import Path

import polars as pl

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location(
    "base_1005", CARPETA.parent / "03_polars_lazy_plans/consultas_lazy.py"
)
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
referencia = base.base.referencia


def preparar(destino, fuente=FUENTE):
    return base.preparar(destino, fuente)


def consultar(ruta, corte=date(2026, 10, 31), minimo=2000):
    """Plan sin ordenar globalmente; no audita valores de la fuente."""
    referencia.validar_parametros(corte, minimo)
    return base.abrir(ruta).filter(
        (pl.col("fecha_corte") == corte) & (pl.col("saldo_mxn") >= minimo)
    ).select("id_credito", "saldo_mxn")


def recorrer_lotes(consulta, filas_lote=2):
    """Consume TODOS los lotes; no guarda una lista de DataFrames."""
    if type(filas_lote) is not int or filas_lote < 1:
        raise ValueError("filas_lote debe ser entero positivo")
    control = dict(lotes=0, registros=0, saldo_mxn=0, max_filas_lote=0)
    for lote in consulta.collect_batches(
        chunk_size=filas_lote, maintain_order=True, lazy=True, engine="streaming"
    ):
        base.base.exigir_esquema(lote, base.base.SELECCION)
        control["lotes"] += 1
        control["registros"] += lote.height
        control["saldo_mxn"] += int(lote["saldo_mxn"].cast(pl.Int64).sum())
        control["max_filas_lote"] = max(control["max_filas_lote"], lote.height)
    return control


def escribir(consulta, destino):
    """Sink inmediato sobre un archivo exclusivo; no crea un DataFrame final."""
    with Path(destino).open("xb") as archivo:
        consulta.sink_parquet(archivo, compression="zstd", engine="streaming")


def verificar(salida, entrada, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    """Solo lectura: auditoria completa de entrada y cada par de salida."""
    referencia.validar_parametros(corte, minimo)
    base.auditar(entrada, fuente)
    consulta = pl.scan_parquet(salida, glob=False, hive_partitioning=False)
    if list(consulta.collect_schema().items()) != list(base.base.SELECCION.items()):
        raise ValueError("Salida debe tener ID String y saldo Int32, en ese orden")
    tabla = consulta.collect()
    return base.base.comprobar_seleccion(tabla, fuente, corte, minimo)


def ejecutar(entrada, destino, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000,
             filas_lote=2):
    referencia.validar_parametros(corte, minimo)
    if type(filas_lote) is not int or filas_lote < 1:
        raise ValueError("filas_lote debe ser entero positivo")
    base.auditar(entrada, fuente)
    consulta = consultar(entrada, corte, minimo)
    logico = consulta.explain(engine="streaming")
    fisico = consulta.show_graph(engine="streaming", plan_stage="physical",
                                raw_output=True, show=False)
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    (destino / "plan_logico.txt").write_text(logico, encoding="utf-8")
    (destino / "plan_fisico.dot").write_text(fisico, encoding="utf-8")
    lotes = recorrer_lotes(consulta, filas_lote)
    salida = destino / "seleccion.parquet"
    escribir(consulta, salida)
    control = verificar(salida, entrada, fuente, corte, minimo)
    if (lotes["registros"], lotes["saldo_mxn"]) != (control["registros"], control["saldo_mxn"]):
        raise ValueError("Control de lotes distinto de la salida conciliada")
    return dict(salida=salida, lotes=lotes, control=control)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    comandos = parser.add_subparsers(dest="comando", required=True)
    nuevo = comandos.add_parser("preparar", help="CSV incluido a Parquet en carpeta NUEVA")
    nuevo.add_argument("destino", type=Path)
    nuevo.add_argument("--fuente", type=Path, default=FUENTE)
    ejecutar_cmd = comandos.add_parser("ejecutar", help="Lotes y sink en carpeta NUEVA")
    ejecutar_cmd.add_argument("entrada", type=Path)
    ejecutar_cmd.add_argument("destino", type=Path)
    ejecutar_cmd.add_argument("--filas-lote", type=int, default=2)
    verificar_cmd = comandos.add_parser("verificar", help="Solo lectura")
    verificar_cmd.add_argument("salida", type=Path)
    verificar_cmd.add_argument("entrada", type=Path)
    for comando in (ejecutar_cmd, verificar_cmd):
        comando.add_argument("--fuente", type=Path, default=FUENTE)
        comando.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
        comando.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    if args.comando == "preparar":
        print(preparar(args.destino, args.fuente))
    elif args.comando == "ejecutar":
        print(json.dumps(ejecutar(args.entrada, args.destino, args.fuente, args.corte,
                                 args.minimo, args.filas_lote), default=str, indent=2))
    else:
        print(json.dumps(verificar(args.salida, args.entrada, args.fuente, args.corte,
                                  args.minimo), indent=2))


if __name__ == "__main__":
    main()

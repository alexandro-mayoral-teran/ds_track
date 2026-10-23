"""Preparacion nueva, consultas diferidas y auditoria completa separada.

Importar no lee fuentes ni escribe archivos. La consulta nativa no valida el
contrato completo: ejecutar_verificado lo comprueba contra el CSV externo.
"""

import argparse
from datetime import date
import importlib.util
from pathlib import Path
import sys

import polars as pl

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location(
    "tablas_1003", CARPETA.parent / "02_polars_tables_expressions/tablas_polars.py"
)
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
ESQUEMA = base.ESQUEMA


def preparar(destino, fuente=FUENTE):
    """Crea una carpeta exclusiva; no sobrescribe fuentes o entregas previas."""
    tabla = base.cargar_tabla(fuente)
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    ruta = destino / "muestra.parquet"
    tabla.write_parquet(ruta)
    auditar(ruta, fuente)
    return ruta


def abrir(ruta):
    """Resuelve esquema; no certifica valores, unicidad ni cobertura."""
    consulta = pl.scan_parquet(Path(ruta), glob=False, hive_partitioning=False)
    if list(consulta.collect_schema().items()) != list(ESQUEMA.items()):
        raise ValueError("Esquema Parquet distinto de String/Date/Int32")
    return consulta


def auditar(ruta, fuente=FUENTE):
    """Materializa TODA la entrada; control didactico sin memoria acotada."""
    esperadas = base.referencia.cargar_filas(fuente)
    tabla = abrir(ruta).collect()
    base.validar_tabla(tabla)
    clave = lambda f: (f["id_credito"], f["fecha_corte"])
    if sorted(tabla.to_dicts(), key=clave) != sorted(esperadas, key=clave):
        raise ValueError("Parquet distinto de la fuente CSV por clave/valor")
    return tabla.height


def seleccionar(entrada, corte=date(2026, 10, 31), minimo=2000):
    """Devuelve un plan; los parametros se validan antes de construirlo."""
    base.referencia.validar_parametros(corte, minimo)
    return (
        entrada.filter((pl.col("fecha_corte") == corte) & (pl.col("saldo_mxn") >= minimo))
        .select("id_credito", "saldo_mxn")
        .sort("id_credito")
    )


def resumir(entrada):
    """Dos columnas bastan en el scan; ampliar antes de sumar."""
    return entrada.group_by("fecha_corte").agg(
        pl.len().alias("registros"),
        pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn"),
    ).sort("fecha_corte")


def ejecutar_verificado(ruta, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    """Solo lectura; referencia independiente, valores y tipos tras collect."""
    base.referencia.validar_parametros(corte, minimo)
    registros = auditar(ruta, fuente)
    entrada = abrir(ruta)
    consulta = seleccionar(entrada, corte, minimo)
    resumen = resumir(entrada)
    planes = dict(sin_optimizar=consulta.explain(optimized=False),
                  optimizado=consulta.explain(), resumen=resumen.explain())
    resultado = consulta.collect()
    por_corte = resumen.collect()
    control = base.comprobar_seleccion(resultado, fuente, corte, minimo)
    base.comprobar_resumen(por_corte, fuente)
    return dict(registros_fuente=registros, planes=planes, seleccion=resultado,
                resumen=por_corte, control=control)


def main():
    # Algunos planes incluyen simbolos griegos; no fallar en consolas cp1252.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    comandos = parser.add_subparsers(dest="comando", required=True)
    preparar_cmd = comandos.add_parser("preparar", help="Carpeta NUEVA con Parquet")
    preparar_cmd.add_argument("destino", type=Path)
    preparar_cmd.add_argument("--fuente", type=Path, default=FUENTE)
    verificar_cmd = comandos.add_parser("verificar", help="Solo lectura")
    verificar_cmd.add_argument("parquet", type=Path)
    verificar_cmd.add_argument("--fuente", type=Path, default=FUENTE)
    verificar_cmd.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    verificar_cmd.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    if args.comando == "preparar":
        print(preparar(args.destino, args.fuente))
        return
    entrega = ejecutar_verificado(args.parquet, args.fuente, args.corte, args.minimo)
    print(f"Polars {pl.__version__}; fuente: {entrega['registros_fuente']} registros")
    for nombre, plan in entrega["planes"].items():
        print(nombre + ":\n" + plan)
    print("Seleccion:", entrega["seleccion"].to_dicts())
    print("Resumen:", entrega["resumen"].to_dicts())
    print("Conciliado:", entrega["control"])


if __name__ == "__main__":
    main()

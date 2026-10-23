"""Operaciones inmediatas y conciliacion didactica; importar no lee ni escribe."""

import argparse
from datetime import date
import importlib.util
from pathlib import Path

import polars as pl

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
ESQUEMA = {"id_credito": pl.String, "fecha_corte": pl.Date, "saldo_mxn": pl.Int32}
SELECCION = {"id_credito": pl.String, "saldo_mxn": pl.Int32}
RESUMEN = {"fecha_corte": pl.Date, "registros": pl.UInt32, "saldo_mxn": pl.Int64}
_spec = importlib.util.spec_from_file_location(
    "referencia_1002", CARPETA.parent / "01_question_contract_reference/referencia.py"
)
referencia = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(referencia)


def exigir_esquema(tabla, esperado):
    """Incluye columnas/orden y ausencias, incluso con cero filas."""
    if not isinstance(tabla, pl.DataFrame) or list(tabla.schema.items()) != list(esperado.items()):
        raise ValueError(f"Se requiere un DataFrame con esquema {esperado}")
    if any(tabla.null_count().row(0)):
        raise ValueError("Este contrato no admite null")


def validar_tabla(tabla):
    """Auditoria de toda la tabla; los bucles son controles, no la consulta Polars."""
    exigir_esquema(tabla, ESQUEMA)
    # Conserva el contrato textual reutilizado, sin convertir floats en enteros.
    textos = [dict(id_credito=f["id_credito"], fecha_corte=f["fecha_corte"].isoformat(),
                   saldo_mxn=str(f["saldo_mxn"])) for f in tabla.to_dicts()]
    evaluadas = referencia.reglas.evaluar_contrato(textos)
    if any(not f["aceptado"] for f in evaluadas):
        raise ValueError("Tabla fuera del contrato: ID, fecha, saldo o clave repetida")


def cargar_tabla(ruta=FUENTE):
    """Valida el CSV completo antes de convertir; no necesita entregas previas."""
    esperadas = referencia.cargar_filas(ruta)
    # Sin inferencia: 001 debe seguir siendo texto. La referencia revisa encabezados.
    textos = pl.read_csv(ruta, infer_schema=False, try_parse_dates=False)
    tabla = textos.with_columns(
        pl.col("fecha_corte").str.to_date("%Y-%m-%d", strict=True),
        pl.col("saldo_mxn").cast(pl.Int32, strict=True),
    )
    validar_tabla(tabla)
    clave = lambda f: (f["id_credito"], f["fecha_corte"])
    if sorted(tabla.to_dicts(), key=clave) != sorted(esperadas, key=clave):
        raise ValueError("La lectura Polars difiere de la referencia independiente")
    return tabla


def transformar(tabla):
    """Columna derivada con unidad distinta; la entrada conserva sus tres columnas."""
    validar_tabla(tabla)
    return tabla.with_columns((pl.col("saldo_mxn") / 1000).alias("saldo_miles_mxn"))


def seleccionar(tabla, corte=date(2026, 10, 31), minimo=2000):
    validar_tabla(tabla)
    referencia.validar_parametros(corte, minimo)
    return (
        tabla.filter((pl.col("fecha_corte") == corte) & (pl.col("saldo_mxn") >= minimo))
        .select("id_credito", "saldo_mxn")
        .sort("id_credito")
    )


def resumir_por_corte(tabla):
    validar_tabla(tabla)
    # Int32 admite cada importe, pero puede no admitir su suma. Ampliar ANTES.
    return tabla.group_by("fecha_corte").agg(
        pl.len().alias("registros"),
        pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn"),
    ).sort("fecha_corte")


def comprobar_seleccion(observada, ruta=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    exigir_esquema(observada, SELECCION)
    return referencia.comprobar_seleccion(observada.to_dicts(), ruta, corte, minimo)


def comprobar_resumen(observado, ruta=FUENTE):
    exigir_esquema(observado, RESUMEN)
    grupos = {}
    for fila in referencia.cargar_filas(ruta):
        grupo = grupos.setdefault(fila["fecha_corte"], dict(registros=0, saldo_mxn=0))
        grupo["registros"] += 1
        grupo["saldo_mxn"] += fila["saldo_mxn"]
    esperado = [dict(fecha_corte=corte, **grupos[corte]) for corte in sorted(grupos)]
    if observado.sort("fecha_corte").to_dicts() != esperado:
        raise ValueError("Resumen distinto por corte; revisar conteos e importes")
    return esperado


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    tabla = cargar_tabla(args.fuente)
    seleccion = seleccionar(tabla, args.corte, args.minimo)
    resumen = resumir_por_corte(tabla)
    control = comprobar_seleccion(seleccion, args.fuente, args.corte, args.minimo)
    comprobar_resumen(resumen, args.fuente)
    # Registros nativos: legibles tambien en terminales sin caracteres de tablas.
    print(f"Polars {pl.__version__}; fuente {tabla.shape}; esquema {dict(tabla.schema)}")
    print("Seleccion:", seleccion.to_dicts())
    print("Resumen:", resumen.to_dicts())
    print("Transformacion (miles MXN):", transformar(tabla).to_dicts())
    print("Conciliado:", control)


if __name__ == "__main__":
    main()

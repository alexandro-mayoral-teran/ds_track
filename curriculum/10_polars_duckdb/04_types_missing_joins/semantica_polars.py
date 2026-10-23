"""Contrato, union muchos-a-uno y cobertura; importar no lee ni escribe.

La auditoria didactica materializa tablas y registros. No mide rendimiento ni
memoria acotada. El CSV externo reconstruye cada valor esperado por clave.
"""

import argparse
import csv
from datetime import date
import importlib.util
from pathlib import Path
import re
import sqlite3

import polars as pl

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
CATALOGO = CARPETA / "catalogo.csv"
_spec = importlib.util.spec_from_file_location(
    "base_1004", CARPETA.parent / "02_polars_tables_expressions/tablas_polars.py"
)
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
ESQUEMA_CATALOGO = {"id_credito": pl.String, "producto": pl.String}
ESQUEMA_UNIDA = {
    **base.ESQUEMA, "producto": pl.String,
    "coincide_catalogo": pl.Boolean, "producto_conocido": pl.Boolean,
}
ESQUEMA_RESUMEN = {
    "fecha_corte": pl.Date, "registros": pl.UInt32, "saldo_mxn": pl.Int64,
    "coincidencias": pl.UInt32, "productos_conocidos": pl.UInt32,
    "sin_catalogo": pl.UInt32, "etiqueta_pendiente": pl.UInt32,
}


def cargar_saldos(ruta=FUENTE):
    """Reutiliza reglas del repositorio, no resultados de practicas anteriores."""
    return base.cargar_tabla(ruta)


def validar_catalogo(tabla):
    if not isinstance(tabla, pl.DataFrame) or list(tabla.schema.items()) != list(ESQUEMA_CATALOGO.items()):
        raise ValueError("Catalogo debe tener id_credito/producto String en ese orden")
    claves = set()
    for fila in tabla.to_dicts():
        clave, producto = fila["id_credito"], fila["producto"]
        if type(clave) is not str or not re.fullmatch(r"[0-9]{3}", clave) or clave in claves:
            raise ValueError("Clave de catalogo incompleta, invalida o repetida, incluso sin uso")
        if producto is not None and (type(producto) is not str or not producto.strip()):
            raise ValueError("Producto debe ser texto no vacio o null declarado")
        claves.add(clave)


def leer_catalogo_referencia(ruta=CATALOGO):
    """CSV textual: solo el campo producto vacio representa ausencia."""
    with Path(ruta).open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != list(ESQUEMA_CATALOGO):
            raise ValueError("Encabezado de catalogo distinto")
        filas = []
        claves = set()
        for f in lector:
            if set(f) != set(ESQUEMA_CATALOGO) or any(v is None for v in f.values()):
                raise ValueError("Registro CSV de catalogo incompleto o con campos adicionales")
            clave, producto = f["id_credito"], f["producto"]
            if not re.fullmatch(r"[0-9]{3}", clave) or clave in claves:
                raise ValueError("Clave de catalogo invalida o repetida")
            if producto != "" and not producto.strip():
                raise ValueError("Producto de espacios no es una etiqueta valida")
            claves.add(clave)
            filas.append(dict(id_credito=clave, producto=None if producto == "" else producto))
    return filas


def cargar_catalogo(ruta=CATALOGO):
    esperadas = leer_catalogo_referencia(ruta)
    tabla = pl.read_csv(ruta, schema=ESQUEMA_CATALOGO, null_values={"producto": ""})
    validar_catalogo(tabla)
    if tabla.to_dicts() != esperadas:
        raise ValueError("Lectura de catalogo distinta de la referencia textual")
    return tabla


def enriquecer(tabla, catalogo):
    """Conserva credito/corte; null en producto no basta para detectar el match."""
    base.validar_tabla(tabla)
    validar_catalogo(catalogo)
    derecha = catalogo.with_columns(pl.lit(True).alias("coincide_catalogo"))
    return (
        tabla.join(derecha, on="id_credito", how="left", validate="m:1", nulls_equal=False)
        .with_columns(
            pl.col("coincide_catalogo").fill_null(False),
            pl.col("producto").is_not_null().alias("producto_conocido"),
        )
        .select(list(ESQUEMA_UNIDA))
        .sort("fecha_corte", "id_credito")
    )


def referencia(fuente=FUENTE, catalogo=CATALOGO):
    filas = base.referencia.cargar_filas(fuente)
    productos = {f["id_credito"]: f["producto"] for f in leer_catalogo_referencia(catalogo)}
    salida = []
    for f in filas:
        clave = f["id_credito"]
        producto = productos.get(clave)
        salida.append(dict(**f, producto=producto, coincide_catalogo=clave in productos,
                           producto_conocido=producto is not None))
    return sorted(salida, key=lambda f: (f["fecha_corte"], f["id_credito"]))


def comprobar_salida(tabla, fuente=FUENTE, catalogo=CATALOGO):
    if not isinstance(tabla, pl.DataFrame) or list(tabla.schema.items()) != list(ESQUEMA_UNIDA.items()):
        raise ValueError("Esquema de union distinto")
    if tabla.sort("fecha_corte", "id_credito").to_dicts() != referencia(fuente, catalogo):
        raise ValueError("Union distinta por clave, valores o banderas; no basta la suma")


def resumir(tabla):
    return tabla.group_by("fecha_corte").agg(
        pl.len().alias("registros"),
        pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn"),
        pl.col("coincide_catalogo").sum().alias("coincidencias"),
        pl.col("producto_conocido").sum().alias("productos_conocidos"),
        (~pl.col("coincide_catalogo")).sum().alias("sin_catalogo"),
        (pl.col("coincide_catalogo") & ~pl.col("producto_conocido")).sum().alias("etiqueta_pendiente"),
    ).sort("fecha_corte")


def comprobar_resumen(tabla, fuente=FUENTE, catalogo=CATALOGO):
    if list(tabla.schema.items()) != list(ESQUEMA_RESUMEN.items()):
        raise ValueError("Esquema de resumen distinto")
    grupos = {}
    for f in referencia(fuente, catalogo):
        g = grupos.setdefault(f["fecha_corte"], dict(registros=0, saldo_mxn=0,
            coincidencias=0, productos_conocidos=0, sin_catalogo=0, etiqueta_pendiente=0))
        g["registros"] += 1
        g["saldo_mxn"] += f["saldo_mxn"]
        g["coincidencias"] += f["coincide_catalogo"]
        g["productos_conocidos"] += f["producto_conocido"]
        g["sin_catalogo"] += not f["coincide_catalogo"]
        g["etiqueta_pendiente"] += f["coincide_catalogo"] and not f["producto_conocido"]
    esperado = [dict(fecha_corte=corte, **grupos[corte]) for corte in sorted(grupos)]
    if tabla.sort("fecha_corte").to_dicts() != esperado:
        raise ValueError("Resumen o cobertura distintos de la referencia")


def contrastar(tabla, fuente=FUENTE, catalogo=CATALOGO):
    """Extension pandas/SQLite: comparar TODOS los campos, no solo agregados."""
    import pandas as pd

    filas = base.referencia.cargar_filas(fuente)
    productos = leer_catalogo_referencia(catalogo)
    izquierda = pd.DataFrame(filas, columns=list(base.ESQUEMA)).astype(
        {"id_credito": "string", "saldo_mxn": "int32"})
    derecha = pd.DataFrame(productos, columns=list(ESQUEMA_CATALOGO)).astype("string")
    unido = izquierda.merge(derecha, on="id_credito", how="left", validate="many_to_one", indicator=True)
    nativas = []
    for f in unido.to_dict("records"):
        producto = None if pd.isna(f["producto"]) else str(f["producto"])
        nativas.append(dict(id_credito=str(f["id_credito"]), fecha_corte=f["fecha_corte"],
            saldo_mxn=int(f["saldo_mxn"]), producto=producto,
            coincide_catalogo=f["_merge"] == "both", producto_conocido=producto is not None))
    comparar = lambda fs: sorted(fs, key=lambda f: (f["fecha_corte"], f["id_credito"]))
    esperado = referencia(fuente, catalogo)
    if comparar(nativas) != esperado:
        raise ValueError("Contraste pandas distinto")
    conexion = sqlite3.connect(":memory:")
    try:
        conexion.execute("CREATE TABLE saldos (id_credito TEXT, fecha_corte TEXT, saldo_mxn INTEGER)")
        conexion.execute("CREATE TABLE productos (id_credito TEXT PRIMARY KEY, producto TEXT)")
        conexion.executemany("INSERT INTO saldos VALUES (?, ?, ?)",
            [(f["id_credito"], f["fecha_corte"].isoformat(), f["saldo_mxn"]) for f in filas])
        conexion.executemany("INSERT INTO productos VALUES (?, ?)",
            [(f["id_credito"], f["producto"]) for f in productos])
        sql = conexion.execute("""SELECT s.id_credito, s.fecha_corte, s.saldo_mxn,
            p.producto, p.id_credito IS NOT NULL, p.producto IS NOT NULL
            FROM saldos AS s LEFT JOIN productos AS p ON s.id_credito = p.id_credito""").fetchall()
        registros = [dict(id_credito=f[0], fecha_corte=date.fromisoformat(f[1]), saldo_mxn=f[2],
            producto=f[3], coincide_catalogo=bool(f[4]), producto_conocido=bool(f[5])) for f in sql]
        if comparar(registros) != esperado:
            raise ValueError("Contraste SQLite distinto")
    finally:
        conexion.close()
    comprobar_salida(tabla, fuente, catalogo)
    return dict(pandas=pd.__version__, sqlite=sqlite3.sqlite_version, registros=len(esperado))


def ejecutar(fuente=FUENTE, catalogo=CATALOGO, otros_motores=False):
    tabla = cargar_saldos(fuente)
    productos = cargar_catalogo(catalogo)
    unida = enriquecer(tabla, productos)
    comprobar_salida(unida, fuente, catalogo)
    resumen = resumir(unida)
    comprobar_resumen(resumen, fuente, catalogo)
    contraste = contrastar(unida, fuente, catalogo) if otros_motores else None
    return dict(unida=unida, resumen=resumen, contraste=contraste)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--catalogo", type=Path, default=CATALOGO)
    parser.add_argument("--contrastar", action="store_true", help="Extension pandas y SQLite")
    args = parser.parse_args()
    entrega = ejecutar(args.fuente, args.catalogo, args.contrastar)
    print(f"Polars {pl.__version__}")
    print("Union:", entrega["unida"].to_dicts())
    print("Resumen:", entrega["resumen"].to_dicts())
    if entrega["contraste"] is not None:
        print("Contraste:", entrega["contraste"])


if __name__ == "__main__":
    main()

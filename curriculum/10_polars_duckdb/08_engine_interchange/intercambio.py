"""Intercambio en memoria; importar define funciones, no lee ni escribe.

La auditoria materializa valores pequenos; no es benchmark ni memoria acotada.
"""
import argparse
from datetime import date
import importlib.util
from pathlib import Path

import duckdb
import pandas as pd
import polars as pl
import pyarrow as pa

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location(
    "referencia_1008", CARPETA.parent / "01_question_contract_reference/referencia.py")
referencia = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(referencia)
ESQUEMA = pa.schema([("id_credito", pa.string()), ("fecha_corte", pa.date32()),
                     ("saldo_mxn", pa.int32())])
SQL = """SELECT id_credito, saldo_mxn FROM entrada
WHERE fecha_corte = CAST(? AS DATE) AND saldo_mxn >= ? ORDER BY id_credito"""


def comprobar_arrow(tabla, esperadas, seleccion=False):
    """Inspecciona antes de adaptar: solo string/large_string son equivalentes aqui.

    No certifica igualdad de metadatos, nullability declarada o disposicion fisica.
    """
    nombres = ["id_credito", "saldo_mxn"] if seleccion else ESQUEMA.names
    if not isinstance(tabla, pa.Table) or tabla.column_names != nombres:
        raise ValueError("Tabla/columnas fuera del contrato")
    for campo in tabla.schema:
        valido = ((campo.name == "id_credito" and
                   (pa.types.is_string(campo.type) or pa.types.is_large_string(campo.type))) or
                  (campo.name == "fecha_corte" and campo.type == pa.date32()) or
                  (campo.name == "saldo_mxn" and campo.type == pa.int32()))
        if not valido:
            raise ValueError(f"Tipo incompatible antes de adaptar: {campo}")
    filas = tabla.to_pylist()
    for f in filas:
        if (type(f["id_credito"]) is not str or type(f["saldo_mxn"]) is not int or
                (not seleccion and type(f["fecha_corte"]) is not date)):
            raise ValueError("Ausencias/tipos nativos incompatibles")
    clave = lambda f: tuple(f[n] for n in nombres)
    if sorted(filas, key=clave) != sorted(esperadas, key=clave):
        raise ValueError("Valores distintos por clave, aunque coincidan sumas")
    return {"filas": len(filas), "esquema": str(tabla.schema),
            "ausencias": {n: tabla[n].null_count for n in nombres}}


def pandas_desde_filas(filas):
    # Dtypes explicitos conservan esquema tambien con cero filas.
    return pd.DataFrame({campo.name: pd.Series([f[campo.name] for f in filas],
        dtype=pd.ArrowDtype(campo.type)) for campo in ESQUEMA})


def ejecutar(fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    referencia.validar_parametros(corte, minimo)
    filas = referencia.cargar_filas(fuente)  # Contrato completo antes de filtrar.
    pandas_origen = pandas_desde_filas(filas)
    origen = pa.Table.from_pandas(pandas_origen, preserve_index=False)
    etapas = {"pandas_a_arrow": comprobar_arrow(origen, filas)}
    polars = pl.from_arrow(origen, rechunk=False)
    puente = polars.to_arrow()
    etapas["polars_a_arrow"] = comprobar_arrow(puente, filas)
    with duckdb.connect(":memory:") as con:
        # Registro explicito, sin depender de nombres de variables Python en SQL.
        for nombre, objeto in [("desde_pandas", pandas_origen), ("desde_polars", polars),
                               ("entrada", puente)]:
            con.register(nombre, objeto)
            try:
                tabla = con.sql(f"SELECT * FROM {nombre}").to_arrow_table()
                etapas[nombre] = comprobar_arrow(tabla, filas)
            finally:
                if nombre != "entrada":
                    con.unregister(nombre)
        try:
            relacion = con.sql(SQL, params=[corte, minimo])
            if [str(t) for t in relacion.types] != ["VARCHAR", "INTEGER"]:
                raise ValueError("Tipos SQL de seleccion incompatibles")
            esperada = referencia.construir_referencia(fuente, corte, minimo)["seleccion"]
            seleccion = relacion.to_arrow_table()
            etapas["seleccion_arrow"] = comprobar_arrow(seleccion, esperada, True)
            etapas["seleccion_polars"] = comprobar_arrow(relacion.pl().to_arrow(), esperada, True)
            # 'tabla' es la lectura completa del registro 'entrada', no la seleccion.
            pandas_final = tabla.to_pandas(types_mapper=pd.ArrowDtype)
            vuelta = pa.Table.from_pandas(pandas_final, preserve_index=False)
            etapas["duckdb_arrow_pandas_arrow"] = comprobar_arrow(vuelta, filas)
            resumen = con.sql("""SELECT fecha_corte, CAST(COUNT(*) AS VARCHAR) AS registros,
                CAST(SUM(saldo_mxn) AS VARCHAR) AS saldo FROM entrada
                GROUP BY fecha_corte ORDER BY fecha_corte""").fetchall()
            grupos = {}
            for f in filas:
                n, s = grupos.get(f["fecha_corte"], (0, 0))
                grupos[f["fecha_corte"]] = n+1, s+f["saldo_mxn"]
            if resumen != [(c, str(grupos[c][0]), str(grupos[c][1])) for c in sorted(grupos)]:
                raise ValueError("Resumen distinto de Python estandar")
        finally:
            con.unregister("entrada")
    return dict(etapas=etapas, seleccion=seleccion.to_pylist(), resumen=resumen,
                dtypes_pandas={n: str(t) for n, t in pandas_final.dtypes.items()},
                control=referencia.comprobar_seleccion(seleccion.to_pylist(), fuente, corte, minimo))


def ejemplo_anulable():
    """Contrato independiente: permite ausencia, vacio y cero; no es cartera aceptada."""
    origen = pa.table({"id": pa.array(["001", "002", "003"], type=pa.string()),
        "importe": pa.array([0, None, 10], type=pa.int32()),
        "etiqueta": pa.array(["", None, "café"], type=pa.string())})
    puente = pl.from_arrow(origen, rechunk=False).to_arrow()
    with duckdb.connect(":memory:") as con:
        con.register("anulable", puente)
        try:
            salida = con.sql("SELECT * FROM anulable ORDER BY id").to_arrow_table()
        finally:
            con.unregister("anulable")
    pandas = salida.to_pandas(types_mapper=pd.ArrowDtype)
    vuelta = pa.Table.from_pandas(pandas, preserve_index=False)
    if not vuelta.equals(origen, check_metadata=False):
        raise ValueError("Cambio de tipos/valores en muestra anulable")
    valores = vuelta.to_pylist()
    observados = [f["importe"] for f in valores if f["importe"] is not None]
    return dict(valores=valores, suma_observada=sum(observados), observados=len(observados), registros=len(valores),
        tipos_default={n: str(t) for n, t in salida.to_pandas().dtypes.items()},
        tipos_anulables={n: str(t) for n, t in pandas.dtypes.items()})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    print("Versiones:", pd.__version__, pa.__version__, pl.__version__, duckdb.__version__)
    print(ejecutar(args.fuente, args.corte, args.minimo))
    print(ejemplo_anulable())


if __name__ == "__main__":
    main()

"""CSV validado -> pandas -> Arrow -> Parquet; verificacion de solo lectura.

Referencia: pandas 2.3.3/PyArrow 21.0.0. No ejecuta acciones al importar.
"""

import argparse
from datetime import date
import importlib.util
import json
from pathlib import Path
import platform

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA.parent / "01_csv_parquet_arrow" / "datos" / "base_comun.csv"

# Reutiliza las reglas de 09.02 sin copiarlas ni instalar el repo como paquete.
_ruta = CARPETA.parent / "02_schemas_types" / "contrato_tabla.py"
_spec = importlib.util.spec_from_file_location("contrato_0902", _ruta)
_contrato = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_contrato)
COLUMNAS = _contrato.COLUMNAS
ESQUEMA = pa.schema([
    pa.field("id_credito", pa.string(), nullable=False),
    pa.field("fecha_corte", pa.date32(), nullable=False),
    pa.field("saldo_mxn", pa.int32(), nullable=False),
])


def _exigir_reglas(textos):
    evaluados = _contrato.evaluar_contrato(textos)
    fallos = [(i, r["motivos"]) for i, r in enumerate(evaluados, 1) if not r["aceptado"]]
    if fallos:
        raise ValueError(f"Contrato incumplido (registro, motivos): {fallos}")
    return evaluados


def cargar_dataframe(ruta=FUENTE):
    """Lee texto y rechaza el lote si una fila falla; no filtra silenciosamente."""
    evaluados = _exigir_reglas(_contrato.leer_textos(ruta, COLUMNAS))
    return pd.DataFrame({
        "id_credito": pd.Series([r["original"]["id_credito"] for r in evaluados],
                                dtype=pd.StringDtype(storage="python")),
        "fecha_corte": pd.Series([r["fecha"] for r in evaluados], dtype="object"),
        "saldo_mxn": pd.Series([r["saldo"] for r in evaluados], dtype="Int32"),
    })


def validar_tabla(tabla):
    """Exige estructura, nulabilidad, valores presentes, dominio y claves.

    validate(full=True) comprueba consistencia Arrow; las reglas del dominio
    se verifican aparte. Los metadatos auxiliares no definen la igualdad aqui.
    """
    if not isinstance(tabla, pa.Table) or not tabla.schema.equals(ESQUEMA, check_metadata=False):
        raise ValueError("Esquema distinto: se exige string/date32/int32 no anulables")
    tabla.validate(full=True)
    if any(col.null_count for col in tabla.columns):
        raise ValueError("El contrato no admite celdas ausentes")
    filas = tabla.to_pylist()
    textos = [{"id_credito": f["id_credito"], "fecha_corte": f["fecha_corte"].isoformat(),
               "saldo_mxn": str(f["saldo_mxn"])} for f in filas]
    _exigir_reglas(textos)
    return filas


def crear_tabla(df):
    """Convierte el DataFrame canonico; el indice solo identifica posiciones locales."""
    if not isinstance(df, pd.DataFrame) or list(df.columns) != COLUMNAS:
        raise ValueError("Se requieren exactamente las tres columnas en orden")
    if (df["id_credito"].dtype != pd.StringDtype(storage="python")
            or df["fecha_corte"].dtype != object
            or df["saldo_mxn"].dtype != pd.Int32Dtype()):
        raise ValueError("Usa string[python], object con date e Int32; no inferir ni truncar")
    if df.isna().any().any() or any(type(v) is not date for v in df["fecha_corte"]):
        raise ValueError("Se requieren valores presentes y fechas date, sin hora")
    tabla = pa.Table.from_pandas(df, schema=ESQUEMA, preserve_index=False, safe=True)
    # El intercambio se apoya en columnas explicitas; no requiere metadatos pandas.
    tabla = tabla.replace_schema_metadata(None)
    validar_tabla(tabla)
    return tabla


def comparar_tablas(esperada, observada):
    """Compara todos los valores por ID/corte, sin depender del orden ni de sumas."""
    a = validar_tabla(esperada)
    b = validar_tabla(observada)
    clave = lambda f: (f["id_credito"], f["fecha_corte"])
    if sorted(a, key=clave) != sorted(b, key=clave):
        raise ValueError("Valores o claves distintos de la fuente, aunque coincidan sumas")


def resumir(tabla):
    """Los importes se suman como int de Python; un resumen vacio no inventa cortes."""
    filas = validar_tabla(tabla)
    cortes = sorted({f["fecha_corte"] for f in filas})
    return dict(registros=len(filas), ids=len({f["id_credito"] for f in filas}),
                cortes=[dict(fecha_corte=c.isoformat(),
                             registros=sum(f["fecha_corte"] == c for f in filas),
                             saldo_mxn=sum(f["saldo_mxn"] for f in filas if f["fecha_corte"] == c))
                        for c in cortes])


def verificar_parquet(ruta_parquet, ruta_csv=FUENTE):
    """Reconstruye la fuente y decodifica un ARCHIVO, sin escribir ni imponer esquema al leer."""
    ruta_parquet = Path(ruta_parquet)
    if not ruta_parquet.is_file():
        raise ValueError("Se requiere un archivo Parquet, no una carpeta de dataset")
    esperada = crear_tabla(cargar_dataframe(ruta_csv))
    # Lee el archivo individual sin descubrir particiones desde sus carpetas padre.
    observada = pq.ParquetFile(ruta_parquet).read()
    comparar_tablas(esperada, observada)
    return resumir(observada)


def crear_entrega(destino, ruta_csv=FUENTE):
    """Crea carpeta nueva, escribe, cierra y relee. Una ruta ocupada nunca se reutiliza.

    Si falla la escritura/relectura, queda la carpeta parcial para diagnosticar;
    no es una entrega completa. No se borra ni repara automaticamente.
    """
    tabla = crear_tabla(cargar_dataframe(ruta_csv))
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    ruta = destino / "base_comun.parquet"
    with ruta.open("xb") as archivo:
        pq.write_table(tabla, archivo, version="2.6", compression="snappy")
    resumen = verificar_parquet(ruta, ruta_csv)
    registro = dict(python=platform.python_version(), pandas=pd.__version__,
                    pyarrow=pa.__version__, esquema=str(ESQUEMA),
                    indice="omitido; clave en columnas", **resumen)
    with (destino / "sesion.json").open("x", encoding="utf-8", newline="\n") as archivo:
        json.dump(registro, archivo, ensure_ascii=False, indent=2)
        archivo.write("\n")
    return registro


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    acciones = parser.add_mutually_exclusive_group(required=True)
    acciones.add_argument("--salida", type=Path, help="Carpeta NUEVA para Parquet y sesion.json")
    acciones.add_argument("--verificar", type=Path, help="Parquet existente; solo lectura")
    parser.add_argument("--fuente", type=Path, default=FUENTE, help="CSV bajo el contrato de 09.02")
    args = parser.parse_args()
    resultado = (crear_entrega(args.salida, args.fuente) if args.salida is not None
                 else verificar_parquet(args.verificar, args.fuente))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

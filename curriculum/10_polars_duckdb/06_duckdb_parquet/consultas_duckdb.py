"""SQL directo sobre Parquet; importar no lee fuentes ni escribe.

La auditoria completa materializa registros y se separa de la consulta selectiva.
Preparar crea una carpeta exclusiva; verificar solo lee archivos existentes.
"""

import argparse
from datetime import date
import importlib.util
from pathlib import Path

import duckdb

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location(
    "referencia_1006", CARPETA.parent / "01_question_contract_reference/referencia.py"
)
referencia = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(referencia)
ESQUEMA = [("id_credito", "VARCHAR"), ("fecha_corte", "DATE"), ("saldo_mxn", "INTEGER")]
SELECCION = [("id_credito", "VARCHAR"), ("saldo_mxn", "INTEGER")]
RESUMEN = [("fecha_corte", "DATE"), ("registros", "BIGINT"), ("saldo_mxn", "HUGEINT")]


def rutas_explicitas(rutas):
    if isinstance(rutas, (str, Path)):
        rutas = [rutas]
    if not isinstance(rutas, (list, tuple)) or not rutas:
        raise ValueError("Se requiere al menos un archivo explicito")
    archivos = [Path(r).resolve() for r in rutas]
    if any(not p.is_file() for p in archivos) or len(set(archivos)) != len(archivos):
        raise ValueError("Archivos ausentes o rutas repetidas")
    return [str(p) for p in archivos]


def esquema_resultado(conexion):
    return [(d[0], str(d[1])) for d in conexion.description]


def auditar(conexion, rutas, fuente=FUENTE):
    archivos = rutas_explicitas(rutas)
    esperadas = referencia.cargar_filas(fuente)
    for archivo in archivos:
        descripcion = conexion.execute("DESCRIBE SELECT * FROM read_parquet(?)", [archivo]).fetchall()
        if [(f[0], f[1]) for f in descripcion] != ESQUEMA:
            raise ValueError("Cada archivo debe tener VARCHAR/DATE/INTEGER en el orden del contrato")
    filas = conexion.execute("SELECT * FROM read_parquet(?)", [archivos]).fetchall()
    if any(type(f[0]) is not str or type(f[1]) is not date or type(f[2]) is not int for f in filas):
        raise ValueError("Ausencias o tipos nativos fuera del contrato")
    textos = [dict(id_credito=f[0], fecha_corte=f[1].isoformat(), saldo_mxn=str(f[2])) for f in filas]
    if any(not f["aceptado"] for f in referencia.reglas.evaluar_contrato(textos)):
        raise ValueError("ID, fecha, saldo o clave repetida fuera del contrato")
    esperado = [(f["id_credito"], f["fecha_corte"], f["saldo_mxn"]) for f in esperadas]
    if sorted(filas) != sorted(esperado):
        raise ValueError("Parquet distinto del CSV externo por clave/valor")
    return archivos


def preparar(destino, fuente=FUENTE):
    filas = referencia.cargar_filas(fuente)
    destino = Path(destino)
    destino.mkdir(parents=True, exist_ok=False)
    partes = destino / "partes"
    partes.mkdir()
    conexion = duckdb.connect(":memory:")
    try:
        conexion.execute("CREATE TABLE saldos(id_credito VARCHAR, fecha_corte DATE, saldo_mxn INTEGER)")
        if filas:
            conexion.executemany("INSERT INTO saldos VALUES (?, ?, ?)",
                [(f["id_credito"], f["fecha_corte"], f["saldo_mxn"]) for f in filas])
        completo = destino / "completo.parquet"
        conexion.execute("COPY saldos TO ? (FORMAT PARQUET, COMPRESSION ZSTD)", [str(completo)])
        archivos = []
        cortes = sorted({f["fecha_corte"] for f in filas})
        for i, corte in enumerate(cortes or [None], 1):
            archivo = partes / f"parte_{i:02d}.parquet"
            conexion.execute("COPY (SELECT * FROM saldos WHERE fecha_corte = ?) TO ? (FORMAT PARQUET, COMPRESSION ZSTD)",
                             [corte, str(archivo)])
            archivos.append(archivo)
        auditar(conexion, completo, fuente)
        auditar(conexion, archivos, fuente)
        return dict(completo=completo, partes=archivos)
    finally:
        conexion.close()


def ejecutar(rutas, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000):
    """Solo lectura; EXPLAIN ANALYZE se limita a nuestro SELECT fijo."""
    referencia.validar_parametros(corte, minimo)
    conexion = duckdb.connect(":memory:")
    try:
        archivos = auditar(conexion, rutas, fuente)
        sql = (CARPETA / "seleccion.sql").read_text(encoding="utf-8")
        parametros = [archivos, corte, minimo]
        plan = conexion.execute("EXPLAIN " + sql, parametros).fetchall()
        analisis = conexion.execute("EXPLAIN ANALYZE " + sql, parametros).fetchall()
        conexion.execute(sql, parametros)
        if esquema_resultado(conexion) != SELECCION:
            raise ValueError("Esquema de seleccion distinto")
        seleccion = conexion.fetchall()
        control = referencia.comprobar_seleccion(
            [dict(id_credito=f[0], saldo_mxn=f[1]) for f in seleccion], fuente, corte, minimo)
        conexion.execute((CARPETA / "resumen.sql").read_text(encoding="utf-8"), [archivos])
        if esquema_resultado(conexion) != RESUMEN:
            raise ValueError("Esquema de resumen distinto de Date/BIGINT/HUGEINT")
        resumen = conexion.fetchall()
        grupos = {}
        for f in referencia.cargar_filas(fuente):
            n, suma = grupos.get(f["fecha_corte"], (0, 0))
            grupos[f["fecha_corte"]] = n + 1, suma + f["saldo_mxn"]
        if resumen != [(c, *grupos[c]) for c in sorted(grupos)]:
            raise ValueError("Resumen distinto por corte")
        return dict(seleccion=seleccion, resumen=resumen, control=control,
                    plan=plan, analisis=analisis)
    finally:
        conexion.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    comandos = parser.add_subparsers(dest="comando", required=True)
    nuevo = comandos.add_parser("preparar")
    nuevo.add_argument("destino", type=Path)
    nuevo.add_argument("--fuente", type=Path, default=FUENTE)
    verificar = comandos.add_parser("verificar")
    verificar.add_argument("archivos", nargs="+", type=Path)
    verificar.add_argument("--fuente", type=Path, default=FUENTE)
    verificar.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    verificar.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    if args.comando == "preparar":
        print(preparar(args.destino, args.fuente))
    else:
        entrega = ejecutar(args.archivos, args.fuente, args.corte, args.minimo)
        print(f"DuckDB {duckdb.__version__}")
        for nombre in ("plan", "analisis"):
            for clave, valor in entrega[nombre]:
                print(clave, "\n", valor)
        print("Seleccion:", entrega["seleccion"])
        print("Resumen:", entrega["resumen"])
        print("Conciliado:", entrega["control"])


if __name__ == "__main__":
    main()

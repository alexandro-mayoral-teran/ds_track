"""Consulta compartida Python/R; importar no lee fuentes ni escribe."""
import argparse
from datetime import date
import importlib.util
from pathlib import Path
import duckdb

CARPETA = Path(__file__).resolve().parent
FUENTE = CARPETA / "muestra.csv"
_spec = importlib.util.spec_from_file_location("base_1007", CARPETA.parent / "06_duckdb_parquet/consultas_duckdb.py")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)


def preparar(destino, fuente=FUENTE):
    return base.preparar(destino, fuente)["completo"]


def ejecutar(archivo, fuente=FUENTE, corte=date(2026, 10, 31), minimo=2000, pagina=2):
    base.referencia.validar_parametros(corte, minimo)
    if not isinstance(archivo, (str, Path)):
        raise ValueError("Indica un unico archivo Parquet")
    if type(pagina) is not int or pagina < 1:
        raise ValueError("pagina debe ser entero positivo")
    with duckdb.connect(":memory:") as con:
        rutas = base.auditar(con, archivo, fuente)
        sql = (CARPETA / "seleccion.sql").read_text(encoding="utf-8")
        con.execute(sql, [rutas[0], corte, minimo])
        if base.esquema_resultado(con) != base.SELECCION:
            raise ValueError("Salida distinta de VARCHAR/INTEGER")
        filas = []
        while True:
            bloque = con.fetchmany(pagina)
            if not bloque:
                break
            filas.extend(bloque)
        control = base.referencia.comprobar_seleccion(
            [dict(id_credito=f[0], saldo_mxn=f[1]) for f in filas], fuente, corte, minimo)
        con.execute((CARPETA / "resumen.sql").read_text(encoding="utf-8"), [rutas[0]])
        if base.esquema_resultado(con) != [("fecha_corte", "DATE"), ("registros_texto", "VARCHAR"), ("saldo_texto", "VARCHAR")]:
            raise ValueError("Resumen debe conservar conteos/sumas como texto exacto")
        resumen = con.fetchall()
        grupos = {}
        for f in base.referencia.cargar_filas(fuente):
            n, suma = grupos.get(f["fecha_corte"], (0, 0))
            grupos[f["fecha_corte"]] = n + 1, suma + f["saldo_mxn"]
        if resumen != [(c, str(grupos[c][0]), str(grupos[c][1])) for c in sorted(grupos)]:
            raise ValueError("Resumen distinto de referencia externa")
        version = con.execute("SELECT version()").fetchone()[0]
    return dict(seleccion=filas, resumen=resumen, control=control, version=version)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path)
    parser.add_argument("--fuente", type=Path, default=FUENTE)
    parser.add_argument("--corte", type=date.fromisoformat, default=date(2026, 10, 31))
    parser.add_argument("--minimo", type=int, default=2000)
    parser.add_argument("--preparar", action="store_true", help="archivo se interpreta como carpeta NUEVA")
    args = parser.parse_args()
    archivo = preparar(args.archivo, args.fuente) if args.preparar else args.archivo
    print(ejecutar(archivo, args.fuente, args.corte, args.minimo))


if __name__ == "__main__":
    main()

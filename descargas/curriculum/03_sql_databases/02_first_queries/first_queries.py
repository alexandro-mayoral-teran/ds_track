"""Consultar la base de 03.01 en solo lectura; no crear ni reemplazar datos."""

from pathlib import Path
import argparse
import sqlite3

DEFAULT_DATABASE = Path(__file__).resolve().parents[1] / "01_relational_sqlite/output/cartera_demo.sqlite"

CONSULTAS = {
    "primeros": ("SELECT id_credito AS credito, saldo_mxn FROM cortes WHERE fecha_corte = ? ORDER BY id_credito LIMIT 3", ("2026-10-31",)),
    "atrasados": ("SELECT id_credito, saldo_mxn, dias_atraso FROM cortes WHERE fecha_corte = ? AND dias_atraso >= ? ORDER BY dias_atraso DESC, id_credito", ("2026-10-31", 30)),
    "sin_saldo": ("SELECT id_credito FROM cortes WHERE fecha_corte = ? AND saldo_mxn IS NULL ORDER BY id_credito", ("2026-10-31",)),
    "cero": ("SELECT id_credito FROM cortes WHERE fecha_corte = ? AND saldo_mxn = 0 ORDER BY id_credito", ("2026-10-31",)),
    "fechas": ("SELECT DISTINCT fecha_corte FROM cortes ORDER BY fecha_corte", ()),
    "vacio": ("SELECT id_credito FROM cortes WHERE fecha_corte = ? AND dias_atraso > ? ORDER BY id_credito", ("2026-10-31", 100)),
}


def abrir_consulta(ruta):
    if not ruta.is_file():
        raise FileNotFoundError("Falta la base: ejecuta primero el preparador de 03.01 o revisa --database")
    # mode=ro impide escrituras y evita crear una base vacía por una ruta equivocada.
    return sqlite3.connect(ruta.resolve().as_uri() + "?mode=ro", uri=True)


def consultar(conexion, sql, parametros=()):
    cursor = conexion.execute(sql, parametros)
    columnas = tuple(campo[0] for campo in cursor.description)
    return columnas, cursor.fetchall()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    argumentos = parser.parse_args()
    conexion = abrir_consulta(argumentos.database)
    try:
        for nombre, (sql, parametros) in CONSULTAS.items():
            columnas, filas = consultar(conexion, sql, parametros)
            print(f"\n{nombre}: {len(filas)} filas; columnas: {columnas}")
            for fila in filas:
                print(fila)
            if not filas:
                print("Sin filas para estas condiciones")
    finally:
        conexion.close()


if __name__ == "__main__":
    main()

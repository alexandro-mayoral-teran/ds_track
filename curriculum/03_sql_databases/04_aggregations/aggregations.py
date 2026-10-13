"""Resumir la muestra SQL con bases explícitas y comprobar contra los CSV."""

import argparse
from collections import defaultdict
import csv
import math
from pathlib import Path
import sqlite3

SOURCE = Path(__file__).resolve().parents[1] / "01_relational_sqlite"
DEFAULT_DATABASE = SOURCE / "output" / "cartera_demo.sqlite"

MEASURES = """
COUNT(*) AS registros,
COUNT(DISTINCT id_credito) AS creditos_distintos,
COUNT(saldo_mxn) AS saldos_conocidos,
SUM(saldo_mxn) AS suma_conocida_mxn,
AVG(saldo_mxn) AS promedio_conocido_mxn,
MIN(saldo_mxn) AS minimo_conocido_mxn,
MAX(saldo_mxn) AS maximo_conocido_mxn,
COUNT(dias_atraso) AS atrasos_conocidos,
COUNT(CASE WHEN dias_atraso >= 30 THEN 1 END) AS atrasos_30_confirmados,
100.0 * COUNT(saldo_mxn) / NULLIF(COUNT(*), 0) AS cobertura_saldo_pct,
100.0 * COUNT(dias_atraso) / NULLIF(COUNT(*), 0) AS cobertura_atraso_pct,
100.0 * COUNT(CASE WHEN dias_atraso >= 30 THEN 1 END)
      / NULLIF(COUNT(dias_atraso), 0) AS atraso_30_pct_conocidos
"""
TOTAL = f"SELECT {MEASURES} FROM cortes WHERE fecha_corte = ?"
BY_DATE = f"SELECT fecha_corte, {MEASURES} FROM cortes GROUP BY fecha_corte ORDER BY fecha_corte"
BY_SEGMENT = f"""
SELECT fecha_corte, segmento, {MEASURES}
FROM detalle
GROUP BY fecha_corte, segmento
ORDER BY fecha_corte, segmento
"""
HAVING = """
SELECT segmento, COUNT(*) AS registros, COUNT(saldo_mxn) AS saldos_conocidos
FROM detalle
WHERE fecha_corte = ?
GROUP BY segmento
HAVING COUNT(*) >= ?
ORDER BY segmento
"""


def read_csv(name):
    with (SOURCE / "data" / f"{name}.csv").open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def source_rows():
    credits = [(row["id_credito"], row["id_cliente"], row["segmento"])
               for row in read_csv("creditos")]
    observations = []
    for row in read_csv("cortes"):
        observations.append((row["id_credito"], row["fecha_corte"],
                             None if row["saldo_mxn"] == "" else int(row["saldo_mxn"]),
                             None if row["dias_atraso"] == "" else int(row["dias_atraso"])))
    return credits, observations


def reference(rows):
    """Cálculos en Python independientes de las expresiones agregadas SQL."""
    balances = [row[2] for row in rows if row[2] is not None]
    delays = [row[3] for row in rows if row[3] is not None]
    late = sum(value >= 30 for value in delays)
    return (len(rows), len({row[0] for row in rows}), len(balances),
            sum(balances) if balances else None,
            sum(balances) / len(balances) if balances else None,
            min(balances) if balances else None, max(balances) if balances else None,
            len(delays), late,
            100.0 * len(balances) / len(rows) if rows else None,
            100.0 * len(delays) / len(rows) if rows else None,
            100.0 * late / len(delays) if delays else None)


def check_rows(actual, expected):
    if len(actual) != len(expected):
        raise ValueError("Cantidad de grupos distinta de la referencia")
    for row, wanted in zip(actual, expected):
        if len(row) != len(wanted):
            raise ValueError("Columnas distintas de la referencia")
        for value, target in zip(row, wanted):
            if isinstance(target, float):
                if value is None or not math.isclose(value, target, rel_tol=1e-12, abs_tol=1e-12):
                    raise ValueError(f"Indicador distinto: {value} frente a {target}")
            elif value != target:
                raise ValueError(f"Resultado distinto: {value} frente a {target}")


def memory_detail(credits, observations):
    # Puente en Python: buscar el segmento por ID; los joins SQL se enseñan en 03.05.
    segments = {row[0]: row[2] for row in credits}
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("""CREATE TABLE detalle (
            id_credito TEXT NOT NULL, fecha_corte TEXT NOT NULL,
            saldo_mxn INTEGER, dias_atraso INTEGER, segmento TEXT NOT NULL,
            PRIMARY KEY (id_credito, fecha_corte))""")
        connection.executemany("INSERT INTO detalle VALUES (?, ?, ?, ?, ?)",
                               [row + (segments[row[0]],) for row in observations])
    except Exception:
        connection.close()
        raise
    return connection


def check_edge_cases():
    cases = {
        "vacio": [],
        "todo_desconocido": [("A", "practica", None, None), ("B", "practica", None, None)],
        "cero_conocido": [("A", "practica", 0, 0)],
        "frontera_30": [("A", "practica", 100, 29), ("B", "practica", 100, 30),
                        ("C", "practica", None, None)],
    }
    for name, rows in cases.items():
        connection = sqlite3.connect(":memory:")
        try:
            connection.execute("CREATE TABLE cortes (id_credito TEXT, fecha_corte TEXT, saldo_mxn INTEGER, dias_atraso INTEGER)")
            connection.executemany("INSERT INTO cortes VALUES (?, ?, ?, ?)", rows)
            cursor = connection.execute(TOTAL, ("practica",))
            result = cursor.fetchall()
            check_rows(result, [reference(rows)])
            labels = [field[0] for field in cursor.description]
            print(f"Caso {name} comprobado:", dict(zip(labels, result[0])))
        finally:
            connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args()
    if not args.database.is_file():
        raise FileNotFoundError("Falta la base de 03.01; prepárala o revisa --database")
    expected_credits, expected_observations = source_rows()
    connection = sqlite3.connect(args.database.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        connection.execute("BEGIN")  # Una instantánea para las consultas de comprobación.
        credits = connection.execute("SELECT id_credito, id_cliente, segmento FROM creditos ORDER BY id_credito").fetchall()
        observations = connection.execute("SELECT id_credito, fecha_corte, saldo_mxn, dias_atraso FROM cortes ORDER BY id_credito, fecha_corte").fetchall()
        if credits != sorted(expected_credits) or observations != sorted(expected_observations):
            raise ValueError("La base difiere de la muestra original; se conserva sin cambios")
        by_date = defaultdict(list)
        for row in expected_observations:
            by_date[row[1]].append(row)
        expected = [(date,) + reference(rows) for date, rows in sorted(by_date.items())]
        cursor = connection.execute(BY_DATE)
        result = cursor.fetchall()
        check_rows(result, expected)
        labels = [field[0] for field in cursor.description]
        print("Por fecha:")
        for row in result:
            print(dict(zip(labels, row)))
        check_rows(connection.execute(TOTAL, ("2099-01-31",)).fetchall(), [reference([])])
    finally:
        connection.close()

    memory = memory_detail(credits, observations)
    try:
        segments = {row[0]: row[2] for row in expected_credits}
        groups = defaultdict(list)
        for row in expected_observations:
            groups[(row[1], segments[row[0]])].append(row)
        expected = [key + reference(rows) for key, rows in sorted(groups.items())]
        cursor = memory.execute(BY_SEGMENT)
        result = cursor.fetchall()
        check_rows(result, expected)
        # Los grupos deben formar una partición del detalle, no repetirlo.
        if sum(row[2] for row in result) != len(observations):
            raise ValueError("Los conteos no concilian con el detalle")
        known = [row[2] for row in observations if row[2] is not None]
        if sum(row[5] for row in result if row[5] is not None) != sum(known):
            raise ValueError("Las sumas por grupo no concilian")
        labels = [field[0] for field in cursor.description]
        print("Por fecha y segmento:")
        for row in result:
            print(dict(zip(labels, row)))
        filtered = memory.execute(HAVING, ("2026-10-31", 5)).fetchall()
        wanted = [(segment, len(rows), sum(row[2] is not None for row in rows))
                  for (date, segment), rows in sorted(groups.items())
                  if date == "2026-10-31" and len(rows) >= 5]
        check_rows(filtered, wanted)
        print("HAVING al menos 5 registros:", filtered)
    finally:
        memory.close()
    check_edge_cases()


if __name__ == "__main__":
    main()

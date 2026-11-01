"""Comparar observaciones y comprobar ventanas SQL en solo lectura."""

import argparse
from collections import defaultdict
import csv
import math
from pathlib import Path
import sqlite3

SOURCE = Path(__file__).resolve().parents[1] / "01_relational_sqlite"
DEFAULT_DATABASE = SOURCE / "output" / "cartera_demo.sqlite"

HISTORY = """
SELECT id_credito, fecha_corte, saldo_mxn,
       LAG(fecha_corte) OVER (PARTITION BY id_credito ORDER BY fecha_corte) AS fecha_anterior,
       LAG(saldo_mxn) OVER (PARTITION BY id_credito ORDER BY fecha_corte) AS saldo_anterior
FROM cortes
"""
COMPARISON = f"""
WITH historia AS ({HISTORY})
SELECT id_credito, fecha_corte, saldo_mxn, fecha_anterior, saldo_anterior,
       saldo_mxn - saldo_anterior AS cambio_mxn,
       100.0 * (saldo_mxn - saldo_anterior) / NULLIF(saldo_anterior, 0) AS cambio_pct,
       CASE
           WHEN fecha_anterior IS NULL THEN 'sin_anterior'
           WHEN saldo_mxn IS NULL AND saldo_anterior IS NULL THEN 'ambos_desconocidos'
           WHEN saldo_mxn IS NULL THEN 'actual_desconocido'
           WHEN saldo_anterior IS NULL THEN 'anterior_desconocido'
           ELSE 'comparable'
       END AS estado
FROM historia WHERE fecha_corte = :fecha
ORDER BY id_credito
"""
PAIRED_TOTALS = f"""
WITH historia AS ({HISTORY})
SELECT COUNT(*) AS pares_comparables,
       SUM(saldo_mxn) AS suma_actual_mxn,
       SUM(saldo_anterior) AS suma_anterior_mxn,
       SUM(saldo_mxn - saldo_anterior) AS suma_cambios_mxn
FROM historia
WHERE fecha_corte = :fecha AND saldo_mxn IS NOT NULL AND saldo_anterior IS NOT NULL
"""
LATEST = """
WITH ordenadas AS (
    SELECT id_credito, fecha_corte, saldo_mxn,
           ROW_NUMBER() OVER (PARTITION BY id_credito ORDER BY fecha_corte DESC) AS posicion
    FROM cortes
)
SELECT id_credito, fecha_corte, saldo_mxn
FROM ordenadas WHERE posicion = 1 ORDER BY id_credito
"""
TOP = """
WITH ordenadas AS (
    SELECT c.segmento, o.id_credito, o.saldo_mxn,
           ROW_NUMBER() OVER (
               PARTITION BY c.segmento ORDER BY o.saldo_mxn DESC, o.id_credito
           ) AS posicion
    FROM cortes AS o INNER JOIN creditos AS c ON c.id_credito = o.id_credito
    WHERE o.fecha_corte = :fecha AND o.saldo_mxn IS NOT NULL
)
SELECT segmento, id_credito, saldo_mxn, posicion
FROM ordenadas WHERE posicion <= :limite ORDER BY segmento, posicion
"""
TOTALS = """
SELECT id_credito, fecha_corte, saldo_mxn,
       COUNT(*) OVER (PARTITION BY fecha_corte) AS registros_corte,
       COUNT(saldo_mxn) OVER (PARTITION BY fecha_corte) AS saldos_conocidos,
       SUM(saldo_mxn) OVER (PARTITION BY fecha_corte) AS suma_conocida_mxn
FROM cortes ORDER BY fecha_corte, id_credito
"""
RUNNING = """
SELECT id_credito, saldo_mxn,
       SUM(saldo_mxn) OVER (
           ORDER BY id_credito ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS aporte_conocido_acumulado_mxn,
       COUNT(saldo_mxn) OVER (
           ORDER BY id_credito ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS conocidos_hasta_fila
FROM cortes WHERE fecha_corte = :fecha ORDER BY id_credito
"""


def sources():
    with (SOURCE / "data/creditos.csv").open(encoding="utf-8", newline="") as file:
        credits = [(r["id_credito"], r["id_cliente"], r["segmento"]) for r in csv.DictReader(file)]
    with (SOURCE / "data/cortes.csv").open(encoding="utf-8", newline="") as file:
        rows = [(r["id_credito"], r["fecha_corte"],
                 None if r["saldo_mxn"] == "" else int(r["saldo_mxn"]),
                 None if r["dias_atraso"] == "" else int(r["dias_atraso"])) for r in csv.DictReader(file)]
    return credits, rows


def check_rows(actual, expected):
    if len(actual) != len(expected):
        raise ValueError("Cantidad de filas distinta")
    for row, wanted in zip(actual, expected):
        if len(row) != len(wanted):
            raise ValueError("Cantidad de columnas distinta")
        for value, target in zip(row, wanted):
            if isinstance(target, float):
                if value is None or not math.isclose(value, target, rel_tol=1e-12, abs_tol=1e-12):
                    raise ValueError("Porcentaje distinto")
            elif value != target:
                raise ValueError(f"Resultado distinto: {value} frente a {target}")


def expected_comparison(rows, date):
    history = defaultdict(list)
    for row in rows:
        history[row[0]].append(row)
    result = []
    for identifier, records in sorted(history.items()):
        previous = None
        for row in sorted(records, key=lambda r: r[1]):
            balance = row[2]
            previous_date = previous[1] if previous else None
            previous_balance = previous[2] if previous else None
            change = balance - previous_balance if balance is not None and previous_balance is not None else None
            percent = 100.0 * change / previous_balance if change is not None and previous_balance != 0 else None
            if previous is None:
                state = "sin_anterior"
            elif balance is None and previous_balance is None:
                state = "ambos_desconocidos"
            elif balance is None:
                state = "actual_desconocido"
            elif previous_balance is None:
                state = "anterior_desconocido"
            else:
                state = "comparable"
            if row[1] == date:
                result.append((identifier, date, balance, previous_date, previous_balance, change, percent, state))
            previous = row
    return result


def verify(connection, credits, rows):
    for date in ("2026-09-30", "2026-10-31", "2099-01-31"):
        result = connection.execute(COMPARISON, {"fecha": date}).fetchall()
        check_rows(result, expected_comparison(rows, date))
        pairs = [r for r in result if r[7] == "comparable"]
        paired = (len(pairs), sum(r[2] for r in pairs) if pairs else None,
                  sum(r[4] for r in pairs) if pairs else None,
                  sum(r[5] for r in pairs) if pairs else None)
        check_rows(connection.execute(PAIRED_TOTALS, {"fecha": date}).fetchall(), [paired])
        print(f"{date}: {len(result)} observaciones comparadas; estados:",
              {state: sum(r[7] == state for r in result) for state in sorted({r[7] for r in result})})
        print("  Pares comparables (cantidad, actual, anterior, cambios):", paired)
        by_segment = defaultdict(list)
        segments = {r[0]: r[2] for r in credits}
        for row in rows:
            if row[1] == date and row[2] is not None:
                by_segment[segments[row[0]]].append(row)
        expected = []
        for segment, records in sorted(by_segment.items()):
            for position, row in enumerate(sorted(records, key=lambda r: (-r[2], r[0]))[:3], 1):
                expected.append((segment, row[0], row[2], position))
        top = connection.execute(TOP, {"fecha": date, "limite": 3}).fetchall()
        check_rows(top, expected)
        print("  Top 3 de saldos conocidos por segmento:", top)
        selected = sorted((r[0], r[2]) for r in rows if r[1] == date)
        running = []
        total, count = 0, 0
        for identifier, balance in selected:
            if balance is not None:
                total += balance
                count += 1
            running.append((identifier, balance, total if count else None, count))
        check_rows(connection.execute(RUNNING, {"fecha": date}).fetchall(), running)
    latest = {}
    for row in sorted(rows, key=lambda r: (r[0], r[1])):
        latest[row[0]] = row[:3]
    check_rows(connection.execute(LATEST).fetchall(), [latest[key] for key in sorted(latest)])
    totals = []
    dates = sorted({r[1] for r in rows})
    for date in dates:
        selected = sorted((r for r in rows if r[1] == date), key=lambda r: r[0])
        known = [r[2] for r in selected if r[2] is not None]
        for row in selected:
            totals.append(row[:3] + (len(selected), len(known), sum(known) if known else None))
    check_rows(connection.execute(TOTALS).fetchall(), totals)
    print("Últimas observaciones y totales de ventana comprobados; detalle conservado")


def demonstrate_frames():
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE movimientos (id TEXT PRIMARY KEY NOT NULL, fecha TEXT, importe_mxn INTEGER)")
        connection.executemany("INSERT INTO movimientos VALUES (?, ?, ?)",
                               [("M1", "2026-10-01", 10), ("M2", "2026-10-01", 20), ("M3", "2026-10-02", 5)])
        result = connection.execute("""SELECT id,
            SUM(importe_mxn) OVER (ORDER BY fecha) AS marco_predeterminado,
            SUM(importe_mxn) OVER (ORDER BY fecha, id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS fila_a_fila
            FROM movimientos ORDER BY fecha, id""").fetchall()
        check_rows(result, [("M1", 30, 10), ("M2", 30, 30), ("M3", 35, 35)])
        print("Empates y marcos en memoria:", result)
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args()
    if sqlite3.sqlite_version_info < (3, 25, 0):
        raise RuntimeError("Esta lección requiere SQLite 3.25.0 o posterior con funciones de ventana")
    if not args.database.is_file():
        raise FileNotFoundError("Falta la base de 03.01; prepárala o revisa --database")
    credits, rows = sources()
    connection = sqlite3.connect(args.database.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        connection.execute("BEGIN")
        check_rows(sorted(connection.execute("SELECT id_credito, id_cliente, segmento FROM creditos").fetchall()), sorted(credits))
        check_rows(sorted(connection.execute("SELECT id_credito, fecha_corte, saldo_mxn, dias_atraso FROM cortes").fetchall()), sorted(rows))
        verify(connection, credits, rows)
        cursor = connection.execute(COMPARISON, {"fecha": "2026-10-31"})
        labels = [r[0] for r in cursor.description]
        print("Comparaciones seleccionadas de octubre:")
        for row in cursor.fetchall():
            if row[0] in {"001", "004", "005", "009", "022", "024"}:
                print(dict(zip(labels, row)))
    finally:
        connection.close()
    demonstrate_frames()


if __name__ == "__main__":
    main()

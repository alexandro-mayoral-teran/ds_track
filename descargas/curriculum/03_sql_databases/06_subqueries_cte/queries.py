"""Consultar por pasos y comprobar subconsultas/CTE sin modificar la base."""

import argparse
from collections import defaultdict
import csv
import math
from pathlib import Path
import sqlite3

SOURCE = Path(__file__).resolve().parents[1] / "01_relational_sqlite"
DEFAULT_DATABASE = SOURCE / "output" / "cartera_demo.sqlite"

ABOVE_AVERAGE = """
SELECT o.id_credito, o.saldo_mxn
FROM cortes AS o
WHERE o.fecha_corte = :fecha
  AND o.saldo_mxn > (
      SELECT AVG(r.saldo_mxn) FROM cortes AS r WHERE r.fecha_corte = :fecha
  )
ORDER BY o.id_credito
"""
ABOVE_AVERAGE_CTE = """
WITH corte AS (
    SELECT id_credito, saldo_mxn FROM cortes WHERE fecha_corte = :fecha
), referencia AS (
    SELECT AVG(saldo_mxn) AS promedio_conocido FROM corte
)
SELECT o.id_credito, o.saldo_mxn
FROM corte AS o CROSS JOIN referencia AS r
WHERE o.saldo_mxn > r.promedio_conocido
ORDER BY o.id_credito
"""
CLIENTS_EXISTS = """
SELECT p.id_cliente FROM clientes AS p
WHERE EXISTS (
    SELECT 1 FROM creditos AS c
    INNER JOIN cortes AS o ON o.id_credito = c.id_credito
    WHERE c.id_cliente = p.id_cliente
      AND o.fecha_corte = :fecha AND o.dias_atraso >= :umbral
)
ORDER BY p.id_cliente
"""
CLIENTS_IN = """
SELECT p.id_cliente FROM clientes AS p
WHERE p.id_cliente IN (
    SELECT c.id_cliente FROM creditos AS c
    INNER JOIN cortes AS o ON o.id_credito = c.id_credito
    WHERE o.fecha_corte = :fecha AND o.dias_atraso >= :umbral
)
ORDER BY p.id_cliente
"""
CLIENTS_JOIN = """
SELECT DISTINCT p.id_cliente FROM clientes AS p
INNER JOIN creditos AS c ON c.id_cliente = p.id_cliente
INNER JOIN cortes AS o ON o.id_credito = c.id_credito
WHERE o.fecha_corte = :fecha AND o.dias_atraso >= :umbral
ORDER BY p.id_cliente
"""
CLIENTS_NOT_EXISTS = CLIENTS_EXISTS.replace("WHERE EXISTS (", "WHERE NOT EXISTS (")

CUT = "SELECT id_credito, saldo_mxn, dias_atraso FROM cortes WHERE fecha_corte = :fecha"
LABELLED = """
SELECT o.id_credito, o.saldo_mxn, o.dias_atraso, c.segmento
FROM cortes AS o INNER JOIN creditos AS c ON c.id_credito = o.id_credito
WHERE o.fecha_corte = :fecha
"""
SUMMARY = """
SELECT c.segmento,
       COUNT(*) AS registros,
       COUNT(o.saldo_mxn) AS saldos_conocidos,
       SUM(o.saldo_mxn) AS suma_conocida_mxn,
       COUNT(o.dias_atraso) AS atrasos_conocidos,
       COUNT(CASE WHEN o.dias_atraso >= :umbral THEN 1 END) AS confirmados
FROM cortes AS o INNER JOIN creditos AS c ON c.id_credito = o.id_credito
WHERE o.fecha_corte = :fecha
GROUP BY c.segmento
"""
REPORT_DERIVED = f"""
SELECT segmento, registros, saldos_conocidos, suma_conocida_mxn,
       atrasos_conocidos, confirmados,
       100.0 * confirmados / NULLIF(atrasos_conocidos, 0) AS tasa_conocidos_pct,
       100.0 * atrasos_conocidos / NULLIF(registros, 0) AS cobertura_atraso_pct
FROM ({SUMMARY}) AS resumen
ORDER BY segmento
"""
REPORT_CTE = """
WITH corte AS (
    SELECT id_credito, saldo_mxn, dias_atraso
    FROM cortes WHERE fecha_corte = :fecha
), detalle AS (
    SELECT o.id_credito, o.saldo_mxn, o.dias_atraso, c.segmento
    FROM corte AS o INNER JOIN creditos AS c ON c.id_credito = o.id_credito
), resumen AS (
    SELECT segmento, COUNT(*) AS registros,
           COUNT(saldo_mxn) AS saldos_conocidos,
           SUM(saldo_mxn) AS suma_conocida_mxn,
           COUNT(dias_atraso) AS atrasos_conocidos,
           COUNT(CASE WHEN dias_atraso >= :umbral THEN 1 END) AS confirmados
    FROM detalle GROUP BY segmento
)
SELECT segmento, registros, saldos_conocidos, suma_conocida_mxn,
       atrasos_conocidos, confirmados,
       100.0 * confirmados / NULLIF(atrasos_conocidos, 0) AS tasa_conocidos_pct,
       100.0 * atrasos_conocidos / NULLIF(registros, 0) AS cobertura_atraso_pct
FROM resumen ORDER BY segmento
"""


def read_csv(name):
    with (SOURCE / "data" / f"{name}.csv").open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def source_rows():
    credits = [(r["id_credito"], r["id_cliente"], r["segmento"]) for r in read_csv("creditos")]
    clients = [(r["id_cliente"], r["alias"], r["region"]) for r in read_csv("clientes")]
    observations = [(r["id_credito"], r["fecha_corte"],
                     None if r["saldo_mxn"] == "" else int(r["saldo_mxn"]),
                     None if r["dias_atraso"] == "" else int(r["dias_atraso"]))
                    for r in read_csv("cortes")]
    return clients, credits, observations


def check_rows(actual, expected):
    if len(actual) != len(expected):
        raise ValueError("No coincide la cantidad de filas")
    for row, wanted in zip(actual, expected):
        if len(row) != len(wanted):
            raise ValueError("No coincide la cantidad de columnas")
        for value, target in zip(row, wanted):
            if isinstance(target, float):
                if value is None or not math.isclose(value, target, rel_tol=1e-12, abs_tol=1e-12):
                    raise ValueError("No coincide el indicador real")
            elif value != target:
                raise ValueError(f"Valor distinto: {value} frente a {target}")


def expected_report(rows, credits, threshold):
    segments = {r[0]: r[2] for r in credits}
    groups = defaultdict(list)
    for row in rows:
        groups[segments[row[0]]].append(row)
    result = []
    for segment, records in sorted(groups.items()):
        balances = [r[2] for r in records if r[2] is not None]
        delays = [r[3] for r in records if r[3] is not None]
        late = sum(value >= threshold for value in delays)
        result.append((segment, len(records), len(balances), sum(balances) if balances else None,
                       len(delays), late, 100.0 * late / len(delays) if delays else None,
                       100.0 * len(delays) / len(records)))
    return result


def verify_date(connection, date, threshold, sources):
    clients, credits, observations = sources
    rows = [r for r in observations if r[1] == date]
    parameters = {"fecha": date, "umbral": threshold}
    known = [r[2] for r in rows if r[2] is not None]
    average = sum(known) / len(known) if known else None
    wanted_above = sorted((r[0], r[2]) for r in rows
                          if average is not None and r[2] is not None and r[2] > average)
    for sql in (ABOVE_AVERAGE, ABOVE_AVERAGE_CTE):
        check_rows(connection.execute(sql, parameters).fetchall(), wanted_above)
    owners = {r[0]: r[1] for r in credits}
    wanted_clients = sorted({owners[r[0]] for r in rows if r[3] is not None and r[3] >= threshold})
    expected = [(client,) for client in wanted_clients]
    for sql in (CLIENTS_EXISTS, CLIENTS_IN, CLIENTS_JOIN):
        check_rows(connection.execute(sql, parameters).fetchall(), expected)
    complement = [(r[0],) for r in sorted(clients) if r[0] not in wanted_clients]
    check_rows(connection.execute(CLIENTS_NOT_EXISTS, parameters).fetchall(), complement)
    cut = connection.execute(CUT, parameters).fetchall()
    labelled = connection.execute(LABELLED, parameters).fetchall()
    check_rows(sorted(cut), sorted(labelled_row[:3] for labelled_row in labelled))
    check_rows(sorted(cut), sorted((r[0], r[2], r[3]) for r in rows))
    expected = expected_report(rows, credits, threshold)
    for sql in (REPORT_DERIVED, REPORT_CTE):
        check_rows(connection.execute(sql, parameters).fetchall(), expected)
    print(f"{date}, umbral {threshold}: corte {len(cut)} -> detalle {len(labelled)} -> resumen {len(expected)}")
    print("  Sobre promedio conocido:", wanted_above)
    print("  Clientes con atraso confirmado:", wanted_clients)
    cursor = connection.execute(REPORT_CTE, parameters)
    labels = [r[0] for r in cursor.description]
    for row in cursor.fetchall():
        print(" ", dict(zip(labels, row)))


def demonstrate_nulls():
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE candidatos (id TEXT PRIMARY KEY NOT NULL)")
        connection.execute("CREATE TABLE seleccion (id TEXT)")
        connection.executemany("INSERT INTO candidatos VALUES (?)", [("A",), ("B",), ("C",)])
        connection.executemany("INSERT INTO seleccion VALUES (?)", [("A",), (None,)])
        not_in = connection.execute("SELECT id FROM candidatos WHERE id NOT IN (SELECT id FROM seleccion) ORDER BY id").fetchall()
        not_exists = connection.execute("SELECT c.id FROM candidatos AS c WHERE NOT EXISTS (SELECT 1 FROM seleccion AS s WHERE s.id = c.id) ORDER BY c.id").fetchall()
        check_rows(not_in, [])
        check_rows(not_exists, [("B",), ("C",)])
        check_rows(connection.execute("SELECT EXISTS(SELECT id FROM seleccion WHERE id IS NULL)").fetchall(), [(1,)])
        check_rows(connection.execute("SELECT (SELECT id FROM seleccion WHERE id = 'Z')").fetchall(), [(None,)])
        print("Caso NULL en memoria: NOT IN", not_in, "; NOT EXISTS", not_exists)
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args()
    if not args.database.is_file():
        raise FileNotFoundError("Falta la base de 03.01; prepárala o revisa --database")
    sources = source_rows()
    connection = sqlite3.connect(args.database.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        connection.execute("BEGIN")
        for table, columns, expected in (
            ("clientes", "id_cliente, alias, region", sources[0]),
            ("creditos", "id_credito, id_cliente, segmento", sources[1]),
            ("cortes", "id_credito, fecha_corte, saldo_mxn, dias_atraso", sources[2]),
        ):
            # Nombres internos fijos; los valores de filtros siempre son parámetros.
            check_rows(sorted(connection.execute(f"SELECT {columns} FROM {table}").fetchall()), sorted(expected))
        for date, threshold in (("2026-10-31", 30), ("2026-09-30", 30),
                                ("2099-01-31", 30), ("2026-10-31", 100)):
            verify_date(connection, date, threshold, sources)
    finally:
        connection.close()
    demonstrate_nulls()


if __name__ == "__main__":
    main()

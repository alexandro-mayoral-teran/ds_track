"""Relacionar la base de 03.01 en solo lectura y comprobar la cardinalidad."""

import argparse
import csv
from pathlib import Path
import sqlite3

SOURCE = Path(__file__).resolve().parents[1] / "01_relational_sqlite"
DEFAULT_DATABASE = SOURCE / "output" / "cartera_demo.sqlite"

DETAIL = """
SELECT o.id_credito, o.fecha_corte, o.saldo_mxn,
       c.id_cliente, c.segmento, p.region
FROM cortes AS o
INNER JOIN creditos AS c ON c.id_credito = o.id_credito
INNER JOIN clientes AS p ON p.id_cliente = c.id_cliente
WHERE o.fecha_corte = ?
ORDER BY o.id_credito
"""
CLIENTS = """
SELECT p.id_cliente, c.id_credito
FROM clientes AS p
LEFT JOIN creditos AS c ON c.id_cliente = p.id_cliente
ORDER BY p.id_cliente, c.id_credito
"""
UNMATCHED = """
SELECT p.id_cliente
FROM clientes AS p
LEFT JOIN creditos AS c ON c.id_cliente = p.id_cliente
WHERE c.id_credito IS NULL
ORDER BY p.id_cliente
"""
OCTOBER_ON = """
SELECT c.id_credito, o.id_credito AS id_observado, o.saldo_mxn
FROM creditos AS c
LEFT JOIN cortes AS o
  ON o.id_credito = c.id_credito AND o.fecha_corte = ?
ORDER BY c.id_credito
"""
OCTOBER_WHERE = """
SELECT c.id_credito, o.id_credito AS id_observado, o.saldo_mxn
FROM creditos AS c
LEFT JOIN cortes AS o ON o.id_credito = c.id_credito
WHERE o.fecha_corte = ?
ORDER BY c.id_credito
"""
BAD_PAIR = """
SELECT a.id_credito, a.fecha_corte, a.saldo_mxn, b.fecha_corte
FROM cortes AS a
INNER JOIN cortes AS b ON b.id_credito = a.id_credito
WHERE a.fecha_corte = ?
ORDER BY a.id_credito, b.fecha_corte
"""
GOOD_PAIR = BAD_PAIR.replace(
    "ON b.id_credito = a.id_credito",
    "ON b.id_credito = a.id_credito AND b.fecha_corte = a.fecha_corte",
)


def open_readonly(path):
    if not path.is_file():
        raise FileNotFoundError("Falta la base de 03.01; prepárala o revisa --database")
    return sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)


def read_csv(name):
    with (SOURCE / "data" / f"{name}.csv").open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def expected_detail(date):
    # Referencia independiente: relacionar los CSV por claves en Python.
    clients = {row["id_cliente"]: row for row in read_csv("clientes")}
    credits = {row["id_credito"]: row for row in read_csv("creditos")}
    rows = []
    for observation in read_csv("cortes"):
        if observation["fecha_corte"] == date:
            credit = credits[observation["id_credito"]]
            client = clients[credit["id_cliente"]]
            balance = observation["saldo_mxn"]
            rows.append((observation["id_credito"], date,
                         None if balance == "" else int(balance),
                         credit["id_cliente"], credit["segmento"], client["region"]))
    return sorted(rows)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def reconcile(connection, date):
    original = connection.execute(
        "SELECT id_credito, fecha_corte, saldo_mxn FROM cortes WHERE fecha_corte = ? ORDER BY id_credito",
        (date,),
    ).fetchall()
    joined = connection.execute(DETAIL, (date,)).fetchall()
    check(joined == expected_detail(date), "La base no coincide con la muestra original")
    check([row[:3] for row in joined] == original, "Se perdieron o multiplicaron observaciones")
    keys = [(row[0], row[1]) for row in joined]
    check(len(keys) == len(set(keys)), "La clave crédito/fecha se repite")
    known = [row[2] for row in original if row[2] is not None]
    # Sobre una lista vacía, sum de Python da 0; informamos None como SUM de SQL.
    total = sum(known) if known else None
    print(f"{date}: {len(joined)} observaciones; {len(known)} saldos conocidos; suma conocida: {total}")
    return joined


def demonstrate_missing():
    """Caso mínimo propio: distinguir falta de observación de saldo desconocido."""
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE creditos (id_credito TEXT PRIMARY KEY NOT NULL)")
        connection.execute("CREATE TABLE cortes (id_credito TEXT NOT NULL, fecha_corte TEXT NOT NULL, saldo_mxn INTEGER, PRIMARY KEY (id_credito, fecha_corte))")
        connection.executemany("INSERT INTO creditos VALUES (?)", [("A",), ("B",), ("C",)])
        connection.executemany("INSERT INTO cortes VALUES (?, ?, ?)",
                               [("A", "2026-10-31", 0), ("B", "2026-10-31", None),
                                ("C", "2026-09-30", 100)])
        on_rows = connection.execute(OCTOBER_ON, ("2026-10-31",)).fetchall()
        where_rows = connection.execute(OCTOBER_WHERE, ("2026-10-31",)).fetchall()
        check(on_rows == [("A", "A", 0), ("B", "B", None), ("C", None, None)], "LEFT JOIN inesperado")
        check(where_rows == on_rows[:2], "WHERE no produjo el resultado esperado")
        print("Caso en memoria; filtro en ON:", on_rows)
        print("Caso en memoria; filtro en WHERE:", where_rows)
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args()
    connection = open_readonly(args.database)
    try:
        connection.execute("BEGIN")  # Todas las comprobaciones leen la misma instantánea.
        for date in ("2026-09-30", "2026-10-31", "2099-01-31"):
            reconcile(connection, date)
        clients = connection.execute(CLIENTS).fetchall()
        source_clients = read_csv("clientes")
        source_credits = read_csv("creditos")
        expected = sorted(
            (client["id_cliente"], credit["id_credito"])
            for client in source_clients
            for credit in source_credits
            if credit["id_cliente"] == client["id_cliente"]
        )
        expected += [(client["id_cliente"], None) for client in source_clients
                     if not any(credit["id_cliente"] == client["id_cliente"] for credit in source_credits)]
        expected.sort(key=lambda row: (row[0], row[1] or ""))
        check(clients == expected, "Clientes/créditos distintos de la fuente")
        missing = connection.execute(UNMATCHED).fetchall()
        check(missing == [(row[0],) for row in clients if row[1] is None], "Sin correspondencia inesperado")
        print(f"LEFT clientes/créditos: {len(clients)} filas; sin crédito: {missing}")
        bad = connection.execute(BAD_PAIR, ("2026-10-31",)).fetchall()
        good = connection.execute(GOOD_PAIR, ("2026-10-31",)).fetchall()
        expected_observations = connection.execute(
            "SELECT id_credito, fecha_corte, saldo_mxn FROM cortes WHERE fecha_corte = ? ORDER BY id_credito",
            ("2026-10-31",),
        ).fetchall()
        check([row[:3] for row in good] == expected_observations,
              "La clave completa no conservó las observaciones")
        original = connection.execute("SELECT saldo_mxn FROM cortes WHERE fecha_corte = ?", ("2026-10-31",)).fetchall()
        check(len(bad) == 2 * len(original), "El ejemplo requiere dos cortes por crédito")
        check(sum(row[2] for row in bad if row[2] is not None) == 2 * sum(row[0] for row in original if row[0] is not None), "Multiplicación inesperada")
        print(f"Unión incompleta: {len(bad)} filas; suma conocida duplicada")
        print(f"Unión con clave completa: {len(good)} filas; observaciones conservadas")
    finally:
        connection.close()
    demonstrate_missing()


if __name__ == "__main__":
    main()

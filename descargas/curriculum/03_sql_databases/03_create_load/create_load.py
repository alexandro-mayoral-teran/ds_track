"""Crear y comprobar una base de práctica; conservar archivos existentes."""

import argparse
import csv
from datetime import date
from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "01_relational_sqlite" / "data"
COLUMNS = {
    "clientes": ("id_cliente", "alias", "region"),
    "creditos": ("id_credito", "id_cliente", "segmento"),
    "cortes": ("id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"),
}


def read_sources():
    sources = {}
    for table, columns in COLUMNS.items():
        with (DATA / f"{table}.csv").open(encoding="utf-8", newline="") as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != list(columns):
                raise ValueError(f"Columnas inesperadas: {table}")
            rows = []
            for row in reader:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"Fila incompleta o con campos extra: {table}")
                if table == "cortes":
                    value = row["fecha_corte"]
                    if date.fromisoformat(value).isoformat() != value:
                        raise ValueError("Fecha fuera del formato YYYY-MM-DD")
                    for column in ("saldo_mxn", "dias_atraso"):
                        row[column] = None if row[column] == "" else int(row[column])
                rows.append(tuple(row[column] for column in columns))
            sources[table] = rows
    return sources


def enable_foreign_keys(connection):
    connection.execute("PRAGMA foreign_keys = ON")
    if connection.execute("PRAGMA foreign_keys").fetchone() != (1,):
        raise RuntimeError("No se habilitaron las claves foráneas")


def create_schema(connection):
    # complete_statement reconoce terminadores sin confundir comentarios.
    # execute conserva el BEGIN explícito; no usamos executescript aquí.
    statement = ""
    for line in (HERE / "schema.sql").read_text(encoding="utf-8").splitlines(True):
        statement += line
        if sqlite3.complete_statement(statement):
            connection.execute(statement)
            statement = ""
    if statement.strip():
        raise ValueError("Sentencia incompleta en schema.sql")


def load_rows(connection, sources):
    for table, columns in COLUMNS.items():
        markers = ", ".join("?" for _ in columns)
        # Los nombres provienen del programa; los valores siempre son parámetros.
        sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({markers})"
        connection.executemany(sql, sources[table])


def verify(connection, sources):
    for table, columns in COLUMNS.items():
        rows = connection.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall()
        # Ordenar por claves evita comparar None con enteros.
        key = (lambda row: row[:2]) if table == "cortes" else (lambda row: row[:1])
        if sorted(rows, key=key) != sorted(sources[table], key=key):
            raise ValueError(f"Contenido distinto de la fuente: {table}; usa otra ruta")
    if connection.execute("PRAGMA foreign_key_check").fetchall():
        raise ValueError("Relaciones inválidas")
    if connection.execute("PRAGMA integrity_check").fetchone() != ("ok",):
        raise ValueError("Integridad inválida")
    reference = sqlite3.connect(":memory:")
    try:
        create_schema(reference)
        query = "SELECT name, sql FROM sqlite_master WHERE type = 'table' ORDER BY name"
        if connection.execute(query).fetchall() != reference.execute(query).fetchall():
            raise ValueError("Esquema distinto del esperado; usa otra ruta")
    finally:
        reference.close()


def check_rejections(sources):
    """Los intentos inválidos ocurren en memoria, nunca en la base guardada."""
    connection = sqlite3.connect(":memory:", isolation_level=None)
    cases = (
        ("clave repetida", "INSERT INTO clientes VALUES (?, ?, ?)", sources["clientes"][0]),
        ("campo obligatorio", "INSERT INTO clientes VALUES (?, ?, ?)", ("nuevo", None, "Norte")),
        ("relación inexistente", "INSERT INTO creditos VALUES (?, ?, ?)", ("nuevo", "inexistente", "A")),
        ("saldo negativo", "INSERT INTO cortes VALUES (?, ?, ?, ?)", ("001", "2026-11-30", -1, 0)),
        ("saldo no entero", "INSERT INTO cortes VALUES (?, ?, ?, ?)", ("001", "2026-11-30", 1.5, 0)),
        ("clave compuesta repetida", "INSERT INTO cortes VALUES (?, ?, ?, ?)", sources["cortes"][0]),
    )
    try:
        enable_foreign_keys(connection)
        create_schema(connection)
        load_rows(connection, sources)
        for name, sql, values in cases:
            try:
                connection.execute(sql, values)
            except sqlite3.IntegrityError:
                print(f"Rechazo comprobado: {name}")
            else:
                raise AssertionError(f"Se aceptó un caso inválido: {name}")
        verify(connection, sources)
    finally:
        connection.close()


def prepare(path, sources):
    path = path.resolve()
    if path.exists():
        connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
        try:
            verify(connection, sources)
        finally:
            connection.close()
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    # x reserva una ruta nueva y falla si otro proceso ya creó el archivo.
    with path.open("xb"):
        pass
    connection = sqlite3.connect(path, isolation_level=None)
    try:
        enable_foreign_keys(connection)
        connection.execute("BEGIN")
        create_schema(connection)
        load_rows(connection, sources)
        verify(connection, sources)
        connection.execute("COMMIT")
    except Exception:
        if connection.in_transaction:
            connection.execute("ROLLBACK")
        raise
    finally:
        connection.close()
    # Reconectar en solo lectura comprueba persistencia, sin recargar.
    connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    try:
        verify(connection, sources)
    finally:
        connection.close()
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=HERE / "output" / "carga_practica.sqlite")
    args = parser.parse_args()
    sources = read_sources()
    check_rejections(sources)
    created = prepare(args.database, sources)
    print("Base creada y persistencia comprobada" if created else "Base existente comprobada; sin cambios")
    for table, rows in sources.items():
        print(f"{table}: {len(rows)} filas conciliadas")


if __name__ == "__main__":
    main()

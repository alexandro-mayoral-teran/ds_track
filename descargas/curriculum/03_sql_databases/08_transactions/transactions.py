"""Practicar escrituras sobre una copia nueva; conservar fuente y copias existentes."""

import argparse
import csv
from datetime import date
from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "01_relational_sqlite"
DEFAULT_SOURCE = SOURCE / "output/cartera_demo.sqlite"
DEFAULT_PRACTICE = HERE / "output/transacciones_practica.sqlite"
COLUMNS = {
    "clientes": ("id_cliente", "alias", "region"),
    "creditos": ("id_credito", "id_cliente", "segmento"),
    "cortes": ("id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"),
}
BATCH = [("001", "2026-11-30", 1400, 0), ("002", "2026-11-30", 1500, 0)]
SELECT_CUT = "SELECT id_credito, fecha_corte, saldo_mxn, dias_atraso FROM cortes WHERE id_credito = ? AND fecha_corte = ?"


def connect(path, readonly=False):
    # Fijar el modo legado explícitamente en Python >= 3.12; compatible con 3.11.
    options = {"isolation_level": None}
    if hasattr(sqlite3, "LEGACY_TRANSACTION_CONTROL"):
        options["autocommit"] = sqlite3.LEGACY_TRANSACTION_CONTROL
    mode = "ro" if readonly else "rw"
    connection = sqlite3.connect(path.resolve().as_uri() + f"?mode={mode}", uri=True, **options)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        if connection.execute("PRAGMA foreign_keys").fetchone() != (1,):
            raise RuntimeError("No se habilitaron claves foráneas")
    except Exception:
        connection.close()
        raise
    return connection


def source_rows():
    result = {}
    for table, columns in COLUMNS.items():
        with (SOURCE / "data" / f"{table}.csv").open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != list(columns):
                raise ValueError("Encabezados inesperados")
            rows = []
            for row in reader:
                if table == "cortes":
                    for column in ("saldo_mxn", "dias_atraso"):
                        row[column] = None if row[column] == "" else int(row[column])
                rows.append(tuple(row[column] for column in columns))
            result[table] = sorted(rows)
    return result


def snapshot(connection):
    return {table: sorted(connection.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall())
            for table, columns in COLUMNS.items()}


def verify(connection, expected):
    if snapshot(connection) != expected:
        raise ValueError("La base difiere del estado esperado; se conserva sin cambios")
    if connection.execute("PRAGMA foreign_key_check").fetchall():
        raise ValueError("Hay relaciones inválidas")
    if connection.execute("PRAGMA integrity_check").fetchone() != ("ok",):
        raise ValueError("Integridad inválida")
    reference = sqlite3.connect(":memory:")
    try:
        reference.executescript((SOURCE / "schema.sql").read_text(encoding="utf-8"))
        sql = "SELECT name, sql FROM sqlite_master WHERE type = 'table' ORDER BY name"
        if connection.execute(sql).fetchall() != reference.execute(sql).fetchall():
            raise ValueError("Esquema distinto del contrato de práctica")
    finally:
        reference.close()


def verify_file(path, expected):
    connection = connect(path, readonly=True)
    try:
        connection.execute("BEGIN")
        verify(connection, expected)
    finally:
        connection.close()


def final_rows(original):
    expected = {table: list(rows) for table, rows in original.items()}
    expected["cortes"] = [
        (r[0], r[1], 1350, r[3]) if r[:2] == ("001", "2026-10-31") else r
        for r in expected["cortes"]
    ]
    expected["cortes"].append(BATCH[0])
    expected["cortes"].sort()
    return expected


def copy_new(source, target, original):
    if source.resolve() == target.resolve() or (target.exists() and source.samefile(target)):
        raise ValueError("La práctica debe usar un archivo distinto de la fuente")
    verify_file(source, original)
    if target.exists():
        # Nunca continuar escribiendo ni reiniciar una práctica existente.
        verify_file(target, final_rows(original))
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb"):
        pass
    source_connection = connect(source, readonly=True)
    try:
        target_connection = connect(target)
        try:
            source_connection.backup(target_connection)
            verify(target_connection, original)
        finally:
            target_connection.close()
    finally:
        source_connection.close()
    return True


def validate_batch(rows):
    for identifier, cut, balance, delay in rows:
        if not isinstance(identifier, str) or not identifier:
            raise ValueError("ID de crédito obligatorio")
        if not isinstance(cut, str) or date.fromisoformat(cut).isoformat() != cut:
            raise ValueError("Fecha requiere YYYY-MM-DD")
        for value in (balance, delay):
            if value is not None and (type(value) is not int or value < 0):
                raise ValueError("Importes y atrasos requieren enteros no negativos o None")


def load_batch(connection, rows):
    """Repetición exacta se acepta; una misma clave con otros valores es conflicto."""
    if connection.in_transaction:
        raise ValueError("Termina la transacción actual antes de iniciar esta carga")
    rows = list(rows)
    validate_batch(rows)
    inserted = 0
    connection.execute("BEGIN IMMEDIATE")
    try:
        for row in rows:
            existing = connection.execute(SELECT_CUT, row[:2]).fetchone()
            if existing is None:
                connection.execute("INSERT INTO cortes VALUES (?, ?, ?, ?)", row)
                inserted += 1
            elif existing != tuple(row):
                raise ValueError(f"Conflicto en la clave {row[:2]}; no se sobrescribe")
        connection.commit()
    except Exception:
        if connection.in_transaction:
            connection.rollback()
        raise
    return inserted


def demonstrate(path, original):
    connection = connect(path)
    key = ("001", "2026-10-31")
    try:
        # Ensayo reversible: mismo WHERE completo para SELECT y UPDATE.
        connection.execute("BEGIN IMMEDIATE")
        try:
            before = connection.execute(SELECT_CUT, key).fetchone()
            if before != ("001", "2026-10-31", 1300, 10):
                raise ValueError("Fila inicial inesperada")
            cursor = connection.execute("UPDATE cortes SET saldo_mxn = ? WHERE id_credito = ? AND fecha_corte = ?", (999,) + key)
            if cursor.rowcount != 1:
                raise ValueError("UPDATE no afectó exactamente una fila")
            observer = connect(path, readonly=True)
            try:
                if observer.execute(SELECT_CUT, key).fetchone() != before:
                    raise ValueError("La otra conexión vio un cambio no confirmado")
            finally:
                observer.close()
            connection.rollback()
        except Exception:
            if connection.in_transaction:
                connection.rollback()
            raise
        verify(connection, original)
        print("UPDATE ensayado y revertido; otra conexión conservó el valor confirmado")

        # Un fallo de la segunda sentencia requiere revertir también la primera.
        connection.execute("BEGIN IMMEDIATE")
        try:
            connection.execute("UPDATE cortes SET saldo_mxn = ? WHERE id_credito = ? AND fecha_corte = ?", (1350,) + key)
            connection.execute("INSERT INTO creditos VALUES (?, ?, ?)", ("prueba", "cliente_inexistente", "consumo"))
        except sqlite3.IntegrityError:
            connection.rollback()
        except Exception:
            if connection.in_transaction:
                connection.rollback()
            raise
        else:
            connection.rollback()
            raise AssertionError("Debió rechazarse la relación inexistente")
        verify(connection, original)
        print("Lote fallido: primera escritura también revertida")

        connection.execute("BEGIN IMMEDIATE")
        try:
            before = connection.execute(SELECT_CUT, key).fetchone()
            if before != ("001", "2026-10-31", 1300, 10):
                raise ValueError("Fila previa inesperada")
            cursor = connection.execute("UPDATE cortes SET saldo_mxn = ? WHERE id_credito = ? AND fecha_corte = ? AND saldo_mxn = ?", (1350,) + key + (1300,))
            if cursor.rowcount != 1:
                raise ValueError("Corrección no aplicada a la fila esperada")
            if connection.execute(SELECT_CUT, key).fetchone() != ("001", "2026-10-31", 1350, 10):
                raise ValueError("Valor posterior inesperado")
            connection.commit()
        except Exception:
            if connection.in_transaction:
                connection.rollback()
            raise
        corrected = {table: list(rows) for table, rows in original.items()}
        corrected["cortes"] = [(r[0], r[1], 1350, r[3]) if r[:2] == key else r for r in corrected["cortes"]]
        verify_file(path, corrected)
        print("Corrección absoluta 1300 -> 1350 confirmada y comprobada al reconectar")

        if load_batch(connection, BATCH) != 2 or load_batch(connection, BATCH) != 0:
            raise AssertionError("La carga no conservó su regla de repetición")
        loaded = {table: list(rows) for table, rows in corrected.items()}
        loaded["cortes"] = sorted(loaded["cortes"] + BATCH)
        verify_file(path, loaded)
        if load_batch(connection, []) != 0:
            raise AssertionError("Lote vacío inesperado")
        print("Carga confirmada: 2 filas nuevas; repetición y lote vacío: 0")

        # Rechazar un conflicto después de una fila válida: debe revertir todo.
        try:
            load_batch(connection, [("003", "2026-11-30", 1600, 0), ("001", "2026-11-30", 999, 0)])
        except ValueError:
            pass
        else:
            raise AssertionError("Debió rechazarse el conflicto de carga")
        verify(connection, loaded)
        print("Conflicto de carga rechazado; ninguna fila parcial persistió")

        delete_key = BATCH[1][:2]
        for confirm in (False, True):
            connection.execute("BEGIN IMMEDIATE")
            try:
                before = connection.execute(SELECT_CUT, delete_key).fetchone()
                if before != BATCH[1]:
                    raise ValueError("La fila a borrar no coincide con el ensayo")
                cursor = connection.execute("DELETE FROM cortes WHERE id_credito = ? AND fecha_corte = ?", delete_key)
                if cursor.rowcount != 1 or connection.execute(SELECT_CUT, delete_key).fetchone() is not None:
                    raise ValueError("DELETE no afectó la fila esperada")
                if confirm:
                    connection.commit()
                else:
                    connection.rollback()
            except Exception:
                if connection.in_transaction:
                    connection.rollback()
                raise
            verify_file(path, final_rows(original) if confirm else loaded)
            print("DELETE confirmado y persistencia comprobada" if confirm else "DELETE ensayado y revertido")
    finally:
        if connection.in_transaction:
            connection.rollback()
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--practice", type=Path, default=DEFAULT_PRACTICE)
    args = parser.parse_args()
    if not args.source.is_file():
        raise FileNotFoundError("Falta la base fuente de 03.01; prepárala primero")
    original = source_rows()
    created = copy_new(args.source, args.practice, original)
    if created:
        demonstrate(args.practice, original)
    else:
        print("Práctica existente comprobada en lectura; no se repiten escrituras")
    verify_file(args.practice, final_rows(original))
    verify_file(args.source, original)
    print("Estado final: 16 clientes, 24 créditos, 49 cortes; fuente intacta")
    print("La copia queda conservada para revisión; una nueva sesión usa otra ruta")


if __name__ == "__main__":
    main()

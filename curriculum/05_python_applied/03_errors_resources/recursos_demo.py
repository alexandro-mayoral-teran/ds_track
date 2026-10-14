"""Cerrar un archivo y una conexión en memoria después de una falla controlada."""

import argparse
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para la demostración")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    # El gestor solo retira el temporal que él mismo creó dentro de esa carpeta.
    with tempfile.TemporaryDirectory(dir=args.output, prefix="recursos-") as temporary:
        path = Path(temporary) / "numero.txt"
        path.write_text("no es un número", encoding="utf-8")
        try:
            with path.open(encoding="utf-8") as handle:
                int(handle.read())
        except ValueError as exc:
            print(f"Conversión detenida: {exc}")
        print(f"Archivo cerrado: {handle.closed}")
        try:
            with closing(sqlite3.connect(":memory:")) as connection:
                with connection:
                    connection.execute("CREATE TABLE demo (valor INTEGER)")
                    connection.execute("INSERT INTO demo VALUES (1)")
                    raise ValueError("Falla didáctica dentro de la transacción")
        except ValueError as exc:
            print(f"Transacción detenida: {exc}")
        try:
            connection.execute("SELECT 1")
        except sqlite3.ProgrammingError:
            print("Conexión cerrada: no permite nuevas consultas")
    print("Temporal propio retirado; la carpeta de salida se conserva")


if __name__ == "__main__":
    main()

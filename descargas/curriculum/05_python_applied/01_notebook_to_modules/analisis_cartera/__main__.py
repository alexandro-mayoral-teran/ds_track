"""Entrada para python -m analisis_cartera; sin argumentos todavía."""

from pathlib import Path

from .flujo import export


def main():
    # __file__ ubica el paquete; no depende de una ruta personal.
    lesson = Path(__file__).resolve().parents[1]
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    output = lesson / "output/entrega_modular"
    import matplotlib
    matplotlib.use("Agg")
    tables = export(source, output)
    print(f"Entrega: {output}")
    print(f"Conciliaciones correctas: {len(tables['conciliacion'])}")


if __name__ == "__main__":
    main()

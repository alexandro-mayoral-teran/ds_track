"""05.07: consumo, último lote y conciliación con la lectura completa."""

from pathlib import Path

from pandas.testing import assert_frame_equal

from analisis_cartera.flujo import build_analysis
from analisis_cartera.iteracion import batch_indicators, iter_batches


def main() -> None:
    numbers = iter([10, 20, 30])
    print("Primer consumo:", next(numbers))
    print("Resto:", list(numbers))
    print("Agotado:", list(numbers))
    print("Lotes:", list(iter_batches([1, 2, 3, 4, 5], 2)))
    lesson = Path(__file__).resolve().parent
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    observed = batch_indicators(source, batch_size=7)
    expected = build_analysis(source)["indicadores"]
    assert_frame_equal(observed, expected, check_exact=True)
    print(observed.to_string(index=False))
    print("Coincide con lectura completa; no se exportaron archivos.")


if __name__ == "__main__":
    main()

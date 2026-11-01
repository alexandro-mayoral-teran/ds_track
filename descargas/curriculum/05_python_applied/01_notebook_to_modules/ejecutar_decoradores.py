"""05.08: funciones como valores y una envoltura sin exportar entregas."""

import inspect
import logging
from pathlib import Path
import sys

from pandas.testing import assert_frame_equal

from analisis_cartera.contratos import coverage_pct
from analisis_cartera.flujo import build_analysis
from analisis_cartera.instrumentacion import logged_indicators


def main() -> None:
    # Configurar únicamente la entrada ejecutada; importar no configura consola.
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="%(levelname)s | %(name)s | %(message)s")
    operation = coverage_pct
    print("Función guardada:", operation(2, 3))
    print("Nombre conservado:", logged_indicators.__name__)
    print("Firma visible:", inspect.signature(logged_indicators))
    lesson = Path(__file__).resolve().parent
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    actual = logged_indicators(source, batch_size=7)
    expected = build_analysis(source)["indicadores"]
    assert_frame_equal(actual, expected, check_exact=True)
    print(actual.to_string(index=False))
    try:
        logged_indicators(source, batch_size=0)
    except ValueError:
        print("Falla prevista conservada: ValueError")
    print("Comparación correcta; no se exportaron archivos.")


if __name__ == "__main__":
    main()

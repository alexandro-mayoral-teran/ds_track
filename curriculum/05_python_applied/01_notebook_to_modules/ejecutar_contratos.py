"""05.05: leer tipos y contratos con ejemplos que no exportan archivos."""

from pathlib import Path

from analisis_cartera.contratos import coverage_pct
from analisis_cartera.revision import review_summary


def double_annotated(value: int) -> int:
    """Demostración deliberadamente sin validación; no usar como conversor."""
    return value * 2


def main() -> None:
    # Una llamada incompatible se ejecuta: las anotaciones no la interceptan.
    print("Solo anotación:", double_annotated("3"))
    print("Cobertura 0/3:", coverage_pct(0, 3))
    print("Cobertura 0/0:", coverage_pct(0, 0))
    try:
        coverage_pct(True, 3)
    except TypeError as exc:
        print("Rechazo previsto:", exc)
    lesson = Path(__file__).resolve().parent
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    summary = review_summary(source, segments=["educacion", "comercio"])
    print(summary[["segmento", "registros", "conocidos", "mediana_mxn", "cobertura_pct"]].to_string(index=False))
    print("Lista vacía:", review_summary(source, segments=[]).shape)


if __name__ == "__main__":
    main()

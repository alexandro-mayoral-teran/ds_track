"""05.06: comparar funciones, diccionario y objetos sin exportar entregas."""

from dataclasses import FrozenInstanceError, replace
from pathlib import Path

from analisis_cartera.contratos import coverage_pct
from analisis_cartera.objetos import CoverageCounts, ReviewJob, ReviewOptions


def main() -> None:
    counts = {"known": 2, "total": 3}
    print("Función con diccionario:", coverage_pct(counts["known"], counts["total"]))
    instance = CoverageCounts(2, 3)
    print("Clase manual:", instance.percentage())
    options = ReviewOptions(segments=("educacion", "comercio"))
    print("Opciones:", options)
    print("Igualdad por campos:", options == ReviewOptions(segments=("educacion", "comercio")))
    try:
        options.cut = "2026-09-30"
    except FrozenInstanceError:
        print("Reasignación bloqueada: FrozenInstanceError")
    lesson = Path(__file__).resolve().parent
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    job = ReviewJob(source, options)
    summary = job.summary()
    print(summary[["segmento", "registros", "conocidos", "mediana_mxn", "cobertura_pct"]].to_string(index=False))
    empty_job = replace(job, options=replace(options, segments=()))
    print("Tupla vacía:", empty_job.summary().shape)
    print("Opciones originales conservadas:", job.options.segments)


if __name__ == "__main__":
    main()

"""05.09: medir una fase equivalente y guardar evidencia en carpeta nueva."""

import argparse
from datetime import date, timedelta
import hashlib
import json
from pathlib import Path
import platform

import altair
import matplotlib
import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.entrada import read_detail
from analisis_cartera.flujo import build_analysis
from analisis_cartera.medicion import (profile_operation, repeat_timings, trace_peak,
                                     validate_dates_each, validate_dates_reusing)
from analisis_cartera.transformacion import summarize


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para evidencia")
    parser.add_argument("--repeats", type=int, default=5, help="Repeticiones positivas; predeterminado 5")
    args = parser.parse_args(argv)
    if args.repeats < 1:
        parser.error("--repeats debe ser positivo")
    if args.output.exists():
        parser.error("La carpeta de salida ya existe; elige otra")
    lesson = Path(__file__).resolve().parent
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"

    def fingerprints():
        return {name: hashlib.sha256((source / name).read_bytes()).hexdigest()
                for name in ["creditos.csv", "cortes.csv"]}

    before = fingerprints()
    detail = read_detail(source)
    cut = "2026-10-31"
    selected, summary = summarize(detail, cut)
    baseline = build_analysis(source, cut)
    assert_frame_equal(summary, baseline["resumen"], check_exact=True)
    base_dates = detail["fecha_corte"].tolist()
    time_tables, memory_rows = [], []
    profiles = {}
    # Son listas de fechas para una fase aislada, NO carteras ampliadas válidas.
    for copies in [1, 10, 100]:
        n = len(base_dates) * copies
        for scenario in ["repetidas", "distintas"]:
            dates = (base_dates * copies if scenario == "repetidas" else
                     [(date(2026, 1, 1) + timedelta(days=i)).isoformat() for i in range(n)])

            def each():
                return validate_dates_each(dates)

            def reusing():
                return validate_dates_reusing(dates)

            def check_count(result):
                if result != n:
                    raise ValueError("La variante no conserva el conteo")

            operations = {"cada_fecha": each, "reusar_fecha": reusing}
            raw = repeat_timings(operations, repeats=args.repeats, warmups=1, check=check_count)
            raw.insert(0, "escenario", scenario)
            raw.insert(1, "n_fechas", n)
            raw.insert(2, "fechas_distintas", len(set(dates)))
            time_tables.append(raw)
            for name, operation in operations.items():
                memory_rows.append({"escenario": scenario, "n_fechas": n,
                                    "variante": name, **trace_peak(operation, check=check_count)})
            if copies == 100 and scenario == "repetidas":
                for name, operation in operations.items():
                    profiles[name] = profile_operation(operation)

    timings = pd.concat(time_tables, ignore_index=True)
    descriptive = timings.groupby(["escenario", "n_fechas", "variante"], sort=False)["segundos"].agg(
        minimo_s="min", mediana_s="median", maximo_s="max").reset_index()
    # Fronteras distintas para ubicar costos; NO compiten ni se suman entre sí.
    phases = repeat_timings({"lectura_validada": lambda: read_detail(source),
                            "transformacion_preleida": lambda: summarize(detail, cut),
                            "analisis_conciliado": lambda: build_analysis(source, cut)},
                           repeats=args.repeats, warmups=1)
    assert_frame_equal(detail, read_detail(source), check_exact=True)
    assert_frame_equal(summary, summarize(detail, cut)[1], check_exact=True)
    if fingerprints() != before:
        raise ValueError("Las fuentes cambiaron durante el experimento; no publicar evidencia")
    metadata = {"corte": cut, "registros_fuente": len(detail), "registros_corte": len(selected),
                "versiones": {"python": platform.python_version(), "pandas": pd.__version__,
                              "matplotlib": matplotlib.__version__, "altair": altair.__version__},
                "plataforma": {"sistema": platform.system(), "arquitectura": platform.machine()},
                "repeats": args.repeats, "warmups_por_variante": 1,
                "copias_lista_fechas": [1, 10, 100], "fuentes_sha256": before,
                "frontera_comparacion": "Solo validación de listas de fechas ya preparadas",
                "tiempo": "perf_counter, sin trazado/perfilado; orden alterno, comprobación fuera del reloj",
                "memoria": "tracemalloc en llamada separada; actual/pico trazados, NO RSS",
                "perfil": "cProfile separado, mayor caso de fechas repetidas",
                "excluidos": ["importaciones", "crear listas de fechas", "exportar evidencia", "figuras"],
                "limites": ["muestra pequeña", "sin aislamiento de proceso por repetición",
                            "sin controlar caché del SO ni recolector", "sin inferencia estadística",
                            "fases solapadas; no sumar lectura/transformación/análisis"]}
    args.output.mkdir(parents=True, exist_ok=False)
    timings.to_csv(args.output / "tiempos.csv", index=False)
    descriptive.to_csv(args.output / "resumen_tiempos.csv", index=False)
    pd.DataFrame(memory_rows).to_csv(args.output / "memoria.csv", index=False)
    phases.to_csv(args.output / "fases.csv", index=False)
    baseline["indicadores"].to_csv(args.output / "indicadores.csv", index=False)
    (args.output / "experimento.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    for name, text in profiles.items():
        (args.output / f"perfil_{name}.txt").write_text(text, encoding="utf-8")
    (args.output / "LEER.md").write_text(
        "# Evidencia 05.09\n\nTiempos y memoria son llamadas separadas. Comparar solo variantes de la misma "
        "frontera/escenario/tamaño. Fases.csv contiene fronteras solapadas, no sumables. "
        "Los perfiles orientan dónde mirar, no miden velocidad sin instrumentación. "
        "La carpeta se escribe por etapas: si falla una escritura puede quedar parcial. "
        "Conservarla y repetir hacia otra carpeta nueva; no es un cierre de entrega de 05.03.\n",
        encoding="utf-8")
    print(descriptive.to_string(index=False))
    print(f"Evidencia: {args.output}; revisar tiempos, memoria, perfiles y experimento.json")


if __name__ == "__main__":
    main()

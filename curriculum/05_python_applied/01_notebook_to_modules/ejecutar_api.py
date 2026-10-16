"""05.10: simular una API paginada y conciliar con las fuentes CSV existentes."""

import argparse
import hashlib
import json
import logging
from pathlib import Path
import platform

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.api import ApiError, fetch_detail, simulation_transport
from analisis_cartera.comprobacion import reconcile, reference
from analisis_cartera.entrada import read_detail
from analisis_cartera.flujo import build_analysis
from analisis_cartera.recursos import write_json_atomic
from analisis_cartera.transformacion import summarize


def main(argv=None):
    lesson = Path(__file__).resolve().parent
    api_lesson = lesson.parent / "10_api_integration"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=["correcto", "recuperable", "error_tardio", "json_invalido"], default="correcto")
    parser.add_argument("--config", type=Path, default=api_lesson / "config.json")
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para evidencia local")
    args = parser.parse_args(argv)
    if args.output.exists():
        parser.error("La carpeta de salida ya existe; usa otra")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    source = lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data"
    samples = api_lesson / "muestras"
    tracked_inputs = [source / "creditos.csv", source / "cortes.csv", args.config, *sorted(samples.iterdir())]

    def fingerprints():
        return {("muestras/" if p.parent == samples else "config/" if p == args.config else "fuentes/") + p.name:
                hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked_inputs if p.is_file()}

    try:
        before = fingerprints()
        config = json.loads(args.config.read_text(encoding="utf-8"))
        if not isinstance(config, dict) or set(config) != {"timeout", "max_attempts", "retry_delay", "max_pages", "max_rows"}:
            raise ApiError("Configuración con campos distintos del contrato")
        waits, requests = [], []
        simulated = simulation_transport(samples / f"{args.scenario}.json")

        def fetch(page, timeout):
            requests.append({"pagina": page, "timeout_s": timeout})
            return simulated(page, timeout)

        # La simulación registra pausas solicitadas, sin dormir ni conectarse.
        detail = fetch_detail(fetch, **config, wait=waits.append)
        expected_detail = read_detail(source)
        assert_frame_equal(detail, expected_detail, check_exact=True)
        cut = "2026-10-31"
        selected, summary = summarize(detail, cut)
        totals, checks = reconcile(summary, selected, reference(source, cut))
        baseline = build_analysis(source, cut)
        assert_frame_equal(totals, baseline["indicadores"], check_exact=True)
        if fingerprints() != before:
            raise ApiError("Las entradas cambiaron durante la ejecución")
        args.output.mkdir(parents=True, exist_ok=False)
        detail.to_csv(args.output / "detalle_api.csv", index=False)
        totals.to_csv(args.output / "indicadores_api.csv", index=False)
        checks.to_csv(args.output / "conciliacion.csv", index=False)
        (args.output / "LEER.md").write_text(
            "# Evidencia local 05.10\n\nNo hubo solicitudes de red. Las pausas fueron registradas, no dormidas. "
            "Una carpeta parcial no acredita éxito: ejecucion.json se escribe al final. "
            "Escritura atómica de ese JSON no hace atómica toda la carpeta. No es una entrega con figura.\n",
            encoding="utf-8")
        write_json_atomic(args.output / "ejecucion.json", {
            "estado": "completo", "modo": "simulado_sin_red", "escenario": args.scenario,
            "python": platform.python_version(), "pandas": pd.__version__, "corte": cut,
            "configuracion": config, "solicitudes": requests, "pausas_simuladas_s": waits,
            "registros": len(detail), "paginas_completas": 3, "controles": len(checks),
            "entradas_sha256": before})
    except (ApiError, OSError, json.JSONDecodeError, AssertionError) as exc:
        # Sin contenido remoto, URLs, cabeceras privadas ni datos en el registro.
        logging.error("Extracción no completada: %s", str(exc) if isinstance(exc, ApiError) else type(exc).__name__)
        return 1
    print(totals.to_string(index=False))
    print(f"Simulación completa: {len(requests)} solicitudes, {len(waits)} pausas registradas. Evidencia: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

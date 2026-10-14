"""Entrada de 05.02: argumentos, configuración y logging del análisis conocido."""

import argparse
import json
import logging
from pathlib import Path
import platform
import sys

from .configuracion import load_settings, LEVELS

LOGGER = logging.getLogger(__name__)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--config", type=Path, help="Archivo JSON; sus rutas son relativas a su carpeta")
    parser.add_argument("--source", type=Path, help="Carpeta de CSV; relativa al directorio de trabajo")
    parser.add_argument("--output", type=Path, help="Carpeta nueva; necesaria aquí o en el JSON")
    parser.add_argument("--cut", help="Fecha YYYY-MM-DD; predeterminado 2026-10-31")
    parser.add_argument("--dpi", type=int, help="Resolución PNG positiva; predeterminado 160")
    parser.add_argument("--log-level", choices=LEVELS, help="Umbral de mensajes; predeterminado INFO")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        settings, origins, config_path = load_settings(args)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    # Configurar la consola solo en la entrada explícita, nunca al importar.
    logging.basicConfig(level=logging.WARNING,
                        format="%(levelname)s | %(name)s | %(message)s")
    LOGGER.setLevel(settings["log_level"])
    LOGGER.info("Inicio: corte=%s dpi=%s", settings["cut"], settings["dpi"])
    LOGGER.info("Fuentes: %s", settings["source"])
    LOGGER.info("Destino nuevo: %s", settings["output"])
    LOGGER.debug("Procedencia de valores: %s", origins)
    # El cálculo y las figuras siguen en el paquete de 05.01.
    import matplotlib
    matplotlib.use("Agg")
    from .flujo import export

    try:
        tables = export(settings["source"], settings["output"], settings["cut"], settings["dpi"])
        overall = tables["indicadores"].iloc[-1]
        if overall.registros == 0:
            LOGGER.warning("Corte sin registros: mediana y cobertura no definidas")
        elif overall.conocidos == 0:
            LOGGER.warning("Hay registros, pero ningún saldo conocido: cobertura 0 %")
        elif overall.conocidos < overall.registros:
            LOGGER.warning("Cobertura parcial: %s/%s saldos conocidos", int(overall.conocidos), int(overall.registros))
        LOGGER.info("Datos conciliados: %s comprobaciones", len(tables["conciliacion"]))
        # Registro persistente, independiente del umbral de mensajes de consola.
        metadata = json.loads((settings["output"] / "entrega.json").read_text(encoding="utf-8"))
        record = {"configuracion_efectiva": {key: str(value) if isinstance(value, Path) else value
                                             for key, value in settings.items()},
                  "origen_valores": origins,
                  "archivo_configuracion": str(config_path) if config_path else None,
                  "versiones": {"python": platform.python_version(), **metadata["versiones"]},
                  "reglas": ["Unidad: un crédito en un corte",
                             "Mediana sobre saldos conocidos; cero válido participa",
                             "Cobertura: conocidos / registros; sin registros no definida",
                             "Referencia independiente CSV/statistics antes de exportar"],
                  "comprobaciones_datos": len(tables["conciliacion"]),
                  "revision_visual": "Pendiente; el registro no acredita revisión ni aprendizaje"}
        (settings["output"] / "ejecucion.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    except (OSError, ValueError) as exc:
        LOGGER.error("Ejecución sin completar: %s", exc)
        LOGGER.debug("Detalle de la falla", exc_info=True)
        return 1
    LOGGER.info("Entrega y registro terminados: %s", settings["output"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

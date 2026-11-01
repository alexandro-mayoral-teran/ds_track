"""05.03: comunicar fallas previstas y cerrar solo una entrega terminada."""

import logging
import sys

from .cli import build_parser
from .configuracion import load_settings

LOGGER = logging.getLogger(__name__)


def main(argv=None):
    parser = build_parser()
    parser.description = __doc__
    parser.add_argument("--simulate-failure", choices=["after-export", "record", "before-close"],
                        help="Falla didáctica en una carpeta NUEVA; omitir en una ejecución normal")
    args = parser.parse_args(argv)
    try:
        settings, origins, config_path = load_settings(args)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    logging.basicConfig(level=logging.WARNING,
                        format="%(levelname)s | %(name)s | %(message)s")
    LOGGER.setLevel(settings["log_level"])
    LOGGER.info("Inicio: corte=%s; destino=%s", settings["cut"], settings["output"])
    LOGGER.debug("Procedencia de valores: %s", origins)
    import matplotlib
    matplotlib.use("Agg")
    from .cierre import run_delivery

    try:
        tables = run_delivery(settings, origins, config_path, args.simulate_failure)
    except (OSError, ValueError) as exc:
        LOGGER.error("Entrega sin cerrar; conservar y revisar %s: %s", settings["output"], exc)
        LOGGER.debug("Causa y recorrido de la falla", exc_info=True)
        return 1
    overall = tables["indicadores"].iloc[-1]
    if overall.registros == 0:
        LOGGER.warning("Corte sin registros: mediana y cobertura no definidas")
    elif overall.conocidos < overall.registros:
        LOGGER.warning("Cobertura parcial: %s/%s saldos conocidos", int(overall.conocidos), int(overall.registros))
    LOGGER.info("Entrega cerrada: %s; %s conciliaciones", settings["output"], len(tables["conciliacion"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

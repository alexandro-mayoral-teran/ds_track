"""05.11: verificar archivos guardados y, opcionalmente, su reconstrucción."""

import argparse
import json
from pathlib import Path

from analisis_cartera.auditoria import compare_deliveries, verify_delivery


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("delivery", type=Path, help="Carpeta cerrada por ejecutar_seguro.py")
    parser.add_argument("--compare", type=Path, help="Otra entrega reconstruida hacia una carpeta nueva")
    args = parser.parse_args(argv)
    try:
        report = (compare_deliveries(args.delivery, args.compare) if args.compare is not None
                  else verify_delivery(args.delivery))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"Verificación no completada: {exc}")
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Genera un .qmd completo desde la muestra propia; renderizar es otro paso."""

import argparse
import importlib.util
from pathlib import Path


def preparar_documento(origen: Path, destino: Path) -> None:
    carpeta = Path(__file__).resolve().parent
    # Reutilizar las reglas no requiere entregas de la lección anterior.
    modulo = carpeta.parent / "01_report_source_render" / "preparar.py"
    spec = importlib.util.spec_from_file_location("referencia1101", modulo)
    referencia = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(referencia)
    inicio = (carpeta / "inicio.qmd").read_text(encoding="utf-8")
    referencia.preparar(origen, destino)
    borrador = (destino / "borrador.md").read_text(encoding="utf-8")
    # Omitir el título/prefacio del borrador: el título está ahora en el YAML.
    contenido = borrador[borrador.index("## Pregunta y público"):]
    (destino / "reporte.qmd").write_text(inicio + "\n" + contenido, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path, help="Carpeta nueva para fuente y evidencia")
    parser.add_argument("--fuente", type=Path, default=Path(__file__).with_name("cartera.csv"))
    args = parser.parse_args()
    preparar_documento(args.fuente, args.destino)
    print(f"Documento creado: {args.destino / 'reporte.qmd'}; falta renderizar con Quarto")

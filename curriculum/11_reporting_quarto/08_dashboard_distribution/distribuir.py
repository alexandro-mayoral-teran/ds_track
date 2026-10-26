"""Copiar un HTML revisado y su nota de lectura a una carpeta nueva."""
import argparse
from pathlib import Path
import shutil


def distribuir(html: Path, destino: Path) -> None:
    nota = Path(__file__).resolve().parent / "LEEME_entrega.md"
    if not html.is_file() or html.suffix.lower() != ".html" or not nota.is_file():
        raise ValueError("Se requiere un HTML existente y la nota de lectura")
    destino.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(html, destino / "dashboard.html")
    shutil.copyfile(nota, destino / "LEEME.md")
    if html.read_bytes() != (destino / "dashboard.html").read_bytes():
        raise ValueError("Copia distinta: conservar carpeta e investigar")
    print("Copia idéntica preparada. Abrir y revisar dashboard.html en el destino.")
    print("La igualdad de copia no verifica datos, recursos o accesibilidad.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("destino", type=Path)
    args = parser.parse_args()
    distribuir(args.html, args.destino)

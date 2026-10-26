"""Abrir una prueba local del portal, construyéndola si aún no existe."""
import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import shutil
import webbrowser

sys.path.insert(0, str(Path(__file__).resolve().parent / "herramientas"))
from preparar_portal import construir


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--destino", type=Path, default=Path("output/portal-local"))
    rstudio = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "RStudio/resources/app/bin/quarto/bin/quarto.exe"
    quarto = shutil.which("quarto") or (str(rstudio) if rstudio.is_file() else "quarto")
    p.add_argument("--quarto", default=quarto)
    p.add_argument("--puerto", type=int, default=8871)
    p.add_argument("--abrir", action="store_true")
    a = p.parse_args()
    sitio = a.destino.resolve() / "_site"
    if not a.destino.exists():
        construir(a.destino, a.quarto)
    if not (sitio / "index.html").is_file():
        raise FileNotFoundError("Copia incompleta: revisar render.log y elegir otro --destino")
    manejador = partial(SimpleHTTPRequestHandler, directory=str(sitio))
    with ThreadingHTTPServer(("127.0.0.1", a.puerto), manejador) as server:
        url = f"http://127.0.0.1:{a.puerto}/"
        print(f"Portal local: {url}\nPara detener: Ctrl+C. Se sirve solo la copia generada.", flush=True)
        if a.abrir:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido. Tus archivos se conservan.")


if __name__ == "__main__":
    main()

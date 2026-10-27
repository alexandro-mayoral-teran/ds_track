"""Abrir una prueba local del portal, construyéndola si aún no existe."""
import argparse
from datetime import datetime
import hashlib
import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import shutil
import webbrowser

sys.path.insert(0, str(Path(__file__).resolve().parent / "herramientas"))
from preparar_portal import construir, REPO


def fuentes_cambiaron(sitio):
    """Comparar fuentes incluidas; no renderizar, escribir ni interpretar el progreso."""
    try:
        registro = json.loads((sitio / "procedencia.json").read_text(encoding="utf-8"))
        if not isinstance(registro, dict) or not isinstance(registro.get("sha256_fuentes"), dict):
            return True
        huellas = registro["sha256_fuentes"]
        if "portal/curso.json" not in huellas:
            return True
        for nombre, huella in huellas.items():
            fuente = (REPO / nombre).resolve()
            if not fuente.is_relative_to(REPO) or not fuente.is_file():
                return True
            if hashlib.sha256(fuente.read_bytes()).hexdigest() != huella:
                return True
        return False
    except (OSError, ValueError, KeyError, TypeError):
        return True


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
    if (sitio / "index.html").is_file() and fuentes_cambiaron(sitio):
        anterior = a.destino
        candidatas = sorted(a.destino.parent.glob(a.destino.name + "-*"), reverse=True)
        vigente = next((p for p in candidatas if p.is_dir()
                        and p.resolve().is_relative_to(a.destino.parent.resolve())
                        and (p / "_site/index.html").is_file()
                        and not fuentes_cambiaron(p / "_site")), None)
        if vigente:
            a.destino = vigente
            print(f"Uso la copia actualizada: {vigente}.", flush=True)
        else:
            a.destino = a.destino.with_name(a.destino.name + "-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
            print(f"Las fuentes cambiaron. Conservo {anterior} y preparo {a.destino}.", flush=True)
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

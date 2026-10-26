"""Adaptar solo el catálogo del piloto y renderizar sin ejecutar código educativo."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
from preparar_practica import REPO, catalogo, preparar

PORTAL = REPO / "portal"


def adaptar(texto, origen, destinos):
    """Enlaces Markdown inline del material seleccionado; no toca bloques de código."""
    lineas, cerca = [], None
    def enlace(m):
        ruta = m.group(2)
        u = urlsplit(ruta)
        if u.scheme or u.netloc or not u.path:
            return m.group(0)
        resuelta = (origen.parent / unquote(u.path)).resolve()
        if resuelta not in destinos:
            raise ValueError(f"Enlace no enumerado en sesiones.json: {origen.name} → {ruta}")
        nueva = destinos[resuelta]
        if u.fragment and "#" not in nueva:
            nueva += "#" + u.fragment
        return f"{m.group(1)}]({nueva})"
    for linea in texto.splitlines():
        marca = re.match(r"^\s*(`{3,}|~{3,})", linea)
        if marca:
            if cerca is None:
                cerca = marca.group(1)
            elif marca.group(1)[0] == cerca[0] and len(marca.group(1)) >= len(cerca):
                cerca = None
            lineas.append(linea)
        else:
            lineas.append(linea if cerca else re.sub(r"(!?\[[^\]\n]*)\]\(([^)\s]+)\)", enlace, linea))
    return "\n".join(lineas) + "\n"


def construir(destino, quarto="quarto"):
    datos = catalogo()
    destino = Path(destino).resolve()
    # La generación nunca modifica curriculum, labs o una carpeta ya iniciada.
    if destino.exists():
        raise FileExistsError("Destino ocupado: conserva esa prueba y elige otra carpeta")
    version = subprocess.check_output([quarto, "--version"], text=True).strip()
    destino.mkdir(parents=True)
    for nombre in ["_quarto.yml", "estilos.css", "scripts.html", "portal.js"]:
        shutil.copyfile(PORTAL / nombre, destino / nombre)
    for nombre in ["index", "sesion", "bitacora"]:
        shutil.copyfile(PORTAL / "paginas" / f"{nombre}.qmd", destino / f"{nombre}.qmd")
    descargas = destino / "descargas"
    descargas.mkdir()
    preparar(descargas / "02.01")
    with ZipFile(descargas / "02.01.zip", "w") as paquete:
        for archivo in sorted((descargas / "02.01").iterdir()):
            paquete.write(archivo, "02.01/" + archivo.name)
    destinos = {(REPO / datos["leccion"]).resolve(): "leccion.qmd",
                (REPO / datos["lab"]).resolve(): "lab.qmd"}
    for nombre, ruta in datos["practica"].items():
        destinos[(REPO / ruta).resolve()] = "descargas/02.01/" + nombre
    consultas = []
    for i, ruta in enumerate(datos["consulta"], 1):
        origen = REPO / ruta
        nombre = f"{i:02d}-{origen.name}"
        shutil.copyfile(origen, descargas / nombre)
        destinos[origen.resolve()] = f"fuentes.qmd#fuente-{i}"
        titulo = origen.read_text(encoding="utf-8").splitlines()[0].lstrip("# ") if origen.suffix == ".md" else origen.name
        consultas.append(f'## {html.escape(titulo)} {{#fuente-{i}}}\n\nRuta en tu clon: `{ruta}`.\n\n'
                         f'Fuera de esta sesión del piloto. Consulta el archivo original en tu clon '
                         f'de DS Track o [descarga su fuente](descargas/{nombre}). '
                         'El Markdown descargado puede contener enlaces relativos al repositorio.\n')
    (destino / "fuentes.qmd").write_text(
        '---\ntitle: "Material de consulta"\n---\n\n'
        'El piloto incluye una sola sesión. Estos archivos se conservan como consulta, '
        'sin presentar otras sesiones como implementadas en el portal.\n\n' + "\n".join(consultas), encoding="utf-8")
    for clave, nombre, paso in [("leccion", "leccion", "COMPRENDER"), ("lab", "lab", "PRACTICAR")]:
        origen = REPO / datos[clave]
        texto = origen.read_text(encoding="utf-8")
        titulo, cuerpo = texto.split("\n", 1)
        cuerpo = adaptar(cuerpo, origen, destinos)
        cabecera = f'---\ntitle: {json.dumps(titulo.lstrip("# "), ensure_ascii=False)}\n---\n\n'
        nota = f'<p class="eyebrow">02.01 / {paso} · CONTENIDO DEL CURSO</p>\n\n'
        nota += '[← Volver a tu recorrido](sesion.qmd){.back-link}\n\n'
        (destino / f"{nombre}.qmd").write_text(cabecera + nota + cuerpo, encoding="utf-8")
    fuentes = sorted(set([datos["leccion"], datos["lab"], *datos["practica"].values(), *datos["consulta"],
                          "portal/sesiones.json", "portal/_quarto.yml", "portal/estilos.css", "portal/scripts.html", "portal/portal.js",
                          *[f"portal/paginas/{n}.qmd" for n in ["index", "sesion", "bitacora"]]]))
    registro = {"sesion": datos["id"], "quarto": version,
                "sha256_fuentes": {n: hashlib.sha256((REPO/n).read_bytes()).hexdigest() for n in fuentes}}
    (destino / "procedencia.json").write_text(json.dumps(registro, indent=2, ensure_ascii=False), encoding="utf-8")
    with (destino / "render.log").open("w", encoding="utf-8") as log:
        subprocess.run([quarto, "render", str(destino)], check=True, stdout=log, stderr=subprocess.STDOUT)
    print(f"Portal generado: {destino / '_site/index.html'}")
    return destino / "_site"


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("destino", type=Path)
    p.add_argument("--quarto", default="quarto")
    a = p.parse_args()
    construir(a.destino, a.quarto)

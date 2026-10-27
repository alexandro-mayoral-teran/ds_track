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
        if u.scheme or u.netloc:
            return m.group(0)
        if not u.path:
            # Quarto quita el número inicial de los identificadores automáticos.
            # Conservamos anclas explícitas, si el autor las declaró.
            fragmento = unquote(u.fragment)
            if fragmento and f'{{#{fragmento}}}' not in texto and f'id="{fragmento}"' not in texto:
                fragmento = re.sub(r"^[0-9]+-", "", fragmento)
            return f"{m.group(1)}](#{fragmento})" if fragmento else m.group(0)
        resuelta = (origen.parent / unquote(u.path)).resolve()
        if resuelta.is_dir():
            resuelta = resuelta / "README.md"
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
    curso = json.loads((PORTAL / "curso.json").read_text(encoding="utf-8"))
    fuentes_curso = [m["fuente"] for m in curso["modulos"]]
    fuentes_curso += [f[k] for f in curso["lecciones_00"] for k in ["leccion", "lab"]]
    fuentes_curso += [p["fuente"] for p in curso["paginas_00"]] + curso["archivos_00"] + curso["consulta_00"]
    navegacion = curso.get("navegacion", {})
    fuentes_curso += list(navegacion)
    if any(ruta not in {"index.qmd", "contenido.qmd"} for ruta in navegacion.values()):
        raise ValueError("La navegación del repo debe apuntar a portada o contenido")
    for n in fuentes_curso:
        path = (REPO / n).resolve()
        if not path.is_relative_to(REPO) or not path.is_file():
            raise ValueError(f"Fuente de curso inválida: {n}")
    destino = Path(destino).resolve()
    # La generación nunca modifica curriculum, labs o una carpeta ya iniciada.
    if destino.exists():
        raise FileExistsError("Destino ocupado: conserva esa prueba y elige otra carpeta")
    version = subprocess.check_output([quarto, "--version"], text=True).strip()
    destino.mkdir(parents=True)
    for nombre in ["_quarto.yml", "estilos.css", "scripts.html", "portal.js"]:
        shutil.copyfile(PORTAL / nombre, destino / nombre)
    for nombre in ["index", "sesion", "bitacora", "modulo-00", "registro"]:
        shutil.copyfile(PORTAL / "paginas" / f"{nombre}.qmd", destino / f"{nombre}.qmd")
    tarjetas_leccion = []
    for leccion in curso["lecciones_00"]:
        prefijo = leccion["id"].replace(".", "-")
        tarjetas_leccion.append(
            f'<article class="lesson-card"><span class="step-num">{leccion["id"]}</span><div>'
            f'<h3>{html.escape(leccion["titulo"])}</h3><p>{html.escape(leccion["resultado"])}</p>'
            f'<a href="{prefijo}-leccion.qmd">Leer lección →</a> '
            f'<a href="{prefijo}-lab.qmd">Ir al lab</a></div></article>')
    modulo = destino / "modulo-00.qmd"
    modulo.write_text(modulo.read_text(encoding="utf-8").replace("<!-- LECCIONES_00 -->", "\n".join(tarjetas_leccion)), encoding="utf-8")
    descargas = destino / "descargas"
    descargas.mkdir()
    preparar(descargas / "02.01")
    with ZipFile(descargas / "02.01.zip", "w") as paquete:
        for archivo in sorted((descargas / "02.01").iterdir()):
            paquete.write(archivo, "02.01/" + archivo.name)
    destinos = {(REPO / datos["leccion"]).resolve(): "leccion.qmd",
                (REPO / datos["lab"]).resolve(): "lab.qmd"}
    destinos.update({(REPO / fuente).resolve(): ruta for fuente, ruta in navegacion.items()})
    destinos[REPO / "PROGRESS.md"] = "registro.qmd"
    paginas_curso = []
    for leccion in curso["lecciones_00"]:
        prefijo = leccion["id"].replace(".", "-")
        for clave in ["leccion", "lab"]:
            ruta = f"{prefijo}-{clave}.qmd"
            destinos[(REPO / leccion[clave]).resolve()] = ruta
            paginas_curso.append((leccion[clave], ruta, leccion["id"]))
    for pagina in curso["paginas_00"]:
        destinos[(REPO / pagina["fuente"]).resolve()] = pagina["ruta"]
        paginas_curso.append((pagina["fuente"], pagina["ruta"], "00 / APOYO"))
    for ruta in curso["archivos_00"]:
        nuevo = "descargas/" + ruta
        (destino / nuevo).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / ruta, destino / nuevo)
        destinos[(REPO / ruta).resolve()] = nuevo
    for nombre, ruta in datos["practica"].items():
        destinos[(REPO / ruta).resolve()] = "descargas/02.01/" + nombre
    consultas = []
    for i, ruta in enumerate(dict.fromkeys(datos["consulta"] + curso["consulta_00"]), 1):
        origen = REPO / ruta
        nombre = f"{i:02d}-{origen.name}"
        shutil.copyfile(origen, descargas / nombre)
        if origen.resolve() not in destinos:
            destinos[origen.resolve()] = f"fuentes.qmd#fuente-{i}"
        titulo = origen.read_text(encoding="utf-8").splitlines()[0].lstrip("# ") if origen.suffix == ".md" else origen.name
        consultas.append(f'## {html.escape(titulo)} {{#fuente-{i}}}\n\nRuta en tu clon: `{ruta}`.\n\n'
                         f'Fuera de esta sesión del piloto. Consulta el archivo original en tu clon '
                         f'de DS Track o [descarga su fuente](descargas/{nombre}). '
                         'El Markdown descargado puede contener enlaces relativos al repositorio.\n')
    (destino / "fuentes.qmd").write_text(
        '---\ntitle: "Material de consulta"\n---\n\n'
        'El portal integra el módulo 00 y la prueba acompañada 02.01. Estos archivos '
        'se conservan también como consulta; las páginas integradas se abren desde Contenido.\n\n' + "\n".join(consultas), encoding="utf-8")
    tarjetas = []
    for modulo in curso["modulos"]:
        numero = modulo["id"]
        origen = REPO / modulo["fuente"]
        ruta_indice = f"descargas/indice-{numero}.md"
        shutil.copyfile(origen, destino / ruta_indice)
        if numero == "00":
            destinos[origen.resolve()] = "modulo-00.qmd"
            enlace = '<a class="button primary" href="modulo-00.qmd">Entrar al módulo →</a>'
            estado = "Lectura y labs en el portal"
        else:
            destinos[origen.resolve()] = f"contenido.qmd#modulo-{numero}"
            etiqueta = "Descargar plan" if modulo["estado"] == "plan" else "Descargar índice del repo"
            enlace = f'<a href="{ruta_indice}" download>{etiqueta} (.md)</a>'
            estado = "Planificado" if modulo["estado"] == "plan" else "Material en el repo · integración en portal pendiente"
        tarjetas.append(f'<article class="module-card" id="modulo-{numero}"><span class="module-number">{numero}</span>'
                        f'<div><p class="eyebrow">{html.escape(estado)}</p><h2>{html.escape(modulo["titulo"])}</h2>'
                        f'<p>{html.escape(modulo["resumen"])}</p>{enlace}</div></article>')
    (destino / "contenido.qmd").write_text(
        '---\ntitle: "Tu recorrido de aprendizaje"\ntoc: false\n---\n\n'
        '<p class="eyebrow">CONTENIDO / 00–14</p>\n\n'
        'Empieza con las herramientas y avanza por sus prerrequisitos. El material '
        'disponible en el repositorio y las páginas integradas en este portal son estados distintos. '
        'Los índices descargados pueden contener rutas relativas al clon del curso. '
        'Streamlit (12) y Shiny (13) son alternativas: basta una aplicación antes '
        'del proyecto reproducible (14).\n\n'
        '<div class="catalogue-key"><span class="pill">00 · integrado</span>'
        '<span>01–11 · material en el repositorio</span><span>12–14 · planes</span></div>\n\n'
        '<div class="module-list">' + "\n".join(tarjetas) + '</div>\n\n'
        '[Probar la sesión acompañada 02.01 de pandas →](sesion.qmd)\n', encoding="utf-8")
    for fuente, ruta, etiqueta in paginas_curso:
        origen = REPO / fuente
        titulo, cuerpo = origen.read_text(encoding="utf-8").split("\n", 1)
        cabecera = f'---\ntitle: {json.dumps(titulo.lstrip("# "), ensure_ascii=False)}\n---\n\n'
        nota = f'<p class="eyebrow">MÓDULO 00 / {etiqueta}</p>\n\n'
        nota += '[Contenido](contenido.qmd) / [Entorno de aprendizaje](modulo-00.qmd)\n\n'
        (destino / ruta).write_text(cabecera + nota + adaptar(cuerpo, origen, destinos), encoding="utf-8")
    for clave, nombre, paso in [("leccion", "leccion", "COMPRENDER"), ("lab", "lab", "PRACTICAR")]:
        origen = REPO / datos[clave]
        texto = origen.read_text(encoding="utf-8")
        titulo, cuerpo = texto.split("\n", 1)
        cuerpo = adaptar(cuerpo, origen, destinos)
        cabecera = f'---\ntitle: {json.dumps(titulo.lstrip("# "), ensure_ascii=False)}\n---\n\n'
        nota = f'<p class="eyebrow">02.01 / {paso} · CONTENIDO DEL CURSO</p>\n\n'
        nota += '[← Volver a tu recorrido](sesion.qmd){.back-link}\n\n'
        (destino / f"{nombre}.qmd").write_text(cabecera + nota + cuerpo, encoding="utf-8")
    fuentes = sorted(set([datos["leccion"], datos["lab"], *datos["practica"].values(), *datos["consulta"], *fuentes_curso,
                          "portal/sesiones.json", "portal/_quarto.yml", "portal/estilos.css", "portal/scripts.html", "portal/portal.js",
                          "portal/curso.json", "portal/herramientas/preparar_portal.py", "portal/herramientas/preparar_practica.py",
                          "portal/servir.py", *[f"portal/paginas/{n}.qmd" for n in ["index", "sesion", "bitacora", "modulo-00", "registro"]]]))
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

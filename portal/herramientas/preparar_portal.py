"""Adaptar las fuentes catalogadas y renderizar sin ejecutar código educativo."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[2]
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
            raise ValueError(f"Enlace no enumerado en el catálogo del portal: {origen.name} → {ruta}")
        nueva = destinos[resuelta]
        if u.fragment and "#" not in nueva:
            fragmento = unquote(u.fragment)
            contenido_destino = resuelta.read_text(encoding="utf-8")
            if (f'{{#{fragmento}}}' not in contenido_destino
                    and f'id="{fragmento}"' not in contenido_destino):
                fragmento = re.sub(r"^[0-9]+-", "", fragmento)
            nueva += "#" + fragmento
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
    curso = json.loads((PORTAL / "curso.json").read_text(encoding="utf-8"))
    modulos_integrados = [m for m in curso["modulos"] if m.get("integrado")]
    lecciones_por_modulo = {
        modulo["id"]: curso.get(f"lecciones_{modulo['id']}", [])
        for modulo in modulos_integrados
    }
    archivos_por_modulo = {
        modulo["id"]: curso.get(f"archivos_{modulo['id']}", [])
        for modulo in modulos_integrados
    }
    consultas_modulos = [
        ruta
        for modulo in modulos_integrados
        for ruta in curso.get(f"consulta_{modulo['id']}", [])
    ]
    fuentes_curso = [m["fuente"] for m in curso["modulos"]]
    fuentes_curso += [
        f[k]
        for lecciones in lecciones_por_modulo.values()
        for f in lecciones
        for k in ["leccion", "lab"]
    ]
    fuentes_curso += [
        p["fuente"] for p in curso.get("paginas_00", [])
    ] + [
        ruta
        for archivos in archivos_por_modulo.values()
        for ruta in archivos
    ] + consultas_modulos
    navegacion = curso.get("navegacion", {})
    fuentes_curso += list(navegacion)
    if any(ruta not in {"index.qmd", "contenido.qmd"} for ruta in navegacion.values()):
        raise ValueError("La navegación del repo debe apuntar a portada o contenido")
    fuentes_curso.append("portal/plantillas/modulo.qmd")
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
    for nombre in ["_quarto.yml", "estilos.css", "favicon.svg"]:
        shutil.copyfile(PORTAL / nombre, destino / nombre)
    for nombre in ["index", "modulo-00", "registro"]:
        shutil.copyfile(PORTAL / "paginas" / f"{nombre}.qmd", destino / f"{nombre}.qmd")
    tarjetas_leccion = []
    for leccion in lecciones_por_modulo["00"]:
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
    destinos = {(REPO / fuente).resolve(): ruta for fuente, ruta in navegacion.items()}
    destinos[REPO / "PROGRESS.md"] = "registro.qmd"
    destinos[(REPO / "docs/architecture.md").resolve()] = "contenido.qmd#modulo-05"
    # Los proyectos siguen pendientes: se remite al recorrido completo.
    destinos[(REPO / "projects/README.md").resolve()] = "contenido.qmd"
    # Un enlace a la carpeta de CSV compartidos se resuelve a la lección que los presenta.
    destinos[(REPO / "curriculum/03_sql_databases/01_relational_sqlite/data/README.md").resolve()] = "03-01-leccion.qmd"
    # Un enlace a una carpeta de pruebas 05.NN se resuelve a la lección que la introduce.
    for carpeta in (REPO / "curriculum/05_python_applied/01_notebook_to_modules").glob("pruebas_05[0-9][0-9]"):
        destinos[(carpeta / "README.md").resolve()] = f"05-{carpeta.name[-2:]}-leccion.qmd"
    paginas_curso = []
    for modulo in curso["modulos"]:
        numero = modulo["id"]
        if modulo.get("integrado"):
            ruta_modulo = f"modulo-{numero}.qmd"
            destinos[(REPO / modulo["fuente"]).resolve()] = ruta_modulo
            for leccion in lecciones_por_modulo[numero]:
                prefijo = leccion["id"].replace(".", "-")
                for clave in ["leccion", "lab"]:
                    ruta = f"{prefijo}-{clave}.qmd"
                    destinos[(REPO / leccion[clave]).resolve()] = ruta
                    paginas_curso.append((leccion[clave], ruta, leccion["id"], numero))
        else:
            destinos[(REPO / modulo["fuente"]).resolve()] = f"contenido.qmd#modulo-{numero}"
            # Las lecciones y labs de módulos no integrados llevan a su tarjeta.
            carpeta = (REPO / modulo["fuente"]).parent
            for sub in carpeta.iterdir():
                for base in (sub, REPO / "labs" / carpeta.name / sub.name):
                    destinos.setdefault((base / "README.md").resolve(), f"contenido.qmd#modulo-{numero}")
    for pagina in curso.get("paginas_00", []):
        destinos[(REPO / pagina["fuente"]).resolve()] = pagina["ruta"]
        paginas_curso.append((pagina["fuente"], pagina["ruta"], "00 / APOYO", "00"))
    for archivos in archivos_por_modulo.values():
        for ruta in archivos:
            nuevo = "descargas/" + ruta
            destinos[(REPO / ruta).resolve()] = nuevo
            (destino / nuevo).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / ruta, destino / nuevo)
    consultas = []
    rutas_consulta = list(dict.fromkeys(consultas_modulos))
    for i, ruta in enumerate(rutas_consulta, 1):
        origen = REPO / ruta
        nombre = f"{i:02d}-{origen.name}"
        shutil.copyfile(origen, descargas / nombre)
        if origen.resolve() not in destinos:
            destinos[origen.resolve()] = f"fuentes.qmd#fuente-{i}"
        titulo = origen.read_text(encoding="utf-8").splitlines()[0].lstrip("# ") if origen.suffix == ".md" else origen.name
        consultas.append(f'## {html.escape(titulo)} {{#fuente-{i}}}\n\nRuta en tu clon: `{ruta}`.\n\n'
                         f'Consulta el archivo original en tu clon '
                         f'de DS Track o [descarga su fuente](descargas/{nombre}). '
                         'El Markdown descargado puede contener enlaces relativos al repositorio.\n')
    (destino / "fuentes.qmd").write_text(
        '---\ntitle: "Material de consulta"\n---\n\n'
        'Aquí encontrarás apoyos opcionales relacionados con los módulos integrados. '
        'Las lecciones y labs se abren desde sus módulos. Para consultar el estado '
        'del resto del recorrido, visita [Contenido](contenido.qmd).\n\n'
        + "\n".join(consultas), encoding="utf-8")
    for fuente, ruta, etiqueta, numero in paginas_curso:
        origen = REPO / fuente
        titulo, cuerpo = origen.read_text(encoding="utf-8").split("\n", 1)
        cabecera = f'---\ntitle: {json.dumps(titulo.lstrip("# "), ensure_ascii=False)}\n---\n\n'
        modulo = next(m for m in modulos_integrados if m["id"] == numero)
        nota = f'<p class="eyebrow">MÓDULO {numero} / {etiqueta}</p>\n\n'
        nota += f'[Contenido](contenido.qmd) / [{html.escape(modulo["titulo"])}](modulo-{numero}.qmd)\n\n'
        (destino / ruta).write_text(cabecera + nota + adaptar(cuerpo, origen, destinos), encoding="utf-8")
    for modulo in modulos_integrados:
        if modulo["id"] == "00":
            continue
        origen = REPO / modulo["fuente"]
        _, cuerpo = origen.read_text(encoding="utf-8").split("\n", 1)
        plantilla = (PORTAL / "plantillas" / "modulo.qmd").read_text(encoding="utf-8")
        pagina = plantilla.replace("{{TITULO}}", json.dumps(modulo["titulo"], ensure_ascii=False))
        pagina = pagina.replace("{{ID}}", modulo["id"])
        pagina = pagina.replace("<!-- CONTENIDO_DEL_MODULO -->", adaptar(cuerpo, origen, destinos))
        (destino / f"modulo-{modulo['id']}.qmd").write_text(pagina, encoding="utf-8")
    tarjetas = []
    for modulo in curso["modulos"]:
        numero = modulo["id"]
        origen = REPO / modulo["fuente"]
        ruta_indice = f"descargas/indice-{numero}.md"
        shutil.copyfile(origen, destino / ruta_indice)
        if modulo.get("integrado"):
            enlace = f'<a class="button primary" href="modulo-{numero}.qmd">Entrar al módulo →</a>'
            estado = "Lectura y labs en el portal"
        else:
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
        '<div class="catalogue-key"><span class="pill">00–05 · integrados</span>'
        '<span>06–14 · material en el repositorio</span></div>\n\n'
        '<div class="module-list">' + "\n".join(tarjetas) + '</div>\n', encoding="utf-8")
    fuentes = sorted(set([*fuentes_curso, "portal/_quarto.yml", "portal/estilos.css",
                          "portal/curso.json", "portal/favicon.svg",
                          "portal/plantillas/modulo.qmd", "portal/herramientas/preparar_portal.py",
                          "portal/servir.py",
                          *[f"portal/paginas/{n}.qmd" for n in ["index", "modulo-00", "registro"]]]))
    registro = {"quarto": version,
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

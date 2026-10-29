"""14.07: lector de solo lectura y reporte estático desde la misma entrega."""
from pathlib import Path
import argparse
import csv
from datetime import datetime, timezone
from html import escape
import re
import shutil
import subprocess

from pipeline import RAIZ, tablas_esperadas, comprobar, md5
from ejecutar import verificar_entorno
from modelo import leer


def cargar(archivo="config/octubre.csv", app="streamlit"):
    cfg, tablas = tablas_esperadas(archivo)
    if app not in ("streamlit", "shiny") or cfg["app"] != app:
        raise ValueError("La app solicitada no coincide con la configuracion")
    destino = cfg["salida_resuelta"]
    comprobar(destino, tablas)  # Nunca llama pipeline(): no crea salidas ausentes.
    # Usar los valores ya conciliados evita una segunda lectura sin comprobar.
    columnas, *filas = tablas["seleccion.csv"]
    contexto = dict(zip(*tablas["contexto.csv"]))
    return {"config": archivo, "entrega": cfg["salida"], "revision": md5(destino / "COMPLETO.csv"),
            "comprobado_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "contexto": contexto, "seleccion": [dict(zip(columnas, f)) for f in filas]}


def vista(p):
    c = p["contexto"]
    encabezado = "".join(f'<p><strong>{escape(k)}:</strong> {escape(str(v))}</p>' for k, v in [
        ("Corte", c["corte"]), ("Segmentos", c["segmentos"]), ("Mínimo MXN", c["minimo_texto"]),
        ("Reglas", c["version_reglas"]), ("App", c["app"]), ("Configuración", p["config"]),
        ("Entrega", p["entrega"]), ("Revisión MD5", p["revision"]), ("Comprobado UTC", p["comprobado_utc"])])
    medidas = "".join(f'<p data-medida="{k}" data-valor="{escape(str(c[k]))}">{etiqueta}: {escape(str(c[k]))}</p>' for k, etiqueta in [
        ("estado", "Estado"), ("creditos_universo", "Créditos del universo"), ("saldo_universo_mxn", "Saldo del universo MXN"),
        ("creditos_seleccion", "Créditos seleccionados"), ("saldo_seleccion_mxn", "Saldo seleccionado MXN"),
        ("porcentaje_creditos", "Cobertura de créditos %")])
    filas = p["seleccion"]
    tabla = '<div style="overflow-x:auto"><table><caption>Selección comprobada, saldos en MXN</caption><thead><tr><th scope="col">ID</th><th scope="col">Segmento</th><th scope="col">Corte</th><th scope="col">Saldo MXN</th></tr></thead><tbody>'
    tabla += "".join('<tr>' + "".join(f'<td>{escape(str(f[k]))}</td>' for k in ("id_credito", "segmento", "fecha_corte", "saldo_mxn")) + '</tr>' for f in filas)
    tabla += '</tbody></table></div>'
    if not filas:
        figura = '<p>Selección vacía sobre universo válido: no hay barras.</p>'
    else:
        maximo = max(1, *(int(f["saldo_mxn"]) for f in filas))
        barras = []
        for f in filas:
            ancho = 100 * int(f["saldo_mxn"]) // maximo
            barras.append(f'<p>{f["id_credito"]}: {f["saldo_mxn"]} MXN</p><div data-id="{f["id_credito"]}" data-saldo="{f["saldo_mxn"]}" style="width:{ancho}%;height:24px;background:#225ea8"></div>')
        figura = '<div role="img" aria-label="Saldo seleccionado por crédito en MXN; valores en la tabla" style="width:100%;max-width:600px">' + ''.join(barras) + '</div>'
    return '<!-- inicio-vista-1407 -->\n<section><h2>Consulta aplicada</h2>' + encabezado + medidas + figura + tabla + '</section>\n<!-- fin-vista-1407 -->'


def carpeta_reporte(nombre):
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,39}", nombre):
        raise ValueError("Reporte: nombre simple nuevo de hasta 40 caracteres")
    padre = RAIZ / "reportes"
    if padre.is_symlink() or (padre.exists() and padre.resolve() != padre):
        raise ValueError("Carpeta reportes enlazada")
    ruta = padre / nombre
    if ruta.is_symlink():
        raise ValueError("Reporte enlazado")
    return ruta


def documento(p):
    return '''---
title: "Consulta de cartera: reporte integrado"
format:
  html:
    embed-resources: true
execute:
  enabled: false
  freeze: false
  cache: false
---

Fotografía de una entrega comprobada. Cambiar datos o filtros exige preparar
otra entrega y otro reporte. La fecha de comprobación no es la fecha del corte.

''' + '```{=html}\n' + vista(p) + '\n```\n\nMD5 compara bytes; no autentica la entrega ni la sesión.\n'


def normalizar_html(texto):
    # Quarto 1.9.38 añade estas decoraciones y espacios al HTML preparado.
    # Se conservan valores, etiquetas, geometría y demás atributos.
    for atributo in [' class="anchored"', ' class="caption-top table"', ' class="caption-top"', ' class="header"',
                     ' class="odd"', ' class="even"', ' data-quarto-table-cell-role="th"']:
        texto = texto.replace(atributo, "")
    texto = texto.replace("viewBox=", "viewbox=")
    texto = re.sub(r"\s+/>", "/>", texto)
    texto = re.sub(r">\s+", ">", texto)
    return re.sub(r"\s+<", "<", texto)


def generar(nombre, archivo="config/octubre.csv", app="streamlit"):
    verificar_entorno()
    p = cargar(archivo, app)
    carpeta = carpeta_reporte(nombre)
    carpeta.parent.mkdir(exist_ok=True)
    carpeta.mkdir(exist_ok=False)
    with (carpeta / "producto.csv").open("x", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["clave", "valor"])
        w.writerows((k, p[k]) for k in ("config", "entrega", "revision", "comprobado_utc"))
    for nombre_tabla in ("seleccion.csv", "contexto.csv"):
        shutil.copyfile(RAIZ / p["entrega"] / nombre_tabla, carpeta / nombre_tabla)
    (carpeta / "reporte.qmd").write_text(documento(p), encoding="utf-8")
    print("Reporte preparado, falta renderizar:", carpeta)
    return carpeta


def verificar(nombre, archivo="config/octubre.csv", app="streamlit", exigir_html=True):
    p = cargar(archivo, app)
    carpeta = carpeta_reporte(nombre)
    columnas, filas = leer(carpeta / "producto.csv")
    claves = ["config", "entrega", "revision", "comprobado_utc"]
    if columnas != ["clave", "valor"] or [f["clave"] for f in filas] != claves:
        raise ValueError("Metadatos del reporte invalidos")
    meta = {f["clave"]: f["valor"] for f in filas}
    instante = datetime.strptime(meta["comprobado_utc"], "%Y-%m-%dT%H:%M:%SZ")
    if instante.strftime("%Y-%m-%dT%H:%M:%SZ") != meta["comprobado_utc"]:
        raise ValueError("Hora de comprobacion no canonica")
    if any(meta[k] != p[k] for k in claves if k != "comprobado_utc"):
        raise ValueError("Reporte de otra entrega/configuracion; conservar como historico")
    p["comprobado_utc"] = meta["comprobado_utc"]
    for nombre_tabla in ("seleccion.csv", "contexto.csv"):
        if leer(carpeta / nombre_tabla) != leer(RAIZ / p["entrega"] / nombre_tabla):
            raise ValueError("Tabla del reporte distinta de la entrega")
    if (carpeta / "reporte.qmd").read_text(encoding="utf-8") != documento(p):
        raise ValueError("Fuente del reporte alterada")
    if exigir_html:
        texto = (carpeta / "reporte.html").read_text(encoding="utf-8")
        fragmentos = re.findall(r"<!-- inicio-vista-1407 -->.*?<!-- fin-vista-1407 -->", texto, re.S)
        if len(fragmentos) != 1 or normalizar_html(fragmentos[0]) != normalizar_html(vista(p)):
            raise ValueError("HTML sin la vista esperada; renderizar en carpeta nueva")
    return p


def renderizar(nombre, archivo="config/octubre.csv", app="streamlit", quarto=None):
    verificar(nombre, archivo, app, exigir_html=False)
    carpeta = carpeta_reporte(nombre)
    if (carpeta / "reporte.html").exists():
        raise ValueError("HTML ocupado; conserva el reporte y usa otro nombre")
    ejecutable = quarto or shutil.which("quarto")
    if not ejecutable:
        candidato = Path("C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe")
        ejecutable = str(candidato) if candidato.is_file() else None
    if not ejecutable:
        raise ValueError("Quarto ausente: indicar --quarto; no se instala automaticamente")
    subprocess.run([ejecutable, "render", "reporte.qmd"], cwd=carpeta, check=True)
    verificar(nombre, archivo, app)
    print("HTML renderizado y conciliado:", carpeta / "reporte.html")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("accion", choices=["generar", "renderizar", "verificar"])
    p.add_argument("nombre")
    p.add_argument("--config", default="config/octubre.csv")
    p.add_argument("--app", choices=["streamlit", "shiny"], default="streamlit")
    p.add_argument("--quarto")
    a = p.parse_args()
    if a.quarto and a.accion != "renderizar":
        p.error("--quarto solo corresponde a renderizar")
    if a.accion == "generar": generar(a.nombre, a.config, a.app)
    elif a.accion == "renderizar": renderizar(a.nombre, a.config, a.app, a.quarto)
    else: verificar(a.nombre, a.config, a.app); print("Reporte conciliado")

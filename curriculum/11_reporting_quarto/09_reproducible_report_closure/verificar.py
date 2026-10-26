"""Verificar una entrega 11.09 contra referencia externa, sin escribir ni renderizar."""
import argparse
import base64
import csv
from datetime import date
from decimal import Decimal
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re


def objeto(pares):
    d = {}
    for k, v in pares:
        if k in d:
            raise ValueError(f"Clave JSON repetida: {k}")
        d[k] = v
    return d


def leer_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=objeto)


def parametros(fecha, minimo):
    if type(fecha) is not str or re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha) is None:
        raise ValueError("Fecha ISO textual requerida")
    if not 1900 <= date.fromisoformat(fecha).year <= 2100:
        raise ValueError("Fecha fuera de 1900–2100")
    if (type(minimo) not in (int, float) or not 0 <= minimo <= 1000000 or minimo != int(minimo)):
        raise ValueError("Mínimo numérico entero de 0 a 1000000; no booleano")
    if fecha not in ["2026-09-30", "2026-10-31"]:
        raise ValueError("Corte no disponible")
    return {"fecha_corte": fecha, "minimo_mxn": int(minimo)}


def leer_parametros(path):
    p = leer_json(path)
    if type(p) is not dict or set(p) != {"fecha_corte", "minimo_mxn"}:
        raise ValueError("Se requieren exactamente fecha_corte y minimo_mxn")
    return parametros(p["fecha_corte"], p["minimo_mxn"])


def leer_csv(path):
    esperadas = {(i, f) for i in ["001", "002", "003"] for f in ["2026-09-30", "2026-10-31"]}
    esperadas.add(("004", "2026-10-31"))
    valores = {}
    with Path(path).open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["credito_id", "fecha_corte", "saldo_mxn"]:
            raise ValueError("Columnas distintas del contrato")
        for fila in lector:
            clave = fila["credito_id"], fila["fecha_corte"]
            saldo = fila["saldo_mxn"]
            if (None in fila or clave not in esperadas or clave in valores or saldo is None
                    or re.fullmatch(r"0|[1-9][0-9]{0,6}", saldo) is None or int(saldo) > 1000000):
                raise ValueError("Clave o saldo inválido/repetido en la fuente completa")
            valores[clave] = int(saldo)
    if set(valores) != esperadas:
        raise ValueError("Falta cobertura: siete observaciones requeridas")
    return valores


def referencia(path, p):
    valores = leer_csv(path)
    filas = [(i, s, s >= p["minimo_mxn"]) for (i, f), s in sorted(valores.items()) if f == p["fecha_corte"]]
    seleccion = [(i, s) for i, s, cumple in filas if cumple]
    r = {**p, "universo_n": len(filas), "universo_mxn": sum(s for _, s, _ in filas),
         "seleccion_n": len(seleccion), "seleccion_mxn": sum(s for _, s in seleccion),
         "proporcion": f"{100 * len(seleccion) / len(filas):.2f}%"}
    return valores, filas, r


def fuentes(motor):
    comunes = ["_quarto.yml", "cartera.csv", "parametros.json", "reporte.qmd", "estilos.css", "README.md", "verificar.py", "copiar_fuentes.py"]
    if motor == "python":
        return comunes + ["analisis.py", "construir.py", "pyproject.toml", "uv.lock"]
    if motor == "r":
        return comunes + ["analisis.R", "construir.R", ".Rprofile", "renv/activate.R", "renv/settings.json",
                          "restaurar.R", "DESCRIPTION", "renv.lock", "cierre.Rproj"]
    raise ValueError("Motor desconocido")


def archivos(motor):
    return fuentes(motor) + ["reporte.html", "salida/detalle.csv", "salida/resumen.csv", "salida/barras.csv",
                            "salida/figura.png", "salida/metadatos.json", "render.log", "comando.txt"]


def huellas(raiz, motor):
    return {n: hashlib.md5((Path(raiz) / n).read_bytes()).hexdigest() for n in archivos(motor)}


class HTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texto, self.tablas, self.imagenes, self.enlaces, self.recursos = [], [], [], [], []
        self.ids = set()
        self.tabla = self.fila = self.celda = None
        self.omitir = 0
        self.idioma = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ["script", "style"]:
            self.omitir += 1
        if tag == "html":
            self.idioma = a.get("lang")
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.enlaces.append(a["href"][1:])
        if tag == "img":
            self.imagenes.append(a)
        if tag in ["img", "script", "link"]:
            recurso = a.get("href") if tag == "link" else a.get("src")
            if recurso:
                self.recursos.append(recurso)
        if tag == "table":
            self.tabla = []
        elif tag == "tr" and self.tabla is not None:
            self.fila = []
        elif tag in ["th", "td"] and self.fila is not None:
            self.celda = []

    def handle_data(self, data):
        if not self.omitir:
            self.texto.append(data)
            if self.celda is not None:
                self.celda.append(data)

    def handle_endtag(self, tag):
        if tag in ["script", "style"]:
            self.omitir = max(0, self.omitir - 1)
        if tag in ["td", "th"] and self.celda is not None:
            self.fila.append(" ".join("".join(self.celda).split()))
            self.celda = None
        elif tag == "tr" and self.fila is not None:
            self.tabla.append(self.fila)
            self.fila = None
        elif tag == "table" and self.tabla is not None:
            self.tablas.append(self.tabla)
            self.tabla = None


def tabla_csv(path, columnas):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        if lector.fieldnames != columnas:
            raise ValueError(f"Columnas de salida incorrectas: {Path(path).name}")
        filas = list(lector)
        if any(None in r or any(v is None for v in r.values()) for r in filas):
            raise ValueError("Campos de salida incompletos")
        return filas


def verificar(raiz, externa, fecha, minimo):
    raiz = Path(raiz)
    p = parametros(fecha, minimo)
    valores, filas, r = referencia(externa, p)
    if leer_parametros(raiz / "parametros.json") != p or leer_csv(raiz / "cartera.csv") != valores:
        raise ValueError("Fuente o parámetros distintos de la referencia externa esperada")
    meta = leer_json(raiz / "salida/metadatos.json")
    if (type(meta) is not dict or set(meta) != {"motor", "version_motor", "version_grafica", "fecha_corte", "minimo_mxn"}
            or meta["motor"] not in ["python", "r"] or meta["fecha_corte"] != fecha
            or type(meta["minimo_mxn"]) is not int or meta["minimo_mxn"] != p["minimo_mxn"]
            or not all(type(meta[k]) is str and re.fullmatch(r"[0-9]+(?:\.[0-9A-Za-z-]+)+", meta[k])
                       for k in ["version_motor", "version_grafica"])):
        raise ValueError("Metadatos de ejecución incompletos o incoherentes")
    if leer_json(raiz / "huellas.json") != huellas(raiz, meta["motor"]):
        raise ValueError("Inventario o huellas distintos de los archivos actuales")
    detalle = [[i, fecha, str(s), "si" if c else "no"] for i, s, c in filas]
    d = tabla_csv(raiz / "salida/detalle.csv", ["credito_id", "fecha_corte", "saldo_mxn", "seleccionado"])
    if [list(x.values()) for x in d] != detalle:
        raise ValueError("Detalle CSV distinto por clave, valor u orden")
    columnas = ["fecha_corte", "minimo_mxn", "universo_n", "universo_mxn", "seleccion_n", "seleccion_mxn", "proporcion"]
    if tabla_csv(raiz / "salida/resumen.csv", columnas) != [{k: str(r[k]) for k in columnas}]:
        raise ValueError("Resumen CSV distinto de la referencia")
    barras = tabla_csv(raiz / "salida/barras.csv", ["grupo", "altura", "etiqueta"])
    if len(barras) != 2:
        raise ValueError("Se requieren dos barras")
    for x, grupo, altura in zip(barras, ["universo", "seleccion"], [r["universo_mxn"], r["seleccion_mxn"]]):
        if (x["grupo"] != grupo or not Decimal(x["altura"]).is_finite()
                or Decimal(x["altura"]) != altura or x["etiqueta"] != str(altura)):
            raise ValueError("Descriptor de barras distinto del cálculo esperado")
    html = HTML()
    html.feed((raiz / "reporte.html").read_text(encoding="utf-8"))
    indicadores = [["Fecha de corte", fecha], ["Mínimo (MXN)", str(p["minimo_mxn"])],
                   ["Créditos del universo", str(r["universo_n"])], ["Saldo del universo (MXN)", str(r["universo_mxn"])],
                   ["Créditos seleccionados", str(r["seleccion_n"])], ["Saldo seleccionado (MXN)", str(r["seleccion_mxn"])],
                   ["Proporción de créditos", r["proporcion"]]]
    if (len(html.tablas) != 2 or html.tablas[0][1:] != indicadores
            or html.tablas[1][1:] != [[i, str(s), "sí" if c else "no"] for i, s, c in filas]):
        raise ValueError("Tablas HTML distintas de los valores esperados")
    frase = f"Corte {fecha}; mínimo {p['minimo_mxn']} MXN. Universo: {r['universo_n']} créditos / {r['universo_mxn']} MXN. Selección: {r['seleccion_n']} créditos / {r['seleccion_mxn']} MXN. Proporción: {r['proporcion']}."
    if frase not in " ".join(" ".join(html.texto).split()):
        raise ValueError("Narrativa desactualizada")
    if (html.idioma != "es" or not {"TOC", "parametros", "detalle", "figura", "limites", "reconstruccion"} <= html.ids
            or any(e and e not in html.ids for e in html.enlaces) or len(html.imagenes) != 1
            or not html.imagenes[0].get("alt", "").strip() or any(not x.startswith("data:") for x in html.recursos)):
        raise ValueError("Revisar idioma, navegación, figura o recursos incorporados")
    src = html.imagenes[0].get("src", "")
    if not src.startswith("data:image/png;base64,") or base64.b64decode(src.split(",", 1)[1]) != (raiz / "salida/figura.png").read_bytes():
        raise ValueError("PNG entregado e imagen HTML distintos")
    print(f"Entrega conciliada: {fecha}, {r['universo_mxn']}/{r['seleccion_mxn']} MXN, {r['seleccion_n']} seleccionados.")
    print("Huellas y registros no autentican sesiones; revisar también figura, teclado y argumento.")
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrega", type=Path)
    parser.add_argument("referencia", type=Path)
    parser.add_argument("--fecha", required=True)
    parser.add_argument("--minimo", type=int, required=True)
    args = parser.parse_args()
    verificar(args.entrega, args.referencia, args.fecha, args.minimo)

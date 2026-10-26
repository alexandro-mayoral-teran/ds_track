"""Contrastar cifras, tablas y estructura HTML con el CSV actual, sin escribir."""
import argparse
import csv
from html.parser import HTMLParser
from pathlib import Path


class Reporte(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.enlaces = []
        self.imagenes = []
        self.regiones = []
        self.tablas = []
        self.texto = []
        self.idioma = None
        self.tabla = self.fila = self.celda = None
        self.omitir = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.omitir += 1
        if tag == "html":
            self.idioma = a.get("lang")
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.enlaces.append(a["href"][1:])
        if tag == "img":
            self.imagenes.append(a)
        if "tabla-ancha" in a.get("class", "").split():
            self.regiones.append(a)
        if tag == "table":
            self.tabla = []
        elif tag == "tr" and self.tabla is not None:
            self.fila = []
        elif tag in ("td", "th") and self.fila is not None:
            self.celda = []

    def handle_data(self, data):
        if self.omitir:
            return
        self.texto.append(data)
        if self.celda is not None:
            self.celda.append(data)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.omitir = max(0, self.omitir - 1)
        if tag in ("td", "th") and self.celda is not None:
            self.fila.append(" ".join("".join(self.celda).split()))
            self.celda = None
        elif tag == "tr" and self.fila is not None:
            self.tabla.append(self.fila)
            self.fila = None
        elif tag == "table" and self.tabla is not None:
            self.tablas.append(self.tabla)
            self.tabla = None


def verificar(origen: Path, html: Path) -> None:
    # Reutilizar el contrato de 11.03; reconstruir la referencia numérica
    # directamente desde el CSV, sin ejecutar el reporte ni sus funciones locales.
    funcion = Path(__file__).resolve().parent.parent / "03_execution_python_r/analisis.py"
    namespace = {}
    exec(compile(funcion.read_text(encoding="utf-8"), str(funcion), "exec"), namespace)
    namespace["analizar"](origen)
    with origen.open(encoding="utf-8", newline="") as archivo:
        valores = {(f["credito_id"], f["fecha_corte"]): int(f["saldo_mxn"])
                   for f in csv.DictReader(archivo)}
    pares = [(i, valores[i, "2026-09-30"], valores[i, "2026-10-31"])
             for i in ["001", "002", "003"]]
    a, b = sum(x for _, x, _ in pares), sum(y for _, _, y in pares)
    tasa = f"{100 * (b-a) / a:.2f}%" if a else "no definida (base inicial cero)"
    resumen = [str(a), str(b), str(b-a), tasa]
    detalle = [[i, "2026-09-30", str(x), "2026-10-31", str(y), str(y-x)]
               for i, x, y in pares]
    r = Reporte()
    r.feed(html.read_text(encoding="utf-8"))
    if len(r.tablas) != 2 or r.tablas[0][1:] != [resumen] or r.tablas[1][1:] != detalle:
        raise ValueError("Tablas distintas del CSV actual: revisar cada crédito y el resumen")
    texto = " ".join(" ".join(r.texto).split())
    frases = [f"El saldo pasó de {a} MXN a {b} MXN",
              f"la diferencia octubre menos septiembre es {b-a} MXN",
              f"Variación sobre septiembre: {tasa}"]
    if not all(f in texto for f in frases):
        raise ValueError("La narrativa no coincide con las cifras actuales")
    requeridos = {"hallazgo", "resumen", "detalle", "figura", "limites", "revision",
                  "tbl-resumen", "tbl-detalle", "fig-saldos", "TOC"}
    if not requeridos <= r.ids or any(e and e not in r.ids for e in r.enlaces):
        raise ValueError("Falta navegación o existe una referencia interna sin destino")
    if any(m in texto for m in ["@tbl-resumen", "@tbl-detalle", "@fig-saldos"]):
        raise ValueError("Quedaron referencias sin resolver")
    if r.idioma != "es" or len(r.imagenes) != 1:
        raise ValueError("Revisar idioma o figura del reporte")
    if not r.imagenes[0].get("alt", "").strip() or not r.imagenes[0].get("src", "").startswith("data:image/png;base64,"):
        raise ValueError("Falta alternativa textual o PNG incorporado")
    if (len(r.regiones) != 1 or r.regiones[0].get("role") != "region"
            or r.regiones[0].get("tabindex") != "0" or not r.regiones[0].get("aria-label")):
        raise ValueError("La tabla ancha requiere región nombrada y foco por teclado")
    print(f"Texto y tablas conciliados: {a}/{b} MXN; diferencia {b-a}; tasa {tasa}.")
    print("Estructura y recursos básicos presentes; revisar visualmente figura, foco y desplazamiento.")
    print("No certifica alturas de barras, CSS, accesibilidad completa ni frescura de una ejecución.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("origen", type=Path)
    parser.add_argument("html", type=Path)
    args = parser.parse_args()
    verificar(args.origen, args.html)

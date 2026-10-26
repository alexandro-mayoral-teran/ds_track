"""Verificar tarjetas, tabla y estructura del dashboard contra CSV, sin escribir."""
import argparse
import csv
import importlib.util
from pathlib import Path


base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("estructura_1107", base.parent / "07_formats_visual_review/verificar.py")
estructura = importlib.util.module_from_spec(spec)
spec.loader.exec_module(estructura)


class Dashboard(estructura.Reporte):
    def __init__(self):
        super().__init__()
        self.titulos = []
        self.valores = []
        self.tabs = []
        self.recursos = []
        self.region = []
        self.captura = None

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        a = dict(attrs)
        clases = a.get("class", "").split()
        if tag == "p" and "value-box-title" in clases:
            self.captura = (self.titulos, [])
        elif tag == "p" and "value-box-value" in clases:
            self.captura = (self.valores, [])
        if a.get("role") == "tab":
            self.tabs.append(a.get("data-value"))
        if "tabla-desplazable" in clases:
            self.region.append(a)
        if tag in ("script", "img", "link"):
            recurso = a.get("src") if tag != "link" else a.get("href")
            if recurso:
                self.recursos.append(recurso)

    def handle_data(self, data):
        super().handle_data(data)
        if self.captura is not None and not self.omitir:
            self.captura[1].append(data)

    def handle_endtag(self, tag):
        if tag == "p" and self.captura is not None:
            lista, partes = self.captura
            lista.append(" ".join("".join(partes).split()))
            self.captura = None
        super().handle_endtag(tag)


def verificar(origen: Path, html: Path) -> None:
    funcion = base.parent / "03_execution_python_r/analisis.py"
    namespace = {}
    exec(compile(funcion.read_text(encoding="utf-8"), str(funcion), "exec"), namespace)
    namespace["analizar"](origen)
    with origen.open(encoding="utf-8", newline="") as f:
        valores = {(r["credito_id"], r["fecha_corte"]): int(r["saldo_mxn"]) for r in csv.DictReader(f)}
    pares = [(i, valores[i, "2026-09-30"], valores[i, "2026-10-31"]) for i in ["001", "002", "003"]]
    a, b = sum(x for _, x, _ in pares), sum(y for _, _, y in pares)
    tasa = f"{100 * (b-a) / a:.2f}%" if a else "no definida (base inicial cero)"
    lector = Dashboard()
    lector.feed(html.read_text(encoding="utf-8"))
    if lector.titulos != ["Septiembre (MXN)", "Octubre (MXN)", "Diferencia octubre menos septiembre (MXN)"]:
        raise ValueError("Títulos de tarjetas distintos de los cortes y unidad previstos")
    if lector.valores != [str(a), str(b), str(b-a)]:
        raise ValueError("Tarjetas distintas del CSV actual")
    detalle = [[i, str(x), str(y), str(y-x)] for i, x, y in pares]
    if len(lector.tablas) != 1 or lector.tablas[0][1:] != detalle:
        raise ValueError("El detalle no conserva cada saldo, ID y diferencia actuales")
    texto = " ".join(" ".join(lector.texto).split())
    if f"Variación sobre septiembre: {tasa}" not in texto:
        raise ValueError("Tasa distinta del cálculo actual")
    if lector.tabs != ["Figura", "Detalle"] or any(e and e not in lector.ids for e in lector.enlaces):
        raise ValueError("Pestañas o destinos internos incompletos")
    if lector.idioma != "es" or len(lector.imagenes) != 1 or not lector.imagenes[0].get("alt", "").strip():
        raise ValueError("Revisar idioma o alternativa de la figura")
    if any(not r.startswith("data:") for r in lector.recursos):
        raise ValueError("Hay recursos de lectura no incorporados; no basta copiar solo el HTML")
    if (len(lector.region) != 1 or lector.region[0].get("tabindex") != "0"
            or lector.region[0].get("role") != "region" or not lector.region[0].get("aria-label")):
        raise ValueError("Falta región de detalle nombrada y alcanzable con teclado")
    print(f"Dashboard conciliado: {a}/{b} MXN; diferencia {b-a}; variación {tasa}.")
    print("Revisar también barras, pestañas, foco y copia final en navegador sin conexión.")
    print("No certifica accesibilidad completa, autenticidad ni nueva ejecución.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("origen", type=Path)
    parser.add_argument("html", type=Path)
    args = parser.parse_args()
    verificar(args.origen, args.html)

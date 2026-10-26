"""Contrastar el HTML con el CSV actual, sin renderizar ni escribir archivos."""
import argparse
import csv
from html.parser import HTMLParser
from pathlib import Path
import re


class Tablas(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tablas = []
        self.tabla = None
        self.fila = None
        self.celda = None
        self.texto = []

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.tabla = []
        elif tag == "tr" and self.tabla is not None:
            self.fila = []
        elif tag in ("td", "th") and self.fila is not None:
            self.celda = []

    def handle_data(self, data):
        self.texto.append(data)
        if self.celda is not None:
            self.celda.append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.celda is not None:
            self.fila.append(" ".join("".join(self.celda).split()))
            self.celda = None
        elif tag == "tr" and self.fila is not None:
            self.tabla.append(self.fila)
            self.fila = None
        elif tag == "table" and self.tabla is not None:
            self.tablas.append(self.tabla)
            self.tabla = None


def verificar(proyecto: Path, motor: str, fecha: str, minimo: int) -> None:
    # El contrato validado en 11.05 se reutiliza; el resumen de referencia se
    # reconstruye por separado desde el CSV y se compara con las celdas HTML.
    base = Path(__file__).resolve().parent
    namespace = {}
    anterior = base.parent / "05_parameters_cutoffs/analisis.py"
    exec(compile(anterior.read_text(encoding="utf-8"), str(anterior), "exec"), namespace)
    origen = proyecto / ("datos/cartera.csv" if motor == "python" else "datos/cartera_1106.csv")
    namespace["analizar"](origen, fecha, minimo)
    with origen.open(encoding="utf-8", newline="") as archivo:
        filas = sorted((f["credito_id"], int(f["saldo_mxn"]))
                       for f in csv.DictReader(archivo) if f["fecha_corte"] == fecha)
    seleccion = [(i, s) for i, s in filas if s >= minimo]
    esperado = (fecha, minimo, sum(s for _, s in filas),
                sum(s for _, s in seleccion), len(seleccion))
    html = proyecto / "output/1106_html/informes/reporte_1106.html"
    lector = Tablas()
    lector.feed(html.read_text(encoding="utf-8"))
    patron = (r"EVIDENCIA_1106\|fecha=([^|\s]+)\|minimo=(\d+)\|universo=(\d+)"
              r"\|seleccion=(\d+)\|n=(\d+)\|revision=(\d+)\|ejecucion=([^\s]+)")
    marcas = re.findall(patron, " ".join(lector.texto))
    if len(marcas) != 1:
        raise ValueError("Se requiere una evidencia de cálculo en el HTML")
    f, m, u, s, n, revision, token = marcas[0]
    if (f, int(m), int(u), int(s), int(n)) != esperado:
        raise ValueError("HTML desactualizado o parámetros distintos del CSV actual")
    detalle = [[i, str(s), "sí" if s >= minimo else "no"] for i, s in filas]
    if len(lector.tablas) != 1 or lector.tablas[0][1:] != detalle:
        raise ValueError("La tabla HTML no conserva cada valor/ID/condición actual")
    print(f"HTML conciliado: {len(filas)} filas; selección {len(seleccion)}/{esperado[3]} MXN.")
    print(f"Revisión mostrada: {revision}; identificador: {token}.")
    print("No acredita que la ejecución sea nueva ni autentica sesiones históricas.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proyecto", type=Path)
    parser.add_argument("--motor", choices=["python", "r"], required=True)
    parser.add_argument("--fecha", default="2026-09-30")
    parser.add_argument("--minimo", type=int, default=2000)
    args = parser.parse_args()
    verificar(args.proyecto, args.motor, args.fecha, args.minimo)

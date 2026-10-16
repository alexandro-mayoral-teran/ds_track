"""05.11: comprobar una entrega guardada sin modificarla ni regenerar figuras."""

import hashlib
from io import StringIO
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

import pandas as pd
from pandas.testing import assert_frame_equal

from .cierre import inspect_delivery
from .flujo import build_analysis
from .presentacion import medians_chart
from .recursos import read_json

TABLES = ["corte", "resumen", "referencia_csv", "indicadores", "conciliacion"]


def _read_table(path):
    # La unidad/claves del detalle son textuales; no perder ceros iniciales.
    return pd.read_csv(path, dtype={"id_credito": "string", "fecha_corte": "string"})


def verify_delivery(output: str | Path) -> dict:
    """Recalcular desde fuentes/ y contrastar cinco tablas y la especificación.

    Solo lectura: no cerrar carpetas incompletas ni corregir resultados. Exige
    cierre de 05.03, corte coherente, tablas CSV equivalentes al mismo ciclo de
    serialización, 20 conciliaciones y Altair igual al construido desde resumen.
    Comprueba tamaños declarados, cabecera/dimensiones PNG y estructura SVG.
    No evalúa visualmente una figura, no autentica al autor ni verifica todos los
    textos/HTML. Requiere el entorno compatible del curso. Lanza ValueError/OSError
    ante incompatibilidades; no considera suficiente que exista cierre.json.
    """
    output = Path(output)
    if inspect_delivery(output)["estado"] != "completada":
        raise ValueError("La carpeta no tiene un cierre completo de 05.03")
    marker = read_json(output / "cierre.json")
    metadata = read_json(output / "entrega.json")
    execution = read_json(output / "ejecucion.json")
    cut = marker["corte"]
    if (not isinstance(metadata, dict) or not isinstance(execution, dict)
            or not isinstance(execution.get("configuracion_efectiva"), dict)):
        raise ValueError("Estructura de metadatos/ejecución incompatible")
    if (metadata.get("corte") != cut or execution["configuracion_efectiva"].get("cut") != cut
            or marker["comprobaciones_datos"] != 20 or metadata.get("comprobaciones_datos") != 20
            or execution.get("comprobaciones_datos") != 20):
        raise ValueError("Corte o cantidad de comprobaciones incoherentes en los registros")
    # Utilizar SOLO las copias de la entrega, no la ruta original de ejecución.
    tables = build_analysis(output / "fuentes", cut)
    for name in TABLES:
        saved = _read_table(output / f"{name}.csv")
        # Comparar en la frontera CSV: índices no exportados y ausencias leídas
        # como en el archivo. Esto no acredita preservar tipos de Python en CSV.
        expected = _read_table(StringIO(tables[name].to_csv(index=False)))
        try:
            assert_frame_equal(saved, expected, check_exact=True)
        except AssertionError as exc:
            raise ValueError(f"La tabla {name}.csv difiere del recálculo") from exc
    if len(tables["conciliacion"]) != 20 or not tables["conciliacion"].coincide.all():
        raise ValueError("Conciliaciones insuficientes o fallidas")
    spec = read_json(output / "altair.json")
    if spec != medians_chart(tables["resumen"], cut).to_dict(validate=True):
        raise ValueError("La especificación Altair difiere del resumen recalculado")
    formats = pd.read_csv(output / "formatos.csv")
    if not {"archivo", "bytes", "ancho_px_esperado", "alto_px_esperado"}.issubset(formats.columns):
        raise ValueError("Columnas de formatos.csv incompatibles")
    if formats.archivo.tolist() != ["matplotlib.png", "matplotlib.svg"]:
        raise ValueError("Formatos de figura distintos de los esperados")
    for row in formats.itertuples(index=False):
        if (output / row.archivo).stat().st_size != row.bytes:
            raise ValueError("El tamaño de una figura difiere de formatos.csv")
    with (output / "matplotlib.png").open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("Cabecera PNG incompatible")
    width, height = struct.unpack(">II", header[16:24])
    png = formats.iloc[0]
    if width != png.ancho_px_esperado or height != png.alto_px_esperado:
        raise ValueError("Dimensiones PNG distintas de las declaradas")
    try:
        svg = ET.parse(output / "matplotlib.svg").getroot()
    except ET.ParseError as exc:
        raise ValueError("SVG no interpretable") from exc
    if svg.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("La raíz del archivo no es SVG")
    hashes = {name: hashlib.sha256((output / "fuentes" / name).read_bytes()).hexdigest()
              for name in ["creditos.csv", "cortes.csv"]}
    return {"estado": "verificada", "corte": cut, "tablas": len(TABLES),
            "conciliaciones": len(tables["conciliacion"]), "fuentes_sha256": hashes,
            "png_px": [width, height], "revision_visual": "Pendiente de quien revisa"}


def compare_deliveries(first: str | Path, second: str | Path) -> dict:
    """Verificar ambas carpetas y comparar corte, fuentes, tablas y spec Altair.

    No exige PNG/SVG idénticos byte a byte: metadatos y renderizado pueden variar.
    Las figuras estáticas de ambas entregas requieren revisión visual.
    """
    first, second = Path(first), Path(second)
    a, b = verify_delivery(first), verify_delivery(second)
    if a["corte"] != b["corte"] or a["fuentes_sha256"] != b["fuentes_sha256"]:
        raise ValueError("Las entregas no usan el mismo corte y fuentes")
    for name in TABLES:
        try:
            assert_frame_equal(_read_table(first / f"{name}.csv"),
                               _read_table(second / f"{name}.csv"), check_exact=True)
        except AssertionError as exc:
            raise ValueError(f"Reconstrucción diferente en {name}.csv") from exc
    if read_json(first / "altair.json") != read_json(second / "altair.json"):
        raise ValueError("Especificaciones distintas entre entregas")
    return {"estado": "reconstruccion_equivalente", "corte": a["corte"],
            "tablas": len(TABLES), "revision_visual": "Pendiente en ambas figuras"}

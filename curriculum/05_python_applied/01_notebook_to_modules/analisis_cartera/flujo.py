"""Coordinar funciones sin activar una lectura o exportación al importar."""

import json
from pathlib import Path
import shutil

import altair as alt
import matplotlib

from .entrada import read_detail
from .transformacion import summarize
from .comprobacion import reference, reconcile
from .presentacion import delivery_figure, save_variant, medians_chart, report


def build_analysis(source, cut="2026-10-31"):
    """Leer, transformar y conciliar; devolver tablas sin escribir entregas."""
    detail = read_detail(source)
    selected, summary = summarize(detail, cut)
    expected = reference(source, cut)
    totals, checks = reconcile(summary, selected, expected)
    return {"corte": selected, "resumen": summary, "referencia_csv": expected,
            "indicadores": totals, "conciliacion": checks}


def export(source, output, cut="2026-10-31", dpi=160):
    """Construir una entrega nueva; solo esta llamada escribe y dibuja."""
    import pandas as pd
    import matplotlib.pyplot as plt

    if isinstance(dpi, bool) or not isinstance(dpi, int) or dpi <= 0:
        raise ValueError("dpi debe ser un entero positivo")
    tables = build_analysis(source, cut)
    summary = tables["resumen"]
    chart = medians_chart(summary, cut)
    chart.to_dict(validate=True)
    # Una carpeta existente nunca se reinicia ni se sobrescribe.
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / "fuentes").mkdir()
    for name in ["creditos.csv", "cortes.csv"]:
        shutil.copyfile(Path(source) / name, output / "fuentes" / name)
    for name, table in tables.items():
        table.to_csv(output / f"{name}.csv", index=False)
    fig = delivery_figure(summary, cut)
    try:
        formats = [save_variant(fig, output, "matplotlib.png", dpi),
                   save_variant(fig, output, "matplotlib.svg")]
    finally:
        plt.close(fig)
    pd.DataFrame(formats).to_csv(output / "formatos.csv", index=False)
    chart.save(output / "altair.json")
    chart.save(output / "altair.html", embed_options={"actions": False, "renderer": "svg"})
    (output / "informe.md").write_text(report(summary, tables["indicadores"], cut), encoding="utf-8")
    instructions = "\n".join([
        "# Reconstruir la entrega de 05.01", "",
        "Conservar esta carpeta y el repositorio con el paquete de la lección.",
        "Desde 01_notebook_to_modules, activar el entorno elegido y usar:",
        "```python",
        "from analisis_cartera.flujo import export",
        f"export('output/entrega_modular/fuentes', 'output/reconstruccion', cut={cut!r}, dpi={dpi})",
        "```", "",
        "Este ejemplo supone la entrega inicial output/entrega_modular; adaptar la ruta si usaste otra.",
        "La carpeta de destino debe ser nueva. Revisar informe.md, figuras y tablas.",
        "Comparar valores, ausencias y bases con 04.09; no exigir imágenes idénticas en bytes.",
        "El HTML necesita conexión. Interacción y HTML incorporado se conservan en 04.08/04.09.",
        "Una interrupción puede dejar archivos parciales; entrega.json se escribe al terminar.", "",
    ])
    (output / "RECONSTRUIR.md").write_text(instructions, encoding="utf-8")
    metadata = {"corte": cut, "dpi_png": dpi, "html_inline": False, "interaccion": False,
                "versiones": {"pandas": pd.__version__, "matplotlib": matplotlib.__version__, "altair": alt.__version__},
                "fuentes": ["fuentes/creditos.csv", "fuentes/cortes.csv"],
                "comprobaciones_datos": len(tables["conciliacion"]),
                "revision_visual": "Pendiente de quien recibe la entrega"}
    (output / "entrega.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    return tables

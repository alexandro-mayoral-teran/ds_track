"""Componer vistas comprobadas y exportarlas sin sobrescribir entregas."""

import argparse
from pathlib import Path
import sys

import pandas as pd

HERE = Path(__file__).resolve().parent
# Reutilización del lector de 04.04; organización de paquetes pertenece a 05.
sys.path.insert(0, str(HERE.parent / "04_distributions_relationships"))
from distributions import read_detail, select_views, box_summary, GROUPS, SOURCE

DATES = ["2026-09-30", "2026-10-31"]
SIZE = (12, 5.5)


def money(value, position=None):
    # Una mediana de saldos enteros puede terminar en medio MXN; no redondearla a cero.
    formatted = f"{value:,.2f}".rstrip("0").rstrip(".")
    return formatted.replace(",", " ")


def summarize(detail, cut):
    selected, _, _, _ = select_views(detail, cut)
    summary = box_summary(selected)[["segmento", "registros", "conocidos", "mediana_mxn"]].copy()
    # Un grupo vacío no tiene un porcentaje de cobertura definido.
    denominator = summary.registros.where(summary.registros.gt(0))
    summary["cobertura_pct"] = 100 * summary.conocidos / denominator
    summary["fecha_corte"] = cut
    return selected, summary


def draw_medians(ax, summary, right, color="#2563eb", hatch="//"):
    from matplotlib.ticker import FuncFormatter
    indexed = summary.set_index("segmento").reindex(GROUPS)
    for position, row in enumerate(indexed.itertuples()):
        if pd.notna(row.mediana_mxn):
            bars = ax.barh(position, row.mediana_mxn, color=color,
                           edgecolor="#172554", hatch=hatch, height=.55)
            ax.bar_label(bars, labels=[f"{money(row.mediana_mxn)} · {row.conocidos}/{row.registros}"], padding=5, fontsize=10)
        else:
            label = "Sin registros" if row.registros == 0 else f"Sin mediana · 0/{row.registros}"
            ax.text(right * .015, position, label, va="center", fontsize=10)
    ax.set_yticks(range(len(GROUPS)), GROUPS)
    ax.set_ylim(len(GROUPS) - .6, -.6)
    ax.set_xlim(0, right)
    ax.set_xlabel("Mediana conocida (MXN) · etiqueta: valor y cobertura")
    ax.xaxis.set_major_formatter(FuncFormatter(money))
    ax.grid(axis="x", alpha=.2)
    ax.set_axisbelow(True)


def common_limit(summary):
    maximum = summary.mediana_mxn.max()
    return max(5000, float(maximum) * 1.5) if pd.notna(maximum) else 5000


def comparison_figure(comparison):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=SIZE, sharex=True, sharey=True,
                             layout="constrained")
    right = common_limit(comparison)
    for ax, cut, color, hatch in zip(axes, DATES, ["#2563eb", "#c2410c"], ["", "//"]):
        table = comparison.loc[comparison.fecha_corte.eq(cut)]
        draw_medians(ax, table, right, color, hatch)
        ax.set_title(cut, loc="left", pad=12)
        # sharey oculta etiquetas repetidas por defecto; aquí las mostramos.
        ax.tick_params(axis="y", labelleft=True)
    fig.suptitle("Dos cortes, una medida y límites comunes · datos sintéticos", fontsize=14)
    fig.supxlabel("Fuente: CSV de SQL 03.01 · disponibles por fecha; no siempre son los mismos créditos.\nUna categoría sin mediana conserva su posición; no se dibuja como cero.", fontsize=10)
    return fig


def delivery_figure(summary, cut, size=SIZE):
    import matplotlib.pyplot as plt
    # Se comparten categorías verticales; los ejes horizontales tienen unidades distintas.
    fig, axes = plt.subplots(1, 2, figsize=size, sharey=True, layout="constrained")
    draw_medians(axes[0], summary, common_limit(summary))
    axes[0].set_title("A · Mediana del saldo conocido", loc="left", pad=12)
    indexed = summary.set_index("segmento").reindex(GROUPS)
    for position, row in enumerate(indexed.itertuples()):
        if row.registros > 0:
            axes[1].scatter(row.cobertura_pct, position, marker="s", s=65, color="#0f766e")
            axes[1].annotate(f"{row.conocidos}/{row.registros}",
                             xy=(row.cobertura_pct, position), xytext=(8, 0),
                             textcoords="offset points", va="center", fontsize=10)
        else:
            axes[1].text(2, position, "Sin registros", va="center", fontsize=10)
    axes[1].set(title="B · Cobertura de saldo", xlabel="Saldos conocidos / registros (%)", xlim=(-5, 125))
    axes[1].set_xticks([0, 25, 50, 75, 100])
    axes[1].tick_params(axis="y", labelleft=True)
    axes[1].grid(axis="x", alpha=.2)
    axes[1].set_axisbelow(True)
    # La flecha apunta a una cobertura cero observada; no a una mediana inventada.
    education = indexed.loc["educacion"]
    if education.registros > 0 and education.conocidos == 0:
        axes[1].annotate("Hay registros,\nningún saldo conocido", xy=(0, GROUPS.index("educacion")),
                         xytext=(28, -42), textcoords="offset points", fontsize=10,
                         arrowprops={"arrowstyle": "->", "color": "#334155"},
                         bbox={"boxstyle": "round,pad=.3", "fc": "white", "ec": "#94a3b8"})
    total = int(summary.registros.sum())
    known = int(summary.conocidos.sum())
    fig.suptitle(f"Saldo conocido y cobertura · {cut} · datos sintéticos", fontsize=14)
    fig.supxlabel(f"Fuente: CSV de SQL 03.01 · {known}/{total} saldos conocidos. Mediana y cobertura son medidas distintas.\nNo inferir riesgo ni la ubicación de saldos ausentes a partir de estas vistas.", fontsize=10)
    return fig


def reading_note(summary, cut):
    lines = [f"# Lectura de la figura · {cut}", "",
             "Fuente: CSV sintéticos de SQL 03.01. Una observación por crédito y corte.", "",
             "| Segmento | Mediana conocida (MXN) | Saldos conocidos / registros |",
             "| --- | ---: | ---: |"]
    for row in summary.itertuples(index=False):
        value = money(row.mediana_mxn) if pd.notna(row.mediana_mxn) else "Sin mediana"
        lines.append(f"| {row.segmento} | {value} | {row.conocidos}/{row.registros} |")
    lines += ["", "El panel A representa medianas de valores conocidos; el B representa cobertura.",
              "Cero conocidos con registros es cobertura 0 %, pero no mediana cero.",
              "Sin registros no hay mediana ni porcentaje de cobertura definido.",
              "La comparación entre cortes describe bases disponibles; no acredita cambios de los mismos créditos.",
              "Los datos son ficticios y no permiten afirmar riesgo real ni causalidad.", ""]
    return "\n".join(lines)


def save_variant(fig, output, filename, dpi=None):
    import matplotlib
    path = output / filename
    options = {"facecolor": "white", "transparent": False,
               "metadata": {"Title": "DS Track: composición y exportación",
                            "Description": "Fuente: CSV sintéticos de SQL 03.01; revisar resumen y lectura.md."}}
    if dpi is not None:
        options["dpi"] = dpi
    # Evitar recorte automático para conservar dimensiones nominales comprobables.
    with matplotlib.rc_context({"savefig.bbox": None}):
        fig.savefig(path, **options)
    width, height = fig.get_size_inches()
    return {"archivo": filename, "formato": path.suffix[1:],
            "ancho_pulgadas": width, "alto_pulgadas": height,
            "dpi_png": dpi, "ancho_px_esperado": int(width * dpi) if dpi else None,
            "alto_px_esperado": int(height * dpi) if dpi else None,
            "bytes": path.stat().st_size}


def export(output, cut="2026-10-31", dpi=160, source=SOURCE):
    import matplotlib.pyplot as plt
    if isinstance(dpi, bool) or not isinstance(dpi, int) or dpi <= 0:
        raise ValueError("dpi debe ser un entero positivo")
    date = pd.to_datetime(cut, format="%Y-%m-%d", errors="raise")
    if date.strftime("%Y-%m-%d") != cut:
        raise ValueError("Usa fecha YYYY-MM-DD")
    detail = read_detail(source)
    selected, summary = summarize(detail, cut)
    comparison = pd.concat([summarize(detail, d)[1] for d in DATES], ignore_index=True)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, table in [("corte", selected), ("resumen", summary), ("comparacion", comparison)]:
        table.to_csv(output / f"{name}.csv", index=False)
    (output / "lectura.md").write_text(reading_note(summary, cut), encoding="utf-8")
    variants = []
    fig = delivery_figure(summary, cut)
    try:
        variants.append(save_variant(fig, output, f"entrega_{dpi}.png", dpi))
        variants.append(save_variant(fig, output, f"entrega_{dpi * 2}.png", dpi * 2))
        variants.append(save_variant(fig, output, "entrega.svg"))
    finally:
        plt.close(fig)
    fig = comparison_figure(comparison)
    try:
        variants.append(save_variant(fig, output, "comparacion.png", dpi))
    finally:
        plt.close(fig)
    pd.DataFrame(variants).to_csv(output / "formatos.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para la entrega")
    parser.add_argument("--cut", default="2026-10-31")
    parser.add_argument("--dpi", type=int, default=160, help="Resolución PNG; también exporta el doble")
    args = parser.parse_args()
    import matplotlib
    matplotlib.use("Agg")
    export(args.output, args.cut, args.dpi)

"""Revisar escalas y etiquetas sin cambiar las observaciones originales."""

import argparse
import math
from pathlib import Path
import sys

import pandas as pd

HERE = Path(__file__).resolve().parent
# Reutilización interna del ejemplo anterior; no requiere instalar un paquete.
sys.path.insert(0, str(HERE.parent / "04_distributions_relationships"))
from distributions import read_detail, select_views, box_summary, GROUPS, SOURCE


def money(value, position=None):
    """Formato de lectura: espacios entre miles; el dato no se transforma."""
    return f"{value:,.0f}".replace(",", " ")


def log_partition(selected):
    """Todo registro conserva su destino y motivo antes de dibujar log."""
    result = selected.copy()
    result["estado_log"] = "positivo"
    result.loc[result.saldo_mxn.isna(), "estado_log"] = "ausente"
    result.loc[result.saldo_mxn.eq(0).fillna(False), "estado_log"] = "cero"
    result.loc[result.saldo_mxn.lt(0).fillna(False), "estado_log"] = "negativo"
    known = result.saldo_mxn.dropna().astype(float)
    if not known.map(math.isfinite).all():
        raise ValueError("Saldo no finito")
    positive = result.loc[result.estado_log.eq("positivo")].copy()
    excluded = result.loc[~result.estado_log.eq("positivo")].copy()
    if len(positive) + len(excluded) != len(selected):
        raise ValueError("La partición logarítmica no concilia")
    return positive, excluded


def axis_style(ax):
    from matplotlib.ticker import FuncFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    ax.grid(axis="y", alpha=.2)
    ax.set_axisbelow(True)


def baseline_figure(stats, cut):
    import matplotlib.pyplot as plt
    # Dos medianas conocidas de los mismos grupos, sin cambiar sus valores.
    part = stats.set_index("segmento").reindex(["comercio", "consumo"])
    values = part.mediana_mxn.astype(float)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), layout="constrained")
    valid = values.notna()
    for ax, title in zip(axes, ["Ejemplo a corregir: barras recortadas", "Revisión: longitud desde cero"]):
        bars = ax.bar([i for i, ok in enumerate(valid) if ok], values[valid],
                      color="#2563eb", edgecolor="#172554")
        ax.bar_label(bars, labels=[money(v) for v in values[valid]], padding=5)
        ax.set_xticks([0, 1], ["comercio", "consumo"])
        ax.set(title=title, ylabel="Mediana del saldo conocido (MXN)")
        for i, ok in enumerate(valid):
            if not ok:
                ax.text(i, .12, "Sin saldos conocidos", transform=ax.get_xaxis_transform(), ha="center", fontsize=9)
        axis_style(ax)
    if valid.any():
        upper = max(3000, float(values[valid].max()) * 1.2)
        # El panel izquierdo es deliberadamente problemático y está identificado.
        axes[0].set_ylim(max(0, float(values[valid].min()) - 150), upper)
        axes[1].set_ylim(0, upper)
    else:
        for ax in axes:
            ax.set_ylim(0, 3000)
    coverage = " · ".join(f"{g}: {int(r.conocidos)}/{int(r.registros)}" for g, r in part.iterrows())
    fig.suptitle(f"Mismos datos, distinta impresión · {cut}\n{coverage} · datos sintéticos", fontsize=12)
    return fig


def log_figure(selected, positive, excluded, cut):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), layout="constrained")
    positions = list(range(len(selected)))
    values = selected.saldo_mxn.astype(float)
    known = values.notna()
    axes[0].scatter([i for i, ok in zip(positions, known) if ok], values[known], color="#2563eb", marker="o")
    if not known.any() and not selected.empty:
        axes[0].text(.5, .5, "Sin saldos conocidos", transform=axes[0].transAxes, ha="center")
    lookup = {credit: i for i, credit in enumerate(selected.id_credito)}
    axes[1].set_yscale("log", base=10)
    if positive.empty:
        axes[1].text(.5, .5, "Sin saldos positivos", transform=axes[1].transAxes, ha="center")
    else:
        axes[1].scatter([lookup[c] for c in positive.id_credito], positive.saldo_mxn.astype(float), color="#2563eb", marker="o")
    axes[0].set_ylim(0, max(4000, float(values[known].max()) * 1.1) if known.any() else 4000)
    # Los mismos límites log en cada ejecución hacen explícito el dominio.
    lower = min(100, float(positive.saldo_mxn.min()) / 1.2) if not positive.empty else 100
    upper = max(10000, float(positive.saldo_mxn.max()) * 1.2) if not positive.empty else 10000
    axes[1].set_ylim(lower, upper)
    for ax, title in zip(axes, [f"Lineal: {int(known.sum())} saldos conocidos", f"Log base 10: {len(positive)} saldos positivos"]):
        ax.set(title=title, xlabel="Crédito (posición común; sin orden temporal)", ylabel="Saldo (MXN)")
        ax.set_xticks(positions, [str(c).removeprefix("CR-") for c in selected.id_credito], rotation=90, fontsize=8)
        axis_style(ax)
        if selected.empty:
            ax.text(.5, .35, "Corte sin registros", transform=ax.transAxes, ha="center")
    counts = excluded.estado_log.value_counts()
    fig.suptitle(f"{cut} · log excluye {counts.get('cero', 0)} ceros, {counts.get('ausente', 0)} ausentes y {counts.get('negativo', 0)} negativos\nSin sumar 1 ni reemplazar valores · datos sintéticos", fontsize=12)
    return fig


def labels_figure(stats, cut):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    fig, ax = plt.subplots(figsize=(11, 5), layout="constrained")
    indexed = stats.set_index("segmento").reindex(GROUPS)
    for i, (group, row) in enumerate(indexed.iterrows()):
        if row.conocidos:
            bars = ax.barh(i, row.mediana_mxn, color="#2563eb", edgecolor="#172554", hatch="//")
            ax.bar_label(bars, labels=[f"{money(row.mediana_mxn)} MXN · {int(row.conocidos)}/{int(row.registros)} conocidos"], padding=5, fontsize=10)
        else:
            ax.text(50, i, f"Sin mediana · 0/{int(row.registros)} conocidos", va="center")
    maximum = indexed.mediana_mxn.max()
    ax.set_xlim(0, max(4600, float(maximum) * 1.8) if pd.notna(maximum) else 4600)
    ax.set_yticks(range(len(GROUPS)), GROUPS)
    ax.set_ylim(len(GROUPS) - .6, -.6)
    ax.set(title=f"Mediana del saldo conocido por segmento · {cut}\nFuente: CSV de SQL 03.01 · datos sintéticos", xlabel="Mediana (MXN); etiqueta: valor y cobertura")
    ax.xaxis.set_major_formatter(FuncFormatter(money))
    ax.grid(axis="x", alpha=.2)
    ax.set_axisbelow(True)
    return fig


def signals_figure(detail):
    import matplotlib.pyplot as plt
    dates = sorted(detail.fecha_corte.unique())
    if dates != ["2026-09-30", "2026-10-31"]:
        raise ValueError("La comparación requiere los dos cortes originales")
    fig, ax = plt.subplots(figsize=(11, 5), layout="constrained")
    styles = [("#2563eb", "o"), ("#c2410c", "s")]
    for date, (color, marker) in zip(dates, styles):
        selected, _, _, _ = select_views(detail, date)
        stats = box_summary(selected).set_index("segmento").reindex(GROUPS)
        values = stats.mediana_mxn.astype(float)
        # NaN conserva el hueco de educación; no lo reemplazamos por cero.
        ax.plot(range(len(GROUPS)), values, color=color, marker=marker,
                linestyle="None", markersize=9, label=date)
    ax.set_xticks(range(len(GROUPS)), GROUPS)
    ax.set(title="Comparar medianas con color y forma · datos sintéticos\nDisponibles por fecha: no son necesariamente los mismos créditos", ylabel="Mediana del saldo conocido (MXN)", ylim=(0, 4000))
    ax.legend(title="Corte: círculo / cuadrado")
    ax.text(2, 300, "Octubre: educación sin mediana", ha="center", fontsize=9)
    axis_style(ax)
    return fig


def export(output, cut="2026-10-31", source=SOURCE):
    import matplotlib.pyplot as plt
    date = pd.to_datetime(cut, format="%Y-%m-%d", errors="raise")
    if date.strftime("%Y-%m-%d") != cut:
        raise ValueError("Usa fecha YYYY-MM-DD")
    detail = read_detail(source)
    selected, _, _, _ = select_views(detail, cut)
    stats = box_summary(selected)
    positive, excluded = log_partition(selected)
    by_date = []
    for observed_date in sorted(detail.fecha_corte.unique()):
        observed, _, _, _ = select_views(detail, observed_date)
        table = box_summary(observed)
        table["fecha_corte"] = observed_date
        by_date.append(table)
    comparison = pd.concat(by_date, ignore_index=True)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, table in [("corte", selected), ("medianas", stats),
                        ("positivos_log", positive), ("excluidos_log", excluded),
                        ("medianas_por_corte", comparison)]:
        table.to_csv(output / f"{name}.csv", index=False)
    factories = [("origen", lambda: baseline_figure(stats, cut)),
                 ("lineal_log", lambda: log_figure(selected, positive, excluded, cut)),
                 ("etiquetas", lambda: labels_figure(stats, cut)),
                 ("senales", lambda: signals_figure(detail))]
    for name, factory in factories:
        fig = factory()
        try:
            fig.savefig(output / f"{name}.png", dpi=160)
        finally:
            plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva")
    parser.add_argument("--cut", default="2026-10-31")
    args = parser.parse_args()
    import matplotlib
    matplotlib.use("Agg")
    export(args.output, args.cut)

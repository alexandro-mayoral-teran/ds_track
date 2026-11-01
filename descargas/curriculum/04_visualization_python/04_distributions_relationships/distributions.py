"""Distribuciones y pares de variables, con coberturas y salidas separadas."""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "03_sql_databases/01_relational_sqlite/data"
GROUPS = ["comercio", "consumo", "educacion", "servicios"]
BINS = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500]


def read_detail(source=SOURCE):
    source = Path(source)
    cuts = pd.read_csv(source / "cortes.csv", dtype={"id_credito": "string",
        "fecha_corte": "string", "saldo_mxn": "Int64", "dias_atraso": "Int64"},
        keep_default_na=False, na_values=[""])
    credits = pd.read_csv(source / "creditos.csv", dtype="string", keep_default_na=False)
    if list(cuts.columns) != ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"]:
        raise ValueError("Columnas de cortes distintas del contrato")
    if list(credits.columns) != ["id_credito", "id_cliente", "segmento"]:
        raise ValueError("Columnas de créditos distintas del contrato")
    if cuts[["id_credito", "fecha_corte"]].isna().any().any() or cuts.duplicated(["id_credito", "fecha_corte"]).any():
        raise ValueError("Clave crédito/fecha inválida")
    if credits["id_credito"].str.strip().eq("").any() or credits["id_credito"].duplicated().any():
        raise ValueError("Clave de crédito inválida")
    if not credits["segmento"].isin(GROUPS).all():
        raise ValueError("Segmento fuera del contrato")
    dates = pd.to_datetime(cuts["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if not dates.dt.strftime("%Y-%m-%d").eq(cuts["fecha_corte"]).all():
        raise ValueError("Formato de fecha inesperado")
    if cuts[["saldo_mxn", "dias_atraso"]].lt(0).any().any():
        raise ValueError("Valores negativos fuera del contrato sintético")
    detail = cuts.merge(credits[["id_credito", "segmento"]], on="id_credito",
                        how="left", validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all():
        raise ValueError("Corte sin crédito correspondiente")
    return detail.drop(columns="_merge").sort_values(["fecha_corte", "id_credito"]).reset_index(drop=True)


def select_views(detail, cut):
    selected = detail.loc[detail.fecha_corte.eq(cut)].copy()
    balances = selected.loc[selected.saldo_mxn.notna()].copy()
    pairs = selected.dropna(subset=["saldo_mxn", "dias_atraso"]).copy()
    excluded = selected.loc[selected.saldo_mxn.isna() | selected.dias_atraso.isna()].copy()
    excluded["saldo_ausente"] = excluded.saldo_mxn.isna()
    excluded["atraso_ausente"] = excluded.dias_atraso.isna()
    if len(pairs) + len(excluded) != len(selected):
        raise ValueError("Pares y exclusiones no concilian")
    return selected, balances, pairs, excluded


def interval_counts(values, edges):
    """No perder silenciosamente observaciones fuera del rango elegido."""
    values = pd.Series(values).dropna().astype(float).to_numpy()
    edges = np.asarray(edges, dtype=float)
    if len(edges) < 2 or not np.isfinite(edges).all() or not np.all(np.diff(edges) > 0):
        raise ValueError("Los bordes deben ser finitos y crecientes")
    if not np.isfinite(values).all() or (len(values) and (values.min() < edges[0] or values.max() > edges[-1])):
        raise ValueError("Valores fuera de los intervalos: revisar bordes")
    counts, _ = np.histogram(values, bins=edges)
    return pd.DataFrame({"desde_mxn": edges[:-1], "hasta_mxn": edges[1:],
                         "incluye_limite_derecho": [False] * (len(edges) - 2) + [True],
                         "conteo": counts})


def box_summary(selected):
    rows = []
    for group in GROUPS:
        part = selected.loc[selected.segmento.eq(group)]
        values = part.saldo_mxn.dropna().astype(float)
        row = {"segmento": group, "registros": len(part), "conocidos": len(values)}
        if values.empty:
            row.update({key: float("nan") for key in ["minimo_mxn", "q1_mxn", "mediana_mxn", "q3_mxn", "maximo_mxn", "media_mxn", "iqr_mxn", "limite_inferior_mxn", "limite_superior_mxn", "bigote_inferior_mxn", "bigote_superior_mxn", "fuera_bigotes"]})
        else:
            q1, median, q3 = values.quantile([.25, .5, .75], interpolation="linear")
            iqr = q3 - q1
            low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            inside = values.loc[values.between(low, high)]
            row.update({"minimo_mxn": values.min(), "q1_mxn": q1, "mediana_mxn": median,
                        "q3_mxn": q3, "maximo_mxn": values.max(), "media_mxn": values.mean(),
                        "iqr_mxn": iqr, "limite_inferior_mxn": low, "limite_superior_mxn": high,
                        "bigote_inferior_mxn": inside.min(), "bigote_superior_mxn": inside.max(),
                        "fuera_bigotes": int((~values.between(low, high)).sum())})
        rows.append(row)
    return pd.DataFrame(rows)


def histogram_figure(selected, balances, cut):
    import matplotlib.pyplot as plt
    values = balances.saldo_mxn.astype(float)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout="constrained", sharey=True)
    upper = 12
    for ax, edges in zip(axes, [BINS, [0, 1000, 2000, 3000, 4000]]):
        interval_counts(values, edges)
        if values.empty:
            ax.text(.5, .5, "Sin observaciones" if selected.empty else "Sin saldos conocidos", transform=ax.transAxes, ha="center")
        else:
            counts, _, bars = ax.hist(values, bins=edges, color="#2563eb", edgecolor="white")
            ax.bar_label(bars, labels=[str(int(c)) for c in counts], padding=3)
            upper = max(upper, float(counts.max()) + 2)
        ax.set(title=f"Intervalos de {edges[1] - edges[0]} MXN", xlabel="Saldo conocido (MXN)", ylabel="Cantidad de créditos")
        ax.set_xticks(edges)
        ax.tick_params(axis="x", labelrotation=30)
        ax.grid(axis="y", alpha=.2)
        ax.set_axisbelow(True)
    axes[0].set_ylim(0, upper)
    fig.suptitle(f"Mismos saldos, distinta agrupación · {cut}\n{len(balances)}/{len(selected)} conocidos · datos sintéticos")
    return fig


def box_figure(selected, cut):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
    labels = []
    for position, group in enumerate(GROUPS, start=1):
        part = selected.loc[selected.segmento.eq(group)]
        values = part.saldo_mxn.dropna().astype(float).sort_values()
        labels.append(f"{group} · {len(values)}/{len(part)}")
        if values.empty:
            ax.text(100, position, "Sin observaciones" if part.empty else "Sin saldo conocido", va="center", color="#6b7280")
        else:
            ax.boxplot([values], positions=[position], orientation="horizontal", widths=.45,
                       whis=1.5, manage_ticks=False, showfliers=True,
                       medianprops={"color": "#c2410c", "linewidth": 2})
            # Separación vertical determinista para ver datos; no modifica el saldo.
            offset = np.linspace(-.10, .10, len(values)) if len(values) > 1 else [0]
            ax.scatter(values, position + np.asarray(offset), s=22, alpha=.7, color="#2563eb", zorder=3)
    ax.set_yticks(range(1, 5), labels)
    ax.set(title=f"Saldo por segmento · {cut} · datos sintéticos\nCaja: Q1–Q3; puntos azules: observaciones conocidas", xlabel="Saldo conocido (MXN)", xlim=(-150, 3700), ylim=(4.6, .4))
    ax.grid(axis="x", alpha=.2)
    ax.set_axisbelow(True)
    return fig


def scatter_figure(selected, pairs, cut):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
    for group, color, marker in zip(GROUPS, ["#2563eb", "#c2410c", "#7c3aed", "#0f766e"], ["o", "s", "^", "D"]):
        part = pairs.loc[pairs.segmento.eq(group)]
        if not part.empty:
            ax.scatter(part.saldo_mxn.astype(float), part.dias_atraso.astype(float),
                       label=f"{group} · n={len(part)}", color=color, marker=marker, s=55, alpha=.8)
    if pairs.empty:
        ax.text(.5, .5, "Sin observaciones" if selected.empty else "Sin pares conocidos", transform=ax.transAxes, ha="center")
    else:
        ax.legend(title="Créditos con ambas variables", fontsize=9, loc="upper right")
    top = max(53, float(pairs.dias_atraso.max()) * 1.35) if not pairs.empty else 53
    ax.set(title=f"Saldo y atraso del mismo crédito · {cut}\n{len(pairs)}/{len(selected)} pares conocidos · datos sintéticos",
           xlabel="Saldo conocido (MXN)", ylabel="Atraso conocido (días)", xlim=(-150, 3700), ylim=(-3, top))
    ax.grid(alpha=.2)
    ax.set_axisbelow(True)
    return fig


def mean_figure():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 3.5), layout="constrained")
    for position, (label, values) in enumerate([("A: 1900, 2000, 2100", [1900, 2000, 2100]),
                                               ("B: 0, 2000, 4000", [0, 2000, 4000])]):
        ax.scatter(values, [position] * 3, s=70, color="#2563eb")
    ax.axvline(2000, color="#c2410c", linestyle="--", label="Media y mediana de ambos: 2000 MXN")
    ax.set_yticks([0, 1], ["A · poca separación", "B · mucha separación"])
    ax.set(title="Mismo centro, distinta variabilidad · ejemplo independiente", xlabel="Saldo (MXN)", ylim=(1.5, -.5), xlim=(-200, 4600))
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(axis="x", alpha=.2)
    return fig


def export(output, cut="2026-10-31", source=SOURCE):
    import matplotlib.pyplot as plt
    date = pd.to_datetime(cut, format="%Y-%m-%d", errors="raise")
    if date.strftime("%Y-%m-%d") != cut:
        raise ValueError("Usa una fecha YYYY-MM-DD")
    detail = read_detail(source)
    selected, balances, pairs, excluded = select_views(detail, cut)
    bins = interval_counts(balances.saldo_mxn, BINS)
    coarse = interval_counts(balances.saldo_mxn, [0, 1000, 2000, 3000, 4000])
    stats = box_summary(selected)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, table in [("corte", selected), ("saldos", balances), ("pares", pairs),
                        ("excluidos", excluded), ("intervalos_500", bins),
                        ("intervalos_1000", coarse), ("resumen_cajas", stats)]:
        table.to_csv(output / f"{name}.csv", index=False)
    for name, factory in [("histogramas", lambda: histogram_figure(selected, balances, cut)),
                          ("cajas", lambda: box_figure(selected, cut)),
                          ("dispersion", lambda: scatter_figure(selected, pairs, cut)),
                          ("mismo_centro", mean_figure)]:
        fig = factory()
        try:
            fig.savefig(output / f"{name}.png", dpi=160)
        finally:
            plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para tablas y PNG")
    parser.add_argument("--cut", default="2026-10-31", help="Corte YYYY-MM-DD")
    args = parser.parse_args()
    import matplotlib
    matplotlib.use("Agg")
    export(args.output, args.cut)

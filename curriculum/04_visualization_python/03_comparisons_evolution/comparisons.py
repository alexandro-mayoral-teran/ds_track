"""Comparar medidas y bases explícitas; fuentes intactas y exportaciones nuevas."""

import argparse
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "03_sql_databases/01_relational_sqlite/data"
DATES = ["2026-09-30", "2026-10-31"]
GROUPS = ["comercio", "consumo", "educacion", "servicios"]


def prepare():
    credits = pd.read_csv(SOURCE / "creditos.csv", dtype="string")
    cuts = pd.read_csv(SOURCE / "cortes.csv", dtype={
        "id_credito": "string", "fecha_corte": "string",
        "saldo_mxn": "Int64", "dias_atraso": "Int64"})
    if credits["id_credito"].isna().any() or credits["id_credito"].duplicated().any():
        raise ValueError("Clave de crédito inválida")
    if cuts[["id_credito", "fecha_corte"]].isna().any().any() or cuts.duplicated(["id_credito", "fecha_corte"]).any():
        raise ValueError("Clave de corte inválida")
    dates = pd.to_datetime(cuts["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if not dates.dt.strftime("%Y-%m-%d").eq(cuts["fecha_corte"]).all():
        raise ValueError("Fecha inválida")
    if set(cuts["fecha_corte"]) != set(DATES):
        raise ValueError("Este ejemplo requiere los dos cortes originales")
    if cuts[["saldo_mxn", "dias_atraso"]].lt(0).any().any():
        raise ValueError("Valores negativos fuera del contrato")
    detail = cuts.merge(credits[["id_credito", "segmento"]], on="id_credito",
                        how="left", validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all() or set(detail["segmento"]) != set(GROUPS):
        raise ValueError("Crédito sin segmento esperado")
    rows = []
    for (date, group), part in detail.groupby(["fecha_corte", "segmento"]):
        known = int(part["dias_atraso"].count())
        overdue = int(part["dias_atraso"].ge(30).sum())
        rows.append({"fecha_corte": date, "segmento": group, "registros": len(part),
                     "saldos_conocidos": int(part["saldo_mxn"].count()),
                     "suma_conocida_mxn": part["saldo_mxn"].sum(min_count=1),
                     "atrasos_conocidos": known, "atrasos_30": overdue,
                     "tasa_30_pct": 100 * overdue / known if known else float("nan")})
    summary = pd.DataFrame(rows).astype({"suma_conocida_mxn": "Float64", "tasa_30_pct": "Float64"})
    # Pivot conserva una fila por crédito; dropna selecciona pares, no imputa.
    wide = cuts.pivot(index="id_credito", columns="fecha_corte", values="saldo_mxn")
    paired = wide[DATES].dropna().copy()
    totals = pd.DataFrame({"fecha_corte": DATES,
                           "suma_disponible_mxn": [cuts.loc[cuts.fecha_corte.eq(d), "saldo_mxn"].sum(min_count=1) for d in DATES],
                           "suma_pares_mxn": [paired[d].sum(min_count=1) for d in DATES],
                           "pares": len(paired)})
    return summary, paired, totals


def calendar(path):
    table = pd.read_csv(path, dtype={"fecha": "string", "saldo_mxn": "Float64"})
    if list(table.columns) != ["fecha", "saldo_mxn"] or table.empty:
        raise ValueError("Se requiere una serie no vacía con fecha y saldo_mxn")
    table["fecha"] = pd.to_datetime(table["fecha"], format="%Y-%m-%d", errors="raise")
    if table.fecha.isna().any() or table.fecha.duplicated().any() or not table.fecha.dt.is_month_end.all():
        raise ValueError("Fechas únicas al cierre mensual")
    if table.saldo_mxn.lt(0).any():
        raise ValueError("Saldo negativo fuera del ejemplo")
    table["fila_presente"] = True
    table = table.set_index("fecha").sort_index()
    expected = pd.date_range(table.index.min(), table.index.max(), freq="ME")
    result = table.reindex(expected)
    result.index.name = "fecha"
    # Solo completamos el indicador de presencia; el importe sigue ausente.
    result["fila_presente"] = result["fila_presente"].eq(True)
    return result


def category_figure(summary):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), layout="constrained")
    for number, (date, color, hatch) in enumerate(zip(DATES, ["#2563eb", "#c2410c"], ["", "//"])):
        part = summary.loc[summary.fecha_corte.eq(date)].set_index("segmento").reindex(GROUPS)
        positions = [i + (number - .5) * .36 for i in range(len(GROUPS))]
        for ax, column in zip(axes, ["suma_conocida_mxn", "tasa_30_pct"]):
            values = part[column].astype(float)
            valid = values.notna()
            bars = ax.barh([y for y, ok in zip(positions, valid) if ok], values[valid],
                           height=.32, color=color, hatch=hatch, label=date)
            if column == "suma_conocida_mxn":
                labels = [f"{v:,.0f} · {int(n)}/{int(total)}" for v, n, total in
                          zip(values[valid], part.loc[valid, "saldos_conocidos"], part.loc[valid, "registros"])]
            else:
                labels = [f"{v:.1f}% · {int(n)}/{int(d)}" for v, n, d in
                          zip(values[valid], part.loc[valid, "atrasos_30"], part.loc[valid, "atrasos_conocidos"])]
            ax.bar_label(bars, labels=labels, padding=4, fontsize=8)
            for y, ok in zip(positions, valid):
                if not ok:
                    ax.text(100 if column == "suma_conocida_mxn" else 1, y, "Sin valor", va="center", fontsize=8, color=color)
    for ax in axes:
        ax.set_yticks(range(len(GROUPS)), GROUPS)
        ax.set_ylim(len(GROUPS) - .6, -.6)
        ax.grid(axis="x", alpha=.2)
        ax.set_axisbelow(True)
        ax.legend(loc="lower right", fontsize=8)
    axes[0].set(title="Suma conocida · etiqueta: MXN y cobertura", xlabel="Suma conocida (MXN)", xlim=(0, 24500))
    axes[1].set(title="Atraso ≥ 30 días · etiqueta: tasa y fracción", xlabel="Porcentaje entre atrasos conocidos (%)", xlim=(0, 100))
    fig.suptitle("Comparaciones por segmento · datos sintéticos")
    return fig


def temporal_figure(totals):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", sharey=True)
    dates = pd.to_datetime(totals.fecha_corte)
    for ax, column, title in zip(axes, ["suma_disponible_mxn", "suma_pares_mxn"],
                                 ["Disponibles: 21 saldos en cada corte\nLos conjuntos difieren", f"Pares: los mismos {int(totals.pares.iloc[0])} créditos\nSaldo conocido en ambos cortes"]):
        values = totals[column].astype(float)
        ax.plot(dates, values, marker="o", color="#0f766e")
        for d, v in zip(dates, values):
            ax.annotate(f"{v:,.0f}", (d, v), xytext=(0, 10), textcoords="offset points", ha="center")
        ax.set(title=title, ylabel="Suma conocida (MXN)", ylim=(0, 55000))
        ax.set_xticks(dates, ["30 sep 2026", "31 oct 2026"])
        ax.margins(x=.25)
        ax.grid(alpha=.2)
    fig.suptitle("Dos cortes: la base cambia la comparación · datos sintéticos")
    return fig


def gap_figure(series):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")
    # NaN corta la línea. Eliminar filas ausentes uniría puntos separados.
    ax.plot(series.index, series.saldo_mxn.to_numpy(dtype=float, na_value=float("nan")), marker="o", color="#2563eb")
    for date, row in series.iterrows():
        if pd.isna(row.saldo_mxn):
            label = "Fila sin importe" if row.fila_presente else "Sin fila mensual"
            ax.annotate(label, (date, 65), ha="center", fontsize=9)
    ax.set_xticks(series.index, series.index.strftime("%Y-%m"))
    ax.set(title="Serie didáctica independiente: ausencias y cero", xlabel="Cierre mensual", ylabel="Saldo observado (MXN)", ylim=(-10, 160))
    ax.grid(alpha=.2)
    return fig


def export(output, series_path=HERE / "serie_mensual.csv"):
    import matplotlib.pyplot as plt
    summary, paired, totals = prepare()
    series = calendar(series_path)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    summary.to_csv(output / "comparaciones.csv", index=False)
    paired.to_csv(output / "pares.csv", index=True)
    totals.to_csv(output / "totales.csv", index=False)
    series.to_csv(output / "calendario.csv", index=True)
    for name, factory, data in [("segmentos", category_figure, summary), ("bases", temporal_figure, totals), ("huecos", gap_figure, series)]:
        fig = factory(data)
        try:
            fig.savefig(output / f"{name}.png", dpi=160)
        finally:
            plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva para tablas y PNG")
    args = parser.parse_args()
    import matplotlib
    matplotlib.use("Agg")
    export(args.output)

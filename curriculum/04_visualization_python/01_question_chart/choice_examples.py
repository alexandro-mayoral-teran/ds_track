"""Preparar cuatro vistas para justificar su elección sobre datos conocidos."""

import argparse
from datetime import date
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1] / "03_sql_databases/01_relational_sqlite/data"


def read_detail():
    observations = pd.read_csv(DATA / "cortes.csv", dtype={"id_credito": "string", "fecha_corte": "string",
                               "saldo_mxn": "Int64", "dias_atraso": "Int64"}, keep_default_na=False, na_values=[""])
    credits = pd.read_csv(DATA / "creditos.csv", dtype="string", keep_default_na=False)
    if observations[["id_credito", "fecha_corte"]].isna().any().any() or observations.duplicated(["id_credito", "fecha_corte"]).any():
        raise ValueError("Claves de observaciones inválidas")
    if credits["id_credito"].eq("").any() or credits["id_credito"].duplicated().any():
        raise ValueError("Claves de créditos inválidas")
    dates = pd.to_datetime(observations["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if not dates.dt.strftime("%Y-%m-%d").eq(observations["fecha_corte"]).all():
        raise ValueError("Formato temporal inesperado")
    detail = observations.merge(credits, on="id_credito", how="left", validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all():
        raise ValueError("Hay observaciones sin crédito")
    return detail.drop(columns="_merge").sort_values(["fecha_corte", "id_credito"]).reset_index(drop=True)


def prepare_views(detail, cut):
    selected = detail.loc[detail["fecha_corte"].eq(cut)].copy()
    summary = selected.groupby("segmento", as_index=False, observed=True, dropna=False).agg(
        registros=("id_credito", "size"), conocidos=("saldo_mxn", "count"),
        suma_mxn=("saldo_mxn", lambda values: values.sum(min_count=1)),
    ).sort_values("segmento").reset_index(drop=True)
    if summary["registros"].sum() != len(selected) or summary["conocidos"].sum() != selected["saldo_mxn"].count():
        raise ValueError("Grupos no conciliados")
    dates = sorted(detail.loc[detail["fecha_corte"].lt(cut), "fecha_corte"].unique())
    previous_date = dates[-1] if dates else None
    previous = detail.loc[detail["fecha_corte"].eq(previous_date), ["id_credito", "saldo_mxn"]]
    paired = selected.loc[:, ["id_credito", "saldo_mxn"]].merge(
        previous, on="id_credito", how="inner", suffixes=("_actual", "_anterior"), validate="one_to_one"
    ).dropna(subset=["saldo_mxn_actual", "saldo_mxn_anterior"])
    balances = selected["saldo_mxn"].dropna()
    relationship = selected.dropna(subset=["saldo_mxn", "dias_atraso"])
    return selected, summary, previous_date, paired, balances, relationship


def create_figure(views, cut):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    selected, summary, previous_date, paired, balances, relationship = views
    fig, axes = plt.subplots(2, 2, figsize=(13, 9.5), layout="constrained")
    fig.suptitle(f"Una fuente, cuatro preguntas · corte {cut}\nDatos ficticios; cada vista declara su base", fontsize=17)
    a, b, c, d = axes.flat
    a.set_title("A. ¿Qué suma conocida tiene cada segmento?", loc="left", fontsize=11)
    if summary.empty:
        a.text(0.5, 0.5, "Sin observaciones", ha="center", transform=a.transAxes)
        a.set_axis_off()
    else:
        maximum = summary["suma_mxn"].max()
        right = max(float(maximum) * 1.65, 1) if pd.notna(maximum) else 1
        for i, row in summary.iterrows():
            value = row["suma_mxn"]
            if pd.notna(value):
                a.barh(i, float(value), color="#2563eb")
                label = f"{int(value):,} · {int(row['conocidos'])}/{int(row['registros'])}"
                a.text(float(value) + right * 0.02, i, label, va="center", fontsize=9)
            else:
                a.text(right * 0.02, i, f"Sin saldo conocido · 0/{int(row['registros'])}", va="center", fontsize=9)
        a.set_yticks(range(len(summary)), summary["segmento"].tolist())
        a.invert_yaxis(); a.set_xlim(0, right)
        a.set_xlabel("Suma conocida (MXN) · etiquetas: conocidos/observados")
    b.set_title("B. ¿Cómo cambió la misma base comparable?", loc="left", fontsize=11)
    if paired.empty:
        b.text(0.5, 0.5, "Sin pares comparables con un corte previo", ha="center", transform=b.transAxes)
        b.set_axis_off()
    else:
        values = [int(paired["saldo_mxn_anterior"].sum()), int(paired["saldo_mxn_actual"].sum())]
        b.plot(pd.to_datetime([previous_date, cut]), values, marker="o", color="#0f766e")
        b.set_xticks(pd.to_datetime([previous_date, cut]), [previous_date, cut])
        for x, value in zip(pd.to_datetime([previous_date, cut]), values):
            b.annotate(f"{value:,}", (x, value), xytext=(0, 8), textcoords="offset points", ha="center")
        b.set_ylim(0, max(values) * 1.25 if max(values) else 1)
        b.set_ylabel("Suma conocida (MXN)")
        b.set_xlabel(f"Mismos {len(paired)} créditos · solo dos cortes, sin inferir tendencia")
    c.set_title("C. ¿Cómo se distribuyen los saldos conocidos?", loc="left", fontsize=11)
    if balances.empty:
        c.text(0.5, 0.5, "Sin saldos conocidos", ha="center", transform=c.transAxes)
        c.set_axis_off()
    else:
        counts, _, _ = c.hist(balances.astype(float), bins=list(range(0, 3501, 500)), color="#2563eb", edgecolor="white")
        if int(sum(counts)) != len(balances):
            raise ValueError("Los intervalos no cubren los saldos de esta muestra")
        c.set_xlabel(f"Saldo (MXN) · {len(balances)}/{len(selected)} conocidos · intervalos de 500")
        c.set_ylabel("Observaciones por intervalo")
    d.set_title("D. ¿Qué relación vemos entre saldo y atraso?", loc="left", fontsize=11)
    if relationship.empty:
        d.text(0.5, 0.5, "Sin pares saldo/atraso conocidos", ha="center", transform=d.transAxes)
        d.set_axis_off()
    else:
        d.scatter(relationship["saldo_mxn"].astype(float), relationship["dias_atraso"].astype(float), color="#0f766e", alpha=0.8)
        d.set_xlabel(f"Saldo (MXN) · {len(relationship)}/{len(selected)} pares conocidos")
        d.set_ylabel("Días de atraso")
    for ax in axes.flat:
        if ax.axison:
            ax.grid(alpha=0.18); ax.set_axisbelow(True)
    fig.supxlabel("No se imputan ausencias. Las líneas no prueban tendencia; la dispersión no prueba causalidad.", fontsize=10)
    return fig


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="2026-10-31")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if date.fromisoformat(args.date).isoformat() != args.date:
        raise ValueError("Usa YYYY-MM-DD")
    views = prepare_views(read_detail(), args.date)
    selected, summary, previous_date, paired, balances, relationship = views
    print(f"Observaciones: {len(selected)}; saldos conocidos: {len(balances)}; pares temporales: {len(paired)}; pares saldo/atraso: {len(relationship)}")
    print(summary.to_string(index=False))
    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=False)
        summary.to_csv(args.output / "comparacion_segmentos.csv", index=False, encoding="utf-8")
        paired.to_csv(args.output / "pares_temporales.csv", index=False, encoding="utf-8")
        relationship.to_csv(args.output / "pares_saldo_atraso.csv", index=False, encoding="utf-8")
        fig = create_figure(views, args.date)
        try:
            fig.savefig(args.output / "cuatro_preguntas.png", dpi=150)
        finally:
            import matplotlib.pyplot as plt
            plt.close(fig)
        print("Vistas guardadas en una carpeta nueva; entradas intactas")


if __name__ == "__main__":
    main()

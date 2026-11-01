"""Construir figuras explícitas desde un resumen comprobado, sin sobrescribir salidas."""

import argparse
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
TYPES = {"fecha_corte": "string", "segmento": "string", "registros": "Int64",
         "saldos_conocidos": "Int64", "suma_conocida_mxn": "Int64"}


def read_summary(path):
    table = pd.read_csv(path, dtype=TYPES, keep_default_na=False, na_values=[""])
    if list(table.columns) != list(TYPES):
        raise ValueError("Columnas distintas del contrato")
    required = ["fecha_corte", "segmento", "registros", "saldos_conocidos"]
    if table[required].isna().any().any() or table["segmento"].str.strip().eq("").any():
        raise ValueError("Campos obligatorios ausentes")
    if table["fecha_corte"].nunique() > 1 or table["segmento"].duplicated().any():
        raise ValueError("Usa una fecha y una fila por segmento")
    dates = pd.to_datetime(table["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if not dates.dt.strftime("%Y-%m-%d").eq(table["fecha_corte"]).all():
        raise ValueError("Fecha fuera del formato YYYY-MM-DD")
    if table["registros"].le(0).any() or table["saldos_conocidos"].lt(0).any() or table["saldos_conocidos"].gt(table["registros"]).any():
        raise ValueError("Conteos incompatibles")
    if table["suma_conocida_mxn"].lt(0).any():
        raise ValueError("Esta muestra no admite saldos negativos")
    if not table["suma_conocida_mxn"].isna().eq(table["saldos_conocidos"].eq(0)).all():
        raise ValueError("Suma desconocida y cobertura no concilian")
    return table.sort_values("segmento").reset_index(drop=True)


def draw_balance(ax, summary):
    """Dibujar sobre el Axes recibido; no crear, guardar ni cerrar la Figure."""
    ax.set_title("Suma de saldos conocidos por segmento", loc="left", pad=12)
    if summary.empty:
        ax.text(0.5, 0.5, "Sin observaciones en la tabla de entrada",
                ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
        return
    maximum = summary["suma_conocida_mxn"].max()
    right = max(float(maximum) * 1.65, 1) if pd.notna(maximum) else 1
    known = summary.loc[summary["suma_conocida_mxn"].notna()]
    bars = ax.barh(known.index.tolist(), known["suma_conocida_mxn"].astype(float).tolist(), color="#2563eb")
    labels = [f"{int(row['suma_conocida_mxn']):,} MXN · {int(row['saldos_conocidos'])}/{int(row['registros'])} conocidos"
              for _, row in known.iterrows()]
    ax.bar_label(bars, labels=labels, padding=6, fontsize=9)
    for position, row in summary.loc[summary["suma_conocida_mxn"].isna()].iterrows():
        ax.text(right * 0.015, position, f"Sin saldo conocido · 0/{int(row['registros'])}", va="center", color="#6b7280", fontsize=9)
    ax.set_yticks(range(len(summary)), summary["segmento"].tolist())
    ax.set_ylim(len(summary) - 0.5, -0.5)
    ax.set_xlim(0, right)
    ax.set_xlabel("Suma conocida (MXN)")
    ax.set_ylabel("Segmento")
    ax.grid(axis="x", alpha=0.2)
    ax.set_axisbelow(True)


def draw_coverage(ax, summary):
    ax.set_title("Cobertura de saldo por segmento", loc="left", pad=12)
    if summary.empty:
        ax.text(0.5, 0.5, "Sin observaciones", ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
        return
    percentages = (100.0 * summary["saldos_conocidos"] / summary["registros"]).astype(float)
    ax.scatter(percentages.tolist(), range(len(summary)), color="#0f766e")
    for position, row in summary.iterrows():
        ax.annotate(f"{int(row['saldos_conocidos'])}/{int(row['registros'])}",
                    (percentages.iloc[position], position), xytext=(8, 0), textcoords="offset points", va="center")
    ax.set_yticks(range(len(summary)), summary["segmento"].tolist())
    ax.set_ylim(len(summary) - 0.5, -0.5)
    ax.set_xlim(-5, 125)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("Saldos conocidos / observaciones (%)")
    ax.grid(axis="x", alpha=0.2)
    ax.set_axisbelow(True)


def create_single(summary):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 5.5), layout="constrained")
    draw_balance(ax, summary)
    cut = summary["fecha_corte"].iloc[0] if not summary.empty else "sin registros"
    fig.suptitle(f"Corte {cut} · datos ficticios", fontsize=13)
    fig.supxlabel("Entrada: resumen por segmento con cobertura. Ausencia de saldo conocido no equivale a cero.", fontsize=9)
    return fig, ax


def create_pair(summary):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), layout="constrained")
    draw_balance(axes[0], summary)
    draw_coverage(axes[1], summary)
    cut = summary["fecha_corte"].iloc[0] if not summary.empty else "sin registros"
    fig.suptitle(f"Una Figure, dos Axes · corte {cut} · datos ficticios", fontsize=14)
    fig.supxlabel("Saldo y cobertura son medidas distintas; comparten categorías, no unidades horizontales.", fontsize=9)
    return fig, axes


def save_outputs(summary, directory, include_pair=False):
    import matplotlib.pyplot as plt
    directory.mkdir(parents=True, exist_ok=False)
    summary.to_csv(directory / "resumen_usado.csv", index=False, encoding="utf-8")
    fig, ax = create_single(summary)
    try:
        fig.savefig(directory / "saldo_conocido.png", dpi=150)
    finally:
        plt.close(fig)
    if include_pair:
        fig, axes = create_pair(summary)
        try:
            fig.savefig(directory / "saldo_y_cobertura.png", dpi=150)
        finally:
            plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE / "resumen_octubre.csv")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--two-panels", action="store_true")
    args = parser.parse_args()
    summary = read_summary(args.input)
    print(f"Segmentos: {len(summary)}; observaciones: {summary['registros'].sum()}; conocidos: {summary['saldos_conocidos'].sum()}")
    print(summary.to_string(index=False))
    if args.output is not None:
        import matplotlib
        matplotlib.use("Agg")  # Backend de archivos; se elige antes de importar pyplot.
        save_outputs(summary, args.output, args.two_panels)
        print("Figuras guardadas y cerradas; entrada y entregas anteriores conservadas")


if __name__ == "__main__":
    main()

"""Conciliar pandas y SQL sobre una base original reconstruible y de solo lectura."""

import argparse
from datetime import date
from pathlib import Path
import sqlite3

import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "01_relational_sqlite"
DEFAULT_DATABASE = HERE / "output/cartera_integracion.sqlite"
TYPES = {
    "clientes": {"id_cliente": "string", "alias": "string", "region": "string"},
    "creditos": {"id_credito": "string", "id_cliente": "string", "segmento": "string"},
    "cortes": {"id_credito": "string", "fecha_corte": "string", "saldo_mxn": "Int64", "dias_atraso": "Int64"},
}
DETAIL_TYPES = TYPES["cortes"] | {"id_cliente": "string", "segmento": "string", "region": "string"}
SUMMARY_TYPES = {"segmento": "string", "registros": "Int64", "saldos_conocidos": "Int64",
                 "suma_conocida_mxn": "Int64", "atrasos_conocidos": "Int64", "confirmados": "Int64",
                 "tasa_conocidos_pct": "Float64", "cobertura_atraso_pct": "Float64"}
KEYS = {"clientes": ["id_cliente"], "creditos": ["id_credito"], "cortes": ["id_credito", "fecha_corte"]}


def canonical(table, keys, types):
    return table.loc[:, list(types)].astype(types).sort_values(keys).reset_index(drop=True)


def read_sources():
    tables = {}
    for name, types in TYPES.items():
        table = pd.read_csv(SOURCE / "data" / f"{name}.csv", dtype=types,
                            keep_default_na=False, na_values=[""], encoding="utf-8")
        if list(table.columns) != list(types):
            raise ValueError(f"Columnas inesperadas: {name}")
        if table[KEYS[name]].isna().any().any() or table.duplicated(KEYS[name]).any():
            raise ValueError(f"Claves inválidas: {name}")
        if name == "cortes":
            dates = pd.to_datetime(table["fecha_corte"], format="%Y-%m-%d", errors="raise")
            if not dates.dt.strftime("%Y-%m-%d").eq(table["fecha_corte"]).all():
                raise ValueError("Formato de fecha distinto del contrato")
        tables[name] = canonical(table, KEYS[name], types)
    return tables


def reference_detail(tables, cut):
    observations = tables["cortes"].loc[tables["cortes"]["fecha_corte"].eq(cut)].copy()
    detail = observations.merge(tables["creditos"], on="id_credito", how="left",
                                validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all():
        raise ValueError("Hay cortes sin crédito")
    detail = detail.drop(columns="_merge").merge(tables["clientes"], on="id_cliente", how="left",
                                                validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all():
        raise ValueError("Hay créditos sin cliente")
    return canonical(detail, ["id_credito", "fecha_corte"], DETAIL_TYPES)


def reference_summary(detail, threshold):
    work = detail.copy()
    # Confirmados cuenta solo condiciones verdaderas, sin clasificar desconocidos.
    work["confirmado"] = work["dias_atraso"].ge(threshold).fillna(False).astype("Int64")
    summary = work.groupby("segmento", as_index=False, dropna=False, observed=True).agg(
        registros=("id_credito", "size"), saldos_conocidos=("saldo_mxn", "count"),
        suma_conocida_mxn=("saldo_mxn", lambda values: values.sum(min_count=1)),
        atrasos_conocidos=("dias_atraso", "count"), confirmados=("confirmado", "sum"),
    )
    base = summary["atrasos_conocidos"].where(summary["atrasos_conocidos"].gt(0))
    summary["tasa_conocidos_pct"] = 100.0 * summary["confirmados"] / base
    summary["cobertura_atraso_pct"] = 100.0 * summary["atrasos_conocidos"] / summary["registros"]
    return canonical(summary, ["segmento"], SUMMARY_TYPES)


def compare_summary(actual, expected):
    integers = [name for name, kind in SUMMARY_TYPES.items() if kind != "Float64"]
    pd.testing.assert_frame_equal(actual[integers], expected[integers], check_exact=True)
    rates = [name for name, kind in SUMMARY_TYPES.items() if kind == "Float64"]
    pd.testing.assert_frame_equal(actual[rates], expected[rates], check_exact=False, rtol=1e-12, atol=1e-12)


def reconcile(database, cut, threshold):
    if not database.is_file():
        raise FileNotFoundError("Primero reconstruye la base con el preparador de 03.03")
    tables = read_sources()
    connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        connection.execute("BEGIN")
        for name, types in TYPES.items():
            query = f"SELECT {', '.join(types)} FROM {name}"  # Nombres internos fijos.
            loaded = pd.read_sql_query(query, connection, dtype=types)
            pd.testing.assert_frame_equal(canonical(loaded, KEYS[name], types), tables[name], check_exact=True)
        if connection.execute("PRAGMA foreign_key_check").fetchall():
            raise ValueError("Relaciones inválidas")
        parameters = {"fecha": cut, "umbral": threshold}
        sql_detail = pd.read_sql_query((HERE / "detail.sql").read_text(encoding="utf-8"),
                                      connection, params=parameters, dtype=DETAIL_TYPES)
        sql_summary = pd.read_sql_query((HERE / "summary.sql").read_text(encoding="utf-8"),
                                       connection, params=parameters, dtype=SUMMARY_TYPES)
    finally:
        connection.close()
    sql_detail = canonical(sql_detail, ["id_credito", "fecha_corte"], DETAIL_TYPES)
    sql_summary = canonical(sql_summary, ["segmento"], SUMMARY_TYPES)
    pandas_detail = reference_detail(tables, cut)
    pandas_summary = reference_summary(pandas_detail, threshold)
    pd.testing.assert_frame_equal(sql_detail, pandas_detail, check_exact=True)
    compare_summary(sql_summary, pandas_summary)
    if sql_summary["registros"].sum() != len(sql_detail):
        raise ValueError("No concilian las filas por grupo")
    if sql_summary["saldos_conocidos"].sum() != sql_detail["saldo_mxn"].count():
        raise ValueError("No concilian los saldos conocidos")
    pd.testing.assert_series_equal(
        pd.Series([sql_summary["suma_conocida_mxn"].sum(min_count=1)], dtype="Int64"),
        pd.Series([sql_detail["saldo_mxn"].sum(min_count=1)], dtype="Int64"),
    )
    return sql_detail, sql_summary


def create_plot(summary, cut):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5.5), layout="constrained")
    if summary.empty:
        ax.text(0.5, 0.5, "Sin observaciones para este corte", ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
    else:
        maximum = summary["suma_conocida_mxn"].max()
        right = max(float(maximum) * 1.45, 1) if pd.notna(maximum) else 1
        for position, row in summary.iterrows():
            known = row["suma_conocida_mxn"]
            if pd.notna(known):
                ax.barh(position, int(known), color="#2563eb")
                label = f"{int(known):,} MXN · {int(row['saldos_conocidos'])}/{int(row['registros'])} conocidos"
                ax.text(float(known) + right * 0.015, position, label, va="center", fontsize=9)
            else:
                ax.text(right * 0.015, position, f"Sin saldo conocido · 0/{int(row['registros'])}", va="center", fontsize=9, color="#6b7280")
        ax.set_yticks(range(len(summary)), summary["segmento"].tolist())
        ax.invert_yaxis()
        ax.set_xlim(0, right)
        ax.set_xlabel("Suma de saldos conocidos (MXN)")
        ax.grid(axis="x", alpha=0.2)
        ax.set_axisbelow(True)
    ax.set_title(f"Saldo conocido por segmento · {cut}\nConciliación pandas/SQL · datos ficticios", loc="left", pad=14)
    fig.supxlabel("Las ausencias se conservan; sin saldo conocido no significa saldo cero.", fontsize=9)
    return fig


def export_result(directory, detail, summary, cut, threshold):
    # Una carpeta nueva por entrega conserva resultados anteriores y archivos del usuario.
    directory.mkdir(parents=True, exist_ok=False)
    detail.to_csv(directory / "detalle.csv", index=False, encoding="utf-8")
    summary.to_csv(directory / "resumen.csv", index=False, encoding="utf-8")
    reloaded = pd.read_csv(directory / "resumen.csv", dtype=SUMMARY_TYPES, keep_default_na=False, na_values=[""])
    compare_summary(canonical(reloaded, ["segmento"], SUMMARY_TYPES), summary)
    reloaded_detail = pd.read_csv(directory / "detalle.csv", dtype=DETAIL_TYPES, keep_default_na=False, na_values=[""])
    pd.testing.assert_frame_equal(canonical(reloaded_detail, ["id_credito", "fecha_corte"], DETAIL_TYPES), detail, check_exact=True)
    fig = create_plot(summary, cut)
    try:
        fig.savefig(directory / "saldo_conocido.png", dpi=150)
    finally:
        import matplotlib.pyplot as plt
        plt.close(fig)
    known = detail["saldo_mxn"].sum(min_count=1)
    delays = detail["dias_atraso"].count()
    confirmed = int(detail["dias_atraso"].ge(threshold).fillna(False).sum())
    note = (f"Corte: {cut}; umbral de atraso: {threshold}.\n"
            f"Observaciones: {len(detail)}; saldos conocidos: {detail['saldo_mxn'].count()}.\n"
            f"Suma conocida MXN: {known}; no representa importes desconocidos.\n"
            f"Atrasos conocidos: {delays}; confirmados: {confirmed}; base de tasa: {delays}.\n"
            "Detalle y grupos conciliados entre CSV/pandas y SQLite/SQL.\n"
            "La gráfica usa el resumen conciliado. Fuente y base conservadas.\n")
    (directory / "evidencia.txt").write_text(note, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--date", default="2026-10-31")
    parser.add_argument("--threshold", type=int, default=30)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if date.fromisoformat(args.date).isoformat() != args.date or args.threshold < 0:
        raise ValueError("Usa fecha YYYY-MM-DD y umbral no negativo")
    detail, summary = reconcile(args.database, args.date, args.threshold)
    print(f"Conciliación comprobada: {len(detail)} observaciones y {len(summary)} grupos")
    print(summary.to_string(index=False))
    if args.output is not None:
        export_result(args.output, detail, summary, args.date, args.threshold)
        print("CSV, gráfica y evidencia guardados en una carpeta nueva")


if __name__ == "__main__":
    main()

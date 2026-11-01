"""Declarar vistas Altair desde tablas comprobadas; exportaciones nuevas."""

import argparse
import importlib.util
import importlib.metadata
import json
from pathlib import Path
import sys

import altair as alt
import pandas as pd

HERE = Path(__file__).resolve().parent
# Reutilizar el análisis anterior; la organización en paquetes se estudia en 05.
sys.path.insert(0, str(HERE.parent / "06_composition_export"))
from composition import summarize, read_detail, select_views, GROUPS, SOURCE, DATES, reading_note

LEVELS = ["Sin atraso", "1–29 días", "30 días o más"]
COLORS = ["#2563eb", "#c2410c", "#0f766e", "#7c3aed"]
SHAPES = ["circle", "square", "triangle-up", "diamond"]


def prepare(detail, cut):
    selected, summary = summarize(detail, cut)
    _, _, pairs, excluded = select_views(detail, cut)
    known = selected.loc[selected.dias_atraso.notna()].copy()
    known["tramo_atraso"] = "Sin atraso"
    known.loc[known.dias_atraso.between(1, 29), "tramo_atraso"] = "1–29 días"
    known.loc[known.dias_atraso.ge(30), "tramo_atraso"] = "30 días o más"
    counts = known.tramo_atraso.value_counts().reindex(LEVELS, fill_value=0)
    bands = pd.DataFrame({"tramo_atraso": LEVELS, "creditos": counts.to_numpy()})
    if int(bands.creditos.sum()) != len(known):
        raise ValueError("Los tramos no concilian con los atrasos conocidos")
    missing_delay = selected.loc[selected.dias_atraso.isna()].copy()
    comparison = pd.concat([summarize(detail, d)[1] for d in DATES], ignore_index=True)
    comparison["fecha_corte"] = pd.to_datetime(comparison.fecha_corte, format="%Y-%m-%d")
    summary["etiqueta"] = [
        f"{format(row.mediana_mxn, ',.2f').rstrip('0').rstrip('.')} MXN · {row.conocidos}/{row.registros}"
        if pd.notna(row.mediana_mxn) else
        ("Sin registros" if row.registros == 0 else f"Sin mediana · 0/{row.registros}")
        for row in summary.itertuples(index=False)
    ]
    summary["fraccion"] = summary.conocidos.astype(str) + "/" + summary.registros.astype(str)
    return {"corte": selected, "resumen": summary, "pares": pairs,
            "excluidos_pares": excluded, "tramos": bands,
            "excluidos_atraso": missing_delay, "comparacion": comparison}


def category_axis():
    return alt.Y("segmento:N", sort=GROUPS, title="Segmento",
                 scale=alt.Scale(domain=GROUPS))


def finish(chart):
    return chart.configure_axis(labelFontSize=12, titleFontSize=12).configure_title(
        fontSize=16, subtitleFontSize=12, anchor="start"
    ).configure_legend(labelFontSize=11, titleFontSize=12)


def medians_chart(summary, cut):
    maximum = summary.mediana_mxn.max()
    right = max(5000, float(maximum) * 1.6) if pd.notna(maximum) else 5000
    valid = summary.loc[summary.mediana_mxn.notna()].copy()
    missing = summary.loc[summary.mediana_mxn.isna()].copy()
    position = alt.X("mediana_mxn:Q", title="Mediana conocida (MXN)",
                     scale=alt.Scale(domain=[0, right], nice=False, zero=True))
    base = alt.Chart(valid).encode(x=position, y=category_axis(),
        tooltip=[alt.Tooltip("segmento:N"), alt.Tooltip("mediana_mxn:Q", format=",.2f"),
                 alt.Tooltip("fraccion:N", title="Conocidos/registros")])
    bars = base.mark_bar(color="#2563eb", size=28)
    labels = base.mark_text(align="left", dx=6, fontSize=12).encode(text="etiqueta:N")
    messages = alt.Chart(missing).mark_text(align="left", dx=6, fontSize=12).encode(
        x=alt.datum(0), y=category_axis(), text="etiqueta:N")
    medians = alt.layer(bars, labels, messages).properties(width=450, height=240, title="A · Mediana del saldo conocido")
    coverage_base = alt.Chart(summary.loc[summary.cobertura_pct.notna()]).encode(
        x=alt.X("cobertura_pct:Q", title="Saldos conocidos / registros (%)",
                scale=alt.Scale(domain=[0, 125], nice=False), axis=alt.Axis(values=[0, 25, 50, 75, 100])),
        y=category_axis())
    coverage = alt.layer(
        coverage_base.mark_point(filled=True, shape="square", color="#0f766e", size=90),
        coverage_base.mark_text(align="left", dx=8, fontSize=12).encode(text="fraccion:N"),
        alt.Chart(summary.loc[summary.registros.eq(0)]).mark_text(align="left", dx=6, fontSize=12).encode(
            x=alt.datum(0), y=category_axis(), text=alt.value("Sin registros")),
    ).properties(width=340, height=240, title="B · Cobertura")
    title = alt.Title(f"Mediana y cobertura · {cut}", subtitle=[
        "Fuente: CSV sintéticos de SQL 03.01 · misma tabla y medida que Matplotlib 04.06.",
        "Sin mediana no significa cero; cobertura y MXN conservan unidades distintas."])
    return finish(alt.hconcat(medians, coverage).resolve_scale(x="independent", y="shared").properties(title=title))


def pairs_chart(pairs, total, cut):
    chart = alt.Chart(pairs).mark_point(filled=True, size=95).encode(
        x=alt.X("saldo_mxn:Q", title="Saldo conocido (MXN)", scale=alt.Scale(zero=True, padding=12)),
        y=alt.Y("dias_atraso:Q", title="Atraso conocido (días)", scale=alt.Scale(zero=True, padding=12)),
        color=alt.Color("segmento:N", title="Segmento", scale=alt.Scale(domain=GROUPS, range=COLORS)),
        shape=alt.Shape("segmento:N", title="Segmento", scale=alt.Scale(domain=GROUPS, range=SHAPES)),
        tooltip=[alt.Tooltip("id_credito:N", title="Crédito"), alt.Tooltip("saldo_mxn:Q", title="Saldo MXN"),
                 alt.Tooltip("dias_atraso:Q", title="Atraso días"), alt.Tooltip("segmento:N", title="Segmento")],
    ).properties(width=640, height=300, title=alt.Title(f"Saldo y atraso · {cut}", subtitle=[
        f"{len(pairs)}/{total} pares conocidos · {total - len(pairs)} excluidos con motivos.",
        "Fuente: SQL 03.01 · datos sintéticos · asociación no demuestra causa."]))
    if pairs.empty:
        message = "Sin registros" if total == 0 else "Sin pares conocidos"
        chart = alt.layer(chart, alt.Chart(pd.DataFrame({"mensaje": [message]})).mark_text(fontSize=16).encode(
            x=alt.value(320), y=alt.value(150), text="mensaje:N"))
    return finish(chart)


def bands_chart(bands, total, cut):
    base = alt.Chart(bands).encode(
        x=alt.X("tramo_atraso:O", title="Tramo de atraso", sort=LEVELS, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("creditos:Q", title="Créditos con atraso conocido", scale=alt.Scale(zero=True), axis=alt.Axis(tickMinStep=1)),
        tooltip=[alt.Tooltip("tramo_atraso:O"), alt.Tooltip("creditos:Q")])
    chart = alt.layer(base.mark_bar(color="#2563eb", size=65),
                      base.mark_text(dy=-8, fontSize=12).encode(text="creditos:Q"))
    known = int(bands.creditos.sum())
    chart = chart.properties(width=640, height=260, title=alt.Title(f"Tramos ordenados · {cut}", subtitle=[
        f"{known}/{total} atrasos conocidos · {total - known} ausentes; no entran en tramos.",
        "Fuente: SQL 03.01 · reglas: 0, 1–29 y ≥30 días · datos sintéticos."]))
    if total == 0:
        chart = alt.layer(chart, alt.Chart(pd.DataFrame({"mensaje": ["Sin registros"]})).mark_text(fontSize=16).encode(
            x=alt.value(320), y=alt.value(100), text="mensaje:N"))
    return finish(chart)


def dates_chart(comparison):
    chart = alt.Chart(comparison.loc[comparison.mediana_mxn.notna()]).mark_point(filled=True, size=90).encode(
        x=alt.X("fecha_corte:T", title="Fecha de corte (UTC)", scale=alt.Scale(type="utc", padding=12),
                axis=alt.Axis(format="%Y-%m-%d", values=[alt.DateTime(year=2026, month=9, date=30),
                    alt.DateTime(year=2026, month=10, date=31)], labelAngle=0, labelOverlap=False)),
        y=alt.Y("mediana_mxn:Q", title="Mediana conocida (MXN)", scale=alt.Scale(zero=True)),
        color=alt.Color("segmento:N", title="Segmento", scale=alt.Scale(domain=GROUPS, range=COLORS)),
        shape=alt.Shape("segmento:N", title="Segmento", scale=alt.Scale(domain=GROUPS, range=SHAPES)),
        tooltip=[alt.Tooltip("fecha_corte:T", format="%Y-%m-%d"), alt.Tooltip("segmento:N"),
                 alt.Tooltip("mediana_mxn:Q"), alt.Tooltip("conocidos:Q"), alt.Tooltip("registros:Q")],
    ).properties(width=640, height=300, title=alt.Title("Dos fechas con tipo temporal", subtitle=[
        "Fuente: SQL 03.01 · datos sintéticos · educación no tiene mediana en octubre.",
        "Valores disponibles por fecha; no afirmar cambios de los mismos créditos."]))
    if comparison.mediana_mxn.notna().sum() == 0:
        chart = alt.layer(chart, alt.Chart(pd.DataFrame({"mensaje": ["Sin medianas conocidas"]})).mark_text(fontSize=16).encode(
            x=alt.value(320), y=alt.value(150), text="mensaje:N"))
    return finish(chart)


def export(output, cut="2026-10-31", bundle=False, source=SOURCE):
    if bundle and importlib.util.find_spec("vl_convert") is None:
        raise RuntimeError("--bundle requiere el grupo chart-export; consulta la lección 04.07")
    date = pd.to_datetime(cut, format="%Y-%m-%d", errors="raise")
    if date.strftime("%Y-%m-%d") != cut:
        raise ValueError("Usa fecha YYYY-MM-DD")
    tables = prepare(read_detail(source), cut)
    charts = {"medianas": medians_chart(tables["resumen"], cut),
              "pares": pairs_chart(tables["pares"], len(tables["corte"]), cut),
              "tramos": bands_chart(tables["tramos"], len(tables["corte"]), cut),
              "fechas": dates_chart(tables["comparacion"])}
    # La validación de esquema comprueba sintaxis; las tablas comprueban significado.
    for chart in charts.values():
        chart.to_dict(validate=True)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, table in tables.items():
        table.to_csv(output / f"{name}.csv", index=False)
    (output / "lectura.md").write_text(reading_note(tables["resumen"], cut), encoding="utf-8")
    for name, chart in charts.items():
        chart.save(output / f"{name}.json")
        chart.save(output / f"{name}.html", inline=bundle,
                   embed_options={"actions": False, "renderer": "svg"})
        if bundle:
            chart.save(output / f"{name}.png", scale_factor=2)
            chart.save(output / f"{name}.svg")
    versions = {"altair": alt.__version__, "pandas": pd.__version__, "html_inline": bundle}
    if bundle:
        # El módulo expone 1.9.0; la distribución distingue el correctivo post1.
        versions["vl_convert_python"] = importlib.metadata.version("vl-convert-python")
    (output / "versiones.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Carpeta nueva")
    parser.add_argument("--cut", default="2026-10-31")
    parser.add_argument("--bundle", action="store_true", help="HTML sin CDN más PNG/SVG; requiere chart-export")
    args = parser.parse_args()
    export(args.output, args.cut, args.bundle)

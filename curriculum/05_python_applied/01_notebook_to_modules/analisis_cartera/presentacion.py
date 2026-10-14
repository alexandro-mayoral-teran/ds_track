"""Figuras de 04.06/04.07 e informe de 04.09; misma medida y diseño."""

import altair as alt
import pandas as pd

from .reglas import GROUPS

SIZE = (12, 5.5)


def money(value, position=None):
    # Una mediana de saldos enteros puede terminar en medio MXN; no redondearla a cero.
    formatted = f"{value:,.2f}".rstrip("0").rstrip(".")
    return formatted.replace(",", " ")


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


def report(summary, totals, cut):
    overall = totals.loc[totals.segmento.eq('Todos')].iloc[0]
    n, k = int(overall.registros), int(overall.conocidos)
    lines = [f'# Cierre visual · {cut}', '',
             'Pregunta: ¿qué mediana de saldo conocido tiene cada segmento y con qué cobertura?',
             'Público: una persona que revisa el análisis y no escribió el código.',
             'Fuente: CSV sintéticos de SQL 03.01, conservados en fuentes/.',
             'Unidad de análisis: un crédito en un corte; saldo en MXN.', '',
             f'Base del corte: {n} registros, {k} saldos conocidos y {n-k} desconocidos.',
             '', '| Segmento | Registros | Conocidos | Mediana (MXN) | Cobertura (%) |',
             '| --- | ---: | ---: | ---: | ---: |']
    for row in summary.itertuples(index=False):
        median = money(row.mediana_mxn) if pd.notna(row.mediana_mxn) else 'Sin mediana'
        coverage = f'{row.cobertura_pct:.1f}' if pd.notna(row.cobertura_pct) else 'No definida'
        lines.append(f'| {row.segmento} | {row.registros} | {row.conocidos} | {median} | {coverage} |')
    lines += ['', '## Hallazgo y límites', '']
    if k:
        available = summary.loc[summary.mediana_mxn.notna()]
        high = available.loc[available.mediana_mxn.idxmax()]
        lines += [f'Entre los segmentos con saldo conocido, {high.segmento} tiene una mediana máxima de {money(high.mediana_mxn)} MXN; puede haber empates.',
                  f'La mediana global sobre los {k} saldos conocidos es {money(overall.mediana_mxn)} MXN; la cobertura global es {overall.cobertura_pct:.1f} % ({k}/{n}).']
    else:
        lines.append('No hay saldos conocidos para comparar medianas.' if n else 'No hay registros del corte; no se pueden comparar medianas ni calcular cobertura.')
    for row in summary.itertuples(index=False):
        if row.registros > 0 and row.conocidos == 0:
            lines.append(f'{row.segmento} tiene {row.registros} registros sin saldo conocido: cobertura 0 %, no mediana cero.')
        elif row.registros == 0:
            lines.append(f'{row.segmento} no tiene registros: mediana y cobertura no definidas.')
    lines += ['No sumar ni promediar medianas de segmentos para reconstruir la mediana global.',
              'La cobertura informa disponibilidad, no la magnitud de los saldos ausentes.',
              'Un saldo cero válido participa; no se imputan ceros a las ausencias.',
              'Estos datos ficticios no permiten inferir riesgo real, causa ni cambios individuales entre cortes.', '',
              '## Figuras y comprobación', '',
              '![Medianas conocidas y cobertura del mismo corte](matplotlib.png)', '',
              '[Vista declarativa de la misma tabla](altair.html) · [SVG estático](matplotlib.svg).',
              'Matplotlib y Altair usan resumen.csv: la conciliación de datos está en conciliacion.csv.',
              'Las comprobaciones automáticas de datos pasaron; todavía corresponde revisar figuras y explicación.',
              'El HTML necesita conexión para cargar las bibliotecas de CDN.', '']
    return '\n'.join(lines)

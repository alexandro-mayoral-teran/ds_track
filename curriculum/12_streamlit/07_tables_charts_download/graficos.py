"""Una barra y una etiqueta por crédito seleccionado; sin nuevas reglas de filtro."""

import altair as alt


def crear_grafico(seleccion, corte):
    if not seleccion:
        return None
    # Datos explícitos, sin agregar ni seleccionar nuevamente.
    base = alt.Chart(alt.Data(values=[dict(f) for f in seleccion])).encode(
        x=alt.X("saldo_mxn:Q", title="Saldo (MXN)",
                scale=alt.Scale(domain=[0, max(1, max(f["saldo_mxn"] for f in seleccion) * 1.18)])),
        y=alt.Y("id_credito:N", title="Crédito", sort=[f["id_credito"] for f in seleccion]),
        tooltip=[alt.Tooltip("id_credito:N", title="Crédito"),
                 alt.Tooltip("segmento:N", title="Segmento"),
                 alt.Tooltip("fecha_corte:N", title="Corte"),
                 alt.Tooltip("saldo_mxn:Q", title="Saldo (MXN)", format="d")],
    )
    barras = base.mark_bar(color="#176D9C")
    etiquetas = base.mark_text(align="left", baseline="middle", dx=4).encode(
        text=alt.Text("saldo_mxn:Q", format="d")
    )
    return (barras + etiquetas).properties(
        title=f"Saldo seleccionado por crédito — {corte}", height=max(120, 45 * len(seleccion))
    )

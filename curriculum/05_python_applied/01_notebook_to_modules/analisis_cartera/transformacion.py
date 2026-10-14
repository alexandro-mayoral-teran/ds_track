"""Calcular la mediana y cobertura de 04.09 desde un detalle ya leído."""

import pandas as pd

from .reglas import GROUPS


def summarize(detail, cut):
    """Retornar detalle del corte y resumen; conservar la entrada intacta."""
    date = pd.to_datetime(cut, format="%Y-%m-%d", errors="raise")
    if date.strftime("%Y-%m-%d") != cut:
        raise ValueError("Usa fecha YYYY-MM-DD")
    selected = detail.loc[detail.fecha_corte.eq(cut)].copy()
    rows = []
    for group in GROUPS:
        part = selected.loc[selected.segmento.eq(group)]
        values = part.saldo_mxn.dropna()
        n, k = len(part), len(values)
        rows.append({"segmento": group, "registros": n, "conocidos": k,
                     "mediana_mxn": float(values.median()) if k else None,
                     "cobertura_pct": 100 * k / n if n else None,
                     "fecha_corte": cut})
    summary = pd.DataFrame(rows)
    # Son las etiquetas conocidas de 04.07: la ausencia no se dibuja como cero.
    summary["etiqueta"] = [
        f"{format(row.mediana_mxn, ',.2f').rstrip('0').rstrip('.')} MXN · {row.conocidos}/{row.registros}"
        if pd.notna(row.mediana_mxn) else
        ("Sin registros" if row.registros == 0 else f"Sin mediana · 0/{row.registros}")
        for row in summary.itertuples(index=False)
    ]
    summary["fraccion"] = summary.conocidos.astype(str) + "/" + summary.registros.astype(str)
    return selected, summary

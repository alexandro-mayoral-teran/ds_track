"""Calcular la mediana y cobertura de 04.09 desde un detalle ya leído."""

import pandas as pd

from .reglas import GROUPS
from .contratos import coverage_pct


def summarize(detail: pd.DataFrame, cut: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Seleccionar un corte y resumir medianas/cobertura sin modificar detail.

    Precondición: detail cumple la estructura y las reglas de read_detail:
    clave id_credito/fecha_corte única, segmentos conocidos, fechas ISO y
    saldos Int64 no negativos o ausentes. Esta función no revalida todo ese
    contrato: el llamador debe proporcionar una tabla previamente validada.
    cut es una fecha existente del calendario en formato YYYY-MM-DD.

    Retorna (selected, summary). selected conserva columnas e índice de las
    filas elegidas; summary tiene una fila por GROUPS en su orden, incluso
    sin observaciones. Sus columnas son segmento, registros, conocidos,
    mediana_mxn, cobertura_pct, fecha_corte, etiqueta y fraccion.
    Mediana en MXN sobre conocidos; cobertura porcentual (0–100).
    Sin conocidos no hay mediana; sin registros tampoco hay cobertura.
    Un corte válido sin filas es un resultado definido. No escribe archivos.
    Lanza ValueError ante fecha textual inválida. Otros incumplimientos de la
    precondición pueden producir errores de pandas; la anotación no los valida.
    """
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
                     "cobertura_pct": coverage_pct(k, n),
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

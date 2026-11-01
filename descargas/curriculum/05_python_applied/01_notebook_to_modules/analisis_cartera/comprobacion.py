"""Referencia independiente y conciliación, conservadas de 04.09."""

import csv
import math
from pathlib import Path
import statistics

import pandas as pd

from .reglas import GROUPS, FIELDS


def reference(source, cut):
    """Calcular una referencia desde CSV con biblioteca estándar, sin groupby."""
    source = Path(source)
    with (source / 'creditos.csv').open(encoding='utf-8', newline='') as handle:
        groups = {row['id_credito']: row['segmento'] for row in csv.DictReader(handle)}
    with (source / 'cortes.csv').open(encoding='utf-8', newline='') as handle:
        selected = [row for row in csv.DictReader(handle) if row['fecha_corte'] == cut]
    rows = []
    for group in [*GROUPS, 'Todos']:
        part = selected if group == 'Todos' else [row for row in selected if groups[row['id_credito']] == group]
        # El campo vacío es desconocido; el texto "0" es un saldo válido.
        values = [int(row['saldo_mxn']) for row in part if row['saldo_mxn'] != '']
        n, k = len(part), len(values)
        rows.append({'segmento': group, 'registros': n, 'conocidos': k,
                     'mediana_mxn': statistics.median(values) if k else None,
                     'cobertura_pct': 100 * k / n if n else None})
    return pd.DataFrame(rows)


def reconcile(summary, selected, expected):
    """Contrastar valores y ausencias; una diferencia detiene la entrega."""
    values = selected.saldo_mxn.dropna()
    total = pd.DataFrame([{'segmento': 'Todos', 'registros': len(selected),
                          'conocidos': len(values),
                          'mediana_mxn': float(values.median()) if len(values) else None,
                          'cobertura_pct': 100 * len(values) / len(selected) if len(selected) else None}])
    actual = pd.concat([summary[['segmento', *FIELDS]], total], ignore_index=True)
    if actual.segmento.tolist() != expected.segmento.tolist():
        raise ValueError('Segmentos u orden diferentes de la referencia')
    rows = []
    for observed, target in zip(actual.itertuples(index=False), expected.itertuples(index=False)):
        for field in FIELDS:
            a, b = getattr(observed, field), getattr(target, field)
            same = (pd.isna(a) and pd.isna(b)) or (
                pd.notna(a) and pd.notna(b) and math.isclose(float(a), float(b), rel_tol=1e-12, abs_tol=1e-12))
            rows.append({'segmento': observed.segmento, 'campo': field,
                         'valor_analisis': a, 'valor_csv': b, 'coincide': bool(same)})
    checks = pd.DataFrame(rows)
    if not checks.coincide.all():
        raise ValueError('La referencia CSV y el análisis difieren; revisar antes de exportar')
    return actual, checks

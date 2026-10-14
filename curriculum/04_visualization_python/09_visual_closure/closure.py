"""Cerrar una entrega visual desde fuentes sintéticas, sin sobrescribir salidas."""

import argparse
import csv
import importlib.metadata
import importlib.util
import json
import math
from pathlib import Path
import shutil
import statistics
import sys

import altair as alt
import matplotlib
import pandas as pd

HERE = Path(__file__).resolve().parent
# Reutilizar funciones anteriores; los paquetes y sus importaciones se estudian en 05.
sys.path.insert(0, str(HERE.parent / '07_altair_declarative'))
from declarative import prepare, read_detail, medians_chart, GROUPS, SOURCE
from composition import delivery_figure, save_variant, money

FIELDS = ['registros', 'conocidos', 'mediana_mxn', 'cobertura_pct']


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


def report(summary, totals, cut, interactive=False):
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
              'El HTML básico necesita bibliotecas de CDN; con --bundle las incorpora.', '']
    if interactive:
        lines += ['[Explorador opcional por segmento](explorador.html).',
                  'Estado inicial: Todos. Los puntos son pares conocidos; las medianas usan saldos conocidos.',
                  'Los controles no reescriben tablas; registrar opción y base si se conserva una captura.', '']
    return '\n'.join(lines)


def export(output, cut='2026-10-31', dpi=160, bundle=False, interactive=False, source=SOURCE):
    if isinstance(dpi, bool) or not isinstance(dpi, int) or dpi <= 0:
        raise ValueError('dpi debe ser un entero positivo')
    date = pd.to_datetime(cut, format='%Y-%m-%d', errors='raise')
    if date.strftime('%Y-%m-%d') != cut:
        raise ValueError('Usa fecha YYYY-MM-DD')
    if bundle and importlib.util.find_spec('vl_convert') is None:
        raise RuntimeError('--bundle requiere chart-export; consulta 04.07')
    source = Path(source)
    tables = prepare(read_detail(source), cut)
    summary = tables['resumen']
    expected = reference(source, cut)
    totals, checks = reconcile(summary, tables['corte'], expected)
    chart = medians_chart(summary, cut)
    chart.to_dict(validate=True)
    explorer = None
    if interactive:
        sys.path.insert(0, str(HERE.parent / '08_altair_interaction'))
        from interaction import summaries, dropdown_chart
        explorer = dropdown_chart(tables, summaries(tables), cut)
        explorer.to_dict(validate=True)
    # Validar antes de crear la carpeta; una salida existente nunca se reinicia.
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / 'fuentes').mkdir()
    for name in ['creditos.csv', 'cortes.csv']:
        shutil.copyfile(source / name, output / 'fuentes' / name)
    for name, table in [('corte', tables['corte']), ('resumen', summary),
                        ('referencia_csv', expected), ('indicadores', totals), ('conciliacion', checks)]:
        table.to_csv(output / f'{name}.csv', index=False)
    import matplotlib.pyplot as plt
    fig = delivery_figure(summary, cut)
    try:
        formats = [save_variant(fig, output, 'matplotlib.png', dpi),
                   save_variant(fig, output, 'matplotlib.svg')]
    finally:
        plt.close(fig)
    pd.DataFrame(formats).to_csv(output / 'formatos.csv', index=False)
    for name, view in [('altair', chart), ('explorador', explorer)]:
        if view is None:
            continue
        view.save(output / f'{name}.json')
        view.save(output / f'{name}.html', inline=bundle,
                  embed_options={'actions': False, 'renderer': 'svg'})
        if bundle and name == 'altair':
            view.save(output / 'altair.png', scale_factor=2)
            view.save(output / 'altair.svg')
    (output / 'informe.md').write_text(report(summary, totals, cut, interactive), encoding='utf-8')
    instructions = ['# Reconstruir y revisar', '',
                    'Conservar esta carpeta completa y el repositorio DS Track con sus scripts.',
                    'Desde la raíz del repositorio, activar el entorno elegido y ejecutar closure.py.',
                    f'Usar --cut {cut}, --dpi {dpi} y --output con una carpeta nueva.',
                    'Para reconstruir desde estas copias, pasar --source con la ruta de fuentes/ de esta entrega.',
                    f'Opciones de esta ejecución: --bundle={bundle}; --interactive={interactive}.',
                    'Estas anotaciones describen opciones; no son comandos para copiar literalmente.', '',
                    '1. Abrir informe.md y revisar población, tabla, hallazgo, límites y PNG.',
                    '2. Cotejar indicadores.csv, referencia_csv.csv y las 20 filas de conciliacion.csv.',
                    '3. Abrir altair.html en un navegador compatible y contrastar con resumen.csv.',
                    '4. Revisar formatos.csv; el HTML básico requiere conexión y el incorporado no con estos datos.',
                    '5. Comparar la reconstrucción por valores, ausencias y bases; no exigir bytes idénticos de imágenes.',
                    '6. Registrar revisión visual y explicación propia antes de acreditar el cierre.', '',
                    'Una interrupción puede dejar archivos parciales. No borrar una entrega para repetirla.',
                    'Interacción opcional; no se requiere notebook, Quarto ni publicación en línea.', '']
    (output / 'RECONSTRUIR.md').write_text('\n'.join(instructions), encoding='utf-8')
    metadata = {'corte': cut, 'dpi_png': dpi, 'html_inline': bundle, 'interaccion': interactive,
                'versiones': {'pandas': pd.__version__, 'matplotlib': matplotlib.__version__, 'altair': alt.__version__},
                'fuentes': ['fuentes/creditos.csv', 'fuentes/cortes.csv'],
                'comprobaciones_datos': int(len(checks)), 'revision_visual': 'Pendiente de quien recibe la entrega'}
    if bundle:
        metadata['versiones']['vl_convert_python'] = importlib.metadata.version('vl-convert-python')
    # Se escribe al terminar los guardados; no sustituye la revisión de archivos.
    (output / 'entrega.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='Carpeta nueva')
    parser.add_argument('--cut', default='2026-10-31')
    parser.add_argument('--dpi', type=int, default=160)
    parser.add_argument('--source', type=Path, default=SOURCE, help='Carpeta con cortes.csv y creditos.csv')
    parser.add_argument('--bundle', action='store_true', help='HTML incorporado y PNG/SVG Altair; requiere chart-export')
    parser.add_argument('--interactive', action='store_true', help='Explorador opcional de 04.08')
    args = parser.parse_args()
    matplotlib.use('Agg')
    export(args.output, args.cut, args.dpi, args.bundle, args.interactive, args.source)

"""Explorar datos comprobados con controles y selecciones en el navegador."""

import argparse
import importlib.metadata
import importlib.util
import json
from pathlib import Path
import sys

import altair as alt
import pandas as pd

HERE = Path(__file__).resolve().parent
# Reutilizar lectura y reglas; la organización en paquetes se estudia en 05.
sys.path.insert(0, str(HERE.parent / '07_altair_declarative'))
from declarative import prepare, read_detail, finish, GROUPS, COLORS, SHAPES, SOURCE

OPTIONS = ['Todos', *GROUPS]


def summaries(tables):
    """Bases del corte, por segmento y global; mediana sobre saldos conocidos."""
    rows = []
    for group in OPTIONS:
        part = tables['corte'] if group == 'Todos' else tables['corte'].loc[tables['corte'].segmento.eq(group)]
        balances = part.saldo_mxn.dropna()
        pairs = part.dropna(subset=['saldo_mxn', 'dias_atraso'])
        n, k, p = len(part), len(balances), len(pairs)
        median = float(balances.median()) if k else None
        coverage = 100 * k / n if n else None
        value = f"mediana {format(median, ',.2f').rstrip('0').rstrip('.')} MXN" if k else 'sin mediana'
        label = (f'{group} · {n} registros · saldos {k}/{n} · pares {p}/{n} · {value}'
                 if n else f'{group} · Sin registros · mediana y cobertura no definidas')
        message = '' if p else ('Sin registros' if n == 0 else 'Sin pares conocidos')
        rows.append({'segmento': group, 'registros': n, 'conocidos': k,
                     'pares': p, 'excluidos_pares': n - p, 'mediana_mxn': median,
                     'cobertura_pct': coverage, 'estado': label, 'mensaje': message})
    return pd.DataFrame(rows)


def points(pairs):
    """Dominios fijos según el corte completo: filtrar no cambia los ejes."""
    xmax = max(3500, float(pairs.saldo_mxn.max()) * 1.1) if not pairs.empty else 3500
    ymax = max(50, float(pairs.dias_atraso.max()) * 1.1) if not pairs.empty else 50
    return alt.Chart(pairs).mark_point(filled=True, size=100).encode(
        x=alt.X('saldo_mxn:Q', title='Saldo conocido (MXN)',
                scale=alt.Scale(domain=[-150, xmax], nice=False)),
        y=alt.Y('dias_atraso:Q', title='Atraso conocido (días)',
                scale=alt.Scale(domain=[-3, ymax], nice=False)),
        color=alt.Color('segmento:N', scale=alt.Scale(domain=GROUPS, range=COLORS), title='Segmento'),
        shape=alt.Shape('segmento:N', scale=alt.Scale(domain=GROUPS, range=SHAPES), title='Segmento'),
        tooltip=[alt.Tooltip('id_credito:N', title='Crédito'),
                 alt.Tooltip('segmento:N', title='Segmento'),
                 alt.Tooltip('saldo_mxn:Q', title='Saldo MXN'),
                 alt.Tooltip('dias_atraso:Q', title='Atraso días')],
    ).properties(width=680, height=300)


def text_panel(table, predicate, field='estado', width=900):
    return alt.Chart(table).transform_filter(predicate).mark_text(
        align='left', fontSize=13
    ).encode(x=alt.value(8), y=alt.value(18), text=f'{field}:N').properties(width=width, height=36)


def dropdown_chart(tables, summary, cut):
    segment = alt.param(name='segmento_elegido', value='Todos',
                        bind=alt.binding_select(options=OPTIONS, name='Segmento: '))
    predicate = (segment == 'Todos') | (alt.datum.segmento == segment)
    scatter = points(tables['pares']).transform_filter(predicate)
    # Cada opción tiene una fila de estado, incluso cuando no hay pares.
    selected = alt.datum.segmento == segment
    message = alt.Chart(summary).transform_filter(selected).mark_text(fontSize=18).encode(
        x=alt.value(340), y=alt.value(150), text='mensaje:N')
    status = text_panel(summary, selected)
    chart = alt.vconcat(alt.layer(scatter, message), status, spacing=8).add_params(segment)
    return finish(chart.properties(title=alt.Title(f'Filtro por segmento · {cut}', subtitle=[
        'Fuente: CSV sintéticos SQL 03.01 · mediana sobre saldos conocidos del segmento.',
        'Los puntos requieren saldo y atraso conocidos; el estado conserva la base completa.',
        'Todos restablece el corte. Cambiar el control no modifica los CSV.'])))


def selection_chart(tables, summary, cut):
    choice = alt.selection_point(name='segmento_click', fields=['segmento'],
                                 on='click', toggle=False, clear='dblclick', empty=False)
    # La tabla de control conserva todos los segmentos, también sin pares.
    controller = alt.Chart(summary.loc[summary.segmento.ne('Todos')]).mark_point(
        filled=True, shape='square', size=220
    ).encode(
        x=alt.X('segmento:N', sort=GROUPS, title='Haz clic en un cuadrado; doble clic limpia',
                axis=alt.Axis(labelAngle=0)),
        y=alt.value(20),
        color=alt.when(choice).then(alt.value('#2563eb')).otherwise(alt.value('#64748b')),
        tooltip=['segmento:N', 'registros:Q', 'conocidos:Q', 'pares:Q'],
    ).properties(width=680, height=45).add_params(choice)
    highlighted = points(tables['pares']).encode(
        opacity=alt.when(choice).then(alt.value(1)).otherwise(alt.value(.18)),
        strokeWidth=alt.when(choice).then(alt.value(2)).otherwise(alt.value(0)),
        stroke=alt.value('#172554'),
    )
    state = text_panel(summary.loc[summary.segmento.ne('Todos')], choice)
    chart = alt.vconcat(controller, highlighted, state, spacing=16)
    return finish(chart.properties(title=alt.Title(f'Resaltar sin filtrar · {cut}', subtitle=[
        f'Fuente: SQL 03.01 · {len(tables["pares"])}/{len(tables["corte"])} pares conocidos del corte permanecen.',
        'Sin selección: todos atenuados y ficha vacía. Un clic elige un segmento.',
        'Educación puede tener registros sin puntos; atenuar no elimina observaciones.'])))


def interval_chart(tables, cut):
    brush = alt.selection_interval(name='ventana', encodings=['x', 'y'],
                                   clear='dblclick', empty=False)
    source = points(tables['pares']).encode(
        opacity=alt.when(brush).then(alt.value(1)).otherwise(alt.value(.22))
    ).add_params(brush).properties(width=480, title='A · Arrastra un rectángulo; doble clic limpia')
    target = points(tables['pares']).transform_filter(brush).properties(
        width=480, title='B · Solo pares dentro del rectángulo')
    # Fila auxiliar de peso cero: permite mostrar 0 aun sin pares seleccionados.
    # Se usa solo en el contador, nunca como punto ni como registro de cartera.
    count_data = tables['pares'][['id_credito', 'saldo_mxn', 'dias_atraso']].copy()
    count_data['peso'] = 1
    count_data = pd.concat([count_data, pd.DataFrame({'id_credito': ['__contador__'], 'peso': [0]})], ignore_index=True)
    count = alt.Chart(count_data).transform_filter(
        brush | (alt.datum.peso == 0)
    ).transform_aggregate(
        seleccionados='sum(peso)'
    ).transform_calculate(
        estado=f"'Pares seleccionados: ' + datum.seleccionados + ' / {len(tables['pares'])} pares conocidos; base del corte: {len(tables['corte'])} registros'"
    ).mark_text(align='left', fontSize=13).encode(
        x=alt.value(8), y=alt.value(18), text='estado:N').properties(width=1000, height=36)
    chart = alt.vconcat(alt.hconcat(source, target), count)
    return finish(chart.properties(title=alt.Title(f'Intervalo y vista vinculada · {cut}', subtitle=[
        'Fuente: SQL 03.01 · datos sintéticos · selección visual sobre pares ya conocidos.',
        'Sin selección: panel B vacío y conteo cero. Las ausencias no entran en el rectángulo.',
        'No es una muestra aleatoria ni una tasa de la cartera.'])))


def export(output, cut='2026-10-31', bundle=False, source=SOURCE):
    date = pd.to_datetime(cut, format='%Y-%m-%d', errors='raise')
    if date.strftime('%Y-%m-%d') != cut:
        raise ValueError('Usa fecha YYYY-MM-DD')
    if bundle and importlib.util.find_spec('vl_convert') is None:
        raise RuntimeError('--bundle requiere chart-export; consulta 04.07')
    tables = prepare(read_detail(source), cut)
    summary = summaries(tables)
    charts = {'filtro': dropdown_chart(tables, summary, cut),
              'resaltado': selection_chart(tables, summary, cut),
              'intervalo': interval_chart(tables, cut)}
    for chart in charts.values():
        chart.to_dict(validate=True)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name in ['corte', 'pares', 'excluidos_pares']:
        tables[name].to_csv(output / f'{name}.csv', index=False)
    summary.to_csv(output / 'resumen_segmentos.csv', index=False)
    for name, chart in charts.items():
        chart.save(output / f'{name}.json')
        chart.save(output / f'{name}.html', inline=bundle,
                   embed_options={'actions': False, 'renderer': 'svg'})
        if bundle:
            # Archivos estáticos del estado inicial; no capturan clics posteriores.
            chart.save(output / f'{name}_inicial.png', scale_factor=2)
            chart.save(output / f'{name}_inicial.svg')
    note = ['# Lectura y estados de interacción', '', f'Corte: {cut}. Fuente: CSV sintéticos SQL 03.01.',
            '', 'Mediana: saldos conocidos de cada opción, no únicamente sus pares.',
            'Filtro: Todos al abrir; resaltado: ninguna selección; intervalo: ninguna selección.',
            'Los CSV contienen la base preparada; los controles no reescriben estos archivos.',
            'Para registrar otro estado, guarda captura, opción/rectángulo y resultados comprobados.',
            '', '```csv', summary.to_csv(index=False).rstrip(), '```', '',
            'No interpretar selección visual como causa, tasa de cartera o muestra aleatoria.', '']
    (output / 'lectura.md').write_text('\n'.join(note), encoding='utf-8')
    versions = {'altair': alt.__version__, 'pandas': pd.__version__, 'html_inline': bundle}
    if bundle:
        versions['vl_convert_python'] = importlib.metadata.version('vl-convert-python')
    (output / 'versiones.json').write_text(json.dumps(versions, indent=2), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='Carpeta nueva')
    parser.add_argument('--cut', default='2026-10-31')
    parser.add_argument('--bundle', action='store_true', help='HTML incorporado y PNG/SVG iniciales; requiere chart-export')
    args = parser.parse_args()
    export(args.output, args.cut, args.bundle)

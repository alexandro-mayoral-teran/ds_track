"""12.02: entradas, selección y presentación sobre seis observaciones propias.

Arrancar con python -m streamlit run. No lee/escribe archivos ni utiliza caché
o estado de sesión propio. 12.03 separará las responsabilidades en módulos.
"""

import streamlit as st

# Unidad: un crédito ficticio en un corte. Clave: ID + fecha.
# Los segmentos son etiquetas de esta muestra; no son una calificación crediticia.
cartera = [
    {"id_credito": "001", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 0},
    {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": 2000},
    {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 2500},
    {"id_credito": "001", "segmento": "comercio", "fecha_corte": "2026-10-31", "saldo_mxn": 100},
    {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-10-31", "saldo_mxn": 1900},
    {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-10-31", "saldo_mxn": 2600},
]

st.title("Cartera: elige y comprueba")
st.write("Selecciona un corte y contrasta los indicadores con las filas del detalle.")

st.sidebar.header("Filtros")
corte = st.sidebar.selectbox("Corte", ["2026-09-30", "2026-10-31"], index=1)
segmentos = st.sidebar.multiselect(
    "Segmentos", ["comercio", "servicios"], default=["comercio", "servicios"]
)
minimo_mxn = st.sidebar.number_input(
    "Saldo mínimo (MXN)", min_value=0, max_value=1_000_000, value=2000, step=1
)
st.sidebar.caption("Vaciar Segmentos selecciona ninguno. El mínimo incluye la igualdad.")

# Primero fijamos la población del denominador; luego aplicamos los otros filtros.
universo = [fila for fila in cartera if fila["fecha_corte"] == corte]
seleccion = [
    fila for fila in universo
    if fila["segmento"] in segmentos and fila["saldo_mxn"] >= minimo_mxn
]
cantidad_universo = len(universo)  # Siempre tres en los dos cortes de esta muestra.
saldo_universo = sum(fila["saldo_mxn"] for fila in universo)
cantidad = len(seleccion)
saldo = sum(fila["saldo_mxn"] for fila in seleccion)
proporcion = cantidad / cantidad_universo * 100

st.subheader("Selección actual")
st.caption(f"Corte: {corte}. Segmentos: {', '.join(segmentos) or 'ninguno'}. Mínimo: {minimo_mxn} MXN (≥).")
st.write(f"Universo del corte: {cantidad_universo} créditos · {saldo_universo} MXN.")

col_cantidad, col_saldo, col_proporcion = st.columns(3)
col_cantidad.metric("Créditos seleccionados", cantidad)
col_saldo.metric("Saldo seleccionado (MXN)", saldo)
col_proporcion.metric("Créditos del universo (%)", f"{proporcion:.2f}%")
st.caption(f"Proporción de créditos: {cantidad} / {cantidad_universo} × 100. No es proporción de saldo.")

st.subheader("Detalle seleccionado")
if seleccion:
    st.table(seleccion)
else:
    st.info("Sin coincidencias con estos filtros. El universo del corte sigue siendo de tres créditos.")
    st.caption("El saldo seleccionado es 0 porque no se seleccionó ninguna fila; no faltan saldos en esta muestra.")

st.caption("Datos sintéticos completos dentro del script. No se suman cortes distintos.")

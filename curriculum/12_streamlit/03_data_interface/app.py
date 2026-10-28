"""Interfaz: obtener entradas, llamar al análisis y presentar su resultado."""

import csv
import streamlit as st

from cartera import MAXIMO_MXN, SEGMENTOS, analizar, leer_cartera
from configuracion import CORTES, CORTE_INICIAL, MINIMO_INICIAL, RUTA_DATOS

st.title("Una cartera, dos formas de usarla")
st.write("La app y el ejecutor de terminal utilizan las mismas funciones de análisis.")

try:
    filas = leer_cartera(RUTA_DATOS)  # Llamada explícita en cada pasada; todavía sin caché.
except (OSError, UnicodeError, csv.Error, ValueError) as error:
    st.error(f"No se pudo leer una cartera válida: {error}")
    st.stop()  # Detiene esta pasada; evita presentar indicadores de una fuente inválida.

st.sidebar.header("Filtros")
corte = st.sidebar.selectbox("Corte", CORTES, index=CORTES.index(CORTE_INICIAL))
segmentos = st.sidebar.multiselect("Segmentos", SEGMENTOS, default=list(SEGMENTOS))
minimo = st.sidebar.number_input("Saldo mínimo (MXN)", min_value=0, max_value=MAXIMO_MXN,
                               value=MINIMO_INICIAL, step=1)
st.sidebar.caption("Vaciar Segmentos selecciona ninguno. El mínimo incluye la igualdad.")

resultado = analizar(filas, corte, segmentos, minimo)
universo = resultado["universo"]
indicadores = resultado["indicadores"]
seleccion = resultado["seleccion"]
porcentaje = indicadores["porcentaje_creditos"]

st.subheader("Selección actual")
st.caption(f"Corte: {corte}. Segmentos: {', '.join(segmentos) or 'ninguno'}. Mínimo: {minimo} MXN (≥).")
st.write(f"Universo del corte: {universo['cantidad']} créditos · {universo['saldo_mxn']} MXN.")
col_cantidad, col_saldo, col_porcentaje = st.columns(3)
col_cantidad.metric("Créditos seleccionados", indicadores["cantidad"])
col_saldo.metric("Saldo seleccionado (MXN)", indicadores["saldo_mxn"])
col_porcentaje.metric("Créditos del universo (%)", f"{porcentaje:.2f}%" if porcentaje is not None else "N/D")
st.caption("Proporción = créditos seleccionados / créditos del corte × 100. Sin universo: N/D.")
st.subheader("Detalle seleccionado")
if seleccion:
    st.table(seleccion)
elif universo["cantidad"]:
    st.info("Sin coincidencias con estos filtros; el universo del corte conserva sus registros.")
else:
    st.info("El corte no tiene registros. La proporción no está definida: no se divide entre cero.")
st.caption("CSV sintético local al servidor. Lectura, validación y cálculo en cartera.py; interfaz en app.py.")

"""Mínimo sin archivos: un cero conocido no equivale a una fuente inválida."""

import streamlit as st

st.title("¿Cero, vacío o desconocido?")
caso = st.selectbox("Escenario simulado", ["Saldo cero", "Filtro sin coincidencias", "Corte sin registros", "Fuente inválida"])
st.caption("Simulación con un crédito conocido de saldo 0; aquí no se lee un CSV.")
if caso == "Fuente inválida":
    st.error("No se puede calcular con una fuente inválida.")
    st.info("Corrige la fuente antes de presentar indicadores.")
    st.stop()
universo = [] if caso == "Corte sin registros" else [{"id_credito": "001", "saldo_mxn": 0}]
if not universo:
    st.warning("No hay registros en este corte. No mostramos un saldo como si estuviera observado.")
    st.stop()
seleccion = [] if caso == "Filtro sin coincidencias" else universo
if not seleccion:
    st.info("El filtro no selecciona créditos; el universo sigue teniendo uno.")
else:
    st.info("Hay un crédito seleccionado cuyo saldo conocido es cero.")
st.metric("Créditos seleccionados", len(seleccion))
st.metric("Saldo de la selección (MXN)", sum(f["saldo_mxn"] for f in seleccion))

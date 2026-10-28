"""Dos ventas ficticias para observar una transición pequeña con AppTest."""

import streamlit as st

st.title("Probar un mínimo")
minimo = st.number_input("Importe mínimo (MXN)", min_value=0, value=100, step=1, key="minimo")
ventas = [100, 200]
seleccion = [importe for importe in ventas if importe >= minimo]
st.metric("Ventas seleccionadas", len(seleccion))
st.metric("Importe seleccionado (MXN)", sum(seleccion))

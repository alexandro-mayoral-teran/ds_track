"""Ejecutar con Streamlit: dos llamadas iguales, dos políticas distintas."""

import streamlit as st
from cache_ejemplos import datos_demo, recurso_demo

st.title("¿Copia de datos o recurso compartido?")
if st.button("Limpiar datos del mínimo"):
    datos_demo.clear()
if st.button("Limpiar recurso del mínimo"):
    recurso_demo.clear()
st.checkbox("Provocar otra pasada", key="otra_pasada")

primera = datos_demo()
primera["importes"].append(999)  # Solo cambia esta copia, no el valor guardado.
segunda = datos_demo()
recurso_a = recurso_demo()
recurso_b = recurso_demo()

st.write(f"Copia editada: {primera['importes']}")
st.write(f"Nueva llamada: {segunda['importes']}")
st.write(f"¿Datos son el mismo objeto?: {primera is segunda}")
st.write(f"¿Recurso es el mismo objeto?: {recurso_a is recurso_b}")
st.caption(f"Cálculo de datos: {segunda['calculo']}")
st.caption(f"Creación de recurso: {recurso_a['creacion']}")
st.caption("Catálogo simulado de solo lectura; no conecta una base ni carga un modelo real.")

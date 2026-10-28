"""Mínimo autónomo: variable local frente a memoria de una sesión."""

import streamlit as st

st.title("¿Qué conserva una sesión?")
local = 0
local += 1
if "contador" not in st.session_state:
    st.session_state["contador"] = 0

if st.button("Sumar uno"):
    st.session_state["contador"] += 1

st.checkbox("Provocar otra pasada", key="otra_pasada")
st.write(f"Variable local: {local}")
st.write(f"Contador de la sesión: {st.session_state['contador']}")
st.caption("La casilla reejecuta el script; solo el botón incrementa el contador.")

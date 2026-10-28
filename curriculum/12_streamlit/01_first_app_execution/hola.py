"""Primer mínimo de 12.01. Iniciar con python -m streamlit run, no con Run Python."""

import streamlit as st

st.title("Mi primera app local")
st.write("Cuatro unidades a 75 MXN por unidad.")
st.metric("Importe (MXN)", 4 * 75)

"""Capa Streamlit; las reglas de negocio siguen en cartera.py (12.03)."""

from uuid import uuid4
import streamlit as st

from cartera import analizar

VERSION_REGLAS = "1205-v1"
TTL_SEGUNDOS = 60
MAX_ENTRADAS = 8


@st.cache_data(ttl=TTL_SEGUNDOS, max_entries=MAX_ENTRADAS, persist=None, show_spinner=False)
def analizar_con_cache(filas, corte, segmentos, minimo_mxn, version_reglas):
    """Todos los argumentos participan en la clave; no leer estado oculto aquí."""
    resultado = analizar(filas, corte, segmentos, minimo_mxn)
    return {"resultado": resultado, "calculo": uuid4().hex}

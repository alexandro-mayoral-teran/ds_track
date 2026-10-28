"""Mínimos didácticos: copia de datos frente a recurso compartido de solo lectura."""

from types import MappingProxyType
from uuid import uuid4
import streamlit as st


@st.cache_data(max_entries=2, show_spinner=False)
def datos_demo():
    return {"importes": [100, 200], "calculo": uuid4().hex}


@st.cache_resource(max_entries=1, show_spinner=False)
def recurso_demo():
    # El diccionario solo se expone mediante una vista de lectura; sus valores son inmutables.
    return MappingProxyType({"segmentos": ("comercio", "servicios"), "creacion": uuid4().hex})

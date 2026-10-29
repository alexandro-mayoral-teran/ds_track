"""UI de lectura; iniciar desde el proyecto de interfaz, sin escribir entregas."""
from pathlib import Path
import platform
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from integracion import cargar, vista
import streamlit as st

if platform.python_version() != "3.12.12" or st.__version__ != "1.66.1":
    raise RuntimeError("Usa Python 3.12.12 y Streamlit 1.66.1 declarados para esta interfaz")
st.set_page_config(page_title="Entrega comprobada", layout="centered")
st.title("Cartera: reporte y app conciliados")
st.write("Elige una configuración y pulsa Comprobar entrega. El borrador no cambia la consulta aplicada.")
opciones = {"Octubre": "config/octubre.csv", "Septiembre": "config/septiembre.csv", "Selección vacía": "config/vacio.csv", "Sin universo": "config/sinuniverso.csv"}
elegida = st.selectbox("Configuración de la entrega", list(opciones))
if "aplicada" not in st.session_state:
    st.session_state.aplicada = None
    st.session_state.aviso = "Todavía no hay consulta aplicada."
if st.button("Comprobar entrega"):
    try:
        st.session_state.aplicada = cargar(opciones[elegida], "streamlit")
        st.session_state.aviso = ""
    except Exception as error:
        st.session_state.aplicada = None
        st.session_state.aviso = "Comprobación rechazada: " + str(error)
if st.session_state.aviso:
    st.warning(st.session_state.aviso)
if st.session_state.aplicada is not None:
    p = st.session_state.aplicada
    if opciones[elegida] != p["config"]:
        st.info("Borrador distinto: la vista conserva la configuración aplicada que aparece abajo.")
    st.html(vista(p))
st.caption("Sin caché de cálculo ni vigilancia del disco. Pulsa de nuevo para comprobar cambios. No hay autenticidad por MD5.")

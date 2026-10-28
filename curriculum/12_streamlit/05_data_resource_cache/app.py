"""12.05: ejecutar desde la carpeta creada por preparar_practica.py."""

import csv
import streamlit as st

from cartera import MAXIMO_MXN, SEGMENTOS, leer_cartera
from configuracion import CORTES, CORTE_INICIAL, MINIMO_INICIAL, RUTA_DATOS
from cache_analisis import MAX_ENTRADAS, TTL_SEGUNDOS, VERSION_REGLAS, analizar_con_cache

st.title("Reutiliza el cálculo, conserva la pregunta")
st.write("Los resultados usan los filtros aplicados. Edita el formulario y pulsa Aplicar filtros para cambiarlos.")

if st.sidebar.button("Limpiar caché del análisis", key="limpiar_cache"):
    analizar_con_cache.clear()  # Todas las combinaciones de esta función; no borra filtros.
st.sidebar.caption("La limpieza afecta esta función compartida, también para otras sesiones.")

try:
    filas = leer_cartera(RUTA_DATOS)  # Lectura y validación completas ANTES de consultar caché.
except (OSError, UnicodeError, csv.Error, ValueError) as error:
    st.error(f"No se pudo leer una cartera válida: {error}")
    st.stop()

# Claves propias: duran entre pasadas de esta sesión, sin pertenecer a un widget.
if "filtros_aplicados" not in st.session_state:
    st.session_state["filtros_aplicados"] = {
        "corte": CORTE_INICIAL,
        "segmentos": list(SEGMENTOS),
        "minimo_mxn": MINIMO_INICIAL,
    }
if "envios" not in st.session_state:
    st.session_state["envios"] = 0

with st.sidebar:
    st.header("Preparar filtros")
    with st.form("filtros", clear_on_submit=False, enter_to_submit=False):
        corte = st.selectbox("Corte", CORTES, index=CORTES.index(CORTE_INICIAL), key="corte_borrador")
        segmentos = st.multiselect("Segmentos", SEGMENTOS, default=list(SEGMENTOS), key="segmentos_borrador")
        minimo = st.number_input("Saldo mínimo (MXN)", min_value=0, max_value=MAXIMO_MXN,
                                 value=MINIMO_INICIAL, step=1, key="minimo_borrador")
        st.caption("Lista vacía = ninguno. Mínimo inclusivo (≥). Enter no envía este formulario.")
        enviado = st.form_submit_button("Aplicar filtros", key="aplicar")
    st.caption("Los cambios del formulario se envían juntos al pulsar Aplicar filtros.")

if enviado:
    # Otra lista: los filtros aplicados no son un alias de los valores del widget.
    st.session_state["filtros_aplicados"] = {
        "corte": corte, "segmentos": list(segmentos), "minimo_mxn": minimo,
    }
    st.session_state["envios"] += 1

aplicados = st.session_state["filtros_aplicados"]
paquete = analizar_con_cache(filas, corte=aplicados["corte"], segmentos=aplicados["segmentos"],
                             minimo_mxn=aplicados["minimo_mxn"], version_reglas=VERSION_REGLAS)
resultado = paquete["resultado"]
universo = resultado["universo"]
indicadores = resultado["indicadores"]
porcentaje = indicadores["porcentaje_creditos"]

st.subheader("Filtros aplicados")
st.caption(f"Corte: {aplicados['corte']}. Segmentos: {', '.join(aplicados['segmentos']) or 'ninguno'}. Mínimo: {aplicados['minimo_mxn']} MXN (≥).")
st.caption(f"Envíos aplicados en esta sesión: {st.session_state['envios']}. Al iniciar se usa la configuración predeterminada.")
st.write(f"Universo del corte: {universo['cantidad']} créditos · {universo['saldo_mxn']} MXN.")
col_cantidad, col_saldo, col_porcentaje = st.columns(3)
col_cantidad.metric("Créditos seleccionados", indicadores["cantidad"])
col_saldo.metric("Saldo seleccionado (MXN)", indicadores["saldo_mxn"])
col_porcentaje.metric("Créditos del universo (%)", f"{porcentaje:.2f}%" if porcentaje is not None else "N/D")
st.caption("Proporción = créditos seleccionados / créditos del corte × 100. Sin universo: N/D.")

# Está fuera del formulario: reejecuta, pero no aplica sus campos pendientes.
mostrar = st.checkbox("Mostrar detalle", value=True, key="mostrar_detalle")
if mostrar:
    st.subheader("Detalle de la selección aplicada")
    if resultado["seleccion"]:
        st.table(resultado["seleccion"])
    elif universo["cantidad"]:
        st.info("Sin coincidencias con los filtros aplicados; el universo conserva sus registros.")
    else:
        st.info("El corte no tiene registros. Su proporción no está definida.")
st.caption("Estado temporal de esta sesión. No guarda tus elecciones al recargar la página o reiniciar el servidor.")

with st.expander("Observa la caché"):
    st.caption(f"Identificador del cálculo: {paquete['calculo']}")
    st.write(f"Versión de reglas: {VERSION_REGLAS}. TTL: {TTL_SEGUNDOS} segundos. Máximo: {MAX_ENTRADAS} entradas.")
    st.write("Un identificador repetido muestra reutilización de esa ejecución. No mide rapidez ni certifica las cifras.")
    st.write("En cada pasada se lee y valida todo el CSV. Solo el análisis está cacheado; no hay persistencia en disco.")

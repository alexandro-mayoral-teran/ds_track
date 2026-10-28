"""12.06: mensajes y recuperación; ejecutar desde la copia preparada."""

import csv
import streamlit as st

from cartera import SEGMENTOS, leer_cartera
from configuracion import CORTES, CORTE_INICIAL, MINIMO_INICIAL, RUTA_DATOS
from cache_analisis import VERSION_REGLAS, analizar_con_cache
from entradas import preparar_filtros


def detener_fuente(titulo, accion, error):
    """Explicar antes de detener la pasada; no fabricar un resultado de éxito."""
    st.error(titulo)
    st.info(accion)
    st.caption("No se muestran indicadores de la fuente ni resultados guardados anteriormente.")
    with st.expander("Diagnóstico de lectura"):
        st.code(str(error))
    st.stop()


st.title("Cada resultado necesita contexto")
st.write("Aplica filtros válidos y distingue una selección vacía de una fuente que no permite calcular.")

if "filtros_aplicados" not in st.session_state:
    st.session_state["filtros_aplicados"] = {
        "corte": CORTE_INICIAL, "segmentos": list(SEGMENTOS), "minimo_mxn": MINIMO_INICIAL,
    }
if "envios" not in st.session_state:
    st.session_state["envios"] = 0
if "error_filtros" not in st.session_state:
    st.session_state["error_filtros"] = None

with st.sidebar:
    st.button("Reintentar lectura", key="reintentar")  # El clic ya provoca otra pasada.
    if st.button("Limpiar caché del análisis", key="limpiar_cache"):
        analizar_con_cache.clear()
    st.caption("Reintentar vuelve a leer. Limpiar descarta esta caché global, sin aplicar el borrador.")
    st.header("Preparar filtros")
    with st.form("filtros", clear_on_submit=False, enter_to_submit=False):
        corte = st.selectbox("Corte", (*CORTES, "2026-11-30"), index=CORTES.index(CORTE_INICIAL), key="corte_borrador")
        segmentos = st.multiselect("Segmentos", SEGMENTOS, default=list(SEGMENTOS), key="segmentos_borrador")
        minimo_texto = st.text_input("Saldo mínimo (MXN)", value=str(MINIMO_INICIAL), max_chars=20, key="minimo_borrador")
        st.caption("Pesos enteros, 0–1000000. Lista vacía = ninguno. Noviembre no tiene registros en la muestra.")
        enviado = st.form_submit_button("Aplicar filtros", key="aplicar")

# Los controles permanecen disponibles ante un fallo para poder reintentar.
try:
    with st.spinner("Leyendo y validando la fuente local..."):
        filas = leer_cartera(RUTA_DATOS)
except FileNotFoundError as error:
    detener_fuente("No se encontró cartera.csv.", "Restaura cartera.csv junto a la app de tu copia y pulsa Reintentar lectura.", error)
except PermissionError as error:
    detener_fuente("No se puede abrir la fuente por un problema de permisos.", "Revisa los permisos de lectura de tu copia y pulsa Reintentar lectura.", error)
except (UnicodeError, csv.Error, ValueError) as error:
    detener_fuente("La fuente no cumple el contrato; no se calcularon indicadores.", "Revisa encabezado, UTF-8, campos y claves en tu copia; corrige el problema y pulsa Reintentar lectura.", error)
except OSError as error:
    detener_fuente("No se pudo leer la fuente local.", "Revisa que cartera.csv sea un archivo accesible en tu copia y pulsa Reintentar lectura.", error)

if enviado:
    try:
        nuevos = preparar_filtros(corte, segmentos, minimo_texto)
    except ValueError as error:
        st.session_state["error_filtros"] = str(error)
    else:
        st.session_state["filtros_aplicados"] = nuevos
        st.session_state["envios"] += 1
        st.session_state["error_filtros"] = None

if st.session_state["error_filtros"]:
    st.error("No se aplicaron los filtros. " + st.session_state["error_filtros"])
    st.subheader("Últimos filtros válidos: el intento no se aplicó")
else:
    st.subheader("Selección aplicada")
aplicados = st.session_state["filtros_aplicados"]
st.caption(f"Corte aplicado: {aplicados['corte']}. Segmentos: {', '.join(aplicados['segmentos']) or 'ninguno'}. Mínimo: {aplicados['minimo_mxn']} MXN (≥).")
st.caption(f"Envíos válidos en esta sesión: {st.session_state['envios']}.")

if not filas:
    st.warning("La fuente tiene un encabezado válido, pero no contiene registros.")
    st.info("Revisa la fuente de tu copia y pulsa Reintentar lectura. No hay indicadores de cartera para mostrar.")
    st.stop()

paquete = analizar_con_cache(filas, aplicados["corte"], aplicados["segmentos"],
                             aplicados["minimo_mxn"], VERSION_REGLAS)
resultado = paquete["resultado"]
universo = resultado["universo"]
if not universo["cantidad"]:
    st.warning(f"No hay registros para el corte {aplicados['corte']}; la proporción no está definida.")
    st.info("Elige septiembre u octubre y pulsa Aplicar filtros. No se muestra un saldo del corte como cero observado.")
    st.stop()

seleccion = resultado["seleccion"]
indicadores = resultado["indicadores"]
st.write(f"Universo del corte: {universo['cantidad']} créditos · {universo['saldo_mxn']} MXN.")
if not aplicados["segmentos"]:
    st.info("No seleccionaste segmentos. La lista vacía elige ninguno; selecciona uno o ambos y pulsa Aplicar filtros.")
elif not seleccion:
    st.info("Ningún crédito cumple estos filtros. El universo conserva sus registros; revisa segmentos o reduce el mínimo y vuelve a aplicar.")
elif indicadores["saldo_mxn"] == 0:
    st.info("Hay créditos seleccionados con saldo conocido igual a cero; no son registros ausentes.")

col_cantidad, col_saldo, col_porcentaje = st.columns(3)
col_cantidad.metric("Créditos seleccionados", indicadores["cantidad"])
col_saldo.metric("Saldo seleccionado (MXN)", indicadores["saldo_mxn"])
col_porcentaje.metric("Créditos del universo (%)", f"{indicadores['porcentaje_creditos']:.2f}%")
st.caption("Proporción de créditos sobre el universo del corte. Un filtro vacío suma 0 MXN de selección, no elimina la cartera.")
mostrar = st.checkbox("Mostrar detalle", value=True, key="mostrar_detalle")
if mostrar and seleccion:
    st.table(seleccion)
with st.expander("Observa la caché"):
    st.caption(f"Identificador del cálculo: {paquete['calculo']}")
st.caption("Los mensajes son parte de esta pasada. La sesión conserva filtros, no sustituye tu bitácora personal.")

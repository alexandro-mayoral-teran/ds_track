"""App autónoma de 12.01: observar pasadas completas sin estado ni caché propios.

Datos ficticios incluidos en el archivo. No lee ni escribe archivos de práctica.
Iniciar desde una terminal con el mismo intérprete que tiene Streamlit.
"""

from uuid import uuid4

import streamlit as st

# Una marca nueva permite relacionar pantalla y consola en cada pasada.
marca = uuid4().hex[:8]
print(f"[12.01] INICIO marca={marca}", flush=True)

# Esta variable se vuelve a crear: no es un contador de sesiones ni de clics.
pasadas = 0
pasadas = pasadas + 1

ventas = [
    {"venta_id": "V001", "unidades": 4, "precio_mxn": 75},
    {"venta_id": "V002", "unidades": 2, "precio_mxn": 120},
    {"venta_id": "V003", "unidades": 0, "precio_mxn": 50},
    {"venta_id": "V004", "unidades": 3, "precio_mxn": 40},
]
for venta in ventas:
    venta["importe_mxn"] = venta["unidades"] * venta["precio_mxn"]
total_mxn = sum(venta["importe_mxn"] for venta in ventas)

st.title("Ventas: observa una ejecución")
st.write("Cuatro ventas ficticias. La casilla cambia la vista; el total incluye las cuatro.")
st.caption(f"Marca de esta ejecución: {marca}")
st.metric("Total de ventas (MXN)", total_mxn)
st.write(f"Variable local pasadas: {pasadas}")

mostrar_detalle = st.checkbox("Mostrar detalle", value=False)
if mostrar_detalle:
    st.table(ventas)

pulsado = st.button("Repetir cálculo")
if pulsado:
    st.info("El botón devolvió True en esta pasada. El total se calculó arriba.")

st.caption("Predice, interactúa y contrasta la nueva marca con la terminal.")
print(f"[12.01] FIN marca={marca} total_mxn={total_mxn} pasadas={pasadas}", flush=True)

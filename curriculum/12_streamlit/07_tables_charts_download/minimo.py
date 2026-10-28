"""Dos filas completas: tabla, gráfico y CSV comparten la misma lista."""

import csv
from io import StringIO
import streamlit as st
from graficos import crear_grafico

seleccion = [
    {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": 2000},
    {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 2500},
]
st.title("Dos filas, tres representaciones")
st.write("Septiembre: 002/2000 y 003/2500 MXN; suma 4500 MXN.")
st.table(seleccion)
st.altair_chart(crear_grafico(seleccion, "2026-09-30"), width="stretch", height=320,
                alt="Dos créditos: 002 con 2000 MXN y 003 con 2500 MXN.")
buffer = StringIO(newline="")
escritor = csv.DictWriter(buffer, fieldnames=list(seleccion[0]), lineterminator="\n")
escritor.writeheader()
escritor.writerows(seleccion)
st.download_button("Descargar mínimo (CSV)", buffer.getvalue().encode("utf-8"),
                   file_name="minimo_2026-09-30.csv", mime="text/csv", on_click="ignore")

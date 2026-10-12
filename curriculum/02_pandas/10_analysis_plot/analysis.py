"""Un análisis reproducible: fuente, reglas, resumen, gráfica y hallazgo."""

from pathlib import Path
import argparse
import hashlib

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "fecha_alta", "saldo_mxn"]
SEGMENTOS = ["consumo", "servicios", "comercio", "educacion"]


def leer_fuente(ruta):
    tabla = pd.read_csv(ruta, dtype={c: "string" for c in COLUMNAS[:-1]} | {"saldo_mxn": "Int64"},
                        keep_default_na=False, na_values=[""], encoding="utf-8-sig")
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Columnas inesperadas")
    return tabla


def limpiar_y_separar(fuente):
    tabla = fuente.reset_index(drop=True).copy()
    tabla.insert(0, "numero_registro", pd.Series(range(1, len(tabla) + 1), dtype="Int64"))
    reglas = {}
    for columna in COLUMNAS[:-1]:
        tabla[columna + "_original"] = tabla[columna]
        tabla[columna] = tabla[columna].str.strip().replace("", pd.NA)
        reglas[columna + "_ausente"] = tabla[columna].isna()
    tabla["segmento"] = tabla["segmento"].str.lower().replace({"educación": "educacion"})
    reglas["id_formato"] = tabla["id_credito"].notna() & ~tabla["id_credito"].str.fullmatch(r"\d{3}")
    reglas["segmento_fuera_catalogo"] = tabla["segmento"].notna() & ~tabla["segmento"].isin(SEGMENTOS)
    for columna in ["fecha_corte", "fecha_alta"]:
        texto = tabla[columna].copy()
        forma = texto.str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False)
        tabla[columna] = pd.to_datetime(texto.where(forma), format="%Y-%m-%d", errors="coerce")
        reglas[columna + "_invalida"] = texto.notna() & tabla[columna].isna()
    reglas["saldo_ausente"] = tabla["saldo_mxn"].isna()
    reglas["saldo_negativo"] = tabla["saldo_mxn"] < 0
    reglas["alta_posterior_corte"] = tabla["fecha_alta"] > tabla["fecha_corte"]
    clave = ["id_credito", "fecha_corte"]
    reglas["clave_repetida"] = tabla[clave].notna().all(axis=1) & tabla.duplicated(subset=clave, keep=False)
    banderas = pd.DataFrame(reglas, index=tabla.index).fillna(False).astype("boolean")
    motivos = pd.Series("", index=tabla.index, dtype="string")
    for nombre in banderas:
        mascara = banderas[nombre]
        separador = pd.Series("", index=tabla.index, dtype="string")
        separador.loc[motivos != ""] = "; "
        motivos.loc[mascara] = motivos.loc[mascara] + separador.loc[mascara] + nombre
    tabla["motivos"] = motivos
    rechazar = banderas.any(axis=1)
    aceptados, rechazados = tabla.loc[~rechazar].copy(), tabla.loc[rechazar].copy()
    reunidos = pd.concat([aceptados, rechazados]).sort_values("numero_registro").reset_index(drop=True)
    pd.testing.assert_frame_equal(tabla, reunidos)
    originales = tabla.loc[:, COLUMNAS].copy()
    for columna in COLUMNAS[:-1]:
        originales[columna] = tabla[columna + "_original"]
    pd.testing.assert_frame_equal(fuente.reset_index(drop=True), originales)
    return aceptados, rechazados


def resumir_corte(aceptados, corte):
    fecha = pd.Timestamp(corte)
    seleccion = aceptados.loc[aceptados["fecha_corte"] == fecha].copy()
    resumen = seleccion.groupby("segmento", as_index=False, dropna=False, observed=True).agg(
        creditos=("id_credito", "size"), saldo_mxn=("saldo_mxn", "sum")
    ).astype({"creditos": "Int64", "saldo_mxn": "Int64"})
    resumen = resumen.sort_values(["saldo_mxn", "segmento"], ascending=[False, True]).reset_index(drop=True)
    total = seleccion["saldo_mxn"].sum(min_count=1)
    base = total if pd.notna(total) and total > 0 else pd.NA
    resumen["participacion_pct"] = (resumen["saldo_mxn"] / base * 100).astype("Float64")
    if resumen["creditos"].sum() != len(seleccion):
        raise ValueError("No concilian los creditos")
    if not seleccion.empty and resumen["saldo_mxn"].sum() != total:
        raise ValueError("No concilia el saldo aceptado")
    return seleccion, resumen


def crear_grafica(resumen, corte, filas_aceptadas):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5.5), layout="constrained")
    if resumen.empty:
        ax.text(0.5, 0.5, "Sin observaciones aceptadas para este corte", ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
    else:
        barras = ax.barh(resumen["segmento"], resumen["saldo_mxn"].astype(float), color="#2563eb")
        ax.invert_yaxis()
        ax.set_xlim(left=0, right=max(float(resumen["saldo_mxn"].max()) * 1.22, 1))
        ax.bar_label(barras, labels=[f"{int(x):,}" for x in resumen["saldo_mxn"]], padding=5)
        ax.set_xlabel("Saldo aceptado (MXN)")
        ax.set_ylabel("Segmento")
        ax.grid(axis="x", alpha=0.2)
        ax.set_axisbelow(True)
    ax.set_title(f"Saldo por segmento · {pd.Timestamp(corte):%Y-%m-%d}\n"
                 f"{filas_aceptadas} créditos aceptados · datos sintéticos", loc="left", pad=14)
    fig.supxlabel("Alcance: registros que pasan las reglas. Los rechazos permanecen aparte.", fontsize=9)
    return fig, ax


def redactar_hallazgo(resumen, corte, aceptados, rechazados):
    contexto = f"Corte {pd.Timestamp(corte):%Y-%m-%d}. Entrada de la práctica: {len(aceptados) + len(rechazados)} registros; "
    contexto += f"{len(aceptados)} aceptados y {len(rechazados)} rechazados entre todos los cortes.\n\n"
    if resumen.empty:
        hallazgo = "No hay observaciones aceptadas para este corte; no se identifica un segmento mayor."
    else:
        mayor = resumen.iloc[0]
        empatados = resumen.loc[resumen["saldo_mxn"] == mayor["saldo_mxn"], "segmento"].tolist()
        hallazgo = f"Mayor saldo aceptado: {', '.join(empatados)}, {int(mayor['saldo_mxn'])} MXN. "
        if pd.notna(mayor["participacion_pct"]):
            hallazgo += f"Cada segmento mencionado representa {mayor['participacion_pct']:.2f}% del saldo aceptado del corte."
        else:
            hallazgo += "La participación no se calcula porque el saldo total aceptado es cero."
    return "# Hallazgo de la práctica\n\n" + contexto + hallazgo + "\n\n" + (
        "Límites: la gráfica excluye rechazos; no representa toda la entrada. "
        "El importe total no demuestra mayor saldo promedio, más riesgo ni una causa. "
        "Para comparar cortes deben revisarse poblaciones y reglas.\n"
    )


def exportar_tablas(tablas, fuente, carpeta):
    rutas = {nombre: carpeta / nombre for nombre in tablas}
    if any(r.resolve() == fuente.resolve() for r in rutas.values()):
        raise ValueError("Una salida reemplazaria la fuente")
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, tabla in tablas.items():
        ruta = rutas[nombre]
        fechas = [c for c in ["fecha_corte", "fecha_alta"] if c in tabla]
        tabla.to_csv(ruta, index=False, encoding="utf-8", date_format="%Y-%m-%d", lineterminator="\n")
        tipos = {c: ("string" if c in fechas else str(t)) for c, t in tabla.dtypes.items()}
        recargada = pd.read_csv(ruta, dtype=tipos, keep_default_na=False, na_values=[""])
        for c in fechas:
            recargada[c] = pd.to_datetime(recargada[c], format="%Y-%m-%d", errors="raise")
        if "motivos" in recargada:
            recargada["motivos"] = recargada["motivos"].fillna("")
        pd.testing.assert_frame_equal(tabla.reset_index(drop=True), recargada, check_exact=False, rtol=1e-12, atol=1e-12)


def main(corte="2026-10-31"):
    import matplotlib
    import matplotlib.pyplot as plt

    carpeta = Path(__file__).resolve().parent
    entrada = carpeta.parent / "06_text_dates" / "cartera_texto_fechas.csv"
    fuente = leer_fuente(entrada)
    original = fuente.copy()
    aceptados, rechazados = limpiar_y_separar(fuente)
    seleccion, resumen = resumir_corte(aceptados, corte)
    salida = carpeta / "output"
    exportar_tablas({"aceptados.csv": aceptados, "rechazados.csv": rechazados,
                     "detalle_corte.csv": seleccion, "resumen_corte.csv": resumen}, entrada, salida)
    fig, ax = crear_grafica(resumen, corte, len(seleccion))
    fig.savefig(salida / "saldo_segmentos.png", dpi=160)
    plt.close(fig)
    nota = redactar_hallazgo(resumen, corte, aceptados, rechazados)
    nota += f"\nVersiones: pandas {pd.__version__}; Matplotlib {matplotlib.__version__}. "
    nota += f"SHA-256 de la fuente: {hashlib.sha256(entrada.read_bytes()).hexdigest()}.\n"
    (salida / "hallazgo.md").write_text(nota, encoding="utf-8")
    pd.testing.assert_frame_equal(fuente, original)
    print(resumen.to_string(index=False))
    print(nota)
    print("Tablas comprobadas; figura y hallazgo exportados; fuente intacta")


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corte", default="2026-10-31", help="Fecha calendario YYYY-MM-DD")
    main(parser.parse_args().corte)

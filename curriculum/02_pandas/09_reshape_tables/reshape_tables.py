"""Cambiar largo/ancho conservando valores y existencia de observaciones."""

from pathlib import Path

import pandas as pd


CORTES = ["2026-09-30", "2026-10-31"]
COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso"]


def leer_detalle(ruta):
    tabla = pd.read_csv(ruta, dtype={"id_credito": "string", "segmento": "string",
                        "fecha_corte": "string", "saldo_mxn": "Int64", "dias_atraso": "Int64"},
                        keep_default_na=False, na_values=[""], encoding="utf-8-sig")
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Columnas inesperadas")
    tabla["fecha_corte"] = pd.to_datetime(tabla["fecha_corte"], format="%Y-%m-%d", errors="raise")
    return tabla


def proyectar(detalle):
    largo = detalle[["id_credito", "fecha_corte", "saldo_mxn"]].copy()
    largo["corte"] = largo["fecha_corte"].dt.strftime("%Y-%m-%d").astype("string")
    largo = largo[["id_credito", "corte", "saldo_mxn"]]
    if largo[["id_credito", "corte"]].isna().any(axis=None):
        raise ValueError("ID y corte son obligatorios")
    if not largo["corte"].isin(CORTES).all():
        raise ValueError("El ejemplo admite solo los dos cortes acordados")
    if largo.duplicated(subset=["id_credito", "corte"]).any():
        raise ValueError("Cada celda ID/corte debe tener una sola observacion")
    return largo


def crear_ancho(largo):
    valores = largo.pivot(index="id_credito", columns="corte", values="saldo_mxn")
    valores = valores.reindex(columns=CORTES).astype("Int64")
    # La marca describe existencia de fila, no conocimiento del importe.
    marcas = largo.assign(observado=True).pivot(index="id_credito", columns="corte", values="observado")
    marcas = marcas.reindex(columns=CORTES).astype("boolean").fillna(False)
    ancho = valores.rename_axis(columns=None).reset_index()
    presencia = marcas.rename_axis(columns=None).reset_index()
    return ancho, presencia


def reconstruir(ancho, presencia):
    largo = ancho.melt(id_vars="id_credito", value_vars=CORTES, var_name="corte", value_name="saldo_mxn")
    marcas = presencia.melt(id_vars="id_credito", value_vars=CORTES, var_name="corte", value_name="observado")
    largo["corte"] = largo["corte"].astype("string")
    marcas["corte"] = marcas["corte"].astype("string")
    ambos = largo.merge(marcas, on=["id_credito", "corte"], how="outer", validate="one_to_one", indicator=True)
    if not ambos["_merge"].eq("both").all() or ambos["observado"].isna().any():
        raise ValueError("Valores y marcas de presencia no tienen las mismas celdas")
    return ambos.loc[ambos["observado"], ["id_credito", "corte", "saldo_mxn"]].astype(
        {"id_credito": "string", "corte": "string", "saldo_mxn": "Int64"}
    ).reset_index(drop=True)


def comprobar_vuelta(original, recuperado):
    clave = ["id_credito", "corte"]
    pd.testing.assert_frame_equal(original.sort_values(clave).reset_index(drop=True),
                                  recuperado.sort_values(clave).reset_index(drop=True), check_exact=True)


def sumar_conocidos(serie):
    return serie.sum(min_count=1)


def resumir_segmentos(detalle):
    trabajo = detalle.copy()
    if trabajo["segmento"].eq("(sin segmento)").any():
        raise ValueError("La etiqueta de presentacion ya existe como categoria real")
    trabajo["segmento"] = trabajo["segmento"].fillna("(sin segmento)")
    trabajo["corte"] = trabajo["fecha_corte"].dt.strftime("%Y-%m-%d").astype("string")
    resumen = trabajo.pivot_table(index="segmento", columns="corte", values="saldo_mxn",
                                  aggfunc=sumar_conocidos, dropna=False, observed=True)
    resumen = resumen.reindex(columns=CORTES).astype("Int64").rename_axis(columns=None).reset_index()
    for corte in CORTES:
        esperado = trabajo.loc[trabajo["corte"] == corte, "saldo_mxn"].sum(min_count=1)
        obtenido = resumen[corte].sum(min_count=1)
        if pd.isna(esperado) != pd.isna(obtenido) or (pd.notna(esperado) and esperado != obtenido):
            raise ValueError("El resumen no concilia el saldo conocido del corte")
    return resumen


def exportar(tablas, entrada, carpeta):
    rutas = {nombre: carpeta / nombre for nombre in tablas}
    if any(r.resolve() == entrada.resolve() for r in rutas.values()):
        raise ValueError("La salida reemplazaria la fuente")
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, tabla in tablas.items():
        ruta = rutas[nombre]
        tabla.to_csv(ruta, index=False, encoding="utf-8", lineterminator="\n")
        tipos = {c: str(t) for c, t in tabla.dtypes.items()}
        recargada = pd.read_csv(ruta, dtype=tipos, keep_default_na=False, na_values=[""])
        pd.testing.assert_frame_equal(tabla.reset_index(drop=True), recargada, check_exact=True)


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta.parent / "07_group_summarize" / "cartera_resumen.csv"
    detalle = leer_detalle(entrada)
    original = detalle.copy()
    largo = proyectar(detalle)
    ancho, presencia = crear_ancho(largo)
    recuperado = reconstruir(ancho, presencia)
    comprobar_vuelta(largo, recuperado)
    segmentos = resumir_segmentos(detalle)
    exportar({"saldo_ancho.csv": ancho, "presencia_ancho.csv": presencia,
              "saldo_largo_recuperado.csv": recuperado, "saldo_segmento_corte.csv": segmentos},
             entrada, carpeta / "output")
    pd.testing.assert_frame_equal(detalle, original)
    print(f"Largo: {len(largo)} observaciones; ancho: {len(ancho)} IDs y {len(CORTES)} columnas de corte")
    print(f"Vuelta: {len(recuperado)} observaciones; saldos desconocidos={recuperado['saldo_mxn'].isna().sum()}; "
          f"saldo conocido={recuperado['saldo_mxn'].sum(min_count=1)}")
    print(segmentos.to_string(index=False))
    print("Claves, valores y ausencias recuperados; cuatro exportaciones comprobadas; fuente intacta")


if __name__ == "__main__":
    main()

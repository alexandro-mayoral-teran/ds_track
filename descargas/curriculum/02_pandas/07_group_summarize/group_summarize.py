"""Resumir observaciones por corte y segmento con denominadores explícitos."""

from pathlib import Path

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso"]
CLAVES = ["fecha_corte", "segmento"]


def leer_detalle(ruta):
    tabla = pd.read_csv(ruta, dtype={"id_credito": "string", "segmento": "string",
                        "fecha_corte": "string", "saldo_mxn": "Int64", "dias_atraso": "Int64"},
                        encoding="utf-8-sig", keep_default_na=False, na_values=[""])
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Las columnas no coinciden con el diccionario")
    tabla["fecha_corte"] = pd.to_datetime(tabla["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if tabla[["id_credito", "fecha_corte"]].isna().any(axis=None):
        raise ValueError("ID y corte son obligatorios")
    if tabla.duplicated(subset=["id_credito", "fecha_corte"]).any():
        raise ValueError("Resolver claves repetidas antes de resumir")
    if (tabla[["saldo_mxn", "dias_atraso"]] < 0).any(axis=None):
        raise ValueError("La muestra no admite cantidades negativas")
    return tabla


def sumar_conocidos(serie):
    return serie.sum(min_count=1)


def resumir(detalle, claves=CLAVES):
    trabajo = detalle.copy()
    trabajo["atraso_30"] = (trabajo["dias_atraso"] >= 30).astype("boolean")
    resumen = trabajo.groupby(claves, as_index=False, dropna=False, observed=True, sort=True).agg(
        registros=("id_credito", "size"),
        ids_distintos=("id_credito", "nunique"),
        saldos_conocidos=("saldo_mxn", "count"),
        saldo_conocido_mxn=("saldo_mxn", sumar_conocidos),
        saldo_promedio_mxn=("saldo_mxn", "mean"),
        atrasos_conocidos=("dias_atraso", "count"),
        atrasos_30_confirmados=("atraso_30", sumar_conocidos),
    )
    enteras = ["registros", "ids_distintos", "saldos_conocidos", "saldo_conocido_mxn",
               "atrasos_conocidos", "atrasos_30_confirmados"]
    resumen[enteras] = resumen[enteras].astype("Int64")
    resumen["saldo_promedio_mxn"] = resumen["saldo_promedio_mxn"].astype("Float64")
    resumen["cobertura_atraso_pct"] = (resumen["atrasos_conocidos"] / resumen["registros"] * 100).astype("Float64")
    base = resumen["atrasos_conocidos"].where(resumen["atrasos_conocidos"] > 0)
    resumen["atraso_30_pct_conocidos"] = (resumen["atrasos_30_confirmados"] / base * 100).astype("Float64")
    comprobar_resumen(detalle, resumen)
    return resumen


def comprobar_resumen(detalle, resumen):
    if resumen["registros"].sum() != len(detalle):
        raise ValueError("El resumen perdio o duplico filas")
    if resumen["saldos_conocidos"].sum() != detalle["saldo_mxn"].count():
        raise ValueError("No concilian los saldos conocidos")
    if resumen["atrasos_conocidos"].sum() != detalle["dias_atraso"].count():
        raise ValueError("No concilian los atrasos conocidos")
    for campo, esperado in [
        ("saldo_conocido_mxn", detalle["saldo_mxn"].sum(min_count=1)),
        ("atrasos_30_confirmados", (detalle["dias_atraso"] >= 30).sum(min_count=1)),
    ]:
        obtenido = resumen[campo].sum(min_count=1)
        if pd.isna(esperado) != pd.isna(obtenido):
            raise ValueError(f"No coincide la ausencia de {campo}")
        if pd.notna(esperado) and esperado != obtenido:
            raise ValueError(f"No concilia {campo}")


def exportar(resumen, entrada, salida):
    if entrada.resolve() == salida.resolve():
        raise ValueError("La salida no puede reemplazar la fuente")
    salida.parent.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(salida, index=False, encoding="utf-8", date_format="%Y-%m-%d", lineterminator="\n")
    tipos = {c: str(t) for c, t in resumen.dtypes.items() if c != "fecha_corte"}
    if "fecha_corte" in resumen:
        tipos["fecha_corte"] = "string"
    recargada = pd.read_csv(salida, dtype=tipos, keep_default_na=False, na_values=[""])
    if "fecha_corte" in recargada:
        recargada["fecha_corte"] = pd.to_datetime(recargada["fecha_corte"], format="%Y-%m-%d", errors="raise")
    pd.testing.assert_frame_equal(resumen.reset_index(drop=True), recargada,
                                  check_exact=False, rtol=1e-12, atol=1e-12)


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "cartera_resumen.csv"
    detalle = leer_detalle(entrada)
    original = detalle.copy()
    resumen = resumir(detalle)
    pd.testing.assert_frame_equal(detalle, original)
    exportar(resumen, entrada, carpeta / "output" / "resumen_corte_segmento.csv")
    print(f"Detalle: {len(detalle)} filas; resumen: {len(resumen)} grupos")
    print(resumen.to_string(index=False))
    print(f"IDs distintos en todo el detalle: {detalle['id_credito'].nunique()}")
    print(f"Saldo conocido: {detalle['saldo_mxn'].sum(min_count=1)}; saldos desconocidos: {detalle['saldo_mxn'].isna().sum()}")
    print("Conteos y totales conciliados; exportacion comprobada; fuente intacta")


if __name__ == "__main__":
    main()

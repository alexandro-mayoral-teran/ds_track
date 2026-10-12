"""Combinar tablas sin perder observaciones ni multiplicar importes accidentalmente."""

from pathlib import Path

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso"]
CLAVE = ["id_credito", "fecha_corte"]


def leer_detalle(ruta):
    tipos = {"id_credito": "string", "segmento": "string", "fecha_corte": "string",
             "saldo_mxn": "Int64", "dias_atraso": "Int64"}
    tabla = pd.read_csv(ruta, dtype=tipos, encoding="utf-8-sig", keep_default_na=False, na_values=[""])
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Columnas de detalle inesperadas")
    tabla["fecha_corte"] = pd.to_datetime(tabla["fecha_corte"], format="%Y-%m-%d", errors="raise")
    comprobar_clave(tabla)
    if (tabla[["saldo_mxn", "dias_atraso"]] < 0).any(axis=None):
        raise ValueError("La muestra requiere cantidades no negativas")
    return tabla


def comprobar_clave(tabla):
    if tabla[CLAVE].isna().any(axis=None) or tabla.duplicated(subset=CLAVE).any():
        raise ValueError("Resolver claves incompletas o repetidas antes de combinar")


def apilar(septiembre, octubre):
    for tabla in [septiembre, octubre]:
        if list(tabla.columns) != COLUMNAS:
            raise ValueError("Ambas partes deben tener las columnas del contrato")
    if not septiembre.dtypes.equals(octubre.dtypes):
        raise ValueError("Los tipos de ambas partes deben coincidir")
    detalle = pd.concat([septiembre, octubre], ignore_index=True)
    comprobar_clave(detalle)
    detalle.insert(0, "numero_registro", pd.Series(range(1, len(detalle) + 1), dtype="Int64"))
    return detalle


def leer_catalogo(ruta):
    catalogo = pd.read_csv(ruta, dtype="string", keep_default_na=False, na_values=[""])
    if list(catalogo.columns) != ["segmento", "equipo"]:
        raise ValueError("Columnas de catalogo inesperadas")
    return catalogo


def unir_catalogo(detalle, catalogo):
    if catalogo["segmento"].isna().any():
        raise ValueError("El catalogo no admite claves ausentes")
    enriquecido = detalle.merge(catalogo, on="segmento", how="left",
                                validate="many_to_one", indicator="estado_union")
    # Facilitar la exportación sin convertir la ausencia de equipo en coincidencia.
    enriquecido["estado_union"] = enriquecido["estado_union"].astype("string")
    if len(enriquecido) != len(detalle):
        raise ValueError("La union cambio el numero de observaciones")
    pd.testing.assert_frame_equal(
        detalle.sort_values("numero_registro").reset_index(drop=True),
        enriquecido.loc[:, detalle.columns].sort_values("numero_registro").reset_index(drop=True),
    )
    antes = detalle["saldo_mxn"].sum(min_count=1)
    despues = enriquecido["saldo_mxn"].sum(min_count=1)
    if pd.isna(antes) != pd.isna(despues) or (pd.notna(antes) and antes != despues):
        raise ValueError("La union cambio el saldo conocido")
    return enriquecido


def comparar_cortes(detalle):
    campos = ["id_credito", "saldo_mxn"]
    septiembre = detalle.loc[detalle["fecha_corte"] == pd.Timestamp("2026-09-30"), campos]
    octubre = detalle.loc[detalle["fecha_corte"] == pd.Timestamp("2026-10-31"), campos]
    comparacion = septiembre.merge(octubre, on="id_credito", how="outer", validate="one_to_one",
                                   suffixes=("_sep", "_oct"), indicator="presencia")
    comparacion["presencia"] = comparacion["presencia"].astype("string")
    comparacion["cambio_saldo_mxn"] = comparacion["saldo_mxn_oct"] - comparacion["saldo_mxn_sep"]
    return comparacion


def exportar(tablas, fuentes, carpeta):
    rutas = {nombre: carpeta / nombre for nombre in tablas}
    if any(r.resolve() == f.resolve() for r in rutas.values() for f in fuentes):
        raise ValueError("Una salida reemplazaria una fuente")
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, tabla in tablas.items():
        ruta = rutas[nombre]
        tabla.to_csv(ruta, index=False, encoding="utf-8", date_format="%Y-%m-%d", lineterminator="\n")
        tipos = {c: str(t) for c, t in tabla.dtypes.items() if c != "fecha_corte"}
        if "fecha_corte" in tabla:
            tipos["fecha_corte"] = "string"
        recargada = pd.read_csv(ruta, dtype=tipos, keep_default_na=False, na_values=[""])
        if "fecha_corte" in recargada:
            recargada["fecha_corte"] = pd.to_datetime(recargada["fecha_corte"], format="%Y-%m-%d", errors="raise")
        pd.testing.assert_frame_equal(tabla.reset_index(drop=True), recargada, check_exact=True)


def main():
    carpeta = Path(__file__).resolve().parent
    fuente_detalle = carpeta.parent / "07_group_summarize" / "cartera_resumen.csv"
    fuente_catalogo = carpeta / "catalogo_segmentos.csv"
    fuente = leer_detalle(fuente_detalle)
    original = fuente.copy()
    septiembre = fuente.loc[fuente["fecha_corte"] == pd.Timestamp("2026-09-30")].copy()
    octubre = fuente.loc[fuente["fecha_corte"] == pd.Timestamp("2026-10-31")].copy()
    # Este ejemplo trabaja solo con los dos cortes acordados: no omitir otro sin avisar.
    if len(septiembre) + len(octubre) != len(fuente):
        raise ValueError("Hay cortes fuera del alcance del ejemplo")
    detalle = apilar(septiembre, octubre)
    catalogo = leer_catalogo(fuente_catalogo)
    enriquecido = unir_catalogo(detalle, catalogo)
    sin_catalogo = enriquecido.loc[enriquecido["estado_union"] == "left_only"].copy()
    comparacion = comparar_cortes(detalle)
    exportar({"detalle_enriquecido.csv": enriquecido, "sin_catalogo.csv": sin_catalogo,
              "comparacion_cortes.csv": comparacion},
             [fuente_detalle, fuente_catalogo], carpeta / "output")
    pd.testing.assert_frame_equal(fuente, original)
    print(f"Concat: {len(septiembre)} + {len(octubre)} = {len(detalle)} observaciones")
    print(f"Left: {len(enriquecido)} filas; saldo conocido={enriquecido['saldo_mxn'].sum(min_count=1)}")
    print(enriquecido["estado_union"].value_counts().to_string())
    print(f"Sin catalogo: {len(sin_catalogo)} filas; saldo conocido={sin_catalogo['saldo_mxn'].sum(min_count=1)}")
    print(f"Comparacion: {len(comparacion)} IDs; cambios evaluables={comparacion['cambio_saldo_mxn'].count()}; "
          f"cambio de la base evaluable={comparacion['cambio_saldo_mxn'].sum(min_count=1)}")
    print("Exportaciones comprobadas; fuentes intactas")


if __name__ == "__main__":
    main()

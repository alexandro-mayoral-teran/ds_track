"""Leer y validar los CSV; extracción del lector de 04.04."""

from pathlib import Path

import pandas as pd

from .reglas import GROUPS


def read_detail(source: str | Path) -> pd.DataFrame:
    """Leer cortes.csv/creditos.csv y devolver detalle validado y ordenado.

    source designa la carpeta de entrada. Conserva claves textuales y ceros
    iniciales; saldo_mxn/dias_atraso usan Int64 con ausencias permitidas.
    La salida tiene id_credito, fecha_corte, saldo_mxn, dias_atraso y segmento,
    con clave crédito/fecha única e índice nuevo, ordenada por fecha/crédito.
    Solo admite segmentos GROUPS, fechas YYYY-MM-DD y números no negativos.
    CSV con cabeceras y sin registros produce tabla vacía con estructura.

    Lee archivos sin modificarlos. Lanza ValueError por incumplimientos del
    contrato o conversión; propaga errores de lectura como FileNotFoundError.
    El llamador proporciona str o Path: la anotación no comprueba ese tipo.
    """
    source = Path(source)
    cuts = pd.read_csv(source / "cortes.csv", dtype={"id_credito": "string",
        "fecha_corte": "string", "saldo_mxn": "Int64", "dias_atraso": "Int64"},
        keep_default_na=False, na_values=[""])
    credits = pd.read_csv(source / "creditos.csv", dtype="string", keep_default_na=False)
    if list(cuts.columns) != ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"]:
        raise ValueError("Columnas de cortes distintas del contrato")
    if list(credits.columns) != ["id_credito", "id_cliente", "segmento"]:
        raise ValueError("Columnas de créditos distintas del contrato")
    if cuts[["id_credito", "fecha_corte"]].isna().any().any() or cuts.duplicated(["id_credito", "fecha_corte"]).any():
        raise ValueError("Clave crédito/fecha inválida")
    if credits["id_credito"].str.strip().eq("").any() or credits["id_credito"].duplicated().any():
        raise ValueError("Clave de crédito inválida")
    if not credits["segmento"].isin(GROUPS).all():
        raise ValueError("Segmento fuera del contrato")
    dates = pd.to_datetime(cuts["fecha_corte"], format="%Y-%m-%d", errors="raise")
    if not dates.dt.strftime("%Y-%m-%d").eq(cuts["fecha_corte"]).all():
        raise ValueError("Formato de fecha inesperado")
    if cuts[["saldo_mxn", "dias_atraso"]].lt(0).any().any():
        raise ValueError("Valores negativos fuera del contrato sintético")
    detail = cuts.merge(credits[["id_credito", "segmento"]], on="id_credito",
                        how="left", validate="many_to_one", indicator=True)
    if not detail["_merge"].eq("both").all():
        raise ValueError("Corte sin crédito correspondiente")
    return detail.drop(columns="_merge").sort_values(["fecha_corte", "id_credito"]).reset_index(drop=True)

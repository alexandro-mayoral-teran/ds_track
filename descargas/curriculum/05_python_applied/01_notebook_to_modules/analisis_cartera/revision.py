"""05.05: obtener un resumen para revisión sin exportar una entrega."""

from pathlib import Path

import pandas as pd

from .contratos import normalize_cut
from .flujo import build_analysis
from .reglas import GROUPS


def review_summary(
    source: str | Path,
    cut: str | None = None,
    *,
    segments: list[str] | None = None,
) -> pd.DataFrame:
    """Leer y conciliar un corte, y devolver sus segmentos en el orden pedido.

    source es una carpeta con los CSV de read_detail. cut sigue normalize_cut:
    None usa 2026-10-31. segments=None conserva todos los grupos; [] devuelve
    cero filas con las mismas columnas/tipos. Una lista explícita debe contener
    nombres de GROUPS sin duplicados y define el orden de salida.

    Retorna una tabla nueva con segmento, registros, conocidos, mediana_mxn,
    cobertura_pct, fecha_corte, etiqueta y fraccion. La mediana usa saldos
    conocidos; cobertura está en escala 0–100. Conserva grupos sin filas
    o sin saldos conocidos. Las ausencias se consultan con pandas.isna.

    Lanza TypeError por tipos incompatibles; ValueError por opciones, datos o
    conciliación inválidos. Propaga OSError (incluido FileNotFoundError) de la
    lectura. Valida opciones antes de leer, pero incluso segments=[] lee y
    concilia la fuente. No modifica la lista recibida ni escribe archivos.
    """
    if not isinstance(source, (str, Path)):
        raise TypeError("source debe ser str o Path")
    if isinstance(source, str) and not source.strip():
        raise ValueError("source no puede ser texto vacío")
    cut = normalize_cut(cut)
    if segments is not None:
        if not isinstance(segments, list) or any(not isinstance(s, str) for s in segments):
            raise TypeError("segments debe ser list[str] o None")
        if len(set(segments)) != len(segments):
            raise ValueError("segments no admite duplicados")
        if any(s not in GROUPS for s in segments):
            raise ValueError("Segmento fuera del contrato")
    summary = build_analysis(source, cut)["resumen"]
    if segments is None:
        return summary.copy(deep=True)
    return summary.set_index("segmento").loc[segments].reset_index().copy(deep=True)

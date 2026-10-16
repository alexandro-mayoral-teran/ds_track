"""05.05: contratos pequeños con anotaciones y comprobaciones explícitas."""

from datetime import datetime

DEFAULT_CUT = "2026-10-31"


def coverage_pct(known: int, total: int) -> float | None:
    """Calcular cobertura porcentual (0–100) sin inventar una base.

    known y total son conteos int de Python, excluyendo bool. Deben cumplir
    0 <= known <= total. Retorna None únicamente cuando ambos son cero;
    con total positivo retorna un float entre 0 y 100, incluido cero.

    Lanza TypeError ante tipos incompatibles y ValueError ante conteos fuera
    de ese dominio. No convierte textos ni modifica objetos del llamador.
    """
    if (isinstance(known, bool) or not isinstance(known, int)
            or isinstance(total, bool) or not isinstance(total, int)):
        raise TypeError("known y total deben ser conteos int, sin bool")
    if not 0 <= known <= total:
        raise ValueError("Los conteos deben cumplir 0 <= known <= total")
    if total == 0:
        return None
    return 100 * known / total


def normalize_cut(cut: str | None = None) -> str:
    """Resolver None al corte didáctico fijo y exigir fecha YYYY-MM-DD.

    None significa DEFAULT_CUT (2026-10-31), no fecha de hoy ni último corte
    del archivo. No acepta texto vacío ni fechas sin ceros iniciales.
    Lanza TypeError para otros tipos y ValueError para textos inválidos.
    No lee archivos ni convierte silenciosamente otros objetos a texto.
    """
    if cut is None:
        return DEFAULT_CUT
    if not isinstance(cut, str):
        raise TypeError("cut debe ser str o None")
    parsed = datetime.strptime(cut, "%Y-%m-%d")
    if parsed.strftime("%Y-%m-%d") != cut:
        raise ValueError("cut debe conservar el formato YYYY-MM-DD")
    return cut

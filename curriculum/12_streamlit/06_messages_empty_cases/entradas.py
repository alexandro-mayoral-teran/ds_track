"""Interpretación de filtros de interfaz; no cambia el contrato del CSV."""

import re
from cartera import MAXIMO_MXN, SEGMENTOS, validar_fecha


def preparar_filtros(corte, segmentos, minimo_texto):
    """Devuelve parámetros nuevos o rechaza el intento sin cambiar una sesión."""
    validar_fecha(corte)
    if not isinstance(segmentos, (list, tuple)) or any(s not in SEGMENTOS for s in segmentos):
        raise ValueError("Elige segmentos del catálogo; una lista vacía significa ninguno.")
    if len(segmentos) != len(set(segmentos)):
        raise ValueError("No repitas segmentos.")
    if not isinstance(minimo_texto, str):
        raise ValueError("Escribe el mínimo como texto de pesos enteros.")
    texto = minimo_texto.strip()  # Solo espacios exteriores del campo de interfaz.
    if not re.fullmatch(r"0|[1-9][0-9]{0,6}", texto):
        raise ValueError("Escribe un entero de 0 a 1000000 MXN, por ejemplo 2000; sin comas, signos ni decimales.")
    minimo = int(texto)
    if minimo > MAXIMO_MXN:
        raise ValueError("El mínimo debe estar entre 0 y 1000000 MXN.")
    return {"corte": corte, "segmentos": list(segmentos), "minimo_mxn": minimo}

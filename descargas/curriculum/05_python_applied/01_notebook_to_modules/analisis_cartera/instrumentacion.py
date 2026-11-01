"""05.08: envolver funciones normales con mensajes sin configurar logging."""

from functools import wraps
import inspect
import logging
from pathlib import Path

import pandas as pd

from .iteracion import batch_indicators

LOGGER = logging.getLogger(__name__)


def log_call(function):
    """Envolver una función Python normal para registrar inicio/fin/falla.

    No ejecuta function al decorar. La envoltura reenvía argumentos y devuelve
    el mismo objeto resultado, sin copiar, validar, consumir ni reintentar.
    Ante Exception registra falla y propaga la misma excepción con raise.
    Interrupciones como KeyboardInterrupt/SystemExit se propagan sin anunciar
    éxito. Requiere un sistema de logging funcional; no garantiza tolerancia
    a fallas de handlers personalizados. No registra valores de argumentos,
    resultados ni mensajes de excepciones y no configura handlers/niveles.

    Acepta funciones normales, no cualquier objeto callable. Rechaza funciones
    generadoras/corutinas/generadoras asíncronas declaradas como tales. Una
    función normal puede devolver un iterador: el fin registra solo el retorno,
    no su consumo. wraps conserva metadatos y un enlace __wrapped__, sin
    reconstruir la firma ejecutable ni certificar tipos estáticos.
    """
    if not inspect.isfunction(function):
        raise TypeError("log_call requiere una función Python normal")
    if (inspect.isgeneratorfunction(function) or inspect.iscoroutinefunction(function)
            or inspect.isasyncgenfunction(function)):
        raise TypeError("log_call no instrumenta consumo de generadores ni funciones async")

    @wraps(function)
    def wrapped(*args, **kwargs):
        LOGGER.info("Inicio: %s", function.__name__)
        try:
            result = function(*args, **kwargs)
        except Exception:
            LOGGER.warning("Falla: %s", function.__name__)
            raise
        else:
            LOGGER.info("Fin: %s", function.__name__)
            return result

    return wrapped


@log_call
def logged_indicators(
    source: str | Path, cut: str | None = None, *, batch_size: int = 10,
) -> pd.DataFrame:
    """Calcular los indicadores de 05.07 con registro alrededor de su ejecución.

    Conserva contrato, validaciones y lectura por lotes de batch_indicators.
    No escribe entregas ni consume una fuente adicional para registrar datos.
    Fin indica que esta llamada retornó; no acredita revisión ni aprendizaje.
    """
    return batch_indicators(source, cut, batch_size=batch_size)

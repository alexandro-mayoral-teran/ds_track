"""05.09: experimentos pequeños, con instrumentos y fronteras explícitos."""

from collections.abc import Callable, Iterable
import cProfile
import io
import pstats
import sys
from time import perf_counter
import tracemalloc

import pandas as pd

from .contratos import normalize_cut


def validate_dates_each(dates: Iterable[str]) -> int:
    """Validar cada texto YYYY-MM-DD y retornar cantidad; consumir una vez.

    No acepta None ni convierte tipos. Propaga TypeError/ValueError antes de
    retornar un conteo de éxito. No modifica la entrada ni conserva una caché.
    """
    count = 0
    for date in dates:
        if not isinstance(date, str):
            raise TypeError("Cada fecha debe ser str")
        normalize_cut(date)
        count += 1
    return count


def validate_dates_reusing(dates: Iterable[str]) -> int:
    """Mismo resultado/reglas; reutilizar fechas válidas solo dentro de esta llamada.

    Conserva un conjunto de textos ya validados: memoria adicional según fechas
    distintas. No salta filas, no cambia el orden de consumo y no persiste caché.
    """
    seen = set()
    count = 0
    for date in dates:
        if not isinstance(date, str):
            raise TypeError("Cada fecha debe ser str")
        if date not in seen:
            normalize_cut(date)
            seen.add(date)
        count += 1
    return count


def _count_option(value: int, name: str, minimum: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} debe ser int, sin bool")
    if value < minimum:
        raise ValueError(f"{name} debe ser al menos {minimum}")


def _profile_active() -> bool:
    # cProfile de CPython 3.12 usa monitoring, sin aparecer en getprofile().
    # Solo consultar el espacio reservado: no apropiarse de sesiones ajenas.
    monitoring = getattr(sys, "monitoring", None)
    return (sys.getprofile() is not None or
            (monitoring is not None and monitoring.get_tool(monitoring.PROFILER_ID) is not None))


def repeat_timings(
    operations: dict[str, Callable], *, repeats: int = 5, warmups: int = 1,
    check: Callable | None = None,
) -> pd.DataFrame:
    """Cronometrar funciones sin argumentos, con calentamiento y orden alterno.

    Una fila por variante/repetición, en orden real. Segundos perf_counter:
    llamada y retorno, sin check, almacenamiento de filas ni destrucción del
    resultado retornado. check, si existe, recibe cada resultado fuera del reloj,
    también en calentamientos. El llamador debe preparar entradas repetibles y
    consumir cualquier resultado diferido que forme parte del trabajo medido.

    No inicia procesos, no reinicia entradas ni promete resultados equivalentes.
    Rechaza tracemalloc o un perfilador activos para separar instrumentos.
    Fallas de la operación/check se propagan sin devolver tabla parcial.
    """
    _count_option(repeats, "repeats", 1)
    _count_option(warmups, "warmups", 0)
    if not isinstance(operations, dict) or not operations:
        raise ValueError("operations debe ser un diccionario no vacío")
    if any(not isinstance(name, str) or not name or not callable(op)
           for name, op in operations.items()):
        raise TypeError("Cada variante requiere nombre str y operación callable")
    if check is not None and not callable(check):
        raise TypeError("check debe ser callable o None")
    if tracemalloc.is_tracing() or _profile_active():
        raise RuntimeError("Cronometrar sin tracemalloc ni perfilador activos")
    for operation in operations.values():
        for _ in range(warmups):
            result = operation()
            if check is not None:
                check(result)
            del result
    rows = []
    names = list(operations)
    for repetition in range(1, repeats + 1):
        order = names if repetition % 2 else list(reversed(names))
        for position, name in enumerate(order, start=1):
            start = perf_counter()
            result = operations[name]()
            seconds = perf_counter() - start
            if check is not None:
                check(result)
            rows.append({"variante": name, "repeticion": repetition,
                         "posicion": position, "segundos": seconds})
            del result
    return pd.DataFrame(rows)


def trace_peak(operation: Callable, *, check: Callable | None = None) -> dict[str, int]:
    """Medir una llamada con tracemalloc; no es RSS ni memoria total del proceso.

    Mantiene el resultado vivo hasta leer actual/pico. Entradas ya preparadas
    antes de start no se incluyen como nuevas asignaciones. No cronometra.
    Rechaza una sesión de trazado/perfilado previa sin reiniciarla ni borrarla.
    Detiene la sesión propia incluso si operation falla. check ocurre después
    de detenerla. Propaga fallas; no devuelve medición de éxito para un error.
    """
    if not callable(operation) or (check is not None and not callable(check)):
        raise TypeError("operation/check deben ser callable")
    if tracemalloc.is_tracing() or _profile_active():
        raise RuntimeError("La medición requiere instrumentos inicialmente inactivos")
    tracemalloc.start()
    try:
        result = operation()
        current, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    if check is not None:
        check(result)
    return {"actual_trazada_bytes": current, "pico_trazado_bytes": peak}


def profile_operation(operation: Callable, *, limit: int = 12) -> str:
    """Devolver perfil cProfile por tiempo acumulado, sin rutas completas.

    Ejecuta una llamada, sin tracemalloc ni otro perfilador activos. No es
    benchmark: el instrumento añade costo. runcall desactiva el perfil propio
    también al fallar; la excepción de la operación se propaga.
    """
    _count_option(limit, "limit", 1)
    if not callable(operation):
        raise TypeError("operation debe ser callable")
    if tracemalloc.is_tracing() or _profile_active():
        raise RuntimeError("El perfil requiere instrumentos inicialmente inactivos")
    profiler = cProfile.Profile()
    profiler.runcall(operation)
    stream = io.StringIO()
    pstats.Stats(profiler, stream=stream).strip_dirs().sort_stats("cumulative").print_stats(limit)
    return stream.getvalue()

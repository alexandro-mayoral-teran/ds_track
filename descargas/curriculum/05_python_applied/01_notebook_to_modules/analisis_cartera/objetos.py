"""05.06: objetos pequeños opcionales sobre las funciones ya comprobadas."""

from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from .contratos import DEFAULT_CUT, coverage_pct, normalize_cut
from .reglas import GROUPS
from .revision import review_summary


class CoverageCounts:
    """Ejemplo de clase manual: reunir dos conteos y una operación conocida.

    Los atributos son públicos y mutables. __init__ valida el estado inicial;
    percentage vuelve a validarlo porque una reasignación puede invalidarlo.
    No es necesario usar esta clase para calcular una cobertura aislada.
    """

    def __init__(self, known: int, total: int) -> None:
        coverage_pct(known, total)
        self.known = known
        self.total = total

    def percentage(self) -> float | None:
        """Calcular desde el estado actual; no almacenar un resultado obsoleto."""
        return coverage_pct(self.known, self.total)


@dataclass(frozen=True)
class ReviewOptions:
    """Agrupar opciones de revisión que pueden reutilizarse sin reasignarlas.

    cut exige texto YYYY-MM-DD y por defecto es el corte didáctico fijo.
    segments=None conserva todos; () pide ninguno; una tupla de nombres
    únicos de GROUPS fija el orden. No convierte listas ni acepta cut=None.
    __post_init__ valida tipos/valores; la dataclass por sí sola no los valida.
    No lee fuentes. frozen bloquea asignaciones normales; los campos elegidos
    contienen solo texto, tupla de textos o None, sin listas anidadas mutables.
    """

    cut: str = DEFAULT_CUT
    segments: tuple[str, ...] | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.cut, str):
            raise TypeError("cut de ReviewOptions debe ser str")
        normalize_cut(self.cut)
        if self.segments is not None:
            if (not isinstance(self.segments, tuple)
                    or any(not isinstance(s, str) for s in self.segments)):
                raise TypeError("segments de ReviewOptions debe ser tuple[str, ...] o None")
            if len(set(self.segments)) != len(self.segments):
                raise ValueError("segments no admite duplicados")
            if any(s not in GROUPS for s in self.segments):
                raise ValueError("Segmento fuera del contrato")


@dataclass(frozen=True)
class ReviewJob:
    """Componer una fuente y unas opciones sin guardar tablas ni recursos.

    Crear el objeto valida opciones/forma de la ruta, sin leer ni escribir.
    source admite str no vacío o Path; las rutas relativas se interpretan
    respecto del directorio de trabajo al llamar summary, como en 05.05.
    options debe ser ReviewOptions; la fábrica crea unas opciones por defecto.
    summary lee y concilia en cada llamada: no es caché ni una instantánea.
    """

    source: str | Path
    options: ReviewOptions = field(default_factory=ReviewOptions)

    def __post_init__(self) -> None:
        if not isinstance(self.source, (str, Path)):
            raise TypeError("source debe ser str o Path")
        if isinstance(self.source, str) and not self.source.strip():
            raise ValueError("source no puede ser texto vacío")
        if not isinstance(self.options, ReviewOptions):
            raise TypeError("options debe ser ReviewOptions")

    def summary(self) -> pd.DataFrame:
        """Delegar en 05.05; propagar sus errores y devolver una tabla nueva.

        Incluso segments=() valida las fuentes. No modifica opciones/fuentes
        ni exporta entregas. La conversión tupla -> lista es explícita para
        respetar la interfaz existente de review_summary.
        """
        segments = None if self.options.segments is None else list(self.options.segments)
        return review_summary(self.source, self.options.cut, segments=segments)

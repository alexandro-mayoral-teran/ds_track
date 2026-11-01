"""05.07: consumir iteradores por lotes sin reunir todos los registros CSV."""

from collections.abc import Iterable, Iterator
import csv
from itertools import islice
from pathlib import Path
import re
import statistics

import pandas as pd

from .contratos import coverage_pct, normalize_cut
from .reglas import GROUPS


def _validate_size(size: int) -> None:
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size debe ser int, sin bool")
    if size <= 0:
        raise ValueError("size debe ser positivo")


def iter_batches(items: Iterable, size: int) -> Iterator[list]:
    """Entregar listas nuevas de hasta size elementos, en orden de consumo.

    Es una función generadora: tamaño y entrada se examinan al consumir,
    no al crear el generador. Acepta cualquier iterable; no anota aquí el
    tipo de sus elementos. Conserva un último lote corto y no entrega lotes
    vacíos. No copia profundamente elementos ni cierra el recurso de entrada.
    El llamador conserva la responsabilidad de abrir/cerrar archivos.
    """
    _validate_size(size)
    iterator = iter(items)
    while True:
        batch = list(islice(iterator, size))
        if not batch:
            return
        yield batch


def _check_row(row: dict, columns: list[str]) -> None:
    # DictReader usa None como clave para extras y como valor para faltantes.
    if list(row) != columns or any(value is None for value in row.values()):
        raise ValueError("Fila CSV con campos faltantes o adicionales")


def _optional_integer(text: str) -> int | None:
    if text == "":
        return None
    if re.fullmatch(r"[0-9]+", text) is None:
        raise ValueError("Se esperaba entero decimal no negativo o campo vacío")
    value = int(text)
    # Misma capacidad de representación que Int64 del lector de referencia.
    if value > 2**63 - 1:
        raise ValueError("Entero fuera del rango Int64")
    return value


def _load_groups(source: Path) -> dict[str, str]:
    columns = ["id_credito", "id_cliente", "segmento"]
    groups = {}
    with (source / "creditos.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        if reader.fieldnames != columns:
            raise ValueError("Columnas de créditos distintas del contrato")
        for row in reader:
            _check_row(row, columns)
            credit = row["id_credito"]
            if not credit.strip() or credit in groups:
                raise ValueError("Clave de crédito inválida")
            if row["segmento"] not in GROUPS:
                raise ValueError("Segmento fuera del contrato")
            groups[credit] = row["segmento"]
    return groups


def batch_indicators(
    source: str | Path, cut: str | None = None, *, batch_size: int = 10,
) -> pd.DataFrame:
    """Calcular indicadores desde CSV por lotes, conservando saldos para mediana.

    Retorna segmento, registros, conocidos, mediana_mxn y cobertura_pct para
    GROUPS y Todos. Valida todas las filas, también fuera del corte pedido.
    No modifica fuentes ni escribe entregas. Propaga errores de lectura y
    lanza ValueError por esquema, claves, relación, fecha o enteros inválidos.
    Propaga csv.Error ante sintaxis CSV inválida, como comillas sin cierre.
    Los enteros CSV admiten solo dígitos ASCII o vacío, hasta máximo Int64;
    no son conversiones generales de cualquier texto aceptado por pandas.

    Es una función normal: lee al llamarla y retorna solo si terminó el archivo.
    Conserva catálogo, claves vistas y saldos conocidos del corte para mediana
    exacta: NO garantiza memoria constante. El tamaño limita filas por lote,
    no bytes totales. Los archivos están dentro de with, incluso ante fallas.
    """
    _validate_size(batch_size)
    cut = normalize_cut(cut)
    if not isinstance(source, (str, Path)):
        raise TypeError("source debe ser str o Path")
    if isinstance(source, str) and not source.strip():
        raise ValueError("source no puede ser texto vacío")
    source = Path(source)
    groups = _load_groups(source)
    counts = {group: 0 for group in GROUPS}
    values = {group: [] for group in GROUPS}
    seen = set()
    columns = ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso"]
    with (source / "cortes.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        if reader.fieldnames != columns:
            raise ValueError("Columnas de cortes distintas del contrato")
        for batch in iter_batches(reader, batch_size):
            for row in batch:
                _check_row(row, columns)
                credit, date = row["id_credito"], row["fecha_corte"]
                normalize_cut(date)
                key = (credit, date)
                if not credit.strip() or key in seen:
                    raise ValueError("Clave crédito/fecha inválida")
                seen.add(key)
                if credit not in groups:
                    raise ValueError("Corte sin crédito correspondiente")
                balance = _optional_integer(row["saldo_mxn"])
                _optional_integer(row["dias_atraso"])
                if date == cut:
                    group = groups[credit]
                    counts[group] += 1
                    if balance is not None:
                        values[group].append(balance)
    # Combinar valores conocidos, nunca promediar medianas de lotes/grupos.
    all_values = [value for group in GROUPS for value in values[group]]
    rows = []
    for group in [*GROUPS, "Todos"]:
        known = all_values if group == "Todos" else values[group]
        total = sum(counts.values()) if group == "Todos" else counts[group]
        rows.append({"segmento": group, "registros": total, "conocidos": len(known),
                     "mediana_mxn": float(statistics.median(known)) if known else None,
                     "cobertura_pct": coverage_pct(len(known), total)})
    return pd.DataFrame(rows)

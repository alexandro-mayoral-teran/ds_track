"""05.10: recibir páginas JSON, validar y retornar solo un detalle completo.

Contrato didáctico propio, no cliente universal de APIs. GET sin credenciales,
paginas consecutivas, total estable y registros del detalle conocido.
"""

from collections.abc import Callable
import json
import logging
import math
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

import pandas as pd

from .contratos import normalize_cut
from .reglas import GROUPS

LOGGER = logging.getLogger(__name__)
COLUMNS = ["id_credito", "fecha_corte", "saldo_mxn", "dias_atraso", "segmento"]


class ApiError(ValueError):
    """No se completó una extracción conforme al contrato de esta lección."""


def _integer(value, name, minimum=0):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ApiError(f"{name} debe ser int >= {minimum}, sin bool")


def _seconds(value, name, *, positive):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or value < 0 or (positive and value == 0)):
        raise ApiError(f"{name} debe ser un número finito {'positivo' if positive else 'no negativo'}")


def _unique_object(pairs):
    # json.loads normalmente conservaría solo el último valor de una clave repetida.
    result = {}
    for key, value in pairs:
        if key in result:
            raise ApiError("JSON con nombre de campo repetido")
        result[key] = value
    return result


def _no_constant(value):
    raise ApiError("JSON con constante no estándar")


def _page_json(response):
    content_type = response["content_type"]
    if not isinstance(content_type, str) or content_type.split(";", 1)[0].strip().lower() != "application/json":
        raise ApiError("La respuesta 200 no declara application/json")
    if not isinstance(response["body"], str):
        raise ApiError("El transporte debe entregar body como texto UTF-8")
    try:
        payload = json.loads(response["body"], object_pairs_hook=_unique_object,
                             parse_constant=_no_constant)
    except json.JSONDecodeError as exc:
        raise ApiError("El cuerpo no es JSON válido") from exc
    if not isinstance(payload, dict) or set(payload) != {"items", "next_page", "total"}:
        raise ApiError("La página requiere exactamente items, next_page y total")
    if not isinstance(payload["items"], list):
        raise ApiError("items debe ser una lista")
    _integer(payload["total"], "total")
    return payload


def _validate_item(item):
    if not isinstance(item, dict) or set(item) != set(COLUMNS):
        raise ApiError("Registro con columnas distintas del contrato")
    identifier = item["id_credito"]
    if not isinstance(identifier, str) or not identifier or identifier.strip() != identifier:
        raise ApiError("id_credito debe ser texto no vacío, sin espacios extremos")
    if not isinstance(item["fecha_corte"], str):
        raise ApiError("fecha_corte debe ser texto presente")
    try:
        normalize_cut(item["fecha_corte"])
    except ValueError as exc:
        raise ApiError("fecha_corte fuera del calendario/formato") from exc
    for name in ["saldo_mxn", "dias_atraso"]:
        value = item[name]
        if value is not None:
            _integer(value, name)
            if value > 2**63 - 1:
                raise ApiError(f"{name} fuera del rango Int64")
    if not isinstance(item["segmento"], str) or item["segmento"] not in GROUPS:
        raise ApiError("segmento fuera del catálogo")


def fetch_detail(fetch: Callable, *, timeout=5.0, max_attempts=2, retry_delay=0.25,
                 max_pages=3, max_rows=100, wait: Callable = time.sleep) -> pd.DataFrame:
    """Extraer desde página 1 y retornar un DataFrame validado, ordenado y tipado.

    fetch(page, timeout) retorna dict con status int, content_type str,
    retry_after str|None y body str. Reintentar SOLO TimeoutError (directo o
    dentro de URLError) y 503 sin Retry-After. max_attempts incluye el inicial,
    por página, entre 1 y 5; pausa fija retry_delay entre 0 y 5 segundos.
    Otros URLError/estados/esquemas fallan. wait recibe segundos; se inyecta en tests.

    Exige páginas consecutivas, total constante, claves crédito/fecha únicas y
    segmento estable por crédito. null en números conserva ausencia. No escribe,
    no modifica respuestas ni retorna resultados parciales. Reúne todo el detalle
    en memoria con límites de páginas/filas; no es streaming ni snapshot remoto.
    timeout limita operaciones bloqueantes del transporte HTTP, no tiempo total.
    """
    if not callable(fetch) or not callable(wait):
        raise ApiError("fetch y wait deben ser funciones")
    _seconds(timeout, "timeout", positive=True)
    _seconds(retry_delay, "retry_delay", positive=False)
    _integer(max_attempts, "max_attempts", 1)
    _integer(max_pages, "max_pages", 1)
    _integer(max_rows, "max_rows")
    if max_attempts > 5 or retry_delay > 5:
        raise ApiError("Esta práctica limita intentos/pausa a 5")
    records, seen, segments = [], set(), {}
    page, expected_total = 1, None
    while True:
        if page > max_pages:
            raise ApiError("Se alcanzó max_pages sin terminar")
        for attempt in range(1, max_attempts + 1):
            try:
                response = fetch(page, timeout)
            except (TimeoutError, URLError) as exc:
                if isinstance(exc, URLError) and not isinstance(exc.reason, TimeoutError):
                    raise ApiError(f"Error de conexión en página {page}; no reintentar automáticamente") from exc
                LOGGER.info("Página=%s intento=%s estado=timeout", page, attempt)
                if attempt == max_attempts:
                    raise ApiError(f"Timeout agotado en página {page}") from exc
            else:
                if not isinstance(response, dict) or set(response) != {"status", "content_type", "retry_after", "body"}:
                    raise ApiError("Sobre del transporte incompatible")
                status = response["status"]
                _integer(status, "status", 100)
                LOGGER.info("Página=%s intento=%s estado=%s", page, attempt, status)
                if status == 200:
                    break
                if status != 503 or response["retry_after"] is not None:
                    raise ApiError(f"HTTP {status} en página {page}; revisar antes de repetir")
                if attempt == max_attempts:
                    raise ApiError(f"HTTP 503 agotado en página {page}")
            wait(retry_delay)
        payload = _page_json(response)
        if expected_total is None:
            expected_total = payload["total"]
            if expected_total > max_rows:
                raise ApiError("total supera max_rows")
        if payload["total"] != expected_total:
            raise ApiError("El total cambió entre páginas")
        if len(records) + len(payload["items"]) > expected_total:
            raise ApiError("Hay más registros que el total declarado")
        for item in payload["items"]:
            _validate_item(item)
            key = (item["id_credito"], item["fecha_corte"])
            if key in seen:
                raise ApiError("Clave crédito/fecha duplicada entre registros/páginas")
            identifier, segment = item["id_credito"], item["segmento"]
            if identifier in segments and segments[identifier] != segment:
                raise ApiError("El segmento de un crédito cambió entre cortes")
            seen.add(key)
            segments[identifier] = segment
            records.append(item.copy())
        next_page = payload["next_page"]
        if next_page is None:
            if len(records) != expected_total:
                raise ApiError("La extracción terminó sin conciliar el total")
            break
        _integer(next_page, "next_page", 1)
        if next_page != page + 1 or not payload["items"]:
            raise ApiError("La paginación no avanza consecutivamente con registros")
        page = next_page
    # Construir arrays tipados directamente evita pasar enteros grandes con
    # ausencias por float64 y perder precisión antes de convertir a Int64.
    detail = pd.DataFrame({column: pd.array([row[column] for row in records],
                           dtype="Int64" if column in ["saldo_mxn", "dias_atraso"] else "string")
                           for column in COLUMNS})
    return detail.sort_values(["fecha_corte", "id_credito"]).reset_index(drop=True)


def simulation_transport(scenario_path: str | Path) -> Callable:
    """Preparar una secuencia local de respuestas; no usa la red ni duerme.

    Cada paso declara page y error=timeout, o status/content_type/retry_after y
    body_file relativo a la carpeta del escenario. Agotarla/fuera de orden falla.
    Crear un transporte NUEVO para repetir: la secuencia es consumible.
    """
    path = Path(scenario_path).resolve()
    steps = iter(json.loads(path.read_text(encoding="utf-8"))["steps"])

    def fetch(page, timeout):
        try:
            step = next(steps)
        except StopIteration as exc:
            raise ApiError("La simulación no tiene más respuestas") from exc
        if step["page"] != page:
            raise ApiError("La solicitud no coincide con la página de la simulación")
        if step.get("error") == "timeout":
            raise TimeoutError("Espera simulada")
        body_path = (path.parent / step["body_file"]).resolve()
        if not body_path.is_relative_to(path.parent):
            raise ApiError("body_file debe permanecer dentro de la muestra local")
        return {"status": step["status"], "content_type": step["content_type"],
                "retry_after": step["retry_after"], "body": body_path.read_text(encoding="utf-8")}

    return fetch


def http_transport(endpoint: str, *, max_bytes=65536) -> Callable:
    """Preparar GET HTTPS ?page=N con timeout y cuerpo UTF-8 acotado por respuesta.

    No conecta al preparar; la llamada fetch conecta. Endpoint sin consulta,
    fragmento ni credenciales. urllib usa su política normal de redirecciones,
    certificados y proxies. No implementa autenticación ni descompresión.
    """
    parts = urlsplit(endpoint)
    if (parts.scheme != "https" or not parts.hostname or parts.query or parts.fragment
            or parts.username is not None or parts.password is not None):
        raise ApiError("Usa endpoint HTTPS sin consulta, fragmento ni credenciales")
    _integer(max_bytes, "max_bytes", 1)

    def fetch(page, timeout):
        _integer(page, "page", 1)
        _seconds(timeout, "timeout", positive=True)
        request = Request(endpoint + "?" + urlencode({"page": page}), method="GET",
                          headers={"Accept": "application/json", "User-Agent": "DS-Track/05.10"})
        try:
            response = urlopen(request, timeout=timeout)
        except HTTPError as exc:
            response = exc  # Es también una respuesta que debemos cerrar.
        with response:
            raw = response.read(max_bytes + 1)
            if len(raw) > max_bytes:
                raise ApiError("El cuerpo supera max_bytes")
            try:
                body = raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                raise ApiError("El cuerpo no es UTF-8") from exc
            return {"status": response.status, "content_type": response.headers.get("Content-Type", ""),
                    "retry_after": response.headers.get("Retry-After"), "body": body}

    return fetch

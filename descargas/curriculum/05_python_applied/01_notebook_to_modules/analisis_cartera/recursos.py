"""05.03: cerrar archivos y reemplazar un JSON mediante un temporal local."""

import json
import logging
import os
from pathlib import Path
import tempfile

LOGGER = logging.getLogger(__name__)


def write_json_atomic(destination, payload, simulate_failure=False):
    """Reemplazar un archivo al terminar; simulación didáctica antes de replace."""
    destination = Path(destination)
    # Serializar antes de abrir: un objeto inválido no trunca el destino anterior.
    text = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=destination.parent,
                                         prefix=f".{destination.name}-", suffix=".tmp",
                                         delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(text + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        # Windows necesita el temporal cerrado antes de reemplazarlo.
        if simulate_failure:
            raise OSError("Falla didáctica después del temporal y antes del reemplazo")
        os.replace(temporary, destination)
    except OSError as exc:
        raise OSError(f"No se completó la escritura de {destination}: {exc}") from exc
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError as exc:
                # No ocultar una falla original con otra falla de limpieza.
                LOGGER.warning("No se pudo retirar el temporal %s: %s", temporary, exc)


def read_json(path):
    """Leer y cerrar el archivo incluso si json.load falla."""
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Falta el archivo requerido: {path}") from exc

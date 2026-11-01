"""Resolver la configuración de 05.02 sin leer archivos al importar."""

from datetime import datetime
import json
from pathlib import Path

KEYS = {"source", "output", "cut", "dpi", "log_level"}
LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def resolve_path(value, base):
    """Interpretar una ruta explícita respecto de la base indicada."""
    if not isinstance(value, (str, Path)) or not str(value).strip():
        raise ValueError("La ruta debe ser texto no vacío")
    path = Path(value).expanduser()
    return (path if path.is_absolute() else base / path).resolve()


def unique_object(pairs):
    """No aceptar dos definiciones de la misma clave en un objeto JSON."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Clave JSON repetida: {key}")
        result[key] = value
    return result


def load_settings(args):
    """Combinar predeterminados, archivo y terminal; validar sin crear salidas."""
    lesson = Path(__file__).resolve().parents[1]
    settings = {"source": lesson.parents[1] / "03_sql_databases/01_relational_sqlite/data",
                "output": None, "cut": "2026-10-31", "dpi": 160, "log_level": "INFO"}
    origins = {key: "predeterminado" for key in settings}
    config_path = None
    if args.config is not None:
        config_path = resolve_path(args.config, Path.cwd())
        with config_path.open(encoding="utf-8") as handle:
            supplied = json.load(handle, object_pairs_hook=unique_object)
        if not isinstance(supplied, dict):
            raise ValueError("La configuración JSON debe ser un objeto")
        unknown = set(supplied) - KEYS
        if unknown:
            raise ValueError(f"Claves de configuración desconocidas: {sorted(unknown)}")
        for key, value in supplied.items():
            if key in ["source", "output"]:
                value = resolve_path(value, config_path.parent)
            settings[key] = value
            origins[key] = "archivo"
    for key in KEYS:
        value = getattr(args, key)
        if value is not None:
            settings[key] = resolve_path(value, Path.cwd()) if key in ["source", "output"] else value
            origins[key] = "terminal"
    if settings["output"] is None:
        raise ValueError("Indica --output o una clave output en el archivo JSON")
    cut = settings["cut"]
    if not isinstance(cut, str):
        raise ValueError("cut debe ser texto YYYY-MM-DD")
    try:
        parsed = datetime.strptime(cut, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("cut debe ser una fecha válida YYYY-MM-DD") from exc
    if parsed.strftime("%Y-%m-%d") != cut:
        raise ValueError("cut debe conservar el formato YYYY-MM-DD")
    dpi = settings["dpi"]
    if isinstance(dpi, bool) or not isinstance(dpi, int) or dpi <= 0:
        raise ValueError("dpi debe ser un entero positivo")
    if not isinstance(settings["log_level"], str) or settings["log_level"] not in LEVELS:
        raise ValueError(f"log_level debe ser uno de {LEVELS}")
    source = settings["source"]
    for filename in ["creditos.csv", "cortes.csv"]:
        if not (source / filename).is_file():
            raise ValueError(f"Falta el archivo de entrada: {source / filename}")
    if settings["output"].exists():
        raise ValueError(f"La carpeta de salida ya existe: {settings['output']}; elige otra")
    return settings, origins, config_path

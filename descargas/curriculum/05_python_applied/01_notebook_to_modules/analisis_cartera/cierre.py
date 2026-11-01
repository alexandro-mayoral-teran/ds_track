"""05.03: cierre explícito tras exportar y registrar, sin borrar entregas parciales."""

from pathlib import Path
import platform

from .flujo import export
from .recursos import read_json, write_json_atomic

REQUIRED = ["corte.csv", "resumen.csv", "referencia_csv.csv", "indicadores.csv",
            "conciliacion.csv", "formatos.csv", "fuentes/creditos.csv", "fuentes/cortes.csv",
            "matplotlib.png", "matplotlib.svg", "altair.json", "altair.html",
            "informe.md", "RECONSTRUIR.md", "entrega.json", "ejecucion.json",
            "RECONSTRUIR_SEGURO.md"]
FAILURES = ["after-export", "record", "before-close"]


def inspect_delivery(output):
    """Informar la etapa; no reemplazar conciliación ni revisión visual."""
    output = Path(output)
    if not output.exists():
        return {"estado": "sin_iniciar"}
    marker = output / "cierre.json"
    if not marker.is_file():
        return {"estado": "incompleta", "motivo": "Falta cierre.json"}
    try:
        record = read_json(marker)
    except (OSError, ValueError) as exc:
        return {"estado": "incompleta", "motivo": f"Cierre ilegible: {exc}"}
    if (not isinstance(record, dict) or record.get("estado") != "completada"
            or record.get("archivos_requeridos") != REQUIRED
            or not isinstance(record.get("corte"), str)
            or type(record.get("comprobaciones_datos")) is not int
            or record["comprobaciones_datos"] <= 0):
        return {"estado": "incompleta", "motivo": "Contenido de cierre no reconocido"}
    missing = [name for name in REQUIRED if not (output / name).is_file()]
    if missing:
        return {"estado": "incompleta", "faltantes": missing}
    return {"estado": "completada", "revision_visual": "Pendiente de quien revisa"}


def run_delivery(settings, origins, config_path, simulate_failure=None):
    """Completar etapas o propagar el error; una falla conserva su carpeta parcial."""
    if simulate_failure is not None and simulate_failure not in FAILURES:
        raise ValueError("Punto de falla didáctica desconocido")
    output = Path(settings["output"])
    tables = export(settings["source"], output, settings["cut"], settings["dpi"])
    if simulate_failure == "after-export":
        raise OSError("Falla didáctica después de exportar; todavía no hay registro final")
    metadata = read_json(output / "entrega.json")
    record = {"configuracion_efectiva": {key: str(value) if isinstance(value, Path) else value
                                         for key, value in settings.items()},
              "origen_valores": origins,
              "archivo_configuracion": str(config_path) if config_path else None,
              "versiones": {"python": platform.python_version(), **metadata["versiones"]},
              "reglas": ["Unidad: un crédito en un corte", "Cero conocido distinto de ausencia",
                         "Mediana desde detalle conocido; cobertura con base explícita",
                         "Referencia independiente CSV/statistics"],
              "comprobaciones_datos": len(tables["conciliacion"]),
              "consumidor": "05.03", "simulacion_solicitada": simulate_failure,
              "revision_visual": "Pendiente; no acredita aprendizaje"}
    write_json_atomic(output / "ejecucion.json", record,
                      simulate_failure=simulate_failure == "record")
    instructions = "\n".join([
        "# Reconstruir con la entrada de 05.03", "",
        "Conservar el repositorio DS Track y esta carpeta completa.",
        "Desde la raíz, activar el entorno elegido y ejecutar ejecutar_seguro.py de 05.01.",
        "Pasar --source con la carpeta fuentes/ de esta entrega y --output con otra carpeta nueva.",
        f"Conservar --cut {settings['cut']} y --dpi {settings['dpi']}.",
        "No pasar --simulate-failure para una reconstrucción normal.",
        "Comprobar cierre.json y los archivos requeridos; revisar tablas, figuras y explicación.",
        "Una carpeta sin cierre válido no está completada por este consumidor.",
        "Los archivos se guardan por etapas; no existe una transacción sobre toda la carpeta.", "",
    ])
    (output / "RECONSTRUIR_SEGURO.md").write_text(instructions, encoding="utf-8")
    if simulate_failure == "before-close":
        raise OSError("Falla didáctica antes del marcador de cierre")
    missing = [name for name in REQUIRED if not (output / name).is_file()]
    if missing:
        raise ValueError(f"No se puede cerrar: faltan archivos {missing}")
    write_json_atomic(output / "cierre.json", {
        "estado": "completada", "corte": settings["cut"],
        "comprobaciones_datos": len(tables["conciliacion"]),
        "archivos_requeridos": REQUIRED,
        "revision_visual": "Pendiente; el cierre registra etapas de ejecución",
    })
    return tables

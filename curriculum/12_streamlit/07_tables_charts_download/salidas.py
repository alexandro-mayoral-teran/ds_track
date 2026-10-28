"""Preparar archivos en memoria desde el resultado ya calculado."""

import csv
from hashlib import sha256
from io import StringIO
import json

from cartera import COLUMNAS


def preparar_descargas(resultado, version_reglas):
    """No vuelve a filtrar, leer fuentes ni escribir archivos en el servidor."""
    buffer = StringIO(newline="")
    escritor = csv.DictWriter(buffer, fieldnames=COLUMNAS, lineterminator="\n")
    escritor.writeheader()
    escritor.writerows(resultado["seleccion"])
    contenido = buffer.getvalue().encode("utf-8")
    contexto = {
        "version_formato": 1,
        "version_reglas": version_reglas,
        "unidad_saldo": "MXN",
        "filtros": {"corte": resultado["corte"], "segmentos": list(resultado["segmentos"]),
                    "minimo_mxn": resultado["minimo_mxn"]},
        "universo": dict(resultado["universo"]),
        "indicadores": dict(resultado["indicadores"]),
        "columnas_csv": list(COLUMNAS),
        "filas_csv": len(resultado["seleccion"]),
        "sha256_csv": sha256(contenido).hexdigest(),
    }
    segmentos = "-".join(resultado["segmentos"]) or "ninguno"
    base = f"seleccion_{resultado['corte']}_min-{resultado['minimo_mxn']}_seg-{segmentos}"
    return {
        "csv": contenido,
        "contexto": (json.dumps(contexto, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8"),
        "nombre_csv": base + ".csv",
        "nombre_contexto": base + "_contexto.json",
    }

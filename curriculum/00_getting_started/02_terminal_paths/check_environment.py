"""Comprueba que el entorno mínimo de DS Track está disponible."""

from __future__ import annotations

import platform
import shutil
import sys
from pathlib import Path


PROJECT_MARKERS = ("README.md", "ROADMAP.md", "pyproject.toml")
TOOLS = ("python", "uv", "git")


def find_project_root(start: Path) -> Path | None:
    """Busca la raíz del proyecto desde ``start`` y sus carpetas padre."""
    for candidate in (start, *start.parents):
        if all((candidate / marker).exists() for marker in PROJECT_MARKERS):
            return candidate
    return None


def main() -> int:
    """Muestra información del entorno y devuelve 0 cuando es utilizable."""
    current_directory = Path.cwd()
    project_root = find_project_root(current_directory)

    print("DS Track - verificacion del entorno")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")
    print(f"Directorio actual: {current_directory}")
    print(
        "Raiz del proyecto: "
        + (str(project_root) if project_root else "no encontrada")
    )

    print("\nHerramientas:")
    missing_tools: list[str] = []
    for tool in TOOLS:
        location = shutil.which(tool)
        if location:
            print(f"  [OK] {tool}: {location}")
        else:
            print(f"  [FALTA] {tool}")
            missing_tools.append(tool)

    if project_root is None:
        print("\nResultado: ejecuta el script desde una carpeta del proyecto.")
        return 1

    if missing_tools:
        print("\nResultado: faltan herramientas por preparar en otra lección.")
        return 1

    print("\nResultado: entorno minimo disponible.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Lab 00.05 — Preparar y comprobar el entorno

## Relación

- Módulo: `00_getting_started`.
- Lección: [05 — Entorno y dependencias](../../../curriculum/00_getting_started/05_environment/README.md).
- Proyecto: no aplica todavía; se prepara el entorno común de DS Track.

## Objetivo y tiempo orientativo

Identificar tu intérprete y ejecutar el script en un entorno reproducible.
Reserva 30 a 45 minutos, además del tiempo de instalación si falta una herramienta.
Intenta cada parte antes de abrir su solución.

## Entrada

La carpeta de DS Track con `pyproject.toml`, `uv.lock` y el script de la lección 04.
Python 3.11 o posterior y uv, preparados según la lección.

## Parte A — Reconocer tu instalación

1. Comprueba versión y ubicación de Python.
2. Pregunta al intérprete por `sys.executable` y anota la ruta.
3. Explica la diferencia entre Python, el editor y un paquete externo.

<details>
<summary>Ver solución orientativa de la parte A</summary>

En PowerShell usa `python --version`, `Get-Command python` y
`python -c "import sys; print(sys.executable)"`.
En Bash/Zsh usa `python3 --version`, `command -v python3` y la misma instrucción
con `python3 -c`. Las rutas dependen de tu instalación. Python ejecuta el código,
el editor lo modifica y un paquete externo aporta funcionalidad instalada aparte.

</details>

## Parte B — Comprender venv y pip

1. Crea `.venv-practice` como indica el recorrido de tu shell.
2. Consulta su ejecutable y su pip mediante las rutas directas.
3. Ejecuta el primer script con ese Python.
4. Explica por qué no necesitas activar el entorno para usar su ejecutable.

<details>
<summary>Ver solución orientativa de la parte B</summary>

En PowerShell:

```powershell
python -m venv .venv-practice
.\.venv-practice\Scripts\python.exe -m pip --version
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\04_first_script\first_summary.py
```

En Bash/Zsh:

```bash
python3 -m venv .venv-practice
./.venv-practice/bin/python -m pip --version
./.venv-practice/bin/python curriculum/00_getting_started/04_first_script/first_summary.py
```

La ruta explícita ya elige el intérprete. El resultado depende de los valores
que conservaste en el script del lab 04; no tiene que volver al ejemplo original.
No se necesita un paquete externo para multiplicar y mostrar texto.

</details>

## Parte C — Preparar el entorno del proyecto

1. Sal del entorno de práctica si lo activaste.
2. Desde la raíz, sincroniza con uv y consulta el ejecutable del proyecto.
3. Ejecuta el script y compara la salida con la parte B.
4. Explica qué papel cumplen pyproject.toml, uv.lock y .venv.

<details>
<summary>Ver solución orientativa de la parte C</summary>

En ambos shells:

```text
uv sync --locked
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python curriculum/00_getting_started/04_first_script/first_summary.py
```

El intérprete pertenece a `.venv`. La salida coincide con la parte B para las
mismas entradas. La configuración declara requisitos, el lockfile conserva
la resolución y `.venv` contiene el entorno generado localmente.

</details>

## Evidencia y reflexión

- Anota versiones, rutas de los intérpretes y resultado del script.
- ¿Por qué un paquete instalado en otro Python puede no estar disponible aquí?
- ¿Qué diferencia hay entre `python -m pip` y `uv sync`?
- ¿Qué archivos compartirías y por qué no subirías `.venv`?
- Si usas Git, revisa `git status --short`: los entornos deben quedar excluidos.
  No agregues carpetas de entornos con `git add -f`.

## Siguiente paso

La lección 06 — Primer notebook está por desarrollar. Consulta el
[índice del nivel 0](../../../curriculum/00_getting_started/README.md).

# 10.04 — Entorno y ejecución desde otra sesión

La [lección](README.md) presenta todos los datos y reglas. Parte de la raíz
de DS Track, con un solo gestor elegido según
[00.05](../../00_getting_started/05_environment/README.md). No necesitas
entregas anteriores: los dos CSV propios ya están incluidos.

Referencia: Python 3.12.12/Polars 2.0.0; contraste opcional pandas 2.3.3 y
`sqlite3` estándar. No hay paquetes nuevos ni cambios de lockfile. Si tu entorno
ya es adecuado, no reinstales. Si falta Polars, los
[recorridos de instalación](../02_polars_tables_expressions/recorridos.md)
explican las alternativas sin exigir sus prácticas.

Con Conda activa el entorno de estudio `ds-track`, nunca `base`; con venv/pip
activa tu entorno local. Revisa el intérprete antes de ejecutar. Con uv trabaja
fuera de Conda/u otro venv y conserva `--locked`; no mezcles gestores.

Cada comando abre un proceso nuevo. El script solo lee fuentes y muestra
registros nativos: unión de seis filas, resumen y comprobaciones. `--contrastar`
añade pandas y una base SQLite temporal en memoria que se cierra al terminar.
No escribe entregas ni modifica bases existentes. La preparación de entorno
es independiente de las salidas de práctica.

## PowerShell

### Conda o venv/pip, con el entorno elegido activado

```powershell
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

### uv

```powershell
# Opcional: otra carpeta local, para sync y run:
# $env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

## Bash/Zsh

### Conda o venv/pip, con el entorno elegido activado

```bash
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

### uv

```bash
# Opcional: otra carpeta local, para sync y run:
# export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

## CMD — Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

Con venv/pip, sustituye la activación Conda por la de tu entorno. Para uv en
CMD, recorrido completo separado:

```bat
REM Opcional: set UV_PROJECT_ENVIRONMENT=.environment-practice/uv-polars
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py
uv run --locked python -X utf8 curriculum/10_polars_duckdb/04_types_missing_joins/semantica_polars.py --contrastar
```

## Resultado y límites de la comprobación

Seis observaciones, saldo por corte 4500/4600 MXN. Por corte: tres registros,
dos coincidencias, un producto conocido, una etiqueta pendiente y uno sin catálogo.
La extensión compara los seis campos en las seis filas con pandas/SQLite y
muestra sus versiones. Para fuentes nuevas pasa `--fuente` y `--catalogo`
conservando ambos contratos; no sobrescribas las muestras incluidas.

Comprobado en Windows con dos entornos uv locales existentes. No se instalaron
dependencias ni se cambiaron Conda, renv, venv raíz o configuración global.
No se probaron instalaciones Conda, otros sistemas o la interfaz del IDE.
La auditoría materializa tablas; estos resultados no miden rendimiento ni RAM.

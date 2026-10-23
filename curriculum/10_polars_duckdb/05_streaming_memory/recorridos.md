# 10.05 — Entorno, lotes, sink y observación local

Vuelve a la [lección](README.md) para conceptos, datos y reglas. Desde la raíz
de DS Track usa un solo gestor según
[00.05](../../00_getting_started/05_environment/README.md): Conda, venv/pip o uv.
No necesitas resultados previos; el CSV propio está incluido.

Polars 2.0.0 ya está declarado. Si tu entorno es adecuado no reinstales.
Si falta, los [recorridos de instalación](../02_polars_tables_expressions/recorridos.md)
explican las alternativas completas, sin exigir sus entregas. Conda usa el
entorno de estudio `ds-track`, nunca `base`; venv/pip usa el entorno local
activado. Con uv, fuera de Conda/u otro venv, conserva `--locked` y no mezcles pip.

`preparar` crea entrada en carpeta nueva. `ejecutar` crea otra carpeta con
selección Parquet y planes lógico/físico; `verificar` solo lee y compara pares
con CSV externo. Cada comando abre otro proceso. `observar_memoria.py` es
una exploración adicional y crea dos trabajadores nuevos, trazas, JSON y salidas
conciliadas. No instala paquetes ni configura variables globales.

Los destinos deben ser nuevos; elige otro nombre al repetir. Se usa octubre
≥ 0 para ver tres filas y más de un lote pequeño. Si omites `--minimo 0`,
la pregunta predeterminada octubre ≥ 2000 devuelve solo `003/2600`.
`-X utf8` permite guardar/mostrar símbolos de planes y trazas.

## PowerShell

### Conda o venv/pip, con el entorno elegido activado

```powershell
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_terminal_entrada
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_terminal_entrada/muestra.parquet output/streaming_1005_terminal_salida --minimo 0
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_terminal_salida/seleccion.parquet output/streaming_1005_terminal_entrada/muestra.parquet --minimo 0
# Observacion adicional:
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_terminal_entrada/muestra.parquet output/streaming_1005_terminal_memoria --minimo 0
```

### uv

```powershell
# Opcional: otra carpeta local, para sync y run:
# $env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_uv_entrada
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_uv_entrada/muestra.parquet output/streaming_1005_uv_salida --minimo 0
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_uv_salida/seleccion.parquet output/streaming_1005_uv_entrada/muestra.parquet --minimo 0
# Observacion adicional:
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_uv_entrada/muestra.parquet output/streaming_1005_uv_memoria --minimo 0
```

## Bash/Zsh

### Conda o venv/pip, con el entorno elegido activado

```bash
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_terminal_entrada
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_terminal_entrada/muestra.parquet output/streaming_1005_terminal_salida --minimo 0
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_terminal_salida/seleccion.parquet output/streaming_1005_terminal_entrada/muestra.parquet --minimo 0
# Observacion adicional:
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_terminal_entrada/muestra.parquet output/streaming_1005_terminal_memoria --minimo 0
```

### uv

```bash
# Opcional: otra carpeta local, para sync y run:
# export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_uv_entrada
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_uv_entrada/muestra.parquet output/streaming_1005_uv_salida --minimo 0
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_uv_salida/seleccion.parquet output/streaming_1005_uv_entrada/muestra.parquet --minimo 0
# Observacion adicional:
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_uv_entrada/muestra.parquet output/streaming_1005_uv_memoria --minimo 0
```

## CMD — Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_cmd_entrada
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_cmd_entrada/muestra.parquet output/streaming_1005_cmd_salida --minimo 0
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_cmd_salida/seleccion.parquet output/streaming_1005_cmd_entrada/muestra.parquet --minimo 0
REM Observacion adicional:
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_cmd_entrada/muestra.parquet output/streaming_1005_cmd_memoria --minimo 0
```

Con venv/pip sustituye la activación por la de tu entorno. Para uv en CMD,
recorrido completo separado:

```bat
REM Opcional: set UV_PROJECT_ENVIRONMENT=.environment-practice/uv-polars
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py preparar output/streaming_1005_uv_cmd_entrada
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py ejecutar output/streaming_1005_uv_cmd_entrada/muestra.parquet output/streaming_1005_uv_cmd_salida --minimo 0
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_uv_cmd_salida/seleccion.parquet output/streaming_1005_uv_cmd_entrada/muestra.parquet --minimo 0
REM Observacion adicional:
uv run --locked python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/observar_memoria.py output/streaming_1005_uv_cmd_entrada/muestra.parquet output/streaming_1005_uv_cmd_memoria --minimo 0
```

## Resultado esperado y alcance

Octubre ≥ 0: tres pares `001/100`, `002/1900`, `003/2600`, total 4600 MXN.
El verificador compara cada par y sus tipos; repetirlo no escribe archivos.
Las dos salidas del observador deben representar los mismos valores. Los
bytes de pico residente varían: no hay un valor numérico universal esperado.

Comprobado en Windows con dos entornos uv locales existentes, Python 3.12.12 /
Polars 2.0.0 y métrica PeakWorkingSetSize en bytes. La rama Linux contempla
ru_maxrss, pero no se ejecutó en esta revisión; otras plataformas indican no
disponible. No se probaron instalaciones Conda, otros sistemas ni la interfaz
del IDE. No hay instalaciones nuevas ni cambios de entornos o configuración
global. La auditoría completa materializa datos y no se incluye en el pico
de los trabajadores; no se acredita RAM acotada, I/O físico ni rendimiento general.

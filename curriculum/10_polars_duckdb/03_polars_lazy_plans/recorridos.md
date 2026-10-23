# 10.03 — Entorno, preparación y ejecución desde otra sesión

Vuelve a la [lección](README.md) para el contexto y los datos. Todos los comandos
parten de la raíz de DS Track. Usa **un solo gestor** conforme a
[00.05](../../00_getting_started/05_environment/README.md): Conda, venv/pip o uv.
Si tu entorno ya tiene Polars 2.0.0, no reinstales. No hay dependencias nuevas;
la preparación siguiente crea datos de práctica, no un entorno Python.

En Conda activa tu entorno de estudio, nunca `base`. En venv/pip activa el
entorno local antes de los comandos `python`; revisa el intérprete. Si falta
Polars, los [recorridos de instalación](../02_polars_tables_expressions/recorridos.md)
explican las alternativas completas. No se exigen sus prácticas ni entregas.
Con uv, fuera de Conda/u otro venv activo, usa la configuración raíz bloqueada;
no mezcles pip sobre ese entorno.

`preparar` crea una carpeta exclusiva con `muestra.parquet`: si ya existe,
elige otro nombre. `verificar` solo lee CSV/Parquet, imprime planes y concilia
selección/resumen. Los dos comandos verificar abren procesos nuevos.
`-X utf8` permite mostrar los símbolos del plan en la salida de Python.
Las rutas bajo `output/` quedan ignoradas. Conserva intacta la fuente incluida.

## PowerShell

### Conda o venv/pip, con el entorno elegido activado

```powershell
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_terminal
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_terminal/muestra.parquet
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_terminal/muestra.parquet --corte 2026-09-30 --minimo 2000
```

### uv

```powershell
# Si necesitas otra carpeta local, define esto antes de sync y run:
# $env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv/muestra.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv/muestra.parquet --corte 2026-09-30 --minimo 2000
```

## Bash/Zsh

### Conda o venv/pip, con el entorno elegido activado

```bash
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_terminal
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_terminal/muestra.parquet
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_terminal/muestra.parquet --corte 2026-09-30 --minimo 2000
```

### uv

```bash
# Opcional: otra carpeta local para todos estos comandos:
# export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv/muestra.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv/muestra.parquet --corte 2026-09-30 --minimo 2000
```

## CMD — Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_cmd
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_cmd/muestra.parquet
python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_cmd/muestra.parquet --corte 2026-09-30 --minimo 2000
```

Con venv/pip en CMD, usa tu activación de entorno en lugar de `conda activate`.
Para uv en CMD, recorrido completo separado:

```bat
REM Opcional: set UV_PROJECT_ENVIRONMENT=.environment-practice/uv-polars
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py preparar output/lazy_1003_uv_cmd
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv_cmd/muestra.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/03_polars_lazy_plans/consultas_lazy.py verificar output/lazy_1003_uv_cmd/muestra.parquet --corte 2026-09-30 --minimo 2000
```

## Resultado esperado

Fuente: seis registros. Octubre ≥ 2000: `003/2600`, uno/2600 MXN.
Septiembre ≥ 2000: `002/2000`, `003/2500`, dos/4500 MXN. En ambos casos,
resumen completo: septiembre tres/4500 y octubre tres/4600 MXN.

El esquema no depende de la apariencia de las tablas en terminal. El script
imprime registros nativos; si una consola no admite `π`, puede mostrar su escape
Unicode. La explicación sigue siendo una proyección. No alteres la configuración
global de la terminal para esta práctica.

Comprobado en Windows con Python 3.12.12/Polars 2.0.0 de entornos uv locales
existentes. No se instalaron paquetes, no se cambió el lockfile ni se probaron
instalaciones Conda, otros sistemas o la interfaz del IDE.

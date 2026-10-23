# 10.09 — Preparar, medir y verificar en otra sesión

Vuelve a la [lección](README.md) para datos y alcance. Todos los comandos parten
de la raíz de DS Track. No requieren entregas anteriores. Python 3.11 o superior;
referencia ejecutada 3.12.12 con pandas 2.3.3, PyArrow 21.0.0, Polars 2.0.0 y
DuckDB 2.0.0, declarados en la configuración raíz. No hay paquetes nuevos.

Elige un entorno local Conda, venv/pip o uv según
[00.05](../../00_getting_started/05_environment/README.md); activar, instalar y
comprobar son pasos distintos. Si faltan bibliotecas, consulta
[10.08](../08_engine_interchange/recorridos.md). No reinstales si ya es adecuado,
no instales en Anaconda base y no mezcles gestores sobre el mismo entorno.

`preparar` crea una carpeta nueva con entrada.parquet. `medir` exige otro destino
nuevo y ejecuta nueve procesos para tres observaciones por motor. `verificar`
solo lee y reconstruye pares/resumen; puedes repetirlo desde otra sesión.
No borres una corrida para reutilizar su nombre: conserva crudas y elige otro.

## PowerShell

Con el entorno Conda o venv/pip elegido y activado:

```powershell
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py preparar output/medir_1009_ps_datos
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_ps_corrida --entrada output/medir_1009_ps_datos/entrada.parquet --nota "Disco y carga del equipo: anotar lo conocido"
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py verificar output/medir_1009_ps_corrida --entrada output/medir_1009_ps_datos/entrada.parquet
```

Alternativa uv, desde fuera de otro entorno activo:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py preparar output/medir_1009_ps_uv_datos
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_ps_uv_corrida --entrada output/medir_1009_ps_uv_datos/entrada.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py verificar output/medir_1009_ps_uv_corrida --entrada output/medir_1009_ps_uv_datos/entrada.parquet
```

## Bash/Zsh

Con el entorno Conda o venv/pip elegido y activado:

```bash
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py preparar output/medir_1009_bash_datos
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_bash_corrida --entrada output/medir_1009_bash_datos/entrada.parquet --nota "Disco y carga del equipo: anotar lo conocido"
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py verificar output/medir_1009_bash_corrida --entrada output/medir_1009_bash_datos/entrada.parquet
```

Alternativa uv, desde fuera de otro entorno activo:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py preparar output/medir_1009_bash_uv_datos
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_bash_uv_corrida --entrada output/medir_1009_bash_uv_datos/entrada.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py verificar output/medir_1009_bash_uv_corrida --entrada output/medir_1009_bash_uv_datos/entrada.parquet
```

La rama Linux de memoria aún no se ha probado por autoría; en macOS se registra
contador no disponible. Los comandos no convierten esa ausencia en cero.

## CMD / Anaconda Prompt

Con el entorno del track preparado:

```bat
conda activate ds-track
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py preparar output/medir_1009_cmd_datos
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_cmd_corrida --entrada output/medir_1009_cmd_datos/entrada.parquet
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py verificar output/medir_1009_cmd_corrida --entrada output/medir_1009_cmd_datos/entrada.parquet
```

## Otro corte, otra pregunta

Para septiembre ≥ 2001 o noviembre, conserva el mismo Parquet y cambia los
parámetros de medir, con otro destino. Por ejemplo en PowerShell/Bash/CMD:

```text
python -X utf8 curriculum/10_polars_duckdb/09_time_memory/comparar.py medir output/medir_1009_noviembre --entrada output/medir_1009_ps_datos/entrada.parquet --corte 2026-11-30
```

Ajusta entrada a la ruta creada por tu recorrido. Verificar lee el corte/umbral
del informe; no necesita recibirlos de nuevo. Una pregunta diferente no se
mezcla en el mismo resumen. Si usas `--fuente` con un CSV distinto, pásalo tanto
al preparar como al medir/verificar.

## R opcional

La lección contiene un bloque autónomo con `system.time` para el proyecto renv
ya preparado. En RStudio/IDE abre un script, copia el bloque, ejecuta e inspecciona
crudas_r; reinicia R y ejecuta todo de nuevo. No hay instalación ni preparador R
nuevo. Este experimento no lee Parquet ni mide el pico residente; no se agrega
al informe Python. Consola R y terminal del sistema son superficies distintas.

Continúa con el [lab 10.09](../../../labs/10_polars_duckdb/09_time_memory/README.md).

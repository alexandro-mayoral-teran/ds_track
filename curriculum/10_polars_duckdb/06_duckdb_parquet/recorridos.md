# 10.06 — Entorno y ejecución desde otra sesión

Vuelve a la [lección](README.md) para datos y conceptos. Parte de la raíz de
DS Track, con un gestor elegido según
[00.05](../../00_getting_started/05_environment/README.md). Python 3.11 o superior;
referencia ejecutada Python 3.12.12/DuckDB 2.0.0. No se necesita la CLI DuckDB.

No instales en Anaconda base ni Python global. Activar, instalar y comprobar
son pasos distintos. Si ya tienes DuckDB 2.0.0 comprobado, omite instalación.
Conda usa python-duckdb como nombre de paquete; pip/uv usan duckdb. Consulta
disponibilidad y revisa el plan Conda antes de aceptar; si falta para tu
plataforma, elige otro entorno separado sin mezclar gestores para forzarlo.

El mini recorrido no exige las entregas de lecciones anteriores. Preparar crea
una carpeta NUEVA con completo.parquet y dos partes, una por corte. Verificar solo
lee y compara, e incluye EXPLAIN ANALYZE de nuestro SELECT. No abre bases
persistentes. Repetir preparación exige otro nombre; conserva la entrega anterior.

Con venv/pip activa el entorno local antes de los comandos. Con uv trabaja
fuera de Conda/u otro venv; la carpeta de entorno elegida es local e ignorada.
Usa la configuración raíz y --locked; no instales con pip sobre ese entorno.
uv.lock no administra Conda. Las referencias de instalación están en la
[API oficial Python](https://duckdb.org/docs/2.0/clients/python/overview).

## PowerShell

### Conda

```powershell
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta: consultar disponibilidad y revisar el plan.
conda search -c conda-forge python-duckdb=2.0.0
conda install -c conda-forge python-duckdb=2.0.0
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_powershell_conda
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_conda/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_conda/partes/parte_01.parquet output/duckdb_1006_powershell_conda/partes/parte_02.parquet
```

### venv/pip, con el entorno activado

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si falta la version elegida:
python -m pip install "duckdb==2.0.0"
python -m pip check
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_powershell_venv_pip
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_venv_pip/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_venv_pip/partes/parte_01.parquet output/duckdb_1006_powershell_venv_pip/partes/parte_02.parquet
```

### uv

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_powershell_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_uv/completo.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_powershell_uv/partes/parte_01.parquet output/duckdb_1006_powershell_uv/partes/parte_02.parquet
```

## Bash/Zsh

### Conda

```bash
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta: consultar disponibilidad y revisar el plan.
conda search -c conda-forge python-duckdb=2.0.0
conda install -c conda-forge python-duckdb=2.0.0
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bash_conda
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_conda/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_conda/partes/parte_01.parquet output/duckdb_1006_bash_conda/partes/parte_02.parquet
```

### venv/pip, con el entorno activado

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si falta la version elegida:
python -m pip install "duckdb==2.0.0"
python -m pip check
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bash_venv_pip
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_venv_pip/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_venv_pip/partes/parte_01.parquet output/duckdb_1006_bash_venv_pip/partes/parte_02.parquet
```

### uv

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bash_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_uv/completo.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bash_uv/partes/parte_01.parquet output/duckdb_1006_bash_uv/partes/parte_02.parquet
```

## CMD — Anaconda Prompt

### Conda

```bat
conda activate ds-track
python -c "import sys; print(sys.executable)"
REM Solo si falta: consultar disponibilidad y revisar el plan.
conda search -c conda-forge python-duckdb=2.0.0
conda install -c conda-forge python-duckdb=2.0.0
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bat_conda
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_conda/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_conda/partes/parte_01.parquet output/duckdb_1006_bat_conda/partes/parte_02.parquet
```

### venv/pip, con el entorno activado

```bat
python -c "import sys; print(sys.executable)"
python -m pip --version
REM Solo si falta la version elegida:
python -m pip install "duckdb==2.0.0"
python -m pip check
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bat_venv_pip
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_venv_pip/completo.parquet
python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_venv_pip/partes/parte_01.parquet output/duckdb_1006_bat_venv_pip/partes/parte_02.parquet
```

### uv

```bat
set UV_PROJECT_ENVIRONMENT=.environment-practice/uv-duckdb
uv sync --locked --python 3.12
uv run --locked python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py preparar output/duckdb_1006_bat_uv
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_uv/completo.parquet
uv run --locked python -X utf8 curriculum/10_polars_duckdb/06_duckdb_parquet/consultas_duckdb.py verificar output/duckdb_1006_bat_uv/partes/parte_01.parquet output/duckdb_1006_bat_uv/partes/parte_02.parquet
```

## Resultado esperado y límites de la comprobación

Ambas representaciones producen 003/2600 para octubre ≥ 2000. Resumen:
septiembre tres/4500 y octubre tres/4600 MXN. Los planes pueden variar;
la comprobación compara esquema y valores, no capturas ni tiempos literales.
Para septiembre añade --corte 2026-09-30 --minimo 2000 al comando verificar.
Para fuentes nuevas pasa --fuente a preparar y verificar, conservando el contrato.

La autoría instaló las dependencias bloqueadas en una carpeta uv nueva y
reconstruyó otra desde caché local sin biblioteca previa, con Python 3.12.12.
Los registros anteriores del lockfile permanecen idénticos salvo la dependencia
del proyecto; DuckDB 2.0.0 es la única incorporación. No se modificaron Conda,
renv, venv raíz ni bibliotecas globales. No se probaron instalaciones Conda,
otros sistemas o la interfaz del IDE. No se instalaron paquetes R.

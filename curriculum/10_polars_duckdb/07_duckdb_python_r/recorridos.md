# 10.07 — Ejecutar y retomar

Consulta la [lección](README.md) para datos, versiones, entorno R y conceptos.
Los comandos parten de la raíz de DS Track. No necesitas resultados anteriores.
Usa un entorno Python local adecuado; la instalación según el gestor elegido
está en [10.06](../06_duckdb_parquet/recorridos.md). Si DuckDB 2.0.0 ya funciona,
no lo reinstales. No mezcles gestores ni instales en Anaconda base.

Preparar exige una carpeta nueva. Ejecutar sin `--preparar` solo lee y concilia;
imprime selección, resumen decimal exacto y versión del motor.

## PowerShell

Con el entorno Conda o venv/pip elegido y activado:

```powershell
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_powershell --preparar
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_powershell/completo.parquet --corte 2026-09-30 --minimo 2000
```

Alternativa uv, desde fuera de otro entorno activo, con la configuración raíz:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_powershell_uv --preparar
uv run --locked python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_powershell_uv/completo.parquet --corte 2026-11-30
```

## Bash/Zsh

Con el entorno Conda o venv/pip elegido y activado:

```bash
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_bash --preparar
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_bash/completo.parquet --corte 2026-09-30 --minimo 2000
```

Alternativa uv, desde fuera de otro entorno activo:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_bash_uv --preparar
uv run --locked python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_bash_uv/completo.parquet --corte 2026-11-30
```

## CMD / Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys, duckdb; print(sys.executable); print(duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_cmd --preparar
python -X utf8 curriculum/10_polars_duckdb/07_duckdb_python_r/clientes.py output/clientes_1007_cmd/completo.parquet --corte 2026-09-30 --minimo 2000
```

## R: recorrido principal en el IDE

Prepara/restaura el proyecto según la [lección](README.md#preparar-la-copia-r-sin-exigir-entregas-previas).
Abre ese proyecto en RStudio/IDE y reinicia R. Abre `ejecutar_clientes.R`,
ejecuta bloques e inspecciona selección, resumen y clases. Para comprobarlo
completo, con carpeta de trabajo en **ese proyecto**, en la consola R:

```r
source("ejecutar_clientes.R", encoding = "UTF-8")
```

El script crea `output/clientes_1007_r/`; repetirlo requiere editar el nombre
del destino. Para comprobar desde otra sesión sin reescribir, reinicia R:

```r
source("R/clientes_1007.R", encoding = "UTF-8")
x <- ejecutar_1007(normalizePath("output/clientes_1007_r/completo.parquet", winslash = "/"))
stopifnot(identical(x$seleccion$saldo_mxn, 2600L))
```

### Terminal opcional para un proceso R nuevo

Usa la ruta del Rscript del R elegido si no está en PATH; no uses accidentalmente
otro R incluido en Anaconda. Cambia primero a la carpeta de tu proyecto preparado.
Los comandos siguientes comprueban solo lectura, después de crear el Parquet.
No sustituyen el reinicio de sesión y la exploración en el IDE.

PowerShell:

```powershell
Rscript --vanilla -e 'source(".Rprofile"); source("R/clientes_1007.R"); print(ejecutar_1007(normalizePath("output/clientes_1007_r/completo.parquet", winslash="/")))'
```

Bash/Zsh:

```bash
Rscript --vanilla -e 'source(".Rprofile"); source("R/clientes_1007.R"); print(ejecutar_1007(normalizePath("output/clientes_1007_r/completo.parquet", winslash="/")))'
```

CMD:

```bat
Rscript --vanilla -e "source('.Rprofile'); source('R/clientes_1007.R'); print(ejecutar_1007(normalizePath('output/clientes_1007_r/completo.parquet', winslash='/')))"
```

Continúa con el [lab 10.07](../../../labs/10_polars_duckdb/07_duckdb_python_r/README.md).

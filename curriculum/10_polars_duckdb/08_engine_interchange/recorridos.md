# 10.08 — Entorno, ejecución y otra sesión

Vuelve a la [lección](README.md) para datos y decisiones de tipos. Desde la
raíz de DS Track usa Python 3.11 o superior; referencia ejecutada 3.12.12.
Se requieren pandas 2.3.3, PyArrow 21.0.0, Polars 2.0.0 y DuckDB 2.0.0.
Ya figuran en la configuración raíz. El ejecutor solo lee el CSV: todo el
intercambio se hace en memoria y no necesita entregas anteriores.

Elige Conda, venv/pip o uv según [00.05](../../00_getting_started/05_environment/README.md).
Activa y comprueba el entorno antes de ejecutar. Si faltan dependencias, sigue
la instalación con el gestor elegido de [10.06](../06_duckdb_parquet/recorridos.md),
comprobando también las otras tres bibliotecas. Con venv/pip, si faltan,
`python -m pip install "pandas==2.3.3" "pyarrow==21.0.0" "polars==2.0.0" "duckdb==2.0.0"`
instala las versiones declaradas, solo dentro de tu entorno activado. No instales
en Anaconda base ni mezcles pip/uv/Conda sobre el mismo entorno.
No necesitas actualizar el lockfile ni instalar un servidor.

## PowerShell

Con Conda o venv/pip adecuado y activado:

```powershell
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py --corte 2026-11-30
```

Alternativa uv desde fuera de otro entorno activo:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py
uv run --locked python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py --corte 2026-09-30 --minimo 2001
```

## Bash/Zsh

Con Conda o venv/pip adecuado y activado:

```bash
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py --corte 2026-11-30
```

Alternativa uv desde fuera de otro entorno activo:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-duckdb"
uv sync --locked --python 3.12
uv run --locked python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py
uv run --locked python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py --corte 2026-09-30 --minimo 2001
```

## CMD / Anaconda Prompt

Con el entorno Conda del track ya preparado:

```bat
conda activate ds-track
python -c "import sys,pandas,pyarrow,polars,duckdb; print(sys.executable); print(pandas.__version__,pyarrow.__version__,polars.__version__,duckdb.__version__)"
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py
python -X utf8 curriculum/10_polars_duckdb/08_engine_interchange/intercambio.py --corte 2026-09-30 --minimo 2001
```

Cada comando Python crea un proceso nuevo. Octubre devuelve 003/2600,
noviembre una selección vacía y septiembre ≥ 2001 solo 003/2500. Todos conservan
la fuente completa y su resumen 4500/4600; imprime además esquemas, ausencias,
tipos pandas y la muestra anulable independiente.

## R opcional: IDE y proceso nuevo

Sigue la [preparación de tres archivos](README.md#6-ampliación-r-arrow--duckdb--dataframe--arrow)
en el mismo proyecto renv de 10.07. No hay paquetes nuevos. En RStudio/IDE,
abre ese proyecto, reinicia R y ejecuta `ejecutar_intercambio.R` completo.
Inspecciona `x$esquema`, `x$seleccion` y `x$resumen`. Repite después de
reiniciar R; solo lee datos y no crea entregas que puedan sobrescribirse.

Como apoyo opcional, desde la **carpeta del proyecto R preparado**, con Rscript
del R elegido en PATH o sustituyéndolo por su ruta completa:

PowerShell:

```powershell
Rscript --vanilla -e 'source(".Rprofile"); source("ejecutar_intercambio.R", encoding="UTF-8")'
```

Bash/Zsh:

```bash
Rscript --vanilla -e 'source(".Rprofile"); source("ejecutar_intercambio.R", encoding="UTF-8")'
```

CMD:

```bat
Rscript --vanilla -e "source('.Rprofile'); source('ejecutar_intercambio.R', encoding='UTF-8')"
```

Estos comandos son de terminal del sistema, distintos de la consola R del IDE.
Continúa con el [lab 10.08](../../../labs/10_polars_duckdb/08_engine_interchange/README.md).

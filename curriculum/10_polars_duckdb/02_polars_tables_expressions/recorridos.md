# 10.02 — Entorno y ejecución completa

Vuelve a la [lección](README.md) para los conceptos. Empieza en la raíz de DS Track,
con tu entorno de estudio creado según [00.05](../../00_getting_started/05_environment/README.md).
Elige **un solo gestor**. Activar, instalar y comprobar son pasos diferentes.

- Conda: entorno de estudio `ds-track`, nunca `base`. Consulta disponibilidad y
  revisa el plan del instalador antes de aceptarlo; uv.lock no administra Conda.
- venv/pip: activa tu entorno local; comprueba `sys.executable` antes de instalar.
- uv: fuera de Conda u otro venv activo; usa la configuración raíz y `--locked`.
  No cambies requisitos mediante pip dentro de ese entorno.

Referencia: Polars 2.0.0. Omite instalación si esa versión ya está comprobada.
Si aún no está disponible para tu plataforma en Conda, conserva ese entorno y
elige una alternativa en **otro entorno separado**; no mezcles gestores para
forzar la actualización. Las instalaciones Conda no se ejecutaron en la autoría.
La reconstrucción comprobada fue uv local con Python 3.12.12.

Los dos comandos del script abren procesos distintos y solo leen. El primero
elige octubre ≥ 2000; el segundo septiembre ≥ 2000. No generan entregas ni
sobrescriben CSV. La raíz contiene la configuración y las rutas relativas.

## PowerShell

### Conda

```powershell
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta; consulta disponibilidad antes de instalar:
conda search -c conda-forge polars=2.0.0
conda install -c conda-forge polars=2.0.0
python -c "import polars; print(polars.__version__)"
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

### venv/pip, con tu entorno activado

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si falta la version elegida:
python -m pip install "polars==2.0.0"
python -m pip check
python -c "import polars; print(polars.__version__)"
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

### uv

```powershell
# Opcional: otra carpeta ignorada si el venv anterior apunta a un Python inexistente.
# $env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
uv run --locked python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

## Bash/Zsh

### Conda

```bash
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta; consulta disponibilidad antes de instalar:
conda search -c conda-forge polars=2.0.0
conda install -c conda-forge polars=2.0.0
python -c "import polars; print(polars.__version__)"
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

### venv/pip, con tu entorno activado

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si falta la version elegida:
python -m pip install 'polars==2.0.0'
python -m pip check
python -c "import polars; print(polars.__version__)"
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

### uv

```bash
# Opcional: otra carpeta ignorada si el venv anterior apunta a un Python inexistente.
# export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-polars"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, polars; print(sys.executable); print(polars.__version__)"
uv run --locked python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
uv run --locked python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

## CMD — Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys; print(sys.executable)"
REM Solo si falta; consulta disponibilidad antes de instalar:
conda search -c conda-forge polars=2.0.0
conda install -c conda-forge polars=2.0.0
python -c "import polars; print(polars.__version__)"
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py
python curriculum/10_polars_duckdb/02_polars_tables_expressions/tablas_polars.py --corte 2026-09-30 --minimo 2000
```

## Comprobar y retomar

Primera ejecución: fuente `(6, 3)`, selección `003/2600`, un registro/2600 MXN;
resumen septiembre tres/4500, octubre tres/4600. Segunda: `002/2000` y `003/2500`,
dos registros/4500 MXN. Ambas reconstruyen la entrada y concilian por valores.
Puedes repetir con `--corte 2026-11-30`: selección vacía y control cero/cero,
con el resumen de toda la fuente intacto. `--fuente` permite otro CSV bajo el
mismo contrato; pasa siempre esa misma fuente a los comprobadores de tus bloques.

En el IDE selecciona el mismo ejecutable que muestra `sys.executable`; reinicia
la sesión y ejecuta el script completo. Una instalación correcta no cambia
automáticamente el intérprete de un notebook o editor ya abierto.
Si la consola falla al imprimir bordes Unicode de una tabla, usa `to_dicts()`;
el ejecutor ya imprime registros nativos para evitar esa dependencia visual.

En uv la variable opcional elige otra carpeta con la **misma configuración raíz**;
afecta esa terminal y debes volver a establecerla al retomar allí. No borres
automáticamente el entorno anterior. Conda y venv/pip deben registrar sus cambios
según sus recorridos de [00.05](../../00_getting_started/05_environment/README.md).
`pip check` comprueba dependencias de paquetes, no claves ni importes.

Fuentes: [instalación oficial de Polars](https://docs.pola.rs/user-guide/installation/),
[sincronización uv](https://docs.astral.sh/uv/concepts/projects/sync/) y
[UV_PROJECT_ENVIRONMENT](https://docs.astral.sh/uv/reference/environment/#uv_project_environment).
No se comprobó instalación en otros sistemas operativos ni la interfaz del IDE.
Continúa con la [lección](README.md) y su
[lab](../../../labs/10_polars_duckdb/02_polars_tables_expressions/README.md).

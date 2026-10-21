# 09.03 — Entorno, ejecución y relectura

Vuelve a la [lección](README.md) para entender la conversión. Estos recorridos
ejecutan [intercambio_python.py](intercambio_python.py) completo y vuelven a
comprobar el Parquet desde otro proceso. Empieza en la raíz de DS Track, con
tu entorno de estudio ya creado como aprendiste en
[00.05](../../00_getting_started/05_environment/README.md).

## Elegir antes de ejecutar

- **Conda:** activa el entorno de estudio, normalmente `ds-track`; nunca `base`.
  Revisa el plan del instalador antes de aceptarlo. El lockfile uv no administra Conda.
- **venv/pip:** activa tu entorno de estudio según
  [su recorrido](../../00_getting_started/05_environment/venv-pip.md), o usa
  directamente su ejecutable. Comprueba `sys.executable` antes de instalar.
- **uv:** usa la configuración raíz, fuera de Conda y otros venv. No es el
  mini proyecto `uv-demo` de 00.05. `--locked` exige correspondencia con el
  lockfile versionado; no ejecutes `uv add` ni pip para cambiar este entorno.

Elige solo una alternativa dentro de tu shell. Omite la línea de instalación
si pandas 2.3.3/PyArrow 21.0.0 ya están disponibles y comprobados. Si falta
algún paquete, instala **en ese entorno**, no en el Python global. Si la
resolución propone cambiar versiones que necesitas conservar, revisa el entorno
antes de aceptar; no sustituyas el gestor a mitad del recorrido.

`--salida` recibe una carpeta nueva. `--verificar` recibe un Parquet existente
y solo lee. Los dos comandos arrancan procesos Python distintos. Si
`output/09_03_python` ya existe, cambia ambos destinos a otro nombre; no borres
tu evidencia para volver a ejecutar. Las rutas relativas parten de la raíz.

## PowerShell

### Alternativa Conda

```powershell
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta la version de referencia en este entorno:
conda install -c conda-forge pandas=2.3.3 pyarrow=21.0.0
python -c "import pandas, pyarrow; print(pandas.__version__, pyarrow.__version__)"
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
conda list pyarrow
```

### Alternativa venv/pip, con tu entorno ya activado

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si faltan las versiones de referencia:
python -m pip install "pandas==2.3.3" "pyarrow==21.0.0"
python -m pip check
python -c "import pandas, pyarrow; print(pandas.__version__, pyarrow.__version__)"
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
```

### Alternativa uv

```powershell
# Si tu .venv anterior apunta a un Python inexistente, puedes descomentar:
# $env:UV_PROJECT_ENVIRONMENT = ".environment-practice/uv-parquet"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, pandas, pyarrow; print(sys.executable); print(pandas.__version__, pyarrow.__version__)"
uv run --locked python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
uv run --locked python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
```

## Bash/Zsh

### Alternativa Conda

```bash
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Solo si falta la version de referencia en este entorno:
conda install -c conda-forge pandas=2.3.3 pyarrow=21.0.0
python -c "import pandas, pyarrow; print(pandas.__version__, pyarrow.__version__)"
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
conda list pyarrow
```

### Alternativa venv/pip, con tu entorno ya activado

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
# Solo si faltan las versiones de referencia:
python -m pip install 'pandas==2.3.3' 'pyarrow==21.0.0'
python -m pip check
python -c "import pandas, pyarrow; print(pandas.__version__, pyarrow.__version__)"
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
```

### Alternativa uv

```bash
# Si tu .venv anterior apunta a un Python inexistente, puedes descomentar:
# export UV_PROJECT_ENVIRONMENT=".environment-practice/uv-parquet"
uv sync --locked --python 3.12
uv run --locked python -c "import sys, pandas, pyarrow; print(sys.executable); print(pandas.__version__, pyarrow.__version__)"
uv run --locked python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
uv run --locked python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
```

## CMD — Anaconda Prompt

```bat
conda activate ds-track
python -c "import sys; print(sys.executable)"
REM Solo si falta la version de referencia en este entorno:
conda install -c conda-forge pandas=2.3.3 pyarrow=21.0.0
python -c "import pandas, pyarrow; print(pandas.__version__, pyarrow.__version__)"
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --salida output/09_03_python
python curriculum/09_arrow_parquet/03_python_read_write/intercambio_python.py --verificar output/09_03_python/base_comun.parquet
conda list pyarrow
```

## Leer el resultado y conservar la configuración

La primera ejecución informa versiones, tres campos no anulables, índice omitido,
28 registros, 14 IDs y dos cortes con 14 registros y 29000/31800 MXN. La segunda
reconstruye el CSV y vuelve a conciliar ese resumen y cada valor por clave. No
depende de objetos que hayan quedado en el IDE. Con un CSV distinto mediante
`--fuente`, se compara contra esa fuente bajo el mismo contrato; los recuentos
conocidos no se imponen como regla universal a cualquier archivo.

En Conda, conserva la configuración según [00.05 Conda](../../00_getting_started/05_environment/conda.md#registrar-después-de-instalar).
En venv/pip registra las dependencias elegidas y revisa tu exportación según
[00.05 venv](../../00_getting_started/05_environment/venv-pip.md).
No sobrescribas registros previos ni publiques rutas personales. `pip check`
verifica dependencias declaradas de paquetes; no comprueba el contrato de datos.
En uv, `pyproject.toml`/`uv.lock` ya registran el requisito; `uv sync --locked`
lo reconstruye. No compartas los entornos ni las salidas de práctica.

Si `import pyarrow` falla después de instalar, comprueba que el IDE usa el
mismo `sys.executable` que el shell. Si un venv apunta a un Python que ya no
existe, revisa su origen y prepara otro entorno local compatible: no lo
soluciones instalando en `base` ni borrando automáticamente el anterior.
En los bloques uv, la variable opcional `UV_PROJECT_ENVIRONMENT` permite usar
otra carpeta ignorada con **la misma configuración raíz**, sin tocar el venv
anterior. Solo afecta esa terminal; para retomar con esa carpeta, vuelve a
establecerla antes de los comandos uv. No es el mini proyecto `uv-demo`.
[Configuración del entorno uv](https://docs.astral.sh/uv/reference/environment/#uv_project_environment).

Fuentes: [PyArrow 21](https://arrow.apache.org/docs/21.0/python/install.html),
[entornos Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html),
[pip install](https://pip.pypa.io/en/stable/cli/pip_install/) y
[lockfile/sincronización uv](https://docs.astral.sh/uv/concepts/projects/sync/).
La autoría comprobó instalación/restauración uv local con Python 3.12.12,
sin modificar Conda ni bibliotecas globales; no ejecutó instalaciones Conda
en otros equipos ni las interfaces de los IDE.

Continúa con los bloques explicados de la [lección 09.03](README.md) y su
[lab](../../../labs/09_arrow_parquet/03_python_read_write/README.md).

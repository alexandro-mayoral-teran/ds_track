# 12.01 — Entorno, arranque y parada

Vuelve a la [lección](README.md) para las explicaciones. Empieza en la raíz de
DS Track, donde están `pyproject.toml` y `uv.lock`. Elige **un gestor y un shell**;
no combines instalaciones Conda, pip y uv sobre el mismo entorno.

La referencia comprobada es Python 3.12.12/Streamlit 1.66.1. Streamlit es un
paquete Python, no una extensión del navegador. Las instrucciones siguientes
inician `app.py`; para el primer mínimo sustituye solo ese nombre por `hola.py`.

## Elegir el entorno

- **uv:** el grupo `streamlit` contiene la dependencia de esta ruta. Se utiliza
  `.environment-practice/streamlit` para conservar el venv raíz. `--locked` exige
  la resolución registrada. No añadas instalaciones pip dentro de ese entorno.
- **venv/pip:** los comandos crean una copia aislada específica de práctica.
  Si esa carpeta ya existe y funciona, omite creación y conserva activación/
  comprobación. Si tiene otro propósito, elige un nombre nuevo; no la reemplaces.
- **Conda:** usa el entorno de estudio creado en [00.05](../../00_getting_started/05_environment/README.md),
  nunca `base`. Consulta disponibilidad y revisa el plan antes de instalar.
  Si la versión no está disponible para tu plataforma, conserva el entorno y
  elige uv o venv en otro separado, sin forzar una mezcla de gestores.

Si la versión ya está comprobada, omite su instalación. Una creación con venv
no instala Streamlit: activar, instalar y comprobar son acciones diferentes.
La reconstrucción de autoría se comprueba con uv en Windows; no se acredita
haber instalado con Conda ni probado Bash/Zsh en Linux/macOS.

## Qué hace el comando de arranque

`python -m streamlit run RUTA` utiliza el módulo del intérprete seleccionado.
`--server.address 127.0.0.1` limita esta práctica a la computadora local;
`--browser.gatherUsageStats false` desactiva el envío de estadísticas de uso.
No crea un despliegue. Si el puerto predeterminado está ocupado, añade
`--server.port 8502` y usa la URL que aparezca en la terminal.

El último comando de cada bloque queda activo. Abre su URL local en el navegador.
Para recuperar el prompt, **Ctrl+C en esa terminal**. Espera la parada antes de
iniciar otro archivo o variante. Cerrar el navegador no sustituye este paso.

## PowerShell

### uv

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### venv/pip

```powershell
python -m venv .environment-practice/streamlit-pip
& ./.environment-practice/streamlit-pip/Scripts/Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install "streamlit==1.66.1"
python -m pip check
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda

```powershell
conda activate ds-track
python -c "import sys; print(sys.executable)"
conda search -c conda-forge streamlit=1.66.1
# Solo si falta y el plan es adecuado:
conda install -c conda-forge streamlit=1.66.1
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### venv/pip

```bash
python -m venv .environment-practice/streamlit-pip
source .environment-practice/streamlit-pip/bin/activate
python -c "import sys; print(sys.executable)"
python -m pip install "streamlit==1.66.1"
python -m pip check
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda

```bash
conda activate ds-track
python -c "import sys; print(sys.executable)"
conda search -c conda-forge streamlit=1.66.1
# Solo si falta y el plan es adecuado:
conda install -c conda-forge streamlit=1.66.1
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

```bat
set "UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### venv/pip

```bat
python -m venv .environment-practice/streamlit-pip
call .environment-practice\streamlit-pip\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
python -m pip install "streamlit==1.66.1"
python -m pip check
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda

```bat
conda activate ds-track
python -c "import sys; print(sys.executable)"
conda search -c conda-forge streamlit=1.66.1
REM Solo si falta y el plan es adecuado:
conda install -c conda-forge streamlit=1.66.1
python -c "import streamlit; print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/01_first_app_execution/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Repetir con una copia propia

Después de detener el servidor, conserva el prefijo de tu gestor y sustituye
la ruta de la app por `output/mi_1201/app.py`, donde guardaste tu variante.
Por ejemplo, en venv/pip o Conda ya activado:

```text
python -m streamlit run output/mi_1201/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

En uv conserva `uv run --locked --group streamlit` delante de `python`.
Comprueba que estás ejecutando la copia correcta, guarda y contrasta 690 MXN
tras el cambio de precio propuesto en el lab. El original debe seguir en 660.

## Comprobación automatizada opcional

Con el entorno elegido y el servidor ya detenido:

```text
python curriculum/12_streamlit/01_first_app_execution/comprobar_app.py
```

En uv conserva el mismo prefijo `uv run --locked --group streamlit`.
AppTest simula casilla/botón, detalle, métrica y sesión nueva; no abre un navegador
ni acredita revisión visual. Esa API se estudiará en 12.08. El primer uso de
bibliotecas puede tardar más; las pruebas conceden un margen de 20 segundos por
pasada, no fijan ese valor como tiempo esperado de la app.

No publiques `.environment-practice/`, cachés o salidas personales. Si tu shell
bloquea la activación de un venv, puedes llamar directamente a su `python` por
ruta completa en lugar de cambiar la política global del sistema.

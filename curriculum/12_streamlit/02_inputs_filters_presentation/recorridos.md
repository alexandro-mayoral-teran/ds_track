# 12.02 — Entorno y arranque

Vuelve a la [lección](README.md) para la pregunta, datos y filtros. Empieza en
la raíz de DS Track. Usa **el mismo gestor y entorno de 12.01**: no hay paquetes
ni lockfiles nuevos. Si falta prepararlo, sigue primero sus
[recorridos completos](../01_first_app_execution/recorridos.md).

Python 3.12.12 y Streamlit 1.66.1 son las referencias comprobadas. Elige un
shell y **solo una** alternativa de los bloques siguientes. `uv` mantiene el
grupo `streamlit` del proyecto; Conda o venv/pip usan su entorno ya activado.
No mezcles gestores sobre el mismo entorno ni instales en `base` o globalmente.

El último comando permanece activo. Abre la URL local que aparezca; si no se
abre una pestaña automáticamente, copia esa URL en el navegador. Si el puerto
está ocupado por tu práctica anterior, detén esa app con Ctrl+C o añade
`--server.port 8502`. No cierres procesos ajenos para liberar un puerto.

## PowerShell

### uv

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```powershell
python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```bash
python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

```bat
set "UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```bat
python -c "import sys, streamlit; print(sys.executable); print(streamlit.__version__)"
python -m streamlit run curriculum/12_streamlit/02_inputs_filters_presentation/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Detener, repetir y usar una copia

Detén el servidor con **Ctrl+C en su terminal**. Cerrar una pestaña no sustituye
este paso. Guarda tu copia propia, por ejemplo `output/mi_1202/app.py`, y cambia
la ruta del comando, conservando el prefijo de tu gestor. Para Conda o venv/pip:

```text
python -m streamlit run output/mi_1202/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Con uv, conserva `uv run --locked --group streamlit` delante de `python` y la
variable del entorno elegida. La app no lee CSV ni escribe resultados: sus seis
registros se reconstruyen desde el archivo guardado.

## Comprobación opcional de autoría

Con el mismo entorno, ejecuta en un proceso Python separado:

```text
python curriculum/12_streamlit/02_inputs_filters_presentation/comprobar_app.py
```

En uv usa el mismo prefijo `uv run --locked --group streamlit`.
Se contrastan doce combinaciones manuales, frontera 2000/2001, ningún segmento,
vacío, recuperación y valores iniciales en una sesión nueva. AppTest no abre
un navegador; esa API se enseñará en 12.08. El lab puede completarse sin usarla.

Reconstrucción y pruebas de autoría realizadas en los dos entornos uv locales
Python 3.12.12 ya existentes de 12.01, sin modificar sus dependencias. Conda y
Bash/Zsh están documentados como recorridos; no se acredita instalación con Conda
ni ejecución en Linux/macOS.

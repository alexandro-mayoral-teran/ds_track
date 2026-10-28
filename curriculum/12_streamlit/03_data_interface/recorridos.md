# 12.03 — Ejecutar desde terminal y desde la app

Vuelve a la [lección](README.md). Empieza en la raíz de DS Track; para tu variante,
reemplaza la ruta de la sección por la de tu carpeta completa. El ejecutor utiliza
solo Python estándar. La app y AppTest requieren el entorno local de 12.01:
si no existe, sigue sus [recorridos de preparación](../01_first_app_execution/recorridos.md).
No hay paquetes ni lockfiles nuevos. Elige un shell y un solo gestor.

Cada bloque ejecuta el caso predeterminado (octubre, ambos, ≥ 2000), compara
septiembre ≥ 2001 y arranca la app. El último comando permanece activo:
abre la URL indicada y detén tu servidor con Ctrl+C al terminar. Si otro servidor
ocupa el puerto, usa `--server.port 8503`; no cierres procesos ajenos.

## PowerShell

### uv

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```powershell
python curriculum/12_streamlit/03_data_interface/ejecutar.py
python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```bash
python curriculum/12_streamlit/03_data_interface/ejecutar.py
python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

```bat
set UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py
uv run --locked --group streamlit python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

```bat
python curriculum/12_streamlit/03_data_interface/ejecutar.py
python curriculum/12_streamlit/03_data_interface/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run curriculum/12_streamlit/03_data_interface/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Parámetros y resultados

Agrega argumentos a `ejecutar.py`, antes de iniciar la app:

| Argumentos | Qué cambia |
| --- | --- |
| `--corte 2026-09-30 --minimo 2001` | Septiembre: 003/2500; universo 4500 |
| `--segmentos servicios --minimo 1900` | Octubre: 002/1900; universo 4600 |
| `--segmentos` | Lista vacía: ninguna fila, 0% con universo de tres |
| `--corte 2026-11-30` | Corte sin registros: porcentaje JSON null |
| `--fuente "ruta/variante.csv"` | Otra fuente del mismo contrato; ruta relativa a la terminal |
| `--help` | Ayuda de argumentos; no inicia Streamlit |

`argparse` convierte `--minimo` a entero y entrega los parámetros al programa.
`nargs="*"` admite cero o más segmentos después de `--segmentos`; omitir el
argumento conserva ambos, escribirlo sin valores selecciona ninguno. Un argumento
inválido o una fuente inválida termina con código 2 y no emite JSON de éxito.
La app recoge parámetros de widgets: no hereda los argumentos de ejecutar.py.

## Comprobación opcional de autoría

En el mismo shell/gestor, sustituye el comando que arranca la app por
`python curriculum/12_streamlit/03_data_interface/comprobar_modelo.py` y después
`python curriculum/12_streamlit/03_data_interface/comprobar_app.py`.
Con uv, antepón `uv run --locked --group streamlit` a cada uno.
El primero también funciona con Python estándar; el segundo necesita Streamlit.
Las pruebas crean y retiran solo sus copias temporales, sin alterar el CSV del
repositorio. Las APIs de pruebas de aplicación se estudiarán en 12.08.

[← Lección 12.03](README.md) · [Lab 12.03](../../../labs/12_streamlit/03_data_interface/README.md)

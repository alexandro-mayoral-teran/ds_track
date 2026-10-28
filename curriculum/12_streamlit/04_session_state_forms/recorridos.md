# 12.04 — Preparación y arranque

Vuelve a la [lección](README.md). Empieza en la raíz del repositorio y usa el
entorno local de 12.01. Si falta, sigue primero sus
[recorridos completos](../01_first_app_execution/recorridos.md). No hay paquetes
nuevos. Referencias: Python 3.12.12 y Streamlit 1.66.1.

Elige **un shell y un gestor**. El destino `output/practica_1204` debe ser nuevo;
si ya existe, conserva su contenido y sustituye esa ruta por otra nueva en todos
los comandos de tu recorrido. El preparador copia seis fuentes; no instala,
no inicia servidores y no sobrescribe una práctica previa.

Cada arranque de Streamlit permanece activo. Abre la URL que aparezca. Detén
ese servidor con Ctrl+C antes de pasar del contador a la app. Si el puerto está
ocupado por otra práctica, añade `--server.port 8504`; no cierres procesos ajenos.
Los comandos de ejemplo limitan la escucha a tu equipo, `127.0.0.1`.

## PowerShell

### uv

Prepara una vez:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```powershell
uv run --locked --group streamlit python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```powershell
uv run --locked --group streamlit python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez:

```powershell
python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```powershell
python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```powershell
python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

Prepara una vez:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```bash
uv run --locked --group streamlit python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```bash
uv run --locked --group streamlit python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez:

```bash
python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```bash
python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```bash
python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

Prepara una vez:

```bat
set UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```bat
uv run --locked --group streamlit python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```bat
uv run --locked --group streamlit python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
uv run --locked --group streamlit python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez:

```bat
python curriculum/12_streamlit/04_session_state_forms/preparar_practica.py output/practica_1204
```

Primero el mínimo:

```bat
python -m streamlit run output/practica_1204/contador.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Detén el mínimo con Ctrl+C. Después contrasta el ejecutor e inicia la app:

```bat
python output/practica_1204/ejecutar.py --corte 2026-09-30 --minimo 2001
python -m streamlit run output/practica_1204/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Reiniciar no es volver a preparar

Para reiniciar tu servidor, Ctrl+C y repite solo el comando `streamlit run` de tu
copia. No repitas el preparador sobre una carpeta ocupada. Al reiniciar se pierde
el estado de sesión; los cambios que hayas hecho al CSV permanecen en disco.
Para una práctica completamente nueva elige otro destino y vuelve a preparar.

Los archivos app.py, cartera.py, configuracion.py y cartera.csv deben permanecer
juntos en la carpeta preparada. No arranques el app.py fuente de 12.04: el
preparador incorpora los módulos reutilizados desde 12.03. No cambies sys.path
ni copies reglas de análisis dentro de la interfaz para resolver un import.

Para comparar con el JSON entrega los mismos filtros al ejecutar.py de tu copia:
`--corte 2026-09-30 --minimo 2001` devuelve 003/2500 y universo 4500.
`--segmentos` sin valores selecciona ninguno; omitir ese argumento usa ambos.
El ejecutor no conoce las elecciones guardadas en la sesión del navegador.

## Comprobaciones opcionales

En el mismo shell, ejecuta
`python curriculum/12_streamlit/04_session_state_forms/comprobar_app.py`.
Si elegiste uv, antepón `uv run --locked --group streamlit` al comando.
Utiliza copias temporales y necesita Streamlit; no modifica tu práctica ni las
fuentes de 12.03. AppTest se desarrollará como tema en 12.08.

AppTest revisa estados y envíos, pero no sustituye el navegador para comprobar
las ediciones que todavía no se enviaron al servidor. Haz también el lab.

[← Lección 12.04](README.md) · [Lab 12.04](../../../labs/12_streamlit/04_session_state_forms/README.md)

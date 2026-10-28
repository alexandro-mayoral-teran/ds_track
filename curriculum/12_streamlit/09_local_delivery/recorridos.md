# 12.09 — Preparación, entrega y reconstrucción

Vuelve a la [lección](README.md). Empieza en la raíz del repositorio con tu
entorno local de 12.01. Si no existe, consulta sus
[recorridos](../01_first_app_execution/recorridos.md). No hay paquetes ni
lockfiles nuevos; referencias: Python 3.12.12/Streamlit 1.66.1/Altair 6.3.0.

Elige **un shell y un gestor**. Los destinos practica_1209, entrega_1209 y
reconstruida_1209 deben ser nuevos; si existen, conserva su contenido y cambia
las rutas en todo tu recorrido. El preparador reúne 18 archivos, el constructor
genera una entrega de 36 y el verificador solo lee. No se inicia un servidor
ni se instalan dependencias al preparar, crear o verificar.

Los comandos de reconstrucción se ejecutan desde la raíz para evitar cambios
de carpeta; la lección y el README de entrega muestran también cómo hacerlo
desde dentro de ella sin acceder al repositorio original.

## PowerShell

### uv

Prepara, crea y verifica una vez:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py crear output/entrega_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```powershell
uv run --locked --group streamlit python output/entrega_1209/entrega.py crear output/reconstruida_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_modelo.py
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```powershell
uv run --locked --group streamlit python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara, crea y verifica una vez:

```powershell
python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
python output/practica_1209/entrega.py crear output/entrega_1209
python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```powershell
python output/entrega_1209/entrega.py crear output/reconstruida_1209
python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
python output/reconstruida_1209/pruebas_modelo.py
python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```powershell
python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

Prepara, crea y verifica una vez:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py crear output/entrega_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```bash
uv run --locked --group streamlit python output/entrega_1209/entrega.py crear output/reconstruida_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_modelo.py
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```bash
uv run --locked --group streamlit python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara, crea y verifica una vez:

```bash
python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
python output/practica_1209/entrega.py crear output/entrega_1209
python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```bash
python output/entrega_1209/entrega.py crear output/reconstruida_1209
python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
python output/reconstruida_1209/pruebas_modelo.py
python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```bash
python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

Prepara, crea y verifica una vez:

```bat
set UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py crear output/entrega_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```bat
uv run --locked --group streamlit python output/entrega_1209/entrega.py crear output/reconstruida_1209
uv run --locked --group streamlit python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_modelo.py
uv run --locked --group streamlit python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```bat
uv run --locked --group streamlit python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara, crea y verifica una vez:

```bat
python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
python output/practica_1209/entrega.py crear output/entrega_1209
python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Reconstruye desde las fuentes entregadas y comprueba la nueva copia:

```bat
python output/entrega_1209/entrega.py crear output/reconstruida_1209
python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
python output/reconstruida_1209/pruebas_modelo.py
python output/reconstruida_1209/pruebas_app.py
```

Inicia la app de la reconstrucción:

```bat
python -m streamlit run output/reconstruida_1209/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Entorno reconstruido en la entrega

Los comandos anteriores reutilizan el entorno existente. Para demostrar una
reconstrucción de dependencias, abre la terminal dentro de la entrega o de su
reconstrucción y sigue su README. Configura UV_PROJECT_ENVIRONMENT=.venv con
la sintaxis de tu shell y ejecuta `uv sync --locked --group streamlit --python 3.12`.
El entorno se crea solo allí; no se incluye al distribuir la carpeta. No uses
una ruta de otro entorno ni mezcles gestores. La primera sincronización puede
necesitar red; no se promete funcionamiento sin paquetes disponibles.

## Navegador y descargas

Abre la URL local mostrada. Si el puerto está ocupado añade `--server.port 8509`.
Ctrl+C detiene solo tu servidor; no cierres procesos ajenos. Repite únicamente
streamlit run para reiniciar. Conserva datos y notas antes: sesión y caché en
memoria no son un registro permanente de la práctica.

Sigue la [demostración](README.md#6-demostrar-la-app-no-solo-la-carpeta). Guarda
dos pares CSV/JSON reales fuera de la carpeta entregable. Relee cada par desde
otra terminal con tu entorno, o después de detener el servidor:

```text
python output/reconstruida_1209/revisar_descarga.py "ruta/seleccion.csv" "ruta/contexto.json"
```

Si elegiste uv, antepón `uv run --locked --group streamlit` en el mismo entorno.
El revisor también funciona con Python estándar. Compara además ID, segmento,
corte y saldo con la referencia externa: una huella coherente no autentica datos.

## Experimento y diagnóstico

Para el experimento del lab, prepara otra entrega con `entrega.py crear
output/alterada_1209`, usando el mismo prefijo Python/uv de tu recorrido.
Verifica cambiando únicamente la carpeta revisada en el comando de referencia;
no cambies el revisor ni la fuente externa. Lee la diferencia entre rechazo de
huella y rechazo por valores tras actualizar esa huella en el experimento.

`crear` rechaza destinos existentes o interiores a su fuente. `verificar`
requiere --referencia y rechaza una referencia situada dentro de la entrega.
No borres carpetas ni regeneres huellas para ocultar fallos; corrige la copia
de trabajo y emite otra entrega con nombre nuevo. Los comandos terminan con
código 2 ante rechazo; revisa cada resultado antes de seguir si tu shell no
se detiene automáticamente.

Los controles opcionales de autoría se ejecutan desde la raíz:

```text
python curriculum/12_streamlit/09_local_delivery/comprobar_entrega.py
```

Con uv antepón el mismo prefijo. Usan Python estándar, copias temporales y doce
métodos; no sustituyen las pruebas de app, la descarga real ni la revisión de
tu compañero. Si el ejecutor bloquea temporales, revisa permisos; no alteres
los esperados ni desactives comprobaciones. Las suites de 12.08 conservan su
contrato original: 7 métodos de modelo y 11 AppTest con las seis filas base.

[← Lección 12.09](README.md) · [Lab 12.09](../../../labs/12_streamlit/09_local_delivery/README.md)

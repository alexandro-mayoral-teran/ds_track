# 12.08 — Preparación y ejecución de pruebas

Vuelve a la [lección](README.md). Empieza en la raíz del repositorio y reutiliza
tu entorno de 12.01. Si falta, consulta sus
[recorridos](../01_first_app_execution/recorridos.md). No hay dependencias nuevas:
unittest viene con Python y AppTest con Streamlit. Referencias comprobadas:
Python 3.12.12, Streamlit 1.66.1 y Altair 6.3.0.

Elige **un gestor y un shell**. El destino `output/practica_1208` debe ser nuevo;
si existe, conserva su contenido y cambia la ruta en todos tus comandos. El
preparador reúne catorce archivos: la app y apoyos de 12.07, un mínimo nuevo
y tres archivos de pruebas. No instala, ejecuta pruebas ni inicia servidores.

Las tres suites se ejecutan por separado con Python. No necesitas abrir el
navegador para AppTest ni ejecutar `streamlit run pruebas_app.py`. Después
iniciarás el servidor para la revisión real de la interfaz y las descargas.

## PowerShell

### uv

Prepara una vez y ejecuta las tres suites, en orden:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
uv run --locked --group streamlit python output/practica_1208/minimo_pruebas.py
uv run --locked --group streamlit python output/practica_1208/pruebas_modelo.py
uv run --locked --group streamlit python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```powershell
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
uv run --locked --group streamlit python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```powershell
uv run --locked --group streamlit python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez y ejecuta las tres suites, en orden:

```powershell
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
python output/practica_1208/minimo_pruebas.py
python output/practica_1208/pruebas_modelo.py
python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```powershell
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```powershell
python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Bash/Zsh

### uv

Prepara una vez y ejecuta las tres suites, en orden:

```bash
export UV_PROJECT_ENVIRONMENT=".environment-practice/streamlit"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
uv run --locked --group streamlit python output/practica_1208/minimo_pruebas.py
uv run --locked --group streamlit python output/practica_1208/pruebas_modelo.py
uv run --locked --group streamlit python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```bash
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
uv run --locked --group streamlit python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```bash
uv run --locked --group streamlit python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez y ejecuta las tres suites, en orden:

```bash
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
python output/practica_1208/minimo_pruebas.py
python output/practica_1208/pruebas_modelo.py
python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```bash
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```bash
python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## CMD / Anaconda Prompt

### uv

Prepara una vez y ejecuta las tres suites, en orden:

```bat
set UV_PROJECT_ENVIRONMENT=.environment-practice/streamlit
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
uv run --locked --group streamlit python output/practica_1208/minimo_pruebas.py
uv run --locked --group streamlit python output/practica_1208/pruebas_modelo.py
uv run --locked --group streamlit python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```bat
uv run --locked --group streamlit python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
uv run --locked --group streamlit python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```bat
uv run --locked --group streamlit python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Conda o venv/pip ya activado

Prepara una vez y ejecuta las tres suites, en orden:

```bat
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/practica_1208
python output/practica_1208/minimo_pruebas.py
python output/practica_1208/pruebas_modelo.py
python output/practica_1208/pruebas_app.py
```

Para la regresión, crea otra copia y comprueba su inicio antes de editar:

```bat
python curriculum/12_streamlit/08_app_testing/preparar_practica.py output/regresion_1208
python output/regresion_1208/pruebas_app.py PruebasApp.test_inicio
```

Repite el segundo comando después del cambio y tras corregirlo.

Para la revisión en navegador usa la copia correcta:

```bat
python -m streamlit run output/practica_1208/app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Resultados y diagnóstico

Antes de añadir tus casos: mínimo, `Ran 1 test`; modelo, `Ran 7 tests`; app,
`Ran 11 tests`. Cada ejecución debe acabar en `OK`. En el experimento deliberado
se espera `FAIL` en `test_inicio` hasta corregir la métrica. El código de salida
de unittest es distinto de cero al fallar: revisa también el resultado de cada
comando si tu shell continúa con el siguiente.

Si aparece `ModuleNotFoundError`, comprueba el intérprete y que ejecutas los
archivos de la copia preparada. No cambies sys.path ni instales paquetes en base.
Los archivos del modelo se importan junto a las pruebas. No ejecutes los tres
archivos de prueba de la fuente educativa: allí los módulos reutilizados todavía
no están reunidos.

Un fallo de permisos en temporales requiere revisar el acceso de tu ejecutor a
su carpeta temporal; no desactives validaciones ni cambies las expectativas para
ocultarlo. Un timeout requiere leer el diagnóstico y comprobar el entorno;
subirlo no corrige una excepción ni una cifra incorrecta. Las suites limpian
su caché y temporales al terminar; no escriben sobre tu cartera.csv preparado.

## Navegador y relectura de archivos

Abre la URL local que muestra Streamlit y sigue la matriz de la
[lección](README.md#7-gráfico-y-descarga-hasta-dónde-llega-la-automatización).
El servidor permanece activo hasta Ctrl+C. Si su puerto está ocupado añade
`--server.port 8508`; no cierres procesos ajenos. Para reiniciar repite solo
`streamlit run` de tu copia, sin volver a preparar sobre ella. Si quieres ver
el mínimo en navegador, detén tu app y sustituye `app.py` por `minimo.py`.

Guarda CSV y JSON del mismo caso. Desde otra terminal con el mismo entorno,
o tras detener tu servidor, ejecuta el revisor con las rutas reales de ambos
archivos. Comando igual en los tres shells con Python activado:

```text
python output/practica_1208/revisar_descarga.py "ruta/seleccion.csv" "ruta/contexto.json"
```

Con uv antepón `uv run --locked --group streamlit`, manteniendo la variable de
entorno elegida. El revisor también funciona con Python estándar. No modifica
archivos: revisa coherencia, no autenticidad, y no reemplaza comparar las cuatro
columnas por ID/corte frente a la muestra conocida.

[← Lección 12.08](README.md) · [Lab 12.08](../../../labs/12_streamlit/08_app_testing/README.md)

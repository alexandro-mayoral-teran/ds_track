# 14.07 — Preparar, producir y conciliar

[Volver a la lección](README.md). Elige Python/Streamlit o R/Shiny; no necesitas
las dos rutas. Todos los nombres propuestos suponen carpetas nuevas. Si existen,
conserva los archivos y cambia los nombres en todos los pasos. Los preparadores
copian 53 fuentes; restaurar los entornos es una operación separada.

## R e IDE, recorrido principal de la ruta Shiny

Desde la raíz de DS Track, en consola R:

```r
source("curriculum/14_reproducible_projects/07_report_app_integration/preparar.R", encoding = "UTF-8")
preparar_integracion("output/practica_1407", app = "shiny")
```

Abre producto_1407.Rproj de esa copia y reinicia R sin workspace. Lee LEEME.md,
entorno.csv, DESCRIPTION, renv.lock y .Rprofile. Confirma getwd(). Se conservan
R 4.6.1 y renv 1.3.1 locales; usa UTF-8 al guardar y cargar tus scripts.

En consola R de la **raíz de la copia**:

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("pruebas.R", encoding = "UTF-8")
probar_proyecto(".")
source("trazar.R", encoding = "UTF-8")
trazar_proyecto(".", "oct01", "config/octubre.csv")
trazar_proyecto(".", "sep01", "config/septiembre.csv")
trazar_proyecto(".", "vacio01", "config/vacio.csv")
source("integracion.R", encoding = "UTF-8")
generar_reporte(".", "octubre", "config/octubre.csv")
renderizar_reporte(".", "octubre", "config/octubre.csv")
generar_reporte(".", "septiembre", "config/septiembre.csv")
renderizar_reporte(".", "septiembre", "config/septiembre.csv")
generar_reporte(".", "vacio", "config/vacio.csv")
renderizar_reporte(".", "vacio", "config/vacio.csv")
```

Se esperan siete grupos aprobados, tres entregas creadas y tres HTML conciliados.
Quarto 1.9.38 existente se detecta en PATH o, en Windows, en la ruta habitual de
RStudio. Si está en otra ubicación, pasa `quarto = "ruta/al/ejecutable"` a
renderizar_reporte. No se instala automáticamente. El render no ejecuta código
R: transforma el .qmd preparado. Si falla, conserva la carpeta; no ocultes el
error ni sobrescribas un HTML previo para repetir.

Abre en el navegador reportes/octubre/reporte.html, septiembre/reporte.html y
vacio/reporte.html. Revisa tabla, contexto, barras y hora de comprobación.
Para comprobar de nuevo desde una sesión nueva de la raíz:

```r
source("integracion.R", encoding = "UTF-8")
verificar_reporte(".", "octubre", "config/octubre.csv")
verificar_reporte(".", "septiembre", "config/septiembre.csv")
verificar_reporte(".", "vacio", "config/vacio.csv")
```

Estas verificaciones son de lectura; no restauran el entorno ni corrigen un
reporte. Rscript permite comprobar una sesión nueva desde terminal. Desde esa
raíz, en PowerShell con Rscript 4.6.1 disponible:

```powershell
Rscript --vanilla -e 'source(".Rprofile"); source("integracion.R", encoding="UTF-8"); verificar_reporte(".", "octubre")'
if ($LASTEXITCODE -ne 0) { throw "Revisar reporte." }
```

En Bash, alternativa completa de esa comprobación:

```bash
Rscript --vanilla -e 'source(".Rprofile"); source("integracion.R", encoding="UTF-8"); verificar_reporte(".", "octubre")' || exit 1
```

### Abrir la interfaz Shiny

Abre **interfaz/r/interfaz_1407.Rproj** en otro proyecto/sesión del IDE y reinicia
sin workspace. La biblioteca de la raíz de cálculo y la de la interfaz son
distintas. Confirma que getwd() termina en interfaz/r. Lee DESCRIPTION y
renv.lock de esta interfaz: se reutilizan los de 13.01, con Shiny 1.14.0 y
renv 1.3.1; restaurar puede descargar esos paquetes a su biblioteca local.

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("iniciar.R", encoding = "UTF-8")
iniciar_app(puerto = 8861, abrir = TRUE)
```

Abre http://127.0.0.1:8861 si no se abre automáticamente. La consola queda ocupada
mientras sirve la app. Pulsa Detener/Esc en el IDE cuando termines. En terminal,
Ctrl+C detiene el proceso. Si el puerto está ocupado, elige otro disponible.

En el navegador:

1. Confirma que no hay cifras al abrir una sesión nueva.
2. Elige Octubre, pulsa Comprobar entrega y contrasta con su reporte.
3. Elige Septiembre sin pulsar: la vista anterior debe seguir identificada como
   octubre y aparecer un aviso de borrador distinto. Pulsa para aplicar septiembre.
4. Aplica Selección vacía: contexto válido, cero seleccionados, tabla sin filas
   y sin barras. Compara su reporte.
5. Aplica Sin universo: debe aparecer rechazo y retirarse la vista anterior.
6. Abre otra sesión/recarga: empieza sin consulta aplicada.

Repite desde una sesión nueva del IDE cargando el script completo. La revisión
de autoría con Rscript y navegador en Windows no acredita operar toda la interfaz
del IDE ni ejecutar Bash/Linux. Si renv informa paquetes base inconsistentes en
un ejecutor restringido, revisa permisos de lectura de su sandbox sin desactivar
los controles para ocultar el problema. Continúa con el [lab](../../../labs/14_reproducible_projects/07_report_app_integration/README.md).

## PowerShell y Python/Streamlit, alternativa completa

Desde DS Track, con uv/Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/07_report_app_integration/preparar.py output/practica_1407 --app streamlit
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
Set-Location output/practica_1407
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de calculo." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -ne 0) { throw "Revisar pruebas." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py oct01 --config config/octubre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega de octubre." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sep01 --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega de septiembre." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py vacio01 --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega vacia." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar septiembre --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar septiembre --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar vacio --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar preparacion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar vacio --config config/vacio.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar render." }
```

Abre los tres reporte.html en sus carpetas bajo reportes/. Se esperan 003/2600,
002/2000 + 003/2500 y selección vacía con universo. Para verificar el HTML de
octubre, en esta misma raíz:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre
if ($LASTEXITCODE -ne 0) { throw "Revisar conciliacion." }
```

El render detecta Quarto existente; si hace falta, añade `--quarto` con la ruta
completa. Solo esa acción acepta la opción. No borra reportes ni instala Quarto.

### Abrir Streamlit

Desde la raíz de la copia cambia al proyecto de interfaz, que tiene su propio
pyproject.toml/uv.lock. Se conservan versiones ya usadas en el curso; el lockfile
separado incluye Streamlit 1.66.1. La raíz de cálculo sigue sin paquetes externos.

```powershell
Set-Location interfaz/python
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de interfaz." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860. Revisa inicio sin cifras; octubre; borrador de
septiembre sin aplicar; septiembre aplicado; vacío; rechazo sin universo y
sesión nueva, como en la lista del recorrido R. Compara los tres reportes.
La terminal permanece ocupada; Ctrl+C detiene la app. No se inicia un servicio
público ni se guarda la consulta en disco. Continúa con el [lab](../../../labs/14_reproducible_projects/07_report_app_integration/README.md).

## Bash y Python/Streamlit, alternativa completa

Desde DS Track, con uv/Python 3.12.12 disponibles. Este recorrido no acredita
una ejecución en Linux o macOS; las comprobaciones de autoría se hicieron en Windows.

```bash
python curriculum/14_reproducible_projects/07_report_app_integration/preparar.py output/practica_1407 --app streamlit || exit 1
cd output/practica_1407 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py oct01 --config config/octubre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sep01 --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py vacio01 --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar octubre || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar octubre || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar septiembre --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar septiembre --config config/septiembre.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py generar vacio --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py renderizar vacio --config config/vacio.csv || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python integracion.py verificar octubre || exit 1
```

Abre los HTML de reportes/octubre, septiembre y vacio y compara con los valores
de referencia. Si Quarto está fuera de PATH, indica --quarto en renderizar.
Después restaura e inicia solo la interfaz elegida:

```bash
cd interfaz/python || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860. Comprueba los mismos estados del recorrido R: inicio,
borrador sin aplicar, casos habitual/vacío, rechazo y sesión nueva. Ctrl+C detiene
la app. Conserva carpetas y registros; realiza el [lab](../../../labs/14_reproducible_projects/07_report_app_integration/README.md).

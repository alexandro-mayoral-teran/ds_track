# 14.08 — Crear, comprobar y reconstruir una entrega

[Volver a la lección](README.md). Esta sección es opcional. Elige una ruta
completa; no necesitas ambas. Todos los destinos e identificadores propuestos
suponen nombres nuevos. Si existen, conserva las copias y cambia el nombre en
todos los pasos. Los preparadores no instalan paquetes ni habilitan CI.

## R e IDE, recorrido principal de la ruta Shiny

Desde DS Track, en consola R:

```r
source("curriculum/14_reproducible_projects/08_delivery_optional_automation/preparar.R", encoding = "UTF-8")
preparar_entrega("output/practica_1408", app = "shiny")
```

Abre producto_1408.Rproj de la copia, reinicia sin workspace y confirma getwd().
Lee LEEME.md, catalogo.csv, entorno.csv, DESCRIPTION, renv.lock y .Rprofile.
Se conservan R 4.6.1 y renv 1.3.1 locales; no se instala una biblioteca global.
Quarto 1.9.38 existente es la versión comprobada.

En consola de la **raíz de la copia**:

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("reconstruir.R", encoding = "UTF-8")
reconstruir_producto(".")
```

Se esperan siete grupos aprobados, tres intentos recon_*, tres consultas bajo
salidas/ y tres HTML bajo reportes/. Si Quarto está fuera de PATH y de su ruta
habitual de RStudio en Windows, indica `quarto = "ruta/al/ejecutable"`.
No se instala automáticamente ni se abre la app durante esta reconstrucción.

Ahora crea una carpeta hermana del proyecto, usando el CSV original de esta
copia como referencia externa al paquete:

```r
source("entrega.R", encoding = "UTF-8")
referencia <- normalizePath("datos/entrada/cartera.csv", winslash = "/", mustWork = TRUE)
crear_entrega("../paquete_shiny", referencia)
verificar_entrega("../paquete_shiny", referencia)
copiar_fuentes("../paquete_shiny", "../reconstruida_1408", referencia)
```

La referencia no puede estar dentro del paquete. Al revisar una entrega de otra
persona, usa el CSV original que conservaste por separado. El revisor y su
catálogo deben venir de herramientas revisadas fuera de esa entrega.
Se esperan 90 archivos en el paquete y 60 fuentes en la copia nueva, sin
salidas/, reportes/, biblioteca, cachés ni intentos del autor. Verificar y copiar
no ejecutan código recibido ni restauran el entorno.

Revisa las fuentes copiadas antes de abrir su proyecto, en especial .Rprofile,
activador, código y scripts. Después abre **producto_1408.Rproj de la copia nueva**,
reinicia sin workspace y restaura su biblioteca local:

```r
getwd()
source("restaurar.R", encoding = "UTF-8")
source("reconstruir.R", encoding = "UTF-8")
reconstruir_producto(".")
```

No copies muestra/ ni renv/library. Abre los HTML nuevos de reportes/octubre,
septiembre y vacio y compáralos con muestra/reportes/ del paquete. Horas de
comprobación pueden cambiar; datos y filtros deben conciliar. La repetición
sobre salidas ocupadas se rechaza: conserva la copia y usa otra para repetir todo.

### Abrir Shiny después de reconstruir

Abre interfaz/r/interfaz_1407.Rproj de la copia reconstruida; se conserva el
nombre de interfaz de 14.07. Reinicia, confirma que getwd() termina en interfaz/r,
revisa sus metadatos y restaura solo esa interfaz:

```r
source("restaurar.R", encoding = "UTF-8")
source("iniciar.R", encoding = "UTF-8")
iniciar_app(puerto = 8861, abrir = TRUE)
```

Aplica octubre, septiembre y selección vacía. Compara filas, indicadores y
barras con el reporte reconstruido y la muestra recibida. La opción Sin universo
debe rechazar y retirar cifras anteriores. Abre otra sesión para comprobar que
no hereda una consulta aplicada. Detener/Esc en el IDE o Ctrl+C en terminal
terminan el servidor; solo escucha en 127.0.0.1.

### Verificación opcional desde terminal

Desde la raíz de las herramientas revisadas, con Rscript 4.6.1 disponible.
En PowerShell:

```powershell
Rscript --vanilla -e 'source("entrega.R", encoding="UTF-8"); verificar_entrega("../paquete_shiny", "datos/entrada/cartera.csv")'
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega." }
```

En Bash, alternativa completa de esa verificación:

```bash
Rscript --vanilla -e 'source("entrega.R", encoding="UTF-8"); verificar_entrega("../paquete_shiny", "datos/entrada/cartera.csv")' || exit 1
```

El verificador solo necesita R base y las herramientas locales revisadas; no
activa renv ni restaura paquetes. La construcción/reconstrucción sí exige su
entorno local. En Windows revisa permisos del sandbox si renv informa paquetes
base inconsistentes, sin desactivar controles. Rscript y navegador no acreditan
operar toda la interfaz del IDE. Continúa con el [lab](../../../labs/14_reproducible_projects/08_delivery_optional_automation/README.md).

## PowerShell y Python/Streamlit, alternativa completa

Desde DS Track, con uv y Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/08_delivery_optional_automation/preparar.py output/practica_1408 --app streamlit
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
Set-Location output/practica_1408
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de calculo." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py
if ($LASTEXITCODE -ne 0) { throw "Revisar reconstruccion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python entrega.py crear ../paquete_streamlit --referencia datos/entrada/cartera.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar creacion de entrega." }
python entrega.py verificar ../paquete_streamlit --referencia datos/entrada/cartera.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar entrega." }
python entrega.py copiar ../paquete_streamlit ../reconstruida_1408 --referencia datos/entrada/cartera.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar copia de fuentes." }
```

Crear usa el entorno de cálculo comprobado. Verificar/copiar requieren solo la
biblioteca estándar de Python 3.12 o posterior y no ejecutan código recibido;
las herramientas deben estar fuera del paquete y ser una copia revisada.
Se esperan 90 archivos en el paquete y 60 en la copia de fuentes.

Revisa código y metadatos copiados antes de ejecutar. Después, desde la raíz
de la copia nueva:

```powershell
Set-Location ../reconstruida_1408
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno nuevo." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py
if ($LASTEXITCODE -ne 0) { throw "Revisar reconstruccion desde fuentes." }
```

Indica --quarto con su ruta si no se detecta la instalación existente. Abre los
HTML nuevos y compara con la muestra, sin copiarla. Después restaura e inicia
solo la interfaz de esta copia:

```powershell
Set-Location interfaz/python
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno de interfaz." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860. Aplica octubre, septiembre y vacío; compara filtros,
filas, sumas, universo y cobertura con reportes nuevos y muestra/. Un borrador
no cambia la vista aplicada; Sin universo retira cifras al rechazar. Ctrl+C
detiene el servidor. Continúa con el [lab](../../../labs/14_reproducible_projects/08_delivery_optional_automation/README.md).

## Bash y Python/Streamlit, alternativa completa

Desde DS Track, con uv/Python 3.12.12 disponibles. La revisión de autoría se
realizó en Windows; este recorrido no certifica Linux/macOS.

```bash
python curriculum/14_reproducible_projects/08_delivery_optional_automation/preparar.py output/practica_1408 --app streamlit || exit 1
cd output/practica_1408 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python entrega.py crear ../paquete_streamlit --referencia datos/entrada/cartera.csv || exit 1
python entrega.py verificar ../paquete_streamlit --referencia datos/entrada/cartera.csv || exit 1
python entrega.py copiar ../paquete_streamlit ../reconstruida_1408 --referencia datos/entrada/cartera.csv || exit 1
```

Se esperan siete grupos aprobados, tres consultas/reportes, paquete de 90
archivos verificado y otra carpeta de 60 fuentes. Revisa las fuentes copiadas
antes de continuar; no copies resultados ni entornos. Después:

```bash
cd ../reconstruida_1408 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python reconstruir.py || exit 1
```

Compara los tres reportes nuevos con la muestra y, si hace falta, pasa --quarto
con la ruta del ejecutable. Restaura/inicia solo la interfaz elegida:

```bash
cd interfaz/python || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8860 --browser.gatherUsageStats false
```

Abre http://127.0.0.1:8860, aplica los casos y compara sus valores y contexto.
Revisa borrador sin aplicar, vacío válido y rechazo sin cifras anteriores.
Ctrl+C detiene la app; realiza el [lab](../../../labs/14_reproducible_projects/08_delivery_optional_automation/README.md).

## CI opcional: comprobar solo su comando local

La plantilla no está activa. Si deseas ensayar su comando, copia las fuentes a
**otra carpeta nueva**, distinta de las anteriores y sin .venv. Usa Python 3.12.12
y confirma python --version antes de crear el entorno. No hace falta instalar uv
para esta prueba de cálculo, que no tiene dependencias externas.

PowerShell, desde esa copia nueva:

```powershell
python -m venv --without-pip .venv
if ($LASTEXITCODE -ne 0) { throw "Revisar venv." }
& ./.venv/Scripts/python.exe pruebas.py
if ($LASTEXITCODE -ne 0) { throw "Revisar pruebas." }
```

El comando del YAML es específico de Windows. No equivale a reconstruir Quarto
ni a restaurar los entornos de interfaz. No se acredita una ejecución en GitHub
Actions ni se activa un workflow del repositorio al estudiar la plantilla.

# 14.04 — Preparar, repetir y separar cortes

Vuelve a la [lección](README.md). Elige una ruta completa; no necesitas ejecutar
las tres. Parte de la raíz del repositorio y de una carpeta nueva. Si existe,
conserva su contenido y sustituye el nombre en todos los pasos.

## R e IDE, recorrido principal

En consola R, desde la raíz del repositorio:

```r
source("curriculum/14_reproducible_projects/04_pipeline_reprocessing/preparar.R")
preparar_pipeline("output/practica_1404")
```

Lee LEEME.md, .Rprofile, entorno.csv y renv.lock de la copia. Abre
producto_1404.Rproj en el IDE y reinicia R sin workspace. Confirma que getwd()
señala esa copia. R 4.6.1 y renv 1.3.1; restaurar puede descargar renv solo para
esta biblioteca local. No cambia Conda ni bibliotecas globales.

```r
getwd()
source("restaurar.R")
source("pipeline.R")
pipeline_proyecto(".") # creada
antes <- tools::md5sum(list.files("salidas/octubre", full.names = TRUE))
pipeline_proyecto(".") # reutilizada y comprobada
stopifnot(identical(antes, tools::md5sum(list.files("salidas/octubre", full.names = TRUE))))
```

Otro corte: copia la configuración sin sobrescribir y cambia **corte y salida**.
El siguiente helper crea archivos nuevos con las siete claves del original:

```r
crear_config <- function(nombre, corte, salida) {
  ruta <- paste0("config/", nombre, ".csv")
  if (file.exists(ruta)) stop("Elige otro nombre de configuracion.")
  tabla <- read.csv("config/consulta.csv", colClasses = "character")
  tabla$valor[tabla$clave == "corte"] <- corte
  tabla$valor[tabla$clave == "salida"] <- salida
  write.csv(tabla, ruta, row.names = FALSE)
  ruta
}
septiembre <- crear_config("septiembre", "2026-09-30", "salidas/septiembre")
pipeline_proyecto(".", septiembre)
read.csv("salidas/septiembre/contexto.csv", colClasses = "character")
read.csv("salidas/septiembre/seleccion.csv", colClasses = "character")
```

Resultado: septiembre selecciona 002/2000 y 003/2500; universo 3/4500,
selección 2/4500 MXN. Octubre conserva 003/2600, universo 3/4600.

Fallo controlado en un destino nuevo; tryCatch permite observar el error esperado:

```r
fallo <- crear_config("fallo", "2026-10-31", "salidas/reintento")
tryCatch(pipeline_proyecto(".", fallo, simular_fallo = TRUE), error = function(e) message(conditionMessage(e)))
stopifnot(!dir.exists("salidas/reintento"))
list.files("salidas", all.files = TRUE)
pipeline_proyecto(".", fallo) # crea final; conserva el temporal fallido
```

No copies archivos del temporal al destino. La sesión nueva para comprobar una
copia ya restaurada puede iniciarse con Rscript --vanilla, source(".Rprofile"),
source("pipeline.R") y pipeline_proyecto("."). La ejecución en Rscript no
acredita toda la interacción con el IDE. Si falla lectura del sandbox en Windows,
revisa permisos del ejecutor sin desactivar las comprobaciones de renv.

## PowerShell y Python/uv, alternativa completa

Desde la raíz del repositorio, con uv y Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/04_pipeline_reprocessing/preparar.py output/practica_1404
if ($LASTEXITCODE -ne 0) { throw "Revisa preparacion." }
Set-Location output/practica_1404
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisa entorno." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py
if ($LASTEXITCODE -ne 0) { throw "Revisa ejecucion." }
$antes1404 = Get-ChildItem -LiteralPath salidas/octubre -File | Get-FileHash -Algorithm MD5
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py
if ($LASTEXITCODE -ne 0) { throw "Revisa repeticion." }
$despues1404 = Get-ChildItem -LiteralPath salidas/octubre -File | Get-FileHash -Algorithm MD5
Compare-Object $antes1404 $despues1404 -Property Path,Hash
```

Compare-Object no debe mostrar diferencias. Si sync necesita un intérprete,
añade --python y su ruta real. Crea configuración nueva:

```powershell
if (Test-Path -LiteralPath config/septiembre.csv) { throw "Elige otro nombre." }
$tabla1404 = Import-Csv -LiteralPath config/consulta.csv
($tabla1404 | Where-Object clave -eq corte).valor = "2026-09-30"
($tabla1404 | Where-Object clave -eq salida).valor = "salidas/septiembre"
$tabla1404 | Export-Csv -LiteralPath config/septiembre.csv -NoTypeInformation -Encoding utf8
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisa septiembre." }
Import-Csv -LiteralPath salidas/septiembre/contexto.csv
Import-Csv -LiteralPath salidas/septiembre/seleccion.csv
```

Debe dar los resultados de septiembre indicados arriba. Para el fallo:

```powershell
if (Test-Path -LiteralPath config/fallo.csv) { throw "Elige otro nombre." }
$tabla1404 = Import-Csv -LiteralPath config/consulta.csv
($tabla1404 | Where-Object clave -eq salida).valor = "salidas/reintento"
$tabla1404 | Export-Csv -LiteralPath config/fallo.csv -NoTypeInformation -Encoding utf8
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/fallo.csv --simular-fallo
if ($LASTEXITCODE -eq 0) { throw "Se esperaba un fallo didactico." }
if (Test-Path -LiteralPath salidas/reintento) { throw "No debe existir final." }
Get-ChildItem -LiteralPath salidas -Force
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/fallo.csv
if ($LASTEXITCODE -ne 0) { throw "Revisa reintento." }
```

El error inicial es esperado. No uses estos comandos sobre una entrega existente:
la simulación se ejecuta solo al crear una nueva.

## Bash y Python/uv, alternativa completa

Desde la raíz del repositorio. Este recorrido presupone uv/Python 3.12.12 y una
shell Bash; la revisión de autoría se realizó en Windows, sin certificar Linux.

```bash
python curriculum/14_reproducible_projects/04_pipeline_reprocessing/preparar.py output/practica_1404 || exit 1
cd output/practica_1404 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py || exit 1
```

Para crear configuraciones sin sobrescribir, desde esa copia:

```bash
uv run --locked --no-python-downloads --cache-dir .uv-cache python - <<'PY'
import csv
from pathlib import Path
with open('config/consulta.csv', encoding='utf-8-sig', newline='') as f:
    original = list(csv.DictReader(f))
for nombre, corte, salida in [('septiembre','2026-09-30','salidas/septiembre'),
                              ('fallo','2026-10-31','salidas/reintento')]:
    filas = [dict(f) for f in original]
    for f in filas:
        if f['clave'] == 'corte': f['valor'] = corte
        if f['clave'] == 'salida': f['valor'] = salida
    with Path('config', nombre+'.csv').open('x', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['clave','valor'])
        w.writeheader(); w.writerows(filas)
PY
```

Detente si falla la creación de configuraciones. Después:

```bash
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/septiembre.csv || exit 1
if uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/fallo.csv --simular-fallo; then
    echo 'Se esperaba un fallo'; exit 1
fi
test ! -e salidas/reintento || exit 1
ls -a salidas
uv run --locked --no-python-downloads --cache-dir .uv-cache python pipeline.py --config config/fallo.csv || exit 1
```

En las tres rutas, compara el contenido de seleccion.csv y contexto.csv, no solo
el mensaje de consola. Continúa al [lab](../../../labs/14_reproducible_projects/04_pipeline_reprocessing/README.md).

# 14.05 — Preparar y ejecutar las pruebas

[Volver a la lección](README.md). Elige un recorrido completo; no necesitas ambos
lenguajes. Parte de la raíz del repositorio y prepara una carpeta nueva. Si existe,
consérvala y elige otro nombre en todos los pasos. Los preparadores no instalan.

## R e IDE, recorrido principal

En consola R, desde la raíz de DS Track:

```r
source("curriculum/14_reproducible_projects/05_tests_data_quality/preparar.R")
preparar_pruebas("output/practica_1405")
```

Lee LEEME.md, entorno.csv, .Rprofile, DESCRIPTION y renv.lock de la copia.
Abre producto_1405.Rproj, reinicia R sin workspace y confirma getwd().
Se requieren R 4.6.1 y renv 1.3.1 en la biblioteca local. Restaurar puede descargar
renv; no cambia Conda ni bibliotecas globales.

```r
getwd()
source("restaurar.R")
source("pruebas.R")
probar_proyecto(".")
```

Resultado esperado: siete grupos PASA y `7 grupos; 0 fallas.`. La suite también
imprime la carpeta de fixtures. No interpreta los errores esperados como fallas
si se cumplieron las aserciones correspondientes. Si hay FALLA, revisa el grupo
y el mensaje; al final se lanza un error. Un problema de entorno puede detener
antes de iniciar los grupos.

Inspecciona referencia/criterios.csv, referencia/calidad.csv y un directorio de
ensayo. No modifiques los criterios para hacer pasar un resultado incorrecto.
Para repetir desde una sesión nueva, reinicia el IDE, deja activar el perfil y
vuelve a source("pruebas.R") / probar_proyecto("."). No guardes el workspace.
La ejecución en Rscript es una comprobación distinta de operar toda la interfaz
del IDE; en Windows revisa permisos de lectura del sandbox antes de atribuir un
fallo a renv, sin desactivar sus comprobaciones.

### Ensayo del defecto en otra copia

Vuelve al proyecto/repositorio DS Track y prepara otra carpeta, por ejemplo
output/falla_1405, con el mismo preparador. Abre su producto_1405.Rproj, reinicia
y restaura como arriba. Trabaja ahora **solo en esa segunda copia**.

En consola R, conserva un respaldo nuevo:

```r
if (file.exists("codigo/modelo_original.R")) stop("Ya existe respaldo; revisa antes de continuar.")
stopifnot(file.copy("codigo/modelo.R", "codigo/modelo_original.R", overwrite = FALSE))
```

En el editor abre codigo/modelo.R. Cambia solo esta comparación:

```r
# Original
universo$saldo_mxn >= as.numeric(minimo)
# Defecto didactico
universo$saldo_mxn > as.numeric(minimo)
```

Guarda el archivo y ejecuta la suite desde consola. El tryCatch de este ejemplo
permite observar el error esperado sin interrumpir tu trabajo interactivo:

```r
source("pruebas.R")
tryCatch(probar_proyecto("."), error = function(e) message(conditionMessage(e)))
```

Debe aparecer FALLA en criterios y/o integración: septiembre ya no incluye 002.
El defecto no se corrige cambiando el esperado a 003. Restaura el archivo que
acabas de alterar desde su respaldo y ejecuta de nuevo, sin capturar el error final:

```r
stopifnot(file.copy("codigo/modelo_original.R", "codigo/modelo.R", overwrite = TRUE))
source("pruebas.R")
probar_proyecto(".")
```

Se esperan siete grupos aprobados. El respaldo y las tandas de ensayo se conservan.
No se modifica el modelo del curso ni una entrega anterior.

## PowerShell y Python/uv, alternativa completa

Desde la raíz del repositorio, con uv y Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/05_tests_data_quality/preparar.py output/practica_1405
if ($LASTEXITCODE -ne 0) { throw "Revisa preparacion." }
Set-Location output/practica_1405
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisa version y entorno." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -ne 0) { throw "La suite no aprobo; revisa el resumen." }
```

Si necesitas seleccionar intérprete, añade --python y su ruta real a sync.
Se esperan `Ran 7 tests` y `OK`. Algunos casos están dentro de subTest: siete
métodos no significa siete entradas. Para el ejemplo mínimo de la lección,
guarda minimo.py en esta carpeta y usa el mismo uv run, sustituyendo pruebas.py
por minimo.py. Debe aprobar una prueba.

### Ensayo del defecto en otra copia

Vuelve a la raíz del repositorio y prepara una segunda copia:

```powershell
Set-Location ../..
python curriculum/14_reproducible_projects/05_tests_data_quality/preparar.py output/falla_1405
if ($LASTEXITCODE -ne 0) { throw "Revisa preparacion nueva." }
Set-Location output/falla_1405
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisa entorno." }
if (Test-Path -LiteralPath codigo/modelo_original.py) { throw "Ya existe respaldo; revisa." }
Copy-Item -LiteralPath codigo/modelo.py -Destination codigo/modelo_original.py -ErrorAction Stop
```

Abre codigo/modelo.py en el editor y cambia solo:

```python
# Original
int(f["saldo_mxn"]) >= int(minimo)
# Defecto didactico
int(f["saldo_mxn"]) > int(minimo)
```

Guarda y ejecuta. Ahora el código de salida distinto de cero es esperado:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -eq 0) { throw "La suite debio detectar el defecto." }
Copy-Item -LiteralPath codigo/modelo_original.py -Destination codigo/modelo.py -Force -ErrorAction Stop
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -ne 0) { throw "La suite debe aprobar despues de restaurar." }
```

Revisa en la salida que el rechazo corresponde al comparador modificado, no a
un Python equivocado o un archivo ausente. Conserva el resumen de ambas ejecuciones.

## Bash y Python/uv, alternativa completa

Desde la raíz del repositorio, con uv/Python 3.12.12 disponibles. La revisión de
autoría se ejecutó en Windows; este recorrido no certifica Linux ni macOS.

```bash
python curriculum/14_reproducible_projects/05_tests_data_quality/preparar.py output/practica_1405 || exit 1
cd output/practica_1405 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py || exit 1
```

Se esperan siete métodos y OK; inspecciona fixtures y casos literales. Para
introducir el defecto en otra copia:

```bash
cd ../.. || exit 1
python curriculum/14_reproducible_projects/05_tests_data_quality/preparar.py output/falla_1405 || exit 1
cd output/falla_1405 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
test ! -e codigo/modelo_original.py || exit 1
cp codigo/modelo.py codigo/modelo_original.py || exit 1
```

En el editor cambia solo `int(f["saldo_mxn"]) >= int(minimo)` por
`int(f["saldo_mxn"]) > int(minimo)` y guarda. Después:

```bash
if uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py; then
    echo 'La suite debio detectar el defecto'; exit 1
fi
cp codigo/modelo_original.py codigo/modelo.py || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py || exit 1
```

Confirma que la falla muestra el efecto del comparador y que la restauración
recupera OK. Continúa con el [lab](../../../labs/14_reproducible_projects/05_tests_data_quality/README.md).

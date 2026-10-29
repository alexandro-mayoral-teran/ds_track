# 14.06 — Preparar, observar y recuperar

[Volver a la lección](README.md). Elige un recorrido completo. Los nombres
propuestos suponen carpetas nuevas: si existen, conserva todo y cambia el
nombre de la copia en todos los pasos. Cada intento también exige nombre nuevo.
Los preparadores no instalan. Lee [LEEME](plantilla/LEEME.md) antes de restaurar.

## R e IDE, recorrido principal

En consola R desde la raíz de DS Track:

```r
source("curriculum/14_reproducible_projects/06_traceability_recovery/preparar.R")
preparar_trazabilidad("output/practica_1406")
```

Abre producto_1406.Rproj de esa copia en RStudio o tu IDE. Reinicia R sin
workspace, confirma getwd() y revisa entorno.csv, DESCRIPTION, renv.lock y
.Rprofile. Necesitas R 4.6.1 y renv 1.3.1 local, como en 14.03.

En consola R de la copia:

```r
getwd()
source("restaurar.R")
source("trazar.R")
source("pruebas.R")
probar_proyecto(".")
tryCatch(trazar_proyecto(".", "a01", simular_fallo = TRUE),
  error = function(error) message(conditionMessage(error)))
eventos <- read.csv("intentos/a01/eventos.csv", colClasses = "character")
eventos[c("secuencia", "etapa", "evento", "detalle")]
read.csv("intentos/a01/error.csv", colClasses = "character")
readLines("intentos/a01/consola.txt")
dir.exists("salidas/octubre")
list.files("salidas", all.files = TRUE)
```

La suite debe aprobar siete grupos. El intento a01 debe terminar FALLO en
pipeline por la simulación, y salidas/octubre debe seguir ausente (`FALSE`).
Localiza en consola.txt el temporal que conserva seleccion.csv. El tryCatch
exterior permite observar **este error esperado** sin terminar la sesión.
No lo uses para ignorar fallas desconocidas.

Ahora ejecuta sin simulación:

```r
trazar_proyecto(".", "a02")
read.csv("salidas/octubre/seleccion.csv", colClasses = "character")
read.csv("salidas/octubre/contexto.csv", colClasses = "character")
trazar_proyecto(".", "a03")
read.csv("intentos/a03/eventos.csv", colClasses = "character")
```

a02 crea y a03 reutiliza. Contrasta 003/2600, tres créditos y 4600 MXN en
universo, uno seleccionado y cobertura 1/3. El temporal a01 permanece.
Reinicia R y vuelve a cargar trazar.R: con otro nombre, por ejemplo a04, la
consulta debe seguir siendo reutilizable sin depender del workspace anterior.

### Fallo final en una segunda copia R

Desde DS Track prepara otra copia con el mismo preparador:
`preparar_trazabilidad("output/cierre_1406")`. Abre su producto_1406.Rproj,
reinicia y restaura. En consola de esa **segunda copia**:

```r
source("restaurar.R")
source("trazar.R")
tryCatch(trazar_proyecto(".", "b01", simular_fallo_final = TRUE),
  error = function(error) message(conditionMessage(error)))
dir.exists("salidas/octubre")
read.csv("intentos/b01/eventos.csv", colClasses = "character")
trazar_proyecto(".", "b02")
```

Debe existir entrega (`TRUE`) aunque b01 termine FALLO en cierre. b02 la
comprueba y devuelve reutilizada. Si falla por otra causa, diagnostica antes
de continuar. Nunca ejecutes ambas simulaciones a la vez.

Para comprobación opcional en terminal PowerShell con **Rscript 4.6.1** disponible:

```powershell
Rscript --vanilla -e 'source(".Rprofile"); source("trazar.R"); trazar_proyecto(".", "terminal01")'
if ($LASTEXITCODE -ne 0) { throw "Revisar diagnostico e intento." }
```

En Bash, desde la copia y con esa misma versión de Rscript:

```bash
Rscript --vanilla -e 'source(".Rprofile"); source("trazar.R"); trazar_proyecto(".", "terminal02")' || exit 1
```

Rscript comprueba una sesión nueva; no acredita operar toda la interfaz del IDE.
En Windows, si renv informa paquetes base inconsistentes al activar su sandbox,
revisa permisos de lectura del ejecutor. No desactives sus comprobaciones para
hacer desaparecer el error. Bash/Linux e interfaz completa del IDE requieren
sus propias revisiones.

## PowerShell y Python/uv, alternativa completa

Desde DS Track, con uv y Python 3.12.12 disponibles:

```powershell
python curriculum/14_reproducible_projects/06_traceability_recovery/preparar.py output/practica_1406
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
Set-Location output/practica_1406
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py
if ($LASTEXITCODE -ne 0) { throw "Revisar pruebas." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a01 --simular-fallo
if ($LASTEXITCODE -eq 0) { throw "Se esperaba el fallo didactico." }
Import-Csv intentos/a01/eventos.csv | Format-Table secuencia,etapa,evento,detalle -Wrap
Get-Content intentos/a01/error.txt
Get-Content intentos/a01/consola.txt
Test-Path salidas/octubre
Get-ChildItem salidas -Force
```

Se esperan siete pruebas OK y después el RuntimeError didáctico. Confirma que
el fallo corresponde al temporal, no a otro problema. El destino final debe
estar ausente (`False`). Después:

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a02
if ($LASTEXITCODE -ne 0) { throw "Revisar recuperacion." }
Import-Csv salidas/octubre/seleccion.csv
Import-Csv salidas/octubre/contexto.csv
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a03
if ($LASTEXITCODE -ne 0) { throw "Revisar reutilizacion." }
Import-Csv intentos/a03/eventos.csv | Format-Table secuencia,etapa,evento,detalle -Wrap
```

a02 crea; a03 reutiliza. Cada comando abre un proceso nuevo. Contrasta los
resultados con la tabla de la lección, no solo con el mensaje TERMINADO.

### Fallo final en una segunda copia Python

Desde la primera copia vuelve al repo y prepara otra:

```powershell
Set-Location ../..
python curriculum/14_reproducible_projects/06_traceability_recovery/preparar.py output/cierre_1406
if ($LASTEXITCODE -ne 0) { throw "Revisar copia." }
Set-Location output/cierre_1406
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisar entorno." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py b01 --simular-fallo-final
if ($LASTEXITCODE -eq 0) { throw "Se esperaba el fallo de cierre." }
Test-Path salidas/octubre
Import-Csv intentos/b01/eventos.csv | Format-Table secuencia,etapa,evento,detalle -Wrap
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py b02
if ($LASTEXITCODE -ne 0) { throw "Revisar comprobacion posterior." }
```

Debe existir entrega aunque b01 termine FALLO en cierre; b02 devuelve reutilizada
tras comparar. Conserva ambas copias. Continúa con el [lab](../../../labs/14_reproducible_projects/06_traceability_recovery/README.md).

## Bash y Python/uv, alternativa completa

Desde DS Track, con uv y Python 3.12.12. El protocolo de autoría se comprobó en
Windows; estos comandos no acreditan una ejecución en Linux/macOS.

```bash
python curriculum/14_reproducible_projects/06_traceability_recovery/preparar.py output/practica_1406 || exit 1
cd output/practica_1406 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python pruebas.py || exit 1
if uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a01 --simular-fallo; then
    echo 'Se esperaba el fallo didactico'; exit 1
fi
cat intentos/a01/eventos.csv intentos/a01/error.txt intentos/a01/consola.txt
test ! -e salidas/octubre || exit 1
ls -a salidas
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a02 || exit 1
cat salidas/octubre/seleccion.csv salidas/octubre/contexto.csv
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py a03 || exit 1
cat intentos/a03/eventos.csv
```

Confirma el RuntimeError didáctico, temporal conservado, a02 creada y a03
reutilizada, con 003/2600 y universo 3/4600. Para la segunda copia:

```bash
cd ../.. || exit 1
python curriculum/14_reproducible_projects/06_traceability_recovery/preparar.py output/cierre_1406 || exit 1
cd output/cierre_1406 || exit 1
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
if uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py b01 --simular-fallo-final; then
    echo 'Se esperaba el fallo de cierre'; exit 1
fi
test -d salidas/octubre || exit 1
cat intentos/b01/eventos.csv intentos/b01/error.txt
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py b02 || exit 1
```

b01 falla en cierre con entrega existente; b02 la comprueba y reutiliza. Lee
los diagnósticos: un código no cero por sí solo no identifica la causa esperada.
Continúa con el [lab](../../../labs/14_reproducible_projects/06_traceability_recovery/README.md).

# 14.02 — Preparar la copia y revisar una consulta

Vuelve a la [lección](README.md). Elige R base en el IDE o Python estándar en
terminal. Se copian trece archivos, sin entornos nuevos ni instalaciones.
Referencias comprobadas: Python 3.12.12 y R 4.6.1 en Windows.

## Recorrido principal: IDE y consola R

Desde la raíz de DS Track, en la consola R de tu IDE:

```r
source("curriculum/14_reproducible_projects/02_structure_configuration/preparar.R")
preparar_estructura("output/practica_1402")
```

Si el destino existe, consérvalo y elige otro. Una copia parcial se conserva
para revisar, sin reutilizarla como nueva. Los archivos de 14.01 se incluyen
automáticamente; no se exigen entregas personales anteriores.

Lee LEEME.md de la copia y abre config/consulta.csv como texto. Desde la misma
consola R, sin cambiar el directorio actual:

```r
source("output/practica_1402/revisar.R")
revisar_proyecto("output/practica_1402")
```

Resultado: octubre, 003/2600 MXN, universo 3/4600 y 100/3. La raíz es explícita.
Si abres la carpeta de la copia como proyecto en tu IDE, usa source("revisar.R")
y revisar_proyecto("."). No se necesita crear .Rproj ni activar renv para este
ejemplo de R base; la reconstrucción de entornos se tratará en 14.03.

Desde la raíz de la copia, crea la variante sin reemplazar la inicial:

```r
stopifnot(file.copy("config/consulta.csv", "config/septiembre.csv", overwrite = FALSE))
```

Edita corte a 2026-09-30 y salida a salidas/septiembre. Guarda y ejecuta:

```r
revisar_proyecto(".", "config/septiembre.csv")
```

Resultado: 002/2000 y 003/2500, saldo 4500 y 2/3. Reinicia R y ejecuta completo
para descartar objetos previos. Luego prueba desde otra carpeta cargando revisar.R
por una ruta absoluta y pasando la raíz absoluta. No cambies las rutas del CSV
para que dependan de esa otra carpeta. Ninguna revisión crea la salida prevista.

## Alternativa completa: PowerShell y Python

Desde la raíz del repositorio, usando tu Python habitual:

```powershell
python curriculum/14_reproducible_projects/02_structure_configuration/preparar.py output/practica_1402
if ($LASTEXITCODE -ne 0) { throw "Revisa la copia; no prepares encima." }
python output/practica_1402/revisar.py
if ($LASTEXITCODE -ne 0) { throw "Revisa el primer error." }
Set-Location output/practica_1402
if (Test-Path -LiteralPath config/septiembre.csv) { throw "Conserva la variante existente." }
Copy-Item -LiteralPath config/consulta.csv -Destination config/septiembre.csv -ErrorAction Stop
```

Edita la variante en tu editor, cambia corte/salida según el paso anterior y guarda:

```powershell
python revisar.py --config config/septiembre.csv
$raizPractica = (Get-Location).Path
Set-Location ..
python (Join-Path $raizPractica "revisar.py") --config config/septiembre.csv
```

La misma configuración debe producir los mismos valores desde ambos lugares.
Para mover la copia completa usa tu explorador en otra carpeta nueva; no copies
solo el punto de entrada, que requiere código/configuración/datos.

## Alternativa completa: Bash/Zsh y Python

Desde la raíz del repositorio:

```bash
python curriculum/14_reproducible_projects/02_structure_configuration/preparar.py output/practica_1402 || exit 1
python output/practica_1402/revisar.py || exit 1
cd output/practica_1402
test ! -e config/septiembre.csv || exit 1
cp config/consulta.csv config/septiembre.csv
```

Edita la variante en tu editor y guarda corte/salida. Después:

```bash
python revisar.py --config config/septiembre.csv
raiz_practica="$PWD"
cd ..
python "$raiz_practica/revisar.py" --config config/septiembre.csv
```

Usa python3 si corresponde a tu entorno. No instales paquetes para estos scripts.
Las instrucciones Bash y la operación completa del IDE no se acreditan por
haber comprobado Rscript/Python en Windows; regístralas por separado al practicar.

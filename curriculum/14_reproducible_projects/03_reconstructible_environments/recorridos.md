# 14.03 — Preparar, reconstruir y registrar

Vuelve a la [lección](README.md). Elige R/renv o Python/uv; no necesitas ambas
rutas. Los preparadores copian 26 fuentes, sin entornos instalados. Si un destino
existe, consérvalo y utiliza otro nombre en todos los pasos. Una carpeta parcial
se conserva para revisar; no se trata como destino nuevo.

## Recorrido principal: R e IDE

### Preparar y restaurar

Desde la raíz de DS Track, en consola R de tu IDE:

```r
source("curriculum/14_reproducible_projects/03_reconstructible_environments/preparar.R")
preparar_entornos("output/practica_1403")
```

Lee LEEME, entorno.csv, DESCRIPTION/renv.lock y el perfil antes de ejecutarlos.
Abre producto_1403.Rproj de la copia, reinicia R sin workspace y confirma getwd:

```r
getwd()
source("restaurar.R")
source("ejecutar.R")
ejecutar_reconstruible(".", "evidencia/r_1.csv")
```

Debe usar R 4.6.1 y renv 1.3.1 local. El cálculo no requiere otros paquetes
externos. Restaurar puede descargar renv; no cambia Conda/base ni bibliotecas
globales. Si en Windows el ejecutor restringido no lee enlaces del sandbox a
paquetes base, revisa permisos sin desactivar comprobaciones.

### Reconstruir solo desde fuentes recibidas

Desde la raíz de esta copia, crea otra carpeta nueva con estas 26 fuentes:

```r
fuentes <- c("LEEME.md", "revisar.py", "revisar.R", "config/consulta.csv",
  "codigo/modelo.py", "codigo/modelo.R", "codigo/configuracion.py", "codigo/configuracion.R",
  "salidas/LEEME.md", "docs/ESPECIFICACION.md", "docs/plantilla_contrato.md",
  "datos/entrada/cartera.csv", "referencia/criterios.csv", "ejecutar.py", "ejecutar.R", "entorno.csv",
  "pyproject.toml", "uv.lock", ".python-version", "DESCRIPTION", "renv.lock", "restaurar.R",
  ".Rprofile", "renv/activate.R", "renv/settings.json", "producto_1403.Rproj")
destino <- "../reconstruccion_1403"
if (file.exists(destino) || dir.exists(destino)) stop("Elige otra carpeta nueva.")
if (!dir.create(destino)) stop("No se pudo crear carpeta.")
for (archivo in fuentes) {
  final <- file.path(destino, archivo)
  if (!dir.exists(dirname(final))) dir.create(dirname(final), recursive = TRUE)
  if (!file.copy(archivo, final, overwrite = FALSE)) stop("Copia parcial: revisar.")
}
```

No se copian biblioteca, caché ni evidencia. Abre el proyecto de la nueva copia
y reinicia R antes de restaurar; no reutilices el proyecto activo de la primera:

```r
getwd()
source("restaurar.R")
source("ejecutar.R")
ejecutar_reconstruible(".", "evidencia/r_2.csv")
```

Compara parámetros y resultado con r_1.csv. Las rutas/fechas describen ejecuciones
distintas. Para septiembre, copia config/consulta.csv como config/septiembre.csv
sin sobrescribir, cambia corte/salida y ejecuta con tercer argumento
"config/septiembre.csv". La evidencia necesita otro nombre nuevo.

Para comprobar un proceso limpio desde la copia ya restaurada, terminal R opcional:

```text
Rscript --vanilla -e 'source(".Rprofile"); source("ejecutar.R"); ejecutar_reconstruible(".", "evidencia/r_3.csv")'
```

La restauración, la ejecución en Rscript y la operación completa de la interfaz
del IDE son comprobaciones distintas. No guardes el workspace como sustituto
del código/configuración.

## Alternativa completa: PowerShell y Python/uv

Desde la raíz del repositorio; uv y Python 3.12.12 deben estar disponibles:

```powershell
python curriculum/14_reproducible_projects/03_reconstructible_environments/preparar.py output/practica_1403
if ($LASTEXITCODE -ne 0) { throw "Revisa preparacion." }
Set-Location output/practica_1403
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisa Python y metadatos." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_1.csv
if ($LASTEXITCODE -ne 0) { throw "Revisa ejecucion." }
```

Si necesitas seleccionar un intérprete, añade a sync `--python` y su ruta real;
no uses otro entorno por accidente. Para reconstruir desde lo recibido, continúa
desde esta carpeta:

```powershell
$fuentes1403 = @("LEEME.md","revisar.py","revisar.R","config/consulta.csv",
 "codigo/modelo.py","codigo/modelo.R","codigo/configuracion.py","codigo/configuracion.R",
 "salidas/LEEME.md","docs/ESPECIFICACION.md","docs/plantilla_contrato.md",
 "datos/entrada/cartera.csv","referencia/criterios.csv","ejecutar.py","ejecutar.R","entorno.csv",
 "pyproject.toml","uv.lock",".python-version","DESCRIPTION","renv.lock","restaurar.R",
 ".Rprofile","renv/activate.R","renv/settings.json","producto_1403.Rproj")
$destino1403 = "../reconstruccion_1403"
if (Test-Path -LiteralPath $destino1403) { throw "Elige otra carpeta nueva." }
New-Item -ItemType Directory -Path $destino1403 -ErrorAction Stop | Out-Null
foreach ($archivo1403 in $fuentes1403) {
  $final1403 = Join-Path $destino1403 $archivo1403
  $padre1403 = Split-Path -Parent $final1403
  if (!(Test-Path -LiteralPath $padre1403)) { New-Item -ItemType Directory -Path $padre1403 -ErrorAction Stop | Out-Null }
  Copy-Item -LiteralPath $archivo1403 -Destination $final1403 -ErrorAction Stop
}
Set-Location $destino1403
uv sync --locked --no-python-downloads --cache-dir .uv-cache
if ($LASTEXITCODE -ne 0) { throw "Revisa reconstruccion." }
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_2.csv
```

No se copió .venv: se crea en la segunda ubicación. Compara ambos registros como
explica el lab. No uses `uv lock` para hacer pasar un --locked que rechazó cambios.

## Alternativa completa: Bash/Zsh y Python/uv

Desde la raíz del repositorio, con el Python de preparación elegido:

```bash
python curriculum/14_reproducible_projects/03_reconstructible_environments/preparar.py output/practica_1403 || exit 1
cd output/practica_1403
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_1.csv || exit 1
destino_1403="../reconstruccion_1403"
mkdir "$destino_1403" || exit 1
for archivo_1403 in LEEME.md revisar.py revisar.R config/consulta.csv codigo/modelo.py codigo/modelo.R codigo/configuracion.py codigo/configuracion.R salidas/LEEME.md docs/ESPECIFICACION.md docs/plantilla_contrato.md datos/entrada/cartera.csv referencia/criterios.csv ejecutar.py ejecutar.R entorno.csv pyproject.toml uv.lock .python-version DESCRIPTION renv.lock restaurar.R .Rprofile renv/activate.R renv/settings.json producto_1403.Rproj; do
  mkdir -p "$destino_1403/$(dirname "$archivo_1403")" || exit 1
  cp "$archivo_1403" "$destino_1403/$archivo_1403" || exit 1
done
cd "$destino_1403"
uv sync --locked --no-python-downloads --cache-dir .uv-cache || exit 1
uv run --locked --no-python-downloads --cache-dir .uv-cache python ejecutar.py evidencia/python_2.csv
```

Usa python3 si corresponde a tu entorno. Bash/Linux no se acredita con una prueba
de Windows; registra tu plataforma real. No instales paquetes o herramientas
adicionales solo por leer la planificación del módulo.

## Herramienta externa: Quarto

En terminal `quarto --version` comprueba la herramienta encontrada en PATH. Si
solo está incluida con tu IDE, puedes consultar su ruta conocida con comillas;
no supongas que eso la añadió al PATH del ejecutor. Su ausencia se registra,
sin instalar ni renderizar. Cuando se implemente el reporte será un requisito
del producto, no una dependencia Python o R intercambiable con el intérprete.

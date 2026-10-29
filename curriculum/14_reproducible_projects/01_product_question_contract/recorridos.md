# 14.01 — Copia de diseño y comprobación numérica

Vuelve a la [lección](README.md). La actividad esencial es redactar/revisar
Markdown y justificar casos. Los scripts son apoyo; elige Python estándar o
R base. No se instala ni restaura nada, ni se inicializa renv en la raíz.

## Recorrido principal: editor y consola R

Desde la raíz de DS Track, en la consola R de tu IDE:

```r
base <- "curriculum/14_reproducible_projects/01_product_question_contract"
destino <- "output/practica_1401"
archivos <- c("ESPECIFICACION.md", "plantilla_contrato.md", "cartera.csv", "criterios.csv", "referencia.py", "referencia.R")
if (file.exists(destino) || dir.exists(destino)) stop("Elige una carpeta nueva.")
if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear carpeta.")
stopifnot(all(file.copy(file.path(base, archivos), destino, overwrite = FALSE)))
```

Son seis archivos de trabajo; conserva la carpeta si una copia queda parcial.
Elige otro nombre al reintentar. Abre la plantilla de la copia, completa el
contrato y guarda con otro nombre para conservar el original. No necesitas
un proyecto .Rproj, gestor de tareas o entorno adicional para este diseño.

Después de predecir los casos, desde la misma consola R:

```r
source(file.path(destino, "referencia.R"))
comprobar_contrato(destino)
```

Puedes reiniciar R y repetir usando la ruta explícita de la carpeta. Si cambias
el directorio actual, ajusta esa ruta: comprobar_contrato no la adivina. Solo
lee e imprime nueve coincidencias o se detiene ante una diferencia; no certifica
la redacción, reconstrucción futura ni interacción del producto.

## Alternativa completa: PowerShell y Python

Desde la raíz, con el Python que ya utilizas:

```powershell
$baseContrato = "curriculum/14_reproducible_projects/01_product_question_contract"
$destinoContrato = "output/practica_1401"
if (Test-Path -LiteralPath $destinoContrato) { throw "Elige una carpeta nueva." }
New-Item -ItemType Directory -Path $destinoContrato -ErrorAction Stop | Out-Null
$archivosContrato = @("ESPECIFICACION.md", "plantilla_contrato.md", "cartera.csv", "criterios.csv", "referencia.py", "referencia.R")
foreach ($archivoContrato in $archivosContrato) {
    Copy-Item -LiteralPath (Join-Path $baseContrato $archivoContrato) -Destination $destinoContrato -ErrorAction Stop
}
python output/practica_1401/referencia.py
if ($LASTEXITCODE -ne 0) { throw "Revisa el primer desacuerdo." }
```

Abre los Markdown de la copia en tu editor. El script localiza los CSV junto
a sí mismo; no depende del directorio desde el que lo invoques. Repite después
de guardar una variante del lab en la copia. No modifiques el repositorio base.

## Alternativa completa: Bash/Zsh y Python

Desde la raíz:

```bash
base_contrato="curriculum/14_reproducible_projects/01_product_question_contract"
destino_contrato="output/practica_1401"
mkdir "$destino_contrato" || exit 1
for archivo_contrato in ESPECIFICACION.md plantilla_contrato.md cartera.csv criterios.csv referencia.py referencia.R; do
  cp "$base_contrato/$archivo_contrato" "$destino_contrato/" || exit 1
done
python output/practica_1401/referencia.py
```

Usa python3 si ese es el comando de tu entorno. Si output no existe, créalo
antes con `mkdir -p output`. Edita los Markdown en tu editor y repite la
comprobación cuando corresponda. La alternativa Bash no se acredita por ejecutar
los scripts con R/Python en Windows.

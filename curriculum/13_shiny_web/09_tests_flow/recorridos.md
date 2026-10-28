# 13.09 — Preparación, pruebas y arranque

Vuelve a la [lección](README.md). Elige el recorrido de IDE y consola R o una
alternativa de terminal. Referencia comprobada: R 4.6.1, Shiny 1.14.0,
ggplot2 4.0.3 y renv 1.3.1, con los mismos 42 registros del lockfile de 13.07.
No se añaden paquetes para probar. reactlog y automatización de navegador
no son requisitos del esencial.

## Recorrido principal: IDE y consola R

### 1. Preparar una copia nueva

Abre DS Track en RStudio o tu IDE. En la **consola R**, desde la raíz:

```r
getwd()
source("curriculum/13_shiny_web/09_tests_flow/preparar_app.R")
preparar_pruebas_flujo("output/practica_1309")
```

Si el destino existe, consérvalo y elige otro en todos los pasos. El preparador
solo copia veinte archivos: mínimo/tres pruebas/ejecutor propios; app/módulo
de 13.08; funciones de 13.04–13.07, CSV de 12.03 y metadatos de 13.07;
proyecto/iniciador/restaurador de 13.01 y configuración renv de 06.08.
No exige entregas previas. Una copia parcial debe revisarse, no reutilizarse
como si fuera un destino nuevo.

### 2. Abrir y restaurar

Abre `output/practica_1309/shiny_1309.Rproj` o su carpeta. Reinicia R sin
cargar workspace guardado y verifica que getwd apunta a la copia:

```r
getwd()
source("restaurar.R")
```

Revisa DESCRIPTION y renv.lock antes. La restauración puede descargar paquetes
y usa biblioteca local; no inicialices renv en la raíz ni modifiques Conda,
bibliotecas globales o lockfiles anteriores. La biblioteca queda en
`renv/library/...` y el estado en `.renv-local/`, sin caché compartida.
Si un ejecutor Windows restringido no lee los enlaces del sandbox a paquetes
base, revisa permisos antes de atribuirlo a renv; no desactives comprobaciones.

### 3. Predecir, observar y probar

En la consola R de la copia:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

Observa número/doble/nota y mensajes. Detén el servidor con Stop/Esc y confirma
que vuelve el prompt. Reinicia R y, desde la misma copia, ejecuta:

```r
source("ejecutar_pruebas.R")
```

Las pruebas no inician HTTP ni abren navegador. Se detienen al primer fallo;
un mensaje OK parcial no indica que terminó todo. Al final correcto aparece
`OK conjunto esencial. Falta complementar con la lista de navegador del lab.`
Los diagnósticos de fuente duplicada/ausente son esperados dentro de pruebas
con archivo temporal propio. La cartera original de la copia se conserva.

Abre los tres archivos de pruebas y ejecuta bloques para entenderlos. Si corres
uno por separado, carga antes el entorno y las funciones como hace el ejecutor;
para repetir de forma completa, reinicia R y ejecuta el archivo entero.
Realiza la regresión y frontera del lab solo en tu copia, restaura minimo.R y
repite completo. No cambies las expectativas para aceptar el fallo.

### 4. Complementar en navegador

Desde una sesión R nueva en la copia:

```r
source("iniciar.R")
iniciar_app("app.R", puerto = 8530)
```

Escucha en 127.0.0.1 y abre navegador en sesión interactiva. Si el puerto está
ocupado elige otro libre, sin cerrar procesos ajenos. La consola muestra la
URL real. Completa la lista del lab: dos paneles, aplicada/borrador, tabla,
CSV reales, cero/vacío/sin universo, rechazo, recarga y nueva sesión.
Descarga selección y contexto antes de aplicar otra consulta: son solicitudes
independientes. Los CSV no constituyen la entrega reconstruible del módulo.
Cerrar la pestaña no sustituye detener tu servidor con Stop/Esc.

## Alternativa completa: PowerShell

Desde la raíz del repositorio. Usa la ruta de tu instalación de R si difiere:

```powershell
$rscript = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rscript --vanilla -e 'source("curriculum/13_shiny_web/09_tests_flow/preparar_app.R"); preparar_pruebas_flujo("output/practica_1309")'
Set-Location output/practica_1309
& $rscript --vanilla -e 'source("restaurar.R")'
& $rscript --vanilla -e 'source("ejecutar_pruebas.R")'
if ($LASTEXITCODE -ne 0) { throw "Revisa el primer fallo antes de seguir." }
& $rscript --vanilla -e 'source("iniciar.R"); iniciar_app("minimo.R", puerto=8531, abrir=FALSE)'
```

Abre la URL indicada en navegador. Detén con Ctrl+C antes del siguiente comando:

```powershell
& $rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8530, abrir=FALSE)'
```

Detén con Ctrl+C al terminar. Edita la copia en el editor; cada nueva llamada a
Rscript crea una sesión nueva. Para la regresión repite el comando de pruebas.

## Alternativa completa: Bash/Zsh

Desde la raíz; Rscript debe corresponder al R elegido:

```bash
Rscript --vanilla -e 'source("curriculum/13_shiny_web/09_tests_flow/preparar_app.R"); preparar_pruebas_flujo("output/practica_1309")'
cd output/practica_1309
Rscript --vanilla -e 'source("restaurar.R")'
Rscript --vanilla -e 'source("ejecutar_pruebas.R")' || exit 1
Rscript --vanilla -e 'source("iniciar.R"); iniciar_app("minimo.R", puerto=8531, abrir=FALSE)'
```

Abre la URL real. Detén con Ctrl+C y después ejecuta:

```bash
Rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8530, abrir=FALSE)'
```

Detén con Ctrl+C. Si falta Rscript, vuelve al recorrido IDE. No instales otras
dependencias para interpretar las pruebas. La ejecución completa en la interfaz
del IDE debe revisarse por separado de la comprobación con Rscript.

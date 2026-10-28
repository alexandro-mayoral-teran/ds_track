# 13.10 — Preparar, entregar y reconstruir

Vuelve a la [lección](README.md). Elige IDE/consola R o una alternativa completa
de terminal. Las rutas de ejemplo parten de DS Track. Si un destino existe,
consérvalo y elige otro en **todos** los comandos que lo mencionan.

## Recorrido principal: IDE y consola R

### 1. Preparar práctica y restaurar

Abre DS Track en tu IDE. En la consola R desde la raíz:

```r
getwd()
source("curriculum/13_shiny_web/10_local_delivery/preparar_app.R")
preparar_cierre_shiny("output/practica_1310")
```

El preparador copia 24 fuentes: las veinte de 13.09, con proyecto renombrado
shiny_1310.Rproj, y entrega.R/LEEME/CONTRATO/casos. No instala ni arranca.
Abre el proyecto de la copia y reinicia R sin cargar workspace guardado:

```r
getwd() # Debe apuntar a output/practica_1310
source("restaurar.R")
source("ejecutar_pruebas.R")
```

Revisa DESCRIPTION/renv.lock antes. Son los mismos 42 registros de 13.07:
R 4.6.1, Shiny 1.14.0, ggplot2 4.0.3 y renv 1.3.1 como referencia comprobada.
La restauración puede descargar paquetes; instala en biblioteca local, sin
modificar Conda/globales ni inicializar renv en la raíz. El estado queda en
.renv-local y la biblioteca en renv/library, sin caché compartida. Ante permisos
Windows sobre enlaces del sandbox, revisa el ejecutor; no ocultes el problema
desactivando controles. Conserva cualquier diagnóstico de versiones no disponibles.

### 2. Crear y verificar la entrega

Desde la copia, con el servidor detenido:

```r
source("entrega.R")
crear_entrega("../entrega_1310")
verificar_entrega("../entrega_1310", referencia = "cartera.csv")
```

La entrega debe estar fuera de práctica, en un destino nuevo cuyo padre exista.
Contiene 41 archivos para la fuente base, sin paquetes instalados. INFORME.md
deja la revisión humana pendiente; no edites archivos generados para simular
que ya se hizo. Guarda notas/capturas fuera. Si hay copia parcial, consérvala
para revisar y usa otro destino después de corregir la causa.

### 3. Reconstruir solo las fuentes

En la consola R de la práctica, con entrega.R cargado:

```r
recibida <- normalizePath("../entrega_1310", winslash = "/", mustWork = TRUE)
destino <- "../reconstruccion_1310"
if (file.exists(destino) || dir.exists(destino)) stop("Elige otra carpeta nueva.")
if (!dir.create(destino)) stop("No se pudo crear reconstruccion.")
dir.create(file.path(destino, "renv"))
for (archivo in archivos_cierre()) {
  if (!file.copy(file.path(recibida, archivo), file.path(destino, archivo), overwrite = FALSE)) stop("Copia parcial: revisar.")
}
```

Este bloque copia 24 fuentes, incluidos .Rprofile y renv/activate.R/settings.json.
No copia resultados, cachés ni biblioteca. Abre shiny_1310.Rproj de la nueva
carpeta en el IDE y reinicia R. Desde esa reconstrucción:

```r
getwd()
source("restaurar.R")
source("ejecutar_pruebas.R")
source("entrega.R")
crear_entrega("../recalculada_1310")
verificar_entrega("../recalculada_1310", referencia = "../entrega_1310/cartera.csv")
```

La referencia recibida permanece fuera de recalculada. No necesitas abrir ni
leer el repositorio original. Compara tablas y figuras; la nota de generación
y las huellas pueden variar por entorno y no deben igualarse como certificado.

### 4. Demostrar la reconstrucción

Desde su consola R:

```r
source("iniciar.R")
iniciar_app("app.R", puerto = 8532)
```

La consola indica URL local y el proceso R queda ocupado. Completa la lista
del lab, con CSV reales en una carpeta de evidencia externa. Si el puerto está
ocupado elige otro, sin cerrar procesos ajenos. Stop/Esc detiene tu servidor;
cerrar la pestaña no lo hace. Reiniciar pierde las consultas aplicadas.

Verificación de solo lectura desde R base nuevo: carga entrega.R revisado con
source y llama verificar_entrega con rutas explícitas. No requiere restaurar
ni ejecutar .Rprofile; no demuestra por sí sola que la app funcione.
La operación completa de la interfaz del IDE se revisa por separado de Rscript.

## Alternativa completa: PowerShell

Desde la raíz; ajusta la ruta de tu R si difiere:

```powershell
$rscript = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rscript --vanilla -e 'source("curriculum/13_shiny_web/10_local_delivery/preparar_app.R"); preparar_cierre_shiny("output/practica_1310")'
if ($LASTEXITCODE -ne 0) { throw "Revisa preparacion." }
Set-Location output/practica_1310
& $rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R"); source("entrega.R"); crear_entrega("../entrega_1310"); verificar_entrega("../entrega_1310", "cartera.csv")'
if ($LASTEXITCODE -ne 0) { throw "Revisa el primer fallo." }
& $rscript --vanilla -e 'source("entrega.R"); destino <- "../reconstruccion_1310"; if (file.exists(destino) || dir.exists(destino)) stop("Destino ocupado"); if (!dir.create(destino)) stop("No se pudo crear"); dir.create(file.path(destino,"renv")); for (a in archivos_cierre()) if (!file.copy(file.path("../entrega_1310",a),file.path(destino,a),overwrite=FALSE)) stop("Copia parcial")'
if ($LASTEXITCODE -ne 0) { throw "Revisa copia." }
Set-Location ../reconstruccion_1310
& $rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R"); source("entrega.R"); crear_entrega("../recalculada_1310"); verificar_entrega("../recalculada_1310", "../entrega_1310/cartera.csv")'
if ($LASTEXITCODE -ne 0) { throw "Revisa reconstruccion." }
& $rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8532, abrir=FALSE)'
```

Abre la URL de consola y completa la demostración. Ctrl+C detiene el servidor.
Cada llamada a Rscript crea una sesión nueva; no dependas del workspace del IDE.

## Alternativa completa: Bash/Zsh

Desde la raíz; Rscript debe corresponder al R elegido:

```bash
Rscript --vanilla -e 'source("curriculum/13_shiny_web/10_local_delivery/preparar_app.R"); preparar_cierre_shiny("output/practica_1310")' || exit 1
cd output/practica_1310
Rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R"); source("entrega.R"); crear_entrega("../entrega_1310"); verificar_entrega("../entrega_1310", "cartera.csv")' || exit 1
Rscript --vanilla -e 'source("entrega.R"); destino <- "../reconstruccion_1310"; if (file.exists(destino) || dir.exists(destino)) stop("Destino ocupado"); if (!dir.create(destino)) stop("No se pudo crear"); dir.create(file.path(destino,"renv")); for (a in archivos_cierre()) if (!file.copy(file.path("../entrega_1310",a),file.path(destino,a),overwrite=FALSE)) stop("Copia parcial")' || exit 1
cd ../reconstruccion_1310
Rscript --vanilla -e 'source("restaurar.R"); source("ejecutar_pruebas.R"); source("entrega.R"); crear_entrega("../recalculada_1310"); verificar_entrega("../recalculada_1310", "../entrega_1310/cartera.csv")' || exit 1
Rscript --vanilla -e 'source("iniciar.R"); iniciar_app("app.R", puerto=8532, abrir=FALSE)'
```

Abre la URL y detén con Ctrl+C. Si Rscript no está disponible usa el IDE.
No instales otras dependencias para comprender el cierre. Bash/Linux no se
acredita por haber comprobado los mismos scripts con Rscript en Windows.

# 13.03 — Preparación y arranque

Vuelve a la [lección](README.md). Usa RStudio o tu IDE de R como recorrido
principal. Una alternativa de terminal basta si la prefieres. Referencia:
R 4.6.1, Shiny 1.14.0 y renv 1.3.1; se reutilizan los 31 registros del lockfile
de 13.01. Ninguna dependencia nueva ni cambio de entornos globales.

## Recorrido principal: IDE y consola R

### 1. Preparar una copia nueva

Abre DS Track en tu IDE. En su **consola R**, comprueba getwd y ejecuta desde
la raíz del repositorio:

```r
getwd()
source("curriculum/13_shiny_web/03_reactivity/preparar_app.R")
preparar_reactividad("output/practica_1303")
```

El destino no debe existir. Si existe, conserva su contenido y elige otro en
todos los pasos. Se copian doce archivos: app/minimo/comprobar nuevos, ventas.R
de 13.02, metadatos e iniciador/restaurador de 13.01 y configuración de proyecto
de 06.08. No hace falta tener entregas de esas secciones. Preparar no instala
ni arranca. Una copia parcial se conserva para revisar, no se usa como destino nuevo.

### 2. Abrir el proyecto y restaurar

Abre `output/practica_1303/shiny_1303.Rproj` o su carpeta en tu IDE. El nombre
del proyecto cambia, su contenido se conserva. Reinicia R sin recuperar una
sesión guardada, confirma que getwd apunta a esta copia y ejecuta:

```r
getwd()
source("restaurar.R")
```

Revisa DESCRIPTION/renv.lock antes. Restaurar puede descargar paquetes y los
instala en la biblioteca local; comprueba sincronización. No inicialices renv
en la raíz ni instales globalmente para resolver un import. Si ya tienes un
entorno adecuado no hace falta reinstalar para entender el concepto; la copia
nueva mostrada permite comprobarlo de forma independiente.

La configuración heredada usa `.renv-local/` y `renv/library/...`, sin caché
compartida. En Windows, si el ejecutor no puede leer los enlaces del sandbox
a paquetes base, revisa sus permisos; no desactives comprobaciones para ocultarlo.

### 3. Observar el mínimo

En la consola R de la copia:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

El proceso escucha en 127.0.0.1 y abre navegador en una sesión interactiva.
Observa la página y la consola: número/doble, nota independiente y rama
desactivada. Detén tu servidor con Stop/Esc; confirma que regresa el prompt `>`.
Cerrar una pestaña no equivale a detener el proceso R.

### 4. Observar ventas y repetir variantes

Desde la misma consola, inicia:

```r
iniciar_app("app.R")
```

Comprueba cinco consultas, la tabla, nota y casilla. No presupongas el orden de
los mensajes. Para editar una variante: detén, guarda el archivo, reinicia R,
carga iniciar.R y arranca el archivo elegido otra vez. No prepares encima ni
dependas de recarga automática. Después de la variante restaura el código inicial.

Si necesitas un puerto fijo usa `iniciar_app("app.R", puerto = 8518)`. Si está
ocupado elige otro libre, sin cerrar procesos ajenos. Usa la dirección impresa
por R. La recarga del navegador inicia otra sesión con los valores de UI;
no persiste elecciones. Revisa independencia entre dos pestañas según el lab.

## Terminal opcional: PowerShell

Recorrido completo desde la raíz de DS Track; adapta la ruta del Rscript elegido:

```powershell
$rEjecutable = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rEjecutable --vanilla -e "source('curriculum/13_shiny_web/03_reactivity/preparar_app.R'); preparar_reactividad('output/practica_1303')"
& $rEjecutable --vanilla -e "setwd('output/practica_1303'); source('restaurar.R')"
& $rEjecutable --vanilla -e "setwd('output/practica_1303'); source('iniciar.R'); iniciar_app('minimo.R', puerto=8518, abrir=FALSE)"
```

Abre `http://127.0.0.1:8518`. Ctrl+C detiene tu servidor. Después inicia ventas:

```powershell
& $rEjecutable --vanilla -e "setwd('output/practica_1303'); source('iniciar.R'); iniciar_app('app.R', puerto=8518, abrir=FALSE)"
```

Tras editar/guardar basta detener y repetir el arranque, no la preparación.

## Terminal opcional: Bash/Zsh

Recorrido completo desde la raíz; Rscript debe ser el de tu instalación elegida:

```bash
Rscript --version
Rscript --vanilla -e 'source("curriculum/13_shiny_web/03_reactivity/preparar_app.R"); preparar_reactividad("output/practica_1303")'
Rscript --vanilla -e 'setwd("output/practica_1303"); source("restaurar.R")'
Rscript --vanilla -e 'setwd("output/practica_1303"); source("iniciar.R"); iniciar_app("minimo.R", puerto=8518, abrir=FALSE)'
```

Abre `http://127.0.0.1:8518`. Ctrl+C detiene tu servidor. Después inicia ventas:

```bash
Rscript --vanilla -e 'setwd("output/practica_1303"); source("iniciar.R"); iniciar_app("app.R", puerto=8518, abrir=FALSE)'
```

Tras editar/guardar basta detener y repetir el arranque, no la preparación.

## Comprobación opcional de autoría

Con el servidor detenido, desde la consola R de la copia preparada:

```r
source("comprobar_app.R")
```

Comprueba celdas contra valores explícitos, reutilización por sesión, nota/casilla,
el mínimo y una sonda sin salidas para aislar invalidación/demanda. La sonda
usa isolate y contadores solo como instrumentación; no son requisitos de la
práctica ni una solución para la app. Las pruebas como tema corresponden a 13.09.
testServer fija entradas y no monta la UI: no comprueba etiquetas, valores de
inicio del navegador, teclado o suspensión real. Revisa esos casos en la página.

## Diagnóstico

| Síntoma | Qué revisar |
| --- | --- |
| Archivo ausente al arrancar | Abre la copia completa, con ventas.R junto a app.R |
| No encuentra Shiny | Proyecto, perfil, restauración y biblioteca local |
| Falta contexto reactivo | No llames consulta() directamente en la consola corriente |
| No aparece otra marca al cambiar nota | Es lo previsto; nota no alimenta consulta |
| Tabla oculta pero consulta se ejecuta al cambiar venta | Resumen aún solicita consulta |
| Se imprimen varias marcas al inicio | Espera la conexión; no equipares conexión con un único ciclo |
| Cambios de código no se ven | Detén, guarda, reinicia R y vuelve a arrancar |

[← Lección 13.03](README.md) · [Lab 13.03](../../../labs/13_shiny_web/03_reactivity/README.md)

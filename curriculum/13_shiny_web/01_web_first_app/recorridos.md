# 13.01 — Preparación y arranque de la primera app Shiny

Vuelve a la [lección](README.md). El recorrido principal usa RStudio o tu IDE
de R elegido. Las alternativas de terminal están separadas y son opcionales.
No necesitas realizar ambas ni tener entregas anteriores de Quarto/Streamlit.

Se comprobó con R 4.6.1, renv 1.3.1 y Shiny 1.14.0. R debe estar disponible
antes de empezar; no confundas el R del IDE con otro R que pueda aparecer
en PATH. El lockfile contiene 31 registros, incluido renv y las dependencias
de Shiny; la declaración directa del proyecto es shiny.

## Recorrido principal: consola R e IDE

### 1. Preparar desde la raíz del repositorio

Abre una consola R del IDE en la raíz de DS Track; `getwd()` permite comprobarla.
Estos son comandos R, no comandos PowerShell:

```r
R.version.string
getwd()
source("curriculum/13_shiny_web/01_web_first_app/preparar_app.R")
preparar_primera_app("output/practica_1301")
```

El destino debe ser nuevo. Si existe, conserva su contenido y elige otro en
todos tus pasos. `source` solo define la función; llamarla copia once fuentes
y no instala ni inicia servidores. Una copia parcial se conserva para revisar
el fallo; no la uses como destino nuevo.

### 2. Abrir la copia y restaurar

Abre `output/practica_1301/shiny_1301.Rproj` en RStudio. Otro IDE debe abrir esa
carpeta como directorio de trabajo. Reinicia la sesión R de ese proyecto,
comprueba la carpeta y ejecuta en **consola R**:

```r
getwd()
source("restaurar.R")
```

Revisa primero DESCRIPTION y renv.lock: ejecutar restaurar acepta descargar e
instalar las versiones registradas **en esta copia**. No instala en Conda/base,
la biblioteca del sistema ni el proyecto de análisis anterior. La primera
restauración puede requerir conexión y herramientas de instalación según la
plataforma; el lockfile no transporta los paquetes ya instalados.

El perfil local heredado de 06.08 dirige estado/sandbox a `.renv-local/`, usa
`renv/library/...` y desactiva la caché compartida. Las variables se aplican al
proceso R, no cambian la configuración global del sistema. No inicialices renv
en la raíz de DS Track.

Al terminar se imprimen versión R, bibliotecas, shiny y renv. Debe aparecer el
estado sincronizado. Si algo falla, conserva el diagnóstico; no desactives
controles ni instales paquetes globalmente para ocultarlo. En Windows un
ejecutor restringido puede impedir leer los enlaces del sandbox de paquetes
base: comprueba sus permisos antes de atribuir el fallo a renv.

### 3. Iniciar el mínimo

En la misma consola, desde la copia preparada:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

Abre la URL mostrada si el navegador no se abre. R queda ocupado mientras
atiende la app. Verás título/párrafo y no habrá filtros ni resultados de ventas.
Detén con Stop/Esc en la consola R; confirma que vuelve `>`.

El iniciador limita la escucha a `127.0.0.1`. Para elegir un puerto conocido:

```r
iniciar_app("minimo.R", puerto = 8513)
```

Si está ocupado, cambia solo a un puerto libre como 8514 y usa la URL nueva.
No cierres procesos ajenos. El puerto y la URL de una sesión no son alojamiento
permanente ni una publicación en Internet.

### 4. Iniciar la app de ventas y repetir

Después de detener el mínimo:

```r
iniciar_app("app.R")
```

Comprueba cuatro filas/660 MXN. Abre la misma URL en otra pestaña y observa los
mensajes de sesiones en la consola. Para la variante: detén, cambia 40 por 50
en el precio de V004, guarda, reinicia R, carga el iniciador y arranca de nuevo.
Debes obtener V004/150 y total 690; no prepares otra carpeta encima de esta.

También puedes abrir el archivo app.R de tu copia y usar **Run App** del IDE,
con el proyecto/renv ya activado. El iniciador permite explicitar la escucha local
y trabajar también con minimo.R. La comprobación de autoría no certifica haber
operado todos los botones/visores de todos los IDE.

Para retomar tras cerrar el IDE, abre otra vez el proyecto y carga iniciar.R;
no repitas restaurar si el entorno ya es adecuado. Si necesitas otra práctica,
prepara un destino distinto. El código y sus cambios quedan en disco; los
objetos de la sesión y el servidor activo no se guardan en app.R.

## Terminal opcional: PowerShell

Desde la raíz de DS Track. Usa el Rscript de tu instalación elegida; esta ruta
es la de R comprobada en Windows, sustitúyela si R está en otra ubicación:

```powershell
$rEjecutable = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rEjecutable --vanilla -e "source('curriculum/13_shiny_web/01_web_first_app/preparar_app.R'); preparar_primera_app('output/practica_1301')"
& $rEjecutable --vanilla -e "setwd('output/practica_1301'); source('restaurar.R')"
& $rEjecutable --vanilla -e "setwd('output/practica_1301'); source('iniciar.R'); iniciar_app('minimo.R', puerto=8513, abrir=FALSE)"
```

Abre `http://127.0.0.1:8513` y observa el mínimo. Ctrl+C detiene ese servidor.
Después arranca ventas desde un proceso nuevo:

```powershell
& $rEjecutable --vanilla -e "setwd('output/practica_1301'); source('iniciar.R'); iniciar_app('app.R', puerto=8513, abrir=FALSE)"
```

Para repetir tras cambiar app.R, detén tu servidor, guarda y repite solo este
último comando. No vuelvas a preparar/restaurar si la copia ya está lista.

## Terminal opcional: Bash/Zsh

Desde la raíz; Rscript debe pertenecer a tu instalación elegida. Verifica la
versión antes de preparar. No es un segundo entorno obligatorio:

```bash
Rscript --vanilla -e 'cat(R.version.string, "\n")'
Rscript --vanilla -e 'source("curriculum/13_shiny_web/01_web_first_app/preparar_app.R"); preparar_primera_app("output/practica_1301")'
Rscript --vanilla -e 'setwd("output/practica_1301"); source("restaurar.R")'
Rscript --vanilla -e 'setwd("output/practica_1301"); source("iniciar.R"); iniciar_app("minimo.R", puerto=8513, abrir=FALSE)'
```

Abre `http://127.0.0.1:8513` y observa el mínimo. Ctrl+C detiene ese servidor.
Después arranca ventas desde un proceso nuevo:

```bash
Rscript --vanilla -e 'setwd("output/practica_1301"); source("iniciar.R"); iniciar_app("app.R", puerto=8513, abrir=FALSE)'
```

Para repetir tras cambiar app.R, detén tu servidor, guarda y repite solo este
último comando. No vuelvas a preparar/restaurar si la copia ya está lista.

`--vanilla` omite perfiles automáticos. Restaurador e iniciador activan
explícitamente el perfil del proyecto preparado; no desactivan su aislamiento.
No uses el Rscript de Anaconda por comodidad si no corresponde al R elegido.

## Comprobaciones opcionales de autoría

Desde una sesión R nueva, en la raíz de la copia preparada:

```r
source("comprobar_app.R")
```

Comprueba objetos app, resumen y valores de las cuatro filas. Necesita el entorno
restaurado y usa testServer internamente; la explicación de pruebas reactivas
se reserva para 13.09. No abre un navegador ni demuestra legibilidad, conexión
real, detener/reiniciar o funcionamiento del IDE.

Este control espera la muestra original de 660. Con tu variante de 690 debe
fallar hasta que revises sus expectativas de forma justificada en una copia de
trabajo; no cambies esperados para ocultar errores. Para volver a la referencia,
conserva tu variante y prepara otra copia nueva.

## Diagnóstico breve

| Situación | Acción para retomar |
| --- | --- |
| No existe preparar_app.R | Comprueba raíz del repo y ruta, sin copiar comandos R en la terminal equivocada |
| No existe shiny o renv | Abre la copia y revisa restaurar; no instales globalmente |
| La consola no responde y muestra Listening | Atiende la app: detén tu servidor para recuperar la consola |
| El navegador no carga | Revisa URL/puerto, servidor activo y diagnóstico de R |
| La pestaña muestra un resultado tras detener R | Puede ser contenido conservado; recarga para comprobar la conexión |
| Cambiaste el archivo y sigues viendo 660 | Guarda, detén/reinicia y confirma que editaste/iniciaste la misma copia |

[← Lección 13.01](README.md) · [Lab 13.01](../../../labs/13_shiny_web/01_web_first_app/README.md)

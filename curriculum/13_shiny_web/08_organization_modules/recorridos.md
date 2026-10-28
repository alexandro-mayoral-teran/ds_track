# 13.08 — Preparación y arranque

Vuelve a la [lección](README.md). El recorrido principal es RStudio o tu IDE
de R; basta una alternativa de terminal si la prefieres. Referencia comprobada:
R 4.6.1, Shiny 1.14.0 y renv 1.3.1. DESCRIPTION/lockfile de 13.07 se copian byte por byte: ggplot2 4.0.3 y los
mismos 42 registros. No hay dependencias nuevas ni cambios globales.

## Recorrido principal: IDE y consola R

### 1. Preparar una carpeta nueva

Abre DS Track en el IDE. En la **consola R**, desde la raíz del repositorio:

```r
getwd()
source("curriculum/13_shiny_web/08_organization_modules/preparar_app.R")
preparar_organizacion_modulos("output/practica_1308")
```

Si el destino existe, consérvalo y elige otro en todos los pasos. Se copian
diecisiete archivos: app/minimo/consulta_module/comprobar de esta sección;
cartera.R de 13.04, consulta.R de 13.05, validacion.R de 13.06, presentacion.R y
DESCRIPTION/lockfile de 13.07, CSV de 12.03; proyecto/iniciador/restaurador de
13.01 y configuración de 06.08.
No exige entregas previas ni ejecutar Streamlit. Preparar no instala ni arranca;
si una copia queda parcial, consérvala para revisar y no la trates como nueva.

### 2. Abrir proyecto y restaurar

Abre `output/practica_1308/shiny_1308.Rproj` o su carpeta en el IDE. El proyecto
conserva el contenido del anterior con nombre distinto. Reinicia R sin cargar
un entorno guardado y verifica que getwd apunta a la copia:

```r
getwd()
source("restaurar.R")
utils::packageVersion("ggplot2")  # 4.0.3
```

Revisa DESCRIPTION y renv.lock antes. Restaurar puede descargar paquetes;
usa biblioteca local y comprueba sincronización. No cambia Conda/base,
metadatos Python ni bibliotecas globales. No inicialices renv en la raíz.
Con un entorno adecuado no hace falta reinstalar para comprender el tema;
el recorrido mostrado reconstruye una copia independiente.

El estado heredado está en `.renv-local/` y la biblioteca en `renv/library/...`,
sin caché compartida. Si en Windows un ejecutor restringido no puede leer
enlaces del sandbox a paquetes base, revisa sus permisos, sin desactivar controles.

### 3. Mínimo y app completa

Abre minimo.R y predice valores guardados de A/B y la lectura del padre. En la consola R de la copia:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

El iniciador escucha en 127.0.0.1 y abre el navegador en sesión interactiva.
Detén tu servidor con Stop/Esc, confirma que vuelve el prompt `>` y ejecuta:

```r
iniciar_app("app.R")
```

La app completa necesita cartera.R, consulta.R, validacion.R, presentacion.R, consulta_module.R y cartera.csv junto al archivo. Revisa
dos instancias A/B, API del padre, namespace dinámico y CSV por panel. Usa un puerto fijo
si lo necesitas: `iniciar_app("app.R", puerto = 8528)`. Si está ocupado elige
otro libre; no cierres procesos ajenos. La URL real aparece en la consola R.
Cerrar una pestaña no sustituye detener el servidor.

### 4. Variantes y sesión nueva

Para la variante del lab cambia el ID de A en las dos llamadas de app.R,
sin modificar el módulo. Guarda y repite desde una sesión nueva. Restaura el
ID original después de contrastar descargas y conexión.

Para comprobar el código completo desde una sesión nueva: detén el servidor,
guarda tus archivos, reinicia R, carga iniciar.R e inicia app.R. Debe volver
sin consulta aplicada. No prepares encima ni dependas de recarga automática.

Editar controles no relee el CSV; Aplicar filtros sí lo relee y valida entero.
La interfaz abre aunque falte el archivo. Descarga selección y contexto antes
de aplicar otra consulta; son dos solicitudes independientes. El CSV vacío
válido conserva encabezado. No hay descargas sin universo o con fuente bloqueada. Para probar fuentes usa explorador y
editor sobre la copia, conservando un respaldo íntegro, mientras R mantiene el
servidor. No ejecutes instrucciones en la consola ocupada. No hace falta reiniciar
para recuperar: restaura cartera.csv y vuelve a aplicar en cada instancia. No modifiques el original
del curso ni uses un CSV inválido como si fuera un filtro sin coincidencias.

Otra pestaña inicia una sesión con valores de UI y sin consulta aplicada.
Recargar también inicia otra sesión; los estados anteriores no se recuperan.
Editar controles no envía: pulsa Aplicar filtros. Enter en el campo de texto
no sustituye ese botón; con foco en el botón sí puede activarlo. Ocultar tabla
solo afecta presentación. Un borrador rechazado conserva la consulta anterior identificada; una fuente
fallida retira cifras al aplicar. Corregir requiere volver a aplicar.

## Terminal opcional: PowerShell

Recorrido completo desde la raíz; adapta la ruta a tu instalación elegida:

```powershell
$rEjecutable = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rEjecutable --vanilla -e "source('curriculum/13_shiny_web/08_organization_modules/preparar_app.R'); preparar_organizacion_modulos('output/practica_1308')"
& $rEjecutable --vanilla -e "setwd('output/practica_1308'); source('restaurar.R')"
& $rEjecutable --vanilla -e "setwd('output/practica_1308'); source('iniciar.R'); iniciar_app('minimo.R', puerto=8528, abrir=FALSE)"
```

Abre `http://127.0.0.1:8528`. Ctrl+C detiene tu servidor. Después inicia la app:

```powershell
& $rEjecutable --vanilla -e "setwd('output/practica_1308'); source('iniciar.R'); iniciar_app('app.R', puerto=8528, abrir=FALSE)"
```

Tras editar código R, guarda y detén/repite el arranque, sin preparar/restaurar otra vez.

## Terminal opcional: Bash/Zsh

Recorrido completo desde la raíz, con el Rscript de tu instalación elegida:

```bash
Rscript --version
Rscript --vanilla -e 'source("curriculum/13_shiny_web/08_organization_modules/preparar_app.R"); preparar_organizacion_modulos("output/practica_1308")'
Rscript --vanilla -e 'setwd("output/practica_1308"); source("restaurar.R")'
Rscript --vanilla -e 'setwd("output/practica_1308"); source("iniciar.R"); iniciar_app("minimo.R", puerto=8528, abrir=FALSE)'
```

Abre `http://127.0.0.1:8528`. Ctrl+C detiene tu servidor. Después inicia la app:

```bash
Rscript --vanilla -e 'setwd("output/practica_1308"); source("iniciar.R"); iniciar_app("app.R", puerto=8528, abrir=FALSE)'
```

Tras editar código R, guarda y detén/repite el arranque, sin preparar/restaurar otra vez.

## Apoyo opcional de autoría

Con servidor detenido, desde la consola R de la copia preparada:

```r
source("comprobar_app.R")
```

Comprueba siete consultas en A con B fijo, API reactiva del padre, mínimo
como módulo y dos instancias, UI estática/dinámica, rechazo, bloqueo y recuperación. testServer no
verifica una descarga real ni inspecciona píxeles de la gráfica; hacerlo en
navegador forma parte del lab. No modifica cartera.csv. testServer no monta
UI ni prueba sus valores iniciales, casillas, teclado o presentación real.
Es apoyo opcional, no la lección de pruebas 13.09 ni sustituto de tu explicación.

[← Lección 13.08](README.md) · [Lab 13.08](../../../labs/13_shiny_web/08_organization_modules/README.md)

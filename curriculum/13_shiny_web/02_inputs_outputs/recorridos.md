# 13.02 — Preparación y arranque

Vuelve a la [lección](README.md). El recorrido principal utiliza RStudio o el
IDE de R elegido. Las alternativas de terminal son opcionales; basta una.
Referencias comprobadas: R 4.6.1, Shiny 1.14.0 y renv 1.3.1, con los mismos
31 registros del lockfile de 13.01. No hay dependencias nuevas ni cambios de
metadatos anteriores.

## Recorrido principal: IDE y consola R

### 1. Preparar desde la raíz de DS Track

En la **consola R**, comprueba getwd y ejecuta:

```r
getwd()
source("curriculum/13_shiny_web/02_inputs_outputs/preparar_app.R")
preparar_entradas_salidas("output/practica_1302")
```

El destino debe ser nuevo. Si existe, conserva su contenido y usa otro en todos
los pasos. Se copian doce fuentes: cuatro archivos nuevos de 13.02 y proyecto/
metadatos/restauración/arranque/configuración reutilizados. La copia es independiente
de tus entregas anteriores; no sobrescribe la práctica de 13.01.

Preparar no instala ni inicia servidores. Si falla la copia, conserva esa
carpeta parcial y revisa el error; no la uses después como destino nuevo.

### 2. Abrir el proyecto y comprobar el entorno

Abre `output/practica_1302/shiny_1302.Rproj` en RStudio, o su carpeta con tu IDE.
El contenido del archivo de proyecto es el de 13.01 con nombre distinto en la
copia; el lockfile y DESCRIPTION se conservan byte por byte. Reinicia la sesión
R y comprueba que getwd apunta a la copia:

```r
getwd()
source("restaurar.R")
```

Revisa antes DESCRIPTION/renv.lock. Restaurar instala localmente lo que falte,
puede descargar paquetes y comprueba sincronización. No cambia Conda/base,
bibliotecas globales, metadatos Python ni otra copia de análisis. No inicialices
renv en la raíz del repositorio ni instales Shiny globalmente para resolver un import.

Si reutilizas un entorno de app adecuado, no necesitas reinstalar paquetes
para comprender esta sección; los scripts fuente y las dependencias siguen
separados. El recorrido mostrado prepara una copia nueva y restaura su biblioteca
local. No copies bibliotecas entre sistemas como sustituto del lockfile.

La configuración heredada dirige estado/sandbox a `.renv-local/` y biblioteca
a `renv/library/...`, sin caché compartida. Si un ejecutor restringido de Windows
impide leer los enlaces del sandbox a paquetes base, revisa permisos; no desactives
controles ni atribuyas automáticamente el fallo a renv.

### 3. Mínimo de texto y app completa

Desde la consola R de la copia:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

El iniciador de 13.01 se reutiliza sin cambios. Escucha en 127.0.0.1 y abre el
navegador en sesión interactiva. Prueba texto, vacío y caracteres HTML. Detén
tu servidor con Stop/Esc en la consola del IDE, confirma que vuelve `>` y ejecuta:

```r
iniciar_app("app.R")
```

Revisa las cinco opciones del selector y oculta/recupera el detalle. No hay botón
de aplicar: estos controles actualizan las salidas al cambiar. La app completa
necesita ventas.R junto a app.R; el mínimo es autónomo.

Si eliges un puerto fijo, usa `iniciar_app("app.R", puerto = 8516)`. Si está
ocupado, cambia a otro puerto libre como 8517; no cierres procesos ajenos.
Usa la URL real que imprime R. Cerrar una pestaña no sustituye detener el servidor.

### 4. Variantes y sesión nueva

Detén el servidor, edita app.R, guarda y reinicia R. Carga de nuevo iniciar.R
y arranca para observar etiqueta global cambiada y, después, selected V004.
No dependas de recarga automática de código ni prepares encima de la copia.

Recargar la pestaña crea otra sesión con el inicio definido en UI. No guarda tu
avance ni promete recuperar elecciones anteriores. Conserva código y notas
personales antes de cerrar. El [lab](../../../labs/13_shiny_web/02_inputs_outputs/README.md)
explica qué comprobar en las variantes.

## Terminal opcional: PowerShell

Desde la raíz del repositorio; usa el Rscript de tu instalación elegida.
La ruta siguiente es la referencia comprobada, cámbiala si R está en otra ubicación:

```powershell
$rEjecutable = "C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
& $rEjecutable --vanilla -e "source('curriculum/13_shiny_web/02_inputs_outputs/preparar_app.R'); preparar_entradas_salidas('output/practica_1302')"
& $rEjecutable --vanilla -e "setwd('output/practica_1302'); source('restaurar.R')"
& $rEjecutable --vanilla -e "setwd('output/practica_1302'); source('iniciar.R'); iniciar_app('minimo.R', puerto=8516, abrir=FALSE)"
```

Abre `http://127.0.0.1:8516`; Ctrl+C detiene tu servidor. Después inicia la app:

```powershell
& $rEjecutable --vanilla -e "setwd('output/practica_1302'); source('iniciar.R'); iniciar_app('app.R', puerto=8516, abrir=FALSE)"
```

Para repetir después de editar/guardar, detén y repite solo este último comando.
No vuelvas a preparar/restaurar si el entorno ya es adecuado.

## Terminal opcional: Bash/Zsh

Desde la raíz, con el Rscript de tu instalación elegida; verifica la versión:

```bash
Rscript --vanilla -e 'cat(R.version.string, "\n")'
Rscript --vanilla -e 'source("curriculum/13_shiny_web/02_inputs_outputs/preparar_app.R"); preparar_entradas_salidas("output/practica_1302")'
Rscript --vanilla -e 'setwd("output/practica_1302"); source("restaurar.R")'
Rscript --vanilla -e 'setwd("output/practica_1302"); source("iniciar.R"); iniciar_app("minimo.R", puerto=8516, abrir=FALSE)'
```

Abre `http://127.0.0.1:8516`; Ctrl+C detiene tu servidor. Después inicia la app:

```bash
Rscript --vanilla -e 'setwd("output/practica_1302"); source("iniciar.R"); iniciar_app("app.R", puerto=8516, abrir=FALSE)'
```

Para repetir después de editar/guardar, detén y repite solo este último comando.
No vuelvas a preparar/restaurar si el entorno ya es adecuado.

`--vanilla` omite perfiles automáticos. Los scripts reutilizados activan
explícitamente el perfil de la copia, sin desactivar el aislamiento. Las
instrucciones por terminal no acreditan haber operado los controles del IDE.

## Controles opcionales de autoría

Desde la consola de una sesión R nueva dentro de la copia:

```r
source("comprobar_app.R")
```

Comprueba funciones, cinco consultas, campos de tabla, ocultar/recuperar y eco
de texto. Usa testServer como apoyo opcional: no monta la UI, por lo que sus
entradas se fijan expresamente. Las opciones iniciales/etiquetas/teclado/HTML
real y sesiones se comprueban en navegador; no las acredita ese control.
Las pruebas reactivas como tema corresponden a 13.09, todavía planificado.

El control tiene expectativas de la muestra conocida. Cambiar datos o la regla
sin revisar esas expectativas debe producir un fallo. Las variantes del lab
cambian etiquetas o selected, no los datos. Guarda tus notas fuera de PROGRESS.md.

## Diagnóstico breve

| Situación | Qué revisar |
| --- | --- |
| Falta ventas.R | Ejecuta la copia preparada completa; source busca ese archivo en la carpeta de la app |
| Salida vacía tras cargar | ID de salida, pareja render y diagnóstico R; distingue inicio transitorio de una conexión incorrecta |
| Etiqueta cambia pero valor recibido no | Es correcto si solo cambiaste el nombre de choices |
| V003 parece no existir | Comprueba si ocultaste el detalle; su consulta debe mantener una fila/0 MXN |
| La tabla desaparece al desmarcar | Es el comportamiento previsto; el resumen conserva la consulta |
| Recarga vuelve a la opción inicial | Es una sesión nueva; aquí no hay persistencia de elecciones |

[← Lección 13.02](README.md) · [Lab 13.02](../../../labs/13_shiny_web/02_inputs_outputs/README.md)

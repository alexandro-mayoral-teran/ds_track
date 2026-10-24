# 11.02 — Primer documento Quarto

## Propósito, prerrequisitos y objetivos

Vas a crear un documento fuente `.qmd`, convertirlo a HTML y revisar qué archivos
se necesitan para leerlo y reconstruirlo. Después prepararás una comparación
con cifras calculadas, eligiendo Python o R. Un render satisfactorio debe dejar
un documento legible y coherente con su evidencia.

Lee [11.01 — Reporte, fuente y renderizado](../01_report_source_render/README.md)
como base conceptual. Esta sección trae su propia entrada y todos los resultados
esperados; no exige carpetas de práctica anteriores. Necesitas un editor de texto,
un navegador y Quarto. Para la comparación elige Python estándar o R base ya
preparados según [00.05](../../00_getting_started/05_environment/README.md).
No se añade ningún paquete a los entornos del curso.

Al terminar podrás reconocer YAML y Markdown, crear un `.qmd` sin extensión
oculta `.txt`, usar `render` y `preview`, distinguir un bloque mostrado de uno
ejecutable y comprobar una entrega HTML local.

## 1. Comprobar la herramienta antes de instalar

**Quarto CLI** es el programa que transforma documentos; una extensión del
editor ayuda a escribirlos y ejecutar comandos. La extensión no sustituye al
programa. Python y R son intérpretes distintos de Quarto.

En la terminal del sistema, prueba `quarto --version`. Si devuelve una versión,
anótala: no necesitas reinstalar para seguir. RStudio puede incluir Quarto
aunque su terminal no encuentre el comando. En Windows, si RStudio está en la
ruta habitual, puedes comprobar esa copia con PowerShell:

```powershell
& "C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe" --version
```

Si ninguna copia está disponible, consulta la [descarga oficial de Quarto](https://quarto.org/docs/download/)
y elige la distribución de tu sistema. Una distribución portable puede guardarse
en una carpeta de herramientas local; no la agregues al repositorio. Una
instalación de usuario también sirve. Cierra y abre la terminal después de un
instalador que cambie sus rutas, y comprueba de nuevo. No instales en Conda base
ni uses `pip install quarto` como sustituto del CLI.

**Autoría comprobada:** Quarto **1.9.38**, incluido en RStudio de este equipo,
y Pandoc **3.8.3** incluido en esa distribución. Son versiones utilizadas en
esta sección, no una afirmación de que sean las últimas disponibles. No se
instaló ni actualizó Quarto. Registrar la versión ayuda a interpretar diferencias
de formato entre equipos.

No necesitas LaTeX, TinyTeX, un servidor público ni una cuenta para producir
este HTML. `quarto check` realiza un diagnóstico más amplio y puede intentar
comprobar R/Jupyter; el primer documento de texto no los utiliza. Si falla un
motor que no elegiste, identifica esa fase antes de concluir que Quarto no funciona.

## 2. Crear un primer archivo pequeño

Abre un archivo nuevo en el editor, pega este contenido completo y guárdalo en
UTF-8 como `hola.qmd`, dentro de una carpeta nueva de práctica. También está
disponible en [hola.qmd](hola.qmd). En el explorador, muestra las extensiones
para comprobar que no quedó como `hola.qmd.txt`.

````markdown
---
title: "Mi primer reporte"
lang: es
format:
  html:
    embed-resources: true
---

## Pregunta

¿Qué archivos necesito para explicar un resultado?

## Respuesta inicial

Conservo **datos, código y documento fuente** para reconstruir el análisis.
El HTML permite leer el resultado generado.

## Próximo paso

Preparar una comparación con datos ficticios y comprobar sus cifras.
````

La primera región, delimitada por `---`, es el **encabezado YAML**: opciones del
documento. `title` establece el título, `lang: es` declara el idioma y `format`
elige HTML. Los espacios forman la jerarquía: `embed-resources` pertenece a
`html`, que pertenece a `format`. Usa espacios, no tabuladores; después de `:`
va un espacio antes del valor. Las comillas permiten escribir títulos como
`"Saldo: comparación entre cortes"` sin confundir sus dos puntos con otra clave.

El cuerpo utiliza **Markdown**: `##` inicia secciones y `**...**` marca énfasis.
No escribas otro título principal si ya lo define el YAML. La sintaxis oficial
se explica en [Markdown Basics](https://quarto.org/docs/authoring/markdown-basics.html).
El [tutorial Hello, Quarto](https://quarto.org/docs/get-started/hello/text-editor.html)
relaciona estas partes con el documento renderizado.

Para esta muestra, `embed-resources: true` incorpora los recursos de presentación
en el HTML. Sin esa opción, una salida habitual necesita también una carpeta
como `hola_files`. Se documenta en [HTML Basics, Self Contained](https://quarto.org/docs/output-formats/html-basics.html#self-contained).
La opción no incorpora automáticamente tu CSV, scripts y fuente como un paquete
de reconstrucción; tampoco convierte cualquier enlace externo en contenido sin red.

### Renderizar y leer

En la terminal sitúate en la carpeta que contiene tu `hola.qmd`. En los ejemplos
se asume que `quarto` está disponible; si necesitas la copia incluida en RStudio,
sustituye el valor de la variable por su ruta completa.

**PowerShell**, recorrido completo:

```powershell
$quarto1102 = "quarto"
& $quarto1102 --version
& $quarto1102 render hola.qmd --to html
```

**Bash/Zsh**, recorrido completo:

```bash
quarto1102="quarto"
"$quarto1102" --version
"$quarto1102" render hola.qmd --to html
```

Las variables contienen el ejecutable. PowerShell usa `&` para ejecutarlo;
Bash/Zsh usa el valor entre comillas. `render` recibe primero el archivo y
`--to html` elige la salida. No escribas estos comandos en la consola Python o R.
Debe aparecer `hola.html` junto al fuente. Ábrelo con tu navegador desde el
explorador y revisa título, acentos, tres secciones y énfasis. Renderizar de nuevo
puede reemplazar el HTML del mismo nombre; trabaja en copias y conserva versiones
en carpetas distintas cuando necesites comparar evidencia.

## 3. Mostrar código y ejecutarlo son cosas distintas

Un bloque que empieza con tres acentos graves seguidos de `python` muestra
código con formato. Si su primera línea utiliza `{python}`, Quarto lo trata como
ejecutable y necesita el motor correspondiente. Con R se distingue `r` de `{r}`.
La diferencia está descrita en [Using Python](https://quarto.org/docs/computations/python.html)
y [Using R](https://quarto.org/docs/computations/r.html).

Por ejemplo, esto puede añadirse al cuerpo de una copia de `hola.qmd`:

````markdown
```python
print(6000 + 300)
```
````

El HTML mostrará la instrucción; **no calcula ni imprime 6300** como salida.
Cambiarla a un bloque ejecutable requiere preparar Jupyter/Python o knitr/R.
Eso corresponde a [11.03](../README.md#03-ejecucion-con-python-o-r), todavía
planificada. No añadas llaves para intentar resolver un problema de estilo.

En el siguiente ejemplo calcularemos primero con un script y renderizaremos
después. Es una secuencia reproducible de dos comandos/acciones; Quarto no
ejecuta esos scripts por conocer el nombre de su archivo.

## 4. Ejemplo completo: preparar una comparación calculada

Una persona revisa el cambio de saldo de **los mismos tres créditos ficticios**
entre el 30 de septiembre y el 31 de octubre de 2026. Una fila representa un
crédito en un corte. Esta es toda la muestra de [cartera.csv](cartera.csv):

```csv
credito_id,fecha_corte,saldo_mxn
001,2026-09-30,1000
002,2026-09-30,2000
003,2026-09-30,3000
001,2026-10-31,1200
002,2026-10-31,1800
003,2026-10-31,3300
```

ID es texto con sus ceros; fecha admite exactamente esos dos cortes; saldo
representa MXN enteros entre 0 y 1000000, sin ausencias. ID/fecha es clave única,
y deben existir las seis combinaciones. El preparador rechaza todo el lote si
no cumple. No es un contrato general para una cartera de tamaño arbitrario.

| Crédito | Septiembre (MXN) | Octubre (MXN) | Diferencia (MXN) |
| --- | ---: | ---: | ---: |
| 001 | 1000 | 1200 | 200 |
| 002 | 2000 | 1800 | -200 |
| 003 | 3000 | 3300 | 300 |
| Total | 6000 | 6300 | 300 |

La tasa sobre septiembre es `300 / 6000 × 100 = 5%`. Hay tres créditos por
corte, no seis créditos distintos. El aumento del agregado no significa que
todos aumentaran; tampoco identifica causas, pagos ni desembolsos mensuales.

[preparar.py](preparar.py) y [preparar.R](preparar.R) reutilizan las reglas y
la narrativa calculada de [11.01](../01_report_source_render/README.md), usando
la entrada **propia de esta sección**. No necesitan ejecutar su lab ni leer
salidas previas. Añaden el encabezado de [inicio.qmd](inicio.qmd) al contenido,
omitiendo el título del borrador para que no se duplique. Ese archivo inicial
solo es la plantilla de opciones y presentación; el documento completo se
genera como `reporte.qmd`.

El resultado conserva copia de fuente, pares, resumen y borrador, y añade un
`.qmd` con título, subtítulo, idioma e índice (`toc: true`). Las cifras de su
tabla y narrativa se insertan desde los resultados calculados; no se escriben
de nuevo a mano. Una vez guardado, el `.qmd` contiene esas cifras como texto.
Renderizarlo solo no vuelve a leer el CSV: para actualizar datos hay que repetir
preparación y render en ese orden.

### Recorrido Python — PowerShell

Desde la raíz de DS Track, con tu entorno Python activado y destino nuevo:

```powershell
$quarto1102 = "quarto"
& $quarto1102 --version
python curriculum/11_reporting_quarto/02_first_document/preparar.py output/1102_python
& $quarto1102 render output/1102_python/reporte.qmd --to html
```

Si utilizas la copia comprobada de RStudio, cambia solo la primera asignación
a `$quarto1102 = "C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe"`.
No modifica el PATH ni la configuración global.

### Recorrido Python — Bash/Zsh

Desde la raíz, con tu entorno activado y destino nuevo:

```bash
quarto1102="quarto"
"$quarto1102" --version
python curriculum/11_reporting_quarto/02_first_document/preparar.py output/1102_python
"$quarto1102" render output/1102_python/reporte.qmd --to html
```

Usa un ejecutable disponible en tu sistema; no copies la ruta Windows a Linux/macOS.
La autoría comprobó Windows; estos recorridos de shell no certifican otros sistemas.

### Recorrido R — RStudio o tu IDE

Abre el proyecto de DS Track con su raíz como directorio de trabajo; comprueba
`getwd()` en la consola R. Guarda un script con este bloque, reinicia R y ejecútalo
completo. La función no necesita paquetes externos ni activar otro proyecto renv:

```r
source("curriculum/11_reporting_quarto/02_first_document/preparar.R", encoding = "UTF-8")
r <- preparar_documento(
  "curriculum/11_reporting_quarto/02_first_document/cartera.csv",
  "output/1102_r"
)
print(r$resumen)
stopifnot(identical(as.numeric(r$resumen$saldo_mxn), c(6000, 6300)),
          identical(r$porcentaje, "5.00%"))
```

Abre el nuevo `output/1102_r/reporte.qmd` en el editor de RStudio y utiliza
**Render**; el YAML selecciona HTML. No hace falta ejecutar una celda R: este
documento contiene texto preparado. Como alternativa reproducible, en la terminal
del sistema desde la raíz, usa uno de estos recorridos completos:

**PowerShell:**

```powershell
$quarto1102 = "quarto"
& $quarto1102 render output/1102_r/reporte.qmd --to html
```

**Bash/Zsh:**

```bash
quarto1102="quarto"
"$quarto1102" render output/1102_r/reporte.qmd --to html
```

Autoría ejecutó R 4.6.1 desde procesos nuevos con locale UTF-8 y Python 3.12.12,
y renderizó ambas preparaciones con Quarto 1.9.38. No se probó el botón del IDE.
La consola R y la terminal del sistema cumplen funciones distintas.

## 5. Preview, revisión y archivos que conservar

`render` produce la salida y termina. `preview` renderiza y mantiene un proceso
local que atiende la vista previa y los cambios del documento guardado. No es
publicación en internet. Con la preparación Python anterior, desde la raíz:

**PowerShell:**

```powershell
$quarto1102 = "quarto"
& $quarto1102 preview output/1102_python/reporte.qmd --no-browser --port 4200
```

**Bash/Zsh:**

```bash
quarto1102="quarto"
"$quarto1102" preview output/1102_python/reporte.qmd --no-browser --port 4200
```

Para R, usa el archivo de `output/1102_r`. Abre la dirección local que informe
la terminal; `--no-browser` evita abrir una ventana automáticamente. Si el puerto
está ocupado, elige otro. Cambia una frase en tu copia del `.qmd`, guarda y observa
la actualización. Termina con **Ctrl+C** en esa terminal. Cambiar el CSV no
regenera por sí solo este documento ni recalcula sus cifras.

Para revisar la entrega, abre `reporte.html` directamente, sin depender de preview:

- Título y subtítulo explican la muestra y los cortes; los acentos se leen bien.
- Índice y secciones permiten encontrar pregunta, hallazgo, método y límites.
- Tabla y párrafo coinciden: 6000/6300 MXN, +300, 5% sobre septiembre y tres créditos.
- La tabla cabe en la ventana; revisa también una ventana estrecha.
- Copia **solo el HTML** a otra carpeta y ábrelo: en esta muestra sin imágenes
  remotas ni vínculos necesarios para leer, los recursos de presentación van incluidos.

Este último punto comprueba lectura de la salida, no reconstrucción. Para repetir
los cálculos conserva los CSV, los scripts y el repositorio con sus funciones;
para repetir el render conserva también `.qmd` y la versión de Quarto. El HTML
no requiere Python/R para leerlo. `fuente.csv` se menciona como procedencia y
se entrega junto a la evidencia para auditar, no se descarga dentro del HTML.

Los preparadores rechazan destinos existentes y no sobrescriben tus prácticas.
Render sí puede actualizar el HTML de una carpeta. Si falla, revisa el error y
no confundas un HTML anterior que quedó en disco con una salida nueva válida.

## 6. Errores habituales

| Síntoma | Comprobación y corrección |
| --- | --- |
| No se reconoce `quarto` | Comprobar versión por ruta completa o revisar instalación/ruta en una terminal nueva |
| No encuentra el `.qmd` | Revisar directorio actual y nombre; mostrar extensiones para descartar `.qmd.txt` |
| Error de YAML | Revisar `---`, espacios, jerarquía y comillas alrededor de textos con dos puntos |
| Se ve código, pero no un resultado | El bloque sin llaves es de presentación; no se ejecuta |
| Solicita Jupyter o knitr | Se añadió un bloque ejecutable; revisar si corresponde a esta sección o al recorrido de 11.03 |
| Cambió el CSV, pero no las cifras | Repetir el preparador hacia un destino nuevo y después renderizar su `.qmd` |
| HTML separado pierde estilos | Revisar `embed-resources` o conservar la carpeta de recursos que realmente requiera esa salida |
| Preparación incompleta | Conservarla para diagnóstico; corregir y usar otro destino. No se promete escritura atómica |

## Práctica, criterio de salida y siguiente paso

Realiza el [lab 11.02](../../../labs/11_reporting_quarto/02_first_document/README.md).
Puedes crear y renderizar el documento, explicar sus dos fases y comprobar
lectura y cifras sin editar el HTML. Registra evidencia en
[PROGRESS.md](../../../PROGRESS.md).

`05_monthly_report` y sus checkpoints siguen previstos en
[proyectos](../../../projects/README.md); este lab no los implementa ni acredita
aprendizaje. El siguiente desarrollo es
[11.03 — Ejecución con Python o R](../README.md#03-ejecucion-con-python-o-r),
todavía planificado: cálculo dentro del `.qmd`, motor y entorno correctos.

## Referencias primarias

Consultadas el 2026-10-23; ejemplos propios, documentación web que puede avanzar
respecto de la versión comprobada. La lectura y los comandos mínimos de Quarto
se apoyan en [Hello, Quarto](https://quarto.org/docs/get-started/hello/text-editor.html);
la [descarga oficial](https://quarto.org/docs/download/) identifica las distribuciones.
Consulta [Markdown Basics](https://quarto.org/docs/authoring/markdown-basics.html),
[HTML Basics](https://quarto.org/docs/output-formats/html-basics.html),
[Using Python](https://quarto.org/docs/computations/python.html) y
[Using R](https://quarto.org/docs/computations/r.html) para sus comportamientos específicos.

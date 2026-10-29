# 00.02 — Terminal, rutas y verificación del entorno

<a id="02--terminal-rutas-y-verificación-del-entorno"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.02**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Ubicarte en el proyecto, interpretar rutas y comprobar herramientas |
| **Necesitas** | Copia de DS Track y PowerShell o Bash/Zsh; para un primer ensayo, notebook opcional en Colab |
| **Evidencia** | Nota con ubicación, rutas y comprobaciones del shell elegido |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Glosario](#glosario) · [Ir al lab](../../../labs/00_getting_started/02_terminal_paths/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Aprender a ubicarse dentro de un proyecto y comprobar qué herramientas están
disponibles. Usaremos PowerShell en Windows y mostraremos el equivalente en un
shell Unix, como Bash o Zsh. El objetivo no es memorizar dos listas de comandos,
sino reconocer las operaciones comunes.

## Antes de empezar

Retoma [00.01 — Markdown y perfil](../01_github_profile/README.md). Necesitas
una copia descargada o clonada de DS Track y acceso a una terminal. Elige
PowerShell o Bash/Zsh; no necesitas completar los dos recorridos.

Comienza identificando la carpeta raíz del proyecto. Las comprobaciones de
versiones permiten detectar herramientas disponibles o faltantes: registra
lo que falta para preparar el entorno en 00.05. El verificador requiere Python;
si aún no está disponible, conserva esa comprobación pendiente.

Si quieres probar sin instalar Python localmente, puedes empezar con el
[notebook para Colab](practica_terminal_colab.ipynb). Prepara su propia carpeta
de ejemplo y permite ensayar Bash. La copia real del proyecto y la comprobación
de tu entorno personal se retoman después; el notebook no las acredita.

<a id="objetivos"></a>

## Qué vas a aprender

- Identificar el directorio actual y distinguir rutas absolutas y relativas.
- Localizar archivos e inspeccionar un CSV con tu shell, reconociendo equivalencias con el otro recorrido.
- Distinguir shell de programa y consultar las versiones de las herramientas disponibles.
- Ejecutar el verificador, interpretar sus resultados y explicar qué ayuda a repetir y comprobar la terminal.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Tabla de equivalencias](shell-cheatsheet.md) | Consultar operaciones al cambiar de shell | Consulta opcional |
| [CSV de ventas](ventas_demo.csv) | Localizar e inspeccionar tres ventas ficticias | Entrada del recorrido |
| [Verificador](check_environment.py) | Consultar qué herramientas y rutas detecta el programa | Requiere Python |
| [Notebook de práctica para Colab](practica_terminal_colab.ipynb) | Ejecutar comandos Bash con explicaciones y una muestra autocontenida | Ensayo opcional en navegador, sin instalación local de Python |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

## Por qué aprender a trabajar en terminal

La terminal permite indicar acciones mediante comandos: abrir una carpeta,
localizar archivos, ejecutar un programa o comprobar qué versión está instalada.
Estos pasos pueden escribirse, compartirse y repetirse. Cuando alguien te entregue
un análisis, podrás seguir sus instrucciones y comprobar cómo se obtuvo el resultado.

No necesitas dejar de usar el explorador o un editor. La terminal los complementa:
el explorador ayuda a ver archivos, el editor a modificarlos y la terminal a
ejecutar acciones concretas sobre ellos.

### Cómo se conecta con el trabajo con datos

| Situación | Para qué sirve la terminal | Qué aprenderás en el recorrido |
| --- | --- | --- |
| Recibes archivos CSV | Localizar el archivo y revisar sus primeras líneas | Rutas y lectura de texto en esta lección |
| Un script no encuentra los datos | Comprobar desde dónde se interpreta la ruta | Directorio actual y rutas relativas |
| Un análisis funciona en otra computadora | Comparar versiones y ejecutables | Verificación de herramientas |
| Repites un reporte cada mes | Ejecutar el mismo programa con nuevas entradas | Scripts y reportes en lecciones posteriores |
| Procesas muchos archivos | Automatizar una secuencia de tareas | Programación y automatización más adelante |
| Trabajas en un servidor | Ejecutar procesos a través de una conexión de terminal | Uso remoto como tema posterior |

Un futuro script podría recibir un archivo y producir un resumen:

```text
python resumir_datos.py --entrada ventas.csv --salida resumen.csv
```

Este ejemplo muestra una posibilidad; el script todavía no existe y no debes
ejecutarlo. Primero aprenderás a ubicarte, leer rutas y reconocer un comando.

> **Para conversar:** si otra persona quisiera repetir tu análisis,
> ¿qué información necesitaría además del comando?

## Cómo seguir esta lección

### Opción en navegador: cargar el archivo `.ipynb`

Un **notebook** reúne explicaciones y celdas ejecutables. Para esta opción,
descarga [practica_terminal_colab.ipynb](practica_terminal_colab.ipynb) desde el
repositorio y súbelo en [Google Colab](https://colab.research.google.com/), mediante
la opción de subir un cuaderno del menú Archivo. Inicia sesión, conecta un entorno
alojado de Python con CPU y ejecuta las celdas de arriba abajo. No necesitas GPU,
instalar Python en tu equipo, clonar el repositorio ni cargar otros archivos.

La primera celda ejecutable prepara una carpeta temporal y las tres ventas del
CSV. Después, cada celda `%%bash` ejecuta comandos reales de Bash. El **kernel**
es el proceso que ejecuta las celdas; aquí Python/IPython permite enviarlas a Bash.
No necesitas estudiar el código de preparación ni configurar kernels todavía;
el trabajo con notebooks se desarrolla en 00.06.

Colab ejecuta en una máquina remota: las rutas y herramientas detectadas son
las de esa sesión, aunque tu computadora use Windows. No ejecuta PowerShell ni
comprueba tu instalación personal. Cada celda Bash inicia un proceso nuevo;
por eso el notebook vuelve a entrar en la carpeta de práctica en cada celda.
En una terminal interactiva el cambio de carpeta sí persiste entre comandos.

Predice, ejecuta y explica cada salida. Guarda tus respuestas en una copia del
cuaderno y descárgala: los archivos temporales pueden desaparecer al finalizar
la sesión. Reiniciar y ejecutar todo debe reconstruir la muestra. El funcionamiento
y los límites se describen en las [preguntas frecuentes de Colab](https://research.google.com/colaboratory/intl/es/faq.html).

### Recorrido con la terminal de tu equipo

Ejecuta los ejemplos del shell que uses, un comando a la vez. Comprueba el
resultado antes de continuar. Elige el [recorrido en PowerShell](#recorrido-en-powershell)
o el [recorrido en Bash/Zsh](#recorrido-en-bashzsh); no necesitas completar ambos.
Las rutas relativas parten de la raíz de
`ds_track`, salvo cuando se indica un cambio de carpeta.

## Antes de comenzar: cuatro conceptos diferentes

| Concepto | Ejemplo | Función |
| --- | --- | --- |
| Sistema operativo | Windows, Linux, macOS | Administra el equipo |
| Terminal | Windows Terminal, una consola SSH | Muestra y recibe texto |
| Shell | PowerShell, Bash, Zsh | Interpreta los comandos |
| Programa | Git, Python, `uv` | Realiza una tarea específica |

PowerShell y Bash no son sistemas operativos ni terminales: son shells. Una
terminal puede ejecutar distintos shells. En servidores y contenedores es común
encontrar Linux con Bash o un shell compatible.

Los comandos propios del shell pueden cambiar. Los comandos de programas
externos suelen conservarse:

```text
git status
python --version
uv run python archivo.py
```

Por eso `git status` es esencialmente igual desde PowerShell o Bash, mientras
que comprobar si un archivo existe utiliza sintaxis diferente.

### Cómo leer un comando

En `python --version`, `python` es el programa y `--version` es una opción que
pide mostrar su versión. En `Test-Path README.md`, `Test-Path` es el comando
de PowerShell y `README.md` es el argumento que indica qué ruta comprobar.

Las opciones pertenecen a cada herramienta: no todas aceptan las mismas.
El comando devuelve una salida o un error; leer ambos forma parte del trabajo.
Un bloque Markdown solo muestra el comando: debes ejecutarlo en la terminal.

## Recorrido en PowerShell

Sigue esta sección si usas PowerShell. Las líneas que empiezan con # son
comentarios: explican el paso y no se ejecutan como comandos.

### 1. El directorio actual

La terminal siempre está situada en una carpeta. Los comandos que usan rutas
relativas parten de esa ubicación.

```powershell
Get-Location
```

La ruta depende de dónde descargaste el proyecto. Por ejemplo:

```text
C:\aprendizaje\ds_track
```

No copies esta ruta como si existiera en tu computadora: comprueba la tuya.
La raíz del proyecto contiene `README.md`, `ROADMAP.md` y `pyproject.toml`.

### 2. Ver el contenido

```powershell
Get-ChildItem
```

Su alias corto es `ls`, pero durante esta primera lección usaremos el nombre
completo para hacer explícita la operación.

Para mostrar también elementos ocultos, como `.gitignore`:

```powershell
Get-ChildItem -Force
```

PowerShell trabaja principalmente con objetos; los shells Unix tradicionalmente
componen herramientas que intercambian texto. Esta diferencia será importante
cuando estudiemos pipes, pero no necesitamos profundizar todavía.

### 3. Rutas absolutas y relativas

Una ruta absoluta parte desde una unidad:

```text
C:\aprendizaje\ds_track\README.md
```

Una ruta relativa parte desde el directorio actual:

```text
README.md
curriculum\00_getting_started\README.md
```

Git y muchas herramientas aceptan `/` también en Windows. En código Python
preferiremos `pathlib` para construir rutas sin asumir un sistema operativo.

Si una ruta contiene espacios, escríbela entre comillas. Ejemplo ilustrativo:

```powershell
Test-Path "C:\Mis proyectos\ds_track\README.md"
```

Podemos preguntar si ambas existen:

```powershell
Test-Path README.md
Test-Path curriculum\00_getting_started\README.md
```

Ambas instrucciones deben devolver `True` cuando se ejecutan desde la raíz del
proyecto.

### 4. Cambiar de carpeta

```powershell
# Entra al módulo desde la raíz de ds_track
Set-Location curriculum\00_getting_started

# Confirma la nueva ubicación
Get-Location

# Lista los archivos de esta carpeta
Get-ChildItem

# Sube dos niveles para volver a la raíz
Set-Location ..\..

# Comprueba que regresaste a ds_track
Get-Location
```

PowerShell también reconoce `cd` como alias de `Set-Location`.

`..` significa "carpeta padre" y `.` significa "carpeta actual".

Antes de ejecutar un archivo, vuelve a comprobar tu ubicación con
`Get-Location`. Muchos errores de archivo no encontrado son, en realidad,
errores de ubicación.

### 5. Comprobar herramientas

Desde la raíz del proyecto:

```powershell
python --version
uv --version
git --version
```

Las versiones exactas pueden cambiar. Lo importante por ahora es que cada
comando responda sin error.

También puedes localizar el programa que PowerShell ejecutará:

```powershell
Get-Command python
Get-Command uv
Get-Command git
```

### 6. Ejecutar el verificador
> **Nota sobre el orden de aprendizaje:** todavía no hemos estudiado Python,
> `pip` ni `uv`. Los veremos en las lecciones de Primer script y Entorno y
> dependencias. Aquí solo mostramos cómo ejecutar un programa desde la terminal
> y leer su resultado; no necesitas comprender el código ni preparar un entorno
> nuevo. No se utiliza `pip`; la preparación con `uv` corresponde a 00.05.
> Si faltan herramientas, anótalo y deja esta verificación pendiente. Puedes
> continuar con la práctica de rutas y CSV y volver después de preparar el entorno.


```powershell
python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

Aquí utiliza Python solo si ya está disponible. La ejecución administrada por
`uv` se prepara en 00.05; no es necesario crear un entorno para este paso.

Todavía no necesitas entender el código del script. Lo revisaremos en la lección
de Primer script Python; antes sigue la lección 03 de Git e historial.

### 7. Primer contacto con un archivo de datos

Incluimos [ventas_demo.csv](ventas_demo.csv), una muestra ficticia de tres ventas.
Un CSV es un archivo de texto que representa una tabla; en este ejemplo las
columnas están separadas por comas y la primera línea contiene sus nombres.

Desde la raíz del proyecto, localízalo y lee las primeras tres líneas:

```powershell
# Busca archivos CSV en la carpeta de la lección
Get-ChildItem curriculum\00_getting_started\02_terminal_paths -Filter *.csv

# Confirma que existe el archivo de muestra
Test-Path curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv

# Lee el encabezado y los primeros dos registros
Get-Content curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv -TotalCount 3
```

`*.csv` busca nombres con esa extensión. `-TotalCount 3` muestra
solo tres líneas, útil para inspeccionar el comienzo sin imprimir todo el archivo.

Resultado esperado de la lectura:

```text
fecha,producto,unidades,importe_mxn
2026-01-01,cuaderno,2,80
2026-01-02,lapiz,5,50
```

Observa que tres líneas incluyen el encabezado y dos registros. Mostrar el texto
no valida tipos, fechas ni importes y, en otros CSV, un registro puede ocupar
varias líneas. La limpieza y el análisis se estudiarán con Python y pandas.

> **Para comprobar:** identifica los nombres de las columnas. Si cambias de
> carpeta, ¿por qué la misma ruta relativa podría dejar de funcionar?

### 8. Extensión: explorar el CSV desde la terminal

Esta sección es opcional. Muestra lo que puedes hacer al combinar comandos;
no necesitas memorizar su sintaxis para continuar a la lección 03.
Trabajaremos con el mismo archivo, sin modificarlo.

#### De texto a registros

Desde la raíz de `ds_track`, guarda la ruta en una variable para no repetirla:

```powershell
$ventasPath = "curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv"
```

Una variable conserva un valor que puedes usar en otros comandos. Aquí guarda
la ruta, no el contenido del archivo.

**Contar líneas de texto:**

```powershell
Get-Content $ventasPath | Measure-Object -Line
```

Verás `Lines: 4`: el encabezado y tres líneas de datos. El símbolo `|`, llamado
pipe, pasa la salida del comando de la izquierda al de la derecha.
`Measure-Object` mide lo que recibe.

**Leer registros del CSV:**

```powershell
# Interpreta el CSV y reúne sus registros en una colección
$ventas = @(Import-Csv $ventasPath)

# Muestra los registros importados
$ventas

# Cuenta los registros sin incluir el encabezado
$ventas.Count
```

`Import-Csv` interpreta el encabezado como nombres de columnas. Cada registro
se convierte en un objeto con propiedades como `producto` e `importe_mxn`.
`@(...)` reúne los resultados en una colección; su propiedad `Count` devuelve
`3`. El encabezado ya no cuenta como un registro.

**Filtrar por producto:**

```powershell
$ventas | Where-Object { $_.producto -eq "lapiz" }
```

`Where-Object` conserva los registros que cumplen la condición. Dentro de las
llaves, `$_` representa el registro que se está revisando y `-eq` significa
«igual a». El resultado es la venta de cinco lápices por 50 MXN.

**Filtrar por importe y elegir columnas:**

```powershell
$ventas |
    Where-Object { [decimal]$_.importe_mxn -ge 50 } |
    Select-Object producto, importe_mxn
```

`Import-Csv` devuelve los campos como texto. `[decimal]` convierte el importe
a número para compararlo; `-ge` significa «mayor o igual que».
`Select-Object` elige las columnas que quieres mostrar. Verás `cuaderno` y
`lapiz`, con importes de 80 y 50. La conversión supone importes válidos con el
formato sencillo de esta muestra.

**Contar las ventas filtradas y sumar importes:**

```powershell
# Filtra los importes y cuenta los registros que cumplen: 2
($ventas | Where-Object { [decimal]$_.importe_mxn -ge 50 } | Measure-Object).Count

# Convierte cada importe a número y suma todas las ventas: 165
($ventas | ForEach-Object { [decimal]$_.importe_mxn } | Measure-Object -Sum).Sum
```

Obtendrás `2` ventas con importe de al menos 50 MXN y `165` MXN de importe
total. `ForEach-Object` transforma cada registro en su importe numérico antes
de sumar. Aquí `importe_mxn` representa el total de cada venta, no el precio
por unidad; no debes multiplicarlo de nuevo por `unidades`.

#### Qué demuestra esta práctica

Puedes encadenar acciones pequeñas: leer → filtrar → seleccionar → resumir.
Ese mismo patrón aparecerá después en pandas y SQL. La terminal te permite
explorar rápidamente; elegir una herramienta adecuada y verificar el resultado
sigue siendo parte del análisis.

> **Reto opcional:** filtra las ventas con al menos dos unidades. ¿Cuántos
> registros quedan? Antes de ejecutar, predice la respuesta leyendo la muestra.

## Recorrido en Bash/Zsh

Sigue este apartado si usas Bash o Zsh. Parte de la raíz de ds_track y
ejecuta un comando a la vez. Las líneas con # explican cada paso.

### 1. Identificar tu ubicación

```bash
# Muestra el directorio actual
pwd
```

La raíz contiene `README.md`, `ROADMAP.md` y `pyproject.toml`. Su ruta absoluta
depende de dónde descargaste el proyecto, por ejemplo `/home/usuario/ds_track`.

### 2. Listar contenido

```bash
# Muestra archivos y carpetas visibles
ls

# Incluye archivos ocultos (-a) y detalles (-l)
ls -la
```

### 3. Comprobar rutas

Una ruta absoluta empieza en `/`; una relativa parte del directorio actual.
Pon entre comillas las rutas con espacios.

```bash
# Comprueba la existencia y muestra un mensaje si la ruta existe
test -e README.md && echo "existe"

# Comprueba un archivo dentro del módulo
test -e curriculum/00_getting_started/README.md && echo "existe"
```

`test -e` comprueba la existencia. `&&` ejecuta el comando siguiente solo si
esa comprobación tuvo éxito. Si la ruta no existe, estos ejemplos no imprimen
el mensaje; no devuelven `True` o `False` como `Test-Path` en PowerShell.

### 4. Cambiar de carpeta

```bash
# Entra al módulo desde la raíz
cd curriculum/00_getting_started

# Confirma la nueva ubicación
pwd

# Lista el contenido de esa carpeta
ls

# Sube dos niveles y vuelve a la raíz
cd ../..

# Comprueba que regresaste a ds_track
pwd
```

`.` representa la carpeta actual y `..` la carpeta padre.

### 5. Comprobar herramientas

```bash
# Muestra las versiones instaladas
python --version
uv --version
git --version

# Localiza el comando que el shell utilizará
command -v python
command -v uv
command -v git
```

Si tu sistema tiene Python como `python3`, usa `python3` en lugar de `python`
en los comandos directos. Anota cualquier herramienta faltante para preparar el entorno.

### 6. Ejecutar el verificador
> **Nota sobre el orden de aprendizaje:** todavía no hemos estudiado Python,
> `pip` ni `uv`. Los veremos en las lecciones de Primer script y Entorno y
> dependencias. Aquí solo mostramos cómo ejecutar un programa desde la terminal
> y leer su resultado; no necesitas comprender el código ni preparar un entorno
> nuevo. No se utiliza `pip`; la preparación con `uv` corresponde a 00.05.
> Si faltan herramientas, anótalo y deja esta verificación pendiente. Puedes
> continuar con la práctica de rutas y CSV y volver después de preparar el entorno.


```bash
# Ejecuta el script desde la raíz del proyecto
python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

Aquí utiliza Python solo si ya está disponible. La ejecución administrada por
`uv` se prepara en 00.05; no es necesario crear un entorno para este paso.

El verificador actual busca los comandos `python`, `uv` y `git`. Si solo existe
`python3`, puede informar que falta `python` aunque hayas podido ejecutar el script.

### 7. Inspeccionar el CSV

```bash
# Lista los archivos con extensión CSV dentro de la lección
ls curriculum/00_getting_started/02_terminal_paths/*.csv

# Comprueba que existe la muestra
test -e curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv && echo "existe"

# Muestra el encabezado y los primeros dos registros
head -n 3 curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv
```

El archivo tiene tres registros y un encabezado. Leer las líneas no valida los datos.

### 8. Extensión opcional: filtrar y resumir

En un shell Unix puedes combinar herramientas de texto. Desde la raíz:

```bash
ventas_path="curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv"
# Cuenta saltos de línea, incluido el encabezado: 4
wc -l < "$ventas_path"
# Busca la línea de la venta de lápices
grep ',lapiz,' "$ventas_path"
# Omite el encabezado y muestra producto e importe para ventas de al menos 50
awk -F',' 'NR > 1 && $4 >= 50 { print $2, $4 }' "$ventas_path"
# Suma los importes de los registros: 165
awk -F',' 'NR > 1 { total += $4 } END { print total }' "$ventas_path"
```

- `wc -l` cuenta los saltos de línea: `4` en el archivo incluido.
- `grep` encuentra la línea que contiene `,lapiz,`.
- `awk -F','` separa por comas; `NR > 1` omite el encabezado, `$2` es producto
  y `$4` es importe. Los últimos comandos muestran las dos ventas de al menos
  50 MXN y el total `165`.

Estos comandos de texto funcionan para esta muestra sencilla. `grep` busca
texto, no interpreta columnas, y separar por comas con `awk` no es un lector
general de CSV: campos entre comillas pueden contener comas o saltos de línea.
Para esos casos necesitas un lector de CSV, como los que estudiarás en Python.
Además, `wc -l` puede dar un resultado distinto si falta el salto de línea final.

> **Para profundizar más adelante:** se incorporará una sección de terminal
> avanzada para estudiar con más detalle filtros, pipes, redirecciones,
> herramientas como `grep` y `awk`, y automatización de tareas con datos.
> Estos ejemplos son una primera exploración; no necesitas dominar toda su
> sintaxis para continuar con el recorrido.

## Cuando un comando no funciona

| Mensaje o situación | Qué revisar primero |
| --- | --- |
| Archivo o ruta no encontrados | Tu ubicación, el nombre y los separadores |
| Comando no reconocido | La instalación de la herramienta y su ubicación |
| Una ruta con espacios falla | Si la escribiste entre comillas |
| El verificador informa herramientas faltantes | Qué herramienta falta; conserva la duda para preparar el entorno |

Vuelve a `Get-Location` o `pwd`, comprueba la ruta y lee el mensaje completo
antes de cambiar comandos al azar. Las herramientas pueden mostrar resultados
correctos aunque tu versión difiera de la del ejemplo.

<a id="aplicación"></a>

<a id="criterio-de-salida"></a>

## Práctica

Realiza el [lab 00.02](../../../labs/00_getting_started/02_terminal_paths/README.md) para practicar ubicación, rutas e inspección con tu shell.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu nota con directorio y rutas | Los archivos se localizan desde la carpeta indicada | Desde dónde se interpreta una ruta relativa |
| Salida del verificador o comprobaciones pendientes | Herramientas detectadas y faltantes, sin confundir ambos estados | Qué debes preparar y cómo distinguir shell, terminal y programa |
| Si usaste el notebook: copia con respuestas | Ubicación, rutas y CSV en la carpeta de ejemplo | Qué se ejecutó remotamente y qué falta comprobar en tu equipo |

Puedes cerrar esta práctica cuando localices los archivos del proyecto,
expliques rutas relativas y absolutas, reconozcas equivalencias entre shells y
ejecutes el mismo verificador sin cambiar su código. Si Python aún no está
disponible, registra esa comprobación pendiente y retómala al preparar el entorno.
Si practicaste en Colab, conserva el ensayo como evidencia de esos conceptos y
anota como pendiente la comprobación de la copia real y del entorno personal.

Quien aprende realiza la práctica y explica el resultado. Tu compañero propone otra carpeta y te pide explicar cómo cambiaría una ruta relativa.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

<a id="referencia-rápida"></a>

## Glosario

| Término | Qué significa en esta lección |
| --- | --- |
| Sistema operativo | Software que administra el equipo, como Windows, Linux o macOS |
| Terminal | Interfaz de texto donde escribes comandos y lees sus resultados |
| Shell | Programa que interpreta comandos; aquí PowerShell, Bash o Zsh |
| Comando | Instrucción que pides ejecutar al shell |
| Argumento | Dato que recibe un comando; por ejemplo, la ruta en `Test-Path README.md` |
| Opción | Indicación que modifica lo que hace una herramienta, como `--version` |
| Directorio | Carpeta que contiene archivos u otras carpetas |
| Directorio actual | Carpeta desde la que se interpretan las rutas relativas |
| Raíz del proyecto | Carpeta principal de DS Track; no es necesariamente la raíz de la unidad |
| Ruta absoluta | Ubicación completa de un archivo o carpeta desde una raíz, como `C:\aprendizaje\ds_track\README.md` en Windows |
| Ruta relativa | Ubicación que parte del directorio actual, como `datos/ventas_demo.csv` |
| Ejecutable | Programa que puede iniciarse; su ubicación permite saber qué instalación se usa |
| CSV | Archivo de texto que representa una tabla; en la muestra separa columnas con comas |
| Encabezado del CSV | Primera línea de la muestra, con los nombres de las columnas |
| Registro | Una fila de datos; cada venta es un registro en esta muestra |
| Variable | Nombre que conserva un valor, como una ruta, para reutilizarlo |
| Pipe (`\|`) | Conexión que pasa la salida de un comando al siguiente |
| Notebook (`.ipynb`) | Documento con explicaciones y celdas ejecutables |
| Kernel | Proceso que ejecuta las celdas de un notebook |
| Entorno remoto | Máquina accesible a través de un servicio; sus archivos y herramientas son distintos de los de tu equipo |

Para términos como repositorio, consulta el [glosario de 00.01](../01_github_profile/README.md#glosario).

## Referencias

Consulta la [tabla de equivalencias](shell-cheatsheet.md) para contrastar
PowerShell y Bash/Zsh; no necesitas memorizarla completa.

- [Colab: funcionamiento y límites](https://research.google.com/colaboratory/intl/es/faq.html).
- [IPython: ejecución de celdas Bash](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-bash).

## Siguiente paso

Después del lab y su comprobación, continúa con [00.03 — Git: historial y actualización del perfil](../03_git_workflow/README.md).

[← Módulo 00](../README.md) · [Lab 00.02](../../../labs/00_getting_started/02_terminal_paths/README.md) · [Siguiente →](../03_git_workflow/README.md)

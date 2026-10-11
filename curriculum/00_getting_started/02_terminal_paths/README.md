# 02 — Terminal, rutas y verificación del entorno

## Propósito

Aprender a ubicarse dentro de un proyecto y comprobar qué herramientas están
disponibles. Usaremos PowerShell en Windows y mostraremos el equivalente en un
shell Unix, como Bash o Zsh. El objetivo no es memorizar dos listas de comandos,
sino reconocer las operaciones comunes.

## Objetivos

Al terminar podrás:

- identificar el directorio actual;
- distinguir una ruta absoluta de una relativa;
- listar y localizar archivos sin depender del explorador gráfico;
- realizar esas operaciones en PowerShell y en un shell Unix;
- distinguir los comandos del shell de los comandos de programas como Git;
- comprobar las versiones de Python, `uv` y Git;
- ejecutar el verificador incluido en el proyecto.
- explicar cómo la terminal ayuda a repetir y verificar tareas con datos;
- localizar un CSV e inspeccionar sus primeras líneas.

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
> nuevo. `pip` no se utiliza en este paso y `uv` es una alternativa si ya lo tienes.
> Si faltan herramientas, anótalo y deja esta verificación pendiente. Puedes
> continuar con la práctica de rutas y CSV y volver después de preparar el entorno.


```powershell
python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

También puede ejecutarse mediante el proyecto de `uv`:

```powershell
uv run python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

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
> nuevo. `pip` no se utiliza en este paso y `uv` es una alternativa si ya lo tienes.
> Si faltan herramientas, anótalo y deja esta verificación pendiente. Puedes
> continuar con la práctica de rutas y CSV y volver después de preparar el entorno.


```bash
# Ejecuta el script desde la raíz del proyecto
python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

Si usas el entorno del proyecto con `uv`, esta es la alternativa:

```bash
# Ejecuta Python mediante el entorno administrado por uv
uv run python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

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

## Práctica

Continúa con el
[lab de terminal y rutas](../../../labs/00_getting_started/02_terminal_paths/README.md).

## Aplicación

Todavía no hay un proyecto asociado. Esta lección prepara el entorno desde el
que se ejecutarán todos los proyectos posteriores.

## Criterio de salida

Puedes explicar desde qué carpeta se interpreta una ruta relativa, localizar
los archivos principales del proyecto, reconocer las equivalencias básicas
entre PowerShell y Unix y ejecutar el mismo verificador sin cambiar su código.

## Referencia rápida

Después de completar el lab, continúa con
[03 — Git: historial y actualización del perfil](../03_git_workflow/README.md).

Consulta la [tabla de equivalencias](shell-cheatsheet.md) cuando necesites cambiar
de un shell a otro. No es necesario memorizarla completa.

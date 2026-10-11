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
resultado antes de continuar. Las rutas relativas parten de la raíz de
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

## 1. El directorio actual

La terminal siempre está situada en una carpeta. Los comandos que usan rutas
relativas parten de esa ubicación.

```powershell
Get-Location
```

En Bash o Zsh:

```bash
pwd
```

La ruta depende de dónde descargaste el proyecto. Por ejemplo:

```text
C:\aprendizaje\ds_track
```

No copies esta ruta como si existiera en tu computadora: comprueba la tuya.
La raíz del proyecto contiene `README.md`, `ROADMAP.md` y `pyproject.toml`.

## 2. Ver el contenido

```powershell
Get-ChildItem
```

Su alias corto es `ls`, pero durante esta primera lección usaremos el nombre
completo para hacer explícita la operación.

Para mostrar también elementos ocultos, como `.gitignore`:

```powershell
Get-ChildItem -Force
```

En Bash o Zsh se usa normalmente:

```bash
ls
ls -la
```

PowerShell trabaja principalmente con objetos; los shells Unix tradicionalmente
componen herramientas que intercambian texto. Esta diferencia será importante
cuando estudiemos pipes, pero no necesitamos profundizar todavía.

## 3. Rutas absolutas y relativas

Una ruta absoluta parte desde una unidad:

```text
C:\aprendizaje\ds_track\README.md
```

Una ruta relativa parte desde el directorio actual:

```text
README.md
curriculum\00_getting_started\README.md
```

En Unix se usa `/` como separador y una ruta absoluta comienza en `/`:

```text
/home/usuario/ds_track/README.md
curriculum/00_getting_started/README.md
```

Git y muchas herramientas aceptan `/` también en Windows. En código Python
preferiremos `pathlib` para construir rutas sin asumir un sistema operativo.

Si una ruta contiene espacios, escríbela entre comillas. Ejemplos ilustrativos:

```powershell
Test-Path "C:\Mis proyectos\ds_track\README.md"
```

```bash
test -e "/home/usuario/Mis proyectos/ds_track/README.md"
```

Podemos preguntar si ambas existen:

```powershell
Test-Path README.md
Test-Path curriculum\00_getting_started\README.md
```

Ambas instrucciones deben devolver `True` cuando se ejecutan desde la raíz del
proyecto.

En Bash o Zsh:

```bash
test -e README.md && echo "existe"
test -e curriculum/00_getting_started/README.md && echo "existe"
```

## 4. Cambiar de carpeta

```powershell
Set-Location curriculum\00_getting_started
Get-Location
Get-ChildItem
Set-Location ..\..
```

PowerShell también reconoce `cd`. En Bash o Zsh usaríamos:

```bash
cd curriculum/00_getting_started
pwd
ls
cd ../..
```

`..` significa "carpeta padre" y `.` significa "carpeta actual".

Antes de ejecutar un archivo, vuelve a comprobar tu ubicación con
`Get-Location`. Muchos errores de archivo no encontrado son, en realidad,
errores de ubicación.

## 5. Comprobar herramientas

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

En Bash o Zsh:

```bash
command -v python
command -v uv
command -v git
```

## 6. Ejecutar el verificador

```powershell
python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

En Bash o Zsh:

```bash
python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

También puede ejecutarse mediante el proyecto de `uv`:

```powershell
uv run python curriculum\00_getting_started\02_terminal_paths\check_environment.py
```

En Bash o Zsh cambia únicamente el separador de la ruta:

```bash
uv run python curriculum/00_getting_started/02_terminal_paths/check_environment.py
```

Todavía no necesitas entender el código del script. Lo revisaremos en la lección
de Primer script Python; antes sigue la lección 03 de Git e historial.

## 7. Primer contacto con un archivo de datos

Incluimos [ventas_demo.csv](ventas_demo.csv), una muestra ficticia de tres ventas.
Un CSV es un archivo de texto que representa una tabla; en este ejemplo las
columnas están separadas por comas y la primera línea contiene sus nombres.

Desde la raíz del proyecto, localízalo y lee las primeras tres líneas:

```powershell
Get-ChildItem curriculum\00_getting_started\02_terminal_paths -Filter *.csv
Test-Path curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv
Get-Content curriculum\00_getting_started\02_terminal_paths\ventas_demo.csv -TotalCount 3
```

En Bash o Zsh:

```bash
ls curriculum/00_getting_started/02_terminal_paths/*.csv
test -e curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv && echo "existe"
head -n 3 curriculum/00_getting_started/02_terminal_paths/ventas_demo.csv
```

`*.csv` busca nombres con esa extensión. `-TotalCount 3` y `head -n 3` muestran
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

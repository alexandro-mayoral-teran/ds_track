# 01 — Terminal, rutas y verificación del entorno

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

En este proyecto, el resultado esperado termina en:

```text
C:\bluepill5\Dev\ds_track
```

No memorices esta ruta: aprende a comprobarla.

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
C:\bluepill5\Dev\ds_track\README.md
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
python curriculum\00_getting_started\01_terminal_paths\check_environment.py
```

En Bash o Zsh:

```bash
python curriculum/00_getting_started/01_terminal_paths/check_environment.py
```

También puede ejecutarse mediante el proyecto de `uv`:

```powershell
uv run python curriculum\00_getting_started\01_terminal_paths\check_environment.py
```

En Bash o Zsh cambia únicamente el separador de la ruta:

```bash
uv run python curriculum/00_getting_started/01_terminal_paths/check_environment.py
```

Todavía no necesitas entender todos los detalles del script. En la siguiente
lección lo revisaremos como nuestro primer programa Python.

## Práctica

Continúa con el
[lab de terminal y rutas](../../../labs/00_getting_started/01_terminal_paths/README.md).

## Aplicación

Todavía no hay un proyecto asociado. Esta lección prepara el entorno desde el
que se ejecutarán todos los proyectos posteriores.

## Criterio de salida

Puedes explicar desde qué carpeta se interpreta una ruta relativa, localizar
los archivos principales del proyecto, reconocer las equivalencias básicas
entre PowerShell y Unix y ejecutar el mismo verificador sin cambiar su código.

## Referencia rápida

Consulta la [tabla de equivalencias](shell-cheatsheet.md) cuando necesites cambiar
de un shell a otro. No es necesario memorizarla completa.

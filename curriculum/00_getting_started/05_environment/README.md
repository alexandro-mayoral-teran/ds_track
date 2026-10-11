# 05 — Entornos y administración de dependencias

## Propósito y objetivos

Comprender qué Python ejecuta tu código, dónde están sus bibliotecas y cómo
reconstruir un entorno. Después de [04 — Primer script](../04_first_script/README.md),
estudia la teoría y completa **uno** de los tres recorridos prácticos.
La meta es identificar el intérprete, instalar y comprobar una biblioteca pequeña
y registrar los requisitos. Necesitas Internet para las descargas.

### Cómo leer esta lección

1. Lee las secciones 1–3 para comprender paquetes, gestores y aislamiento.
2. En la sección 4, consulta la creación y activación de tu camino y shell;
   los demás bloques son referencias, no ejercicios adicionales.
3. Compara las opciones en las secciones 5–6 y abre un solo recorrido.
4. Cuando tengas el entorno preparado, usa la sección 7 si trabajas en VS Code.
5. Realiza el lab con ese mismo entorno.

Puedes dividirlo en dos sesiones: conceptos y elección primero; preparación
y práctica después. No ejecutes todos los bloques del documento de una vez.

## 1. Intérprete, bibliotecas y dependencias

| Concepto | Qué significa | Ejemplo |
| --- | --- | --- |
| Intérprete | Programa que ejecuta Python | El ejecutable indicado por sys.executable |
| Biblioteca estándar | Funcionalidad incluida con Python | csv, pathlib, sys |
| Biblioteca externa | Funcionalidad instalada aparte | tabulate, pandas |
| Paquete distribuido | Software descargado e instalado por el gestor | tabulate |
| Dependencia directa | Software que tu proyecto solicita | tabulate para mostrar una tabla |
| Dependencia transitiva | Software requerido por otra dependencia | Una biblioteca instalada para satisfacer otra |
| Versión | Edición concreta de un paquete | tabulate==0.9.0 |

### Instalar y utilizar son dos pasos diferentes

1. **Instalar el paquete:** el gestor descarga sus archivos y los coloca en el
   entorno elegido. Por ejemplo, instalar `tabulate` deja esa biblioteca
   disponible para el Python de ese entorno.
2. **Importar en el programa:** el código indica qué funcionalidad quiere
   utilizar. En nuestro ejemplo, `from tabulate import tabulate` permite usar
   la función que presenta los datos como una tabla.

Instalar una biblioteca no la añade automáticamente a todos tus programas.
Importarla tampoco la descarga: si no está disponible para el intérprete que
ejecuta el código, Python informará que no encuentra el módulo.

### Dos nombres que conviene distinguir

- **Nombre de instalación:** identifica el paquete que solicitas al gestor.
- **Nombre de importación:** identifica el módulo que utilizas en el código.

En esta práctica ambos son `tabulate`. En otras bibliotecas pueden ser distintos;
consulta sus instrucciones de instalación y uso en lugar de asumir que coinciden.

### Qué papel tiene el editor

VS Code te permite escribir el programa. Abrir un archivo o instalar una extensión
del editor no instala automáticamente las bibliotecas que el programa necesita.
Esas bibliotecas deben estar disponibles en el entorno del Python que lo ejecuta.

## 2. Qué es pip y qué cambia con uv

### pip: instalar paquetes para un Python concreto

pip es el instalador habitual de paquetes Python. Busca el paquete en un índice,
como PyPI, obtiene una versión compatible e instala también las dependencias
que necesita. PyPI es el catálogo; pip es la herramienta que consulta e instala.

```text
# Consulta el pip asociado al Python elegido
python -m pip --version
```

La forma `python -m pip` indica explícitamente qué intérprete recibirá la
instalación. La salida muestra la versión de pip y dónde está instalado.
pip permite instalar, consultar, actualizar y retirar paquetes, pero no crea
el entorno ni descarga otra versión del intérprete por sí solo.

### uv: añadir la gestión del proyecto

uv es una herramienta independiente que puede gestionar Python, crear entornos
y resolver dependencias. En su flujo de proyectos mantiene los requisitos en
`pyproject.toml` y la resolución en `uv.lock`.

| Acción | venv + pip | uv, flujo de proyectos |
| --- | --- | --- |
| Preparar el entorno | Lo creas con venv | uv lo prepara para el proyecto |
| Agregar una biblioteca | pip la instala; tú registras el requisito | uv add la declara y prepara el entorno |
| Reconstruir | Creas el entorno e instalas un archivo de requisitos | uv sync utiliza configuración y lockfile |
| Ejecutar | Seleccionas el Python del entorno | uv run selecciona el entorno del proyecto |

uv también tiene comandos `uv pip` para flujos parecidos a pip. **No son el
programa pip**, ni cada comando equivale a la gestión completa de un proyecto.
En nuestro recorrido de uv utilizaremos `add`, `sync` y `run`; no necesitas
combinar las dos interfaces para aprender la base.

Conda cubre otra combinación de responsabilidades: administra entornos, Python
y paquetes de sus canales, incluidos componentes binarios. Lo compararemos
con las otras opciones después de comprender el aislamiento.

## 3. Cómo funciona un entorno y para qué sirve

Un análisis puede necesitar una versión de una biblioteca y otro una diferente.
Si comparten una instalación global, actualizar para uno puede afectar al otro.
Un entorno por proyecto separa sus paquetes y permite identificar el conjunto usado.

```text
Proyecto A → entorno A → intérprete y paquetes para A
Proyecto B → entorno B → intérprete y paquetes para B
```

### Cómo prepara el entorno cada herramienta

**Con venv:**

- Empiezas con una instalación de Python que ya existe en tu computadora.
- venv crea un entorno basado en ese Python, con su propio lugar para instalar
  paquetes. Ese directorio suele llamarse `site-packages`.
- Después utilizas pip para instalar las bibliotecas dentro de ese entorno.
- venv no descarga otra versión de Python: debes elegir una instalación disponible.

**Con Conda:**

- Puedes crear un entorno indicando qué versión de Python quieres utilizar.
- Conda instala y administra ese intérprete junto con los paquetes del entorno.
- También puede instalar componentes binarios: bibliotecas ya compiladas que
  algunos paquetes necesitan, además del código Python.

**Con uv:**

- Defines los requisitos del proyecto y uv prepara su entorno.
- Puede obtener una versión de Python si necesita una que no está disponible.
- Instala las dependencias y registra su resolución en un lockfile, para poder
  preparar ese conjunto de paquetes nuevamente.

Los tres caminos permiten separar los paquetes de un proyecto. La diferencia
es qué partes administra cada herramienta y qué necesitas preparar por separado.

### Ventajas y límites

- **Aislamiento:** instalar en un entorno no cambia los paquetes del otro.
- **Claridad:** puedes consultar qué Python y paquetes ejecutan la práctica.
- **Reconstrucción:** guardas requisitos y regeneras el entorno en otro equipo.
- **Límites:** ocupa espacio y requiere mantenimiento. No es una máquina virtual
  ni una barrera de seguridad; no protege tus archivos de un programa ejecutado.

El entorno por sí solo tampoco garantiza resultados idénticos: cuentan los datos,
la plataforma y las versiones documentadas. No crearemos un entorno por lección;
el elegido puede acompañarte en DS Track. La demostración de uv usa un proyecto
aparte para no modificar las dependencias del repositorio compartido.

## 4. Crear, activar y comprobar un entorno

Activar cambia la selección de comandos de **esa sesión del shell**, para que
python y otras herramientas resuelvan al entorno. No mueve tu código ni copia
paquetes entre instalaciones. Una terminal nueva puede requerir otra activación.

Puedes usar directamente el ejecutable de venv sin activarlo o ejecutar con
uv run. En Conda activar también prepara variables que pueden requerir sus bibliotecas.

```text
# Consulta el ejecutable que está usando Python
python -c "import sys; print(sys.executable)"
```

### Crear no es lo mismo que activar

Crear genera o prepara los archivos del entorno. Activar elige sus comandos
para la sesión actual. Creas una vez y vuelves a activar cuando lo necesitas.
Los siguientes bloques son referencias: ejecuta solo el camino que elegiste,
no todos los entornos. Evita recrear una carpeta o nombre que ya existe.

### Windows — PowerShell, venv

Desde la raíz de `ds_track`, con Python disponible:

```powershell
# Crea el entorno de práctica una sola vez
python -m venv .venv-practice
# Actívalo en esta terminal
.\.venv-practice\Scripts\Activate.ps1
# Comprueba qué ejecutable seleccionaste
python -c "import sys; print(sys.executable)"
# Sale del entorno cuando termines
deactivate
```

Si PowerShell bloquea Activate.ps1, no necesitas cambiar políticas: usa
`.\.venv-practice\Scripts\python.exe` directamente, como en el recorrido pip.

### Windows — CMD o Anaconda Prompt, venv

```bat
REM Crea y activa el entorno
python -m venv .venv-practice
.venv-practice\Scripts\activate.bat
REM Comprueba y después sal
python -c "import sys; print(sys.executable)"
deactivate
```

### Linux/macOS — Bash/Zsh, venv

```bash
# Crea con el Python instalado
python3 -m venv .venv-practice
# Carga la activación en el shell actual
source .venv-practice/bin/activate
# Después de activar, python pertenece al entorno
python -c "import sys; print(sys.executable)"
# Sale de la activación
deactivate
```

Windows guarda estos ejecutables y scripts en `Scripts`; Unix utiliza `bin`.
La activación también depende del shell: no copies Activate.ps1 en Bash ni
uses source en CMD. Estas rutas son para entornos creados en el sistema indicado.

### Conda — mismo comando, shell preparado

```text
# Crea una sola vez; revisa y confirma la instalación
conda create --name ds-track python=3.12 pip
# Activa en un shell donde Conda esté integrado
conda activate ds-track
python -c "import sys; print(sys.executable)"
# Vuelve al entorno anterior
conda deactivate
```

Funciona en PowerShell, CMD y Bash/Zsh cuando Conda está configurado para ese
shell. Si no lo está, usa primero el acceso de Anaconda que ya funciona y
consulta el [recorrido Conda](conda.md). No actives además un venv sobre él.

### uv — ejecución sin activación y activación opcional

Entra al mini proyecto que creaste siguiendo el [recorrido uv](uv.md):

```text
# Prepara el entorno desde los archivos de ese proyecto
uv sync --locked
# Ejecuta directamente en él, sin activación
uv run --locked python -c "import sys; print(sys.executable)"
```

Si quieres ejecutar `python` sin el prefijo `uv run`, puedes activar su `.venv`
ya preparado. Elige únicamente el bloque de tu shell:

**PowerShell en Windows:**

```powershell
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
deactivate
```

**CMD en Windows:**

```bat
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
deactivate
```

**Bash/Zsh en Linux/macOS:**

```bash
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
deactivate
```

Para el recorrido mantendremos `uv run`. Activar no instala paquetes nuevos
ni sincroniza la configuración: esas son acciones diferentes.

> **Para conversar:** ¿por qué «ya instalé la biblioteca» no basta para explicar
> que el programa pueda importarla?

## 5. Qué aporta cada camino

### Conda

**Ventajas:** encaja con Anaconda y permite gestionar Python y componentes
binarios desde una herramienta. **Limitaciones:** disponibilidad según canales
y plataformas, espacio de instalación y resolución de dependencias. Mezclar
pip requiere cuidado y registrar ambas fuentes.

### venv + pip

**Ventajas:** herramientas estándar, ampliamente documentadas y explícitas sobre
qué intérprete recibe cada instalación. **Limitaciones:** administras Python,
el entorno y los requisitos por separado; pip no gestiona bibliotecas del sistema.
pip freeze describe lo instalado, pero no es un lockfile multiplataforma.

### uv

**Ventajas:** registra requisitos en pyproject.toml y resolución en uv.lock,
automatiza el entorno y está diseñado para realizar esas tareas rápidamente.
**Limitaciones:** requiere aprender otra herramienta y sus convenciones; no
sustituye la gestión general de componentes binarios de Conda o del sistema.
Una sincronización exacta puede retirar paquetes que no declaraste.

| Pregunta | Conda | venv + pip | uv (proyectos) |
| --- | --- | --- | --- |
| ¿Crea entornos? | Sí | venv | Sí |
| ¿Gestiona Python? | Sí | Usa una instalación existente | Sí |
| ¿De dónde obtiene paquetes? | Canales Conda | Índices como PyPI | Índices como PyPI |
| ¿Qué compartes aquí? | environment.yml revisado | requirements.txt y versión de Python | pyproject.toml y uv.lock |
| ¿Activas en este recorrido? | Sí | No, usamos rutas directas | No, usamos uv run |

Estos archivos no son equivalentes: un YAML con requisitos o una lista de
paquetes no fija automáticamente toda la resolución para todas las plataformas.

## 6. Elegir tu recorrido

- **Ya usas Anaconda:** [Conda](conda.md).
- **Quieres las herramientas estándar:** [venv + pip](venv-pip.md).
- **Quieres configuración y lockfile integrados:** [uv](uv.md).

Cada documento separa shells, explica instalación y consulta de paquetes, e
incluye la misma práctica con tabulate 0.9.0. DS Track requiere Python 3.11 o posterior.
No completes los tres ni mezcles gestores en el mismo entorno. Evita instalar
los ejercicios en base o usar --user dentro de un entorno.

No copies carpetas de entornos entre computadoras: reconstruye desde sus archivos.
Antes de compartir configuración, revisa rutas personales y credenciales.

## 7. Gestionar la elección del entorno en VS Code

### Seleccionar el intérprete existente

1. Abre la carpeta `ds_track` e instala la extensión **Python**, publicada por
   Microsoft, si está permitida y todavía no la tienes.
2. Abre el script y la paleta con Ctrl+Shift+P en Windows.
3. Busca **Python: Select Interpreter** y elige el entorno de tu recorrido.
4. Si no aparece, utiliza la opción para indicar la ruta del intérprete.

| Recorrido | Qué Python seleccionar |
| --- | --- |
| Conda | El de ds-track; consulta su ubicación tras conda activate |
| venv + pip | .venv-practice/Scripts/python.exe en Windows o .venv-practice/bin/python en Unix |
| uv de esta práctica | .environment-practice/uv-demo/.venv/Scripts/python.exe en Windows o su equivalente bin/python en Unix |

No selecciones la `.venv` de la raíz para importar tabulate del mini proyecto:
son entornos distintos. Comprueba la ruta, no solo la etiqueta del menú.

### Crear y consultar desde el editor

La extensión ofrece **Python: Create Environment** para crear entornos; las
opciones dependen de las extensiones y herramientas detectadas. La extensión
**Python Environments**, también de Microsoft, puede ofrecer una vista para
descubrir, crear y consultar entornos y paquetes.

Para esta lección crea el entorno con los comandos de tu recorrido y selecciónalo
después. Evita crear otro automáticamente y terminar usando una instalación
distinta. En proyectos uv, conserva el flujo uv add/sync para gestionar dependencias,
aunque el editor permita acciones de instalación.

### Comprobar la terminal integrada

1. Tras seleccionar el intérprete, abre **Terminal → Nueva terminal**.
2. La extensión normalmente intenta activarlo en terminales nuevas, según su
   configuración y el shell. No supongas que ocurrió: compruébalo.
3. Ejecuta `python -c "import sys; print(sys.executable)"` y compara la ruta con
   el intérprete seleccionado. Si falta la activación, utiliza el bloque de tu shell.
4. Comprueba también `python -c "import tabulate; print(tabulate.__version__)"`
   cuando hayas instalado el paquete según el recorrido elegido.

Seleccionar el intérprete del editor no cambia automáticamente todas las
terminales abiertas. Si el botón de ejecución funciona pero tu comando no,
compara ambas rutas. En el flujo uv, `uv run` elige el proyecto según la ubicación;
seleccionar un intérprete en VS Code no cambia ese proyecto.

En la próxima lección elegiremos además el kernel de un notebook. Consulta la
[guía de VS Code](../../../docs/vscode-guide.md) para sus paneles y atajos.

## Práctica y criterio de salida

Lee el recorrido elegido y realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md).
La meta común es preparar un entorno, importar la biblioteca, ejecutar un ejemplo
y explicar cómo reconstruirlo. No hay proyecto de datos asociado todavía.

## Siguiente lección

06 — Primer notebook (por desarrollar). Consulta el [índice del nivel 0](../README.md).

## Referencias oficiales

- [Entornos de Python](https://docs.python.org/3/library/venv.html).
- [pip y entornos](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
- [Conda y uso de pip](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).
- [Proyectos con uv](https://docs.astral.sh/uv/guides/projects/).
- [Sincronización y lockfiles](https://docs.astral.sh/uv/concepts/projects/sync/).
- [Entornos Python en VS Code](https://code.visualstudio.com/docs/python/environments).
- [De pip a proyectos uv](https://docs.astral.sh/uv/guides/migration/pip-to-project/).

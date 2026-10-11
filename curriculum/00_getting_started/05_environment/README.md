# 05 — Entorno y dependencias

## Propósito y prerrequisitos

Comprender qué Python ejecuta tu código y dónde se instalan sus paquetes.
Prepararemos un entorno para continuar hacia la manipulación de datos.
Completa [04 — Primer script](../04_first_script/README.md) y utiliza las
instalaciones permitidas en tu equipo. Las descargas requieren Internet.

## 1. Distinguir las herramientas

| Pieza | Para qué sirve |
| --- | --- |
| Anaconda | Distribución que incluye Python, Conda y herramientas para datos |
| Conda | Crear entornos y administrar Python y paquetes |
| Intérprete Python | Ejecutar el código `.py` |
| Biblioteca estándar | Módulos incluidos en Python, como csv o sys |
| Paquete externo | Funcionalidad que instalas aparte, como pandas |
| Dependencia | Paquete que necesita un proyecto |
| pip | Instalar paquetes para un intérprete Python |
| uv | Gestionar Python y dependencias de proyectos, con archivos de configuración |
| venv | Módulo de Python para crear entornos virtuales |

Un entorno separa las versiones y paquetes de otros proyectos. No es una máquina
virtual ni una barrera de seguridad. Dos intérpretes pueden tener paquetes distintos.
El editor modifica el código, el shell interpreta comandos y Python ejecuta el programa.

## 2. Elegir un recorrido y reconocer tu terminal

**Si ya usas Anaconda, sigue Conda.** Si prefieres gestionar el proyecto desde
`pyproject.toml` y `uv.lock`, sigue uv. Basta con completar uno; venv queda como
referencia opcional. No necesitas instalar pandas ni preparar tres entornos.

| Ventana o perfil | Shell habitual | Ejemplo para consultar la ubicación |
| --- | --- | --- |
| Anaconda Prompt en Windows | CMD | `cd` sin argumentos |
| Anaconda PowerShell Prompt | PowerShell | `Get-Location` |
| Terminal con Bash/Zsh | Bash o Zsh | `pwd` |
| Terminal integrada de VS Code | El perfil que seleccionaste | Depende del shell |

Los comandos de Conda son los mismos, pero la navegación y activación de venv
pueden cambiar. Anaconda Prompt suele abrir con Conda listo; una terminal normal
necesita su integración configurada. Si no reconoce `conda`, empieza con el
acceso de Anaconda que funciona y consulta las instrucciones oficiales antes
 de configurar otro shell. No necesitas modificar todos tus perfiles para estudiar.

## 3. Recorrido principal — Anaconda y Conda

### Preparar Anaconda si falta

Si ya tienes Anaconda, no reinstales Python por separado para este recorrido.
Si falta, consulta la [instalación oficial](https://www.anaconda.com/docs/getting-started/anaconda/install).
Abre su terminal y comprueba `conda --version`.

### Qué significa base

`base` es el entorno inicial de Anaconda. Crearemos `ds-track` para los ejercicios
sin añadir sus dependencias a base. El entorno se guarda normalmente en el
área de entornos de Conda, no dentro del repositorio.

### PowerShell — Anaconda PowerShell Prompt

```powershell
# Consulta la herramienta y los entornos existentes
conda --version
conda env list
# Crea el entorno una sola vez; confirma la propuesta de instalación
conda create --name ds-track python=3.12 pip
# Activa el entorno para esta terminal
conda activate ds-track
# Comprueba la versión y el ejecutable elegido
python --version
python -c "import sys; print(sys.executable)"
# Consulta pip asociado a ese Python y los paquetes del entorno
python -m pip --version
conda list
# Sitúate en tu carpeta real del proyecto; sustituye el marcador
Set-Location "RUTA_REAL_DE_DS_TRACK"
Get-Location
# Ejecuta el primer script
python curriculum\00_getting_started\04_first_script\first_summary.py
```

### CMD — Anaconda Prompt

```bat
REM Consulta los entornos antes de crear uno nuevo
conda --version
conda env list
REM Crea una sola vez y activa
conda create --name ds-track python=3.12 pip
conda activate ds-track
REM Comprueba el intérprete y los paquetes
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
conda list
REM Sustituye la ruta; /d permite cambiar también de unidad
cd /d "RUTA_REAL_DE_DS_TRACK"
REM Muestra la ubicación y ejecuta el script
cd
python curriculum\00_getting_started\04_first_script\first_summary.py
```

### Bash/Zsh — Conda disponible en el shell

```bash
# Consulta entornos y crea solo si aún no existe ds-track
conda --version
conda env list
conda create --name ds-track python=3.12 pip
# Activa y comprueba qué Python utilizarás
conda activate ds-track
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
conda list
# Sustituye la ruta, confirma la ubicación y ejecuta
cd "RUTA_REAL_DE_DS_TRACK"
pwd
python curriculum/00_getting_started/04_first_script/first_summary.py
```

Elige solo el bloque de tu shell. Python 3.12 es la versión elegida para este
recorrido; cumple el requisito del proyecto de Python 3.11 o posterior.
La ruta de `sys.executable` debe pertenecer a `ds-track` y su nombre suele
aparecer en el prompt. El cálculo coincide con los valores que guardaste en el script.
Si `ds-track` ya existe, comprueba su contenido y actívalo; no repitas create
ni sobrescribas un entorno existente sin revisarlo.

### Retomar otra sesión

Ejecuta `conda activate ds-track`, entra en el proyecto y comprueba el intérprete.
Para salir usa `conda deactivate`. No vuelvas a crear el entorno cada día.

### pip dentro de Conda

`python -m pip` elige el pip de ese Python. En Conda instala primero lo disponible
con Conda y utiliza pip para lo que necesites y no obtengas por esa vía.
No uses `--user` dentro del entorno ni agregues paquetes de los ejercicios a base.
Si después necesitas reorganizar dependencias mezcladas, es preferible reconstruir
el entorno desde su especificación. En esta práctica solo consultamos pip: no
hay paquetes externos necesarios para el script.

### Compartir la configuración

Desde la raíz del proyecto, con `ds-track` activado:

```text
# Exporta requisitos elegidos explícitamente, no toda la instalación
conda env export --from-history > environment.yml
```

Revisa el archivo antes de compartirlo: elimina un campo `prefix` con una ruta
personal si aparece. No sobrescribas un environment.yml existente sin revisarlo.
Este export conserva elecciones hechas con Conda; no registra paquetes instalados
con pip ni fija todas las dependencias transitivas. No equivale a un lockfile.
Otra persona puede reconstruirlo con `conda env create -f environment.yml`
si el nombre no existe. Los paquetes de pip requerirán su declaración aparte.

## 4. Alternativa — uv para el proyecto

Sigue esta parte si eliges uv; no es un paso obligatorio después de Conda.
Consulta su [instalación oficial](https://docs.astral.sh/uv/getting-started/installation/)
y comprueba `uv --version`. Antes de empezar sal de entornos Conda activados
con `conda deactivate` hasta que no quede uno activo; para venv usa `deactivate`.

### PowerShell

Desde la raíz de DS Track:

```powershell
# Prepara .venv respetando el lockfile
uv sync --locked
# Comprueba el Python del proyecto
uv run --locked python -c "import sys; print(sys.executable)"
# Ejecuta el script sin activar .venv
uv run --locked python curriculum\00_getting_started\04_first_script\first_summary.py
```

### Bash/Zsh

```bash
# Desde la raíz, prepara el entorno y consulta su intérprete
uv sync --locked
uv run --locked python -c "import sys; print(sys.executable)"
# Ejecuta el script
uv run --locked python curriculum/00_getting_started/04_first_script/first_summary.py
```

En CMD puedes usar los mismos comandos de uv y la ruta con barras `/`.
El ejecutable debe pertenecer a `.venv`. `--locked` evita actualizar el lockfile
si no corresponde a la configuración: en ese caso falla para que revises el cambio.
No instales manualmente con pip o Conda dentro de `.venv`; sync puede retirar
paquetes que el proyecto no declara. Más adelante usaremos `uv add` cuando
una lección necesite una dependencia.

## 5. Referencia opcional — venv y pip

<details>
<summary>Ver cómo crear un entorno directamente con Python</summary>

Este recorrido explica el mecanismo estándar; no es necesario completarlo si
ya elegiste Conda o uv. Sal de cualquier entorno activo antes de practicar.
`.venv-practice` está separado de `.venv` y está excluido de Git.

### PowerShell

```powershell
# Crea solo si todavía no existe
python -m venv .venv-practice
# Usa directamente el ejecutable sin activar
.\.venv-practice\Scripts\python.exe -m pip --version
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\04_first_script\first_summary.py
```

La activación opcional usa `.\.venv-practice\Scripts\Activate.ps1`; si está
bloqueada, utiliza la ruta directa sin cambiar políticas. Para salir, `deactivate`.

### Bash/Zsh

```bash
python3 -m venv .venv-practice
./.venv-practice/bin/python -m pip --version
./.venv-practice/bin/python curriculum/00_getting_started/04_first_script/first_summary.py
```

Puedes activar con `source .venv-practice/bin/activate` y salir con `deactivate`.
En CMD la activación es `.venv-practice\Scripts\activate.bat`.
En algunas distribuciones Linux necesitas instalar el componente venv de Python.

</details>

## 6. Qué compartir y qué seleccionar en VS Code

| Recorrido | Entorno local | Archivos para describirlo |
| --- | --- | --- |
| Conda | `ds-track`, normalmente fuera del repositorio | environment.yml revisado |
| uv | `.venv` | pyproject.toml y uv.lock |

El repositorio ya incluye los archivos de uv; no describen automáticamente las
instalaciones hechas con Conda. Cuando introduzcamos paquetes, mantendremos las
instrucciones de cada recorrido acordes a sus requisitos. No copies carpetas de
entornos a otra computadora: reconstruye desde la configuración.

En VS Code, con la extensión Python de Microsoft, usa **Python: Select Interpreter**
y selecciona el Python de tu recorrido: `ds-track` para Conda o `.venv` para uv.
La selección del editor y la activación de la terminal son distintas; comprueba
`sys.executable` cuando obtengas resultados diferentes.

## Cuando algo no funciona

| Situación | Qué revisar |
| --- | --- |
| conda no se reconoce en una terminal normal | Prueba el acceso de Anaconda e integración del shell |
| El prompt indica base | Activa ds-track y comprueba sys.executable |
| Falta un módulo | El intérprete elegido y dónde se instaló el paquete |
| El entorno busca un Python eliminado | Reconstruir el entorno con una instalación compatible |
| uv rechaza el lockfile | Si cambió pyproject.toml; revisar antes de actualizar |
| La descarga falla | Conexión, permisos y mensaje del instalador |

## Práctica y criterio de salida

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md).
Puedes avanzar cuando prepares **un** entorno, identifiques su Python y ejecutes
el script, explicando dónde se instalarían sus paquetes. No hay proyecto asociado todavía.

## Siguiente lección

06 — Primer notebook (por desarrollar). Consulta el [índice del nivel 0](../README.md).

## Referencias oficiales

- [Entornos con Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).
- [Paquetes con Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-pkgs.html).
- [Proyectos con uv](https://docs.astral.sh/uv/guides/projects/).
- [Entornos virtuales de Python](https://docs.python.org/3/library/venv.html).

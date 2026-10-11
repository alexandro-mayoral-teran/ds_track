# Recorrido — Conda

Lee [05A](environment.md) antes de la parte A y [05B](dependencies.md) antes de la parte B.
Sigue solo el bloque de tu shell.

## Parte A — Preparar y usar el entorno

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

## Parte B — Instalar y conservar dependencias

Lee [05B](dependencies.md) antes de continuar. Ya debes tener ds-track preparado.

### Instalar y comprobar una biblioteca

Lee primero la [teoría común](README.md). Con ds-track activado, desde la raíz:

```text
# Instala una versión concreta desde un canal explícito; revisa el plan
conda install -c conda-forge tabulate=0.9.0
# Consulta su instalación y comprueba que el Python activo puede importarla
conda list tabulate
python -c "import tabulate; print(tabulate.__version__)"
# Ejecuta la misma demostración de los tres recorridos
python curriculum/00_getting_started/05_environment/library_demo.py
```

Debes ver 0.9.0 y una tabla con cuaderno 80, lapiz 50 y carpeta 35.
El script presenta datos ficticios; sus estructuras se estudiarán en Python fundamental.
Ahora registra el entorno con la biblioteca instalada, como indica el siguiente apartado.

## Registrar después de instalar

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

## Consultar, actualizar y retirar: referencia

conda list consulta paquetes; conda update tabulate propone una actualización
permitida por los requisitos; conda remove tabulate propone retirarlo y puede
afectar dependencias. No ejecutes estos cambios antes de terminar el lab.
El export desde historial no es un lockfile exacto y no registra paquetes de pip.

Continúa con el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md).
Fuente: [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).

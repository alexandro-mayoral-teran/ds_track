# 00.05 — Recorrido con Conda

<a id="recorrido--conda"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / [00.05](README.md) / **Conda**

> **Camino alternativo:** completa este recorrido solo si elegiste Conda.
> Conserva el mismo entorno en A y B; no necesitas completar los otros caminos.

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Preparar, utilizar y registrar el entorno con Conda |
| **Necesitas** | Anaconda y el shell del recorrido; preparación indicada más abajo |
| **Evidencia** | Ruta de Python, tabla comprobada y configuración revisada |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Aplicar las dos sesiones de 00.05 con Conda, comprobando intérprete,
importación y registro de dependencias.

## Antes de empezar

Lee los conceptos comunes de [05A](environment.md) antes de elegir este camino
y de realizar la parte A; lee [05B](dependencies.md) antes de la parte B.
Sigue solo el bloque de tu shell.

## Qué vas a aprender

- Preparar y reconocer el intérprete de este camino en la parte A.
- Instalar y comprobar la biblioteca en la parte B.
- Registrar y explicar los archivos que permiten reconstruir el entorno.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Teoría de entornos](environment.md) | Comprender qué preparas antes de la parte A | Sesión A |
| [Teoría de dependencias](dependencies.md) | Comprender instalación y registro antes de la parte B | Sesión B |
| [Primer script](../04_first_script/first_summary.py) | Comprobar ejecución sin paquetes externos | Sesión A |
| [Demostración con biblioteca](library_demo.py) | Contrastar la importación y la tabla de ventas | Sesión B |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

[Parte A: teoría](environment.md) · [Parte B: teoría](dependencies.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md)

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

**PowerShell:**

```powershell
New-Item -ItemType Directory -Force .environment-practice
conda env export --from-history | Set-Content -Encoding utf8 .environment-practice/environment.yml
```

**CMD — Anaconda Prompt:**

```bat
if not exist .environment-practice mkdir .environment-practice
conda env export --from-history > .environment-practice\environment.yml
```

**Bash/Zsh:**

```bash
mkdir -p .environment-practice
conda env export --from-history > .environment-practice/environment.yml
```

Ejecuta solo el bloque de tu shell. Exporta los requisitos elegidos explícitamente
a `.environment-practice/environment.yml`, una carpeta de práctica excluida de Git.
Antes de exportar, comprueba si el archivo ya existe: los comandos de escritura
lo reemplazan. Si necesitas conservarlo, elige otro nombre y usa esa misma ruta
al reconstruir.
Revisa el archivo antes de compartirlo: elimina un campo `prefix` con una ruta
personal si aparece.
Este export conserva elecciones hechas con Conda; no registra paquetes instalados
con pip ni fija todas las dependencias transitivas. No equivale a un lockfile.
Otra persona puede reconstruirlo desde la raíz con
`conda env create -f .environment-practice/environment.yml`
si el nombre no existe. Los paquetes de pip requerirán su declaración aparte.

## Consultar, actualizar y retirar: referencia

conda list consulta paquetes; conda update tabulate propone una actualización
permitida por los requisitos; conda remove tabulate propone retirarlo y puede
afectar dependencias. No ejecutes estos cambios antes de terminar el lab.
El export desde historial no es un lockfile exacto y no registra paquetes de pip.

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para completar las sesiones A y B con Conda.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Nota y configuración del camino elegido | Ruta de Python, versión importada y tabla de ventas | Qué archivos conservar y cómo reconstruir sin copiar el entorno |

Completa la sesión A antes de B. Al cerrar ambas, contrasta la evidencia con
el [criterio común de 00.05](README.md#evidencia-y-criterio-de-salida).

Quien aprende realiza la práctica y explica el resultado. Tu compañero pide identificar qué entorno ejecutó cada comprobación.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

## Referencias

Fuente: [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).

## Siguiente paso

Después del lab y su comprobación, continúa con [00.06 — Tu primer notebook](../06_first_notebook/README.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](../06_first_notebook/README.md)

[Volver a la entrada de 00.05](README.md) · [Revisar 05A](environment.md) · [Revisar 05B](dependencies.md).

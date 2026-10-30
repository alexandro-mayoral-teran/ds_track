# 00.05 — Recorrido con venv + pip

<a id="recorrido--venv--pip"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / [00.05](README.md) / **venv + pip**

> **Camino alternativo:** completa este recorrido solo si elegiste venv + pip.
> Conserva el mismo entorno en A y B; no necesitas completar los otros caminos.

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Preparar un entorno con venv y registrar sus paquetes con pip |
| **Necesitas** | Python 3.11 o posterior y el shell elegido |
| **Evidencia** | Ruta de Python, tabla comprobada y requisitos revisados |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Glosario](#glosario) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Aplicar las dos sesiones de 00.05 con venv + pip, comprobando intérprete,
importación y registro de dependencias.

## Antes de empezar

Este recorrido es el camino estándar si eliges administrar paquetes con pip. Sal de cualquier entorno activo antes de practicar.
`.venv-practice` está separado de `.venv` y está excluido de Git.

Lee primero los [conceptos comunes de 05A](environment.md). Necesitas Python 3.11 o posterior;
si falta, consulta la [descarga oficial](https://www.python.org/downloads/).
Elige un solo shell y completa su bloque antes de pasar al lab.

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

## Recorrido en PowerShell

### Parte A — Preparar y usar el entorno

```powershell
# Sustituye el marcador por la carpeta real de tu copia de DS Track
Set-Location "RUTA_REAL_DE_DS_TRACK"
Get-Location
# Comprueba el Python disponible para crear el entorno
python --version
# Crea solo si todavía no existe
python -m venv .venv-practice
# Usa directamente el ejecutable sin activar
.\.venv-practice\Scripts\python.exe --version
.\.venv-practice\Scripts\python.exe -c "import sys; print(sys.executable)"
.\.venv-practice\Scripts\python.exe -m pip --version
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\04_first_script\first_summary.py
```

La activación opcional usa `.\.venv-practice\Scripts\Activate.ps1`; si está
bloqueada, utiliza la ruta directa sin cambiar políticas. Para salir, `deactivate`.

### Parte B — Instalar, comprobar y registrar

Antes de continuar, lee [05B](dependencies.md). Conserva el entorno de la parte A.

Lee primero la [teoría común](README.md). Desde la raíz, después de crear venv:

```powershell
# Instala para este intérprete, no para el Python global
.\.venv-practice\Scripts\python.exe -m pip install "tabulate==0.9.0"
# Consulta y comprueba dependencias declaradas
.\.venv-practice\Scripts\python.exe -m pip show tabulate
.\.venv-practice\Scripts\python.exe -m pip check
# Comprueba importación y ejecuta el ejemplo
.\.venv-practice\Scripts\python.exe -c "import tabulate; print(tabulate.__version__)"
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\05_environment\library_demo.py
# Conserva lo instalado en una carpeta de práctica local
New-Item -ItemType Directory -Force .environment-practice
.\.venv-practice\Scripts\python.exe -m pip freeze | Set-Content -Encoding utf8 .environment-practice/requirements.txt
```

## Recorrido en Bash/Zsh

### Parte A — Preparar y usar el entorno

```bash
# Sustituye el marcador por la carpeta real de tu copia
cd "RUTA_REAL_DE_DS_TRACK"
pwd
python3 --version
# Crea solo si todavía no existe
python3 -m venv .venv-practice
./.venv-practice/bin/python --version
./.venv-practice/bin/python -c "import sys; print(sys.executable)"
./.venv-practice/bin/python -m pip --version
./.venv-practice/bin/python curriculum/00_getting_started/04_first_script/first_summary.py
```

Puedes activar con `source .venv-practice/bin/activate` y salir con `deactivate`.
En CMD la activación es `.venv-practice\Scripts\activate.bat`.
En algunas distribuciones Linux necesitas instalar el componente venv de Python.

### Parte B — Instalar, comprobar y registrar

Antes de continuar, lee [05B](dependencies.md). Conserva el entorno de la parte A.

```bash
# Instala y consulta el paquete en el intérprete elegido
./.venv-practice/bin/python -m pip install 'tabulate==0.9.0'
./.venv-practice/bin/python -m pip show tabulate
./.venv-practice/bin/python -m pip check
# Comprueba y ejecuta
./.venv-practice/bin/python -c "import tabulate; print(tabulate.__version__)"
./.venv-practice/bin/python curriculum/00_getting_started/05_environment/library_demo.py
# Registra lo instalado
mkdir -p .environment-practice
./.venv-practice/bin/python -m pip freeze > .environment-practice/requirements.txt
```

Debes ver 0.9.0 y una tabla con cuaderno 80, lapiz 50 y carpeta 35.
pip check comprueba las dependencias declaradas, no que cualquier programa funcione.

## Comprobar y retomar el entorno

La ruta consultada debe terminar en `.venv-practice/Scripts/python.exe` en
Windows o `.venv-practice/bin/python` en Linux/macOS. Usa el separador de rutas
de tu sistema. El primer script debe mostrar un total de 120 MXN con su fuente original.
Si la carpeta ya existe, consulta su Python y sus paquetes antes de reutilizarla;
no repitas la creación a ciegas.

Al retomar, vuelve a la raíz de tu copia y utiliza la ruta directa del mismo
Python. Cerrar la terminal no elimina el entorno. La parte B de ambos shells
también empieza desde esa raíz.

## Registrar y reconstruir

Antes de exportar, comprueba si `.environment-practice/requirements.txt` ya
existe: la escritura lo reemplaza. Si necesitas conservarlo, usa otro nombre
y emplea esa misma ruta al reconstruir.

Revisa requirements.txt y documenta la versión de Python. freeze incluye lo
instalado, también dependencias transitivas; no identifica por sí solo las
necesidades directas ni crea un lockfile multiplataforma. Crea un nuevo entorno
y usa su Python con `-m pip install -r .environment-practice/requirements.txt`
para reinstalar la lista. No copies el directorio del entorno.

Para actualizar se usa `-m pip install --upgrade tabulate`; para retirar,
`-m pip uninstall tabulate`. Son referencias, no pasos obligatorios; conserva
la instalación para el lab. Documenta y comprueba cualquier actualización.
Si falta Python, consulta su instalación oficial. Si en Linux falla venv o
ensurepip, consulta el componente requerido por tu distribución.

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para completar las sesiones A y B con venv + pip.

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

## Glosario

Consulta el [glosario común de 00.05](README.md#glosario) para recuperar
intérprete, entorno, gestor, instalación, importación y reconstrucción.
Las lecturas incluyen además los glosarios de [05A](environment.md#glosario)
y [05B](dependencies.md#glosario), con los conceptos utilizados en ambas partes.

## Referencias

Fuente: [pip y entornos](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

## Siguiente paso

Después del lab y su comprobación, continúa con [00.06 — Tu primer notebook](../06_first_notebook/README.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](../06_first_notebook/README.md)

[Volver a la entrada de 00.05](README.md) · [Revisar 05A](environment.md) · [Revisar 05B](dependencies.md).

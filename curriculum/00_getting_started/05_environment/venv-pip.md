# Recorrido — venv + pip

Este recorrido es el camino estándar si eliges administrar paquetes con pip. Sal de cualquier entorno activo antes de practicar.
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

## Instalar y comprobar — PowerShell

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

## Instalar y comprobar — Bash/Zsh

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

## Registrar y reconstruir

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

Continúa con el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md).
Fuente: [pip y entornos](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

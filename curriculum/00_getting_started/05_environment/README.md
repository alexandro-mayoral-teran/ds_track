# 05 — Entorno y dependencias

## Propósito

Saber qué Python ejecuta tu código, dónde se instalan sus paquetes y cómo
preparar el entorno de DS Track. Esta base evita mezclar instalaciones de
proyectos distintos y permite repetir un análisis en otra computadora.

## Prerrequisitos y objetivos

Completa [04 — Primer script](../04_first_script/README.md) hasta donde permita
tu instalación. Necesitas terminal y acceso a Internet para descargar herramientas
o paquetes. En un equipo administrado, utiliza las instalaciones autorizadas.

Al terminar podrás identificar tu intérprete, crear un entorno de práctica,
explicar pip frente a uv y ejecutar el script con el entorno del proyecto.
No necesitas pandas todavía.

## 1. Las piezas del entorno

| Pieza | Qué es | Ejemplo |
| --- | --- | --- |
| Intérprete | Programa que ejecuta Python | `python` o `python3` |
| Biblioteca estándar | Módulos incluidos en Python | `csv`, `pathlib`, `sys` |
| Paquete externo | Código que instalas por separado | pandas, más adelante |
| Dependencia | Paquete que necesita tu proyecto | Una biblioteca para leer datos |
| Entorno virtual | Instalación aislada de paquetes asociada a un Python | `.venv` |
| pip | Instalador de paquetes para un intérprete | `python -m pip` |
| uv | Herramienta para gestionar Python, entornos y dependencias | `uv sync` |

VS Code edita tu programa; el intérprete lo ejecuta. Dos instalaciones de Python
pueden tener paquetes distintos. Instalar un paquete en una no lo hace disponible
automáticamente en otra.

Un entorno virtual separa paquetes de Python, no es una máquina virtual ni una
barrera de seguridad. Usaremos uno compartido para DS Track, no uno por lección.

> **Para conversar:** un script funciona en tu computadora, pero otra persona
> recibe «módulo no encontrado». ¿Qué revisarías además del código?

## 2. Preparar las herramientas si faltan

### Python

DS Track requiere **Python 3.11 o posterior**, según `pyproject.toml`.
Si ya tienes una versión compatible, no necesitas instalar otra para esta práctica.
Si falta, utiliza la [descarga e instrucciones oficiales](https://www.python.org/downloads/)
para tu sistema. En Windows puedes seguir la instalación del gestor oficial de
Python; en Linux/macOS utiliza las instrucciones oficiales o el método de tu sistema.
Abre una terminal nueva al terminar y comprueba la versión.

### uv

Consulta las [instrucciones oficiales de instalación](https://docs.astral.sh/uv/getting-started/installation/).
Una opción, si tu instalación de Python admite instalar herramientas de usuario,
es `python -m pip install --user uv` (o `python3 -m pip install --user uv`).
No lo ejecutes dentro del entorno de práctica: uv es la herramienta que lo gestiona.
Si tu sistema bloquea esa instalación, sigue un método oficial compatible; no
necesitas forzar cambios en el Python del sistema.

Comprueba `uv --version` en una terminal nueva. Si no se reconoce, revisa la
ubicación de la instalación y las instrucciones del instalador.

## 3. Cómo estudiar los dos recorridos

Elige [PowerShell](#recorrido-en-powershell) o [Bash/Zsh](#recorrido-en-bashzsh).
En cada uno hay dos partes:

1. **venv y pip:** un entorno aparte para comprender el mecanismo.
2. **uv:** preparar el entorno habitual de DS Track desde sus archivos.

El entorno didáctico `.venv-practice` está separado de `.venv`, que administra uv.
No instales paquetes manualmente en `.venv`: `uv sync` puede eliminar paquetes
que el proyecto no declara. Si ya estás en otro entorno activado, desactívalo
antes de empezar; en un entorno venv se utiliza `deactivate`.

## Recorrido en PowerShell

### A. Identificar el intérprete

Desde la raíz de `ds_track`:

```powershell
# Comprueba la versión y la ubicación del comando
python --version
Get-Command python
# Pregunta al propio Python qué ejecutable está usando
python -c "import sys; print(sys.executable)"
```

`-c` ejecuta una instrucción breve. `sys` pertenece a la biblioteca estándar y
`sys.executable` muestra el ejecutable real. Su ruta depende de tu instalación.
Si solo tienes el lanzador `py`, usa `py -3` en lugar de `python` para crear el
entorno; comprueba que su versión cumple el requisito.

### B. Crear un entorno de práctica y conocer pip

```powershell
# Crea el entorno de práctica; hazlo solo si todavía no existe
python -m venv .venv-practice
# Comprueba directamente su intérprete, sin activar el entorno
.\.venv-practice\Scripts\python.exe -c "import sys; print(sys.executable)"
# Consulta pip asociado a ese Python y sus paquetes instalados
.\.venv-practice\Scripts\python.exe -m pip --version
.\.venv-practice\Scripts\python.exe -m pip list
# Ejecuta el script con el intérprete aislado
.\.venv-practice\Scripts\python.exe curriculum\00_getting_started\04_first_script\first_summary.py
```

`-m venv` ejecuta el módulo que crea entornos. `-m pip` utiliza el pip de ese
intérprete. La ruta mostrada debe estar dentro de `.venv-practice`; la lista de
paquetes depende de la versión de Python. El script funciona sin paquetes externos.

Activar es una comodidad, no un requisito. Si lo deseas:

```powershell
# Hace que python resuelva al entorno en esta terminal
.\.venv-practice\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
# Vuelve a la selección anterior del shell
deactivate
```

Si PowerShell bloquea la activación, usa la ruta directa de los ejemplos anteriores;
no necesitas cambiar la política de ejecución para completar la práctica.

### C. Preparar DS Track con uv

```powershell
# Comprueba la herramienta
uv --version
# Crea o sincroniza .venv respetando el lockfile existente
uv sync --locked
# Comprueba qué Python utiliza el proyecto
uv run --locked python -c "import sys; print(sys.executable)"
# Ejecuta el primer script dentro de ese entorno
uv run --locked python curriculum\00_getting_started\04_first_script\first_summary.py
```

La ruta del intérprete del proyecto debe estar dentro de `.venv`. No necesitas
activarlo para utilizar `uv run`. Si aparece un aviso por otro entorno activado,
sal de ese entorno antes de continuar.

## Recorrido en Bash/Zsh

### A. Identificar el intérprete

Desde la raíz de `ds_track`:

```bash
# Comprueba la versión y la ubicación
python3 --version
command -v python3
# Consulta el ejecutable que Python utiliza
python3 -c "import sys; print(sys.executable)"
```

Si tu instalación utiliza `python`, sustituye `python3` en estos comandos.

### B. Crear un entorno de práctica y conocer pip

```bash
# Crea el entorno solo si todavía no existe
python3 -m venv .venv-practice
# Consulta directamente su intérprete y su pip
./.venv-practice/bin/python -c "import sys; print(sys.executable)"
./.venv-practice/bin/python -m pip --version
./.venv-practice/bin/python -m pip list
# Ejecuta el script sin activar el entorno
./.venv-practice/bin/python curriculum/00_getting_started/04_first_script/first_summary.py
```

La ruta debe señalar `.venv-practice`. Si tu distribución informa que falta
`venv` o `ensurepip`, instala el componente de entornos indicado por su
documentación con quien te acompaña; no uses una instalación global forzada.

Activación opcional:

```bash
# Selecciona el entorno para esta terminal
source .venv-practice/bin/activate
python -c "import sys; print(sys.executable)"
# Sale de la activación
deactivate
```

### C. Preparar DS Track con uv

```bash
# Comprueba uv y sincroniza las dependencias declaradas
uv --version
uv sync --locked
# Consulta el intérprete del proyecto
uv run --locked python -c "import sys; print(sys.executable)"
# Ejecuta el script en .venv
uv run --locked python curriculum/00_getting_started/04_first_script/first_summary.py
```

## 4. Qué instalar y cómo registrar dependencias

pip instala paquetes, pero instalar no documenta por sí solo lo que necesita
el proyecto. La forma `python -m pip install NOMBRE_DEL_PAQUETE` selecciona el
pip del intérprete que indicas. Es un patrón ilustrativo: no ejecutes el marcador
ni instales paquetes adicionales para este lab.

En el flujo del proyecto, `uv add NOMBRE_DEL_PAQUETE` agrega una dependencia y
actualiza su configuración y lockfile. Lo practicaremos cuando una lección
requiera una biblioteca. Ahora `dependencies = []`: no hay paquetes externos.

| Archivo o carpeta | Qué conserva | ¿Se comparte en Git? |
| --- | --- | --- |
| `pyproject.toml` | Requisitos del proyecto y dependencias declaradas | Sí |
| `uv.lock` | Versiones y resolución de dependencias | Sí |
| `.venv` | Entorno local generado por uv | No |
| `.venv-practice` | Entorno didáctico de esta lección | No |

`uv sync --locked` prepara el entorno y falla si el lockfile no corresponde a
la configuración, en lugar de modificarlo. Puede necesitar Internet para obtener
Python o paquetes. Compartir estos archivos permite reconstruir el entorno;
no copies la carpeta `.venv` a otra computadora.

## 5. Usar el mismo Python en VS Code

Si instalaste la extensión Python de Microsoft, abre la paleta y ejecuta
**Python: Select Interpreter**. Selecciona el Python dentro de `.venv` del proyecto.
Consulta la [guía de VS Code](../../../docs/vscode-guide.md).
La selección del editor y la activación de una terminal son acciones distintas:
comprueba el ejecutable si obtienes resultados diferentes. `uv run` utiliza el
entorno del proyecto sin depender de esa selección del editor.

## Cuando algo no funciona

| Situación | Qué revisar |
| --- | --- |
| Python o uv no se reconoce | Instalación, nombre del comando y terminal nueva |
| Python no cumple 3.11 o posterior | La versión elegida para el proyecto |
| Activación bloqueada en PowerShell | Ejecutar directamente el Python del entorno |
| Un paquete no se encuentra | Qué intérprete lo ejecuta y dónde se instaló |
| El lockfile está desactualizado | Si cambiaste pyproject.toml; revisa con quien acompaña antes de actualizarlo |
| Falla una descarga | Conexión y mensaje del instalador; conserva el pendiente |
| El entorno busca un Python que ya no existe | Se movió o eliminó la instalación base; identifica un Python compatible y reconstruye el entorno con quien acompaña |

Si ya existe un entorno dañado, no repitas instalaciones al azar. Los entornos
son regenerables, pero comprueba primero su ruta y conserva los archivos del
proyecto. Eliminar o cambiar la instalación base de Python puede invalidarlos.

> **Para comprobar:** ¿qué se comparte para reconstruir el entorno y qué se
> genera de nuevo en cada computadora?

## Práctica y criterio de salida

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md).
Puedes avanzar cuando identifiques el intérprete, distingas pip de uv y ejecutes
el script en el entorno del proyecto. No hay proyecto de datos asociado todavía.

## Siguiente lección

06 — Primer notebook (por desarrollar). Consulta el [índice del nivel 0](../README.md).

## Referencias oficiales

- [Entornos virtuales de Python](https://docs.python.org/3/library/venv.html).
- [Uso de pip](https://pip.pypa.io/en/stable/user_guide/).
- [Instalación de uv](https://docs.astral.sh/uv/getting-started/installation/).
- [Proyectos con uv](https://docs.astral.sh/uv/guides/projects/).
- [Sincronización y lockfiles](https://docs.astral.sh/uv/concepts/projects/sync/).

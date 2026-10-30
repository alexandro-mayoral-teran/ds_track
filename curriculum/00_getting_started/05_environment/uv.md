# 00.05 — Recorrido con uv

<a id="recorrido--uv"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / [00.05](README.md) / **uv**

> **Camino alternativo:** completa este recorrido solo si elegiste uv.
> Conserva el mismo entorno en A y B; no necesitas completar los otros caminos.

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Preparar y registrar el mini proyecto de práctica con uv |
| **Necesitas** | uv y el shell elegido; preparación indicada más abajo |
| **Evidencia** | Ruta de Python, tabla comprobada, configuración y lockfile revisados |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Aplicar las dos sesiones de 00.05 con uv, comprobando intérprete,
importación y registro de dependencias.

## Antes de empezar

Lee los [conceptos comunes de 05A](environment.md). Completa este camino si eliges configuración
y lockfile integrados; no necesitas practicar también Conda o venv + pip.

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

## Preparar la herramienta

Consulta la [instalación oficial](https://docs.astral.sh/uv/getting-started/installation/)
y comprueba uv --version. Sal de entornos Conda con conda deactivate o de venv
con deactivate. No uses el mismo entorno con otros gestores.

Practicaremos en .environment-practice/uv-demo, un mini proyecto local ignorado
por Git, para no modificar las dependencias del repositorio compartido. Si ya
existe, entra y consulta sus archivos en lugar de repetir init.

## PowerShell

### Parte A — Preparar y usar el entorno

Desde la raíz de ds_track:

```powershell
# Conserva la ubicación para volver después
$dsTrackRoot = (Get-Location).Path
# Crea una configuración mínima, sin otro repositorio Git
uv init --bare --no-workspace --vcs none --python 3.12 .environment-practice/uv-demo
Set-Location .environment-practice/uv-demo
# Primera preparación: genera el lockfile inicial sin bibliotecas externas
uv sync
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python ../../curriculum/00_getting_started/04_first_script/first_summary.py
Set-Location $dsTrackRoot
```

### Parte B — Instalar y conservar dependencias

Lee [05B](dependencies.md). Desde la raíz de ds_track:

```powershell
# Usa el proyecto que ya preparaste en la parte A
$dsTrackRoot = (Get-Location).Path
Set-Location .environment-practice/uv-demo
# Declara e instala el paquete; actualiza configuración y lockfile
uv add "tabulate==0.9.0"
# Consulta el intérprete y comprueba la importación
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python -c "import tabulate; print(tabulate.__version__)"
# Ejecuta el ejemplo con el entorno del mini proyecto
uv run --locked python ../../curriculum/00_getting_started/05_environment/library_demo.py
# Consulta dependencias y vuelve a la raíz
uv tree --locked
Set-Location $dsTrackRoot
```

## Bash/Zsh

### Parte A — Preparar y usar el entorno

```bash
# Desde ds_track, conserva la ubicación
ds_track_root="$PWD"
# Crea solo si todavía no existe
uv init --bare --no-workspace --vcs none --python 3.12 .environment-practice/uv-demo
cd .environment-practice/uv-demo
# Prepara el entorno y genera su lockfile inicial
uv sync
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python ../../curriculum/00_getting_started/04_first_script/first_summary.py
cd "$ds_track_root"
```

### Parte B — Instalar y conservar dependencias

Lee [05B](dependencies.md). Desde la raíz de ds_track:

```bash
# Entra al proyecto ya creado
ds_track_root="$PWD"
cd .environment-practice/uv-demo
# Declara e instala
uv add 'tabulate==0.9.0'
# Consulta el intérprete y comprueba
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python -c "import tabulate; print(tabulate.__version__)"
uv run --locked python ../../curriculum/00_getting_started/05_environment/library_demo.py
uv tree --locked
# Regresa al repositorio
cd "$ds_track_root"
```

La versión es 0.9.0 y la tabla contiene cuaderno 80, lapiz 50 y carpeta 35.
El ejecutable pertenece a .environment-practice/uv-demo/.venv. uv puede descargar
Python si no hay una instalación compatible.

## Registrar y reconstruir

init crea la configuración; add declara la dependencia, resuelve y prepara el
entorno; run ejecuta en el proyecto actual. --locked exige que el lockfile
corresponda a los requisitos. tree muestra dependencias directas y transitivas.

Lee pyproject.toml y uv.lock dentro del mini proyecto. Comparte esos archivos
y el código, no .venv. En otra copia, uv sync --locked reconstruye el entorno.
La carpeta está ignorada porque es una práctica; guarda una copia revisada de
la configuración como evidencia si lo deseas, sin sobrescribir la de DS Track.

Para retomar, entra al mini proyecto y utiliza uv run. La raíz de DS Track
es otro proyecto; sus archivos actuales no declaran tabulate y su uv run no
necesariamente permite importarlo.

## Consultar, actualizar y retirar: referencia

uv lock --upgrade-package tabulate actualiza dentro de las restricciones: con
==0.9.0 no puede elegir otra versión. Para cambiar ese requisito primero modifica
la dependencia con uv add. uv remove tabulate retira su declaración y sincroniza.
Conserva el paquete para el lab. No instales manualmente con pip en este entorno:
una sincronización exacta puede retirar paquetes no declarados.

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para completar las sesiones A y B con uv.

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

Fuentes: [proyectos](https://docs.astral.sh/uv/guides/projects/) y
[sincronización](https://docs.astral.sh/uv/concepts/projects/sync/).

## Siguiente paso

Después del lab y su comprobación, continúa con [00.06 — Tu primer notebook](../06_first_notebook/README.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](../06_first_notebook/README.md)

[Volver a la entrada de 00.05](README.md) · [Revisar 05A](environment.md) · [Revisar 05B](dependencies.md).

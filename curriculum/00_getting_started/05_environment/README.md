# 05 — Entornos y administración de dependencias

## Propósito y objetivos

Comprender qué Python ejecuta tu código, dónde están sus bibliotecas y cómo
reconstruir un entorno. Después de [04 — Primer script](../04_first_script/README.md),
estudia la teoría y completa **uno** de los tres recorridos prácticos.
La meta es identificar el intérprete, instalar y comprobar una biblioteca pequeña
y registrar los requisitos. Necesitas Internet para las descargas.

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

Instalar prepara el paquete; import permite utilizarlo desde un programa.
El nombre para instalar no siempre coincide con el nombre para importar; en
este ejemplo ambos son tabulate. El editor no incluye automáticamente todas
las bibliotecas que tu script necesita.

## 2. Cómo funciona un entorno y para qué sirve

Un análisis puede necesitar una versión de una biblioteca y otro una diferente.
Si comparten una instalación global, actualizar para uno puede afectar al otro.
Un entorno por proyecto separa sus paquetes y permite identificar el conjunto usado.

```text
Proyecto A → entorno A → intérprete y paquetes para A
Proyecto B → entorno B → intérprete y paquetes para B
```

venv se apoya en un Python instalado y crea su propio directorio de paquetes,
normalmente site-packages. Conda también puede administrar el intérprete y
componentes binarios. uv gestiona entornos y dependencias de proyectos y puede
obtener versiones de Python.

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

## 3. Qué hace activar un entorno

Activar cambia la selección de comandos de **esa sesión del shell**, para que
python y otras herramientas resuelvan al entorno. No mueve tu código ni copia
paquetes entre instalaciones. Una terminal nueva puede requerir otra activación.

Puedes usar directamente el ejecutable de venv sin activarlo o ejecutar con
uv run. En Conda activar también prepara variables que pueden requerir sus bibliotecas.

```text
# Consulta el ejecutable que está usando Python
python -c "import sys; print(sys.executable)"
```

En VS Code, Python: Select Interpreter elige el Python del editor, pero no cambia
 automáticamente todas las terminales abiertas. En notebooks elegiremos además
el kernel; lo veremos en la siguiente lección.

> **Para conversar:** ¿por qué «ya instalé la biblioteca» no basta para explicar
> que el programa pueda importarla?

## 4. Qué aporta cada camino

### Conda

Gestiona entornos, Python y paquetes, incluidos componentes que no son solo
Python. Obtiene paquetes de canales. Anaconda es una distribución que incluye
Conda y herramientas; Anaconda Prompt es una ventana con un shell configurado.

**Ventajas:** encaja con Anaconda y permite gestionar Python y componentes
binarios desde una herramienta. **Limitaciones:** disponibilidad según canales
 y plataformas, espacio de instalación y resolución de dependencias. Mezclar
pip requiere cuidado y registrar ambas fuentes.

### venv + pip

venv crea el entorno a partir de un Python existente. pip instala paquetes
Python y resuelve sus dependencias, habitualmente desde PyPI. **pip no crea
por sí solo el entorno**.

**Ventajas:** herramientas estándar, ampliamente documentadas y explícitas sobre
qué intérprete recibe cada instalación. **Limitaciones:** administras Python,
el entorno y los requisitos por separado; pip no gestiona bibliotecas del sistema.
pip freeze describe lo instalado, pero no es un lockfile multiplataforma.

### uv

Integra entornos, versiones de Python y dependencias de proyectos. Aquí usamos
su interfaz de proyectos: uv add, uv sync y uv run.

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

## 5. Elegir tu recorrido

- **Ya usas Anaconda:** [Conda](conda.md).
- **Quieres las herramientas estándar:** [venv + pip](venv-pip.md).
- **Quieres configuración y lockfile integrados:** [uv](uv.md).

Cada documento separa shells, explica instalación y consulta de paquetes, e
incluye la misma práctica con tabulate 0.9.0. DS Track requiere Python 3.11 o posterior.
No completes los tres ni mezcles gestores en el mismo entorno. Evita instalar
los ejercicios en base o usar --user dentro de un entorno.

No copies carpetas de entornos entre computadoras: reconstruye desde sus archivos.
Antes de compartir configuración, revisa rutas personales y credenciales.

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

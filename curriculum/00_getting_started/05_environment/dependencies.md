# 00.05B — Instalar y conservar dependencias

<a id="05b--instalar-y-conservar-dependencias"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.05B**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Comprobar una biblioteca y conservar los requisitos del entorno |
| **Necesitas** | Camino elegido en 00.05 y shell correspondiente |
| **Evidencia** | Comprobación y nota personal de la sesión B |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/00_getting_started/05_environment/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

[← Entrada de 00.05](README.md) · [Sesión A](environment.md) · [Sesión B](dependencies.md)

## Propósito

Relacionar instalación e importación y conservar los requisitos del entorno que preparaste en la sesión A.

## Antes de empezar

Completa [00.05A — Preparar y usar un entorno](environment.md).
Utiliza el mismo camino y entorno en ambas partes; no crees otro para esta
sesión. Las instrucciones de instalación están en la parte B de tu recorrido.

## Qué vas a aprender

- Distinguir instalar una biblioteca de importarla.
- Comprobar versión e importación desde el intérprete elegido.
- Explicar qué registran requirements, environment.yml o el lockfile de tu camino.
- Identificar qué compartir para reconstruir y qué límites tiene ese registro.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Demostración con biblioteca](library_demo.py) | Ejecutar la misma tabla de ventas en el entorno de la sesión A | Sesión B |
| [Conda](conda.md) | Consultar instalación y registro con Conda | Solo si lo elegiste |
| [venv + pip](venv-pip.md) | Consultar instalación y registro con pip | Solo si lo elegiste |
| [uv](uv.md) | Consultar declaración y lockfile con uv | Solo si lo elegiste |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

## 1. Instalar e importar

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


## 2. Qué contiene requirements.txt y cómo se utiliza

requirements.txt es un archivo de texto con una lista de cosas que pip debe
instalar. Puedes escribir los requisitos que necesita el proyecto, por ejemplo:

```text
# Biblioteca utilizada en la demostración
tabulate==0.9.0
```

`==0.9.0` pide esa versión exacta. También existen requisitos sin una versión
fijada o con rangos, pero aquí usamos una versión concreta para comparar resultados.
El nombre requirements.txt es convencional; no es una palabra reservada de Python.

Desde la carpeta que contiene el archivo y utilizando el Python del entorno:

```text
# Instala lo declarado en el archivo
python -m pip install -r requirements.txt
```

`-r` indica que pip debe leer los requisitosdel archivo. **No crea un entorno
ni instala Python**: primero prepara y selecciona el intérprete de 05A.
Si no activaste el entorno, usa la ruta directa de su Python como en el recorrido pip.

### Escribir requisitos o capturar lo instalado

Son dos operaciones distintas:

- **Escribir el archivo:** declaras los paquetes que quieres instalar para el proyecto.
- **Generarlo con freeze:** registras las versiones de lo que está instalado en
  el entorno, incluidas sus dependencias transitivas.

```text
# Captura el estado instalado en una lista de requisitos
python -m pip freeze > requirements.txt
```

`>` escribe en el archivo y puede sobrescribirlo. Revisa la ubicación antes de
usarlo. En PowerShell sigue el método con Set-Content del recorrido pip para
escribir texto UTF-8. Exporta desde un entorno del proyecto, no desde una
instalación con paquetes de muchos trabajos distintos.

freeze no analiza cuáles paquetes usa tu código ni genera por sí solo un lockfile.
Aunque fijes versiones, pueden existir limitaciones de plataforma o requisitos
externos. Documenta también Python y comprueba la reconstrucción.

## 3. Archivos de cada recorrido

### Conda: environment.yml

Describe el nombre del entorno, los canales y sus dependencias. Ejemplo para leer:

```yaml
name: ds-track
channels:
  - conda-forge
dependencies:
  - python=3.12
  - pip
  - tabulate=0.9.0
```

La exportación desde historial recoge elecciones hechas con Conda, sin fijar
necesariamente todas las dependencias transitivas ni incluir paquetes instalados
con pip. Si utilizas ambas fuentes, debes declararlas. El archivo permite crear
el entorno; no es una carpeta de paquetes ni un lockfile exacto.

### uv: pyproject.toml y uv.lock

pyproject.toml declara información del proyecto y requisitos. TOML es el formato
del archivo, no una herramienta exclusiva de uv. Ejemplo de un fragmento:

```toml
[project]
name = "uv-demo"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["tabulate==0.9.0"]
```

uv.lock conserva la resolución de dependencias que produjo uv. No lo escribas
manualmente para esta práctica: uv add o uv lock lo generan. uv sync --locked
prepara el entorno y comprueba que el lockfile corresponda a la configuración.
Los dos archivos cumplen funciones distintas y se comparten junto con el código.

| Archivo | Qué expresa | Qué no hace por sí solo |
| --- | --- | --- |
| requirements.txt | Requisitos de instalación para pip | Crear el entorno o instalar Python |
| environment.yml | Especificación de un entorno Conda | Garantizar toda la resolución exacta entre plataformas |
| pyproject.toml | Metadatos y requisitos del proyecto Python | Contener una copia de los paquetes |
| uv.lock | Resolución de dependencias de uv | Sustituir el código, los datos o todos los requisitos del sistema |

## 4. Reconstruir en vez de copiar el entorno

La secuencia es **compartir código y configuración → preparar un entorno →
instalar lo declarado → ejecutar y comprobar**. No copies .venv entre computadoras.

- pip: crea el entorno primero e instala el archivo con `-m pip install -r`.
- Conda: crea el entorno desde el YAML, como indica su recorrido.
- uv: utiliza la configuración y el lockfile con `uv sync --locked`.

Revisa los archivos antes de compartir: evita rutas personales, credenciales y
paquetes ajenos al proyecto. Los archivos de práctica están en carpetas locales
ignoradas; conserva una copia revisada si necesitas presentar la evidencia.

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para realizar la sesión B y la parte B del recorrido elegido.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Configuración revisada y nota con ejecutable/versión | Tabulate 0.9.0 y tabla con importes 80, 50 y 35 MXN | Qué archivo compartirías, cómo se reconstruye y qué no garantiza |

Puedes avanzar cuando importes tabulate 0.9.0, ejecutes la demostración y
expliques qué archivo compartirías para reconstruir esa instalación y cuáles
son sus límites. No basta con que el instalador haya terminado sin error.

Quien aprende realiza la práctica y explica el resultado. Tu compañero contrasta la comprobación con el camino que elegiste.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

<a id="referencias-oficiales"></a>

## Referencias

- [Archivos de requisitos de pip](https://pip.pypa.io/en/stable/reference/requirements-file-format/).
- [Qué registra pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/).
- [Entornos de Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).
- [Lockfiles y sincronización de uv](https://docs.astral.sh/uv/concepts/projects/sync/).

<a id="siguiente-lección"></a>

## Siguiente paso

Después del lab y su comprobación, continúa con [00.06 — Tu primer notebook](../06_first_notebook/README.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](../06_first_notebook/README.md)

[Volver a la entrada de 00.05](README.md).

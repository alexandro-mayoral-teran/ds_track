# 00.05A — Preparar y usar un entorno

<a id="05a--preparar-y-usar-un-entorno"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.05A**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Preparar un entorno y comprobar su intérprete |
| **Necesitas** | El primer script y las bases de terminal de 00.02; la elección del gestor viene al final |
| **Evidencia** | Comprobación y nota personal de la sesión A |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/00_getting_started/05_environment/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

[← Entrada de 00.05](README.md) · [Sesión A](environment.md) · [Sesión B](dependencies.md)

## Propósito

Comprender por qué separar las dependencias de los proyectos y qué piezas
intervienen al ejecutar un programa. Después elegirás una herramienta, prepararás
su entorno y comprobarás qué intérprete ejecuta el primer script.

## Antes de empezar

Lee la [entrada de 00.05](README.md) y retoma el [primer script](../04_first_script/README.md).
Lee primero los conceptos comunes de esta página. No necesitas elegir ni instalar
un gestor para comprenderlos. Para la práctica necesitarás Python 3.11 o posterior,
o una herramienta que lo prepare; el recorrido elegido explicará esa preparación.
La instalación de la biblioteca de demostración corresponde a 05B.

## Qué vas a aprender

- Explicar qué problema resuelve separar los entornos.
- Distinguir intérprete, biblioteca, dependencia y entorno.
- Elegir Conda, venv + pip o uv según tu preparación.
- Comprobar la ruta de Python y ejecutar el primer script en ese entorno.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Conda](conda.md) | Preparar el entorno si eliges Anaconda | Después de los conceptos comunes |
| [venv + pip](venv-pip.md) | Preparar un entorno con Python disponible | Después de los conceptos comunes |
| [uv](uv.md) | Preparar el mini proyecto de práctica | Después de los conceptos comunes |
| [Primer script](../04_first_script/first_summary.py) | Ejecutar un cálculo sin bibliotecas externas | Sesión A |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

## 1. Por qué necesitamos un entorno

En [00.04](../04_first_script/README.md), Python ejecutó tu cálculo con las
operaciones que ya incluye. Ahora queremos presentar unas ventas como tabla.
Podríamos escribir el formato a mano, pero una biblioteca llamada `tabulate`
ya ofrece esa funcionalidad. Para usarla, el Python que ejecuta el programa
debe tenerla disponible.

Imagina que tienes dos trabajos: una tabla de ventas y un reporte que recibiste
de otra persona. El primero se comprobó con una versión de una biblioteca y el
segundo necesita otra. Si ambos usan la misma instalación y cambias esa biblioteca,
puedes afectar al trabajo anterior aunque su archivo `.py` siga igual.
Es un ejemplo del problema; no vamos a provocar ese conflicto en tu computadora.

Separar sus entornos permite mantener los paquetes de cada trabajo y comprobar
con qué Python se ejecuta cada uno. También ayuda cuando retomas semanas después
o compartes el código: necesitas saber qué software lo acompañaba.

> **Para conversar:** si conservas el archivo `.py`, ¿qué más necesitarías saber
> para ejecutarlo en otra computadora?

<a id="1-intérprete-bibliotecas-y-dependencias"></a>

## 2. Las piezas de cualquier recorrido

El **intérprete** es el programa que ejecuta las instrucciones de Python. El
archivo `ventas.py` contiene instrucciones; el ejecutable de Python las procesa.
En una computadora puede haber varios intérpretes, con versiones o paquetes distintos.

Una **biblioteca** reúne funcionalidad reutilizable. Python incluye una
**biblioteca estándar**, por ejemplo `sys`, que permite consultar información
del intérprete. Una biblioteca **externa**, como `tabulate`, se instala aparte.
Para descargarla e instalarla utilizamos un **paquete distribuido**: en este
caso también se llama `tabulate`.

Cuando tu programa necesita ese software, lo llamamos una **dependencia**.
Su **versión** identifica una edición concreta. En esta práctica utilizaremos
`tabulate` 0.9.0 para contrastar la misma demostración en todos los caminos.
La versión de Python y la de tabulate pertenecen a programas diferentes.

```text
Tu archivo .py contiene instrucciones
        ↓ lo ejecuta
Un intérprete de Python
        ↓ utiliza
Su biblioteca estándar y los paquetes externos disponibles en su entorno
```

El **gestor** es la herramienta que ayuda a preparar o administrar ese software.
Algunas herramientas crean entornos; otras instalan paquetes; algunas combinan
varias funciones. Por eso elegir un gestor viene después de entender las piezas.

<details>
<summary>Ampliación: dependencias directas y transitivas</summary>

Una dependencia es **directa** cuando tu proyecto la solicita, como tabulate
para presentar la tabla. Es **transitiva** cuando otra dependencia la necesita.
Un gestor puede instalarla para satisfacer ese requisito. No todas las
bibliotecas tienen dependencias externas; este ejemplo no implica que tabulate
necesite instalar otras.

</details>

<a id="3-cómo-funciona-un-entorno-y-para-qué-sirve"></a>

## 3. Qué reúne un entorno y qué separa

Un **entorno** proporciona un intérprete y un espacio de paquetes para ejecutar
un trabajo. Según la herramienta, puede basarse en un Python existente o incluir
uno administrado por ella. Los paquetes externos se instalan en ese espacio.

```text
Proyecto A: código y datos → Python del entorno A → paquetes de A
Proyecto B: código y datos → Python del entorno B → paquetes de B
```

**La carpeta del código y el entorno cumplen funciones distintas.** Tu script
puede permanecer en la carpeta del proyecto y ejecutarse con el Python del
entorno. Crear o activar un entorno no mueve el script ni copia tus datos.
Algunos entornos están dentro del proyecto; otros se guardan en otra ubicación.
No guardes tus scripts dentro de la carpeta de paquetes del entorno.

Esto aporta:

- **Separación:** los paquetes instalados para un entorno no se añaden al otro.
- **Identificación:** puedes consultar el Python y las versiones que usas.
- **Reconstrucción:** puedes preparar el entorno de nuevo desde requisitos guardados.

Ocupa espacio y requiere mantenimiento. No es una máquina virtual ni una barrera
de seguridad: un programa ejecutado conserva acceso a los archivos que permitan
tus permisos. Tampoco garantiza resultados idénticos por sí solo; importan el
código, los datos, las versiones y la plataforma.

No crearemos un entorno por lección. El elegido puede acompañarte en DS Track;
la demostración de uv usará un mini proyecto aparte para conservar intacta la
configuración compartida del repositorio.

<a id="4-crear-activar-y-comprobar-un-entorno"></a>

## 4. Crear, seleccionar, instalar y comprobar

Estas acciones aparecen en cualquier recorrido, aunque una herramienta pueda
resolver varias con un comando:

| Acción | Qué significa | Qué observarás en la práctica |
| --- | --- | --- |
| Crear o preparar | Disponer del intérprete y del espacio de paquetes | Un entorno con nombre o carpeta identificable |
| Seleccionar para ejecutar | Usar el Python de ese entorno | La ruta del ejecutable que ejecuta el programa |
| Instalar | Añadir un paquete al entorno elegido | El gestor informa qué versión está disponible allí |
| Importar | Pedir desde el código la funcionalidad que utilizará | El Python elegido puede cargarla |
| Comprobar | Contrastar entorno, importación y resultado | Ruta, versión y tabla esperadas |

**Crear se hace una vez; seleccionar se repite al retomar.** Abrir otra terminal
no borra el entorno. Sin embargo, esa terminal puede seleccionar un Python
diferente. Antes de ejecutar, comprueba cuál estás usando.

### Activar es una forma de seleccionar

**Activar** prepara la sesión actual del shell para que comandos como `python`
utilicen el entorno. No cambia el código ni instala bibliotecas. La activación
no tiene que mantenerse al cerrar la terminal.

También puedes indicar directamente la ruta del ejecutable o utilizar un comando
que ejecute dentro del proyecto. En Conda activaremos el entorno, con venv usaremos
su ejecutable y con uv utilizaremos `uv run`. Los comandos completos están en
los recorridos; todavía no hace falta ejecutarlos.

### Cómo reconocer el intérprete

Una vez que el recorrido haya seleccionado su Python, consultarás:

```text
python -c "import sys; print(sys.executable)"
```

Lectura del comando: `-c` pide a Python ejecutar el texto entre comillas;
`import sys` carga una parte de su biblioteca estándar, y `print(sys.executable)`
muestra la ruta del ejecutable actual. No instala paquetes.
Con una ruta directa o con uv cambia el comienzo del comando; la consulta
entre comillas es la misma.

Ejemplos ilustrativos de salida, no rutas que debas copiar:

```text
Windows: C:\practicas\ds_track\.venv-practice\Scripts\python.exe
Linux/macOS: /home/estudiante/ds_track/.venv-practice/bin/python
```

En Windows los ejecutables de venv suelen estar en `Scripts`; en Linux/macOS,
en `bin`. El recorrido Conda mostrará la ubicación de su entorno `ds-track`;
el de uv, la `.venv` del mini proyecto. Compara la ruta con la ubicación del
entorno que preparaste, no solo con el nombre que aparece en la terminal.

> **Predice:** si instalas tabulate para el Python del entorno A y ejecutas
> con el del entorno B, ¿puedes asegurar que podrá importarlo?

<details>
<summary>Ver explicación</summary>

No. La instalación en A no instala el paquete en B. B podría tener su propia
instalación o no tenerla. Por eso comprobamos el intérprete, la versión importada
y el resultado, en lugar de concluir que «ya está instalado en la computadora».

</details>

## 5. Conservar los requisitos para reconstruir

Al compartir un script que utiliza una biblioteca externa, otra persona necesita
el código y una indicación de qué software preparar. Guardamos esa indicación
en **archivos de configuración**: texto que las herramientas pueden leer para
preparar el entorno. Documentamos también la versión de Python.

Un **requisito** expresa qué necesita el proyecto, por ejemplo una biblioteca y
su versión. La **resolución** es la selección de versiones compatibles para esos
requisitos y sus dependencias. Un **lockfile** conserva una resolución; su alcance
depende de la herramienta y no sustituye los datos ni los requisitos del sistema.
En 05B leerás los archivos concretos de tu camino.

```text
Código + datos + configuración revisada
        ↓ preparar el entorno e instalar lo declarado
Ejecutar y comprobar en la nueva ubicación
```

Compartimos esos archivos en lugar de copiar la carpeta completa del entorno,
que puede contener rutas y componentes ligados al equipo original.
No necesitas memorizar todavía los formatos. Antes de elegir una herramienta,
lo esencial es poder explicar por qué guardar el script por sí solo puede ser
insuficiente.

<a id="5-qué-aporta-cada-camino"></a>

## 6. Elegir tu recorrido

Ahora las herramientas responden a necesidades que ya conoces. Completa un solo
camino en las partes A y B; no necesitas dominar los tres para continuar.

| Camino | Qué administra aquí | Cuándo elegirlo |
| --- | --- | --- |
| [Conda](conda.md) | Entornos, intérprete de Python y paquetes de sus canales | Si ya utilizas Anaconda, es el comienzo recomendado |
| [venv + pip](venv-pip.md) | venv crea el entorno a partir de un Python disponible; pip instala paquetes para él | Si tienes Python y quieres practicar con sus herramientas estándar |
| [uv](uv.md) | Puede obtener Python, preparar el entorno y gestionar requisitos y lockfile | Si quieres trabajar con configuración y resolución integradas |

**Si tienes dudas, elige con quien te acompaña según lo que ya esté instalado.**
Para esta lección los tres caminos permiten comprobar lo mismo: el Python elegido
ejecuta el primer script y después importa tabulate para presentar una tabla.
DS Track requiere Python 3.11 o posterior; Conda y uv usarán 3.12 en esta práctica.

<a id="2-qué-es-pip-y-qué-cambia-con-uv"></a>

<details>
<summary>Comparación de herramientas para consultar después de elegir</summary>

- **Conda** obtiene paquetes de canales y puede administrar componentes binarios
  que necesitan algunas bibliotecas. Su disponibilidad depende de la plataforma
  y los canales. En este ejercicio usaremos Conda para instalar tabulate.
- **venv** utiliza una instalación de Python existente; no descarga otra versión.
  **pip** instala paquetes desde índices como PyPI. PyPI es el catálogo;
  pip es la herramienta que lo consulta. `python -m pip` ejecuta el pip asociado
  a ese Python. pip no crea el entorno ni instala Python por sí solo.
- **uv** gestiona aquí un proyecto con `pyproject.toml` y `uv.lock`. Usaremos
  `add`, `sync` y `run`. También ofrece una interfaz `uv pip`, pero no es el
  programa pip ni la necesitamos para este recorrido. Una sincronización exacta
  puede retirar paquetes que no estén declarados.

Ninguna opción garantiza por sí sola que cualquier proyecto funcione en cualquier
plataforma. Cada recorrido explica cómo conservar sus requisitos y sus límites.

</details>

Abre tu recorrido y completa **solo la parte A** y contrástala con la sesión A del lab.
En 05B instalarás la biblioteca. Conserva el mismo camino para ambas partes y
comprueba entornos existentes antes de crear otro. Evita mezclar gestores en el
mismo entorno o instalar los ejercicios en el Python global o en `base` de Conda.

## 7. Gestionar la elección del entorno en VS Code

<details>
<summary>Apoyo opcional: seleccionar en VS Code el entorno que ya preparaste</summary>

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
   el intérprete seleccionado. Si no coincide, consulta el recorrido elegido y utiliza su forma de ejecución.
4. La comprobación de bibliotecas se realizará en la parte 05B.

Seleccionar el intérprete del editor no cambia automáticamente todas las
terminales abiertas. Si el botón de ejecución funciona pero tu comando no,
compara ambas rutas. En el flujo uv, `uv run` elige el proyecto según la ubicación;
seleccionar un intérprete en VS Code no cambia ese proyecto.

En la próxima lección elegiremos además el kernel de un notebook. Consulta la
[guía de VS Code](../../../docs/vscode-guide.md) para sus paneles y atajos.

</details>

<a id="práctica-y-siguiente-paso"></a>

## Práctica

Realiza el [lab 00.05](../../../labs/00_getting_started/05_environment/README.md) para realizar la sesión A y la parte A del recorrido elegido.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Nota con gestor y ruta del intérprete | El primer script corre con el Python elegido | Qué separa el entorno y cómo identificaste su ejecutable |

Puedes continuar a 05B cuando identifiques la ruta del intérprete y ejecutes
el primer script en ese entorno. Conserva el mismo camino para la segunda sesión.

Quien aprende realiza la práctica y explica el resultado. Tu compañero contrasta la comprobación con el camino que elegiste.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

## Glosario

| Término | En esta lección |
| --- | --- |
| Intérprete | Ejecutable que procesa el programa Python |
| Biblioteca y paquete distribuido | Funcionalidad reutilizable y software que el gestor instala para disponer de ella |
| Dependencia | Software que el proyecto necesita para funcionar |
| Versión | Edición concreta de Python o de un paquete |
| Entorno | Intérprete y espacio de paquetes seleccionados para un trabajo |
| Gestor | Herramienta que prepara o administra entornos, intérpretes o paquetes |
| Activación | Preparación del shell actual para utilizar los comandos del entorno |
| Configuración y lockfile | Declaración de requisitos y archivo que conserva una resolución de dependencias |

<a id="referencias-oficiales"></a>

## Referencias

- [Entornos de Python](https://docs.python.org/3/library/venv.html).
- [pip y entornos](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
- [Conda y uso de pip](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).
- [Proyectos con uv](https://docs.astral.sh/uv/guides/projects/).
- [Sincronización y lockfiles](https://docs.astral.sh/uv/concepts/projects/sync/).
- [Entornos Python en VS Code](https://code.visualstudio.com/docs/python/environments).
- [De pip a proyectos uv](https://docs.astral.sh/uv/guides/migration/pip-to-project/).

## Siguiente paso

Después del lab y su comprobación, continúa con [00.05B — Instalar y conservar dependencias](dependencies.md).

[← Módulo 00](../README.md) · [Lab 00.05](../../../labs/00_getting_started/05_environment/README.md) · [Siguiente →](dependencies.md)

[Volver a la entrada de 00.05](README.md).

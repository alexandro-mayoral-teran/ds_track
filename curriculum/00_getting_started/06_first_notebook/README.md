# 00.06 — Tu primer notebook

<a id="06--tu-primer-notebook"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.06**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Relacionar explicación, código y resultados con un kernel comprobado |
| **Necesitas** | Entorno de 00.05, editor de notebooks y soporte de kernel del recorrido |
| **Evidencia** | Notebook modificado, reiniciado y ejecutado completo; nota de comprobación |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/00_getting_started/06_first_notebook/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-objetivos"></a>

## Propósito

Combinar explicación, código y resultados en un documento que puedas ejecutar
y comprender, con el kernel correcto y resultados reconstruidos desde cero.

Si utilizaste el cuaderno opcional de
[00.02 — Terminal y rutas](../02_terminal_paths/README.md), allí ejecutaste un
material preparado para practicar comandos. Ahora aprenderás cómo funciona un
notebook, cómo modificar sus celdas y cómo comprobar su ejecución desde cero.
Si no lo utilizaste, puedes comenzar aquí sin realizar ese ensayo previo.

## Antes de empezar

Completa [00.05 — Entornos y dependencias](../05_environment/README.md) y conserva
el entorno elegido. Esta lección usa VS Code con las extensiones **Python** y
**Jupyter**, publicadas por Microsoft. Consulta la
[guía del editor](../../../docs/vscode-guide.md). No necesitas pandas ni
conocimientos avanzados de Python. Prepara solo el soporte de kernel que
corresponde a tu entorno siguiendo el apartado 2; no repitas los tres caminos.

## Qué vas a aprender

- Distinguir celdas de texto y código y explicar el papel del kernel.
- Seleccionar el entorno y comprobarlo desde el notebook.
- Agregar una predicción y un cálculo con entradas explícitas.
- Reiniciar y ejecutar todo para contrastar los resultados sin estado previo.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Notebook de ejemplo](first_notebook.ipynb) | Abrir celdas de texto y código y comprobar el intérprete | Para el recorrido |
| [Guía de VS Code](../../../docs/vscode-guide.md) | Consultar paneles y atajos del editor utilizado | Apoyo opcional |

Abre cada recurso cuando aparezca en el recorrido. Conserva los originales y
trabaja las modificaciones en tu copia personal.

## 1. Qué es un notebook

Imagina que quieres probar una venta, anotar cuánto esperas obtener y explicar
el resultado junto al cálculo. Después quieres cambiar las unidades y comparar.
Un notebook permite reunir esas explicaciones, el código y sus salidas en un
documento, y ejecutar una parte mientras exploras.

Un notebook Jupyter es un documento `.ipynb` organizado en celdas. Puede contener
texto, código y salidas. Una **celda** es un bloque que puedes editar por separado.
En las celdas de texto escribes Markdown; en las de código escribes Python.

| Elemento | Qué hace |
| --- | --- |
| Celda Markdown | Explica el objetivo, una decisión o un resultado |
| Celda de código | Envía instrucciones al kernel para ejecutarlas |
| Salida | Muestra texto, tablas o gráficas producidas por una celda |
| Kernel | Proceso que ejecuta el código y mantiene sus variables en memoria |
| Entorno | Python y paquetes disponibles para ese kernel |

Las celdas Markdown usan lo aprendido en [00.01](../01_github_profile/README.md). El kernel de Python
utiliza un intérprete de uno de tus entornos: elegir otro puede cambiar qué
bibliotecas están disponibles.

### Documento, editor, kernel y entorno

**Jupyter** es el proyecto que proporciona herramientas y protocolos para
trabajar con estos documentos. **VS Code** es el editor que utilizaremos aquí
para abrirlos. El documento conserva las celdas y puede guardar sus salidas;
el **kernel** es el proceso en ejecución que recibe el código. En esta práctica,
ese proceso utiliza el intérprete y los paquetes del entorno elegido en 00.05.

```text
VS Code abre tu archivo .ipynb
        ↓ envías una celda de código
El kernel la ejecuta con el Python y los paquetes de tu entorno
        ↓ devuelve un resultado
VS Code muestra la salida debajo de la celda
```

El kernel conserva **variables**: nombres asociados a valores, como `unidades`
asociado a 3. A ese conjunto de valores y otros objetos que siguen disponibles
lo llamamos **estado en memoria**. El archivo y esa memoria son cosas distintas:
puedes guardar el documento aunque el cálculo todavía no se haya ejecutado.

<details>
<summary>Curiosidad opcional: qué contiene un archivo .ipynb</summary>

El archivo guarda una estructura de texto en formato JSON con celdas, metadatos
y salidas guardadas. Los metadatos describen el documento, por ejemplo el tipo
de kernel. Normalmente lo editas con un editor de notebooks; no necesitas
aprender JSON para realizar esta práctica. Guardar el archivo no conserva el
proceso del kernel ni toda su memoria.

</details>

### Script frente a notebook

Un script se ejecuta normalmente de arriba hacia abajo en un proceso nuevo.
En un notebook puedes ejecutar celdas por separado y repetirlas en otro orden;
el kernel mantiene los valores anteriores hasta que lo reinicies.

Los notebooks ayudan a explorar y explicar. Para procesos repetibles y lógica
reutilizable, después trasladaremos código a scripts y funciones cuando corresponda.

## 2. Preparar el kernel en tu entorno

VS Code necesita `ipykernel` dentro del entorno que ejecutará el notebook.
**ipykernel** es el paquete que permite que Python funcione como kernel de
Jupyter. La extensión Jupyter prepara la interfaz del editor; el paquete
prepara la ejecución en tu entorno. Son componentes distintos.

En la terminal del sistema, consulta primero el intérprete e intenta importar
ipykernel con el comando de comprobación de tu camino. Si ya está disponible,
conserva esa instalación y revisa que esté registrada; no necesitas reinstalarla.
Si falta, utiliza el comando de instalación del mismo camino de 00.05 y registra
la dependencia según sus instrucciones. No ejecutes estos comandos en una celda.

### Conda — ds-track activado

```text
# Instala el soporte de kernel en el entorno, no en base
conda activate ds-track
conda install -c conda-forge ipykernel
# Confirma qué Python y paquete utilizarás
python -c "import sys, ipykernel; print(sys.executable); print(ipykernel.__version__)"
```

Vuelve a exportar y revisar `.environment-practice/environment.yml` siguiendo el
[registro de Conda en 00.05](../05_environment/conda.md#registrar-después-de-instalar).
Conserva la configuración anterior si necesitas comparar los cambios.

### venv + pip — PowerShell

Desde la raíz de ds_track:

```powershell
# Instala en el entorno elegido sin activarlo
.\.venv-practice\Scripts\python.exe -m pip install ipykernel
# Comprueba el intérprete y el paquete
.\.venv-practice\Scripts\python.exe -c "import sys, ipykernel; print(sys.executable); print(ipykernel.__version__)"
```

### venv + pip — Bash/Zsh

```bash
./.venv-practice/bin/python -m pip install ipykernel
./.venv-practice/bin/python -c "import sys, ipykernel; print(sys.executable); print(ipykernel.__version__)"
```

Actualiza `.environment-practice/requirements.txt` desde ese entorno como
aprendiste en el [recorrido venv + pip](../05_environment/venv-pip.md#registrar-y-reconstruir).
Conserva la configuración anterior si necesitas compararla.

### uv — mini proyecto de la lección 05

Entra a `.environment-practice/uv-demo` desde la raíz. Utiliza `Set-Location`
en PowerShell o `cd` en Bash/Zsh y después:

```text
# Declara el soporte para notebooks como dependencia de desarrollo
uv add --dev ipykernel
# Comprueba el intérprete de este mini proyecto
uv run --locked python -c "import sys, ipykernel; print(sys.executable); print(ipykernel.__version__)"
```

Conserva el pyproject.toml y uv.lock actualizados. No agregues esta dependencia
a la configuración raíz por error. Para esta práctica no necesitas registrar
manualmente un kernel con --user ni ejecutar un servidor Jupyter.

> Si una instalación falla, conserva el mensaje y revisa el entorno antes de
> instalar en otra parte. Las descargas requieren Internet.

## 3. Abrir el ejemplo y elegir el kernel

### Preparar tu copia personal

1. Abre la carpeta `ds_track` en VS Code y luego el
   [notebook de ejemplo](first_notebook.ipynb).
2. Antes de editarlo, usa **Archivo → Guardar como / File → Save As** para crear
   `mi_primer_notebook.ipynb` en tu carpeta personal de práctica. Puedes usar la
   de 00.04 o crear otra; conserva el original del curriculum.
3. Comprueba la ruta de la pestaña con el cursor o desde el explorador del editor.
   Debe corresponder a tu copia personal. Si ese nombre ya existe, retoma esa
   copia o elige otro nombre para conservarla.

Mover la copia del notebook no mueve su entorno. Este ejemplo no lee archivos
externos, por lo que puede ejecutarse desde esa carpeta con el mismo kernel.

### Seleccionar y comprobar

1. En tu copia, pulsa **Select Kernel / Seleccionar kernel** en la esquina superior derecha.
2. Si hace falta, elige **Select Another Kernel → Python Environments**.
3. Selecciona ds-track, .venv-practice o el .venv del mini proyecto uv, según tu camino.
4. Si el entorno no aparece, comprueba su ruta y la detección de entornos de la
   extensión; no crees otra instalación sin revisar la que ya preparaste.

Ejecuta la primera celda de código: muestra `sys.executable`. Compáralo con la ruta de
la lección 05. La selección del intérprete para scripts no garantiza que este
notebook utilice el mismo kernel: compruébalo dentro del documento.

GitHub permite ver el notebook, pero visualizarlo allí no ejecuta sus celdas.
Descarga o clona el material y ábrelo en tu editor para practicar.

## 4. Ejecutar una celda y leer el resultado

Pulsa el botón de ejecución de una celda o **Shift+Enter** para ejecutarla y
avanzar. **Ctrl+Enter** ejecuta sin avanzar. En una celda Markdown, estas acciones
permiten mostrar el texto con formato.

Ejecuta las celdas de arriba hacia abajo. Primero se definen las entradas y
después se calcula el resultado. Los números de ejecución muestran el orden
en que se enviaron las celdas al kernel, no una posición fija del documento.

El ejemplo calcula tres cuadernos a 40 MXN: total de 120 MXN. La segunda
situación calcula cinco a ese mismo precio: 200 MXN. Cada explicación debe
coincidir con los datos y resultados del código.

## 5. Comprender el estado en memoria

Trabaja con las dos celdas de la **primera situación**: una define las entradas
y la siguiente calcula. La segunda venta tiene entradas propias y seguirá
produciendo 200 MXN.

1. Con `unidades = 3`, predice el total y ejecuta entradas y cálculo. Comprueba 120 MXN.
2. Cambia a `unidades = 4` en la celda de entradas, **sin ejecutarla**. Anota qué
   valor ves escrito y cuál esperas que el kernel conserve.
3. Antes de ejecutar solo el cálculo, predice su salida. Ejecútalo y compara.
4. Ejecuta ahora las entradas modificadas y después el cálculo. Predice y
   comprueba el nuevo total antes de abrir la explicación.

<details>
<summary>Ver explicación del experimento</summary>

| Momento | Código visible de entradas | Unidades en memoria | Salida del cálculo |
| --- | --- | --- | --- |
| Ejecutaste entradas y cálculo originales | `unidades = 3` | 3 | 120 MXN |
| Editaste y ejecutaste solo el cálculo | `unidades = 4` | 3 | 120 MXN |
| Ejecutaste entradas modificadas y cálculo | `unidades = 4` | 4 | 160 MXN |

La celda de cálculo lee los valores que el kernel tiene en memoria. Modificar el
texto de la celda de entradas no ejecuta esa asignación.

</details>

Editar no actualiza el kernel hasta ejecutar. Además, una salida guardada en el
archivo puede pertenecer a una ejecución anterior. Por eso no basta con ver un
resultado para asegurar que corresponde al código actual.

> **Para conversar:** si dos personas leen el mismo código pero ejecutan celdas
> en distinto orden, ¿podrían ver resultados diferentes?

## 6. Reiniciar y ejecutar todo

Usa **Restart / Reiniciar kernel** y después **Run All / Ejecutar todo** desde
la barra del notebook. Confirma el reinicio si se solicita. Si el menú ofrece
reiniciar y ejecutar todas las celdas en una acción, puedes utilizarla.

- Reiniciar elimina las variables y otros estados de memoria de ese kernel.
- Ejecutar todo recorre las celdas de código desde el principio.
- Borrar salidas limpia lo mostrado, pero no borra las variables del kernel.

### Qué cambia con cada acción

| Acción | Código y archivo | Memoria del kernel | Salidas visibles |
| --- | --- | --- | --- |
| Editar una celda | Cambia el contenido en el editor; guardar lo conserva en disco | Conserva los valores anteriores | Pueden seguir mostrando resultados anteriores |
| Ejecutar una celda de código | Ejecuta su contenido actual, sin guardar necesariamente el archivo | Puede crear o cambiar valores | Actualiza las salidas de esa celda |
| Guardar | Conserva celdas y salidas actuales en el archivo | No recalcula ni reinicia | Conserva las que se guardaron |
| Borrar salidas | Retira las salidas del documento; guarda para conservar ese cambio | Conserva las variables | Desaparecen las salidas elegidas |
| Reiniciar kernel | Conserva el código editado | Elimina el estado de la sesión anterior | Pueden permanecer salidas antiguas hasta limpiarlas o ejecutar |
| Ejecutar todo | Recorre el código actual de arriba hacia abajo | Construye valores sobre la sesión actual | Actualiza las salidas conforme ejecuta |

**Reiniciar no deshace tus ediciones.** Si dejaste `unidades = 4`, reiniciar y
ejecutar todo debe producir 160 y 200 MXN. **Ejecutar todo por sí solo tampoco
asegura una memoria limpia:** por eso lo precedemos con un reinicio.
La comprobación «desde cero» se refiere aquí al estado del kernel; no vuelve a
instalar el entorno ni demuestra que cualquier otro equipo pueda reconstruirlo.

Comprueba que todas las celdas terminan sin error y que las explicaciones siguen
coincidiendo con los resultados. Guarda el notebook después de comprobarlo.
Antes de compartir, revisa que las salidas no incluyan rutas personales; la celda
del intérprete puede limpiarse tras la verificación.
Guarda otra vez después de limpiar esa salida para que el archivo compartido
conserve la limpieza. La ruta completa puede quedar en tu nota personal local.

## 7. Crear tu propia celda y documentar

Agrega una celda Markdown con una predicción y una celda de código con otro
cálculo de venta. Utiliza `+ Markdown` y `+ Code` del editor. Escribe entradas
explícitas para que la nueva celda pueda entenderse al ejecutar desde cero.

No instales paquetes desde las celdas de este primer ejemplo: gestiona las
dependencias desde el recorrido elegido para conservar su configuración.

## Pausar y retomar tu notebook

Antes de pausar, guarda tu copia y anota su ruta, el entorno/kernel comprobado,
los resultados observados, la duda pendiente y el siguiente paso. No necesitas
resolver toda la lección en una sesión.

Al retomar:

1. Abre tu copia personal y revisa su ruta.
2. Selecciona el kernel del entorno que ya preparaste; no crees otro por cambiar de día.
3. Reinicia y ejecuta todo desde el principio. Comprueba el intérprete y los
   totales con tus entradas actuales.
4. Continúa cuando el resultado coincida con tu explicación. Si falla, conserva
   el mensaje y revisa la primera celda que no pudo ejecutarse.

Una salida que aparece al abrir puede estar guardada de otra sesión. Abrir o
guardar el notebook no demuestra que lo hayas ejecutado en la sesión actual.

## Cuando algo no funciona

| Situación | Qué revisar |
| --- | --- |
| No se puede ejecutar | Kernel seleccionado, extensión Jupyter e ipykernel |
| NameError tras reiniciar | Si ejecutaste la celda que define la variable |
| La salida no refleja la edición | Si ejecutaste de nuevo las celdas necesarias |
| Falta una biblioteca ya instalada | sys.executable y el entorno del kernel |
| Funciona manualmente pero no con Run All | Dependencias entre celdas o estado de ejecuciones anteriores |

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 00.06](../../../labs/00_getting_started/06_first_notebook/README.md) para crear celdas y reconstruir sus resultados desde una sesión limpia.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu notebook con una predicción y el cálculo nuevo | Kernel correcto y resultados tras reiniciar y ejecutar todo | Por qué el estado en memoria puede ocultar celdas pendientes |
| Nota con ruta del intérprete y resultados | Coincidencia con el entorno elegido en 00.05 | Diferencia entre seleccionar intérprete para scripts y kernel del notebook |

Puedes avanzar cuando selecciones el kernel correcto, modifiques una celda,
expliques el estado en memoria y reconstruyas los resultados con reinicio y Run All.
Revisa también las evidencias de scripts, entorno y documentación del módulo.

Quien aprende realiza la práctica y explica el resultado. Tu compañero pide reiniciar y ejecutar todo y contrastar la predicción con la salida obtenida.
Guarda evidencia y dudas en tu copia de la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o en una nota propia. PROGRESS.md registra el desarrollo editorial del curso.
Todavía no hay proyecto de datos ni checkpoint asociado a esta lección.

## Glosario

| Término | Significado en esta práctica |
| --- | --- |
| Notebook o cuaderno | Documento que combina explicaciones, celdas de código y salidas |
| `.ipynb` | Extensión del archivo de notebook Jupyter |
| Jupyter | Proyecto de herramientas y protocolos para trabajar con notebooks y kernels |
| Editor | Aplicación donde abres y modificas el documento; aquí usamos VS Code |
| Celda | Bloque del notebook que se edita por separado |
| Markdown | Formato de texto para escribir explicaciones con títulos, listas y otros elementos |
| Kernel | Proceso que recibe y ejecuta el código y mantiene su estado en memoria |
| ipykernel | Paquete que permite utilizar Python como kernel de Jupyter |
| Intérprete | Ejecutable de Python que utiliza el kernel para procesar el código |
| Entorno | Intérprete y conjunto de paquetes disponibles para ejecutar la práctica |
| Variable | Nombre asociado a un valor, como `unidades` asociado a 3 |
| Estado en memoria | Valores y objetos que conserva el kernel durante la sesión |
| Salida | Texto u otro resultado que una celda produjo y que puede quedar guardado |
| Contador de ejecución | Número que indica el orden de envío de una celda al kernel durante una sesión |
| Reiniciar | Iniciar de nuevo el kernel para eliminar el estado de la sesión anterior |
| Ejecutar todo / Run All | Ejecutar las celdas de código en el orden del documento |

<a id="referencias-oficiales"></a>

## Referencias

- [Notebooks en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
- [Selección de kernels](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).
- [uv con Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/).

## Siguiente paso

Después del lab y su comprobación, continúa con [01 — Python fundamental](../../01_python_foundations/README.md).

[← Módulo 00](../README.md) · [Lab 00.06](../../../labs/00_getting_started/06_first_notebook/README.md) · [Siguiente →](../../01_python_foundations/README.md)

Python fundamental ya dispone de sus seis lecciones y labs; empieza por 01.01
desde su índice. El material disponible no acredita prácticas completadas.

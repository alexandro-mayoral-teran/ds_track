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

Un notebook Jupyter es un documento `.ipynb` organizado en celdas. Puede contener
texto, código y salidas. Su archivo guarda una estructura JSON: normalmente lo
editas con un visor de notebooks, no como texto JSON.

| Elemento | Qué hace |
| --- | --- |
| Celda Markdown | Explica el objetivo, una decisión o un resultado |
| Celda de código | Envía instrucciones al kernel para ejecutarlas |
| Salida | Muestra texto, tablas o gráficas producidas por una celda |
| Kernel | Proceso que ejecuta el código y mantiene sus variables en memoria |
| Entorno | Python y paquetes disponibles para ese kernel |

Las celdas Markdown usan lo aprendido en la lección 01. El kernel de Python
utiliza un intérprete de uno de tus entornos: elegir otro puede cambiar qué
bibliotecas están disponibles.

### Script frente a notebook

Un script se ejecuta normalmente de arriba hacia abajo en un proceso nuevo.
En un notebook puedes ejecutar celdas por separado y repetirlas en otro orden;
el kernel mantiene los valores anteriores hasta que lo reinicies.

Los notebooks ayudan a explorar y explicar. Para procesos repetibles y lógica
reutilizable, después trasladaremos código a scripts y funciones cuando corresponda.

## 2. Preparar el kernel en tu entorno

VS Code necesita `ipykernel` dentro del entorno que ejecutará el notebook.
La extensión Jupyter del editor no sustituye ese paquete. Elige solo el camino
de la lección 05 y registra la nueva dependencia según sus instrucciones.

### Conda — ds-track activado

```text
# Instala el soporte de kernel en el entorno, no en base
conda activate ds-track
conda install -c conda-forge ipykernel
# Confirma qué Python y paquete utilizarás
python -c "import sys, ipykernel; print(sys.executable); print(ipykernel.__version__)"
```

Vuelve a exportar y revisar environment.yml después de instalar.

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

Actualiza tu requirements.txt desde ese entorno como aprendiste en 05B.

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

1. Abre la carpeta `ds_track` en VS Code y luego
   [first_notebook.ipynb](first_notebook.ipynb).
2. Pulsa **Select Kernel / Seleccionar kernel** en la esquina superior derecha.
3. Si hace falta, elige **Select Another Kernel → Python Environments**.
4. Selecciona ds-track, .venv-practice o el .venv del mini proyecto uv, según tu camino.
5. Si el entorno no aparece, comprueba su ruta y la detección de entornos de la
   extensión; no crees otra instalación sin revisar la que ya preparaste.

La primera celda de código muestra `sys.executable`. Compáralo con la ruta de
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

1. Ejecuta las entradas y el cálculo.
2. Cambia `unidades = 3` por `unidades = 4` en la celda de entradas, sin ejecutarla.
3. Ejecuta solo la celda del cálculo: seguirá usando el valor anterior en memoria.
4. Ejecuta la celda de entradas y después el cálculo: ahora el total es 160 MXN.

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

Comprueba que todas las celdas terminan sin error y que las explicaciones siguen
coincidiendo con los resultados. Guarda el notebook después de comprobarlo.
Antes de compartir, revisa que las salidas no incluyan rutas personales; la celda
del intérprete puede limpiarse tras la verificación.

## 7. Crear tu propia celda y documentar

Agrega una celda Markdown con una predicción y una celda de código con otro
cálculo de venta. Utiliza `+ Markdown` y `+ Code` del editor. Escribe entradas
explícitas para que la nueva celda pueda entenderse al ejecutar desde cero.

No instales paquetes desde las celdas de este primer ejemplo: gestiona las
dependencias desde el recorrido elegido para conservar su configuración.

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

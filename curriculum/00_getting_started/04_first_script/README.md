# 04 — Tu primer script Python

## Propósito

Ejecutar un programa pequeño, comprender qué hace y modificarlo para obtener
otro resultado. Conectaremos la terminal con un cálculo de datos ficticios.

## Prerrequisitos

- Haber practicado rutas y comandos en la lección 02.
- Tener un editor de texto y Python 3 instalado.
- Git es opcional para conservar la modificación, como aprendiste en la lección 03.

Comprueba `python --version` o `python3 --version`. Si ninguno funciona, puedes
leer la explicación y predecir los resultados, pero la ejecución queda pendiente
hasta preparar Python. Consulta la [descarga oficial](https://www.python.org/downloads/)
con quien te acompaña. La instalación y los entornos se desarrollarán en la
lección 05. Este ejemplo no necesita pip, uv ni paquetes adicionales.

## Objetivos

Si usarás VS Code, consulta la [guía del editor](../../../docs/vscode-guide.md)
para abrir el proyecto, guardar archivos y utilizar la terminal integrada.

- Distinguir un archivo `.py`, el editor y el intérprete de Python.
- Ejecutar un script desde la raíz del proyecto.
- Reconocer datos de entrada, un cálculo y la salida.
- Cambiar un valor, predecir el resultado y comprobarlo.

## 1. Qué es Python y qué es un script

Python es un lenguaje de programación. Escribes instrucciones en un archivo
de texto y el intérprete de Python las ejecuta. Un **script** es un programa
que puedes ejecutar; `.py` es la extensión habitual de su código fuente.

| Elemento | Su papel en esta práctica |
| --- | --- |
| Editor | Escribir y guardar el código |
| Archivo `first_summary.py` | Conservar las instrucciones |
| Terminal | Pedir la ejecución y ver su resultado |
| Intérprete `python` | Leer y ejecutar las instrucciones |

Guardar el archivo no ejecuta el programa. Ejecutarlo tampoco crea un commit:
son acciones distintas, como guardar y publicar el README en la lección anterior.

## 2. Leer el ejemplo antes de ejecutarlo

Abre [first_summary.py](first_summary.py). Estos son sus pasos:

```python
# Datos de entrada
producto = "cuaderno"
unidades = 3
precio_unitario_mxn = 40

# Transformación
importe_mxn = unidades * precio_unitario_mxn

# Salida
print(f"Importe total: {importe_mxn} MXN")
```

Una **variable** da un nombre a un valor. `=` asigna ese valor; no representa una
pregunta de igualdad. El texto va entre comillas y los números de este ejemplo
se escriben sin comillas. `*` multiplica. Las líneas con `#` son comentarios.

`print(...)` muestra información. En una cadena con prefijo `f`, las llaves
insertan valores: `{importe_mxn}` se reemplaza por el resultado del cálculo.
El programa ejecuta estas instrucciones en orden, de arriba hacia abajo.

Aquí las entradas están escritas dentro del código; todavía no leemos un CSV
ni solicitamos datos al usuario. Cada ejecución usa esos valores y calcula de nuevo.

> **Antes de ejecutar:** ¿cuánto debería valer `importe_mxn`? ¿Qué unidad tiene?

## 3. Ejecutar desde la terminal

### PowerShell

Desde la raíz de `ds_track`:

```powershell
# Confirma tu ubicación
Get-Location
# Comprueba que el script existe
Test-Path curriculum\00_getting_started\04_first_script\first_summary.py
# Ejecuta el archivo con Python
python curriculum\00_getting_started\04_first_script\first_summary.py
```

### Bash/Zsh

Desde la raíz de `ds_track`:

```bash
# Confirma tu ubicación
pwd
# Comprueba el archivo
test -e curriculum/00_getting_started/04_first_script/first_summary.py && echo "existe"
# Ejecuta el archivo con Python
python3 curriculum/00_getting_started/04_first_script/first_summary.py
```

Si tu instalación utiliza `python` en lugar de `python3`, sustituye el nombre
del ejecutable. El código del archivo es el mismo en ambos sistemas.

### Resultado esperado

```text
Mi primer resumen de datos
Producto: cuaderno
Unidades: 3
Precio unitario: 40 MXN
Importe total: 120 MXN
```

El script muestra texto en la terminal. No crea un archivo de resultados ni
modifica el CSV de la lección 02.

## 4. Modificar, guardar y comprobar

1. Cambia `unidades = 3` por `unidades = 5` en el editor.
2. Predice el nuevo importe antes de ejecutar.
3. Guarda el archivo y repite el comando de tu shell.
4. Comprueba que ahora aparecen cinco unidades y un importe de 200 MXN.

Modifica un valor a la vez para relacionar causa y resultado. Un cálculo que
termina sin error también puede estar equivocado: compáralo con tu predicción.

## 5. Leer un error sin perder el hilo

| Situación | Qué revisar |
| --- | --- |
| Comando no reconocido | Si Python está instalado y qué nombre tiene |
| `can't open file` | Ubicación, ruta y nombre del archivo |
| `SyntaxError` | La línea indicada: comillas, paréntesis y otros signos |
| `NameError` | Si escribiste el mismo nombre de variable y lo definiste antes |
| Sigue apareciendo el resultado anterior | Si guardaste el archivo y ejecutaste la copia correcta |

Como experimento, cambia una vez `unidades` por `unidadess` en la línea del
cálculo. Ejecuta, identifica el error y corrige el nombre. Vuelve a ejecutar
para confirmar que recuperaste el resultado esperado.

## 6. De este ejemplo a la manipulación de datos

El patrón es **entrada → transformación → salida**. Más adelante las entradas
vendrán de CSV o bases de datos, las transformaciones operarán sobre muchos
registros y las salidas podrán ser tablas o reportes. Primero necesitamos poder
ejecutar y explicar un cálculo pequeño.

El verificador de la lección 02 es otro script, pero incorpora funciones,
importaciones y búsqueda de rutas. Por ahora observa que también termina
mostrando información; estudiaremos esos conceptos en Python fundamental.

## Práctica y criterio de salida

Realiza el [lab 00.04 — Primer script](../../../labs/00_getting_started/04_first_script/README.md).
Puedes avanzar cuando ejecutes el script, modifiques sus entradas, compruebes
el cálculo y expliques entrada, transformación y salida con tus palabras.
La evidencia es tu script modificado; todavía no hay proyecto asociado.

## Siguiente lección

05 — Entorno y dependencias (por desarrollar): instalación de Python, entornos,
pip y uv. Consulta el [índice del nivel 0](../README.md).

## Referencias

- [Introducción a Python](https://docs.python.org/es/3/tutorial/introduction.html).
- [Uso del intérprete](https://docs.python.org/es/3/tutorial/interpreter.html).

# 01.01 — Variables, tipos y operaciones

<a id="01--variables-tipos-y-operaciones"></a>

[Inicio](../../../README.md) / [Módulo 01](../README.md) / **Lección 01.01**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Interpretar valores y comprobar un cálculo con tipos y unidades claros |
| **Necesitas** | Entorno de Python del módulo 00; biblioteca estándar |
| **Evidencia** | Script adaptado y nota con entradas, tipos, predicción y resultado |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/01_python_foundations/01_variables_types/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Comprender cómo Python representa un dato y por qué su tipo cambia las
operaciones que puedes realizar. Pasaremos del primer cálculo del módulo 00
a interpretar valores que podrían venir de un archivo.

<a id="prerrequisitos-y-objetivos"></a>

## Antes de empezar

Retoma el [primer script](../../00_getting_started/04_first_script/README.md) y
los [entornos del módulo 00](../../00_getting_started/05_environment/README.md).
Usa el entorno que elegiste, con Python y sin paquetes externos. Puedes editar
en tu editor habitual y ejecutar desde la terminal. El ejemplo define sus
entradas en el propio script: todavía no necesitas un CSV.

## Qué vas a aprender

- Asignar y reasignar variables, distinguiendo asignación de comparación.
- Reconocer texto, enteros, decimales, booleanos y ausencia mediante su tipo.
- Convertir una entrada numérica válida y explicar un error de conversión.
- Calcular un importe en MXN y contrastarlo con una predicción manual.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](variables_types.py) | Simular campos de texto de una venta, convertirlos y calcular su importe | Para el ejemplo |

Abre los archivos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y compara la salida con los resultados esperados. Para practicar,
modifica tu copia y conserva los originales.

## 1. Variables: dar nombres a los valores

```python
producto = "cuaderno"
unidades = 3
precio_unitario_mxn = 40
```

`=` asigna un valor a un nombre. Escribe nombres que expliquen qué representa
el dato; utiliza guion bajo para separar palabras. Python distingue mayúsculas:
`unidades` y `Unidades` son nombres diferentes.

```python
unidades = 3
unidades = 5
print(unidades)
```

El último valor asignado es 5. Reasignar no modifica las instrucciones anteriores
ni recalcula automáticamente resultados que ya guardaste en otra variable:

```python
unidades = 3
importe_mxn = unidades * 40
unidades = 5
print(importe_mxn)  # Sigue siendo 120
```

Para obtener 200, ejecuta otra vez el cálculo con el nuevo valor. Esto se conecta
con el estado del kernel que observaste en la
[lección 00.06 — Primer notebook](../../00_getting_started/06_first_notebook/README.md).

## 2. Tipos: qué clase de dato estás usando

| Tipo | Ejemplo | Uso inicial |
| --- | --- | --- |
| `str` | `"cuaderno"`, `"3"` | Texto, incluso si contiene dígitos |
| `int` | `3`, `40` | Cantidades enteras |
| `float` | `1.5` | Valores con parte decimal |
| `bool` | `True`, `False` | Resultado de una condición |
| Valor `None` | `None` | Ausencia de un valor; su tipo es `NoneType` |

Puedes consultar el tipo con `type(valor)`:

```python
print(type("3"))  # <class 'str'>
print(type(3))    # <class 'int'>
```

La salida usa la palabra `class` para describir el tipo. No necesitas crear
clases ni estudiar POO para entender esta comprobación.

Para datos con unidades, explícitalas: `importe_mxn` no es lo mismo que
`importe_usd`. En esta práctica los importes son enteros. Los decimales tienen
límites de precisión; profundizaremos en representación y redondeo cuando haga falta.

## 3. Texto numérico frente a número

```python
print("3" + "2")  # 32: une dos textos
print(3 + 2)      # 5: suma dos números
```

Las comillas importan. En los archivos CSV, un lector puede entregar los campos
como texto aunque parezcan números. Para calcular, primero debes interpretar su tipo:

```python
unidades_texto = "3"
unidades = int(unidades_texto)
importe_mxn = unidades * 40
print(importe_mxn)  # 120
```

`int(...)` convierte texto válido a entero. `float("1.5")` interpreta un decimal
con punto; `str(3)` produce texto. Convertir no valida todas las reglas del dato:
`int("-3")` es válido para Python, pero puede ser inválido como cantidad de una venta.

No todos los textos se convierten: `int("tres")` produce `ValueError`, y
`int("3.5")` tampoco representa un entero válido en ese formato. No intentes
resolverlo cambiando datos al azar: revisa qué recibió el programa.

## 4. Operaciones y comparaciones

| Operador | Función | Ejemplo |
| --- | --- | --- |
| `+`, `-` | Sumar o restar números | `80 + 50` |
| `*` | Multiplicar | `3 * 40` |
| `/` | Dividir; produce un float con estos enteros | `120 / 3` da `40.0` |
| `==` | Comparar igualdad | `unidades == 3` |
| `>=`, `<` | Comparar valores | `importe_mxn >= 100` |

`=` asigna; `==` compara. Una comparación produce un booleano:

```python
importe_mxn = 120
alcanza_umbral = importe_mxn >= 100
print(alcanza_umbral)  # True
```

El umbral de 100 es una regla ficticia para practicar comparaciones.
En las siguientes lecciones utilizaremos condiciones para actuar sobre comparaciones.

## 5. Mostrar y explicar el resultado

```python
print(f"{unidades} unidades de {producto}: {importe_mxn} MXN")
```

La cadena con prefijo `f` inserta valores entre llaves. `print` los muestra en
la terminal; no crea un archivo de salida. Una explicación debe indicar qué
calculaste y sus unidades, además del número.

## 6. Ejecutar el ejemplo

Lee [variables_types.py](variables_types.py) antes de ejecutar. Sus entradas
simulan campos de texto de una venta; todavía no lee un CSV.

### PowerShell

Desde la raíz de ds_track, con tu entorno activado:

```powershell
# Confirma el intérprete elegido
python -c "import sys; print(sys.executable)"
# Ejecuta el ejemplo
python curriculum\01_python_foundations\01_variables_types\variables_types.py
```

Si utilizas la ruta directa de venv, sustituye `python` por
`.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
# Desde la raíz y con el entorno seleccionado
python -c "import sys; print(sys.executable)"
python curriculum/01_python_foundations/01_variables_types/variables_types.py
```

Sin activación, utiliza `./.venv-practice/bin/python` si elegiste venv.

### uv

Desde el mini proyecto `.environment-practice/uv-demo` de la lección 05:

```text
uv run --locked python ../../curriculum/01_python_foundations/01_variables_types/variables_types.py
```

### Resultado esperado

```text
3 unidades de cuaderno: 120 MXN
Tipo de la entrada: str
Tipo después de convertir: int
¿Importe de al menos 100 MXN?: True
```

Predice los resultados cuando cambies las entradas. Anota el tipo y el valor:
conocer solo uno de ellos puede ocultar un error.
En el script, `type(valor).__name__` muestra el nombre del tipo de forma breve;
`type(valor)` permite consultar ese mismo tipo sin abreviar la presentación.

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 01.01](../../../labs/01_python_foundations/01_variables_types/README.md) para
adaptar una venta, contrastar tipos y valores y explicar una conversión que falla.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu copia del script con las variantes del lab | Tipo y valor de las entradas; importe y comparación esperados | Por qué texto y número permiten operaciones diferentes |
| Una nota con predicciones y resultados | La diferencia entre reasignar unidades y volver a calcular el importe | Qué hacen `=`, `==` y la conversión; por qué convertir no valida la venta |

Puedes avanzar cuando distingas texto de número, conviertas una entrada válida,
expliques asignación frente a comparación y compruebes el cálculo modificado.

Quien aprende modifica y ejecuta su copia, y explica lo que comprobó.
Tu compañero cambia una entrada y te pide predecir el tipo y el importe antes de ejecutar.
Guarda la evidencia, las ayudas y las dudas en una nota personal junto a tu
práctica; PROGRESS.md registra el desarrollo editorial del curso.

Todavía no hay proyecto ni checkpoint asociado a esta lección. El material
disponible no acredita por sí solo la finalización de tus prácticas.

<a id="referencia"></a>

## Referencias

- [Introducción a Python: números, texto y variables](https://docs.python.org/es/3/tutorial/introduction.html).

## Siguiente paso

Después del lab y su comprobación, continúa con
[01.02 — Listas y diccionarios](../02_lists_dicts/README.md) antes de realizar su lab.

[← Módulo 01](../README.md) · [Lab 01.01](../../../labs/01_python_foundations/01_variables_types/README.md) · [Siguiente →](../02_lists_dicts/README.md)

# 01 — Variables, tipos y operaciones

## Propósito

Comprender cómo Python representa un dato y por qué su tipo cambia las
operaciones que puedes realizar. Pasaremos del primer cálculo del nivel 0
a interpretar valores que podrían venir de un archivo.

## Prerrequisitos y objetivos

Utiliza el entorno elegido en el nivel 0. Solo necesitas Python, sin paquetes
externos. Puedes trabajar en VS Code y ejecutar desde tu terminal.
Al terminar podrás asignar variables, reconocer tipos, convertir texto numérico,
calcular un resultado y comprobarlo con una predicción.

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
con el estado del kernel que observaste en la lección de notebooks.

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

## Práctica y criterio de salida

Realiza el [lab 01.01](../../../labs/01_python_foundations/01_variables_types/README.md).
Puedes avanzar cuando distingas texto de número, conviertas una entrada válida,
expliques asignación frente a comparación y compruebes el cálculo modificado.
Todavía no hay checkpoint de proyecto asociado.

## Siguiente paso

02 — Listas y diccionarios está por desarrollar. Consulta el [índice del módulo](../README.md).

## Referencia

- [Introducción a Python: números, texto y variables](https://docs.python.org/es/3/tutorial/introduction.html).

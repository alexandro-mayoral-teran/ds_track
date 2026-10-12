# 02 — Listas y diccionarios

## Propósito y objetivos

Representar varios datos sin crear una variable distinta para cada uno.
Después de [variables y tipos](../01_variables_types/README.md), aprenderás a
acceder a posiciones y campos, modificar registros y distinguir compartir de copiar.
Usa el mismo entorno: esta lección no necesita paquetes externos.

## 1. Listas: agrupar elementos en orden

Una lista reúne elementos entre corchetes, separados por comas:

```python
productos = ["cuaderno", "lapiz", "carpeta"]
print(len(productos))  # 3 elementos
```

La lista conserva un orden y permite repetir elementos. Puede contener valores
de distintos tipos, pero conviene mantener un significado consistente para
entender tus datos. `len(...)` cuenta elementos, no suma sus valores.

### Acceder a una posición

```python
print(productos[0])   # cuaderno: primera posición
print(productos[1])   # lapiz: segunda posición
print(productos[-1])  # carpeta: última posición
```

Los índices empiezan en cero. Una lista de tres elementos tiene índices 0, 1
y 2; `productos[3]` produce `IndexError`. Una posición no es un identificador
permanente: puede cambiar cuando agregas, quitas o reordenas elementos.

### Seleccionar un tramo

```python
print(productos[0:2])  # ["cuaderno", "lapiz"]
```

Este corte, llamado slice, incluye el inicio y excluye el final. Produce otra
lista; no elimina elementos de la original.

## 2. Modificar una lista

```python
# Cambia el elemento de una posición
productos[1] = "lapiz azul"
# Agrega al final
productos.append("rotulador")
# Retira y devuelve el último elemento
retirado = productos.pop()
print(retirado)  # rotulador
```

`append` y `pop` son métodos: operaciones de ese objeto. El punto conecta la
lista con el método. `append` modifica la lista y devuelve `None`; no escribas
`productos = productos.append(...)`, porque perderías el nombre que refería a la lista.
Una lista vacía se escribe `[]`; retirar con `pop()` de una lista vacía falla.

> **Para comprobar:** ¿cuántos elementos quedan después de agregar y retirar
> el último? Predice antes de ejecutar.

## 3. Diccionarios: nombrar los campos de un registro

Una venta tiene campos con significados distintos. Un diccionario relaciona
**claves** con **valores**, usando llaves y pares separados por comas:

```python
venta = {
    "producto": "cuaderno",
    "unidades": 2,
    "precio_unitario_mxn": 40,
}
```

En este ejemplo las claves son textos. El nombre del campo permite acceder
sin recordar una posición:

```python
print(venta["producto"])  # cuaderno
importe_mxn = venta["unidades"] * venta["precio_unitario_mxn"]
print(importe_mxn)  # 80
```

Una clave es única dentro del diccionario. Asignar de nuevo a esa misma clave
reemplaza su valor; no agrega un segundo campo con igual nombre.

### Modificar y agregar campos

```python
# Cambia un campo existente
venta["unidades"] = 3
# Agrega un campo nuevo, calculado con las entradas actuales
venta["importe_mxn"] = venta["unidades"] * venta["precio_unitario_mxn"]
```

El diccionario es mutable: su contenido puede cambiar. Un campo calculado no
se actualiza solo si después cambias las unidades; debes recalcularlo, como
con las variables de la lección 01.

### Consultar una clave que puede faltar

```python
print("region" in venta)            # False: pregunta si existe la clave
print(venta.get("region"))          # None: la clave no existe
print(venta.get("region", "sin dato"))  # Valor alternativo
```

`venta["region"]` produciría `KeyError` en este registro. `get` permite consultar
con un valor alternativo; no agrega el campo ni demuestra que el registro sea válido.
Si la clave existe con valor `None`, `get` devuelve ese `None`, no el alternativo.
`in` sobre un diccionario comprueba sus claves; sobre una lista comprueba sus elementos.

`len(venta)` cuenta campos, no ventas. Un diccionario vacío se escribe `{}`.

## 4. Lista de diccionarios: varios registros

```python
ventas = [
    {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
    {"producto": "lapiz", "unidades": 5, "precio_unitario_mxn": 10},
    {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
]
```

La lista contiene tres registros. Cada diccionario describe uno:

```python
print(len(ventas))                    # 3 registros
print(ventas[0]["producto"])          # cuaderno
print(ventas[1]["unidades"])          # 5
```

Lee `ventas[0]["producto"]` en dos pasos: elige el primer diccionario y después
su campo producto. Los registros mantienen los mismos nombres de campos para
poder compararlos. En un CSV esos campos se parecerán a los nombres de columnas.

Con esta estructura todavía no filtramos ni recorremos todos los registros.
Lo haremos con condiciones y ciclos en la siguiente lección.

## 5. Referencias y copias: qué estás modificando

### Asignar otro nombre no crea una copia

```python
original = {"producto": "cuaderno", "unidades": 2}
otro_nombre = original
otro_nombre["unidades"] = 4
print(original["unidades"])  # 4: ambos nombres refieren al mismo diccionario
```

Lo mismo ocurre al asignar una lista a otro nombre. No son dos registros
independientes: estás accediendo al mismo objeto mutable.

### Copiar un registro sencillo

```python
original = {"producto": "cuaderno", "unidades": 2}
copia = original.copy()
copia["unidades"] = 4
print(original["unidades"])  # 2
print(copia["unidades"])     # 4
```

`copy()` crea otro diccionario. Aquí sus valores son texto y enteros, así que
modificar el campo de la copia no cambia el original.

### Una copia superficial no duplica los registros internos

```python
copia_ventas = ventas.copy()
copia_ventas[0]["unidades"] = 9
print(ventas[0]["unidades"])  # 9
```

La lista exterior es nueva, pero contiene los mismos diccionarios. Este detalle
importa al explorar cambios sin querer alterar los datos originales. Por ahora
copia explícitamente el registro sencillo que modificarás; copias profundas se
estudiarán cuando haya estructuras más complejas.

> **Para conversar:** ¿qué diferencia hay entre una colección nueva y registros
> nuevos dentro de esa colección?

## 6. Ejecutar el ejemplo

Lee [lists_dicts.py](lists_dicts.py), que muestra registros, un importe y una
copia independiente de una venta sencilla. Ejecútalo desde la raíz de ds_track.

### PowerShell

```powershell
# Con el entorno elegido activado
python curriculum\01_python_foundations\02_lists_dicts\lists_dicts.py
```

Sin activar venv, sustituye `python` por `.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
# Con el entorno elegido activado
python curriculum/01_python_foundations/02_lists_dicts/lists_dicts.py
```

Sin activar venv, utiliza `./.venv-practice/bin/python`.

### uv

Desde el mini proyecto `.environment-practice/uv-demo` del nivel 0:

```text
uv run --locked python ../../curriculum/01_python_foundations/02_lists_dicts/lists_dicts.py
```

Resultado esperado:

```text
Registros iniciales: 3
Primer producto: cuaderno
Importe de la primera venta: 80 MXN
Registros después de agregar: 4
Unidades del original: 2
Unidades de la copia: 4
Región del primer registro: sin dato
```

## Errores que conviene reconocer

| Situación | Qué revisar |
| --- | --- |
| IndexError | Si la posición existe y empezaste a contar desde cero |
| KeyError | Nombre exacto de la clave y si está presente |
| TypeError al calcular | Si el campo contiene texto, None o un número |
| La lista se vuelve None | Si asignaste el resultado de append a su nombre |
| Cambió el original | Si compartiste una referencia o hiciste una copia superficial |

## Práctica y criterio de salida

Realiza el [lab 01.02](../../../labs/01_python_foundations/02_lists_dicts/README.md).
Puedes avanzar cuando representes varios registros, accedas a posiciones y
campos, agregues uno y expliques qué cambios afectan al original. Todavía no
hay checkpoint de proyecto asociado.

## Siguiente paso

03 — Condiciones y ciclos está por desarrollar. Consulta el [índice del módulo](../README.md).

## Referencias

- [Estructuras de datos de Python](https://docs.python.org/es/3/tutorial/datastructures.html).
- [Copias superficiales y profundas](https://docs.python.org/es/3/library/copy.html).

# Lab 01.02 — Representar varios registros

## Relación y entrada

- Lección: [Listas y diccionarios](../../../curriculum/01_python_foundations/02_lists_dicts/README.md).
- Entrada: su script de ventas ficticias y el entorno elegido.
- Proyecto: todavía no aplica.

Reserva 30 a 45 minutos. Predice los resultados y después consulta las soluciones.
No necesitas ciclos ni bibliotecas externas para esta práctica.

## Parte A — Leer la estructura

1. Identifica la lista y los diccionarios del script.
2. Predice el número inicial de registros y el importe de la primera venta.
3. Ejecuta el ejemplo y muestra, además, el producto del segundo registro.

<details>
<summary>Ver solución de la parte A</summary>

Hay tres diccionarios en la lista inicial. La primera venta vale `2 * 40 = 80` MXN.
Para mostrar el segundo producto, antes o después de agregar el cuarto registro:

```python
print(ventas[1]["producto"])  # lapiz
```

El índice 1 elige el segundo registro; la clave producto elige su campo.

</details>

## Parte B — Agregar y modificar

1. Conserva el registro de rotulador que agrega el script.
2. Agrega otra venta: regla, 3 unidades, precio unitario 12 MXN.
3. Comprueba que la lista contiene cinco registros.
4. Muestra el importe del último registro sin guardar un resultado fijo.

<details>
<summary>Ver solución de la parte B</summary>

Después del append del ejemplo:

```python
ventas.append({"producto": "regla", "unidades": 3, "precio_unitario_mxn": 12})
print(len(ventas))  # 5
ultima_venta = ventas[-1]
print(ultima_venta["unidades"] * ultima_venta["precio_unitario_mxn"])  # 36
```

El importe calculado es 36 MXN. append modifica la lista; no asignes su resultado
a ventas. Cada ejecución del script reconstruye la lista inicial.

</details>

## Parte C — Compartir frente a copiar

1. Predice qué pasaría si reemplazaras `copia = primera_venta.copy()` por
   `copia = primera_venta`.
2. Ejecuta el cambio y observa las unidades del original y de la copia.
3. Restaura copy y comprueba que el original conserva dos unidades.

<details>
<summary>Ver solución de la parte C</summary>

Con la asignación directa, ambos nombres refieren al mismo diccionario: al
modificarlo se muestran 4 unidades en ambos. Con copy, el registro sencillo
es independiente: original 2 y copia 4. Los campos calculados previamente no
se recalculan automáticamente, aunque cambies las entradas.

</details>

## Parte D — Una clave ausente

1. Añade una consulta `ventas[0]["region"]`, observa el error y luego corrígela.
2. Consulta con get y un valor alternativo.
3. Comprueba si get agregó la clave usando `"region" in ventas[0]`.

<details>
<summary>Ver solución de la parte D</summary>

La consulta con corchetes produce KeyError. Después de corregir:

```python
print(ventas[0].get("region", "sin dato"))  # sin dato
print("region" in ventas[0])               # False
```

get ofrece un resultado alternativo sin agregar el campo al registro.

</details>

## Evidencia y reflexión

- Conserva el script con cinco registros y el importe del último calculado.
- Explica por qué len de una lista de ventas y len de una venta cuentan cosas distintas.
- ¿Por qué el último índice puede cambiar al agregar un registro?
- ¿Por qué ventas.copy no independiza los diccionarios internos?
- Si usas un notebook para experimentar, reinicia y ejecuta todo al comprobar.
- Si usas Git, revisa el cambio y registra solo el material de la práctica.

## Siguiente paso

03 — Condiciones y ciclos está por desarrollar. Consulta el
[índice de Python fundamental](../../../curriculum/01_python_foundations/README.md).

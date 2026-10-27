# 01.03 — Condiciones y ciclos

<a id="03--condiciones-y-ciclos"></a>

[Inicio](../../../README.md) / [Módulo 01](../README.md) / **Lección 01.03**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Recorrer registros, aplicar una regla y distinguir totales generales y filtrados |
| **Necesitas** | Entorno de Python del módulo 00; biblioteca estándar |
| **Evidencia** | Script con la variante del lab y nota con conteos, importes y fronteras |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/01_python_foundations/03_conditions_loops/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-objetivos"></a>

## Propósito

Pasar de consultar registros individuales a recorrer una colección,
seleccionar los que cumplen una regla y calcular un resumen que puedas
contrastar con las ventas de origen.

## Antes de empezar

Completa [01.02 — Listas y diccionarios](../02_lists_dicts/README.md) y su lab.
Conserva tu entorno de Python y trabaja desde la raíz de DS Track con el editor
y terminal que elegiste. La página y el script incluyen las ventas completas;
no necesitas bibliotecas externas ni definir funciones propias.

El recorrido esencial utiliza `if`, `elif`, `else` y `for`. La ampliación con
`while`, `continue` y `break` es opcional y no bloquea la siguiente lección.

## Qué vas a aprender

- Explicar una condición y el orden de sus alternativas con la sangría adecuada.
- Recorrer una colección con `for` e inicializar sus contadores y acumuladores.
- Filtrar sin modificar los registros originales y conciliar conteos e importes.
- Contrastar `>=` con `>` y explicar el resultado cuando no hay coincidencias.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](conditions_loops.py) | Seguir la clasificación y selección de las mismas tres ventas con sus acumuladores | Para el ejemplo |

Abre los archivos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y compara la salida con los resultados esperados. Para practicar,
modifica tu copia y conserva los originales.

## 1. Una condición decide qué ejecutar

Una comparación produce True o False. `if` ejecuta un bloque cuando la
condición es verdadera y `else` permite definir la alternativa:

```python
importe_mxn = 80

if importe_mxn >= 50:
    print("Cumple el umbral")
else:
    print("No cumple el umbral")
```

Las líneas `if` y `else` terminan en dos puntos. La **sangría** indica qué
instrucciones pertenecen a cada bloque; usa cuatro espacios por nivel.
Una línea sin esa sangría vuelve al bloque exterior.

### Varias alternativas con elif

```python
if importe_mxn >= 80:
    categoria = "alto"
elif importe_mxn >= 50:
    categoria = "medio"
else:
    categoria = "bajo"
```

Python comprueba en orden y ejecuta solo la primera alternativa verdadera.
Con 80 se elige alto, con 50 medio y con 35 bajo. Son categorías ficticias para
practicar. Si pusieras `>= 50` primero, 80 también cumpliría esa condición
y no llegaría a la alternativa más específica.

### Combinar condiciones

```python
unidades = 2
producto = "cuaderno"
print(unidades >= 2 and importe_mxn >= 50)  # Ambas deben cumplirse
print(producto == "cuaderno" or producto == "carpeta")  # Basta una
print(not (importe_mxn >= 50))  # Invierte el resultado
```

Utiliza `==` para comparar, no `=`. No escribas
`producto == "cuaderno" or "carpeta"`: ese segundo texto no es otra comparación.
Los textos no vacíos se consideran verdaderos en condiciones; cada alternativa
debe expresar la pregunta que realmente quieres comprobar.

## 2. for: repetir una acción por registro

```python
ventas = [
    {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
    {"producto": "lapiz", "unidades": 5, "precio_unitario_mxn": 10},
    {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
]

for venta in ventas:
    print(venta["producto"])
```

`venta` recibe cada diccionario de la lista, uno a la vez. En este ejemplo el
bloque se ejecuta tres veces. No necesitas escribir índices 0, 1 y 2.
Una lista vacía produce cero repeticiones.

El nombre `venta` no crea una copia del diccionario. Si cambias sus campos,
modificas el registro de la lista. Reutiliza lo aprendido sobre referencias.

## 3. Acumuladores: construir un total paso a paso

```python
total_mxn = 0
cantidad = 0

for venta in ventas:
    importe_mxn = venta["unidades"] * venta["precio_unitario_mxn"]
    total_mxn += importe_mxn
    cantidad += 1

print(cantidad)   # 3
print(total_mxn)  # 165
```

`total_mxn += importe_mxn` abrevia `total_mxn = total_mxn + importe_mxn`.
Un **acumulador** conserva el resultado parcial. El contador suma una unidad
por cada registro. Se inicializan antes del ciclo, no dentro de él.

| Paso | Importe de la venta | Total después del paso |
| --- | --- | --- |
| Inicio | — | 0 |
| cuaderno | 80 | 80 |
| lapiz | 50 | 130 |
| carpeta | 35 | 165 |

Si reinicias el total dentro del ciclo perderás los resultados anteriores.
En un notebook vuelve a ejecutar también la inicialización al repetir el cálculo;
ejecutar solo el ciclo puede acumular sobre el total de una ejecución anterior.

## 4. Filtrar y resumir sin alterar las entradas

```python
umbral_mxn = 50
seleccionadas = []
total_seleccionado_mxn = 0

for venta in ventas:
    importe_mxn = venta["unidades"] * venta["precio_unitario_mxn"]
    if importe_mxn >= umbral_mxn:
        registro = venta.copy()
        registro["importe_mxn"] = importe_mxn
        seleccionadas.append(registro)
        total_seleccionado_mxn += importe_mxn
```

El ciclo considera todas las ventas, pero el `if` agrega solo las que cumplen.
La segunda sangría identifica las acciones dentro de la condición.
Se copia el registro sencillo antes de agregar un campo calculado, para no
modificar las entradas.

Resultado: cuaderno y lapiz, dos registros con total de 130 MXN. El total de
todas las ventas sigue siendo 165 MXN: **total general y filtrado responden a
preguntas diferentes**. Con umbral 100 no se selecciona ninguna y el total es 0.

Estos ejemplos suponen campos presentes y cantidades numéricas. Todavía no
gestionan texto inválido, datos faltantes o reglas completas de calidad;
lo desarrollaremos en la lección de validación.

> **Para comprobar:** ¿la venta de 50 MXN entra con `>= 50`? ¿Qué cambia con `> 50`?

## 5. Ejecutar el ejemplo completo

Lee [conditions_loops.py](conditions_loops.py). Clasifica, cuenta y filtra las
mismas ventas sin crear funciones todavía.

### PowerShell

Desde la raíz de ds_track y con el entorno activado:

```powershell
python curriculum\01_python_foundations\03_conditions_loops\conditions_loops.py
```

Con venv sin activar, sustituye `python` por `.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
python curriculum/01_python_foundations/03_conditions_loops/conditions_loops.py
```

Con venv sin activar, utiliza `./.venv-practice/bin/python`.

### uv

Desde `.environment-practice/uv-demo`:

```text
uv run --locked python ../../curriculum/01_python_foundations/03_conditions_loops/conditions_loops.py
```

Resultado esperado:

```text
cuaderno: 80 MXN, categoría alto
lapiz: 50 MXN, categoría medio
carpeta: 35 MXN, categoría bajo
Registros revisados: 3
Total general: 165 MXN
Registros con importe de al menos 50 MXN: 2
Total seleccionado: 130 MXN
```

## 6. Extensión opcional: controlar la repetición

<details>
<summary>Ver while, continue y break</summary>

### while: repetir mientras una condición sea verdadera

```python
paso = 0
while paso < 3:
    print(paso)
    paso += 1
```

Muestra 0, 1 y 2. La actualización hace que termine. Si olvidas cambiar el
valor, el ciclo podría no terminar; Ctrl+C interrumpe en una terminal. Para
una lista de registros, empieza con for: ya conoce cuándo agotó la colección.

### continue: omitir el resto del paso actual

```python
for venta in ventas:
    if venta["unidades"] <= 0:
        continue
    print(venta["producto"])
```

Con una cantidad no positiva, pasa al siguiente registro. Es una regla de
ejemplo: un proceso de calidad también debería explicar o registrar qué omitió.

### break: detener el ciclo completo

```python
for venta in ventas:
    if venta["producto"] == "lapiz":
        print("Producto encontrado")
        break
```

Detiene la búsqueda en la primera coincidencia. Si no existe el producto,
el mensaje no se imprime. No uses break para obtener el total de toda la
colección: dejarías registros sin revisar.

</details>

## Errores que conviene reconocer

| Situación | Qué revisar |
| --- | --- |
| IndentationError | Sangría del bloque, sin mezclar espacios y tabuladores |
| SyntaxError en if o for | Dos puntos y estructura de la instrucción |
| Total igual solo al último importe | Si inicializaste dentro del ciclo |
| Filtro incluye demasiados registros | Operadores y cada alternativa de and/or |
| Cambian los datos de entrada | Si modificaste el diccionario original |
| Total aumenta al repetir una celda | Si ejecutaste la inicialización antes del ciclo |

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 01.03](../../../labs/01_python_foundations/03_conditions_loops/README.md) para
cambiar umbrales, agregar una venta y comprobar el resumen general y el filtrado.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu script con los cuatro registros del lab | Conteos y totales general y seleccionado calculados manualmente | Qué instrucciones se repiten siempre y cuáles dependen del filtro |
| Una nota con umbrales y casos de frontera | Diferencia entre `>=` y `>`; selección vacía | Por qué cero sin coincidencias no describe el total de todas las ventas |

Puedes avanzar cuando recorras registros, expliques una condición, construyas
un total y distingas el resumen general del filtrado. La extensión opcional
no es necesaria para cerrar el recorrido esencial.

Quien aprende modifica y ejecuta su copia, y explica lo que comprobó.
Tu compañero propone un valor igual al umbral y te pide predecir si se selecciona antes de ejecutar.
Guarda la evidencia, las ayudas y las dudas en una nota personal junto a tu
práctica; PROGRESS.md registra el desarrollo editorial del curso.

Todavía no hay proyecto ni checkpoint asociado a esta lección. El material
disponible no acredita por sí solo la finalización de tus prácticas.

<a id="referencia"></a>

## Referencias

- [Control de flujo en Python](https://docs.python.org/es/3/tutorial/controlflow.html).

## Siguiente paso

Después del lab y su comprobación, continúa con
[01.04 — Funciones](../04_functions/README.md) antes de realizar su lab.

[← Módulo 01](../README.md) · [Lab 01.03](../../../labs/01_python_foundations/03_conditions_loops/README.md) · [Siguiente →](../04_functions/README.md)

# 06 — Validación y resumen

## Propósito y prerrequisitos

Cerrar Python fundamental con un proceso que puedas explicar y comprobar:
leer una entrada, aplicar reglas, conservar rechazos y resumir solo los datos
aceptados. Completa [05 — Archivos CSV](../05_csv_files/README.md) y su lab.
Utiliza tu entorno habitual; el ejemplo solo necesita la biblioteca estándar.

Al terminar podrás justificar qué registros aceptaste, explicar por qué otros
quedaron fuera y comprobar que el resumen corresponde a los registros válidos.
Puedes dividir la lección en dos sesiones: validación y conciliación.

## 1. Leer un dato no demuestra que sea válido

`int("-1")` funciona, pero una venta de menos una unidad no cumple nuestras
reglas. `int("tres")` produce un error de conversión. Son situaciones distintas:

| Capa | Pregunta | Ejemplo |
| --- | --- | --- |
| Estructura | ¿Se puede interpretar el archivo acordado? | Encabezado y cantidad de campos |
| Conversión | ¿Se puede obtener el tipo esperado? | Convertir unidades de texto a entero |
| Regla del ejercicio | ¿El valor tiene sentido para esta venta? | Unidades mayores que cero |
| Comprobación | ¿La transformación conserva lo que debe conservar? | Conteo y total del resumen |

Validar requiere definir reglas antes de procesar. Que el programa termine sin
errores no basta para demostrar que sus datos o cálculos sean correctos.

## 2. Contrato de datos: las reglas de esta muestra

Un contrato de datos describe el formato y los valores que esperas recibir.
En [ventas_revision.csv](ventas_revision.csv) usaremos estas reglas:

| Campo o condición | Regla | Tratamiento |
| --- | --- | --- |
| Encabezado | producto, unidades, precio_unitario_mxn, en ese orden | Detener si cambia |
| Estructura del registro | Tres campos | Detener si sobran o faltan campos |
| producto | Texto no vacío después de quitar espacios exteriores | Rechazar si queda vacío |
| unidades | Texto convertible a entero y valor mayor que 0 | Rechazar si falla |
| precio_unitario_mxn | Texto convertible a entero y valor mayor o igual que 0 | Rechazar si falla |
| importe_mxn | unidades × precio, calculado sobre datos válidos | Agregar a la salida |

Son decisiones del ejercicio, no reglas universales. El precio cero está permitido
para representar una entrega gratuita. Los precios usan pesos enteros: `12.50`
queda rechazado; no lo redondeamos ni lo truncamos. Un proyecto con centavos
necesita otro contrato y una representación adecuada, que desarrollaremos después.

`int` admite espacios exteriores y signos en texto numérico. Quitar espacios
del producto con `strip()` es una normalización explícita; no cambia mayúsculas
ni une nombres diferentes. La entrada original permanece intacta.

Esta muestra no tiene identificador de venta. Repetir un producto puede representar
otra venta; no eliminamos duplicados automáticamente. Identificadores, fechas y
reglas de unicidad se incorporarán cuando exista un contrato que los defina.

## 3. Reconocer excepciones: try, except y raise

Una excepción informa que una operación no pudo completarse. Ya viste ValueError
cuando `int` recibe texto que no representa un entero. Ahora podemos atender ese
caso esperado y registrar su motivo:

```python
errores = []
unidades = None
try:
    unidades = int(fila["unidades"])
except ValueError:
    errores.append("unidades no es un entero")

if unidades is not None and unidades <= 0:
    errores.append("unidades debe ser mayor que 0")
```

- `try` intenta la conversión. Si funciona, no se ejecuta except.
- `except ValueError` atiende ese error concreto; el programa puede seguir.
- `None` indica que todavía no tenemos un entero. No representa cero.
- `is not None` permite comparar el valor solo si la conversión funcionó.
- `and` evalúa la segunda condición cuando la primera es verdadera; así evitamos
  comparar None con un número.

No usamos `except: pass` ni capturamos todos los errores para continuar como si
nada hubiera ocurrido. Un nombre de variable incorrecto o una clave equivocada
debe poder detectarse, en lugar de convertirse en un rechazo silencioso.

```python
if lector.fieldnames != CAMPOS_ENTRADA:
    raise ValueError("Encabezado inesperado")
```

`raise` genera una excepción deliberadamente. Si no se atiende, detiene el proceso
y muestra su explicación. El ejemplo detiene errores de estructura, archivo
inexistente, codificación o lectura CSV: no dispone de reglas para recuperar
esos archivos de manera confiable. `strict=True` ayuda a detectar ciertos errores
de formato CSV, pero no comprueba las reglas de negocio.

## 4. Validar una venta y conservar los rechazos

La función `validar_venta` del [script](validation_summary.py) recibe un diccionario
de texto y devuelve otro diccionario con dos claves:

```python
# Una entrada aceptada
{"venta": {"producto": "cuaderno", "unidades": 2,
           "precio_unitario_mxn": 40, "importe_mxn": 80}, "errores": []}

# Una entrada rechazada
{"venta": None, "errores": ["unidades no es un entero"]}
```

Se comprueban los tres campos antes de devolver el resultado: una venta puede
tener varios motivos. No reemplazamos valores inválidos por cero para forzar
el cálculo. Eso alteraría su significado y ocultaría un problema de origen.

`separar_registros` construye dos listas nuevas. Una lista vacía de errores
se evalúa como falsa; una lista con motivos, como verdadera.

```python
for numero, fila in enumerate(registros, start=1):
    resultado = validar_venta(fila)
    if resultado["errores"]:
        # Conservar campos originales y motivos en rechazados
        ...
    else:
        validos.append(resultado["venta"])
```

Los puntos suspensivos señalan una parte omitida: consulta el script para ejecutar
el programa completo. `enumerate` proporciona número y registro en cada vuelta.
El número empieza en 1 y corresponde al orden de registros leídos, sin encabezado;
no es un número de línea física ni un identificador permanente. DictReader omite
líneas completamente vacías y un registro puede ocupar varias líneas.

En ventas_rechazadas.csv conservamos los valores originales y el motivo.
`"; ".join(errores)` reúne varios mensajes en un campo de texto. La corrección
queda para una revisión posterior; rechazar no equivale a borrar ni corregir.

## 5. Resumir solo los registros válidos

Un resumen agrupa registros y acumula medidas. Aquí la clave es producto:

```python
if producto not in por_producto:
    por_producto[producto] = {
        "producto": producto, "registros": 0, "unidades": 0, "importe_mxn": 0
    }
grupo = por_producto[producto]
grupo["registros"] += 1
grupo["unidades"] += venta["unidades"]
grupo["importe_mxn"] += venta["importe_mxn"]
```

El primer registro crea el acumulador; los siguientes del mismo producto lo
actualizan. `grupo` hace referencia al diccionario guardado en por_producto:
al actualizarlo, cambia ese acumulador. Los diccionarios de entrada no se modifican.
`list(por_producto.values())` convierte los grupos en una lista para escribir CSV.

No mezcles estas cantidades: registros cuenta ventas; unidades cuenta artículos;
importe_mxn expresa pesos. Una venta de cinco lápices es un registro y cinco unidades.

## 6. Conciliar: comprobar conteos y totales

Antes de escribir se verifican estas igualdades:

```text
registros leídos = registros válidos + registros rechazados
registros válidos = suma de registros del resumen
unidades válidas = suma de unidades del resumen
importe válido = suma de importes del resumen
```

Para nuestra entrada: **8 = 4 + 4**, **10 unidades** y **165 MXN**.
Los registros rechazados no tienen un importe aceptado; no inventamos un total
de la entrada completa. El resumen describe solo las ventas válidas.

Estas comprobaciones detectan pérdidas o errores de agregación, pero totales
iguales no demuestran que todos los campos sean correctos. También revisa casos
conocidos y el detalle. El script usa `if` y `raise ValueError` para estos controles;
`assert` es útil en comprobaciones de desarrollo, pero puede desactivarse al
ejecutar Python con optimización y no debe ser el único control de entradas.

Si no hay válidos, el resumen es vacío, unidades e importe son cero, y los CSV
conservan sus encabezados. Eso no demuestra que la entrada haya sido adecuada:
revisa los rechazos. Un archivo con solo encabezado también se procesa como cero
registros; un archivo sin encabezado se rechaza por estructura.

## 7. Ejecutar y revisar

### PowerShell

Desde la raíz, con tu entorno activado:

```powershell
# Leer, validar, resumir y escribir resultados
python curriculum\01_python_foundations\06_validation_summary\validation_summary.py
# Revisar valores originales y razones de rechazo
Get-Content curriculum\01_python_foundations\06_validation_summary\output\ventas_rechazadas.csv -Encoding utf8
# Revisar los indicadores por producto
Get-Content curriculum\01_python_foundations\06_validation_summary\output\resumen_productos.csv -Encoding utf8
```

Sin activar venv, sustituye python por `.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
# Ejecutar desde la raíz con el entorno activado
python curriculum/01_python_foundations/06_validation_summary/validation_summary.py
# Consultar rechazos y resumen
cat curriculum/01_python_foundations/06_validation_summary/output/ventas_rechazadas.csv
cat curriculum/01_python_foundations/06_validation_summary/output/resumen_productos.csv
```

Sin activar venv, utiliza `./.venv-practice/bin/python`.
Con uv, desde `.environment-practice/uv-demo`, ejecuta:

```text
uv run --locked python ../../curriculum/01_python_foundations/06_validation_summary/validation_summary.py
```

### Resultados esperados

```text
Registros de entrada: 8
Válidos: 4 | Rechazados: 4
Unidades válidas: 10
Importe válido: 165 MXN
Conteo y resumen conciliados. Revisa los tres CSV en output.
```

| Registro de entrada | Decisión | Razón o importe |
| --- | --- | --- |
| 1: cuaderno | Válido | 80 MXN |
| 2: lápiz, azul | Válido | 50 MXN |
| 3: carpeta | Válido | 35 MXN |
| 4: espacios como producto | Rechazado | producto vacío |
| 5: goma | Rechazado | unidades debe ser mayor que 0 |
| 6: regla | Rechazado | unidades no es un entero |
| 7: rotulador | Válido | 0 MXN, dos unidades |
| 8: carpeta | Rechazado | precio no es un entero |

Se generan ventas_validas.csv, ventas_rechazadas.csv y resumen_productos.csv en
output, carpeta ignorada por Git. Cada ejecución reemplaza esos archivos y conserva
la entrada. La validación y conciliación ocurren antes de escribir; si fallan,
las salidas anteriores pueden permanecer y no representan la ejecución fallida.
Una falla durante la escritura puede dejar archivos incompletos o de distintas
ejecuciones. Revisa el resultado del proceso; escribir un conjunto de salidas
de forma atómica será una profundización posterior.

## Práctica, evidencia y criterio de salida

Realiza el [lab 01.06](../../../labs/01_python_foundations/06_validation_summary/README.md).
Conserva código y una nota con reglas, conteos, motivos y total. Puedes cerrar
este módulo cuando expliques el recorrido completo, compruebes casos límite y
demuestres que no se modificó la entrada. El desarrollo de la lección no acredita
por sí mismo la finalización de tus prácticas. Todavía no hay checkpoint asociado.

## Siguiente paso

Consulta [02 — pandas](../../02_pandas/README.md), el siguiente módulo del track.
Ya está disponible la [primera lección — Series y DataFrame](../../02_pandas/01_series_dataframe/README.md);
las siguientes están por desarrollar.
DataFrame permitirá expresar operaciones tabulares, conservando estas mismas
preguntas sobre tipos, reglas, registros y totales.

## Referencias oficiales

- [Errores y excepciones](https://docs.python.org/es/3/tutorial/errors.html).
- [Lectura y escritura CSV](https://docs.python.org/es/3/library/csv.html).
- [enumerate](https://docs.python.org/es/3/library/functions.html#enumerate).

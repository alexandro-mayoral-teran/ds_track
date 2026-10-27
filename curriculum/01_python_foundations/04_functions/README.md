# 01.04 — Funciones

<a id="04--funciones"></a>

[Inicio](../../../README.md) / [Módulo 01](../README.md) / **Lección 01.04**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Separar y reutilizar transformaciones mediante entradas y resultados explícitos |
| **Necesitas** | Entorno de Python del módulo 00; biblioteca estándar |
| **Evidencia** | Script con la función del lab y nota de casos comprobados |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/01_python_foundations/04_functions/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-objetivos"></a>

## Propósito

Separar cálculos, selección y presentación para reutilizar transformaciones
sin copiar bloques enteros. Una misma función podrá resumir la colección
completa o una selección y devolver datos para seguir trabajando.

## Antes de empezar

Completa [01.03 — Condiciones y ciclos](../03_conditions_loops/README.md) y su
lab. Usa el mismo entorno de Python sin instalar bibliotecas. Edita y ejecuta
desde la raíz de DS Track; las ventas están incluidas en la página y el script.
Retoma las [referencias y copias de 01.02](../02_lists_dicts/README.md#5-referencias-y-copias-qué-estás-modificando)
para explicar qué ocurre al pasar una colección a una función.

## Qué vas a aprender

- Distinguir definir una función de llamarla y parámetros de argumentos.
- Usar `return` para entregar datos y diferenciarlo de `print`.
- Separar cálculo, selección y resumen con entradas explícitas y nombres locales.
- Reutilizar funciones con otra colección, incluida una vacía, y comprobar que conservan las entradas.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](functions_demo.py) | Leer funciones separadas y seguir cómo main prepara, transforma y presenta datos | Para el ejemplo |

Abre los archivos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y compara la salida con los resultados esperados. Para practicar,
modifica tu copia y conserva los originales.

## 1. De un cálculo repetido a una función

Una función agrupa instrucciones bajo un nombre. Permite ejecutar la misma
operación con entradas diferentes:

```python
def calcular_importe(unidades, precio_unitario_mxn):
    importe_mxn = unidades * precio_unitario_mxn
    return importe_mxn

resultado = calcular_importe(3, 40)
print(resultado)  # 120
```

| Parte | Qué hace |
| --- | --- |
| `def` | Define la función |
| `calcular_importe` | Nombre que expresa su responsabilidad |
| `unidades`, `precio_unitario_mxn` | Parámetros: nombres de las entradas |
| `3`, `40` al llamarla | Argumentos: valores que entregas |
| Sangría y dos puntos | Delimitan el bloque, como en if y for |
| `return` | Entrega el resultado a quien llamó la función |

Definir no ejecuta el cálculo. La llamada con paréntesis lo ejecuta.
`calcular_importe` sin paréntesis refiere a la función, pero no obtiene el importe.

## 2. print y return tienen propósitos distintos

`print` muestra información; `return` entrega un valor para seguir trabajando:

```python
importe = calcular_importe(3, 40)
cumple_umbral = importe >= 100
print(cumple_umbral)  # True
```

Si tu función solo imprimiera el importe y no tuviera return, la llamada
devolvería `None`. Ver el número en la pantalla no significa que lo hayas recibido
como resultado. `return` también termina esa llamada: las instrucciones posteriores
de ese mismo bloque no se ejecutan.

Preferiremos funciones de transformación que devuelvan datos y una parte separada
que los presente. Así el mismo resultado puede alimentar una terminal, notebook,
reporte o aplicación sin rehacer el cálculo.

## 3. Llamar con argumentos claros

```python
# Por posición: el orden corresponde a los parámetros
calcular_importe(3, 40)
# Por nombre: deja explícito el significado de cada valor
calcular_importe(unidades=3, precio_unitario_mxn=40)
```

Los nombres deben coincidir con la definición. Si falta un argumento obligatorio,
Python informa TypeError. Revisa la llamada antes de cambiar el cálculo.
Una función recibe valores, no sabe por sí sola si sus unidades son correctas.

### Un valor predeterminado

```python
def alcanza_umbral(importe_mxn, umbral_mxn=50):
    return importe_mxn >= umbral_mxn

print(alcanza_umbral(80))                 # True: utiliza 50
print(alcanza_umbral(80, umbral_mxn=100))  # False
```

Aquí se usa un número inmutable como predeterminado. Evita usar `[]` o `{}` como
valores predeterminados de funciones que los modifican: se crean al definir la
función y pueden compartirse entre llamadas. Por ahora pasa las colecciones
explícitamente como argumentos.

## 4. Alcance: dónde existe una variable

Los parámetros y nombres asignados dentro de una función son locales a su llamada:

```python
def calcular_importe(unidades, precio_unitario_mxn):
    importe_local = unidades * precio_unitario_mxn
    return importe_local

resultado = calcular_importe(2, 40)
print(resultado)  # 80
```

No puedes consultar `importe_local` desde fuera como si fuera una variable del
script: se produciría NameError. Recibe el resultado mediante return.
Evita depender de variables globales para hacer un cálculo: declara lo que
necesita la función en sus parámetros. Eso permite probarla con otras entradas.

### Los argumentos mutables siguen siendo objetos compartidos

Pasar una lista o diccionario no lo copia automáticamente. Una función que
modifica sus campos puede afectar el objeto del código que la llamó.
Utiliza la copia explícita que aprendiste cuando quieras enriquecer un registro
sin modificar las entradas, y documenta esa decisión.

## 5. Una función por responsabilidad

El ejemplo completo separa tres operaciones:

| Función | Entrada | Resultado |
| --- | --- | --- |
| calcular_importe | Unidades y precio | Número con el importe |
| seleccionar_ventas | Lista de registros y umbral | Lista nueva con copias seleccionadas |
| resumir_ventas | Lista de registros | Diccionario con cantidad y total |

`resumir_ventas` sirve tanto para toda la colección como para la selección:

```python
general = resumir_ventas(ventas)
seleccionadas = seleccionar_ventas(ventas, umbral_mxn=50)
filtrado = resumir_ventas(seleccionadas)
```

Para las tres ventas conocidas, general contiene cantidad 3 y total 165; filtrado
contiene cantidad 2 y total 130. La función devuelve datos, no imprime ese resumen.
Con una colección vacía devuelve cantidad 0 y total 0.

Coloca `return` después del ciclo cuando quieras recorrer todos los registros.
Si lo pones dentro sin una condición que lo justifique, podrías terminar en la
primera venta. La sangría también cambia el resultado de una función.

Estos ejemplos suponen campos numéricos presentes. Convertir y validar entradas
será una responsabilidad explícita en las siguientes lecciones.

## 6. Documentar sin repetir todo el código

La cadena al principio de una función, llamada **docstring**, explica su contrato:

```python
def calcular_importe(unidades, precio_unitario_mxn):
    """Calcula el importe con entradas numéricas ya preparadas."""
    return unidades * precio_unitario_mxn
```

Describe qué recibe, qué devuelve y supuestos importantes. Un nombre claro y
una explicación breve ayudan más que un comentario que repita cada operador.

## 7. Ejecutar y leer el ejemplo

Abre [functions_demo.py](functions_demo.py). Primero define las funciones y
después `main` prepara los datos, llama a las transformaciones y muestra resultados.

### PowerShell

Desde la raíz y con tu entorno activado:

```powershell
python curriculum\01_python_foundations\04_functions\functions_demo.py
```

Con venv sin activar, usa `.\.venv-practice\Scripts\python.exe` en lugar de python.

### Bash/Zsh

```bash
python curriculum/01_python_foundations/04_functions/functions_demo.py
```

Con venv sin activar, utiliza `./.venv-practice/bin/python`.

### uv

Desde `.environment-practice/uv-demo`:

```text
uv run --locked python ../../curriculum/01_python_foundations/04_functions/functions_demo.py
```

Resultado esperado:

```text
Registros generales: 3
Total general: 165 MXN
Registros seleccionados: 2
Total seleccionado: 130 MXN
```

### La última condición del archivo

`if __name__ == "__main__":` llama a main cuando ejecutas ese archivo directamente.
Si otro programa importa sus funciones, no ejecuta automáticamente la demostración.
Es una convención útil; estudiaremos las importaciones con más detalle al organizar
la lectura y transformación de archivos. No necesitas memorizarla para calcular.

## Errores que conviene reconocer

| Situación | Qué revisar |
| --- | --- |
| Recibes None aunque se mostró un número | Si falta return y solo utilizaste print |
| TypeError en la llamada | Argumentos requeridos, nombres y tipos |
| NameError fuera de una función | Si intentaste usar una variable local |
| Solo se resume el primer registro | Sangría y ubicación de return |
| Cambian las entradas después de llamar | Modificaciones sobre objetos mutables compartidos |

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 01.04](../../../labs/01_python_foundations/04_functions/README.md) para
reutilizar funciones con otras entradas y agregar una transformación con su comprobación.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu script con la función nueva del lab | Resultados para distintas entradas y para una colección vacía | Qué recibe y devuelve cada función y qué presenta `main` |
| Una nota con argumentos y resultados | Las entradas no cambian después de transformar | Por qué `return` no equivale a `print` ni pasar una lista equivale a copiarla |

Puedes avanzar cuando reutilices el resumen con entradas diferentes, expliques
parámetros frente a argumentos y `return` frente a `print`, y compruebes que las
entradas no fueron modificadas.

Quien aprende modifica y ejecuta su copia, y explica lo que comprobó.
Tu compañero propone otros argumentos y te pide anticipar el resultado sin cambiar la definición de la función.
Guarda la evidencia, las ayudas y las dudas en una nota personal junto a tu
práctica; PROGRESS.md registra el desarrollo editorial del curso.

Todavía no hay proyecto ni checkpoint asociado a esta lección. El material
disponible no acredita por sí solo la finalización de tus prácticas.

<a id="referencia"></a>

## Referencias

- [Definir funciones y sus argumentos](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions).

## Siguiente paso

Después del lab y su comprobación, continúa con
[01.05 — Archivos CSV](../05_csv_files/README.md) antes de realizar su lab.

[← Módulo 01](../README.md) · [Lab 01.04](../../../labs/01_python_foundations/04_functions/README.md) · [Siguiente →](../05_csv_files/README.md)

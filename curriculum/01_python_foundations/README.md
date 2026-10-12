# 01 — Python fundamental

Aprender tipos, colecciones, control de flujo, funciones, módulos, archivos y
errores mediante registros sintéticos pequeños. Comenzamos con una venta sencilla
y después trabajaremos con los registros del recorrido. El módulo termina con una
transformación de CSV realizada con la biblioteca estándar.

## Orden de desarrollo

| Orden | Lección | Resultado |
| --- | --- | --- |
| 1 | [Variables, tipos y operaciones](01_variables_types/) | Interpretar entradas y comprobar un cálculo |
| 2 | [Listas y diccionarios](02_lists_dicts/) | Representar, consultar y modificar varios registros |
| 3 | [Condiciones y ciclos](03_conditions_loops/) | Filtrar registros y comprobar resúmenes |
| 4 | [Funciones](04_functions/) | Separar, reutilizar y comprobar transformaciones |
| 5 | [Archivos CSV](05_csv_files/) | Leer, transformar y escribir con la biblioteca estándar |
| 6 | [Validación y resumen](06_validation_summary/) | Comprobar entradas y totales, documentar reglas |

Se utilizan csv y pathlib como módulos de la biblioteca estándar, y excepciones
para atender conversiones y comprobar resultados. JSON queda como ampliación posterior. Las lecciones 01–06 y sus labs
[01.01](../../labs/01_python_foundations/01_variables_types/README.md) y
[01.02](../../labs/01_python_foundations/02_lists_dicts/README.md) y
[01.03](../../labs/01_python_foundations/03_conditions_loops/README.md) y
[01.04](../../labs/01_python_foundations/04_functions/README.md) y
[01.05](../../labs/01_python_foundations/05_csv_files/README.md) y
[01.06](../../labs/01_python_foundations/06_validation_summary/README.md) están disponibles.
La meta es transformar un CSV pequeño y explicar el resultado antes de pasar a pandas.

## Bases y profundización posterior

El alcance esencial incluye mutabilidad y referencias, funciones con parámetros
y retorno, métodos básicos, rutas, lectura de errores y comprobaciones pequeñas.
Usaremos objetos y `with` cuando ayuden a leer archivos, sin exigir diseñar clases.

Clases, composición, dataclasses, decoradores y generadores se desarrollarán en
la [ruta de Python aplicado](../../docs/architecture.md#python-aplicado-del-notebook-al-proyecto)
después de pandas y SQL. Esa ruta está planificada; todavía no hay lecciones
ni labs y no bloquea el paso al análisis tabular.


## Continuidad del track

Prerrequisito de estudio: [00 — Entorno de aprendizaje](../00_getting_started/README.md).
Consulta después [02 — pandas](../02_pandas/README.md).

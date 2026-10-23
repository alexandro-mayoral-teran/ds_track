# 10.02 — Polars: tablas y expresiones

## Propósito y prerrequisitos

Aprender a leer una tabla con Polars, elegir columnas, calcular otras, filtrar
registros y resumir grupos. Cada operación tendrá una pregunta concreta y una
respuesta que puedas comprobar a mano antes de confiar en el código.

Necesitas reconocer variables, llamadas a funciones y tablas, preparar un entorno
Python según [00.05](../../00_getting_started/05_environment/README.md) y entender
qué significa un contrato de datos. Puedes consultar
[10.01](../01_question_contract_reference/README.md) para profundizar en contrato
y referencia. Aquí se presentan de nuevo todos los datos, reglas y resultados;
no necesitas una entrega personal anterior ni recordar otra muestra.

**Esencial:** recorrido Python inmediato, expresiones y conciliación.
**Práctica:** modificar fecha/umbral y justificar resultados.
**Extensión:** explorar 40 filas y contrastar con pandas. No bloquea avanzar.
Lazy se desarrollará en 10.03; faltantes/uniones en 10.04. Esta introducción no
mide tiempos ni demuestra que una herramienta sea más rápida.

## Objetivos

- Distinguir `DataFrame`, `Series` y expresión.
- Relacionar `select`, `with_columns`, `filter` y `group_by().agg()` con cambios
  de columnas, filas y unidad de observación.
- Conservar IDs textuales, fechas y pesos enteros; ampliar el tipo de una suma.
- Comprobar esquema y cada par crédito/importe contra una referencia independiente,
  incluidos resultados vacíos.

## Entorno y archivos

Referencia comprobada: **Python 3.12.12 y Polars 2.0.0**, declarada en
[`pyproject.toml`](../../../pyproject.toml) y [`uv.lock`](../../../uv.lock).
Elige un gestor y sigue el [recorrido completo de tu shell](recorridos.md):
PowerShell, Bash/Zsh o CMD. No instales en Anaconda `base` ni en Python global.
Un entorno adecuado ya comprobado no necesita reinstalación.

Abre la raíz de DS Track en tu editor y selecciona ese mismo intérprete.
Los bloques Python se ejecutan en una consola Python o en un script abierto,
no directamente en PowerShell. Cuando se indica «desde la raíz», se trata de
la carpeta que contiene `pyproject.toml`. La ejecución por terminal está explicada
por separado en los recorridos.

| Archivo | Función |
| --- | --- |
| [muestra.csv](muestra.csv) | Entrada completa de seis observaciones |
| [tablas_polars.py](tablas_polars.py) | Lectura, operaciones nativas y comprobaciones reutilizables |
| [recorridos.md](recorridos.md) | Entorno y ejecución completa desde otra sesión |
| [Lab 10.02](../../../labs/10_polars_duckdb/02_polars_tables_expressions/README.md) | Actividad, evidencia y soluciones razonadas |

El script reutiliza reglas y referencia incluidas en el repositorio. No importa
resultados guardados de tus prácticas. Importarlo no lee fuentes ni escribe
archivos; ejecutar su programa principal solo lee y muestra resultados.

## 1. Pregunta, datos y contrato completos

Una financiera ficticia registra saldos de tres créditos en dos cortes. Queremos
responder: **¿qué créditos tienen al menos 2000 MXN el 31 de octubre de 2026,
y cuántos son y cuánto suman?** Después resumiremos cada corte completo.

| id_credito | fecha_corte | saldo_mxn |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Una fila es **un crédito en un corte**, no un crédito para toda su historia.
Hay seis filas y tres créditos distintos. La clave compuesta es
`(id_credito, fecha_corte)`; `001` puede aparecer en ambos cortes.

Reglas: ID textual de tres dígitos, fecha válida entre 1900 y 2100,
saldo entero en MXN entre 0 y 2147483647, sin ausencias y sin claves repetidas.
Se rechaza la fuente completa ante una incidencia, incluso fuera del filtro.
No se imputan valores ni se descartan duplicados. Que un dato quepa en un tipo
no demuestra todas estas reglas.

Respuesta manual: en octubre, 100 y 1900 no cumplen; `003` con 2600 sí.
La selección es una fila y suma 2600 MXN. Por corte completo: septiembre
`0 + 2000 + 2500 = 4500`; octubre `100 + 1900 + 2600 = 4600`.
Sumar ambos cortes daría 9100 **MXN de observaciones a distintas fechas**;
no representa el saldo de cartera en una sola fecha.

## 2. Construir e inspeccionar un DataFrame

Este bloque es autónomo: copia los datos y ejecuta desde un script nuevo.

```python
from datetime import date
import polars as pl

tabla = pl.DataFrame(
    {
        "id_credito": ["001", "002", "003", "001", "002", "003"],
        "fecha_corte": [date(2026, 9, 30)] * 3 + [date(2026, 10, 31)] * 3,
        "saldo_mxn": [0, 2000, 2500, 100, 1900, 2600],
    },
    schema={"id_credito": pl.String, "fecha_corte": pl.Date, "saldo_mxn": pl.Int32},
    strict=True,
)
print(tabla.shape)
print(dict(tabla.schema))
print(tabla.head(2).to_dicts())
```

`DataFrame` es una tabla con columnas nombradas y tipos. `shape` produce `(6, 3)`:
seis filas y tres columnas. `schema` informa `String`, `Date`, `Int32` en ese
orden. `head(2)` permite inspeccionar las primeras dos filas; `to_dicts()` las
convierte a registros Python para leerlas con facilidad. No hagas esa conversión
por costumbre con tablas enormes: materializa objetos Python adicionales.

`date(año, mes, día)` construye una fecha sin hora; `* 3` repite esa fecha tres
veces en la lista. `strict=True` exige conversiones estrictas al construir,
pero **no valida** la clave ni la regla de saldo no negativo. Un esquema tampoco
prohíbe por sí solo `null` en Polars. Por eso hay controles separados.

El ID es texto: convertir `001` a entero pierde ceros que forman parte de su
representación. `Int32` es un entero con rango limitado; aquí permite almacenar
cada saldo del contrato. No implica que cualquier suma también quepa en Int32.

Polars no utiliza un índice de etiquetas como el índice de pandas. El ID es
una columna normal y la clave la definimos nosotros. Tener números de fila
en pantalla no crea una identidad persistente para los registros.

## 3. Series y expresiones: valores frente a una operación

```python
# Continuación del bloque anterior.
columna = tabla.get_column("saldo_mxn")
expresion = pl.col("saldo_mxn") / 1000
print(type(columna).__name__)    # Series
print(type(expresion).__name__)  # Expr
```

Una `Series` contiene valores de una columna. Una expresión describe una
operación que Polars aplicará a columnas dentro de un **contexto**. `pl.col`
señala la columna por nombre, `/ 1000` describe una división y todavía falta
indicar en qué tabla y con qué forma de salida ejecutarla.

Esto no vuelve diferida toda la consulta: en esta lección trabajamos con
`DataFrame` y las llamadas a `select`, `filter`, etc. producen resultados
inmediatos. Una expresión sin contexto es una descripción, no una tabla ya
calculada. La API de consultas lazy se verá después.

## 4. select: elegir y calcular columnas de salida

```python
vista = tabla.select(
    pl.col("id_credito"),
    (pl.col("saldo_mxn") / 1000).alias("saldo_miles_mxn"),
)
print(vista.to_dicts())
```

`select` determina las columnas que saldrán. `alias` asigna un nombre a la
expresión; no cambia el nombre de la fuente. Esta vista tiene seis filas y
dos columnas. Sus importes son aproximadamente `0.0, 2.0, 2.5, 0.1, 1.9, 2.6`
**miles de MXN**. La división produce `Float64`; algunos valores decimales
se representan aproximadamente y pueden imprimirse como `1.9000000000000001`.
Esta columna sirve para presentación. Conciliamos dinero en los pesos enteros
originales; no redondeamos la fuente para ocultar diferencias.

Con expresiones por fila, `select` conserva aquí las seis filas. Con una
agregación cambia la forma:

```python
total_observaciones = tabla.select(
    pl.len().alias("registros"),
    pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn"),
)
print(total_observaciones.to_dicts())
# [{'registros': 6, 'saldo_mxn': 9100}]
```

Ahora hay una fila porque se resumió toda la entrada. `pl.len()` cuenta filas;
`pl.col("saldo_mxn").count()` cuenta valores no nulos de esa columna. Coinciden
en esta fuente porque el contrato excluye ausencias; no son definiciones
intercambiables. Faltantes y sus denominadores se desarrollarán en 10.04.

## 5. with_columns: conservar columnas y añadir derivadas

```python
ampliada = tabla.with_columns(
    (pl.col("saldo_mxn") / 1000).alias("saldo_miles_mxn"),
    (pl.col("saldo_mxn") >= 2000).alias("cumple_umbral"),
    pl.lit("MXN").alias("unidad_saldo"),
)
print(ampliada.shape)  # (6, 6)
print(tabla.shape)     # (6, 3)
```

`with_columns` conserva las columnas existentes y añade las calculadas. Si un
alias coincide con un nombre existente, lo reemplaza **en el resultado**.
La tabla `tabla` sigue disponible con sus tres columnas. Evita asignar encima
de ella hasta comprobar las derivadas si necesitas comparar antes/después.

La comparación produce booleanos: `False, True, True, False, False, True`.
`pl.lit("MXN")` expresa un texto constante, repetido en cada fila. En muchos
argumentos de expresiones, un string se interpreta como nombre de columna;
`lit` evita confundir una etiqueta literal con una columna llamada `MXN`.

Las expresiones de una misma llamada se resuelven sobre sus columnas de entrada.
No uses un alias recién creado como si ya existiera dentro de esa misma llamada.
Si un cálculo depende de otro nuevo, separa los pasos:

```python
dos_pasos = (
    tabla.with_columns((pl.col("saldo_mxn") / 1000).alias("saldo_miles_mxn"))
    .with_columns((pl.col("saldo_miles_mxn") >= 2).alias("cumple_en_miles"))
)
```

Esta variante ilustra dependencias; para nuestro indicador usamos la comparación
directa en pesos, que conserva la unidad del contrato.

## 6. filter: conservar filas cuya condición es verdadera

```python
corte = date(2026, 10, 31)
minimo = 2000
seleccion = (
    tabla.filter(
        (pl.col("fecha_corte") == corte)
        & (pl.col("saldo_mxn") >= minimo)
    )
    .select("id_credito", "saldo_mxn")
    .sort("id_credito")
)
print(seleccion.to_dicts())
# [{'id_credito': '003', 'saldo_mxn': 2600}]
```

`filter` elige filas, `select` columnas y `sort` ordena la salida para comparar.
El operador `&` combina condiciones por registro; cada comparación lleva
paréntesis. `and` intenta decidir la verdad de objetos Python completos y no
sirve para esta combinación de expresiones. `>=` incluye la frontera de 2000.

Primero filtra por fecha y saldo, después retira la fecha de la salida. Si
quitaras `fecha_corte` antes de filtrar por ella, esa columna ya no estaría
disponible. No dependas del orden incidental de grupos o archivos para comparar.

**Vacío esperado:** cambia `corte` a `date(2026, 11, 30)`. No hay ese corte;
sale una tabla de cero filas y dos columnas, con `String/Int32`. Su conteo y
suma de conjunto vacío son cero por la definición de nuestra pregunta. Eso no
equivale a reemplazar un saldo desconocido por cero: la fuente no tiene faltantes.

## 7. group_by y agg: cambiar la unidad a un corte

```python
resumen = (
    tabla.group_by("fecha_corte")
    .agg(
        pl.len().alias("registros"),
        pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn"),
    )
    .sort("fecha_corte")
)
print(resumen.to_dicts())
```

| fecha_corte | registros | saldo_mxn |
| --- | ---: | ---: |
| 2026-09-30 | 3 | 4500 |
| 2026-10-31 | 3 | 4600 |

`group_by` establece grupos de filas con la misma fecha. `agg` calcula un conteo
y una suma **dentro de cada grupo**. La unidad de salida es un corte; ya no
un crédito/corte. Por eso no conservamos `id_credito` como si identificara cada
fila del resumen. En el runtime estándar comprobado, `registros` es `UInt32`
y la suma es `Int64`. El esquema vacío también se conserva, pero una agrupación
de entrada vacía devuelve cero grupos; no inventa una fecha con saldo cero.

Sin `.sum()`, agregar `pl.col("saldo_mxn")` recopilaría los valores en listas
por grupo, no calcularía un total. Expresa la reducción que necesitas.

### Por qué ampliar antes de sumar

Este ejemplo independiente no necesita la tabla anterior:

```python
import polars as pl

grandes = pl.DataFrame({"saldo_mxn": [2147483647, 2147483647]},
                      schema={"saldo_mxn": pl.Int32})
correcto = grandes.select(
    pl.col("saldo_mxn").cast(pl.Int64).sum().alias("saldo_mxn")
)
print(correcto.to_dicts())  # [{'saldo_mxn': 4294967294}]
```

Cada importe cabe en Int32; su suma no. Convertir a Int64 **después** de sumar
en Int32 no recupera un resultado desbordado. Amplía los valores antes de la
reducción. Int64 también tiene límites: no es una promesa para cualquier volumen.
En este contrato hay a lo sumo 1000 IDs de tres dígitos por corte, con clave única;
incluso al máximo permitido, la suma por corte cabe en Int64.
El generador de práctica utiliza hasta 999 IDs. Para otros contratos, revisa
de nuevo límites, unidades y precisión.

## 8. Leer el CSV sin perder el contrato

Los bloques anteriores partían de valores Python explícitos. Un CSV no lleva
ese esquema incorporado. Este recorrido completo carga la muestra de esta
sección desde la raíz y comprueba todas las filas antes de filtrar:

```python
from pathlib import Path
import sys

carpeta = Path("curriculum/10_polars_duckdb/02_polars_tables_expressions").resolve()
sys.path.insert(0, str(carpeta))
from tablas_polars import cargar_tabla, seleccionar, resumir_por_corte
from tablas_polars import comprobar_seleccion, comprobar_resumen, transformar

tabla_csv = cargar_tabla()
salida = seleccionar(tabla_csv)
resumen_csv = resumir_por_corte(tabla_csv)
print(comprobar_seleccion(salida))
print(comprobar_resumen(resumen_csv))
print(transformar(tabla_csv).shape)  # (6, 4)
```

`sys.path.insert` permite importar las funciones del directorio de la lección
sin instalar un paquete adicional. En un script guardado en esa misma carpeta,
puedes importar `tablas_polars` directamente. El ejecutor completo ya lo resuelve.

Dentro de `cargar_tabla`, la lectura nativa es:

```python
# Fragmento explicado del cargador; ruta apunta a un CSV validado completo.
textos = pl.read_csv(ruta, infer_schema=False, try_parse_dates=False)
tabla_convertida = textos.with_columns(
    pl.col("fecha_corte").str.to_date("%Y-%m-%d", strict=True),
    pl.col("saldo_mxn").cast(pl.Int32, strict=True),
)
```

`infer_schema=False` lee columnas como texto, conservando `001`.
`.str.to_date` interpreta la forma año-mes-día y `cast` convierte el saldo a
entero. Conversión estricta evita sustituir silenciosamente un error por null;
no reemplaza validar rango, fecha, ausencia y clave.

El cargador reutiliza la referencia Python estándar para validar el CSV entero,
lee también con Polars y compara todas las filas convertidas por clave.
Después revisa el esquema y las reglas de la tabla. Las funciones de operación
también rechazan tablas alteradas fuera del contrato. Estos controles didácticos
leen/materializan datos adicionales: **no son un benchmark, un lector por lotes
ni un diseño para memoria acotada**. La transformación principal se expresa con
operaciones Polars nativas; los bucles Python pertenecen a la auditoría independiente.

Una selección correcta podría ocultar un saldo negativo en septiembre. Validar
únicamente octubre sería insuficiente. No uses `ignore_errors`, conversiones
permisivas ni un filtro para hacer desaparecer una incidencia de la fuente.

## 9. Conciliar antes de dar por correcto

`comprobar_seleccion` exige las dos columnas `String/Int32` sin null y compara
cada par ID/importe con la referencia. En un vacío revisa el esquema igualmente:
una lista vacía no demuestra que el tipo sea correcto.
`comprobar_resumen` reconstruye conteos y sumas por fecha con Python estándar.
No compara únicamente un total global que podría esconder errores compensados.

```python
# Continuación del recorrido CSV: estas dos filas tienen suma correcta, pares erróneos.
from datetime import date
import polars as pl
from tablas_polars import SELECCION

erronea = pl.DataFrame(
    {"id_credito": ["002", "003"], "saldo_mxn": [2100, 2400]}, schema=SELECCION
)
try:
    comprobar_seleccion(erronea, corte=date(2026, 9, 30), minimo=2000)
except ValueError as error:
    print(error)  # Pares ID/importe distintos...
```

En septiembre esperamos `002/2000` y `003/2500`; dos filas y 4500 MXN coinciden
en la salida equivocada, pero cada importe cambió. Tampoco conviertas una salida
Float64 a entero antes de comprobar: ocultaría una diferencia de tipos.

## 10. Relación con pandas y escala opcional

| Necesidad | Polars en esta sección | Relación conceptual con pandas |
| --- | --- | --- |
| Elegir columnas | `select(...)` | Selección de columnas |
| Añadir una derivada | `with_columns(...)` | Asignación o `assign` |
| Elegir filas | `filter(condicion)` | Máscara booleana |
| Resumir por fecha | `group_by(...).agg(...)` | Agrupación y agregación |
| Expresar una columna | `pl.col(...)` | No equivale a extraer una Series y alinear por índice |

La tabla orienta preguntas; no promete firmas, tipos ni reglas de faltantes
idénticas. Consulta la [introducción de pandas](../../02_pandas/README.md)
si necesitas repasar su modelo. Evita traducir cada línea mecánicamente o
introducir una función Python por fila cuando bastan las expresiones mostradas.

Como extensión, usa el generador incluido en
[10.01](../01_question_contract_reference/referencia.py): crea una carpeta nueva
en `output/`, genera `escala.csv` con `creditos=20` y tendrás 40 filas, dos cortes
y 20 IDs. Es una fórmula determinista con claves únicas, no duplicación de seis
filas. Pasa esa ruta a `cargar_tabla`, `comprobar_seleccion` y `comprobar_resumen`;
ya no impongas 2600/4500/4600 como respuestas a otra fuente. El lab incluye el
recorrido completo. No atribuyas ventajas de rendimiento a esta muestra pequeña.

## Práctica, criterio de salida y siguiente paso

Realiza el [lab 10.02](../../../labs/10_polars_duckdb/02_polars_tables_expressions/README.md).
Puedes explicar qué filas/columnas produce cada contexto, conservar las seis
observaciones originales, comprobar pares y resumen desde una sesión nueva,
y justificar el vacío y la ampliación de enteros antes de avanzar.

Proyecto `04_large_credit_dataset` y checkpoints siguen planificados; no hay
checkpoint activo asociado. Desarrollar material no acredita práctica del estudiante.
Siguiente: [10.03 — Polars lazy y planes de consulta](../03_polars_lazy_plans/README.md).
Al retomar, consulta [PROGRESS.md](../../../PROGRESS.md).

## Referencias y atribución

Ejemplos propios con datos ficticios; consulta de fuentes oficiales: 2026-10-23.
Los ejemplos se ejecutaron con Polars 2.0.0, no se presupone que la documentación
«stable» conserve siempre esa versión.

- [Tipos y estructuras](https://docs.pola.rs/user-guide/concepts/data-types-and-structures/).
- [Expresiones y contextos](https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/).
- [Lectura CSV y parámetros](https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html).
- [Agregaciones](https://docs.pola.rs/user-guide/expressions/aggregation/).
- [Suma y tipos enteros](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.sum.html).
- [Migración desde pandas](https://docs.pola.rs/user-guide/migration/pandas/).
- [Instalación](https://docs.pola.rs/user-guide/installation/) y
  [distribución Polars 2.0.0](https://pypi.org/project/polars/2.0.0/).

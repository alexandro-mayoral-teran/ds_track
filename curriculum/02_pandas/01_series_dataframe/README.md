# 02.01 — Series y DataFrame

<a id="01--series-y-dataframe"></a>

[Inicio](../../../README.md) / [Módulo 02](../README.md) / **Lección 02.01**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Representar registros como una tabla y reconocer su estructura |
| **Necesitas** | Python del módulo 00; preparación de pandas en el apartado 2 |
| **Evidencia** | Script adaptado o notebook alternativo, con formas y consultas comprobadas |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/02_pandas/01_series_dataframe/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Representar registros como una tabla y explicar sus partes antes de leer archivos
o hacer limpieza.

## Antes de empezar

Completa [01 — Python fundamental](../../01_python_foundations/README.md).
Usa el entorno que elegiste en [00.05](../../00_getting_started/05_environment/README.md).
El apartado 2 explica cómo preparar y comprobar pandas con tu gestor; la versión
de referencia es 2.3.3. No necesitas otro entorno ni instalar todos los gestores.
Las tres ventas están definidas en la página y el script, sin archivos CSV
ni vocabulario crediticio todavía.

## Qué vas a aprender

- Distinguir Series y DataFrame por su forma y significado.
- Leer filas, columnas, índice y tipos con los atributos y métodos del ejemplo.
- Localizar un valor por etiqueta o posición sin confundir ambas consultas.
- Predecir cómo cambia la estructura al agregar un registro.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script](series_dataframe.py) | Inspeccionar formas, tipos y consultas de tres ventas | Ejemplo |
| [Notebook](../../../labs/02_pandas/01_series_dataframe/practica.ipynb) | Explorar y modificar las ventas por celdas | Opcional |

Abre los recursos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y contrasta sus resultados esperados. Conserva los originales y
trabaja las variantes en tu copia. Los datos compartidos se reutilizan desde
su ubicación actual, sin duplicarlos.

## 1. Para qué sirve pandas

Con listas y diccionarios aprendiste a representar datos y recorrerlos. pandas
ofrece estructuras y operaciones para trabajar con tablas: seleccionar columnas,
aplicar reglas, combinar datos y resumirlos. Estas operaciones se introducirán
gradualmente; la biblioteca no decide por ti qué significa un registro válido.

Una tabla en pandas vive en memoria. No es una hoja de cálculo con fórmulas en
celdas ni una base de datos que guarda cambios automáticamente. Imprimirla muestra
una representación; conservarla en un archivo será parte de la siguiente lección.

## 2. Preparar pandas en tu entorno

Esta lección utiliza **pandas 2.3.3 como versión de referencia**, comprobada con
Python 3.12. No significa que sea la versión más reciente. Se registra en
[pyproject.toml](../../../pyproject.toml) y [uv.lock](../../../uv.lock).
Python 3.11 o posterior es el requisito declarado del proyecto.

Elige **solo el recorrido que ya usas**. Si pandas ya está instalado, comprueba
su versión antes de cambiarlo; si es otra, algunos tipos o formatos mostrados
pueden variar. No necesitas instalar herramientas de gráficos en esta lección.

### Conda

En Anaconda Prompt o el shell donde ya configuraste Conda:

```text
# Usa el entorno de estudio, no base
conda activate ds-track
# Instala la versión de referencia en ese entorno
conda install pandas=2.3.3
# Comprueba intérprete y versión
python -c "import sys, pandas as pd; print(sys.executable); print(pd.__version__)"
```

Si tu entorno tiene otro nombre, utiliza ese nombre. Conserva su configuración
siguiendo el [recorrido Conda](../../00_getting_started/05_environment/conda.md).

### venv y pip

Con el entorno de estudio activado, los comandos son iguales en PowerShell y
Bash/Zsh:

```text
# Instala en el Python activo
python -m pip install "pandas==2.3.3"
# Confirma qué Python utiliza la biblioteca
python -c "import sys, pandas as pd; print(sys.executable); print(pd.__version__)"
```

Conserva el requisito en tu archivo local de dependencias como aprendiste en
[venv y pip](../../00_getting_started/05_environment/venv-pip.md).
No ejecutes pip dentro de un entorno administrado por uv para agregar paquetes.

### uv: entorno del proyecto

Desde la raíz de ds_track, fuera de los entornos de otros gestores:

```text
# Instala las dependencias ya declaradas, sin modificar el lockfile
uv sync --locked
# Comprueba el Python del proyecto
uv run --locked python -c "import sys, pandas as pd; print(sys.executable); print(pd.__version__)"
```

Ahora usamos la configuración de la raíz porque pandas es una dependencia real
del curso. El mini proyecto uv del nivel 0 era una práctica independiente:
no ejecutes estos comandos desde .environment-practice/uv-demo. No necesitas
uv add; el requisito ya está declarado. Si usas un notebook, selecciona el kernel
del mismo entorno y sigue la [lección de notebooks](../../00_getting_started/06_first_notebook/README.md).

## 3. De registros a DataFrame

```python
import pandas as pd

registros = [
    {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
    {"producto": "lápiz, azul", "unidades": 5, "precio_unitario_mxn": 10},
    {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
]
tabla = pd.DataFrame(registros)
```

`pd` es un alias del módulo. `pd.DataFrame(...)` construye la tabla a partir
de una lista de diccionarios: cada diccionario aporta una fila y sus claves
identifican las columnas. `tabla` es un nombre elegido por nosotros.
No necesitas diseñar una clase para utilizar esta estructura.

| Índice | producto | unidades | precio_unitario_mxn |
| --- | --- | --- | --- |
| 0 | cuaderno | 2 | 40 |
| 1 | lápiz, azul | 5 | 10 |
| 2 | carpeta | 1 | 35 |

Cada fila representa una venta; unidades y precio describen esa venta.
El índice que aparece a la izquierda etiqueta las filas y no cuenta como una
de las tres columnas de datos. Su secuencia inicial es 0, 1, 2.

## 4. Leer la estructura: atributos y métodos

```python
print(tabla.shape)       # (3, 3): filas y columnas
print(tabla.columns)     # Nombres de columnas
print(tabla.index)       # Etiquetas de las filas
print(tabla.dtypes)      # Tipo de cada columna
```

Estos elementos son **atributos**: se consultan sin paréntesis. `shape` es una
tupla; su primer componente corresponde a filas y el segundo a columnas.
`len(tabla)` cuenta filas. `columns` e `index` son objetos de pandas, no listas
comunes; `list(tabla.columns)` permite mostrar sus elementos como lista.

Un **método** realiza una operación y se llama con paréntesis, por ejemplo
`tabla["unidades"].sum()`. Usar `tabla.shape()` produce un error porque intenta
llamar a una tupla como si fuera una función.

### Qué indican los tipos

En la versión y muestra de referencia:

```text
producto               object
unidades                int64
precio_unitario_mxn     int64
```

Los tipos describen las columnas. `int64` representa enteros; `object` es un
tipo general que aquí contiene texto, pero no garantiza que una columna tenga
solo cadenas. En otras versiones o con tipos explícitos puede aparecer un tipo
de texto diferente. No memorices la salida como regla universal.

Crear un DataFrame no valida el contrato. Si introdujeras `"cinco"` entre las
unidades, tener una tabla no convertiría ese texto en 5. Conversión, faltantes y
reglas se desarrollan después. Tampoco hay que sumar precios unitarios como si
fueran el total vendido: el significado de cada medida sigue siendo necesario.

## 5. Series frente a DataFrame

```python
unidades = tabla["unidades"]        # Series
tabla_unidades = tabla[["unidades"]]  # DataFrame con una columna

print(type(unidades).__name__)      # Series
print(unidades.shape)               # (3,)
print(tabla_unidades.shape)          # (3, 1)
print(unidades.sum())               # 8 unidades
```

Una Series tiene un eje de etiquetas y un dtype; puede representar una columna
y también existir por separado:

```python
unidades_sueltas = pd.Series([2, 5, 1], name="unidades")
```

Un DataFrame tiene filas y columnas. En `tabla[["unidades"]]`, la lista interior
contiene los nombres solicitados, mientras los corchetes exteriores seleccionan.
Para varias columnas se usa la misma idea:

```python
vista = tabla[["producto", "unidades"]]  # Forma (3, 2)
```

La coma de lápiz, azul es parte del texto; aquí no estamos interpretando un CSV.
Sumar la columna unidades reproduce el cálculo 2 + 5 + 1 = 8. Cálculos entre
columnas y agregaciones más amplias se estudiarán en sus respectivas lecciones.

## 6. Índice, etiqueta y posición

Las etiquetas pueden ser texto. Creamos una copia para mostrarlo sin cambiar
la tabla original:

```python
etiquetada = tabla.copy()
etiquetada.index = ["venta_a", "venta_b", "venta_c"]

print(etiquetada.loc["venta_b", "producto"])  # lápiz, azul
print(etiquetada.iloc[1, 0])                  # lápiz, azul
```

`loc` utiliza etiquetas de fila y columna; `iloc` utiliza posiciones que empiezan
en cero. Ambas encuentran el mismo valor en esta tabla, por razones distintas.
La posición 1 es la segunda fila; su etiqueta ahora es venta_b.

Si las etiquetas son números, loc continúa interpretándolos como etiquetas,
no como posiciones. El índice no garantiza por sí mismo una clave única o estable:
estas etiquetas didácticas no sustituyen un identificador de venta de la fuente.
Un cambio de orden puede cambiar posiciones sin cambiar las etiquetas.
Filtros y selección de conjuntos se profundizan en la lección 03.

## 7. Ejecutar el ejemplo completo

El [script series_dataframe.py](series_dataframe.py) reúne estos pasos. Los datos
están dentro del programa; no lee ni escribe archivos. Su función crear_tabla
declara las tres columnas para conservar la estructura incluso con una lista vacía.
Eso no añade validación de claves o tipos a registros externos.

### PowerShell

Desde la raíz, con Conda o venv activado:

```powershell
python curriculum\02_pandas\01_series_dataframe\series_dataframe.py
```

Sin activar venv, usa `.\.venv-practice\Scripts\python.exe` en lugar de python.

### Bash/Zsh

```bash
python curriculum/02_pandas/01_series_dataframe/series_dataframe.py
```

Sin activar venv, usa `./.venv-practice/bin/python`.

### uv

Desde la raíz:

```text
uv run --locked python curriculum/02_pandas/01_series_dataframe/series_dataframe.py
```

Comprueba: forma (3, 3), índice [0, 1, 2], Series (3,), DataFrame de una
columna (3, 1), total de unidades 8 y el mismo producto consultado por loc/iloc.
El espaciado al imprimir puede variar; contrasta valores y estructura.

## Errores frecuentes

| Situación | Qué revisar |
| --- | --- |
| ModuleNotFoundError: pandas | Instalación y Python/kernel elegido |
| KeyError al consultar una columna | Nombre exacto y mayúsculas |
| KeyError en loc | La etiqueta solicitada debe existir |
| IndexError en iloc | La posición debe estar dentro de la tabla |
| Error al asignar index | Cantidad de etiquetas igual a cantidad de filas |
| Tipos inesperados | Valores de origen y versión; una tabla no valida por sí sola |

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 02.01](../../../labs/02_pandas/01_series_dataframe/README.md) para
adaptar una tabla y comprobar formas, tipos y consultas.

Si eliges explorar por celdas, abre el
[notebook del lab](../../../labs/02_pandas/01_series_dataframe/practica.ipynb)
junto al script y selecciona el kernel del mismo entorno. Reinicia y ejecuta
todas las celdas al comprobar; esta alternativa no añade otro lab obligatorio.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu script modificado o el notebook alternativo junto al script | Formas y tipos de la tabla y de las selecciones | Cómo distinguir una Series de un DataFrame |
| Nota con consultas y resultados | El mismo valor al consultar la etiqueta y posición correctas | Por qué el índice no es automáticamente el identificador del registro |

Puedes avanzar cuando expliques la estructura, distingas Series/DataFrame y
localices un valor sin confundir etiqueta y posición. No necesitas leer un CSV
ni hacer limpieza para demostrar esta primera habilidad.

Quien aprende modifica y ejecuta su copia y explica lo que comprobó.
Tu compañero señala una columna y una etiqueta y te pide anticipar la forma y el valor de la consulta.
Guarda evidencia, ayudas y dudas en una nota personal junto a tu práctica;
PROGRESS.md registra el desarrollo editorial del curso. El material disponible
no acredita por sí solo aprendizaje completado.

El proyecto de limpieza y sus checkpoints siguen previstos, sin proyecto
asociado implementado ni práctica adicional de proyecto obligatoria.

<a id="siguiente-paso-y-referencias"></a>

## Referencias

- [Primeras estructuras tabulares](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html).
- [DataFrame, pandas 2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.html).
- [loc](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.loc.html) e
  [iloc](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.iloc.html).
- [Instalación oficial](https://pandas.pydata.org/docs/getting_started/install.html).

## Siguiente paso

Después del lab y su comprobación, continúa con [02.02 — Leer, inspeccionar y exportar](../02_read_inspect_export/README.md)
antes de realizar su lab.

[← Módulo 02](../README.md) · [Lab 02.01](../../../labs/02_pandas/01_series_dataframe/README.md) · [Siguiente →](../02_read_inspect_export/README.md)

# 03 — Seleccionar, filtrar y ordenar

## Propósito y prerrequisitos

Responder una pregunta con parte de una tabla, conservando la fuente y explicando
qué filas se incluyen. Completa [Leer, inspeccionar y exportar](../02_read_inspect_export/README.md)
y su lab; utiliza el mismo entorno con pandas 2.3.3.

Trabajaremos con [cartera_demo.csv](../02_read_inspect_export/cartera_demo.csv),
sus seis créditos ficticios y el diccionario de la lección anterior. No duplicamos
la muestra. Esta lección enseña selección y orden; convertir, crear columnas y
limpiar datos se desarrollará después.

Al terminar podrás elegir columnas, usar loc/iloc, construir condiciones,
combinar máscaras, ordenar con desempate y comprobar una selección vacía.

## 1. Primero definir la pregunta

Buscamos **saldo de al menos 500 MXN y atraso conocido de al menos 5 días**.
Después mostramos esos registros de mayor a menor saldo. Los umbrales son
decisiones didácticas; no representan una regla de riesgo o cobranza.

| Operación | Qué cambia | Ejemplo |
| --- | --- | --- |
| Seleccionar columnas | Campos que se muestran | ID, segmento y saldo |
| Filtrar filas | Registros que se incluyen | Saldo ≥ 500 y atraso ≥ 5 |
| Ordenar | Posición en la presentación | Mayor saldo primero |

Filtrar no demuestra que las filas excluidas sean incorrectas. Solo delimita
la pregunta. Ordenar tampoco valida ni elimina duplicados.

## 2. Elegir columnas y recordar loc/iloc

Los siguientes fragmentos utilizan tabla, leída con el contrato de 02.02.
El [script completo](select_filter_sort.py) incluye esa lectura y las funciones.

```python
saldo = tabla["saldo_mxn"]                     # Series
vista = tabla[["id_credito", "saldo_mxn"]]     # DataFrame (6, 2)
vista = tabla.loc[:, ["id_credito", "saldo_mxn"]]  # Todas las filas; esas columnas
primeras = tabla.iloc[:2, :2]                  # Dos primeras filas y columnas
```

En loc, la coma separa selección de filas y columnas. `:` significa todas en
ese eje. En iloc se usan posiciones; `:2` llega hasta antes de la posición 2,
como los slices de Python. La lista de nombres mantiene el orden solicitado.

Sobre el índice inicial 0, 1, 2…, `tabla.loc[0:2]` incluye las etiquetas 0, 1 y 2,
mientras `tabla.iloc[0:2]` toma las posiciones 0 y 1. Un slice de etiquetas loc
incluye el extremo final cuando está presente. No generalices posiciones a etiquetas.

No hace falta cambiar el índice para filtrar por id_credito: es una columna de
texto que identifica el crédito ficticio y conserva sus ceros iniciales.

## 3. Una comparación produce una máscara

```python
mascara_saldo = tabla["saldo_mxn"] >= 500
print(mascara_saldo)
seleccion_saldo = tabla.loc[mascara_saldo]
```

La comparación se aplica a cada elemento y devuelve una Series de valores lógicos
con el mismo índice. La máscara indica qué filas incluir; no es una tabla de
resultados ni modifica la fuente.

En nuestra muestra saldo ≥ 500 incluye todos salvo 004, que tiene saldo cero.
`>=` incluye el límite: 006, con 500 MXN, también se selecciona. `>` lo excluiría.
Para comparar igualdad se utiliza `==`, no la asignación `=`.

## 4. Combinar condiciones: &, | y ~

```python
mascara = (tabla["saldo_mxn"] >= 500) & (tabla["dias_atraso"] >= 5)
seleccion = tabla.loc[mascara.fillna(False)]
```

Cada comparación va entre paréntesis; `&` combina las Series elemento a elemento.
No sustituirlo por and: and intenta decidir el valor lógico de una Series completa
y suele producir «The truth value of a Series is ambiguous».

| Operador | Idea | Uso |
| --- | --- | --- |
| `&` | Ambas condiciones | Saldo suficiente y atraso suficiente |
| `\|` | Al menos una | Un saldo o un atraso que cumple el umbral |
| `~` | Negación de una máscara | Invertir una condición lógica |

```python
alternativa = (tabla["saldo_mxn"] >= 1000) | (tabla["dias_atraso"] >= 30)
no_consumo = ~(tabla["segmento"] == "consumo")
segmentos = tabla["segmento"].isin(["consumo", "servicios"])
```

isin pregunta si cada valor está en una colección. No usar
`tabla["segmento"] in ["consumo", "servicios"]`: in no realiza aquí la comparación
elemento a elemento que necesitas. Las condiciones deben responder una pregunta
explícita; cambiar & por | cambia el conjunto obtenido.

## 5. Un resultado desconocido no equivale a cero

dias_atraso usa Int64 y contiene un `<NA>`. Compararlo puede producir una máscara
lógica con True, False o `<NA>`:

| ID | Saldo ≥ 500 | Atraso ≥ 5 | Ambas |
| --- | --- | --- | --- |
| 001 | True | False | False |
| 002 | True | True | True |
| 003 | True | True | True |
| 004 | False | False | False |
| 005 | True | Desconocido | Desconocido |
| 006 | True | True | True |

`mascara.fillna(False)` hace explícita la decisión de **incluir solo condiciones
confirmadas**. Cambia la máscara utilizada, no los datos de tabla. loc con una
máscara nullable también trata NA como no seleccionado; aquí documentamos esa
política en lugar de dejarla implícita.

Para mantener visible lo que falta evaluar:

```python
desconocidos = tabla.loc[tabla["dias_atraso"].isna()].copy()
```

isna detecta ausencia. No usamos dias_atraso == 0 ni lo rellenamos con cero.
El detalle de causas y tratamiento de faltantes se desarrolla en 05.

La lógica de tres valores importa: `True | <NA>` es True y `False & <NA>` es
False, porque en esos casos ya se puede determinar el resultado. Por ello una
fila con atraso desconocido puede entrar en otra pregunta si la condición de
saldo por sí sola basta. No afirmar que todo NA excluye siempre una fila.

También `~<NA>` sigue desconocido. Si necesitas una partición explícita, decide
primero qué hacer con NA; negar una máscara sin esa decisión no reúne necesariamente
todos los registros que faltan. Selección y desconocidos tampoco suman aquí la
entrada completa: existen registros conocidos que no cumplen el filtro.

## 6. Seleccionar filas y columnas en un paso

```python
columnas = ["id_credito", "segmento", "saldo_mxn", "dias_atraso"]
seleccion = tabla.loc[mascara.fillna(False), columnas].copy()
```

El resultado tiene tres filas y cuatro columnas, con índices originales 1, 2 y 5.
La máscara se construye desde la misma tabla; pandas alinea una Series lógica
por etiquetas. No reutilices sin revisar una máscara creada antes de cambiar
el conjunto o el índice: puede desalinearse o dejar de expresar la pregunta.

copy crea una tabla de trabajo independiente para esta muestra de valores simples.
No editaremos columnas en esta lección, pero evitamos depender de modificar una
vista o una selección encadenada. Asignación con loc y copias se profundizan en 04.

## 7. Ordenar y definir los empates

```python
ordenada = seleccion.sort_values(
    by=["saldo_mxn", "id_credito"],
    ascending=[False, True],
    na_position="last",
)
```

by indica las columnas de ordenación. False solicita saldo descendente;
True solicita ID ascendente para desempatar. El ID sigue siendo texto: se ordena
como texto, no como una cantidad. Los tres dígitos de la muestra facilitan su lectura.
na_position="last" sitúa los faltantes al final si los campos ordenados los contienen.
sort_values devuelve otra tabla y no cambia la fuente con esta llamada.

| Índice original | ID | Saldo MXN | Días de atraso |
| --- | --- | --- | --- |
| 1 | 002 | 1500 | 10 |
| 2 | 003 | 750 | 45 |
| 5 | 006 | 500 | 5 |

El subtotal es **2750 MXN**, correspondiente solo a la selección. El origen tiene
6000 MXN y no debe confundirse con ese subtotal. El crédito 005 permanece aparte,
con saldo 2250 MXN y atraso desconocido.

Si solo se ordena por saldo, no se ha definido qué orden deben tener saldos iguales.
Una segunda clave explícita hace reproducible el desempate en este caso. No usar
head para elegir «los mayores» antes de ordenar: head solo toma las primeras filas.

## 8. Después de filtrar, etiqueta y posición siguen siendo distintas

```python
print(ordenada.iloc[0]["id_credito"])  # 002, primera posición
print(ordenada.loc[1, "id_credito"])  # 002, etiqueta original 1
```

`ordenada.loc[0]` produciría KeyError: la etiqueta 0 ya no está en esta selección.
Filtrar y ordenar no renumeran automáticamente el índice.

```python
presentacion = ordenada.reset_index(drop=True)
```

reset_index(drop=True) crea un índice consecutivo sin guardar el anterior como
una columna. No cambia id_credito. El script conserva el índice durante la selección
y lo normaliza solo al comparar la salida recargada: to_csv(index=False) no exporta
las etiquetas originales y read_csv crea un índice nuevo.

## 9. Caso sin coincidencias y exportación

```python
sin_coincidencias = tabla.loc[tabla["saldo_mxn"] >= 10000, columnas].copy()
if sin_coincidencias.empty:
    print("No hay coincidencias para este filtro")
```

La tabla vacía conserva cuatro columnas. No consultar iloc[0] sin comprobar que
exista una fila. Un filtro vacío no necesariamente es un error; puede ser una
respuesta válida a la pregunta.

El script exporta la selección sin índice y la vuelve a leer con tipos acordados.
También comprueba que la tabla de entrada no cambió. La salida de una selección
vacía conserva el encabezado; sum(min_count=1) informa ausencia de observaciones
en vez de presentar cero como un subtotal medido.

El programa no valida todas las reglas de una cartera. Al ejecutar con otra
entrada, comprueba claves, política de faltantes y resultado esperado, no solo
que se genere el archivo. Cada ejecución reemplaza su salida; una falla puede
dejar resultados anteriores o incompletos, como se explicó en 02.02.

## 10. Ejecutar el ejemplo completo

### PowerShell

Desde la raíz y con el entorno activado:

```powershell
# Filtrar, ordenar, conservar desconocidos aparte y comprobar una exportación
python curriculum\02_pandas\03_select_filter_sort\select_filter_sort.py
# Revisar el resultado escrito
Get-Content curriculum\02_pandas\03_select_filter_sort\output\creditos_seleccionados.csv -Encoding utf8
```

Sin activar venv, usa `.\.venv-practice\Scripts\python.exe` en lugar de python.

### Bash/Zsh

```bash
python curriculum/02_pandas/03_select_filter_sort/select_filter_sort.py
cat curriculum/02_pandas/03_select_filter_sort/output/creditos_seleccionados.csv
```

Sin activar venv, usa `./.venv-practice/bin/python`.

### uv

Desde la raíz, con la configuración del proyecto:

```text
uv run --locked python curriculum/02_pandas/03_select_filter_sort/select_filter_sort.py
```

Resultado esperado: entrada 6, seleccionados 3, subtotal 2750 MXN, un registro
con atraso desconocido y orden 002 → 003 → 006. La fuente sigue en la lección 02;
la copia generada está en output de esta lección y queda ignorada por Git.

## Errores frecuentes

| Situación | Qué revisar |
| --- | --- |
| Truth value of a Series is ambiguous | and/or en lugar de &/\| para Series |
| Condición combinada incorrecta | Paréntesis alrededor de cada comparación |
| KeyError después de filtrar | Etiqueta ausente o nombre de columna incorrecto |
| IndexError en iloc[0] | Selección vacía |
| Máscara no alineada | Tabla e índice con los que se construyó |
| Subtotal inesperado | >= frente a >, & frente a \| y política de NA |
| Orden inesperado | Claves, dirección y desempate explícitos |

## Práctica, criterio de salida y siguiente paso

Realiza el [lab 02.03](../../../labs/02_pandas/03_select_filter_sort/README.md).
Puedes avanzar cuando predigas y compruebes IDs, orden y subtotal, expliques
el tratamiento de lo desconocido y resuelvas un filtro vacío sin modificar la fuente.
No hay checkpoint implementado; el proyecto de limpieza sigue previsto.

Continúa con [04 — Tipos y columnas calculadas](../04_types_calculated_columns/README.md)
antes de realizar su lab.

## Referencias oficiales

- [Selección e índices](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/indexing.html).
- [Máscaras con valores desconocidos](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/boolean.html).
- [sort_values](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sort_values.html).
- [loc](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.loc.html) e
  [iloc](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.iloc.html).
- [isin](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.isin.html) y
  [reset_index](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.reset_index.html).

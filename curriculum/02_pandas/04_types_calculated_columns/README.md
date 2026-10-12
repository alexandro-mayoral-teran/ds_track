# 04 — Tipos y columnas calculadas

## Propósito, prerrequisitos y objetivos

Convertir columnas de texto en cantidades y calcular sobre una tabla completa,
sin escribir un ciclo por registro. Completa [Seleccionar, filtrar y ordenar](../03_select_filter_sort/README.md)
y su lab; conserva el entorno con pandas 2.3.3. Las funciones y el ciclo sobre
nombres de columnas retoman [Python fundamental](../../01_python_foundations/README.md).

Al terminar podrás explicar un dtype, distinguir ausencia de conversión fallida,
crear columnas por operaciones entre Series y modificar una copia con loc.
El detalle de limpieza, duplicados y reglas de aceptación corresponde a la lección 05.

## 1. Una muestra más amplia para explorar

[cartera_conversion.csv](cartera_conversion.csv) contiene **40 registros sintéticos**.
Es una muestra nueva: las seis filas de las lecciones anteriores siguen intactas.
Cada fila representa un crédito ficticio en un corte; no hay datos de personas.

| Campo de entrada | Significado | Tratamiento en esta práctica |
| --- | --- | --- |
| id_credito | Identificador de tres dígitos | Texto; conservar ceros iniciales |
| segmento | Categoría ficticia | Texto; cuatro categorías |
| fecha_corte | Corte 2026-09-30 | Texto; fechas se estudiarán en 06 |
| saldo_mxn | Importe de referencia en pesos | Entero pequeño o dato sin interpretar |
| pago_mxn | Importe ficticio a restar | Entero pequeño o dato sin interpretar |
| dias_atraso | Conteo de días completos | Entero o dato sin interpretar |

Los importes se eligieron en **pesos enteros**, sin centavos. Esta decisión permite
practicar Int64 y restas exactas; no es un formato universal para dinero. Si una
entrada admite centavos, hay que definir otra representación, por ejemplo enteros
en centavos. No truncaremos una fracción para hacerla encajar en este contrato.

La resta saldo − pago es un ejercicio aritmético; no modela intereses ni amortización.
Los umbrales de atraso también son didácticos. Se conservan todas las filas,
incluidas las que no permiten calcular algún resultado.

## 2. Leer como texto antes de interpretar

```python
import pandas as pd

# entrada es la ruta al CSV; el script completo la construye con pathlib
tabla = pd.read_csv(
    entrada, dtype="string", encoding="utf-8-sig",
    keep_default_na=False, na_values=[""],
)
print(tabla.dtypes)  # Las seis columnas son string
```

dtype establece el tipo de las columnas. string mantiene "001" como identificador
y "1250" como texto. **Que un texto parezca un número no significa que ya sea una cantidad.**
Sumar dos textos puede concatenarlos: "1250" + "100" da "1250100".

keep_default_na=False desactiva la lista automática de textos interpretados como
faltantes; na_values=[""] declara que aquí solo el campo vacío representa ausencia.
Así, "error", "pendiente" y "no_dato" siguen visibles para revisión. La lectura
no conserva todos los detalles del archivo, como comillas originales: conserva
los valores interpretados por el lector CSV.

## 3. Interpretar números: to_numeric y astype

Son dos pasos relacionados, con propósitos distintos:

| Operación | Pregunta que responde | Ejemplo |
| --- | --- | --- |
| pd.to_numeric | ¿Este texto representa un número? | "1250" → 1250 |
| astype("Int64") | ¿Cómo almacenar los valores interpretados? | Enteros con posibilidad de NA |

```python
texto = pd.Series(["1250", "error", pd.NA, "3.5"], dtype="string")
numero = pd.to_numeric(texto, errors="coerce")
print(numero)
```

1250 y 3.5 se interpretan; "error" pasa a faltante. El dato ya ausente también
sigue ausente. Dependiendo del tipo de entrada, ese resultado puede mostrarse
como NaN o `<NA>`; revisa dtypes e isna, no solo su representación en pantalla.

errors="raise", el comportamiento predeterminado, detiene la conversión ante un
texto incompatible. errors="coerce" permite continuar, **pero requiere registrar
qué texto no se convirtió**. No significa que el dato sea correcto o que valga cero.

```python
fallo_texto = texto.notna() & numero.isna()
```

notna indica que había un valor; isna indica que no quedó número. Solo "error"
cumple ambas condiciones. El campo ausente no es una conversión fallida.

## 4. Un número puede incumplir el tipo requerido

"3.5" es numérico, pero no es un conteo de días completos para este contrato.
El [script completo](types_calculated_columns.py) utiliza esta función:

```python
def convertir_entero(texto):
    numero = pd.to_numeric(texto, errors="coerce")
    es_entero = numero.notna() & (numero % 1 == 0)
    incompatible = (texto.notna() & ~es_entero).astype("boolean")
    convertido = numero.where(es_entero).astype("Int64")
    return convertido, incompatible
```

1. to_numeric interpreta los valores posibles.
2. `% 1` obtiene la parte fraccionaria; cero confirma un valor entero en esta muestra.
3. incompatible señala un valor presente que no cumple el contrato de entero.
4. where conserva los números cuya condición es verdadera y deja faltantes en el resto.
5. astype("Int64") almacena enteros y `<NA>`; retorna también la máscara de incompatibles.

Esta función está pensada para las cantidades pequeñas de la práctica; no es un
lector universal de números, separadores de miles ni valores fuera del rango Int64.
No convierte automáticamente "1,250" en 1250 ni redondea 3.5 a 3 o 4.

| Tipo | Para qué lo usamos |
| --- | --- |
| string | Identificadores y textos |
| Int64, con I mayúscula | Cantidades enteras que pueden faltar |
| Float64, con F mayúscula | Porcentajes fraccionarios que pueden faltar |
| boolean | Máscaras que admiten valores desconocidos |

int64 de NumPy y Int64 de pandas son tipos distintos: el primero no almacena
pd.NA como entero nullable. Cambiar el nombre a minúsculas no es un detalle decorativo.

## 5. Conservar la fuente y crear columnas calculadas

```python
resultado = tabla.copy()
for columna in ["saldo_mxn", "pago_mxn", "dias_atraso"]:
    resultado[columna + "_texto"] = tabla[columna]
    convertido, incompatible = convertir_entero(tabla[columna])
    resultado[columna] = convertido
    resultado[columna + "_incompatible"] = incompatible

resultado["saldo_despues_pago_mxn"] = resultado["saldo_mxn"] - resultado["pago_mxn"]
```

El ciclo recorre **tres columnas**, no 40 filas. La resta se aplica a las Series
completas: es una operación vectorizada. No necesitas iterrows ni apply para
esta aritmética. Vectorizar expresa la operación por columna; no garantiza que
cualquier operación sea rápida con cualquier volumen.

Para 001: 1250 − 100 = **1150 MXN**. Para 002: 1500 − 200 = **1300 MXN**.
Si falta saldo o pago, la resta queda desconocida. Un pago cero conocido sí
permite restar; un pago vacío no equivale a cero.

Cada campo numérico conserva un compañero _texto y una marca _incompatible.
Así podemos revisar "error" aunque el saldo convertido sea NA. La tabla de origen
no se modifica; el resultado tiene 40 filas y 15 columnas.

### Alineación por índice

Al combinar Series, pandas empareja **etiquetas**, no simplemente posiciones:

```python
a = pd.Series([100, 200], index=["A", "B"], dtype="Int64")
b = pd.Series([20, 10], index=["B", "A"], dtype="Int64")
print(a - b)  # A: 90; B: 180
```

No se obtiene 80 y 190: el 100 de A se combina con el 10 de A.
Si las etiquetas no coinciden, pueden aparecer faltantes. En nuestro cálculo ambas
Series salen de resultado y comparten índice. No reinicies el índice de una sola
columna filtrada antes de asignarla sin comprobar qué fila representa.

## 6. Un porcentaje necesita un denominador definido

```python
# Solo evaluar el porcentaje cuando el saldo es positivo
denominador = resultado["saldo_mxn"].where(resultado["saldo_mxn"] > 0)
resultado["porcentaje_pago"] = (
    resultado["pago_mxn"] / denominador * 100
).astype("Float64")
```

where deja NA donde el saldo no es positivo. Evitamos dividir entre cero y
conservar un infinito como si fuera un porcentaje útil. Para 001: 100 / 1250 × 100
= **8 %**. Para 028, saldo y pago son cero: la resta es cero, el porcentaje es NA.
Si falta pago, también falta porcentaje.

Los porcentajes usan coma flotante y pueden tener aproximaciones; redondear para
mostrar no es lo mismo que cambiar la precisión del dato almacenado. No sumes
porcentajes individuales para obtener automáticamente un porcentaje del conjunto.

## 7. Asignar con loc y controlar qué tabla cambia

```python
resultado["estado_atraso"] = pd.Series(
    "sin dato evaluable", index=resultado.index, dtype="string"
)
conocido = resultado["dias_atraso"].notna()
resultado.loc[conocido, "estado_atraso"] = "menos de 30 dias"
resultado.loc[(resultado["dias_atraso"] >= 30).fillna(False), "estado_atraso"] = "30 dias o mas"
```

Primero creamos la columna; luego modificamos filas y columna en una sola llamada
a loc. La última asignación cambia la categoría de los atrasos desde 30 inclusive.
Los días ausentes o incompatibles conservan "sin dato evaluable". Es una clasificación
didáctica de esta muestra no negativa, no una validación de cualquier archivo.

Evita la asignación encadenada `resultado[mascara]["estado_atraso"] = "..."`:
selecciona un objeto intermedio y no expresa de forma fiable qué tabla se modifica.
Para editar solo un subconjunto, crea `subtabla = resultado.loc[mascara].copy()`
y modifica subtabla conscientemente.

**Sobre Copy-on-Write:** en pandas 2.3.3 es una opción; en pandas 3.0 pasa a ser
el comportamiento predeterminado. No dependemos de activar esa opción: usamos
una copia explícita y loc sobre el objeto previsto. copy basta para los valores
simples de esta muestra; no implica copiar recursivamente objetos Python anidados.

## 8. Comprobar con la misma base de filas

La muestra contiene estas excepciones deliberadas:

| ID | Campo | Valor de origen | Resultado |
| --- | --- | --- | --- |
| 005 | saldo_mxn | Vacío | Ausente; no incompatible |
| 009 | pago_mxn | pendiente | Incompatible |
| 014 | saldo_mxn | error | Incompatible |
| 018 | dias_atraso | Vacío | Ausente |
| 023 | dias_atraso | 3.5 | Numérico, incompatible con entero |
| 028 | saldo_mxn / pago_mxn | 0 / 0 | Resta 0, porcentaje NA |
| 033 | pago_mxn | Vacío | Ausente |
| 038 | dias_atraso | no_dato | Incompatible |

Hay **36 restas evaluables**: quedan sin resultado 005, 009, 014 y 033. Sobre
esas mismas 36 filas, saldo suma 217750, pago suma 6600 y la resta suma
**211150 MXN**. Comprobación: 217750 − 6600 = 211150.

No compares la suma de todos los saldos conocidos con la de todos los pagos conocidos:
sus universos difieren. El script delimita primero las filas con ambos operandos.
Usa sum(min_count=1) para no presentar un cero medido cuando no hay observaciones.

La exportación conserva las 40 filas, valores originales y marcas. Al releer, el
script declara los tipos: CSV no los guarda. Compara toda la tabla, tolerando una
diferencia de coma flotante de 1e-12 en valores aproximados; no redondea importes.
Cada ejecución reemplaza output/cartera_calculada.csv; revisa que haya terminado
correctamente antes de utilizar una salida que podría ser de otra ejecución.

## 9. Ejecutar el ejemplo

Desde la raíz, con el entorno que ya preparaste:

### PowerShell

```powershell
# Convertir, calcular y comprobar que la fuente no cambió
python curriculum\02_pandas\04_types_calculated_columns\types_calculated_columns.py
# Explorar la salida; output permanece ignorado por Git
Get-Content curriculum\02_pandas\04_types_calculated_columns\output\cartera_calculada.csv -Encoding utf8
```

### Bash/Zsh

```bash
python curriculum/02_pandas/04_types_calculated_columns/types_calculated_columns.py
cat curriculum/02_pandas/04_types_calculated_columns/output/cartera_calculada.csv
```

### uv

Con la configuración raíz del proyecto:

```text
uv run --locked python curriculum/02_pandas/04_types_calculated_columns/types_calculated_columns.py
```

Resultado: entrada/salida 40 filas; saldo con 1 ausente y 1 incompatible;
pago con 1 ausente y 1 incompatible; atraso con 1 ausente y 2 incompatibles.
No necesitas preparar otro entorno ni instalar paquetes adicionales.

## Práctica, errores frecuentes y siguiente paso

Realiza el [lab 02.04](../../../labs/02_pandas/04_types_calculated_columns/README.md).
Puedes avanzar cuando compruebes conversiones y cálculos, expliques un cero frente
a NA y concilies totales sobre las mismas filas conservando la fuente.

Si astype falla, revisa textos, fracciones y rango requerido. Si una resta concatena
o falla, revisa dtypes. Si aparecen NA inesperados, revisa operandos e índices.
Un programa que termina no demuestra por sí solo que todas las filas sean válidas.

No hay checkpoint implementado; el proyecto de limpieza sigue previsto.
Continúa con el [alcance de 05 — Faltantes, duplicados y reglas](../README.md#05-faltantes-duplicados-y-reglas),
todavía por desarrollar, antes de su futuro lab.

## Referencias oficiales

- [to_numeric](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.to_numeric.html) y
  [astype](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.astype.html).
- [Enteros con faltantes](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/integer_na.html).
- [Series.where](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.where.html).
- [Asignación e índices](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/indexing.html) y
  [Copy-on-Write](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/copy_on_write.html).

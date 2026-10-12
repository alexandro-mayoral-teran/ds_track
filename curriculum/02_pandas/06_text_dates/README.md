# 06 — Texto y fechas

## Propósito, prerrequisitos y objetivos

Interpretar categorías y fechas con reglas explícitas, conservando la entrada y
los casos que no se pudieron interpretar. Completa [Faltantes, duplicados y reglas](../05_missing_duplicates_rules/README.md)
y su lab; utiliza el mismo entorno con pandas 2.3.3.

Al terminar podrás usar métodos str, acordar equivalencias de categorías, convertir
fechas con formato declarado, extraer componentes con dt y seleccionar un período.
La agrupación se desarrolla en 07; comparar crédito por crédito mediante uniones,
en 08. No necesitas dominar expresiones regulares ni zonas horarias para avanzar.

## 1. Una muestra de dos cortes

[cartera_texto_fechas.csv](cartera_texto_fechas.csv) contiene **48 registros ficticios**:
24 posiciones en septiembre y 24 en octubre de 2026, con excepciones deliberadas.
Las muestras anteriores permanecen intactas.

| Campo | Significado | Contrato de esta práctica |
| --- | --- | --- |
| id_credito | Crédito ficticio | Texto de tres dígitos, tras quitar espacios exteriores |
| segmento | Categoría | consumo, servicios, comercio o educacion |
| fecha_corte | Día de la fotografía del saldo | Fecha calendario con forma YYYY-MM-DD |
| fecha_alta | Día de incorporación del crédito | Mismo formato; no posterior al corte |
| saldo_mxn | Saldo observado en ese corte | Entero de pesos, presente y no negativo |

La clave sigue siendo **ID + corte**. El mismo crédito en dos fechas tiene dos
observaciones legítimas. fecha_alta describe un evento; fecha_corte, una fotografía.
No confundir la diferencia entre estas fechas con días de atraso.

Los importes ya cumplen el contrato de lectura Int64; si otra fuente trae importes
incompatibles, hay que volver al proceso de conversión de 02.04. Esta lección se
concentra en texto y fechas, sin afirmar que se verificó cualquier regla imaginable.

## 2. Métodos str: operar sobre una columna de texto

```python
import pandas as pd

texto = pd.Series([" Consumo ", "SERVICIOS", "   ", pd.NA], dtype="string")
limpio = texto.str.strip().replace("", pd.NA)
normalizado = limpio.str.lower()
```

str permite aplicar operaciones de texto a la Series. strip quita espacios,
tabulaciones y saltos de línea **de los extremos**; no elimina espacios internos.
lower convierte letras a minúsculas. Las ausencias siguen siendo ausencias.

replace("", pd.NA) reemplaza el valor completo vacío después de strip. Así un
campo formado solo por espacios se reconoce como ausente. No convierte el texto
"no_dato" automáticamente en ausencia: esa equivalencia requeriría otra regla.

Estas llamadas devuelven Series: no cambian la columna original hasta que asignes
el resultado. El [script completo](text_dates.py) mantiene compañeros _original
antes de modificar ID, segmento y ambas fechas.

## 3. Normalizar categorías requiere un catálogo

```python
segmento = tabla["segmento"].str.strip().replace("", pd.NA).str.lower()
segmento = segmento.replace({"educación": "educacion"})
fuera_catalogo = segmento.notna() & ~segmento.isin(
    ["consumo", "servicios", "comercio", "educacion"]
)
```

| Entrada | Valor normalizado | Decisión |
| --- | --- | --- |
| " Consumo " | consumo | Categoría conocida |
| "SERVICIOS" | servicios | Categoría conocida |
| "Educación" | educacion | Equivalencia explícita del catálogo |
| "   " | NA | Ausente |
| "microcredito" | microcredito | Presente, fuera del catálogo |

replace con el diccionario cambia **valores completos**: no reemplaza fragmentos
de cualquier palabra. "educación superior" no se vuelve automáticamente "educacion".
Quitar todos los acentos o todos los espacios puede unir categorías que deberían
ser distintas. Aquí solo se declaró una equivalencia; no adivinamos categorías.

No alteramos la escritura original de nombres de personas ni identificadores
quitando caracteres arbitrariamente. El ID se conserva como texto: convertir
"001" a número perdería ceros y cambiaría su representación.

### Búsquedas de texto (práctica complementaria)

```python
mascara = segmento.str.contains("com", regex=False, na=False)
coincidencias = tabla.loc[mascara]
```

contains busca un fragmento. regex=False interpreta literalmente el texto buscado;
na=False decide no incluir ausencias. En cambio, isin comprueba pertenencia exacta
a categorías. Buscar "com" no valida por sí solo un segmento ni sustituye al catálogo.

## 4. Un texto con apariencia de fecha aún no es una fecha

```python
fecha = pd.to_datetime(texto_fecha, format="%Y-%m-%d", errors="coerce")
```

to_datetime interpreta valores temporales. El formato indica año de cuatro
dígitos (%Y), mes (%m) y día (%d). errors="coerce" convierte valores que no se
pueden interpretar a **NaT**, la ausencia temporal. errors="raise" detendría la
conversión ante un valor inválido. Siempre conservamos el texto original.

NaT e Int64 con NA corresponden a tipos distintos; ambos se detectan con isna.
En esta muestra las fechas quedan como datetime64[ns], a medianoche y sin zona
horaria. No significa que sean eventos registrados a esa hora: la fuente solo
describe días calendario.

### Forma literal y validez calendario

El formato de parsing no sustituye una comprobación estricta de la forma literal.
Por ejemplo, el lector puede aceptar un mes o día sin cero inicial. Si el contrato
exige exactamente YYYY-MM-DD, separamos forma e interpretación:

```python
texto_fecha = tabla["fecha_corte"].str.strip().replace("", pd.NA)
forma = texto_fecha.str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False)
fecha = pd.to_datetime(
    texto_fecha.where(forma), format="%Y-%m-%d", errors="coerce"
)
invalida = texto_fecha.notna() & fecha.isna()
```

fullmatch pide que todo el texto cumpla el patrón. En este ejemplo `\d` indica
un dígito y `{4}` o `{2}` cuántas veces se repite; los guiones son separadores.
El prefijo r mantiene las barras del patrón en una cadena literal de Python.
Esta breve expresión comprueba la forma, **no el calendario**.

where conserva los textos que cumplen esa forma. to_datetime comprueba su
interpretación calendario: 2026-09-31 cumple la forma pero no existe. La máscara
invalida distingue un valor presente no interpretable de uno ausente tras strip.

| Entrada | Resultado | Motivo |
| --- | --- | --- |
| " 2026-10-31 " | 2026-10-31 | Espacios exteriores permitidos |
| "2026-09-31" | NaT | Día imposible |
| "30/09/2026" | NaT | Formato no declarado |
| "2026-10-3" | NaT | Forma literal fuera del contrato |
| Vacío o espacios | NaT | Ausencia, no fecha inválida presente |

Una fecha válida en otro formato no es necesariamente un error de calendario;
simplemente no cumple este contrato. No convertir errores a una fecha inventada.

## 5. Evitar ambigüedades al interpretar

"03/04/2026" puede significar 3 de abril o 4 de marzo según el convenio. Si una
fuente declara día/mes/año, utiliza format="%d/%m/%Y"; si declara mes/día/año,
format="%m/%d/%Y". Elige a partir de la fuente, no del resultado que parezca razonable.

dayfirst=True expresa una preferencia, no valida estrictamente un contrato de
formato. La inferencia automática o format="mixed" requieren decisiones adicionales;
no los usamos como reparación general. Cuando una fuente admite varios formatos,
define cuáles, identifica sus registros y documenta la interpretación de cada uno.

## 6. Componentes dt y diferencias entre fechas

```python
trabajo["mes_corte"] = trabajo["fecha_corte"].dt.month.astype("Int64")
trabajo["dias_desde_alta"] = (
    trabajo["fecha_corte"] - trabajo["fecha_alta"]
).dt.days.astype("Int64")
posterior = trabajo["fecha_alta"] > trabajo["fecha_corte"]
```

dt accede a propiedades temporales. También existen dt.year y dt.day. Restar
fechas devuelve una duración, timedelta; dt.days extrae días completos. Como estas
fechas representan días a medianoche, la resta coincide con la diferencia calendario.
Para horas y duraciones fraccionarias se necesitaría otro tratamiento.

001 tiene alta 2026-08-01: al corte de septiembre han pasado **60 días**, y al de
octubre **91**. Para el registro 12, alta 2026-10-01 y corte 2026-09-30 dan **−1**:
la fecha se interpretó, pero la relación incumple la regla. Las ausencias generan
diferencias desconocidas, no cero días.

No basta con que to_datetime funcione: puede haber fechas válidas fuera del
período permitido o incoherentes con otra columna. Aquí registramos alta_posterior_corte.

## 7. Normalizar antes de revisar la clave

```python
clave = ["id_credito", "fecha_corte"]
completa = trabajo[clave].notna().all(axis=1)
repetida = completa & trabajo.duplicated(subset=clave, keep=False)
```

En origen, los registros 43 y 44 tienen ID "019" y " 019 ". Tras strip ambos
son 019 y comparten el corte de octubre. La normalización revela una clave repetida
que la comparación del texto original no detectaba.

Aplicamos la política de 02.05: ambos se apartan para revisión. Conservar originales
permite explicar qué transformación reveló el conflicto. Nunca comprobar unicidad
solo antes de normalizar y suponer que sigue intacta después.

El script reúne reglas de ID, segmento, fechas, relación temporal y clave, conserva
todos los motivos y separa aceptados/rechazados. isna después del parsing captura
NaT, pero para distinguir su causa se necesita el texto previo.

## 8. Seleccionar un período y comparar cortes

```python
septiembre = aceptados.loc[
    (aceptados["fecha_corte"] >= pd.Timestamp("2026-09-01"))
    & (aceptados["fecha_corte"] < pd.Timestamp("2026-10-01"))
].copy()
```

Timestamp representa el límite como fecha temporal. El intervalo incluye el inicio
y excluye el siguiente mes: **[1 de septiembre, 1 de octubre)**. Este convenio
evita solapamientos y no requiere inventar una última hora del último día.
Comparamos fechas interpretadas, no cadenas con distintos formatos.

Con la muestra original, después de las reglas:

| Período por fecha_corte | Filas aceptadas | Saldo MXN |
| --- | --- | --- |
| Septiembre | 18 | 39900 |
| Octubre | 18 | 41500 |
| Total aceptado | 36 | 81400 |

El segundo saldo supera al primero por 1600, **pero los conjuntos de créditos
aceptados no son idénticos**. Esto describe totales de cada corte disponible;
no demuestra crecimiento de la misma población. Comparar créditos comunes y
registrar entradas/salidas se desarrollará con uniones en 08.

Tampoco sumes los saldos de ambos cortes como si fueran créditos distintos:
un crédito puede estar observado dos veces. El total de la tabla sirve aquí para
conciliar registros, no para calcular una cartera única vigente.

## 9. Ejecución, resultados y exportación

Hay 48 registros, **36 aceptados y 12 rechazados**. El saldo de todos los registros
es 112800: 81400 aceptado + 31400 rechazado. Todos los saldos están presentes en
esta muestra; no es una afirmación sobre cualquier otra entrada.

Se exportan normalizados.csv (todos), aceptados.csv y rechazados.csv, con número
de registro, columnas _original, motivos y componentes temporales. CSV guarda
texto, no tipos temporales: el programa relee fechas con el formato declarado y
compara exactamente las tablas. dt.strftime sirve para presentar fechas como texto;
no lo necesitas para filtrar fechas y no conserva por sí solo el tipo datetime.

### PowerShell

Desde la raíz, con el entorno preparado:

```powershell
# Normalizar, interpretar, evaluar reglas y comprobar tres exportaciones
python curriculum\02_pandas\06_text_dates\text_dates.py
# Revisar fechas y motivos junto a sus valores originales
Get-Content curriculum\02_pandas\06_text_dates\output\rechazados.csv -Encoding utf8
```

### Bash/Zsh

```bash
python curriculum/02_pandas/06_text_dates/text_dates.py
cat curriculum/02_pandas/06_text_dates/output/rechazados.csv
```

### uv

Con la configuración raíz del proyecto:

```text
uv run --locked python curriculum/02_pandas/06_text_dates/text_dates.py
```

No hay nuevas dependencias. Las salidas se reemplazan y permanecen ignoradas por
Git; un fallo puede dejar archivos antiguos o parciales. Comprueba que la ejecución
terminó y confirmó las exportaciones antes de usarlas. La fuente permanece intacta.

## Ampliación opcional: horas y zonas horarias

Una fecha calendario y un instante con hora son conceptos distintos. Si un evento
incluye zona u offset, habrá que acordar la zona de origen y la de comparación,
y cómo manejar cambios de horario. utc=True puede convertir instantes con offset
a UTC; un dato sin zona no revela automáticamente en qué lugar ocurrió.
No agregamos zonas a estas fechas calendario ni adelantamos esa complejidad al núcleo.

## Errores frecuentes, práctica y siguiente paso

| Situación | Qué revisar |
| --- | --- |
| .dt no funciona | La columna sigue siendo texto u object |
| Desaparecieron causas de NaT | Si se conservaron valores originales |
| Fecha interpretada con otro significado | Contrato explícito, no solo inferencia |
| Se perdieron ceros del ID | Tipo de lectura y conversión numérica innecesaria |
| Catálogo fusionado incorrectamente | Equivalencias y reemplazos demasiado amplios |
| Duplicados después de limpiar | Clave sobre los campos normalizados |

Realiza el [lab 02.06](../../../labs/02_pandas/06_text_dates/README.md). Puedes avanzar
cuando expliques normalizaciones, causas de NaT, conflictos de clave y límites de
la comparación entre cortes. No hay checkpoint implementado; el proyecto sigue previsto.

Continúa con [07 — Agrupar y resumir](../07_group_summarize/README.md)
antes de realizar su lab.

## Referencias oficiales

- [Trabajo con texto](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/text.html),
  [str.strip](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.strip.html) y
  [str.contains](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.contains.html).
- [to_datetime](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.to_datetime.html).
- [Fechas, duraciones y zonas horarias](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/timeseries.html).

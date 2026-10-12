# 07 — Agrupar y resumir

## Propósito, prerrequisitos y objetivos

Convertir una tabla de observaciones en indicadores por grupo, comprobando que
el resumen conserve lo conocido del detalle. Completa [Texto y fechas](../06_text_dates/README.md)
y su lab; usa el mismo entorno con pandas 2.3.3.

Al terminar podrás agrupar por una o varias claves, nombrar agregaciones, distinguir
filas de valores conocidos, calcular tasas con una base explícita y conciliar
conteos/sumas. transform será una ampliación breve; ventanas y acumulados quedan
para profundización posterior. No necesitas apply para los indicadores de esta lección.

## 1. Definir primero la unidad del indicador

[cartera_resumen.csv](cartera_resumen.csv) contiene **48 observaciones sintéticas**:
24 créditos ficticios en dos cortes. Es una nueva muestra analítica con categorías
normalizadas y fechas en formato declarado; las fuentes anteriores siguen intactas.

| Campo | Significado | Contrato |
| --- | --- | --- |
| id_credito | Identificador ficticio | Texto, presente |
| segmento | Categoría de la observación | Texto normalizado; puede faltar |
| fecha_corte | Fotografía del crédito | 2026-09-30 o 2026-10-31 en esta muestra |
| saldo_mxn | Saldo de esa fotografía | Pesos enteros no negativos; puede faltar |
| dias_atraso | Conteo en ese corte | Entero no negativo; puede faltar |

La clave de detalle es **ID + corte**, única y completa. Una fila es una observación;
no es necesariamente una persona ni un crédito distinto en toda la tabla.
El resumen principal tendrá una fila por **corte + segmento**.

Aquí se permite conservar segmento, saldo y atraso ausentes para describir cobertura.
Es un contrato analítico diferente al de 02.05, donde esos campos eran obligatorios
para aceptar una fila. No cambiamos sus reglas retroactivamente: cada pregunta
debe declarar qué observaciones utiliza y qué información necesita.

El lector comprueba claves y cantidades negativas antes de resumir. No resuelve
duplicados mediante una suma: una repetición accidental inflaría indicadores.

## 2. groupby: separar, calcular y reunir

```python
grupos = detalle.groupby("segmento", dropna=False)
conteos = grupos.size()
```

groupby construye un objeto con las reglas de agrupación; todavía no es la tabla
final. size produce el número de filas de cada grupo. Conceptualmente:

```text
Detalle de observaciones
    → separar por clave de grupo
    → calcular conteos, sumas o promedios dentro de cada grupo
    → reunir una fila de resultados por grupo
```

Agrupar no cambia la fuente, elimina duplicados ni ordena créditos por saldo.
Si agrupas solo por segmento mezclarás los dos cortes; usa ambas claves cuando
la pregunta necesite distinguir fechas.

```python
grupos = detalle.groupby(
    ["fecha_corte", "segmento"],
    as_index=False, dropna=False, observed=True, sort=True,
)
```

| Opción | Decisión de esta lección |
| --- | --- |
| as_index=False | Mantener las claves como columnas en el resumen |
| dropna=False | Conservar los grupos cuya clave contiene ausencias |
| observed=True | Para claves categóricas, incluir combinaciones observadas |
| sort=True | Ordenar las claves de grupo; no elegir los mayores saldos |

Con as_index=True, las claves aparecen en el índice, posiblemente MultiIndex.
No lo necesitamos para este primer resumen. observed solo tiene efecto especial
cuando hay claves de tipo category; nuestra muestra usa string. Se declara para
hacer explícita la decisión si después utilizas categorías.

## 3. size, count y nunique responden preguntas distintas

| Operación | Qué cuenta | Qué ocurre con una ausencia |
| --- | --- | --- |
| size | Filas del grupo | La fila cuenta |
| count sobre una columna | Valores presentes en ese campo | No cuenta ese valor |
| nunique sobre una columna | Valores distintos presentes | Por defecto no cuenta NA como valor distinto |

En consumo de septiembre hay **9 filas**, pero solo **7 saldos conocidos** y
**7 atrasos conocidos**. Los faltantes de saldo y atraso no son necesariamente
las mismas filas. Un conteo sobre saldo no sirve automáticamente como base del atraso.

Dentro de cada grupo corte/segmento los IDs son únicos: nunique coincide con size
porque la clave de detalle ya fue comprobada. En todo el detalle hay **24 IDs**
pero **48 observaciones**. Sumar IDs distintos de varios cortes no da el número
de créditos distintos de la tabla: un ID puede contarse una vez en cada grupo.

## 4. Agregaciones con nombres claros

El [script completo](group_summarize.py) usa agregación nombrada:

```python
def sumar_conocidos(serie):
    return serie.sum(min_count=1)

resumen = grupos.agg(
    registros=("id_credito", "size"),
    saldos_conocidos=("saldo_mxn", "count"),
    saldo_conocido_mxn=("saldo_mxn", sumar_conocidos),
    saldo_promedio_mxn=("saldo_mxn", "mean"),
)
```

Cada argumento tiene un **nombre de salida** y una tupla con columna de entrada
y operación. "mean" indica el promedio de valores presentes. sumar_conocidos es
la función que pandas llama con la Series de cada grupo; no la ejecutamos al
escribir su nombre en agg.

Esto permite decidir min_count=1 para cada suma. Una suma predeterminada puede
mostrar cero cuando todos los valores faltan; aquí queremos expresar ausencia de
observaciones conocidas. No confundimos un saldo cero conocido con falta de saldo.

El script también calcula IDs distintos, atrasos conocidos y atrasos confirmados
de al menos 30 días. Los umbrales son didácticos; no representan una regla de riesgo.

## 5. Grupos con faltantes: en la clave y en la cantidad

Son dos decisiones independientes:

1. **Clave ausente:** ¿conservar la observación en un grupo sin segmento?
2. **Cantidad ausente:** ¿qué cálculo se puede hacer dentro de su grupo?

groupby usa dropna=True por defecto, lo que excluye filas con NA en las claves de
agrupación. La muestra tiene dos segmentos ausentes: saldo 1700 en septiembre y
2300 en octubre. Si se excluyen sin registrar, desaparecen dos filas y **4000 MXN
conocidos** del resumen.

Con dropna=False existen dos grupos sin segmento, uno por corte. El NA no es una
categoría de negocio nueva; significa que no conocemos la categoría. Puedes rotularlo
al presentar, conservando esa distinción y sin inventar una pertenencia.

Para educación de octubre hay tres filas y **ningún saldo conocido**. Su suma y
promedio son NA. Para educación de septiembre hay tres filas y **ningún atraso
conocido**. Su tasa de atraso no se puede calcular, aunque sí tenga saldos conocidos.

## 6. Calcular una tasa y mostrar cobertura

```python
trabajo = detalle.copy()
trabajo["atraso_30"] = (trabajo["dias_atraso"] >= 30).astype("boolean")
```

True confirma el umbral, False confirma que no se alcanza y NA expresa desconocido.
No rellenamos el indicador con False antes de medir cobertura. Una suma de booleanos
cuenta True; utilizamos min_count=1 para que un grupo sin evaluaciones no aparente
tener cero casos confirmados con una base conocida.

Después de agregar:

```python
resumen["cobertura_atraso_pct"] = (
    resumen["atrasos_conocidos"] / resumen["registros"] * 100
)
base = resumen["atrasos_conocidos"].where(resumen["atrasos_conocidos"] > 0)
resumen["atraso_30_pct_conocidos"] = (
    resumen["atrasos_30_confirmados"] / base * 100
)
```

| Indicador | Numerador | Denominador |
| --- | --- | --- |
| Cobertura de atraso | Atrasos conocidos | Filas del grupo |
| Tasa de atraso ≥ 30 entre conocidos | Casos confirmados ≥ 30 | Atrasos conocidos |

Consumo de septiembre: 9 observaciones, 7 atrasos conocidos y 2 casos confirmados.
Cobertura **7/9 ≈ 77.78 %**; tasa entre conocidos **2/7 ≈ 28.57 %**.
Usar 2/9 daría otra medida: casos confirmados respecto de todas las observaciones.
No equivale a conocer el atraso de quienes faltan.

Educación de septiembre tiene cobertura cero y tasa NA. Si el denominador es cero,
where lo vuelve ausente antes de dividir. Ningún infinito se presenta como tasa útil.

## 7. Promedios y porcentajes no se suman como importes

Para consumo de septiembre, saldo conocido 10400 entre 7 saldos presentes:
promedio **10400/7 ≈ 1485.71 MXN**. Dividir entre las 9 filas imputaría implícitamente
saldo cero a las dos desconocidas.

No promedies sin ponderación los promedios de grupos con tamaños diferentes:
un grupo de una fila recibiría el mismo peso que uno de diez. Para reconstruir el
promedio conocido del conjunto, suma los saldos conocidos y divide entre su conteo.
En esta muestra: **93900/42 ≈ 2235.71 MXN por observación con saldo conocido**.

La tasa global entre atrasos conocidos es **15/40 = 37.5 %**, utilizando todos
los grupos y cortes de esta tabla. No es la tasa de 24 créditos únicos en una fecha.
Para tasas por corte, primero delimita ese corte o resume numeradores y bases
por fecha; no sumes porcentajes ni tomes una media simple de tasas de segmentos.

Redondea para mostrar, no antes de conciliar. Los campos Float64 de la salida
pueden aproximar decimales; los importes enteros y conteos conservan su significado.

## 8. Conciliar el resumen contra el detalle

Resultados conocidos del ejemplo:

| Comprobación | Resultado |
| --- | --- |
| Observaciones / grupos corte-segmento | 48 / 10 |
| IDs distintos de toda la tabla | 24 |
| Saldos conocidos / desconocidos | 42 / 6 |
| Saldo conocido total | 93900 MXN |
| Atrasos conocidos / desconocidos | 40 / 8 |
| Casos confirmados de atraso ≥ 30 | 15 |

La suma de registros de grupos debe dar 48. Los conteos de saldos y atrasos
conocidos deben dar 42 y 40. Las sumas de saldos conocidos y casos confirmados
deben coincidir con 93900 y 15 obtenidos directamente del detalle.

El script comprueba esas igualdades y si un resultado debe permanecer NA. Conciliar
un saldo parcial no lo vuelve completo: las seis cantidades desconocidas se cuentan
aparte. El total de dos cortes es una suma de observaciones para verificar el
proceso; no representa una cartera única vigente ni dinero acumulado durante el mes.

Para investigar un grupo, filtra el detalle con el mismo corte y segmento y calcula
a mano. Si el segmento es NA, utiliza isna en lugar de compararlo con `== pd.NA`.
Una coincidencia global ayuda, pero no sustituye revisar grupos y denominadores.

## 9. Ejecutar y revisar la salida

### PowerShell

Desde la raíz, con el entorno preparado:

```powershell
# Crear el resumen, conciliar y comprobar su lectura posterior
python curriculum\02_pandas\07_group_summarize\group_summarize.py
# Revisar los indicadores por corte y segmento
Get-Content curriculum\02_pandas\07_group_summarize\output\resumen_corte_segmento.csv -Encoding utf8
```

### Bash/Zsh

```bash
python curriculum/02_pandas/07_group_summarize/group_summarize.py
cat curriculum/02_pandas/07_group_summarize/output/resumen_corte_segmento.csv
```

### uv

Con la configuración raíz del proyecto:

```text
uv run --locked python curriculum/02_pandas/07_group_summarize/group_summarize.py
```

No hay nuevas dependencias. La salida se reemplaza, se relee con tipos declarados
y se compara, tolerando 1e-12 para aproximaciones decimales. El CSV no almacena
tipos; fecha_corte se interpreta al recargar. La fuente queda intacta y output
permanece ignorado por Git. Verifica que la ejecución terminó antes de usar la salida.

## 10. Ampliación opcional: transform

agg reduce a una fila por grupo. transform devuelve resultados alineados con las
filas del objeto agrupado: sirve para añadir a cada observación un total de su grupo.

```python
practica = detalle.copy()
total_corte = practica.groupby("fecha_corte", dropna=False)["saldo_mxn"].transform(sumar_conocidos)
practica["participacion_saldo_conocido_pct"] = (
    practica["saldo_mxn"] / total_corte.where(total_corte > 0) * 100
)
```

Una fila con saldo desconocido conserva porcentaje desconocido. Este porcentaje
describe participación en el **saldo conocido del corte**, no en su saldo completo
si faltan cantidades. No agrega ni elimina filas. No hace falta una unión para
esta transformación; combinar otras tablas se estudiará en 08.

Ventanas rolling, acumulados cumsum y groupby.apply se reservan para profundización.
Primero comprueba resúmenes básicos, cobertura y bases de comparación.

## Errores frecuentes, práctica y siguiente paso

| Situación | Qué revisar |
| --- | --- |
| Faltan filas o saldos en el resumen | dropna y claves de agrupación |
| NA se convirtió en cero | sum predeterminado o imputación previa |
| Promedio demasiado bajo | Si se dividió entre filas en lugar de cantidades conocidas |
| Tasa cambia sin cambiar casos | Denominador y cobertura |
| Más IDs contados que créditos distintos | Repetición legítima entre cortes |
| Columnas no encontradas en la salida | as_index y nombres de agregación |

Realiza el [lab 02.07](../../../labs/02_pandas/07_group_summarize/README.md).
Puedes avanzar cuando reconstruyas indicadores desde el detalle, expliques grupos
con NA y distingas suma, promedio, cobertura y tasa. No hay checkpoint implementado;
el proyecto de limpieza sigue previsto.

Continúa con [08 — Combinar tablas](../08_combine_tables/README.md)
antes de realizar su lab.

## Referencias oficiales

- [Agrupación y agregación nombrada](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/groupby.html).
- [Opciones de DataFrame.groupby](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.groupby.html).
- [Sumas y min_count](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.core.groupby.DataFrameGroupBy.sum.html).

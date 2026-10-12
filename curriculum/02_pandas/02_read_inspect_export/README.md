# 02 — Leer, inspeccionar y exportar

## Propósito y prerrequisitos

Cargar un CSV con pandas, entender qué se leyó y verificar una salida sin alterar
la fuente. Completa [Series y DataFrame](../01_series_dataframe/README.md) y su lab.
Usa el entorno con pandas 2.3.3 preparado allí; no necesitas instalar otro paquete.

Al terminar podrás interpretar head, info y describe, preservar identificadores
de texto y volver a leer una exportación para comprobarla. Todavía no haremos
filtros, limpieza ni cálculos entre columnas: se desarrollan en las siguientes lecciones.

## 1. Una muestra nueva y su diccionario

[cartera_demo.csv](cartera_demo.csv) contiene seis registros **completamente ficticios**.
Cada fila representa un crédito observado en una fecha de corte, no una persona
ni una transacción. Los identificadores no corresponden a créditos reales.

| Campo | Significado | Representación acordada |
| --- | --- | --- |
| id_credito | Identificador del crédito ficticio | Texto: conservar 001, 002, etc. |
| segmento | Categoría descriptiva | Texto; comercio, local es un solo valor |
| fecha_corte | Fecha de la observación | Texto AAAA-MM-DD por ahora |
| saldo_mxn | Saldo observado | Pesos enteros; cero es un dato conocido |
| dias_atraso | Días de atraso registrados | Entero; un campo vacío significa desconocido |

La fecha se mantiene como texto; interpretarla como fecha se estudiará en 06.
Los saldos son pesos enteros para esta muestra. No se deducen intereses ni riesgo
a partir de estas columnas. Aprenderemos el dominio a medida que se necesite.

```csv
id_credito,segmento,fecha_corte,saldo_mxn,dias_atraso
001,consumo,2026-09-30,1000,0
002,"comercio, local",2026-09-30,1500,10
003,servicios,2026-09-30,750,45
004,consumo,2026-09-30,0,0
005,educación,2026-09-30,2250,
006,servicios,2026-09-30,500,5
```

Abre primero el archivo como texto. Las comillas conservan la coma de un segmento;
el campo vacío del registro 005 no equivale a cero. El encabezado no es un registro.

## 2. Leer el archivo y elegir tipos

```python
from pathlib import Path
import pandas as pd

# En una consola o notebook ubicado en la raíz del repositorio
ruta = Path("curriculum") / "02_pandas" / "02_read_inspect_export" / "cartera_demo.csv"
tabla = pd.read_csv(ruta, sep=",", encoding="utf-8-sig", dtype={
    "id_credito": "string",
    "segmento": "string",
    "fecha_corte": "string",
    "saldo_mxn": "Int64",
    "dias_atraso": "Int64",
})
```

read_csv devuelve un DataFrame. sep declara el separador; encoding indica cómo
leer el texto. utf-8-sig acepta UTF-8 con o sin marca BOM. La primera fila aporta
los nombres de columnas y el índice se crea aparte.

El diccionario dtype relaciona columna y tipo esperado. Sin él, la inferencia
podría convertir 001 en el número 1: un identificador no es una cantidad.
`string` conserva texto; `Int64`, con I mayúscula, admite enteros y valores
faltantes. Es diferente de `int64`, que no admite esos faltantes de la misma forma.
El dato desconocido se mostrará como `<NA>` en esta columna.

Declarar dtype no corrige un texto como cinco ni demuestra que las cantidades
sean válidas: una conversión incompatible puede fallar. Conversión detallada se
estudia en 04 y calidad de datos en 05. pandas reconoce campos vacíos y ciertos
marcadores de ausencia por defecto; si una fuente usa NA como texto legítimo,
su política de faltantes debe definirse, no asumirse.

### Dónde comienza una ruta

Una ruta relativa parte del directorio actual. El script incluido utiliza
`Path(__file__).resolve().parent` para encontrar el CSV junto al script, como
aprendiste en [archivos CSV de Python](../../01_python_foundations/05_csv_files/README.md).
Ese patrón no se copia directamente en celdas: un notebook normalmente no define __file__.

## 3. Inspeccionar antes de interpretar

### head: una vista de las primeras filas

```python
print(tabla.head())       # Primeras cinco filas
print(tabla.head(2))      # Solo dos, para una revisión rápida
print(tabla.shape)        # (6, 5): tamaño completo
```

head no cambia la tabla y no es una muestra aleatoria. Ver cinco filas no demuestra
que el archivo tenga cinco: el registro 006 queda fuera de esa primera vista.
Comprueba shape, nombres y tipos para saber qué se cargó.

### info: estructura y valores presentes

```python
tabla.info()
```

info muestra filas, columnas, cantidad de valores no faltantes, tipos y una
estimación de memoria. Imprime su informe y devuelve None; `print(tabla.info())`
añadiría un None debajo. En esta muestra, las primeras cuatro columnas tienen
seis valores presentes y dias_atraso tiene cinco.

Un cero cuenta como presente. info no indica qué regla de negocio cumple un
campo, si hay duplicados o cuál fue la causa de un faltante. Tampoco sustituye
una medición completa de memoria del proceso.

### describe: resumen descriptivo

```python
print(tabla.describe())
```

Por defecto resume las columnas numéricas de esta tabla:

| Etiqueta | Qué permite observar |
| --- | --- |
| count | Cantidad de valores presentes, no siempre cantidad de filas |
| mean | Promedio de los valores presentes |
| std | Desviación estándar muestral; se profundizará cuando haga falta |
| min / max | Menor y mayor valor observado |
| 25%, 50%, 75% | Cuartiles; describen la distribución, no tasas de incumplimiento |

saldo_mxn tiene count 6 y mean 1000; dias_atraso tiene count 5 y mean 12.
La suma de saldos conocidos es 6000 MXN. Es una observación de esta muestra,
no una validación completa de la cartera ni una conclusión sobre una población real.

Opcionalmente, `tabla.describe(include="all")` incorpora columnas no numéricas;
su resumen tiene otras medidas. Basta interpretar count, rangos y el hecho de
que una ausencia afecta el número de observaciones para esta lección.

El script utiliza sum(min_count=1) para que una columna sin ningún saldo conocido
no produzca cero como si fuera un total comprobado. Si falta solo parte de los
saldos, la suma sigue siendo parcial: conocerla no implica conocer el saldo total.

## 4. Exportar una copia, sin convertir el índice en una columna

```python
salida = ruta.parent / "output" / "cartera_copia.csv"
salida.parent.mkdir(parents=True, exist_ok=True)
tabla.to_csv(salida, index=False, encoding="utf-8")
```

to_csv escribe un archivo; la carpeta debe existir. index=False evita agregar
las etiquetas del índice como datos. Si lo omites, la lectura posterior puede
mostrar una columna adicional, frecuentemente Unnamed: 0.

El modo de escritura habitual reemplaza la salida existente. Entrada y salida
deben ser archivos distintos. El script comprueba sus rutas antes de escribir y
output está ignorado por Git. La salida se puede regenerar sin duplicar filas.

CSV contiene texto: no conserva por sí solo los dtypes de pandas. El valor
faltante se exporta como campo vacío; al leer nuevamente utilizaremos el mismo
contrato de tipos y ausencia. El escritor coloca comillas cuando un campo lo requiere.
No es necesario agregar comillas manualmente al segmento con coma.

## 5. Volver a leer y comprobar

```python
# En el script, leer_cartera aplica separador, codificación, tipos y columnas
recargada = leer_cartera(salida)
print(tabla.equals(recargada))  # True en esta muestra
```

Este fragmento utiliza una función definida en el
[script read_inspect_export.py](read_inspect_export.py). equals compara estructura,
valores y tipos de columnas, y considera iguales los faltantes en posiciones
correspondientes. En este recorrido se conserva también el índice inicial generado.

El script separa lectura, escritura y presentación; si la copia recargada no coincide,
genera ValueError. La igualdad comprueba esta exportación, pero no valida que el
archivo de origen tenga datos correctos. No sustituye reglas de calidad de 05.

Comprueba además: seis filas, cinco columnas, ID 001 conservado, segmento con
coma y acento intactos, dias_atraso desconocido en 005 y saldos conocidos de 6000 MXN.
No basta que el archivo exista. Si una ejecución falla, puede permanecer una
salida anterior; un fallo durante escritura puede dejarla incompleta.

## 6. Ejecutar el ejemplo

### PowerShell

Desde la raíz y con el entorno activado:

```powershell
# Leer, inspeccionar, exportar y comprobar
python curriculum\02_pandas\02_read_inspect_export\read_inspect_export.py
# Ver el archivo generado como texto
Get-Content curriculum\02_pandas\02_read_inspect_export\output\cartera_copia.csv -Encoding utf8
```

Sin activar venv, sustituye python por `.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
python curriculum/02_pandas/02_read_inspect_export/read_inspect_export.py
cat curriculum/02_pandas/02_read_inspect_export/output/cartera_copia.csv
```

Sin activar venv, utiliza `./.venv-practice/bin/python`.

### uv

Desde la raíz, con la configuración de dependencias del proyecto:

```text
uv run --locked python curriculum/02_pandas/02_read_inspect_export/read_inspect_export.py
```

Se imprimen vistas, estructura y resumen, seguidos de la confirmación de seis
filas/cinco columnas y la ubicación de la copia. No se realizan filtros ni limpieza.

## Errores que conviene reconocer

| Situación | Qué comprobar |
| --- | --- |
| FileNotFoundError | Ubicación actual, ruta y existencia de la entrada |
| UnicodeDecodeError o texto mal interpretado | Codificación real de la fuente |
| Solo aparece una columna | Separador y encabezado; no asumir que siempre es coma |
| ID sin ceros iniciales | Tipo declarado al leer, no solo formato visual |
| Conversión incompatible | Campo recibido y tipo requerido |
| Columna extra tras exportar | index=False y encabezado de salida |
| Error al escribir | Permisos y si otra aplicación bloquea el archivo |

Otros formatos CSV pueden usar `;` o decimales con coma. Configurar sep y decimal
según la fuente es distinto de limpiar registros; no hace falta instalarlos como
otra biblioteca. Primero comprobar el contrato y una muestra pequeña.

## Práctica y criterio de salida

Realiza el [lab 02.02](../../../labs/02_pandas/02_read_inspect_export/README.md).
Puedes avanzar al explicar qué muestra cada inspección, conservar los ID y
faltantes, exportar a otra ruta y demostrar una lectura equivalente. El proyecto
de limpieza sigue previsto: no hay checkpoint implementado todavía.

## Siguiente paso y referencias

03 — Seleccionar, filtrar y ordenar está por desarrollar. Consulta su
[alcance previsto](../README.md#03-seleccionar-filtrar-y-ordenar).

- [read_csv](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_csv.html).
- [info](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.info.html) y
  [describe](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.describe.html).
- [to_csv](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_csv.html).
- [equals](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.equals.html).

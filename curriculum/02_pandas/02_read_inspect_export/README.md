# 02.02 — Leer, inspeccionar y exportar

<a id="02--leer-inspeccionar-y-exportar"></a>

[Inicio](../../../README.md) / [Módulo 02](../README.md) / **Lección 02.02**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Cargar e inspeccionar un CSV y comprobar su exportación |
| **Necesitas** | Entorno de estudio con pandas; entrada incluida o compartida según la lección |
| **Evidencia** | Código, exportación y nota de relectura comprobada |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/02_pandas/02_read_inspect_export/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Cargar un CSV con pandas, entender qué se leyó y verificar una salida sin alterar
la fuente.

## Antes de empezar

Completa [02.01 — Series y DataFrame](../01_series_dataframe/README.md) y su lab.
Usa el mismo entorno con pandas 2.3.3 como referencia. Trabaja desde la raíz
de DS Track, con tu editor y el shell elegido. La entrada se enlaza más abajo;
no necesitas producir archivos de lecciones anteriores para leer esta muestra.

## Qué vas a aprender

- Explicar qué representa una fila con el diccionario de la muestra.
- Declarar tipos al leer para conservar identificadores de texto y ausencias.
- Interpretar head, info y describe sin confundir vista previa y validación.
- Exportar a otra ruta y releer para demostrar equivalencia.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](read_inspect_export.py) | Seguir lectura, inspección, exportación y relectura de la misma muestra | Para el ejemplo |
| [CSV de entrada](cartera_demo.csv) | Leer seis observaciones ficticias con su diccionario en el apartado 1 | Entrada incluida |

Abre los recursos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y contrasta sus resultados esperados. Conserva los originales y
trabaja las variantes en tu copia. Los datos compartidos se reutilizan desde
su ubicación actual, sin duplicarlos.

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

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 02.02](../../../labs/02_pandas/02_read_inspect_export/README.md) para
interpretar la muestra, exportar y contrastar una relectura.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu código y copia exportada | IDs con ceros, ausencias y encabezado sin índice adicional | Qué informa cada inspección y qué no demuestra |
| Nota de comprobación y referencia a la fuente | Relectura equivalente y original intacto | Por qué guardar el CSV no conserva automáticamente los tipos de pandas |

Puedes avanzar al explicar qué muestra cada inspección, conservar los ID y
faltantes, exportar a otra ruta y demostrar una lectura equivalente.

Quien aprende modifica y ejecuta su copia y explica lo que comprobó.
Tu compañero elige un ID con ceros iniciales y pide contrastarlo en la fuente y la relectura.
Guarda evidencia, ayudas y dudas en una nota personal junto a tu práctica;
PROGRESS.md registra el desarrollo editorial del curso. El material disponible
no acredita por sí solo aprendizaje completado.

El proyecto de limpieza y sus checkpoints siguen previstos, sin proyecto
asociado implementado ni práctica adicional de proyecto obligatoria.

<a id="siguiente-paso-y-referencias"></a>

## Referencias

- [read_csv](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_csv.html).
- [info](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.info.html) y
  [describe](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.describe.html).
- [to_csv](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_csv.html).
- [equals](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.equals.html).

## Siguiente paso

Después del lab y su comprobación, continúa con [02.03 — Seleccionar, filtrar y ordenar](../03_select_filter_sort/README.md)
antes de realizar su lab.

[← Módulo 02](../README.md) · [Lab 02.02](../../../labs/02_pandas/02_read_inspect_export/README.md) · [Siguiente →](../03_select_filter_sort/README.md)

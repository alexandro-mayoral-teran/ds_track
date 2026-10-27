# 01.05 — Leer y escribir archivos CSV

<a id="05--leer-y-escribir-archivos-csv"></a>

[Inicio](../../../README.md) / [Módulo 01](../README.md) / **Lección 01.05**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Leer, transformar y escribir un CSV sin alterar la entrada |
| **Necesitas** | Entorno de Python del módulo 00; biblioteca estándar |
| **Evidencia** | Script, copias de práctica y salida CSV con conteos e importes comprobados |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/01_python_foundations/05_csv_files/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-objetivos"></a>

## Propósito

Utilizar datos guardados en un archivo, transformarlos con Python y
conservar el resultado en otro archivo. La entrada y la salida permiten
revisar qué se leyó, qué se convirtió y qué se escribió.

## Antes de empezar

Completa [01.04 — Funciones](../04_functions/README.md) y su lab. Usa tu entorno
habitual: `csv` y `pathlib` pertenecen a la biblioteca estándar, sin pandas
ni paquetes nuevos. Abre DS Track en tu editor y ejecuta desde su raíz.

La entrada está incluida en esta lección; no necesitas generar archivos con
prácticas anteriores. Conserva el CSV original y realiza los cambios del lab
en una copia dentro de `output`, como indica su consigna.

## Qué vas a aprender

- Interpretar encabezado, registros, separador y comillas de un CSV.
- Leer campos como texto con `DictReader` y convertirlos antes de calcular.
- Explicar rutas y apertura con `with` y escribir columnas con `DictWriter`.
- Revisar la salida con sus conteos, unidades e importes conservando la entrada original.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Script de ejemplo](csv_pipeline.py) | Seguir la lectura, conversión y escritura separadas en funciones | Para el ejemplo |
| [CSV de entrada](ventas_entrada.csv) | Inspeccionar las tres ventas, incluido el nombre que contiene una coma | Entrada incluida |

Abre los archivos cuando aparezcan en el recorrido. Lee el código antes de
ejecutarlo y compara la salida con los resultados esperados. Para practicar,
modifica tu copia y conserva los originales.

## 1. Qué contiene un CSV

Un CSV representa una tabla en texto. El encabezado identifica las columnas;
cada registro contiene sus campos en el orden definido. Aquí usamos comas:

```csv
producto,unidades,precio_unitario_mxn
cuaderno,2,40
"lápiz, azul",5,10
carpeta,1,35
```

Son tres registros, no cuatro: el encabezado no es una venta. Abre
[ventas_entrada.csv](ventas_entrada.csv) en VS Code para comparar el texto.

### Separadores, comillas y tipos

- La coma de `"lápiz, azul"` pertenece al producto, no separa otra columna.
  Las comillas permiten conservarla dentro de un campo.
- Otros archivos utilizan punto y coma o tabuladores. La extensión `.csv`
  no garantiza el mismo separador en todas las fuentes.
- El archivo no define automáticamente los tipos: el lector que usaremos
  entrega `"2"` y `"40"` como texto, y debemos convertirlos para calcular.
- Un campo entre comillas puede contener un salto de línea. Contar líneas
  físicas no siempre equivale a contar registros.

Por eso no leeremos con `linea.split(",")`: dividir por cada coma rompería el
producto de este ejemplo. El módulo csv interpreta separadores y comillas.

## 2. Importaciones y rutas

```python
import csv
from pathlib import Path
```

`import csv` permite utilizar elementos del módulo como `csv.DictReader`.
`from pathlib import Path` permite construir rutas con Path. Importar un módulo
no descarga ni instala paquetes; en este caso ambos ya vienen con Python.

### Una ruta desde la carpeta actual

```python
ruta = Path("curriculum") / "01_python_foundations" / "05_csv_files" / "ventas_entrada.csv"
```

En Path, `/` une componentes de ruta; aquí no divide números. Esta ruta relativa
parte del directorio actual, como aprendiste en terminal.

### Las rutas del script incluido

```python
carpeta_leccion = Path(__file__).resolve().parent
ruta_entrada = carpeta_leccion / "ventas_entrada.csv"
ruta_salida = carpeta_leccion / "output" / "ventas_con_importe.csv"
```

`__file__` identifica el archivo Python que se está ejecutando; `resolve()`
obtiene su ruta absoluta y `parent` su carpeta. Así la ubicación de los datos
no depende de dónde abriste la terminal, siempre que puedas localizar el script.
`__file__` no suele existir en una celda de notebook: allí construye una ruta
desde una ubicación comprobada, en lugar de copiar esa línea sin adaptarla.

## 3. Abrir y cerrar con with

```python
with ruta_entrada.open("r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo, delimiter=",")
    for fila in lector:
        print(fila)
```

| Elemento | Qué significa |
| --- | --- |
| `"r"` | Abre para leer |
| `encoding` | Indica cómo interpretar los bytes como texto |
| `utf-8-sig` | Lee UTF-8 y admite una marca BOM al inicio si existe |
| `newline=""` | Deja que csv gestione los saltos de línea |
| `as archivo` | Da un nombre al archivo abierto dentro del bloque |
| `with` | Cierra el archivo al salir, incluso si ocurre un error |

Una codificación incorrecta puede producir un error o caracteres mal interpretados.
UTF-8 no equivale a todas las codificaciones; confirma qué utiliza tu fuente.
Para escribir esta salida utilizaremos UTF-8 sin BOM.

El recorrido de las filas debe ocurrir mientras el archivo está abierto. Si
necesitas trabajar después, conserva los registros en una lista dentro de with.
Cerrar el archivo no elimina esa lista de memoria.

## 4. DictReader: del encabezado a diccionarios

El lector utiliza los nombres del encabezado como claves. La primera venta es:

```python
{"producto": "cuaderno", "unidades": "2", "precio_unitario_mxn": "40"}
```

No necesitas suministrar fieldnames al lector porque este archivo ya tiene
encabezado. Recorrerlo consume sus registros; no es una lista que puedas volver
a recorrer desde el principio. Si necesitas todas las filas, puedes reunirlas:

```python
registros = []
with ruta_entrada.open("r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        registros.append(fila)
```

Esta solución es para muestras pequeñas que caben en memoria. No es una estrategia
para cargar cualquier volumen de datos; estudiaremos lotes y otros motores después.

## 5. Convertir y transformar

```python
unidades = int(fila["unidades"])
precio_unitario_mxn = int(fila["precio_unitario_mxn"])
importe_mxn = unidades * precio_unitario_mxn
```

La función `preparar_ventas` del ejemplo realiza esos pasos y devuelve
diccionarios nuevos. Los originales conservan sus campos de texto.
Los importes esperados son 80, 50 y 35 MXN; su total es 165 MXN.

Si encuentras `"dos"`, un campo vacío o un decimal donde esperabas un entero,
no lo reemplaces por cero automáticamente. La conversión puede fallar y la
causa debe revisarse. La [siguiente lección](../06_validation_summary/README.md) define reglas y tratamiento de
registros inválidos. Convertir `"-2"` funciona en Python, pero no demuestra
que esas unidades sean válidas para una venta.

## 6. DictWriter: conservar el resultado

```python
campos = ["producto", "unidades", "precio_unitario_mxn", "importe_mxn"]
with ruta_salida.open("w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)
```

`fieldnames` indica las columnas y su orden. `writeheader()` escribe una sola
fila de nombres y `writerows()` escribe la colección. Los números se representan
como texto al guardarlos: al volver a leer deberás interpretar sus tipos otra vez.
El escritor pone comillas cuando un campo lo necesita; no las agregues manualmente.

> **Antes de escribir:** el modo `"w"` reemplaza un archivo existente. La entrada
> y la salida deben tener rutas distintas. El script escribe únicamente su
> archivo generado en output; no utiliza ventas_entrada.csv como destino.

El script crea output con `mkdir(parents=True, exist_ok=True)` si hace falta.
Esa carpeta está excluida de Git y su CSV puede regenerarse. Repetir el script
reemplaza la salida, no agrega encabezados o registros duplicados.

La conversión de todas las entradas ocurre antes de abrir la salida. Si falla
ese paso, no se escribe un nuevo resultado. Un fallo durante la escritura sí
puede dejar una salida incompleta; no confíes en un archivo solo porque exista.

## 7. Leer el programa como una secuencia

El [script csv_pipeline.py](csv_pipeline.py) separa responsabilidades:

| Paso | Función | Resultado |
| --- | --- | --- |
| Entrada | leer_csv | Lista de registros con campos de texto |
| Transformación | preparar_ventas | Lista con cantidades numéricas e importe |
| Salida | escribir_csv | CSV con las cuatro columnas |
| Presentación | main | Cantidades leídas/escritas y total |

El script hace comprobaciones mínimas del encabezado y la cantidad de campos.
En el lector, `fieldnames` permite consultar el encabezado; `fila.values()`
permite examinar sus valores. Una columna sobrante o faltante puede aparecer
con una clave o valor None en DictReader; el ejemplo rechaza esa estructura.
`raise ValueError(...)` detiene el proceso con una explicación. La lección 06 desarrolla
gestión de errores y reglas explícitas para esta muestra.

Esto no valida duplicados, productos vacíos o cantidades negativas. Mantén clara
la diferencia entre poder leer el formato y demostrar calidad de los datos.

## 8. Ejecutar y revisar la salida

### PowerShell

Desde la raíz y con tu entorno activado:

```powershell
# Ejecuta lectura, conversión y escritura
python curriculum\01_python_foundations\05_csv_files\csv_pipeline.py
# Inspecciona la salida generada
Get-Content curriculum\01_python_foundations\05_csv_files\output\ventas_con_importe.csv -Encoding utf8
```

Con venv sin activar, sustituye python por `.\.venv-practice\Scripts\python.exe`.

### Bash/Zsh

```bash
python curriculum/01_python_foundations/05_csv_files/csv_pipeline.py
cat curriculum/01_python_foundations/05_csv_files/output/ventas_con_importe.csv
```

Con venv sin activar, utiliza `./.venv-practice/bin/python`.

### uv

Desde `.environment-practice/uv-demo`:

```text
uv run --locked python ../../curriculum/01_python_foundations/05_csv_files/csv_pipeline.py
```

Vuelve a la raíz para inspeccionar la salida con el comando de tu shell.

### Resultado esperado

```text
Registros leídos: 3
Registros escritos: 3
Total calculado: 165 MXN
Salida: ventas_con_importe.csv en la carpeta output de esta lección
```

El archivo generado debe contener:

```csv
producto,unidades,precio_unitario_mxn,importe_mxn
cuaderno,2,40,80
"lápiz, azul",5,10,50
carpeta,1,35,35
```

Revisa encabezado, registros, nombre con coma y total. Puedes volver a leerlo
con DictReader para comprobar campos; abrirlo en una hoja de cálculo puede
interpretar tipos o separadores de otra forma. El archivo de texto es la referencia.

## Errores que conviene reconocer

| Situación | Qué revisar |
| --- | --- |
| FileNotFoundError | La ruta y existencia de la entrada |
| UnicodeDecodeError o texto incorrecto | Codificación de la fuente |
| Encabezado esperado no coincide | Nombres, orden y separador |
| ValueError al convertir | Texto recibido y tipo esperado |
| Archivo cerrado | Si intentaste recorrer el lector fuera del bloque with |
| PermissionError al escribir | Permisos o archivo bloqueado por otra aplicación |
| Salida inesperada | Qué archivo se ejecutó y si corresponde a la última ejecución correcta |

Si el CSV utiliza `;`, ajusta delimiter en el lector y escritor según el formato
que quieras conservar. Eso no cambia automáticamente los decimales: `"12,50"`
requiere otra regla de interpretación que no utiliza nuestro ejemplo con enteros.

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 01.05](../../../labs/01_python_foundations/05_csv_files/README.md) para
leer la muestra, trabajar con otra entrada en una copia y revisar el CSV producido.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu script y las copias de entrada/salida del lab | Conteo de registros, encabezado e importes; original intacto | Cómo se interpretan campos con comas y cuándo se convierten los tipos |
| Una nota con rutas y controles | La salida corresponde a la ejecución revisada y conserva el producto completo | Qué hace `with`, qué escribe `DictWriter` y qué validaciones aún faltan |

Puedes avanzar cuando leas y escribas registros, expliques las conversiones,
verifiques cantidades y total, y conserves intacta la entrada original.

Quien aprende modifica y ejecuta su copia, y explica lo que comprobó.
Tu compañero contrasta una fila de salida con la entrada y te pide justificar el importe y las columnas conservadas.
Guarda la evidencia, las ayudas y las dudas en una nota personal junto a tu
práctica; PROGRESS.md registra el desarrollo editorial del curso.

Todavía no hay proyecto ni checkpoint asociado a esta lección. El material
disponible no acredita por sí solo la finalización de tus prácticas.

<a id="referencias-oficiales"></a>

## Referencias

- [Lectura y escritura CSV](https://docs.python.org/es/3/library/csv.html).
- [Archivos y with](https://docs.python.org/es/3/tutorial/inputoutput.html#reading-and-writing-files).
- [Rutas con pathlib](https://docs.python.org/es/3/library/pathlib.html).

## Siguiente paso

Después del lab y su comprobación, continúa con
[01.06 — Validación y resumen](../06_validation_summary/README.md) antes de realizar su lab.

[← Módulo 01](../README.md) · [Lab 01.05](../../../labs/01_python_foundations/05_csv_files/README.md) · [Siguiente →](../06_validation_summary/README.md)

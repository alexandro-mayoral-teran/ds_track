# 05.05 — Tipos y contratos de funciones

## Propósito y prerrequisitos

Hacer explícito qué recibe una función, qué devuelve, qué condiciones exige y
qué ocurre cuando no se cumplen. Usaremos anotaciones y documentación para
leer el código, validaciones para proteger sus límites y pruebas para comprobar
ejemplos. Cada herramienta responde a una pregunta distinta.

Completa [05.04 — Pruebas de código y datos](../04_testing/README.md) y su lab.
Recupera [funciones y argumentos de 01.04](../../01_python_foundations/04_functions/README.md),
[tipos y columnas de 02.04](../../02_pandas/04_types_calculated_columns/README.md)
y [errores de 05.03](../03_errors_resources/README.md).
Trabajamos sobre el paquete de [05.01](../01_notebook_to_modules/README.md),
con sus consumidores y muestras anteriores conservados.

**Esencial para esta práctica:** firmas, tipos de entrada/salida, docstrings,
condiciones y responsabilidades. **Práctica:** parámetros opcionales, resultados
ausentes y estructura tabular. **Extensión:** análisis estático; no exige instalar
un checker ni bibliotecas de esquemas. Clases/dataclasses siguen siendo opcionales
en 05.06. Puedes dividir esta lección en varias sesiones.

## Objetivos observables

- Leer `parametro: Tipo` y `-> Tipo` sin confundirlos con conversión o validación.
- Distinguir omisión, valor predeterminado, None, cero y colección vacía.
- Documentar entradas, salida, errores, efectos y reglas de datos.
- Explicar qué comprueba cada límite del paquete y qué asume su interior.
- Usar una función de revisión que conserva fuentes, ausencias y orden solicitado.
- Ejecutar pruebas de contrato y reconocer los límites del análisis estático.

## 1. El problema: una firma puede dejar preguntas abiertas

Hasta ahora leíamos `summarize(detail, cut)`. Su nombre ayuda, pero no responde:
¿detail es una ruta o una tabla? ¿cut admite None? ¿la función devuelve una tabla
o dos? ¿modifica detail? ¿qué ocurre cuando no hay filas?

Un **contrato** reúne los compromisos necesarios para usar una función:

| Parte | Pregunta | Ejemplo del análisis |
| --- | --- | --- |
| Entrada | ¿Qué objetos y significados recibe? | Tabla validada y fecha YYYY-MM-DD |
| Precondición | ¿Qué debe cumplirse antes de llamar? | Una fila por crédito/fecha, saldos no negativos |
| Salida y postcondición | ¿Qué entrega si termina correctamente? | Detalle seleccionado y cuatro segmentos resumidos |
| Errores | ¿Cómo comunica que no puede cumplir? | ValueError por fecha textual inválida |
| Efectos | ¿Qué lee, escribe o modifica? | summarize no escribe y conserva detail |

La palabra contrato no requiere una biblioteca. Puede expresarse mediante una
firma, un docstring, código de comprobación y ejemplos probados. Escribirlo no
hace que Python lo imponga automáticamente: hay que identificar qué parte es
documentación y cuál se verifica al ejecutar.

## 2. Anotar una función, paso a paso

La firma actual de summarize es:

```python
def summarize(detail: pd.DataFrame, cut: str) -> tuple[pd.DataFrame, pd.DataFrame]:
```

Se lee: recibe detail como DataFrame y cut como texto; devuelve una tupla de
dos DataFrames, en este orden: detalle seleccionado y resumen. `pd` es el alias
de pandas importado en el módulo. Después de la firma viene el cuerpo ya conocido.

El `:` después de cada parámetro introduce su anotación. La flecha `->` describe
el retorno; no es el return ni ejecuta una operación. Los corchetes describen
el contenido de una colección. El `:` final abre el bloque de la función.

| Anotación | Cómo leerla |
| --- | --- |
| int, float, str, bool | Entero, número de punto flotante, texto, booleano |
| list[str] | Lista cuyos elementos se esperan como texto |
| tuple[pd.DataFrame, pd.DataFrame] | Tupla de dos tablas con posiciones definidas |
| dict[str, pd.DataFrame] | Diccionario con claves de texto y valores tabulares |
| str \| Path | Texto o un objeto Path |
| float \| None | Número de punto flotante o ausencia explícita de resultado |
| -> None | La función no entrega un resultado útil al llamador |

`-> None` no significa que la función carezca de efectos: una función puede
imprimir o escribir y devolver None. Aquí main imprime; build_analysis devuelve
tablas. Python admite estas anotaciones en la versión mínima 3.11 del curso;
no necesitamos importar List/Dict ni la sintaxis `type Nombre = ...` de versiones posteriores.

## 3. Una anotación no cambia el objeto

En [ejecutar_contratos.py](../01_notebook_to_modules/ejecutar_contratos.py) hay
una demostración deliberadamente sin validación:

```python
def double_annotated(value: int) -> int:
    return value * 2

print(double_annotated(3))     # 6
print(double_annotated("3"))   # 33: texto repetido, no entero convertido
```

La segunda llamada incumple la anotación. Python ejecuta el cuerpo y el operador
`*` repite el texto. Tampoco comprueba automáticamente que el retorno sea int.
`int("3")` sería una conversión explícita y puede fallar; `value: int` describe
una expectativa. No añadimos conversiones silenciosas para encubrir errores de uso.

Un editor o checker puede señalar esa llamada antes de ejecutarla, si su análisis
está activo. Ejecutar `python archivo.py` no ejecuta un checker. Las anotaciones
son útiles aunque todavía no uses uno: ayudan a leer firmas y detectar ambigüedades.

## 4. Del tipo al dominio: contrato de cobertura

Abre [contratos.py](../01_notebook_to_modules/analisis_cartera/contratos.py).
coverage_pct hace explícita una regla que summarize ya utilizaba:

```python
def coverage_pct(known: int, total: int) -> float | None:
    # El archivo completo valida tipos y 0 <= known <= total antes de dividir.
    ...
```

Los tres puntos aquí indican cuerpo omitido para leer la firma; no copies este
fragmento como implementación. La función real exige conteos int de Python,
excluye bool, devuelve porcentaje en escala 0–100 y nunca interpreta texto.

| Llamada | Resultado | Razón |
| --- | --- | --- |
| coverage_pct(2, 3) | Aproximadamente 66,6667 | Dos conocidos sobre tres registros |
| coverage_pct(0, 3) | 0.0 | Hay base y ningún conocido |
| coverage_pct(0, 0) | None | No existe base para el porcentaje |
| coverage_pct(4, 3) | ValueError | Conocidos no puede superar registros |
| coverage_pct(-1, 3) | ValueError | Un conteo no puede ser negativo |
| coverage_pct("2", 3) | TypeError | Se recibió texto en lugar de un conteo |
| coverage_pct(True, 3) | TypeError | Un booleano no representa aquí un conteo |

Python considera bool una subclase de int: `isinstance(True, int)` da True.
La validación excluye bool antes de aceptar int. El contrato está restringido a
conteos de Python como los obtenidos con len; no promete aceptar todos los escalares
numéricos de NumPy o pandas. Para adaptarlos se necesita decidir una conversión
explícita en su frontera, no cambiar la regla sin revisarla.

El tipo int no expresa por sí solo `0 <= known <= total`. La función comprueba
esa relación con if/raise. Aquí diferenciamos TypeError (tipo incompatible) y
ValueError (valor fuera del dominio). El paquete anterior mantiene sus errores
ya documentados; no renombramos todas sus excepciones para esta lección.

La cobertura es un porcentaje; la diferencia entre dos coberturas se expresa en
puntos porcentuales. No confundas 0,6 como proporción con 60 como porcentaje.
La mediana está en MXN y puede terminar en medio peso aunque los saldos sean enteros.

## 5. Retorno ausente: None no es cero

Si la firma devuelve `float | None`, quien llama debe considerar ambas ramas:

```python
from analisis_cartera.contratos import coverage_pct

coverage = coverage_pct(0, 0)
if coverage is None:
    print("Sin base")
else:
    print(f"{coverage:.1f} %")
```

No uses `if not coverage` para decidir si falta la base: también sería verdadero
con 0.0, que es una cobertura válida. `is None` pregunta por la ausencia exacta.
Formatear None como número produce un error; decidir su presentación pertenece al llamador.

Una función que devuelve un escalar puede usar None; al reunir filas en pandas,
una columna numérica puede representar esa ausencia con NaN, y una columna
nullable puede usar pd.NA. La anotación `float | None` de coverage_pct no impone
la representación interna de un DataFrame. Dentro de tablas consulta `pd.isna`,
como en 05.04; no reemplaces ausencias por cero para que parezcan cumplir el tipo.

## 6. Parámetro opcional no siempre significa que admite None

Compara estas firmas del paquete:

```python
def build_analysis(source: str | Path, cut: str = "2026-10-31") -> dict[str, pd.DataFrame]:
    ...

def normalize_cut(cut: str | None = None) -> str:
    ...
```

En ambas puedes omitir cut porque hay valor predeterminado. Solo la segunda
declara que admite None. En normalize_cut, omitir y pasar None significan usar
**2026-10-31**, el corte didáctico fijo. No significa fecha actual ni último corte disponible.
Una fecha explícita debe ser válida y conservar YYYY-MM-DD; texto vacío se rechaza.

| Uso de normalize_cut | Significado |
| --- | --- |
| normalize_cut() | Usar el corte predeterminado |
| normalize_cut(None) | Pedir explícitamente ese mismo comportamiento |
| normalize_cut("2026-09-30") | Elegir otro corte |
| normalize_cut("") | Error: no se decidió que vacío equivalga a None |

La escritura `Optional[str]` de typing significa `str | None`; no significa
“se puede omitir” si la firma no tiene predeterminado. Usaremos la unión con `|`
para mantener la lectura uniforme. Un corte válido sin registros sigue siendo
un resultado definido, distinto de una fecha imposible o una fuente ausente.

## 7. Una nueva entrada para revisar, sin exportar

[revision.py](../01_notebook_to_modules/analisis_cartera/revision.py) ofrece:

```python
def review_summary(
    source: str | Path,
    cut: str | None = None,
    *,
    segments: list[str] | None = None,
) -> pd.DataFrame:
```

source es obligatorio; cut puede omitirse o nombrarse. El asterisco aislado
exige nombrar los argumentos posteriores. Así, `segments=["comercio"]` deja
claro qué seleccionamos. Pasar la lista como tercer argumento posicional
produce TypeError antes de entrar al cuerpo: esa regla sí la impone Python.

Con source ya definido como carpeta de los CSV:

```python
all_groups = review_summary(source)
chosen = review_summary(source, "2026-10-31", segments=["educacion", "comercio"])
no_groups = review_summary(source, segments=[])
```

| segments | Resultado |
| --- | --- |
| Omitido o None | Todos los grupos en el orden conocido |
| ["educacion", "comercio"] | Solo esos grupos, en ese orden |
| [] | Tabla con cero filas y las ocho columnas del resumen |
| "comercio" | TypeError: texto no equivale a lista de textos |
| ["otro"] | ValueError: nombre fuera de los segmentos permitidos |
| ["comercio", "comercio"] | ValueError: selección duplicada |

No usamos `segments or GROUPS`: convertiría [] en “todos” y rompería el contrato.
La comprobación es `segments is None`. Tampoco usamos [] como predeterminado
mutable. Los predeterminados se evalúan una vez al definir la función; si luego
se modifica esa lista, llamadas futuras podrían compartir cambios. None permite
decidir explícitamente el comportamiento en cada llamada.

La función valida opciones, llama build_analysis (que lee y concilia) y selecciona
el resumen. Incluso [] lee y valida las fuentes: “no mostrar grupos” no autoriza
a ocultar un archivo inexistente o una clave duplicada. Retorna una tabla nueva,
conserva la lista del llamador y no escribe una entrega. Los segmentos elegidos
no cambian la población usada para calcular cada mediana ni recalculan un total global.

## 8. DataFrame describe el contenedor; falta su esquema

La firma `detail: pd.DataFrame` también admitiría, para un checker general,
una tabla con columnas de temperaturas. El contrato del análisis debe precisar
contenido y significado. El detalle que produce read_detail tiene:

| Columna | Representación de referencia | Regla y significado |
| --- | --- | --- |
| id_credito | string de pandas | Texto, conserva ceros iniciales; con fecha forma la clave |
| fecha_corte | string de pandas | Fecha válida YYYY-MM-DD |
| saldo_mxn | Int64 nullable | Saldo no negativo en MXN o desconocido |
| dias_atraso | Int64 nullable | Días no negativos o desconocidos |
| segmento | Texto procedente del catálogo | Uno de los cuatro grupos conocidos |

La unidad es **un crédito en un corte**. El lector comprueba duplicados y relación
con el catálogo; conserva ausencias. El detalle se ordena por fecha/crédito y
recibe índice nuevo. summarize asume esa entrada validada; si construyes una
tabla manual, tú eres responsable de cumplir su precondición.

No repetimos toda la validación dentro de cada función interna. La entrada pública
review_summary pasa por el lector; llamar summarize directamente requiere conocer
su contrato. Una función que recibe una tabla mal formada puede lanzar KeyError
u otro error de pandas: anotar no convierte ese incumplimiento en un rechazo uniforme.

El resumen conserva las ocho columnas: segmento, registros, conocidos,
mediana_mxn, cobertura_pct, fecha_corte, etiqueta y fraccion. Los cuatro grupos
aparecen aunque no tengan registros. Los tipos físicos de columnas con todos
sus valores ausentes pueden diferir de los de una tabla con números; aquí no
prometemos un dtype físico fijo para todas las salidas posibles. La selección []
conserva columnas y dtypes del resumen que acaba de calcularse.

También `dict[str, pd.DataFrame]` deja preguntas: no garantiza que exista
"resumen" ni detalla las columnas de cada valor. El docstring de build_analysis
enumera corte, resumen, referencia_csv, indicadores y conciliacion. Que todos
sean tablas no autoriza intercambiarlos ni usar cualquier clave.

## 9. Docstrings que explican decisiones

Un docstring es el primer texto entre comillas de una función. Resume el propósito
y se puede consultar con `help(funcion)`; un comentario `#` explica una parte del
código, pero no sustituye esa documentación de uso.

Para redactarlo, usa esta lista como guía y ajusta el detalle al riesgo:

1. Qué hace y cuál es su unidad de trabajo.
2. Entradas, valores predeterminados y condiciones que no expresa el tipo.
3. Retorno: estructura, orden, unidades y representación de ausencias.
4. Errores relevantes y qué debe hacer quien llama.
5. Efectos: lectura/escritura, modificación de entradas y propiedad de resultados.

Lee los docstrings de coverage_pct, review_summary y summarize en sus archivos.
El primero promete comprobar tipos y conteos; el último declara qué tabla espera
previamente validada. Esa diferencia evita prometer una garantía que el código
no implementa. Un docstring no tiene que copiar cada línea del cuerpo ni cada
error posible del sistema operativo; debe permitir usar la función con criterio.

## 10. Análisis estático, validación y pruebas se complementan

| Herramienta | Cuándo actúa | Qué puede aportar | Límite en este ejemplo |
| --- | --- | --- | --- |
| Anotación/docstring | Al leer y mantener código | Expectativas y significado | No rechaza datos por sí solo |
| Checker estático | Al analizar el código | Detectar llamada textual donde espera int | No conoce todas las reglas de conteos o CSV reales |
| Validación explícita | Al llamar y leer los datos | Rechazar tipos, valores y relaciones inválidas | Debe programarse con reglas correctas |
| Prueba automatizada | Al ejecutar casos elegidos | Detectar regresiones y comprobar límites | No cubre automáticamente todas las entradas |

Un checker suele aceptar un entero negativo como int, y bool es compatible con
int en el sistema habitual de tipos. Tampoco `list[str]` expresa cuáles son los
nombres del catálogo ni su unicidad. Las validaciones siguen siendo necesarias.

El análisis es gradual: código sin anotaciones o descrito como Any puede limitar
lo que la herramienta comprueba. Any significa que se permite operar sin esa
comprobación estática; no certifica que el dato sea válido. Los paquetes de
*stubs* aportan descripciones de tipos para bibliotecas; no ejecutan validaciones
de columnas de nuestros CSV. No se instalan stubs ni checker para cerrar esta sección.

**Extensión opcional:** si ya tienes mypy en tu entorno elegido, copia la
demostración de double_annotated en un archivo propio y analízalo siguiendo su
[documentación oficial](https://mypy.readthedocs.io/en/stable/running_mypy.html).
Compara el diagnóstico de la llamada con "3" con la ejecución que imprime 33.
No presentamos la revisión del paquete completo como aprobada por un checker:
el alcance verificado aquí es ejecución y pruebas, no certificación estática.
TypedDict, Protocol y esquemas tabulares pueden estudiarse cuando una necesidad
justifique más estructura; no es necesario introducir clases para este contrato.

## 11. Ejecutar los ejemplos y las pruebas

Usa el entorno elegido en [00.05](../../00_getting_started/05_environment/README.md)
con pandas, Matplotlib y Altair ya disponibles. Los recorridos empiezan en la
raíz de DS Track. No reinstales paquetes si el entorno es adecuado.

### PowerShell

```powershell
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
Set-Location curriculum/05_python_applied/01_notebook_to_modules
python ejecutar_contratos.py
$LASTEXITCODE
python -m unittest discover -s pruebas_0505 -t . -p "test_*.py" -v
$LASTEXITCODE
python -m unittest discover -s pruebas_0504 -t . -p "test_*.py" -v
$LASTEXITCODE
Set-Location ../../..
```

### Bash/Zsh

```bash
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
cd curriculum/05_python_applied/01_notebook_to_modules
python ejecutar_contratos.py
echo $?
python -m unittest discover -s pruebas_0505 -t . -p 'test_*.py' -v
echo $?
python -m unittest discover -s pruebas_0504 -t . -p 'test_*.py' -v
echo $?
cd ../../..
```

### CMD / Anaconda Prompt

```bat
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
cd curriculum\05_python_applied\01_notebook_to_modules
python ejecutar_contratos.py
echo %ERRORLEVEL%
python -m unittest discover -s pruebas_0505 -t . -p "test_*.py" -v
echo %ERRORLEVEL%
python -m unittest discover -s pruebas_0504 -t . -p "test_*.py" -v
echo %ERRORLEVEL%
cd ..\..\..
```

El script imprime `Solo anotación: 33`, cobertura 0.0 para 0/3, None para 0/0
y el rechazo previsto de True. Con las fuentes originales de octubre, educación
tiene 3 registros, 0 conocidos y mediana ausente; comercio tiene 5/5 y mediana
3100 MXN. La selección vacía imprime `(0, 8)`. El script no exporta archivos.

La colección nueva tiene **12 métodos**, y la anterior mantiene **21**; ambas
terminan con OK y código 0. Si agregaste el ejercicio de 05.04, esa colección
tendrá 22. Conserva tu trabajo. Nombres, descubrimiento y lectura de FAIL/ERROR
se explicaron en 05.04; cero métodos descubiertos no cumple la comprobación.

Las pruebas nuevas reutilizan la muestra pequeña de 05.04: allí comercio tiene
3 registros, 2 conocidos y mediana 0,5. No confundas esa fixture con la fuente
original de 24 registros. Las pruebas comprueban ambos lados de los contratos:
casos permitidos y rechazos, selección vacía, orden, no modificación y errores
de fuente. La cobertura compartida conserva los resultados anteriores.

## Práctica, criterio de salida y continuidad

Realiza el [lab 05.05](../../../labs/05_python_applied/05_types_contracts/README.md).
Puedes avanzar cuando expliques una firma y su contrato completo, distingas
None/cero/vacío, identifiques quién valida y demuestres casos válidos e inválidos.
No hay proyecto/checkpoint implementado asociado; conserva evidencia y dudas
en PROGRESS.md sin acreditar aprendizaje por la disponibilidad del material.

Después puedes estudiar [05.06 — Clases, composición y dataclasses](../06_classes_composition/README.md),
disponible como práctica opcional con objetos pequeños y composición. El [cierre 05.11](../README.md#11-cierre-del-proyecto-python)
sigue planificado; las ampliaciones 05.06–05.10 no bloquean el cierre esencial.
Volver al [índice de Python aplicado](../README.md).

## Referencias y atribución

Ejemplos propios de DS Track, con paquete y análisis de 05.01–05.04 conservados.
Se consultaron fuentes primarias el 2026-10-15, con sintaxis compatible con
Python 3.11. Ejecución local con Python 3.12.12, pandas 2.3.3, Matplotlib 3.10.7
y Altair 6.3.0. No se copian ejemplos de las fuentes ni se agregan dependencias.

- [Python: anotaciones y typing](https://docs.python.org/3.11/library/typing.html).
- [Python: parámetros, predeterminados y anotaciones](https://docs.python.org/3.11/tutorial/controlflow.html#more-on-defining-functions).
- [Python: bool y tipos incorporados](https://docs.python.org/3.11/library/stdtypes.html#boolean-values).
- [PEP 257: convenciones de docstrings](https://peps.python.org/pep-0257/).
- [Especificación de tipos: conceptos y tipado gradual](https://typing.python.org/en/latest/spec/concepts.html).
- [pandas 2.3: DataFrame](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.html).
- [pandas 2.3: datos ausentes](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/missing_data.html).
- [mypy: ejecución y límites de importaciones](https://mypy.readthedocs.io/en/stable/running_mypy.html), ampliación opcional.

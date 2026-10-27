# 05.04 — Pruebas de código y datos

[Inicio](../../../README.md) / [Módulo 05](../README.md) / **Lección 05.04**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Detectar regresiones con casos conocidos y respuestas justificadas |
| **Necesitas** | Paquete de 05.01 y unittest de la biblioteca estándar |
| **Evidencia** | Prueba propia, falla demostrada y explicación de los resultados |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Ir al lab](../../../labs/05_python_applied/04_testing/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Detectar cambios que alteran resultados o rompen una regla del análisis. Una
prueba conserva una pregunta concreta, una entrada y una respuesta esperada
para poder repetir la comprobación después de modificar el código.

## Antes de empezar

Completa [05.03 — Errores y recursos](../03_errors_resources/README.md) y su lab.
Recupera [funciones de 01.04](../../01_python_foundations/04_functions/README.md),
[calidad de datos de 02.05](../../02_pandas/05_missing_duplicates_rules/README.md)
y [uniones de 02.08](../../02_pandas/08_combine_tables/README.md).
Reutilizamos el paquete de [05.01](../01_notebook_to_modules/README.md).
No se instala pytest ni otra dependencia: unittest pertenece a Python.

**Esencial:** casos conocidos, fronteras, vacíos, fallas esperadas e interpretación
del resultado. **Práctica:** tablas, archivos temporales e integración real.
**Extensión:** orden de ejecución y diseño de nuevas pruebas; cobertura automática,
mocking y CI pueden estudiarse después. No necesitas terminar todo en una sesión.

<a id="objetivos-observables"></a>

## Qué vas a aprender

- Escribir una comprobación cuyo resultado esperado puedas justificar a mano.
- Ejecutar una prueba y una colección, comprobar cuántas se descubrieron y leer fallas.
- Diferenciar prueba de función, integración y validación de datos de cada ejecución.
- Conservar claves, tipos, ausencias y entradas al comparar tablas.
- Comprobar rechazos y escrituras fallidas sin tocar fuentes o entregas anteriores.
- Demostrar que un cambio incorrecto produce una falla y que corregirlo recupera el éxito.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Colección de pruebas](../01_notebook_to_modules/pruebas_0504/) | Consultar casos de función e integración | Para el recorrido |
| [Muestras de prueba](../01_notebook_to_modules/pruebas_0504/muestras.py) | Justificar resultados conocidos | Para el recorrido |
| [Pruebas de transformación](../01_notebook_to_modules/pruebas_0504/test_transformacion.py) | Contrastar claves, tipos y ausencias | Para el recorrido |
| [Pruebas de integración](../01_notebook_to_modules/pruebas_0504/test_integracion.py) | Seguir una ejecución completa comprobada | Para el recorrido |

Abre los recursos cuando aparezcan en el recorrido. El paquete compartido vive
en 05.01 y se reutiliza sin copiar sus módulos; conserva las fuentes y entregas
anteriores. Lee las comprobaciones y los resultados esperados antes de ejecutar.

## 1. Que termine sin error no demuestra que calcule bien

Imagina que cambiamos la cobertura de `conocidos / registros` a
`conocidos / conocidos`. El programa podría exportar CSV y figuras sin lanzar
excepciones. Sin embargo, diría 100 % aunque hubiera saldos desconocidos.
Una **regresión** es la pérdida de un comportamiento que antes debía conservarse.
Automatizar ejemplos significativos ayuda a detectarla al volver a ejecutar.

Antes de programar una prueba, escribe:

1. **Regla:** el cero cuenta como conocido; el ausente no.
2. **Entrada:** tres registros con saldos 0, 1 y desconocido.
3. **Esperado:** dos conocidos, mediana 0,5 y cobertura 2/3 × 100.
4. **Error que detectaría:** excluir cero, imputar ausencia o cambiar el denominador.

La respuesta esperada también se llama *oráculo*. Calcularla llamando otra vez
a la misma función reproduce sus errores. Aquí usamos cuentas manuales y
la referencia CSV independiente de 04.09; ninguna referencia es infalible,
por eso también revisamos las reglas y ejemplos pequeños.

## 2. Tres preguntas diferentes

| Comprobación | Pregunta | Ejemplo del paquete |
| --- | --- | --- |
| Prueba de función o unitaria | ¿Esta función cumple su comportamiento para este caso? | summarize recibe tabla tipada y conserva cero/ausencia |
| Prueba de integración | ¿Las partes trabajan juntas? | CSV → lectura → resumen → conciliación → entrega |
| Validación durante el uso | ¿Estos datos concretos cumplen las reglas al procesarlos? | read_detail rechaza claves repetidas o créditos sin correspondencia |

Una prueba usa una entrada elegida; la validación debe seguir ejecutándose
cuando llegan archivos nuevos. Haber probado una unión no vuelve válidos todos
los CSV futuros. Las veinte conciliaciones de cada entrega siguen siendo controles
de esa ejecución; no son veinte métodos de unittest.

La frontera entre pruebas depende de lo que se conecte: leer CSV temporales ya
integra función y sistema de archivos. El nombre del archivo organiza la lectura;
no convierte mágicamente una prueba en unitaria.

## 3. Elegir una muestra que puedas explicar

Las pruebas nuevas viven junto al paquete compartido en
[pruebas_0504](../01_notebook_to_modules/pruebas_0504/).
Su [muestra](../01_notebook_to_modules/pruebas_0504/muestras.py) contiene seis
observaciones. Cinco son del 31 de octubre; otra es del 30 de septiembre y
permite detectar una selección de fecha equivocada. Los identificadores son
texto con ceros iniciales. Campo vacío en CSV significa desconocido.

| Segmento, octubre | Saldos MXN | Registros | Conocidos | Mediana MXN | Cobertura |
| --- | --- | ---: | ---: | ---: | ---: |
| comercio | 0; 1; desconocido | 3 | 2 | 0,5 | 66,666… % |
| consumo | 10 | 1 | 1 | 10 | 100 % |
| educacion | desconocido | 1 | 0 | No definida | 0 % |
| servicios | Sin filas | 0 | 0 | No definida | No definida |
| Todos | 0; 1; desconocido; 10; desconocido | 5 | 3 | 1 | 60 % |

La mediana global se calcula desde [0, 1, 10], no promediando medianas de segmentos.
La mediana de [0, 1] es (0 + 1)/2: los saldos enteros no obligan a una mediana entera.
Educación tiene base y ningún conocido; servicios no tiene base. Esas dos
situaciones no deben producir la misma cobertura.

Una *fixture* es la preparación y limpieza necesarias para una prueba.
Puede ser una tabla recién creada o una carpeta temporal con CSV; no es
obligatoriamente un archivo especial. detail_fixture construye una tabla sin
usar read_detail: así podemos probar summarize aunque el lector tenga un defecto.
write_sources prepara CSV para probar el lector y el recorrido real.

## 4. Primera prueba con unittest, leída línea por línea

Abre [test_transformacion.py](../01_notebook_to_modules/pruebas_0504/test_transformacion.py).
Este ejemplo abreviado usa la misma muestra y función:

```python
import unittest
from analisis_cartera.transformacion import summarize
from pruebas_0504.muestras import CUT, detail_fixture

class PruebasResumen(unittest.TestCase):
    def test_mediana_con_cero_y_medio_peso(self):
        detail = detail_fixture()                    # preparar
        selected, summary = summarize(detail, CUT)    # actuar
        row = summary.set_index("segmento").loc["comercio"]
        self.assertEqual(row["mediana_mxn"], 0.5)     # comprobar
```

Aquí introducimos únicamente la sintaxis de clase necesaria para usar TestCase:

- `class PruebasResumen(unittest.TestCase):` agrupa comprobaciones y recibe
  las herramientas de TestCase. No exige diseñar clases para nuestro análisis;
  composición y diseño de objetos se desarrollarán en 05.06.
- `def test_...(self):` define una función dentro de esa clase, llamada método.
  self representa el caso actual. unittest crea y ejecuta esos casos por nosotros.
- `self.assertEqual(actual, esperado)` falla si los valores no son iguales.
  El método no devuelve una nota: termina normalmente o señala una diferencia.
- El nombre descriptivo explica la regla; el prefijo `test_` permite descubrirla.

El archivo completo usa `setUp(self)` para crear self.detail antes de **cada**
método de prueba. Se reutiliza la receta, no una tabla ya modificada por otro
método. Preparar → actuar → comprobar ayuda a ver qué falló. No hace falta
forzar una única afirmación cuando varias describen el mismo comportamiento.

## 5. Ejecutar desde el directorio correcto

Activa el entorno elegido en [00.05](../../00_getting_started/05_environment/README.md).
Si ya contiene las dependencias declaradas, úsalo sin reinstalar.
Los recorridos siguientes empiezan en la raíz de DS Track con ese entorno activo.
El cambio de carpeta permite importar el paquete local sin modificar sys.path.

### PowerShell

```powershell
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
Set-Location curriculum/05_python_applied/01_notebook_to_modules
python -m unittest -v pruebas_0504.test_transformacion.PruebasResumen.test_mediana_con_cero_y_medio_peso
$LASTEXITCODE
python -m unittest discover -s pruebas_0504 -t . -p "test_*.py" -v
$LASTEXITCODE
Set-Location ../../..
```

### Bash/Zsh

```bash
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
cd curriculum/05_python_applied/01_notebook_to_modules
python -m unittest -v pruebas_0504.test_transformacion.PruebasResumen.test_mediana_con_cero_y_medio_peso
echo $?
python -m unittest discover -s pruebas_0504 -t . -p 'test_*.py' -v
echo $?
cd ../../..
```

### CMD / Anaconda Prompt

```bat
python -c "import sys, pandas, matplotlib, altair; print(sys.executable); print(pandas.__version__, matplotlib.__version__, altair.__version__)"
cd curriculum\05_python_applied\01_notebook_to_modules
python -m unittest -v pruebas_0504.test_transformacion.PruebasResumen.test_mediana_con_cero_y_medio_peso
echo %ERRORLEVEL%
python -m unittest discover -s pruebas_0504 -t . -p "test_*.py" -v
echo %ERRORLEVEL%
cd ..\..\..
```

`-m unittest` ejecuta el módulo de Python; `-v` muestra los nombres.
`discover` busca archivos; `-s` indica dónde empezar, `-t .` establece la base
de importaciones y `-p` selecciona nombres. Los archivos __init__.py permiten
usar paquetes regulares, también con Python 3.11. No ejecutes estos archivos
por doble clic ni los copies fuera de su estructura.

Resultado del material original: **una prueba** en el primer comando y
**21 pruebas** en la colección, `OK` y código 0. La duración varía. Las variantes
subTest no se cuentan como métodos adicionales. El código se consulta inmediatamente
después de Python; otro comando puede sustituirlo. `Ran 0 tests` no comprueba
este material aunque aparezca OK: revisa directorio, nombres y argumentos.

## 6. Leer FAIL, ERROR y una excepción esperada

| Resultado | Interpretación inicial | Qué revisar |
| --- | --- | --- |
| ok / OK | Pasaron los casos ejecutados | Cantidad, alcance y expectativas |
| FAIL | Una comprobación encontró una diferencia | Valor observado, esperado y regla |
| ERROR | Una excepción interrumpió el caso fuera de lo previsto | Traceback, importación, preparación y operación |

Una falla puede señalar un defecto del programa **o de la propia prueba**.
No cambies la expectativa hasta que coincida solo para obtener verde: vuelve
al ejemplo manual y a la regla. Si falta pandas, revisa el intérprete;
si falta analisis_cartera, revisa la carpeta. Si aparece PermissionError en
un temporal, revisa el directorio temporal y sus permisos: no es una diferencia de mediana.

Para comprobar que se rechaza una entrada usamos:

```python
with self.assertRaises(ValueError):
    summarize(self.detail, "2026-02-30")
```

Este `with` observa la llamada: pasa si ocurre ValueError, falla si no hay
excepción y registra error si aparece otra no esperada. Protege solo la
operación bajo prueba. `assertRaisesRegex` añade una búsqueda por patrón
en el mensaje; usamos fragmentos significativos como `sin crédito correspondiente`,
sin exigir rutas o mensajes internos completos que cambian entre versiones.

`with self.subTest(cut=cut):` identifica variantes de una misma regla y permite
continuar con las siguientes cuando una falla. No sustituye separar pruebas
que tienen propósitos distintos.

## 7. Elegir la comparación adecuada

| Dato | Comprobación del material | Motivo |
| --- | --- | --- |
| Conteos, claves y 0,5 MXN | assertEqual | Resultado exacto conocido |
| Cobertura 200/3 | assertAlmostEqual con places=10 | Comparar redondeo de punto flotante en puntos porcentuales |
| Mediana/cobertura ausente | assertTrue(pd.isna(valor)) | NaN no se compara mediante igualdad ordinaria |
| Tabla conservada/reconstruida | pandas.testing.assert_frame_equal con check_exact=True | Revisar valores, tipos, índices y columnas |
| Fuente o JSON anterior | Igualdad de bytes | Debe conservarse exactamente |

0,5 tiene representación binaria exacta; 2/3 no. La tolerancia se elige por la
unidad y la precisión requerida, no para esconder una diferencia económica.
`places=10` comprueba la diferencia redondeada a diez decimales; no significa
que los datos originales tengan esa precisión. En otras aplicaciones se
definiría una tolerancia absoluta/relativa o unidades monetarias enteras.

`DataFrame == DataFrame` produce una tabla de booleanos, no una única decisión.
assert_frame_equal informa dónde difieren las tablas y comprueba dtype por defecto.
No desactives tipos para hacer pasar una clave numérica que perdió "001".
Si el orden no forma parte del contrato, primero define claves, comprueba unicidad
y ordena ambos lados de la misma manera. Aquí el orden es parte del resultado conocido.

En conservación hacemos una copia previa con `copy(deep=True)`, llamamos summarize
y comparamos. Después alteramos selected y volvemos a comparar la entrada:
esto detecta también una selección que comparta datos indebidamente. La muestra
contiene escalares; deep=True no promete copiar recursivamente objetos Python
anidados que pudieran guardarse en otras tablas.

## 8. Fronteras y vacíos que cambian el significado

No se trata de generar muchos casos al azar. Elegimos los puntos donde cambia
una regla: cero frente a positivo; cero/uno/dos conocidos; ninguna fila frente
a filas todas desconocidas; fecha válida sin observaciones frente a fecha imposible.
Vacío debe conservar estructura: columnas y tipos para poder continuar el recorrido.

El [archivo de transformación](../01_notebook_to_modules/pruebas_0504/test_transformacion.py)
comprueba esos casos. El [archivo de entrada](../01_notebook_to_modules/pruebas_0504/test_entrada.py)
añade claves duplicadas, falta de correspondencia, valores negativos, archivo
ausente y CSV con cabeceras sin registros. Una clave crédito/fecha repetida
no se arregla borrando una fila arbitraria; un crédito repetido no debe multiplicar la unión.
Los días 30 y 31 son datos de la muestra, pero este resumen no calcula mora;
incluirlos no demuestra que aquí se haya probado un umbral de atraso.

Una variante independiente usa [1, 2, 100]: su mediana 2 distingue el centro
del promedio 103/3. El lab añade [0, 0, 100] para practicar también con ceros
repetidos. Los casos complementan la muestra CSV sin cambiarla.

## 9. Archivos temporales y fallas sin dañar entregas

TemporaryDirectory crea una carpeta aislada y la elimina al cerrar el bloque:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    destination = Path(folder) / "registro.json"
    destination.write_text('{"anterior": true}', encoding="utf-8")
    # Aquí se llama y comprueba write_json_atomic; ver test_recursos.py.
```

En setUp usamos `self.addCleanup(temporary.cleanup)` para registrar la limpieza
de cada carpeta. Esa limpieza se ejecuta aun si falla el caso; no depende de que
otro método termine antes. Cada prueba recibe una carpeta nueva. Los archivos
son pequeños y desechables; la evidencia del lab se registra fuera del temporal.

[test_recursos.py](../01_notebook_to_modules/pruebas_0504/test_recursos.py)
comprueba reemplazo normal, error antes de replace y serialización inválida.
Ante falla exige bytes anteriores intactos y ausencia de temporales sobrantes;
además comprueba que se conserva la causa OSError. Usa la simulación de 05.03,
no permisos globales ni desconectar el disco. Esto prueba ese punto de falla;
no reproduce un apagón ni demuestra durabilidad total del sistema de archivos.

## 10. Integración y límites de lo comprobado

[test_integracion.py](../01_notebook_to_modules/pruebas_0504/test_integracion.py)
usa los CSV pequeños con lectura, referencia independiente y consumidores reales.
Exige total manual 5/3/1/60 y veinte conciliaciones; altera una mediana en una
copia para comprobar que reconcile rechaza la diferencia. Luego exporta, reconstruye
desde fuentes conservadas, compara tablas y exige que un destino existente quede intacto.
Las tres simulaciones de 05.03 deben conservar carpeta parcial sin cierre válido.

Las figuras se guardan mediante el backend Agg, seleccionado para estas pruebas
sin ventanas. Se comprueba que no quedan figuras abiertas. No comparamos bytes
de PNG/SVG: formato y metadatos pueden variar. Esta suite no automatiza la revisión
visual ni los comandos completos de terminal de 05.02/05.03. Una entrega válida
todavía requiere revisar figuras y narrativa; ningún OK acredita aprendizaje.

La configuración `tool.pytest.ini_options` de la raíz no ejecuta estas pruebas;
es una configuración de otra herramienta. Aquí se utiliza el comando explícito
de unittest. No hace falta instalar pytest ni agregar dependencias para continuar.

## 11. Comprobar que una prueba puede detectar el cambio

En el [lab 05.04](../../../labs/05_python_applied/04_testing/README.md) provocarás
una expectativa equivocada de forma controlada y después la restaurarás.
Eso enseña a leer FAIL. También diseñarás un caso nuevo: [0, 0, 100] distingue
mediana 0 de promedio 33,333…; [0, 1] no distingue ambas operaciones.
Una prueba que pasa con un cálculo incorrecto necesita un caso más informativo.

Al revisar este material se comprobó además, sobre copias temporales del paquete,
que sustituir mediana por promedio, cambiar el denominador o excluir ceros
provoca fallas. El paquete original y sus consumidores permanecen conservados.
Estas comprobaciones acotan ejemplos de regresión, no demuestran ausencia de todos los defectos.

<a id="práctica-criterio-de-salida-y-continuidad"></a>

## Práctica

Realiza el [lab 05.04](../../../labs/05_python_applied/04_testing/README.md) para
añadir un caso con respuesta manual y demostrar una regresión y su corrección.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Caso propio y respuesta esperada razonada | Descubrimiento de pruebas, fallo relevante y recuperación | Por qué el caso puede detectar un error |
| Nota sobre colección y datos | Entradas, claves, tipos y ausencias conservados | Diferencia entre pruebas del programa y validación de cada entrada |

Puedes avanzar cuando ejecutes y expliques la colección, interpretes una falla,
agregues un caso con respuesta manual y distingas validación de datos y pruebas.

Quien aprende realiza la práctica y explica las decisiones; su compañero revisa.
Tu compañero pregunta qué modificación incorrecta detectaría tu caso y por qué.
Guarda evidencia, ayudas y dudas en una nota personal junto a tu práctica.
PROGRESS.md registra el desarrollo editorial, no tu expediente de aprendizaje.
No hay proyecto ni checkpoint implementado asociado en projects/; esta práctica
reutiliza el paquete educativo sin dar por completado un proyecto del catálogo.

<a id="referencias-y-atribución"></a>

## Referencias

Ejemplos propios de DS Track sobre el análisis compartido de 05.01–05.03;
referencia CSV/statistics procedente de 04.09. Consulta: 2026-10-15.
APIs de Python 3.11 y pandas 2.3.3; comprobación local con el entorno existente,
sin nuevas dependencias. unittest y tempfile son biblioteca estándar.

- [Python: unittest](https://docs.python.org/3.11/library/unittest.html), ejecución y herramientas de comprobación.
- [Python: TemporaryDirectory](https://docs.python.org/3.11/library/tempfile.html#tempfile.TemporaryDirectory), preparación y limpieza temporal.
- [Python: sentencia assert](https://docs.python.org/3.11/reference/simple_stmts.html#the-assert-statement), omisión con optimización.
- [pandas 2.3: assert_frame_equal](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.testing.assert_frame_equal.html), comparación de tablas.

La sentencia Python `assert condicion` puede omitirse con `python -O`.
Por eso la validación necesaria para aceptar datos usa comprobaciones y `raise`
explícitos. Los métodos de TestCase como assertEqual son llamadas normales,
distintas de esa sentencia. Pasar una suite tampoco reemplaza validaciones al usar el programa.

## Siguiente paso

Después de la práctica y su comprobación, la continuación del núcleo es
[05.05 — Tipos y contratos de funciones](../05_types_contracts/README.md).

[← Módulo 05](../README.md) · [Lab 05.04](../../../labs/05_python_applied/04_testing/README.md) · [Siguiente →](../05_types_contracts/README.md)

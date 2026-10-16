# Lab 05.08 — Funciones como valores y decoradores

## Entrada, propósito y resultado

Completa la [lección 05.08](../../../curriculum/05_python_applied/08_functions_decorators/README.md).
Usa el entorno elegido y el paquete compartido. Esta extensión no requiere
dependencias nuevas, notebook ni un checker. No hay proyecto/checkpoint implementado asociado.

**Resultado:** explicación de función/llamada, envoltura revisada, tablas
conciliadas y una prueba propia. Puedes dividirlo en sesiones de funciones
como valores, sintaxis @ y conservación del comportamiento.

## A. Función o resultado — base

Desde 01_notebook_to_modules, inicia `python` y prepara:

```python
from analisis_cartera.contratos import coverage_pct

def evaluate(operation, known, total):
    return operation(known, total)

operation = coverage_pct
result = coverage_pct(2, 3)
```

1. Predice el tipo de operation y result; después consulta type.
2. Ejecuta evaluate(operation, 0, 3) y evaluate(operation, 0, 0).
3. Explica qué fallaría al pasar result en lugar de operation.
4. Describe quién llama a len en el ejemplo sorted de la lección.

**Comprobación:** identificas dónde se guarda una función y dónde se ejecuta.
**Evidencia:** tabla breve con expresión, objeto recibido y resultado esperado.

<details>
<summary>Ver solución razonada de A</summary>

operation es una función; result es float. Las llamadas producen 0.0 y None.
Si evaluate recibe result, intenta llamar un número y aparece TypeError.
sorted recibe len como función y la llama para obtener claves de orden;
no le entregamos el resultado de len().

</details>

## B. Dos momentos y dos return — base

1. Ejecuta el ejemplo announce de la lección, desde su definición hasta la llamada.
2. Identifica qué se ejecuta al preparar observed y qué al llamarla.
3. Explica por qué el return exterior devuelve wrapped y el interior devuelve result.
4. Escribe en papel la forma expandida de @log_call, sin aplicar el decorador dos veces.
5. Sal con exit() y sigue el recorrido completo de tu shell en la lección.
   Registra intérprete, comandos y códigos de script/colecciones.

**Comprobación:** “Envoltura preparada” aparece antes de “Antes”; la llamada
devuelve 0.0. Original: trece métodos nuevos y setenta y cuatro combinados, OK/0.
**Evidencia:** flujo de preparación/llamada y salida comentada.

<details>
<summary>Ver solución razonada de B</summary>

announce crea y devuelve wrapped; todavía no calcula cobertura. Al llamar
observed se imprime Antes, se ejecuta coverage_pct, se imprime Después y se
devuelve su resultado. El return exterior no debe ejecutar wrapped. El interior
no debe perder el resultado ni convertir un error en None.
@log_call sobre una definición equivale, en este caso, a definir la función
y después reasignar su nombre mediante `function = log_call(function)`.

</details>

## C. Argumentos, identidad y metadatos — práctica

En una nueva sesión `python` desde el mismo directorio:

```python
import inspect
from analisis_cartera.instrumentacion import log_call

def keep(items, *, marker=None):
    """Devolver el mismo objeto recibido, sin copiarlo."""
    return items

observed = log_call(keep)
items = []
returned = observed(items, marker=0)
print(returned is items)
print(observed.__name__)
print(observed.__doc__)
print(observed.__wrapped__ is keep)
print(inspect.signature(observed))
print(inspect.signature(observed, follow_wrapped=False))
```

1. Explica por qué la prueba de identidad es más precisa que == para este contrato.
2. Identifica cómo se recogieron/reexpidieron marker y la lista.
3. Relaciona la firma visible con __wrapped__ y la firma sin seguimiento con
   *args/**kwargs. ¿Impone wraps las condiciones del docstring?
4. Explica por qué puedes no ver mensajes INFO en esa sesión, aunque la función se ejecute.

**Comprobación:** misma lista, nombre/documentación conservados y enlace original.
**Evidencia:** resultados y explicación de lo que wraps aporta y no aporta.

<details>
<summary>Ver solución razonada de C</summary>

La identidad es True: no se devuelve otra lista simplemente igual. args recoge
items y kwargs recoge marker=0; la llamada con asteriscos los reenvía. wraps
conserva el nombre keep y su docstring, y enlaza la función original.
inspect.signature muestra (items, *, marker=None); sin seguir el enlace muestra
los parámetros variables. El docstring sigue siendo documentación, no validación.
El logger no configura la consola al importarse y el nivel puede ocultar INFO.

</details>

## D. Conciliación y falla prevista — práctica

1. Lee logged_indicators en instrumentacion.py y localiza la delegación a 05.07.
2. Ejecuta ejecutar_decoradores.py con el recorrido de la lección.
3. Separa las dos llamadas: una válida con tamaño 7 y otra inválida con tamaño 0.
   Relaciona sus mensajes Inicio/Fin/Falla con la ruta de retorno o excepción.
4. Comprueba Todos 24/21, mediana 2300 MXN y cobertura 87,5 % en la fuente original.
5. Lee test_error_y_causa_conservados_sin_fin. Explica qué prueban is y __cause__.
6. Lee test_retorno_iterador_no_se_consume_ni_certifica. Explica el alcance de Fin.

**Comprobación:** equivalencia de tablas, error visible y ninguna falsa confirmación
de éxito para la llamada inválida. No se generan entregas.
**Evidencia:** tabla con llamada, mensajes, resultado/error y límite de la observación.

<details>
<summary>Ver solución razonada de D</summary>

La válida registra Inicio/Fin y devuelve indicadores; la inválida Inicio/Falla
y propaga ValueError. El Fin de la primera no corresponde a la segunda.
El script atiende deliberadamente ese rechazo después de demostrarlo.
La prueba de error exige el mismo objeto excepción y la misma causa: no basta
producir otro ValueError con mensaje parecido. Un iterador retornado sigue
sin consumirse; ese Fin solo afirma que la función normal devolvió su objeto.

</details>

## E. Un error no debe repetir el efecto — práctica

1. En pruebas_0508/test_decoradores.py agrega a PruebasEnvoltura el método
   test_falla_no_repite_efecto. Conserva tus ediciones personales.
2. Prepara una función que añada una marca a una lista y lance un ValueError conocido.
3. Envuélvela, captura su excepción y comprueba que solo hay una marca.
4. Captura registros con assertLogs y comprueba Inicio/Falla, sin Fin.
5. Ejecuta la colección nueva: con tu caso debe descubrir catorce métodos.

**Comprobación:** misma excepción y un solo efecto; ningún reintento añadido
por la instrumentación. **Evidencia:** método, ejecución y razón de cada esperado.

<details>
<summary>Ver una solución razonada de E</summary>

Dentro de la clase existente:

```python
    def test_falla_no_repite_efecto(self):
        calls = []
        error = ValueError("Falla prevista")

        @log_call
        def operation():
            calls.append("efecto")
            raise error

        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            with self.assertRaises(ValueError) as caught:
                operation()
        self.assertEqual(calls, ["efecto"])
        self.assertIs(caught.exception, error)
        self.assertEqual([r.getMessage() for r in captured.records],
                         ["Inicio: operation", "Falla: operation"])
```

LOGGER_NAME y log_call ya están disponibles en el archivo. La marca es un efecto
pequeño y local que permite detectar una repetición sin escribir entregas.
assertLogs captura los mensajes temporalmente y los consulta mediante records.
No se garantiza repetibilidad de una operación solo por envolverla: reintentos
requieren otro contrato, especialmente ante escrituras.

</details>

## Extensión opcional

Explica `a(b(function))` cuando hay dos decoradores. Predice qué ocurriría si
aplicaras log_call dos veces y cómo distinguirías los mensajes de una doble
envoltura de dos ejecuciones del cálculo. No hace falta modificar el paquete.
Propón cuándo bastaría registrar explícitamente una llamada sin crear un decorador.

## Reflexión, evidencia y continuidad

- ¿Qué cambia al pasar una función en lugar de su resultado?
- ¿Qué captura un cierre y qué se ejecuta al importar una función decorada?
- ¿Qué preserva wraps y qué sigue necesitando validación/pruebas?
- ¿Por qué retornar None normalmente difiere de ocultar una excepción con None?
- ¿Qué observación faltaría para declarar terminado el consumo de un generador?

Registra resultados y dudas en PROGRESS.md. Puedes cerrar esta extensión cuando
expliques el flujo y compruebes argumentos, retorno, errores y límites con tus
palabras. Desarrollar o ejecutar el material no acredita aprendizaje.

Si sigues las ampliaciones, continúa con el
[05.09 — Medir antes de optimizar](../../../curriculum/05_python_applied/09_measure_optimize/README.md),
disponible con lab de extensión. El cierre 05.11 sigue planificado; esta extensión no bloquea
el núcleo. Volver a la [lección 05.08](../../../curriculum/05_python_applied/08_functions_decorators/README.md).

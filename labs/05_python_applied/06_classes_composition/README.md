# Lab 05.06 — Clases, composición y dataclasses

## Entrada, propósito y resultado

Completa la [lección 05.06](../../../curriculum/05_python_applied/06_classes_composition/README.md).
Esta es una práctica opcional. Usa el paquete compartido y el entorno elegido;
no requiere dependencias nuevas ni notebook. No hay proyecto/checkpoint
implementado asociado.

**Resultado:** comparación razonada de representaciones, explicación de estado
y composición, ejemplos ejecutados y una prueba propia. Puedes repartirlo en
sesiones: clase manual, dataclass y revisión con pruebas.

## A. Elegir antes de construir — base de la ampliación

Para cada caso, elige función, diccionario o clase/dataclass y justifica:

1. Calcular una sola cobertura de 2/3.
2. Recibir un objeto JSON con claves que aún debes validar.
3. Conservar corte/segmentos para preparar varias solicitudes comparables.
4. Transformar una tabla de miles de filas con pandas.

Lee CoverageCounts, ReviewOptions y ReviewJob en objetos.py. Describe en una
frase la responsabilidad de cada una; identifica qué función conserva el cálculo.

**Comprobación:** tu decisión responde a una necesidad y al costo añadido.
**Evidencia:** tabla de cuatro decisiones y mapa de tres responsabilidades.

<details>
<summary>Ver solución razonada de A</summary>

Una función basta para la cobertura aislada; un diccionario validado permite
inspeccionar el JSON recibido. Una dataclass puede dar nombres estables a
opciones que se reutilizan. La transformación tabular conserva pandas y
funciones; no necesita una instancia nueva por fila.
CoverageCounts reúne dos conteos y delega la operación en coverage_pct;
ReviewOptions conserva parámetros validados; ReviewJob compone fuente/opciones
y delega el resumen en review_summary. Una decisión diferente es aceptable si
explica el beneficio concreto y conserva contratos y resultados.

</details>

## B. Predecir estado y alias — base de la ampliación

Desde 01_notebook_to_modules, inicia `python` y prepara:

```python
from analisis_cartera.objetos import CoverageCounts

first = CoverageCounts(2, 3)
alias = first
second = CoverageCounts(2, 3)
alias.known = 1
```

1. Antes de ejecutarlas, predice first.known, second.known, first is alias y
   first is second. Después comprueba.
2. Compara first.percentage() con CoverageCounts.percentage(first).
3. Reasigna alias.known a 4 y llama first.percentage(). Identifica el error.
4. Explica qué validó __init__ y por qué no impidió esa reasignación posterior.
5. Sal con exit(); sigue el recorrido completo de tu shell en la lección para
   ejecutar el script y las tres colecciones.

**Comprobación:** el método observa el estado de la instancia y rechaza 4/3.
**Evidencia:** predicciones, resultados y códigos/cantidades de las colecciones.

<details>
<summary>Ver solución razonada de B</summary>

first.known es 1; second.known sigue en 2. first is alias es True y first is
second es False. Las dos formas de llamar al método dan 100/3 aproximadamente.
La asignación a 4 modifica el mismo objeto que first; percentage llama la
validación y lanza ValueError. El inicializador validó 2/3 al construir; no
intercepta cada asignación futura. Los atributos públicos de esta clase son mutables.

Las colecciones originales tienen 13 métodos nuevos, 12 de 05.05 y 21 de
05.04, con OK/código 0. Los métodos de ejercicios propios aumentan esas cifras.

</details>

## C. Configuración y composición — práctica

En una sesión nueva `python` desde el mismo directorio:

```python
from dataclasses import replace
from pathlib import Path
from pandas.testing import assert_frame_equal
from analisis_cartera.objetos import ReviewJob, ReviewOptions
from analisis_cartera.revision import review_summary

source = Path("../../03_sql_databases/01_relational_sqlite/data")
options = ReviewOptions(segments=("educacion", "comercio"))
job = ReviewJob(source, options)
actual = job.summary()
expected = review_summary(source, options.cut, segments=list(options.segments))
assert_frame_equal(actual, expected, check_exact=True)
print(actual[["segmento", "registros", "conocidos", "mediana_mxn", "cobertura_pct"]])
```

1. Explica qué objeto contiene a cuál y quién lee los CSV.
2. Consulta job.options is options. ¿Se duplicaron las opciones al construir job?
3. Prepara `empty_job = replace(job, options=replace(options, segments=()))`.
   Compara forma del resumen y opciones originales.
4. Intenta cambiar options.cut mediante asignación y lee la excepción.
5. Prueba construir ReviewOptions con cut=None y con segments=["comercio"].
   Explica por qué el contrato de esta configuración difiere de la función de 05.05.

**Comprobación:** resumen equivalente, orden solicitado y ausencias preservadas;
tupla vacía produce (0, 8) sin alterar el original.
**Evidencia:** comparación de tablas, errores identificados y diagrama explicado.

<details>
<summary>Ver solución razonada de C</summary>

job contiene options; summary delega a review_summary, que lee y concilia.
La referencia pasada se conserva (is True); es una configuración validada con
campos de solo lectura. replace crea instancias nuevas sin modificar las previas.
La asignación normal lanza FrozenInstanceError. cut=None y selección como lista
se rechazan con TypeError: aquí se almacena texto y tupla; el método adapta esa
tupla a la interfaz existente de la función.

Con los CSV originales, educación tiene 3/0 y mediana ausente; comercio 5/5
y mediana 3100. No son las cifras de la fixture pequeña usada en las pruebas.

</details>

## D. Añadir una prueba de variación — práctica

1. Abre pruebas_0506/test_objetos.py y conserva tus ediciones personales.
2. En PruebasTrabajo agrega test_replace_de_trabajo_conserva_original.
3. Sobre self.source, crea un trabajo con solo comercio y corte predeterminado.
4. Usa replace para preparar septiembre sin modificar el trabajo original.
5. Comprueba los cortes guardados y las medianas de ambas ejecuciones:
   octubre 0,5; septiembre 900. Explica esas cifras desde muestras.py de 05.04.
6. Ejecuta la colección 05.06: ahora debe descubrir catorce métodos.

**Comprobación:** cambiar opciones crea otro trabajo y realmente cambia el corte
delegado, mientras conserva el original.
**Evidencia:** método propio, cuenta manual y resumen de ejecución.

<details>
<summary>Ver una solución razonada de D</summary>

Agregar dentro de la clase existente, con la misma indentación que los demás métodos:

```python
    def test_replace_de_trabajo_conserva_original(self):
        original = ReviewJob(self.source, ReviewOptions(segments=("comercio",)))
        changed = replace(original, options=replace(original.options, cut="2026-09-30"))
        self.assertEqual(original.options.cut, "2026-10-31")
        self.assertEqual(changed.options.cut, "2026-09-30")
        self.assertEqual(original.summary().iloc[0]["mediana_mxn"], 0.5)
        self.assertEqual(changed.summary().iloc[0]["mediana_mxn"], 900)
```

replace, ReviewJob y ReviewOptions ya están importados. La fixture de octubre
tiene [0, 1, desconocido] en comercio, cuya mediana conocida es 0,5; septiembre
contiene un solo saldo 900 en ese grupo. Esta prueba detecta una delegación que
ignore el corte de las opciones. No demuestra que futuros CSV sean válidos.

</details>

## Extensión opcional — fábrica y frozen no son lo mismo

Ejecuta los ejemplos SharedNotes, OwnNotes y Notes de la lección por separado.
Predice qué lista se comparte, cuál se crea por instancia y por qué append
puede funcionar dentro de una dataclass frozen. No modifiques ReviewOptions
para guardar listas: compara los diseños en los ejemplos aislados.

## Reflexión, evidencia y continuidad

- ¿Qué representa tu objeto y qué operación debería seguir siendo una función?
- ¿Qué diferencia hay entre alias, igualdad por campos y copia?
- ¿Qué valida __post_init__ y qué validación sigue pendiente hasta summary()?
- ¿Por qué frozen no conserva una instantánea de los CSV?
- ¿Qué aporta composición en este ejemplo y qué costo agrega frente a la función?

Registra resultados, decisiones y dudas en PROGRESS.md. Completar material o
ejecutar ejemplos no acredita por sí solo el aprendizaje del estudiante.

Si sigues las ampliaciones, continúa con el
[05.07 — Iteradores y generadores](../../../curriculum/05_python_applied/07_iterators_generators/README.md),
disponible como extensión. El cierre 05.11 está disponible con lab; esta ampliación no
bloquea el núcleo. Volver a la [lección 05.06](../../../curriculum/05_python_applied/06_classes_composition/README.md).

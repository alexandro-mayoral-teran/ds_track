# Lab 05.07 — Iteradores y generadores

## Entrada, propósito y resultado

Completa la [lección 05.07](../../../curriculum/05_python_applied/07_iterators_generators/README.md).
Esta extensión usa el paquete y las fuentes conservadas, con el entorno elegido.
No requiere nuevas dependencias, notebook ni datos grandes. 05.06 no es
requisito para escribir los generadores. No hay proyecto/checkpoint implementado asociado.

**Resultado:** predicciones de consumo, indicadores conciliados con distintos
tamaños de lote, un caso nuevo y un inventario de memoria. Puedes dividirlo
en sesiones de recorrido, archivos y comprobación del análisis.

## A. Predecir qué queda por consumir — base

En una sesión `python` desde 01_notebook_to_modules, escribe:

```python
values = [10, 20, 30]
walk = iter(values)
alias = walk
```

Predice y después ejecuta, en este orden:

1. next(alias).
2. list(walk).
3. list(alias).
4. list(iter(values)).
5. iter(walk) is walk.

Ejecuta además el ejemplo squares de la lección y explica cuándo aparece el
mensaje que está dentro del cuerpo. No confundas crear otro generador con
reiniciar el anterior.

**Comprobación:** puedes dibujar la posición después de cada consumo.
**Evidencia:** tabla de predicción/resultado y explicación de alias.

<details>
<summary>Ver solución razonada de A</summary>

Resultados: 10; [20, 30]; []; [10, 20, 30]; True. alias y walk comparten el
avance. La lista sigue disponible y permite otro iterador. En squares el mensaje
interno aparece al primer next, después de “Generador creado”; después de
entregar 4 y 9, ese generador queda agotado.

</details>

## B. Último lote y errores diferidos — base

Importa iter_batches en la misma sesión:

```python
from analisis_cartera.iteracion import iter_batches

walk = iter_batches([1, 2, 3, 4, 5], 2)
print(next(walk))
print(list(walk))
print(list(walk))
```

1. Predice y comprueba los tres resultados.
2. Repite con fuente vacía y con tamaño 20 sobre cinco valores.
3. Crea `invalid = iter_batches([1], 0)`. Identifica en qué llamada aparece
   ValueError y dónde tendría que estar try/except.
4. Explica qué ocurriría si solo se entregaran lotes de tamaño exactamente 2.
5. Sal con exit() y sigue el recorrido de tu shell en la lección para ejecutar
   script, colección nueva y colección combinada. Conserva las cantidades/códigos.

**Comprobación:** mantienes [5], distingues fin normal de error y no reinicias
accidentalmente el recorrido. Original: 15 métodos nuevos y 61 combinados.
**Evidencia:** resultados, comandos, intérprete y códigos de salida.

<details>
<summary>Ver solución razonada de B</summary>

Se imprime [1, 2], luego [[3, 4], [5]] y finalmente []. La fuente vacía no
entrega lotes; tamaño 20 entrega una lista con los cinco elementos.
La validación de cero ocurre al consumir invalid, por ejemplo con next, no
al crearlo. Exigir lotes completos descartaría [5] y rompería conteos y resultados.
El código de salida de script/pruebas correctos es 0; no basta obtener OK con
cero pruebas descubiertas. Los ejercicios propios aumentan los métodos contados.

</details>

## C. Archivo abierto durante el consumo — práctica

Ejecuta el ejemplo con path, DictReader y salida temprana de la lección.

1. Explica por qué handle.closed es False tras break dentro de with.
2. Comprueba que es True al salir del bloque.
3. Identifica qué objeto posee el archivo: reader, iter_batches o el llamador.
4. Explica el problema de devolver un DictReader después de cerrar su archivo.

**Comprobación:** el consumo se realiza mientras el recurso está abierto;
el cierre no depende de agotar el generador.
**Evidencia:** secuencia de estados y responsable del cierre.

<details>
<summary>Ver solución razonada de C</summary>

break termina el ciclo, pero el with exterior continúa activo. El llamador
abrió el archivo y su bloque lo cierra al salir. Reader y generador consumen
esa fuente; iter_batches no promete cerrarla. Devolver un lector cuyo with
ya terminó deja pendiente un consumo sobre un archivo cerrado. Una excepción
también debe salir por el with para liberar el recurso.

</details>

## D. Conciliar y explicar la memoria — práctica

Desde 01_notebook_to_modules, inicia `python` y prepara:

```python
from pathlib import Path
from pandas.testing import assert_frame_equal
from analisis_cartera.flujo import build_analysis
from analisis_cartera.iteracion import batch_indicators

source = Path("../../03_sql_databases/01_relational_sqlite/data")
expected = build_analysis(source, "2026-10-31")["indicadores"]
for size in [1, 7, 100]:
    actual = batch_indicators(source, "2026-10-31", batch_size=size)
    assert_frame_equal(actual, expected, check_exact=True)
print(actual)
```

1. Verifica Todos: 24/21, mediana 2300 MXN y cobertura 87,5 %.
2. Explica por qué educación conserva tres registros sin mediana y con cobertura 0.
3. Calcula el error de promediar medianas de los lotes [0, 0] y [100].
4. Identifica qué guardan groups, seen, values y all_values dentro de la función.
   ¿Qué cambia al reducir batch_size y qué estructuras siguen creciendo?
5. Lee test_duplicado_entre_lotes_y_fuera_del_corte. Explica qué se perdería
   reiniciando seen en cada lote o filtrando antes de validar.

**Comprobación:** tablas equivalentes para todos los tamaños y límite de memoria
explicado sin prometer mejoras de tiempo o memoria no medidas.
**Evidencia:** conciliación, cuenta manual e inventario de objetos vivos.

<details>
<summary>Ver solución razonada de D</summary>

Los valores originales coinciden con el recorrido completo. Educación tiene
base 3 y ningún conocido; su cobertura es 0, pero no hay mediana. El promedio
de medianas 0 y 100 sería 50; la mediana de [0, 0, 100] es 0.
groups retiene el catálogo; seen todas las claves; values los saldos conocidos
del corte; all_values reúne referencias para la mediana global. Reducir el
lote no elimina esas estructuras ni los ordenamientos temporales.
Un duplicado fuera del corte también invalida el archivo. seen debe atravesar
los lotes; el filtro no debe ocultar ese problema.

</details>

## E. Agregar un caso del último lote — práctica

1. En pruebas_0507/test_iteracion.py agrega a PruebasIndicadores el método
   test_ultimo_lote_aporta_al_resultado. Conserva tus ediciones personales.
2. Sobre self.source crea tres créditos con cortes de saldos [0, 100, 100] en
   comercio. Usa batch_size=2; la última fila debe participar en el resultado.
3. Antes de programar, calcula registros, conocidos, mediana y cobertura.
4. Ejecuta la colección: debe descubrir dieciséis métodos con tu caso nuevo.

**Comprobación:** tres registros/conocidos, mediana 100 y cobertura 100 %;
descartar el último lote cambiaría la mediana a 50.
**Evidencia:** método propio, cálculo y resumen de ejecución.

<details>
<summary>Ver una solución razonada de E</summary>

Dentro de la clase existente:

```python
    def test_ultimo_lote_aporta_al_resultado(self):
        cuts = [["001", CUT, "0", "0"], ["002", CUT, "100", "0"],
                ["003", CUT, "100", "0"]]
        write_sources(self.source, cuts=cuts, credits=CREDITS[:3])
        row = batch_indicators(self.source, CUT, batch_size=2).set_index("segmento").loc["comercio"]
        self.assertEqual(row["registros"], 3)
        self.assertEqual(row["conocidos"], 3)
        self.assertEqual(row["mediana_mxn"], 100)
        self.assertEqual(row["cobertura_pct"], 100)
```

Los nombres ya están importados en el archivo. El caso complementa las pruebas
existentes; no demuestra por sí solo ausencia de errores para cualquier CSV.
Trabaja con archivos temporales, conservando las fuentes del curso.

</details>

## Reflexión, evidencia y continuidad

- ¿Qué consumidores avanzan el iterador y por qué no vuelve a empezar?
- ¿Qué se conserva al suspenderse en yield y cuándo aparece una falla del cuerpo?
- ¿Por qué un lote corto normal difiere de una fuente que falla a mitad del lote?
- ¿Qué estados impiden afirmar que todo el análisis usa memoria constante?
- ¿Qué garantiza terminar la conciliación y qué seguiría requiriendo revisión?

Registra resultados y dudas en PROGRESS.md. Puedes cerrar esta extensión cuando
expliques el consumo, concilies el resultado y justifiques recursos/memoria con
tus palabras. La disponibilidad del material no acredita aprendizaje.

Continúa, si sigues las ampliaciones, con el
[05.08 — Funciones como valores y decoradores](../../../curriculum/05_python_applied/08_functions_decorators/README.md),
disponible como extensión. El cierre 05.11 sigue planificado; esta extensión no bloquea
el núcleo. Volver a la [lección 05.07](../../../curriculum/05_python_applied/07_iterators_generators/README.md).

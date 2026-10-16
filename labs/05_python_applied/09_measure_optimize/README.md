# Lab 05.09 — Medir un cambio y justificar la decisión

## Propósito y entradas

Este lab de **extensión** acompaña
[05.09 — Medir antes de optimizar](../../../curriculum/05_python_applied/09_measure_optimize/README.md).
Revisa sus ejemplos y utiliza sus recorridos completos de PowerShell, Bash/Zsh
o CMD con el entorno elegido ya disponible. Una sesión puede cubrir solo parte
de las actividades. No hace falta instalar paquetes ni desarrollar decoradores.

Recibes el paquete de
[05.01](../../../curriculum/05_python_applied/01_notebook_to_modules/README.md),
[medicion.py](../../../curriculum/05_python_applied/01_notebook_to_modules/analisis_cartera/medicion.py),
[ejecutar_medicion.py](../../../curriculum/05_python_applied/01_notebook_to_modules/ejecutar_medicion.py)
y [trece pruebas](../../../curriculum/05_python_applied/01_notebook_to_modules/pruebas_0509/test_medicion.py).
Las fuentes previas se conservan: 48 cortes, dos fechas, 24 observaciones por
fecha. El experimento ampliado solo crea listas de fechas, no nuevas carteras.

Entrega una carpeta nueva de evidencia ignorada por Git, una explicación breve
y una prueba propia. No borres corridas anteriores para repetir. No hay
proyecto/checkpoint implementado asociado a este lab.

## A. Pregunta, frontera y condiciones

Antes de ejecutar, escribe la hipótesis sobre fechas repetidas y el resultado que
debe conservarse. Identifica qué incluye cada una de las tres fases del análisis.
Explica por qué no puedes sumar sus tiempos ni usar la transformación sobre
datos ya leídos para afirmar cuánto tarda una entrega con figura.

Anota tu versión de Python, entorno elegido, repeticiones y tamaños previstos.
Predice qué cambiaría si todas las fechas fueran distintas. No necesitas acertar
los segundos; explica de dónde podría venir el ahorro y qué estado se acumula.

<details>
<summary>Orientación para comprobar la frontera</summary>

El parseo de un mismo texto se repite N veces en la base y U veces en la
candidata. Ambos recorren N elementos y deben contar N; un conjunto local evita
repetir conversiones, pero retiene hasta U textos. lectura_validada incluye
lectura/conversión/unión; transformacion_preleida empieza después de leer;
analisis_conciliado vuelve a leer y añade referencia/conciliación. Son llamadas
solapadas con tareas distintas, no tres partes disjuntas de una misma ejecución.

</details>

## B. Ejecutar y leer observaciones

Ejecuta el script con cinco repeticiones y las pruebas mediante el recorrido de
tu shell en la lección. Revisa el código de salida inmediatamente después de
cada comando. Espera 13 métodos nuevos y 87 combinados antes de añadir tu prueba.

Comprueba archivos y conteos: 60 tiempos crudos, 12 resúmenes, 12 observaciones
de memoria y 15 tiempos de fases. En tiempos.csv filtra el mismo escenario y
tamaño para comparar ambas variantes. Consulta posición para comprobar el orden
alterno; no busques los calentamientos, pues sus tiempos se descartan.

Para 48 y 4800 fechas, registra mínimo, mediana y máximo de cada variante.
Describe si el rango permite sostener la diferencia que observas. Conserva todas
las observaciones y distingue «no encuentro evidencia clara» de «son iguales».
Repite hacia otra carpeta nueva si necesitas explorar variación entre corridas.

<details>
<summary>Comprobaciones y respuesta razonada</summary>

Dos escenarios × tres tamaños × dos variantes × cinco repeticiones producen 60
filas. Cada grupo de escenario/tamaño/variante tiene cinco, y su resumen debe
cumplir mínimo ≤ mediana ≤ máximo. Los segundos son no negativos. Las
observaciones de memoria son llamadas separadas, una por cada combinación.

Es razonable encontrar ahorro con dos fechas distintas, pero ninguna cifra ni
relación entre velocidades es requisito de aprobación. Si hay mucha variación,
describe las condiciones, repite el experimento y evita una conclusión más
amplia que la evidencia. Alternar orden reduce un sesgo; no controla todos.
Las fases pueden orientar a investigar lectura/validación o conciliación, pero
su diferencia no calcula exactamente el tiempo de una subtarea.

</details>

## C. Equivalencia antes de declarar una mejora

Lee ambas funciones. Sigue a mano una entrada repetida, otra vacía y otra con
una fecha imposible después de dos válidas. Explica dónde se incrementa count
y por qué validar el tipo debe ocurrir incluso al reutilizar fechas.

Localiza las pruebas de error y consumo. Explica qué quedaría sin detectar si
solo compararas el conteo en la entrada válida. Revisa indicadores.csv y los
hashes de las fuentes en experimento.json. Para Todos, conserva 24 registros,
21 conocidos, mediana 2300 MXN y cobertura 87,5 %. Educación mantiene ausencia
de mediana por no tener saldos conocidos.

<details>
<summary>Respuesta razonada</summary>

El conteo se incrementa por elemento, fuera del if que comprueba si la fecha ya
estaba. Contar solo textos nuevos devolvería U y perdería observaciones. La
entrada vacía retorna 0; una fecha imposible lanza ValueError y un elemento de
tipo incorrecto lanza TypeError. Un iterador se detiene después del elemento
inválido sin adelantar al siguiente. Las pruebas verifican también esa posición.

Un conteo correcto puede ocultar que no se validó nada. Las pruebas de inválidos,
ausencia de caché entre llamadas y entrada intacta protegen ese comportamiento.
Las listas de este experimento no modifican fuentes ni alimentan los indicadores:
el análisis original se ejecuta y concilia aparte. Coincidir en este experimento
no convierte la candidata en reemplazo completo del lector pandas.

</details>

## D. Investigar el costo de tiempo y memoria

Abre los dos perfiles y busca normalize_cut. ¿Cuántas veces aparece llamada en
el caso repetido de 4800 elementos? Explica tottime y cumtime, y por qué sumar
los tiempos acumulados puede duplicar trabajo. No calcules la aceleración a
partir de los segundos instrumentados del perfil.

En memoria.csv compara el pico de la base/candidata para 4800 fechas repetidas
y distintas. ¿Por qué la memoria actual puede ser baja en ambas? ¿Qué memoria
de entrada quedó fuera del trazado? Explica por qué estos bytes no equivalen a
la memoria total mostrada por el administrador de tareas.

<details>
<summary>Interpretación posible, sin exigir un resultado de velocidad</summary>

Se esperan 4800 validaciones en la base y 2 en la candidata para el escenario
repetido mayor. cumtime incluye llamadas descendientes; tottime las excluye.
Los perfiles ayudan a relacionar costo con trabajo, pero instrumentar afecta
la duración. La comparación de tiempos se hace con tiempos.csv.

Cuando U=N, el conjunto retiene muchas referencias durante la llamada. Puede
liberarse antes de medir actual, mientras pico conserva la máxima acumulación
trazada. La lista preparada antes de tracemalloc.start no se cuenta como nueva
asignación. Tampoco se garantiza trazar toda asignación nativa. Un pico pequeño
en repetidas no permite afirmar que el proceso entero usa pocos bytes.

</details>

## E. Prueba propia: una fuente nueva por repetición

En la clase PruebasCronometro de test_medicion.py añade un método que mida una
función que crea `iter(dates)` en **cada llamada** y consume esa entrada mediante
validate_dates_each. Usa tres fechas, dos repeticiones y un calentamiento.
Comprueba fuera del reloj que las tres llamadas procesaron tres elementos y que
la tabla contiene dos tiempos. No impongas un límite de milisegundos.

Antes de ejecutarlo, predice qué fallaría si el iterador se creara una sola vez
fuera de la función medida. Revisa el [contrato de consumo de 05.07](../../../curriculum/05_python_applied/07_iterators_generators/README.md)
si necesitas apoyo. Ejecuta nuevamente pruebas nuevas y combinadas.

<details>
<summary>Una solución y por qué detecta un trabajo incorrecto</summary>

Inserta este método dentro de PruebasCronometro, con la misma indentación que sus
otros métodos. Los nombres importados ya están disponibles en el archivo:

```python
    def test_iterador_nuevo_en_cada_repeticion(self):
        dates = ["2026-10-31", "2026-09-30", "2026-10-31"]
        counts = []

        def operation():
            return validate_dates_each(iter(dates))

        def check(result):
            self.assertEqual(result, 3)
            counts.append(result)

        raw = repeat_timings({"base": operation}, repeats=2, warmups=1, check=check)
        self.assertEqual(counts, [3, 3, 3])
        self.assertEqual(len(raw), 2)
```

Crear un iterador nuevo permite repetir el mismo trabajo. Si guardaras uno
fuera de operation, el calentamiento lo agotaría; la primera medición devolvería
0 y check fallaría. La prueba comprueba la repetibilidad de esta preparación,
no promete que cualquier función sea repetible. Con esta solución aislada hay
14 métodos nuevos y 88 combinados; tus otros ejercicios pueden añadir más.

</details>

## Evidencia, reflexión y continuidad

Conserva tu carpeta de evidencia, la prueba y una nota con pregunta, frontera,
entorno, N/U, tiempos crudos/resumen, memoria, perfil y decisión. Anota qué
falta comprobar antes de trasladar una mejora a la ejecución completa.

- ¿Qué resultado correcto te protege de una alternativa que omite trabajo?
- ¿Qué cambió al aumentar N y qué cambió al aumentar U?
- ¿Por qué una reducción grande en esta fase no prueba el mismo ahorro total?
- ¿Qué costo de memoria/claridad aceptarías y con qué evidencia?
- ¿Cuándo preferirías conservar la implementación actual?

Puedes cerrar esta extensión cuando expliques la comparación y sus límites con
tus palabras. Registra evidencia y dudas en PROGRESS.md sin confundir desarrollar
material con completar el aprendizaje.

Si sigues las ampliaciones, continúa con la siguiente lección:
[05.10 — Integración con APIs](../../../curriculum/05_python_applied/10_api_integration/README.md),
disponible con lab. El cierre 05.11 está disponible con lab. Esta extensión no
bloquea el núcleo ni R. Volver a la
[lección 05.09](../../../curriculum/05_python_applied/09_measure_optimize/README.md).

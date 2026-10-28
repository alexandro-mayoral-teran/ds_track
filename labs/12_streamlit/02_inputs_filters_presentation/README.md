# Lab 12.02 — Entradas, filtros y presentación

[Inicio](../../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.02**

[Volver a la lección](../../../curriculum/12_streamlit/02_inputs_filters_presentation/README.md) · [Evidencia](#evidencia-y-reflexión)

## Propósito y entradas

Conectar elecciones con un subconjunto verificable y explicar su denominador.
Usa [app.py](../../../curriculum/12_streamlit/02_inputs_filters_presentation/app.py)
y sus [recorridos de arranque](../../../curriculum/12_streamlit/02_inputs_filters_presentation/recorridos.md).
La entrada son los seis registros sintéticos definidos en el script y en la
[tabla de la lección](../../../curriculum/12_streamlit/02_inputs_filters_presentation/README.md#1-pregunta-datos-y-reglas-completos).
No necesitas una entrega anterior ni cargar un CSV. No hay proyecto/checkpoint
implementado asociado. Una sesión puede cubrir parte de la actividad.

## 1. Predecir cuatro respuestas

Antes de ejecutar, anota los pares ID/saldo, cantidad, suma y proporción de créditos:

1. Octubre, ambos segmentos, mínimo 2000.
2. Septiembre, ambos segmentos, mínimo 2000.
3. Septiembre, ambos segmentos, mínimo 2001.
4. Octubre, solo servicios, mínimo 1900.

En cada caso escribe qué filas forman el universo y qué denominador utilizaste.
Explica por qué dos cortes con tres filas no deben sumarse como un único saldo.

## 2. Ejecutar y rastrear una selección

Arranca con tu gestor. Confirma los filtros visibles antes de interpretar las
métricas. Reproduce los cuatro casos y contrasta **cada ID, segmento, fecha e
importe** del detalle. Después concilia cantidad, suma y porcentaje.

Tu compañero elige un registro excluido y pide señalar la condición concreta
que no cumplió. Si una predicción era distinta, registra la corrección con tus
palabras; no cambies la tabla de entrada para forzarla.

<details>
<summary>Pista: se cumplen todos los filtros, pero cualquiera de los segmentos elegidos</summary>

`in segmentos` admite comercio o servicios si elegiste ambos. `and` exige
también el mínimo. La fecha ya se aplicó para obtener `universo`.

</details>

## 3. Investigar ceros y selecciones vacías

Prueba estas tres combinaciones y predice antes de cambiar:

- Septiembre, ambos segmentos, mínimo 0.
- Octubre, servicios, mínimo 2000.
- Octubre, ningún segmento, mínimo 0.

Comprueba que 001/septiembre, con saldo **cero conocido**, sí participa en el
primer caso. En los otros dos, registra el mensaje y explica por qué el universo
sigue teniendo tres créditos. Vuelve al caso inicial y comprueba que la tabla
anterior no queda visible como si perteneciera a la selección vacía.

## 4. Cambiar una regla en una copia

Detén el servidor y guarda una copia nueva como `output/mi_1202/app.py`.
En la condición del mínimo cambia solo `>=` por `>`. Predice septiembre, ambos
segmentos, mínimo 2000. Arranca tu copia, contrasta los pares y explica la diferencia.
La pantalla aún dice «incluye igualdad»: identifica y corrige también esa descripción
en tu copia para que el texto corresponda a la regla nueva. El original se conserva.

No se trata de decidir que una frontera sea mejor: se trata de declarar cuál
aplica y comprobar que código, texto y resultados coinciden. Los esperados de la
lección y el comprobador de autoría corresponden al original inclusivo.

## 5. Reconstruir y leer en otra ventana

Detén tu copia y vuelve a iniciar el original desde el archivo guardado.
Comprueba octubre, ambos segmentos y mínimo 2000. Abre otra pestaña independiente,
cambia los filtros en una y contrasta que no se modifican los de la otra.

En una ventana estrecha recupera los filtros desde la barra lateral y lee las
cuatro columnas del detalle. Conserva una nota de lo que revisaste y de los límites;
un comprobador automático no demuestra que otra persona entendió las etiquetas.
Al terminar, detén tu servidor con Ctrl+C.

## Comprobación razonada

<details>
<summary>Ver los resultados y su explicación después de practicar</summary>

Octubre/ambos/2000 devuelve **003/2600**, cantidad 1, saldo 2600 y 33.33%.
Septiembre/ambos/2000 devuelve **002/2000 y 003/2500**, cantidad 2, saldo 4500
y 66.67%. Subir a 2001 deja **003/2500**, cantidad 1 y 33.33%.
Octubre/servicios/1900 devuelve **002/1900**, cantidad 1 y 33.33%.
El denominador sigue siendo los tres créditos del corte, antes de los otros filtros.

Septiembre/ambos/0 incluye 001/0, 002/2000 y 003/2500: tres y 4500, 100%.
Los dos casos vacíos seleccionan cero filas y muestran cantidad 0, saldo seleccionado 0 y 0%, con mensaje.
Eso no convierte un desconocido en cero: todos los saldos de esta muestra son conocidos.

Cambiar `>=` por `>` excluye 002/2000 en septiembre con mínimo 2000; quedan
003/2500 y 33.33%. La etiqueta debe dejar de prometer igualdad en esa copia.
Cambiar solo el texto o solo el código deja una interfaz contradictoria.

Conservar una suma no basta: por ejemplo, intercambiar importes entre IDs podría
mantenerla sin conservar los pares correctos. Por eso se revisa el detalle completo.

</details>

## Evidencia y reflexión

Conserva predicciones/correcciones, filtros efectivos, pares y cuentas, además
de tu copia con la regla distinta. Indica intérprete/versión, nuevo arranque,
revisión de pantalla y ayudas recibidas en tu bitácora personal. No publiques
salidas personales ni uses PROGRESS.md como registro de aprendizaje.

- ¿Por qué elegir un segmento no convierte el denominador en uno o dos?
- ¿Qué cambiaría si la pregunta pidiera porcentaje de saldo?
- ¿Dónde se decide qué significa una lista vacía de segmentos?
- ¿Cómo detectas una métrica calculada sobre las seis filas en lugar de la selección?

Cierra cuando puedas trazar cada entrada hasta su filtro, recuperar los pares
correctos y justificar los casos vacíos y la frontera. El material y las pruebas
de autoría no acreditan por sí solos tu práctica.

[← Lección 12.02](../../../curriculum/12_streamlit/02_inputs_filters_presentation/README.md) · [Módulo 12](../../../curriculum/12_streamlit/README.md) · [Siguiente: alcance de 12.03, aún planificado →](../../../curriculum/12_streamlit/README.md#03-separar-datos-e-interfaz)

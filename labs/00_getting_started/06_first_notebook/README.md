# Lab 00.06 — Un notebook que funciona desde cero

## Relación y entrada

- Lección: [06 — Primer notebook](../../../curriculum/00_getting_started/06_first_notebook/README.md).
- Entrada: su notebook de ejemplo y el entorno preparado en la lección 05, con ipykernel.
- Proyecto: todavía no aplica.

Lee la lección y prepara el soporte de kernel en el entorno que elegiste en
00.05. Trabaja con las pausas que necesites e intenta cada parte antes de abrir
su solución. Conserva el notebook original del curriculum.

## Parte A — Reconocer y ejecutar

1. Guarda una copia como `mi_primer_notebook.ipynb` en tu carpeta personal,
   siguiendo la lección. Comprueba la ruta para reconocer qué archivo editarás.
2. Explica el recorrido de una celda: editor → kernel → Python del entorno → salida.
3. Elige tu kernel y ejecuta la consulta del intérprete. Compara con 00.05.
4. Identifica qué celdas explican y cuáles ejecutan código.
5. Predice y ejecuta los cálculos en orden.

<details>
<summary>Ver respuesta orientativa de la parte A</summary>

La celda de sys.executable señala el Python elegido en la lección 05.
Markdown explica; las celdas de código ejecutan. Los resultados iniciales son
120 y 200 MXN. El visor de GitHub muestra contenido sin ejecutar el notebook.
El editor envía el código al kernel, que lo ejecuta con el Python y los paquetes
del entorno seleccionado y devuelve una salida. La copia personal conserva tus
modificaciones sin cambiar el ejemplo original.

</details>

## Parte B — Observar el estado

1. Con las entradas originales ejecutadas, cambia las unidades de la primera
   situación a 4 **sin ejecutar esa celda**.
2. Anota el valor escrito, el que esperas en memoria y tu predicción de salida.
   Ejecuta solo el cálculo y explica por qué conserva el resultado anterior.
3. Predice qué cambiará al ejecutar las entradas y después el cálculo. Hazlo y
   contrasta el nuevo total; comprueba que la segunda venta mantiene 200 MXN.
4. Antes de reiniciar, explica si se perderá tu edición `unidades = 4`.
   Reinicia y ejecuta todo para verificar el cambio con una memoria limpia.

<details>
<summary>Ver respuesta orientativa de la parte B</summary>

El kernel conserva 3 unidades hasta que ejecutas su asignación modificada.
Después el total es `4 * 40 = 160` MXN. Reiniciar borra la memoria; Run All
vuelve a construir los valores con el código actual en el orden del documento.
Limpiar las salidas por sí solo no reinicia el estado.
El reinicio conserva el código editado: al ejecutar todo obtienes 160 y 200 MXN.
Guardar conserva el documento y sus salidas, pero no recalcula ni guarda toda
la memoria del kernel.

</details>

## Parte C — Crear y explicar

1. Agrega una celda Markdown con una predicción para 6 carpetas a 25 MXN.
2. Agrega una celda de código con entradas, cálculo y salida de esa situación.
3. Reinicia, ejecuta todo y compara el resultado con la predicción.
4. Comprueba los tres totales: 160 MXN en la primera venta modificada, 200 MXN
   en la comparación y tu predicción para las carpetas. Guarda tu copia.
5. Revisa las salidas. Limpia la que contiene la ruta personal antes de compartir
   y vuelve a guardar; conserva la comprobación completa en tu nota local.

<details>
<summary>Ver una solución de la parte C</summary>

La predicción es 150 MXN. En una nueva celda de código:

```python
producto_nuevo = "carpeta"
unidades_nuevas = 6
precio_nuevo_mxn = 25
importe_nuevo_mxn = unidades_nuevas * precio_nuevo_mxn
print(f"{unidades_nuevas} unidades de {producto_nuevo}: {importe_nuevo_mxn} MXN")
```

La celda incluye todas sus entradas. No depende de un valor que solo exista
en memoria por haber ejecutado antes una celda eliminada.

</details>

## Parte D — Pausar y retomar

1. Anota ruta de tu copia, entorno elegido, resultados, dudas y siguiente paso.
2. En otra sesión, abre esa copia, selecciona el mismo entorno como kernel y
   reinicia antes de ejecutar todo. No necesitas crear otro entorno.
3. Comprueba intérprete y totales con las entradas actuales. Explica por qué las
   salidas guardadas al abrir no bastaban para comprobar esta sesión.

<details>
<summary>Ver comprobación orientativa de la parte D</summary>

La copia conserva el código modificado. Al reconstruir los resultados con un
kernel recién reiniciado, se obtienen 160, 200 y 150 MXN. La ruta corresponde
al entorno preparado, aunque el notebook esté en otra carpeta. Si conservas
otras entradas, documenta sus resultados esperados antes de compararlos.

</details>

## Evidencia y reflexión

- Conserva el notebook con tu predicción, código y resultado comprobado.
- Explica qué intérprete usa y por qué ese kernel fue elegido.
- ¿Qué diferencia hay entre editar, ejecutar, borrar salidas y reiniciar?
- ¿Por qué una salida visible no demuestra que el código actual la produjo?
- Si tu copia personal pertenece a un repositorio Git propio, revisa los cambios
  y crea un commit después de comprobar el notebook. Si tu carpeta no utiliza
  Git, basta conservar el archivo y tu nota; no publiques en el repositorio compartido.
- Antes de compartir, limpia la salida con la ruta personal del intérprete.

Puedes continuar cuando expliques el recorrido de una celda, compruebes el
kernel, distingas archivo/memoria/salida y reconstruyas los tres cálculos tras
reiniciar. El [glosario de 00.06](../../../curriculum/00_getting_started/06_first_notebook/README.md#glosario)
te permite recuperar los términos. Conserva dudas y evidencia en tu
[bitácora personal](../../../templates/learning-session/bitacora-00.md).

## Siguiente paso

Revisa las evidencias del [nivel 0](../../../curriculum/00_getting_started/README.md)
y consulta [Python fundamental](../../../curriculum/01_python_foundations/README.md).
Python fundamental dispone de seis lecciones y labs. Continúa con
[01.01 — Variables y tipos](../../../curriculum/01_python_foundations/01_variables_types/README.md)
después de comprobar y explicar tu práctica; disponer de material no acredita
haber completado el aprendizaje del módulo 00.

# Lab 00.06 — Un notebook que funciona desde cero

## Relación y entrada

- Lección: [06 — Primer notebook](../../../curriculum/00_getting_started/06_first_notebook/README.md).
- Entrada: su notebook de ejemplo y el entorno preparado en la lección 05, con ipykernel.
- Proyecto: todavía no aplica.

Reserva 30 a 45 minutos. Lee la lección y prepara un solo kernel antes de practicar.
Intenta cada parte antes de abrir su solución.

## Parte A — Reconocer y ejecutar

1. Abre el notebook, elige tu kernel y comprueba su intérprete.
2. Identifica qué celdas explican y cuáles ejecutan código.
3. Predice y ejecuta los cálculos en orden.

<details>
<summary>Ver respuesta orientativa de la parte A</summary>

La celda de sys.executable señala el Python elegido en la lección 05.
Markdown explica; las celdas de código ejecutan. Los resultados iniciales son
120 y 200 MXN. El visor de GitHub muestra contenido sin ejecutar el notebook.

</details>

## Parte B — Observar el estado

1. Cambia las unidades de la primera situación a 4 sin ejecutar esa celda.
2. Ejecuta solo el cálculo y explica por qué conserva el resultado anterior.
3. Ejecuta las entradas y después el cálculo; comprueba el nuevo total.
4. Reinicia y ejecuta todo para verificar tu cambio desde cero.

<details>
<summary>Ver respuesta orientativa de la parte B</summary>

El kernel conserva 3 unidades hasta que ejecutas su asignación modificada.
Después el total es `4 * 40 = 160` MXN. Reiniciar borra la memoria; Run All
vuelve a construir los valores con el código actual en el orden del documento.
Limpiar las salidas por sí solo no reinicia el estado.

</details>

## Parte C — Crear y explicar

1. Agrega una celda Markdown con una predicción para 6 carpetas a 25 MXN.
2. Agrega una celda de código con entradas, cálculo y salida de esa situación.
3. Reinicia, ejecuta todo y compara el resultado con la predicción.
4. Guarda el notebook y revisa la información que contienen sus salidas.

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

## Evidencia y reflexión

- Conserva el notebook con tu predicción, código y resultado comprobado.
- Explica qué intérprete usa y por qué ese kernel fue elegido.
- ¿Qué diferencia hay entre editar, ejecutar, borrar salidas y reiniciar?
- ¿Por qué una salida visible no demuestra que el código actual la produjo?
- Si usas Git, revisa los cambios y crea un commit después de comprobar el notebook.
  No necesitas hacer push al repositorio compartido para completar el lab.
- Antes de compartir, limpia la salida con la ruta personal del intérprete.

## Siguiente paso

Revisa las evidencias del [nivel 0](../../../curriculum/00_getting_started/README.md)
y consulta [Python fundamental](../../../curriculum/01_python_foundations/README.md).
Las lecciones detalladas del siguiente módulo están por desarrollar.

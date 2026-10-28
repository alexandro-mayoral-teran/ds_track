# Lab 12.01 — Primera app y modelo de ejecución

[Inicio](../../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.01**

[Volver a la lección](../../../curriculum/12_streamlit/01_first_app_execution/README.md) · [Evidencia](#evidencia-y-reflexión)

## Propósito y entradas

Relacionar una acción en el navegador con una nueva pasada del script, su
resultado y lo impreso en la terminal. Usa el entorno de la lección, los
[recorridos de arranque](../../../curriculum/12_streamlit/01_first_app_execution/recorridos.md)
y [app.py](../../../curriculum/12_streamlit/01_first_app_execution/app.py).
No necesitas carpetas de otros labs ni crear un notebook. Proyecto/checkpoint:
no hay uno implementado asociado a esta práctica.

La entrada está dentro del script: V001 4 × 75, V002 2 × 120, V003 0 × 50 y
V004 3 × 40, en MXN. Conserva el original; tus variantes irán en una copia
personal con nombre nuevo. Puedes hacer la actividad en varias sesiones.

## 1. Predecir antes de iniciar

Escribe la cuenta de las cuatro ventas. Sin ejecutar, predice total, tabla,
marca, valor de `pasadas` y mensaje del botón para esta secuencia:

1. Primera carga.
2. Marcar «Mostrar detalle».
3. Pulsar «Repetir cálculo».
4. Desmarcar «Mostrar detalle».

Indica en cada caso dónde esperas observar el cambio: pantalla o terminal.
Tu compañero elige una predicción y pide justificarla con el orden del código.

## 2. Ejecutar y contrastar

Arranca el original con el comando de tu gestor. No ejecutes el archivo como
un script Python ordinario. Conserva la terminal y abre la URL local indicada.
Realiza la secuencia despacio. Después de cada acción anota la marca visible,
el total, `pasadas`, la visibilidad del detalle y del mensaje.

Cuando aparezca la tabla, contrasta **cada ID e importe**, no solo su suma.
Relaciona una marca con sus líneas `INICIO`/`FIN`. Si observas otra pasada
por recarga o reconexión, registra esa circunstancia sin forzar tu conteo.
No es requisito acertar la predicción: sí explicar la diferencia.

<details>
<summary>Pista: localiza qué instrucciones están antes de los widgets</summary>

El total y la inicialización de `pasadas` aparecen antes de la casilla y del
botón. La nueva pasada vuelve a atravesarlos. Ocultar la tabla no elimina ventas.

</details>

## 3. Hacer una variante y reconstruirla

Detén con Ctrl+C. Copia el archivo a `output/mi_1201/app.py`, usando otra
carpeta si ya contiene trabajo. Cambia solo el precio de V004 de 40 a 50.
Predice su importe y el total antes de iniciar **la ruta de tu copia**.

Guarda y arranca la variante. Marca la casilla y contrasta todos los importes.
Detén, vuelve a iniciar esa misma copia guardada y repite la comprobación.
Después inicia el original: debe conservar su resultado anterior. No se
requiere exportar una tabla ni guardar registros de clics en un archivo.

## 4. Separar sesión, variable y proceso

Con la app original, marca la casilla en la primera pestaña. Abre la misma URL
en otra pestaña independiente. Compara su estado inicial y luego interactúa
en una de ellas. No supongas que todas las trazas de la terminal pertenecen a
la misma sesión: relaciona las marcas de cada pantalla.

Explica por qué la casilla puede conservar su elección entre pasadas, mientras
la variable `pasadas` sigue en 1. Cierra una pestaña y observa que la terminal
puede seguir atendiendo la app. Detén el servidor explícitamente con Ctrl+C.
No detengas procesos de otras prácticas para liberar un puerto.

## Resultado y comprobación razonada

<details>
<summary>Ver resultados y explicación después de practicar</summary>

El original muestra 300/240/0/120 MXN y total **660**. Marcar la casilla muestra
las cuatro filas sin cambiar ese total. El botón provoca una nueva pasada y su
mensaje aparece entonces; al desmarcar la casilla desaparece ese mensaje.
`pasadas` sigue en **1** porque vuelve a inicializarse a cero antes de incrementar.
La marca cambia, aunque las cifras permanezcan iguales.

La variante cambia V004 a 3 × 50 = **150**, por lo que el total es **690**.
El original debe seguir en 660. Una captura de 690 no basta: explica qué archivo
se ejecutó, contrasta los cuatro pares y repite desde un arranque nuevo.

Una pestaña independiente crea otra sesión de la app y comienza con la casilla
desmarcada en este ejemplo. La elección de la primera pestaña no convierte una
variable Python en almacenamiento compartido. El servidor puede atender varias
sesiones; detenerlo sí corta la aplicación que atendía.

</details>

## Evidencia y reflexión

Conserva tu copia y una nota con predicciones, observaciones, una marca
relacionada con la terminal, cuenta manual, intérprete/versión y nuevo arranque.
Registra las ayudas que necesitaste y lo que aún no entiendes. No subas salidas
personales al repositorio del curso ni uses PROGRESS.md como expediente personal.

- ¿Qué evidencia tienes de otra pasada si la suma no cambió?
- ¿Por qué el botón no decide si se calcula el total de esta app?
- ¿Qué ocurriría si arriba del archivo hubiera una escritura sin protección?
- ¿Qué detuviste al cerrar la pestaña y qué al usar Ctrl+C?

Cierra cuando puedas explicar esas diferencias y reconstruir la variante con
su resultado correcto. El material y sus pruebas de autoría no acreditan tu práctica.

[← Lección 12.01](../../../curriculum/12_streamlit/01_first_app_execution/README.md) · [Módulo 12](../../../curriculum/12_streamlit/README.md) · [Siguiente: lección 12.02 →](../../../curriculum/12_streamlit/02_inputs_filters_presentation/README.md)

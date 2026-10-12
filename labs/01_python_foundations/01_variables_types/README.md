# Lab 01.01 — Interpretar y calcular con datos pequeños

## Relación y entrada

- Lección: [Variables, tipos y operaciones](../../../curriculum/01_python_foundations/01_variables_types/README.md).
- Entrada: su script de ejemplo y el entorno del nivel 0.
- Proyecto: no aplica todavía.

Reserva 25 a 40 minutos. Predice antes de ejecutar; consulta las soluciones después.

## Parte A — Distinguir valores y tipos

1. Lee las entradas y predice su tipo antes y después de convertirlas.
2. Ejecuta y comprueba la salida inicial.
3. Explica por qué `"3" + "2"` y `3 + 2` tienen resultados diferentes.

<details>
<summary>Ver solución de la parte A</summary>

Las entradas numéricas del script son texto (`str`), se convierten a enteros
(`int`) y producen `3 * 40 = 120` MXN. La comparación devuelve True.
Sumar textos concatena: `"3" + "2"` produce `"32"`; sumar enteros da 5.

</details>

## Parte B — Modificar y comprobar

1. Cambia producto a `carpeta`, unidades_texto a `"4"` y precio_unitario_texto a `"25"`.
2. Predice total y resultado de la comparación, guarda y ejecuta.
3. Cambia el precio a `"20"`, predice y comprueba de nuevo.

<details>
<summary>Ver solución de la parte B</summary>

Primero el total es 100 MXN y `100 >= 100` es True. Con precio de 20, el
total es 80 MXN y la comparación es False. Conserva las conversiones y el
cálculo; no reemplaces el resultado por un número fijo.

</details>

## Parte C — Comprender una entrada inválida

1. Sustituye unidades_texto por `"cuatro"` y ejecuta.
2. Identifica el tipo de error y la línea que intenta convertir.
3. Corrige a `"4"` y comprueba que el script vuelve a funcionar.

<details>
<summary>Ver solución de la parte C</summary>

`int("cuatro")` produce ValueError: el texto no tiene un formato numérico
entero válido. El error aparece antes del cálculo. Corregir la entrada permite
convertirla; más adelante aprenderemos a validar y gestionar estos errores.

</details>

## Evidencia y reflexión

- Conserva el script modificado y una nota con entradas, tipos y resultados.
- ¿Qué distingue `=` de `==`?
- Si reasignas unidades después de calcular, ¿se recalcula el importe por sí solo?
- ¿Convertir `"-4"` a entero demuestra que es una venta válida?
- Si usas Git, revisa el diff y registra únicamente los cambios de la práctica.

## Siguiente paso

Continúa con la [lección 02 — Listas y diccionarios](../../../curriculum/01_python_foundations/02_lists_dicts/README.md)
antes de realizar el lab 01.02.

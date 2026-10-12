# Lab 01.03 — Filtrar y resumir registros

## Relación y entrada

- Lección: [Condiciones y ciclos](../../../curriculum/01_python_foundations/03_conditions_loops/README.md).
- Entrada: su script de ventas y el entorno elegido.
- Proyecto: todavía no aplica.

Reserva 30 a 45 minutos. Predice antes de ejecutar y consulta las soluciones después.

## Parte A — Seguir el recorrido

1. Calcula manualmente las tres ventas y predice su categoría.
2. Predice el contador, total general, cantidad filtrada y total filtrado.
3. Ejecuta y compara. Explica qué instrucciones se ejecutan en cada vuelta.

<details>
<summary>Ver solución de la parte A</summary>

Cuaderno 80, alto; lapiz 50, medio; carpeta 35, bajo. Se revisan tres registros,
total general 165. Con umbral 50 entran cuaderno y lapiz: dos registros y 130 MXN.
El contador y total general se actualizan siempre; la selección solo cuando
cumple su condición. Las categorías son independientes del umbral del filtro.

</details>

## Parte B — Cambiar una regla

1. Cambia el umbral a 80 y predice antes de ejecutar.
2. Cámbialo a 100 y comprueba el caso sin coincidencias.
3. Restaura 50 y compara `>=` con `>` solo en la condición del filtro.
4. Restaura `>=` antes de la siguiente parte.

<details>
<summary>Ver solución de la parte B</summary>

Con umbral 80 se selecciona cuaderno: un registro y 80 MXN.
Con 100 no se selecciona ninguno: lista vacía y total 0.
Con `> 50`, lapiz queda fuera y solo cuaderno cumple. El total general siempre
sigue en 165 porque cambiar la selección no cambia las entradas.

</details>

## Parte C — Agregar otro registro

1. Agrega rotulador, 3 unidades y precio 30 a la lista inicial.
2. Con umbral 50 y `>=`, predice los cuatro indicadores.
3. Ejecuta y comprueba que el registro original no ganó el campo importe_mxn.

<details>
<summary>Ver solución de la parte C</summary>

Agrega este diccionario a la lista inicial, antes del ciclo:

```python
{"producto": "rotulador", "unidades": 3, "precio_unitario_mxn": 30},
```

Se revisan cuatro registros. Rotulador vale 90 y se clasifica alto.
Total general: 255; tres registros seleccionados; total seleccionado: 220.
Puedes comprobar después del ciclo:

```python
print("importe_mxn" in ventas[-1])         # False
print("importe_mxn" in seleccionadas[-1])  # True
```

La copia sencilla permite enriquecer la selección sin alterar las entradas.

</details>

## Parte D — Comprender un acumulador

1. Explica qué pasaría si `total_general_mxn = 0` estuviera dentro del ciclo.
2. Prueba en una copia del script o mueve temporalmente esa línea, conservando
   la sangría correcta. Observa el resultado y restaura el cálculo original.

<details>
<summary>Ver solución de la parte D</summary>

Reiniciar el total en cada vuelta descarta lo acumulado. Con el cuarto registro
de la parte C, terminaría en 90, no 255. La inicialización pertenece al bloque
anterior al ciclo y la suma al bloque que se repite.

</details>

## Evidencia y reflexión

- Conserva el script con cuatro registros y los indicadores comprobados.
- ¿Por qué importa el orden de if y elif?
- ¿Qué se repite siempre y qué depende del filtro?
- ¿Qué cambia al pasar de >= a > en un valor de frontera?
- ¿Qué significa total 0 cuando no hubo coincidencias?
- Si usas notebook, reinicia y ejecuta todo para descartar estado anterior.
- Si usas Git, revisa y registra el cambio de la práctica.

## Siguiente paso

Continúa con la [lección 04 — Funciones](../../../curriculum/01_python_foundations/04_functions/README.md)
antes de realizar el lab 01.04.

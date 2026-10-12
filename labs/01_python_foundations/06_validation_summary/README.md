# Lab 01.06 — Validar, conservar rechazos y conciliar un resumen

## Relación, entradas y resultado

- Lección: [06 — Validación y resumen](../../../curriculum/01_python_foundations/06_validation_summary/README.md).
- Entradas: ventas_revision.csv y validation_summary.py de la lección.
- Resultado: ventas válidas, rechazos con motivos y resumen por producto.
- Proyecto asociado: todavía no aplica.

Reserva 50 a 70 minutos, o dos sesiones. Intenta y predice antes de abrir las
soluciones. Utiliza el entorno habitual, sin instalar paquetes adicionales.

## Parte A — Decidir antes de ejecutar

1. Clasifica las ocho entradas con las reglas de la lección.
2. Predice cuántas serán válidas y rechazadas, unidades e importe válidos.
3. Ejecuta y revisa los tres CSV. Comprueba conteos y motivos por registro.
4. Explica por qué el precio cero no se rechaza y por qué 12.50 sí.

<details>
<summary>Ver solución de la parte A</summary>

Válidos: registros 1, 2, 3 y 7. Rechazados: 4 (producto vacío), 5 (unidades
negativas), 6 (cantidad no convertible), 8 (precio no entero). Hay 4 válidos y
4 rechazos: 8 = 4 + 4. Las unidades válidas suman 2 + 5 + 1 + 2 = 10;
el importe suma 80 + 50 + 35 + 0 = 165 MXN. Las reglas permiten precio cero
y requieren precios enteros, sin redondear decimales.

</details>

## Parte B — Reutilizar con otra entrada

1. Después de la parte A, copia la entrada en output/ventas_practica.csv.
2. En main, cambia entrada a esa copia y salida a output/practica para separar resultados.
3. Agrega otra venta de cuaderno: 3 unidades a 40 MXN.
4. Predice las cantidades, el total y el grupo cuaderno. Ejecuta y comprueba.
5. Repite: verifica que no se duplican registros y que la entrada original está intacta.

<details>
<summary>Ver solución de la parte B</summary>

```python
entrada = carpeta / "output" / "ventas_practica.csv"
salida = carpeta / "output" / "practica"
```

Agrega `cuaderno,3,40` a la copia. Tendrás 9 entradas, 5 válidos y 4 rechazos,
13 unidades válidas y 285 MXN. El grupo cuaderno tendrá 2 registros, 5 unidades
y 200 MXN. El resumen mantiene cuatro productos: agrupar no conserva necesariamente
el mismo número de filas que el detalle. Repetir reemplaza las salidas.

</details>

## Parte C — Cambiar una regla de forma explícita

1. Decide que este ejercicio ahora requiere un precio estrictamente positivo.
2. Cambia la condición del precio y el mensaje de rechazo. Documenta la regla.
3. Predice y comprueba resultados sobre la copia de la parte B.
4. Explica por qué un total igual no significa que nada cambió.

<details>
<summary>Ver solución de la parte C</summary>

```python
if precio is not None and precio <= 0:
    errores.append("precio debe ser mayor que 0")
```

Rotulador pasa a rechazados. Sobre la copia de la parte B: 9 entradas, 4 válidos,
5 rechazos, 11 unidades válidas y 285 MXN. El importe no cambia porque esa venta
valía cero, pero sí cambia la cantidad de válidos, unidades y productos del resumen.
Actualizar código sin documentar la decisión dejaría un contrato contradictorio.

</details>

## Parte D — Comprobar casos límite

Vuelve a la regla inicial que permite precio cero. Abre la consola Python desde
la carpeta de esta lección para importar las funciones. Es una comprobación
local; no necesitas instalar el script como paquete.

1. Valida una venta con producto compuesto solo de espacios, unidades 0 y precio -1.
2. Prueba separar y resumir una lista vacía.
3. Prueba una lista con una sola entrada inválida.
4. Comprueba que un resumen deliberadamente incorrecto produce un error.

<details>
<summary>Ver una solución de la parte D</summary>

```python
from validation_summary import validar_venta, separar_registros, resumir_ventas, comprobar_resultado

fila = {"producto": "   ", "unidades": "0", "precio_unitario_mxn": "-1"}
print(validar_venta(fila))  # Tres motivos; venta es None
print(separar_registros([]))  # Ambas listas vacías
print(resumir_ventas([]))  # Lista vacía
print(comprobar_resultado([], [], [], []))  # Unidades e importe cero

resultado = separar_registros([fila])
print(comprobar_resultado([fila], resultado["validos"], resultado["rechazados"], []))
# Una entrada, ningún válido, un rechazo; indicadores cero

venta = validar_venta({"producto": "cuaderno", "unidades": "2", "precio_unitario_mxn": "40"})["venta"]
comprobar_resultado([venta], [venta], [], [])
# ValueError: un resumen vacío no concilia con una venta válida
```

La función de control usa el número de entradas, no vuelve a validarlas. Los
tipos de campos se comprueban previamente. Importar este script no ejecuta main.

</details>

## Evidencia y reflexión

- Conserva el script modificado y una nota: reglas, casos, cantidades y totales.
- Explica la diferencia entre convertir un valor y validarlo.
- ¿Por qué atender ValueError no debe ocultar errores del resto del programa?
- ¿Por qué rechazados conserva los valores originales y todos los motivos?
- ¿Qué igualdad detecta una venta perdida? ¿Qué errores no detecta un total igual?
- Si usas Git, revisa el diff y registra código y reglas. Las salidas están ignoradas;
  no necesitas publicar en el repositorio compartido para completar la práctica.

## Siguiente paso

Consulta [02 — pandas](../../../curriculum/02_pandas/README.md) después de
comprobar el cierre de Python fundamental. Es planificación: las lecciones de
ese módulo todavía están por desarrollar.

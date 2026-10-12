# Lab 01.04 — Reutilizar transformaciones

## Relación y entrada

- Lección: [Funciones](../../../curriculum/01_python_foundations/04_functions/README.md).
- Entrada: su script de ejemplo y el entorno elegido.
- Proyecto: todavía no aplica.

Reserva 30 a 45 minutos. Predice antes de ejecutar y consulta las soluciones después.

## Parte A — Seguir las llamadas

1. Identifica parámetros, argumentos y return de cada transformación.
2. Ejecuta el script y comprueba los dos resúmenes.
3. Explica qué función calcula, cuál filtra y cuál presenta el resultado.

<details>
<summary>Ver solución de la parte A</summary>

calcular_importe multiplica dos entradas, seleccionar_ventas construye la
selección y resumir_ventas devuelve cantidad y total. main prepara y presenta.
El resumen general es 3/165 MXN y el seleccionado 2/130 MXN. Las transformaciones
devuelven datos; los print están en main.

</details>

## Parte B — Reutilizar con otras entradas

1. En main, cambia la llamada a seleccionar_ventas para usar umbral 80.
2. Predice y comprueba sin modificar el código de las funciones.
3. Prueba umbral 100 y explica el resultado sin coincidencias.
4. Restaura 50 y agrega rotulador, 3 unidades y precio 30 a la colección.

<details>
<summary>Ver solución de la parte B</summary>

```python
seleccionadas = seleccionar_ventas(ventas, umbral_mxn=80)
```

Con 80: cantidad 1, total 80. Con 100: cantidad 0, total 0.
El general sigue siendo 3/165. Con la nueva venta y umbral 50, el general es
4/255 y la selección 3/220. Cambias argumentos y datos sin copiar la transformación.

</details>

## Parte C — Agregar una función pequeña

1. Define alcanza_umbral con importe y umbral, usando 50 como predeterminado.
2. Devuelve la comparación, sin imprimir dentro de esa función.
3. Desde main, comprueba 80 con el predeterminado y después con umbral 100.

<details>
<summary>Ver solución de la parte C</summary>

Antes de main:

```python
def alcanza_umbral(importe_mxn, umbral_mxn=50):
    """Indica si el importe alcanza el umbral elegido."""
    return importe_mxn >= umbral_mxn
```

Dentro de main:

```python
print(alcanza_umbral(80))                 # True
print(alcanza_umbral(80, umbral_mxn=100))  # False
```

El valor devuelto permite reutilizar la comparación en otra condición, además de mostrarla.

</details>

## Parte D — Comprobar el contrato

1. Desde main, imprime resumir_ventas([]) y predice el resultado.
2. Comprueba si la primera venta conserva solo sus campos originales después de filtrar.
3. Explica por qué no puedes consultar una variable local de resumir_ventas desde main.

<details>
<summary>Ver solución de la parte D</summary>

```python
print(resumir_ventas([]))             # {'cantidad': 0, 'total_mxn': 0}
print("importe_mxn" in ventas[0])     # False
```

La selección usa copias de registros sencillos. total_mxn es local a la función:
para usarlo desde main recibes el diccionario retornado y consultas su campo.

</details>

## Evidencia y reflexión

- Conserva el script con la función nueva y los casos comprobados.
- ¿Qué cambia entre definir una función y llamarla?
- ¿Por qué un print dentro de una función no sustituye return?
- ¿Cambiar argumentos requiere cambiar siempre la definición?
- ¿Pasar una lista como argumento la copia automáticamente?
- Si usas Git, revisa el diff y registra tu modificación.

## Siguiente paso

Continúa con la [lección 05 — Archivos CSV](../../../curriculum/01_python_foundations/05_csv_files/README.md)
antes de realizar su lab.

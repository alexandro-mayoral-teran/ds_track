# Lab 02.02 — Inspeccionar un CSV y comprobar su copia

## Relación, entrada y resultado

- Lección: [Leer, inspeccionar y exportar](../../../curriculum/02_pandas/02_read_inspect_export/README.md).
- Entradas: cartera_demo.csv y read_inspect_export.py de la lección.
- Resultado: copia CSV comprobada y nota de inspección.
- Proyecto: todavía no aplica; el proyecto de limpieza está por implementar.

Reserva 40 a 60 minutos. Utiliza el entorno con pandas preparado antes;
no instales otro paquete. Predice e intenta antes de abrir las soluciones.

## Parte A — Inspeccionar la fuente

1. Abre el CSV como texto. Identifica filas, columnas y el campo desconocido.
2. Predice shape, cuántas filas mostrará head y count de cada columna numérica.
3. Ejecuta el script y comprueba el ID 001, texto con coma/acento y ausencia en 005.
4. Revisa la copia: filas, columnas y saldos conocidos. Explica qué no valida equals.

<details>
<summary>Ver solución de la parte A</summary>

La tabla tiene seis filas y cinco columnas. head muestra las cinco primeras,
pero el sexto crédito existe y debe contarse. saldo_mxn tiene seis valores
presentes, incluidos los 0 MXN; dias_atraso tiene cinco. El saldo conocido suma
6000 MXN. El ID sigue siendo texto 001 y la ausencia de 005 no se convierte en cero.

La lectura equivalente demuestra que se conserva la tabla exportada, no que
el origen cumpla todas las reglas de una cartera. La salida no agrega el índice.

</details>

## Parte B — Cambiar la entrada sin alterar la original

1. Después de la parte A, copia cartera_demo.csv como output/cartera_practica.csv.
2. Agrega un crédito: ID 007, consumo, corte 2026-09-30, saldo 250 MXN y atraso 0.
3. En main, cambia entrada a esa copia y salida a output/cartera_practica_copia.csv.
4. Predice shape, cantidad de saldos presentes y su suma. Ejecuta y comprueba.
5. Repite y verifica que no se duplican filas y que cartera_demo.csv permanece intacto.

<details>
<summary>Ver solución de la parte B</summary>

En main conserva carpeta y sustituye las rutas:

```python
entrada = carpeta / "output" / "cartera_practica.csv"
salida = carpeta / "output" / "cartera_practica_copia.csv"
```

Agrega a la copia, sin otro encabezado:

```csv
007,consumo,2026-09-30,250,0
```

La tabla tiene forma (7, 5), siete saldos presentes y suma de saldos conocidos
6250 MXN. dias_atraso tiene seis valores presentes, pues 005 sigue desconocido.
head conserva su límite inicial de cinco filas. La exportación repetida reemplaza
la salida y mantiene siete filas.

</details>

## Parte C — Detectar una exportación que incluye el índice

Al final de main, después de comprobar la salida correcta:

1. Escribe otra salida de práctica omitiendo index=False.
2. Vuelve a leerla con pandas y compara columnas y forma con tabla.
3. Explica el origen de la columna adicional. Mantén la exportación principal correcta.

<details>
<summary>Ver una solución de la parte C</summary>

```python
con_indice = carpeta / "output" / "cartera_con_indice.csv"
tabla.to_csv(con_indice, encoding="utf-8")
otra = pd.read_csv(con_indice, dtype=TIPOS)
print(list(otra.columns))
print(otra.shape)  # (7, 6), después de la parte B
print(tabla.equals(otra))  # False
```

El índice inicial se exportó como un campo adicional, leído normalmente como
Unnamed: 0. No era otro atributo del crédito. La función leer_cartera rechazaría
esa lista de columnas. La corrección para nuestra salida es usar index=False;
no eliminar columnas indiscriminadamente de una fuente sin conocer su significado.

</details>

## Parte D — Explicar observaciones que pueden confundirse

1. ¿Por qué print(tabla.info()) añade None? Prueba y conserva solo tabla.info().
2. ¿Qué cambiaría en el conteo de dias_atraso si el dato desconocido de 005 fuera
   reemplazado por cero? No lo corrijas sin una regla.
3. ¿Se puede concluir que todos los registros son válidos porque describe se ejecutó?
4. ¿Qué ocurriría si entrada y salida apuntaran al mismo archivo en este script?

<details>
<summary>Ver respuestas orientativas de la parte D</summary>

info imprime el informe y devuelve None; print imprime también ese retorno.
Con la copia de siete filas, sustituir el desconocido por cero aumentaría count
de dias_atraso de seis a siete, cambiando las estadísticas y el significado del dato.
No es una reparación neutra. describe resume; no demuestra unicidad o reglas de negocio.

guardar_y_comprobar compara las rutas resueltas y detiene la operación con
ValueError antes de escribir si coinciden. Mantener la fuente separada permite
revisar y repetir el ejercicio sin perder la entrada.

</details>

## Evidencia y reflexión

- Conserva el script modificado y una nota: fuente, columnas, tipos, valores
  presentes, suma conocida y cómo se comprobó la copia.
- Explica por qué se utiliza string para identificadores y Int64 para atraso.
- ¿Por qué contar lo visible en head no es contar registros del archivo?
- ¿Qué diferencia hay entre un campo desconocido y cero?
- ¿Qué datos de la fuente debes confirmar antes de elegir sep y encoding?
- Si usas Git, revisa y registra código y nota; output está ignorado. No necesitas
  publicar en el repositorio compartido para completar el lab.

## Siguiente paso

Continúa con la [lección 03 — Seleccionar, filtrar y ordenar](../../../curriculum/02_pandas/03_select_filter_sort/README.md)
antes de realizar su lab.

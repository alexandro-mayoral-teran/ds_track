# Lab 02.01 — Interpretar una tabla y sus etiquetas

## Relación, entrada y resultado

- Lección: [Series y DataFrame](../../../curriculum/02_pandas/01_series_dataframe/README.md).
- Entrada: series_dataframe.py y sus tres ventas ficticias.
- Resultado: script modificado y una nota con formas, tipos y consultas comprobadas.
- Proyecto: todavía no aplica; el proyecto de limpieza está por implementar.

Reserva 35 a 50 minutos. Usa el entorno elegido con pandas instalado. Intenta
predecir antes de ejecutar y abrir soluciones. No necesitas escribir archivos CSV.

## Parte A — Leer la estructura

1. Predice filas, columnas, índice y total de unidades del ejemplo.
2. Ejecuta el script y compara.
3. Explica qué representa una fila y por qué el índice no es una cuarta columna.
4. Distingue los resultados de tabla["unidades"] y tabla[["unidades"]].

<details>
<summary>Ver solución de la parte A</summary>

Hay tres filas y tres columnas; shape es (3, 3). Las etiquetas iniciales son
0, 1 y 2. Las unidades suman 8. Una fila es una venta, y el índice etiqueta
esa fila por separado de las columnas de datos. La primera selección devuelve
Series, forma (3,); la segunda DataFrame, forma (3, 1).

</details>

## Parte B — Agregar un registro

1. Agrega rotulador, 3 unidades y precio 30 a registros dentro de main.
2. Agrega venta_d a la lista de etiquetas del ejemplo.
3. Predice nueva forma, índice inicial y suma de unidades. Ejecuta y comprueba.
4. Explica por qué cambiar el número de filas exige ajustar la lista de etiquetas.

<details>
<summary>Ver solución de la parte B</summary>

```python
{"producto": "rotulador", "unidades": 3, "precio_unitario_mxn": 30},
```

Agrega ese diccionario como cuarto elemento de registros. Cambia las etiquetas:

```python
etiquetada.index = ["venta_a", "venta_b", "venta_c", "venta_d"]
```

La forma será (4, 3), el índice inicial [0, 1, 2, 3] y el total 11 unidades.
Una Series de unidades tendrá forma (4,); su versión DataFrame, (4, 1).
El índice personalizado necesita una etiqueta por fila; con tres etiquetas
para cuatro filas pandas produce ValueError.

</details>

## Parte C — Consultar por dos caminos

1. Sobre etiquetada, encuentra las unidades del lápiz por etiqueta y por posición.
2. Conserva una vista con producto y unidades; predice su forma.
3. Predice qué ocurre al intentar loc[1, "producto"] con las etiquetas de texto.
4. Prueba esa consulta incorrecta al final del script, observa el error y corrígela.

<details>
<summary>Ver solución de la parte C</summary>

```python
print(etiquetada.loc["venta_b", "unidades"])  # 5
print(etiquetada.iloc[1, 1])                  # 5
vista = tabla[["producto", "unidades"]]
print(vista.shape)  # (4, 2), después de la parte B
```

loc[1, "producto"] busca la etiqueta numérica 1, que no existe en ese índice
de texto: produce KeyError. No pide la segunda fila; para eso utiliza iloc.
La selección de columnas mantiene las filas y cambia el número de columnas.

</details>

## Parte D — Una tabla vacía también tiene estructura

Al final de main, sin reemplazar la tabla de ventas:

1. Crea otra tabla con crear_tabla([]).
2. Predice shape y columnas.
3. Explica por qué iloc[0, 0] no puede devolver un dato.

<details>
<summary>Ver solución de la parte D</summary>

```python
vacia = crear_tabla([])
print(vacia.shape)          # (0, 3)
print(list(vacia.columns))  # Las tres columnas previstas
```

La función declara las columnas aunque no haya registros. No existe una primera
fila: iloc[0, 0] produce IndexError. Conservar las columnas no garantiza los
tipos de una tabla vacía ni crea registros ficticios.

</details>

## Evidencia y reflexión

- Conserva código y una nota con versión de pandas, formas y resultados.
- ¿En qué se parecen una lista de diccionarios y un DataFrame? ¿Qué cambia?
- ¿Por qué shape no lleva paréntesis y sum sí?
- ¿Una columna con dtype object demuestra que todos sus valores son texto?
- ¿El índice representa necesariamente un identificador único de venta?
- Si usas Git, revisa los cambios y registra la práctica como aprendiste antes.
  No necesitas publicar en el repositorio compartido para completar el lab.

## Siguiente paso

Continúa con la [lección 02 — Leer, inspeccionar y exportar](../../../curriculum/02_pandas/02_read_inspect_export/README.md)
antes de realizar su lab.

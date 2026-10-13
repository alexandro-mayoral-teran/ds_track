# Lab 03.05 — Relacionar tablas con joins

## Entrada, actividad y resultado

Lee la [lección 03.05](../../../curriculum/03_sql_databases/05_joins/README.md)
y completa 03.01–03.04 con sus labs. Recupera los
[conteos y agregados de 03.04](../../../curriculum/03_sql_databases/04_aggregations/README.md).
Recibes la base ficticia de 03.01, sus CSV y el ejemplo
[joins.py](../../../curriculum/03_sql_databases/05_joins/joins.py).
Produce consultas, una tabla de comprobaciones y una explicación de la unidad
del resultado. Conserva base y fuentes; las consultas sobre archivos se hacen
en solo lectura. Los casos nuevos se construyen exclusivamente en memoria.

Puedes copiar el script a tu carpeta de práctica, adaptar SOURCE a la carpeta
de 03.01 y usar --database para señalar una base existente compatible.
Para modificar una consulta, conserva SQL y parámetros separados.
Ejecuta el recorrido de tu shell y entorno indicado en la lección.
Una sesión puede cubrir solo A y B; C–E completan el criterio esencial.

## A — Definir y construir la unión

1. Anota la pregunta, tabla de partida y clave del resultado para añadir región
   a cada observación de octubre.
2. Relaciona cortes → creditos → clientes con INNER JOIN.
3. Selecciona ID, fecha, saldo, cliente, segmento y región; ordena por ID.
4. Compara las columnas originales con la consulta de cortes sin join.

<details>
<summary>Ver solución razonada de A</summary>

La unidad sigue siendo crédito/fecha; clave: id_credito + fecha_corte.
Las relaciones muchos a uno permiten añadir atributos sin aumentar filas.

```sql
SELECT o.id_credito, o.fecha_corte, o.saldo_mxn,
       c.id_cliente, c.segmento, p.region
FROM cortes AS o
INNER JOIN creditos AS c ON c.id_credito = o.id_credito
INNER JOIN clientes AS p ON p.id_cliente = c.id_cliente
WHERE o.fecha_corte = ?
ORDER BY o.id_credito;
```

Usa ('2026-10-31',) como parámetros en Python. Se esperan 24 filas; 001
corresponde a C001, consumo, norte, con saldo 1300. Compara todas las primeras
tres columnas con la selección original, no solo la primera fila.
La función reconcile del ejemplo también contrasta los atributos con los CSV.

</details>

## B — Conciliar y comprobar vacíos

1. Obtén cantidad de filas, saldos conocidos y suma conocida antes y después.
2. Comprueba que ninguna clave crédito/fecha se repita.
3. Repite con septiembre y una fecha inexistente.
4. Explica por qué la suma conocida no representa todos los saldos.

<details>
<summary>Ver solución razonada de B</summary>

| Fecha | Filas | Saldos conocidos | Suma conocida MXN |
| --- | --- | --- | --- |
| 2026-09-30 | 24 | 21 | 47 200 |
| 2026-10-31 | 24 | 21 | 46 700 |
| 2099-01-31 | 0 | 0 | NULL |

Para SQL, COUNT(*) cuenta filas, COUNT(o.saldo_mxn) valores conocidos y
SUM(o.saldo_mxn) su suma. Reemplaza las columnas del SELECT de A por esos
agregados y quita ORDER BY; en la consulta original usa saldo_mxn sin alias
de tabla. Ambos resultados deben coincidir.
En Python, verifica la unicidad:

```python
claves = [(fila[0], fila[1]) for fila in filas]
assert len(claves) == len(set(claves))
```

La consulta de detalle de la fecha inexistente devuelve []; la agregada sin
GROUP BY devuelve [(0, 0, None)]. No hay registros para esa fecha; no inventamos
una observación de saldo cero. Para octubre hay tres saldos desconocidos,
aunque exista una fila para cada crédito.

</details>

## C — Conservar clientes sin crédito

1. Consulta clientes → créditos con LEFT JOIN sobre la muestra original.
2. Predice cuántas filas aparecerán y explica por qué no son 16.
3. En una conexión nueva en memoria, crea el caso mínimo siguiente:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.execute("CREATE TABLE clientes (id_cliente TEXT PRIMARY KEY NOT NULL)")
conexion.execute("CREATE TABLE creditos (id_credito TEXT PRIMARY KEY NOT NULL, id_cliente TEXT NOT NULL)")
conexion.executemany("INSERT INTO clientes VALUES (?)", [("X",), ("Y",)])
conexion.executemany("INSERT INTO creditos VALUES (?, ?)", [("K1", "X"), ("K2", "X")])
```

Este esquema mínimo aísla la cardinalidad; no es el esquema completo de 03.03.
4. Compara INNER y LEFT. Detecta clientes sin crédito usando la clave derecha.
5. Agrupa por cliente y compara COUNT(*) con COUNT(c.id_credito).
   Cierra la conexión en finally, como en la lección.

<details>
<summary>Ver solución razonada de C</summary>

La muestra original tiene 24 filas: C001–C008 con dos créditos, C009–C016 con uno;
no hay clientes sin crédito. En el caso temporal:

```sql
SELECT p.id_cliente, c.id_credito
FROM clientes AS p
LEFT JOIN creditos AS c ON c.id_cliente = p.id_cliente
ORDER BY p.id_cliente, c.id_credito;
```

LEFT devuelve ('X','K1'), ('X','K2'), ('Y',NULL); INNER devuelve solo las dos
primeras parejas. `WHERE c.id_credito IS NULL` identifica Y. En el agregado,
X tiene COUNT(*) = 2 y COUNT(c.id_credito) = 2; Y tiene 1 y 0. La fila
conservada para Y no representa un crédito. Aquí el aumento de filas es legítimo.

</details>

## D — ON, WHERE y dos formas de ausencia

1. Lee y ejecuta demonstrate_missing del script; predice las dos salidas.
2. Explica por separado A, B y C del caso temporal de la lección.
3. Consulta los créditos sin observación de octubre usando filtro de fecha
   en ON y `WHERE o.id_credito IS NULL`.
4. Explica qué resultado obtendrías si filtras `o.saldo_mxn IS NULL` en su lugar.

<details>
<summary>Ver solución razonada de D</summary>

Con la fecha en ON se conservan A, B y C; en WHERE solo A y B. Para detectar
ausencia de observación:

```sql
SELECT c.id_credito
FROM creditos AS c
LEFT JOIN cortes AS o
  ON o.id_credito = c.id_credito AND o.fecha_corte = ?
WHERE o.id_credito IS NULL
ORDER BY c.id_credito;
```

El parámetro de octubre produce C. Filtrar saldo NULL produce B y C: B sí tiene
observación, con saldo desconocido. A tiene saldo cero conocido. No confundas
esos estados ni cambies la fuente para hacer que todas las uniones coincidan.
Añadir `OR o.fecha_corte IS NULL` al filtro de fecha en WHERE no rescata C,
porque C sí encontró una fila de septiembre y no tiene una fila derecha NULL.

</details>

## E — Detectar y corregir multiplicación

1. Ejecuta BAD_PAIR del script y compara filas/suma con octubre antes de unir.
2. Inspecciona las dos parejas de 001 y explica por qué el saldo aparece dos veces.
3. Añade la fecha a la condición de igualdad y vuelve a comprobar.
4. Explica por qué DISTINCT y SUM(DISTINCT saldo) no son reglas de reparación.

<details>
<summary>Ver solución razonada de E</summary>

La unión incompleta produce 48 filas y suma conocida 93 400 MXN; la correcta
conserva 24 y 46 700. 001 de octubre coincide con 001 de septiembre y octubre,
repitiendo 1300. Usa
`ON b.id_credito = a.id_credito AND b.fecha_corte = a.fecha_corte`.
La clave completa conserva una pareja por observación; recuperar la misma fila
solo ilustra la comprobación, no añade atributos nuevos.

DISTINCT actúa sobre la proyección elegida y puede esconder multiplicidad;
SUM(DISTINCT saldo) suma una vez cada importe distinto, aunque dos créditos
legítimos compartan saldo. La solución depende de la pregunta y la unidad,
no de eliminar filas hasta que el total parezca razonable.

</details>

## Extensión — Parámetros y comparación con pandas

Consulta créditos con la fecha 2099-01-31 en ON y luego en WHERE. En la muestra
original, ON conserva 24 créditos sin observación; WHERE devuelve cero filas.
Explica la diferencia con una consulta de cortes de esa fecha, también vacía.
Agrupa la unión correcta de octubre por región y concilia observaciones,
clientes distintos, saldos conocidos y suma con el total del corte. Explica
por qué COUNT(*) no cuenta clientes. Revisa la advertencia de pandas.merge sobre claves nulas antes de comparar
resultados entre herramientas; esa comparación completa se desarrolla en 03.09.

<details>
<summary>Ver comprobación del resumen regional</summary>

| Región | Observaciones | Clientes distintos | Saldos conocidos | Suma conocida MXN |
| --- | --- | --- | --- | --- |
| centro | 8 | 5 | 7 | 14 400 |
| norte | 9 | 6 | 8 | 18 000 |
| sur | 7 | 5 | 6 | 14 300 |

Los grupos concilian con 24 observaciones, 16 clientes, 21 saldos conocidos y
46 700 MXN conocidos. Aquí las regiones son excluyentes por cliente, por lo que
los conteos de clientes distintos son aditivos. Eso no se garantiza para
cualquier clasificación. COUNT(*) conserva la unidad observación;
COUNT(DISTINCT c.id_cliente) mide otra unidad.

</details>

## Evidencia, reflexión y siguiente paso

Conserva SQL, parámetros y tu tabla de comprobaciones; identifica para cada
consulta su unidad, claves, coincidencias ausentes y suma conocida con cobertura.
Repite el script: las filas ordenadas deben coincidir y la base quedar intacta.
Explica: ¿cuándo es correcto aumentar filas? ¿Por qué una clave foránea no obliga
a un cliente a tener créditos? ¿Cómo distinguirías una pareja ausente de un
saldo desconocido? ¿Por qué un total coincidente no basta para validar una unión?

No hay checkpoint de proyecto implementado. Continúa con el
[plan de 03.06 — Subconsultas y CTE](../../../curriculum/03_sql_databases/README.md#06-subconsultas-y-cte),
todavía sin lección ni siguiente lab disponible.

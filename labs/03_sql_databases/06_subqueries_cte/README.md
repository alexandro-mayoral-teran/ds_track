# Lab 03.06 — Subconsultas y CTE

## Entrada, actividad y resultado

Lee la [lección 03.06](../../../curriculum/03_sql_databases/06_subqueries_cte/README.md)
y completa 03.04–03.05 con sus prerrequisitos. Recibes la base ficticia de 03.01,
sus CSV y [queries.py](../../../curriculum/03_sql_databases/06_subqueries_cte/queries.py).
Produce consultas equivalentes, una tabla de comprobaciones por etapa y una
explicación de su unidad y tratamiento de ausencias. Conserva todas las entradas.
Los archivos se consultan en solo lectura; los casos adicionales viven en memoria.

Ejecuta el recorrido de tu shell y gestor de la lección. Puedes adaptar el script
con otro nombre en su misma carpeta, conservando el original. Si lo mueves,
adapta SOURCE y utiliza --database para señalar una copia existente compatible.
Las constantes SQL están al principio; los filtros usan :fecha y :umbral con
un diccionario de valores. No interpolas valores en el texto.

Sesiones sugeridas: A–B para referencias/presencia; C–D para ausencia y tablas
derivadas; E–F para consultas por pasos y comprobación. La extensión G no bloquea
el siguiente tema. Intenta predecir resultados antes de abrir cada solución.

## A — Una referencia escalar sobre el mismo corte

1. Calcula el promedio conocido de octubre con una consulta independiente.
2. Usa una subconsulta escalar para obtener ID y saldo de quienes lo superan.
3. Reescribe la consulta con las CTE corte y referencia del ejemplo.
4. Compara filas completas ordenadas, no solo la cantidad.
5. Explica qué pasa cuando no hay saldos conocidos para calcular AVG.

<details>
<summary>Ver solución razonada de A</summary>

ABOVE_AVERAGE y ABOVE_AVERAGE_CTE implementan ambas versiones en el script.
Su parámetro fecha es octubre. La referencia es 46 700 / 21 ≈ 2 223.8095;
se obtienen 011–021, once filas con saldos de 2 300 a 3 300.
La fecha interior y exterior debe coincidir. No compares contra 2 223.81
redondeado si quieres conservar la definición exacta del filtro.

En la CTE referencia, AVG sin GROUP BY devuelve una fila incluso si corte
está vacío. CROSS JOIN con esa única fila aporta la referencia sin multiplicar
el detalle. El filtro sigue descartando saldos NULL y comparaciones con promedio
NULL. Una referencia agrupada por segmento requeriría otra clave de unión.

En Python, si ambos resultados están ordenados por ID:

```python
parametros = {"fecha": "2026-10-31"}
escalar = conexion.execute(ABOVE_AVERAGE, parametros).fetchall()
por_cte = conexion.execute(ABOVE_AVERAGE_CTE, parametros).fetchall()
assert escalar == por_cte
```

La igualdad compara tuplas y multiplicidad. Para reales obtenidos mediante
agregación en distintas implementaciones, usa la tolerancia explicada en
check_rows; aquí los saldos recuperados son los mismos enteros de la fuente.

</details>

## B — Clientes con presencia confirmada

1. Escribe la pregunta «clientes con al menos un crédito que cumpla el umbral».
2. Ejecuta las versiones IN, EXISTS y join de la lección con octubre y 30.
3. Identifica la correlación en EXISTS. Explica qué ocurriría al quitarla.
4. Quita DISTINCT de la versión join y compara filas e IDs distintos.
5. Explica por qué SELECT 1 no cuenta créditos.

<details>
<summary>Ver solución razonada de B</summary>

Las constantes CLIENTS_IN, CLIENTS_EXISTS y CLIENTS_JOIN producen:
C002, C004, C005, C007, C010, C011 y C015. Son siete clientes para nueve
créditos con atraso confirmado. El join sin DISTINCT produce nueve filas:
C002 y C007 aparecen dos veces porque tienen dos créditos que cumplen.
IN y EXISTS no repiten una fila exterior por cada pareja encontrada.

La correlación es `c.id_cliente = p.id_cliente`. Si se elimina, existe alguna
coincidencia en toda la cartera y pasan los 16 clientes, aunque no sea su crédito.
SELECT 1 entrega una constante por pareja; EXISTS solo pregunta si hay fila.
Puede haber una fila con saldo NULL, como el crédito 023, y la existencia
seguir siendo verdadera para su cliente si el atraso cumple la regla.

Aquí DISTINCT en la versión join expresa deliberadamente «clientes distintos»;
no corrige una condición incompleta ni se usa antes de sumar saldos. Si necesitas
el detalle de los créditos, conserva los nueve registros y cambia la unidad
de tu respuesta de cliente a crédito/corte.

</details>

## C — Ausencia y la trampa de NOT IN

1. Ejecuta CLIENTS_NOT_EXISTS sobre octubre: explica qué significa su resultado.
2. En una conexión nueva en memoria, prepara este caso mínimo:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.execute("CREATE TABLE candidatos (id TEXT PRIMARY KEY NOT NULL)")
conexion.execute("CREATE TABLE seleccion (id TEXT)")
conexion.executemany("INSERT INTO candidatos VALUES (?)", [("A",), ("B",), ("C",)])
conexion.executemany("INSERT INTO seleccion VALUES (?)", [("A",), (None,)])
```

3. Consulta los candidatos sin coincidencia con NOT IN y NOT EXISTS.
4. Comprueba `EXISTS(SELECT id FROM seleccion WHERE id IS NULL)`.
5. Explica la diferencia entre desconocido y falso. Cierra la conexión temporal
   en finally, como en el ejemplo.

<details>
<summary>Ver solución razonada de C</summary>

En octubre NOT EXISTS devuelve C001, C003, C006, C008, C009, C012, C013,
C014 y C016. Significa «sin coincidencia confirmada de esa regla», no «todos
sus atrasos conocidos y menores de 30». El complemento conserva desconocidos.

En el caso A/B/C:

```sql
SELECT id FROM candidatos
WHERE id NOT IN (SELECT id FROM seleccion)
ORDER BY id;
```

Devuelve []. A sí pertenece; B y C producen desconocido por el NULL interior.

```sql
SELECT c.id FROM candidatos AS c
WHERE NOT EXISTS (SELECT 1 FROM seleccion AS s WHERE s.id = c.id)
ORDER BY c.id;
```

Devuelve [('B',), ('C',)]. No hay una igualdad verdadera para esos candidatos.
La consulta siguiente da [(1,)]: hay una fila aunque el valor proyectado sea NULL.

```sql
SELECT EXISTS(SELECT id FROM seleccion WHERE id IS NULL) AS hay_fila;
```

WHERE conserva solo condiciones verdaderas; falso y desconocido se descartan,
pero tienen significados distintos. Si se garantiza que ambos lados son no
nulos, la comparación de pertenencia puede tener otro contrato; no generalices
la equivalencia desde la muestra sin comprobarlo.

</details>

## D — Leer un resumen como tabla

1. Ejecuta la tabla derivada de la sección 6 de la lección.
2. Reescríbela con una CTE resumen y comprueba que las cinco columnas coincidan.
3. Explica qué columnas quedaron disponibles para la consulta exterior.
4. Intenta consultar resumen en una sentencia separada y explica el error.

<details>
<summary>Ver solución razonada de D</summary>

Ambas versiones entregan cuatro filas: comercio (5, 5, 2, 40 %), consumo
(10, 9, 4, ≈ 44.44 %), educacion (3, 2, 1, 50 %) y servicios
(6, 5, 2, 40 %), con columnas registros, atrasos_conocidos, confirmados y tasa.
El resumen ya no conserva un id_credito por fila: cada fila representa segmento.

WITH nombra resumen solo para su propia sentencia. Un SELECT posterior da
no such table si no existe otra tabla real con ese nombre. No crees una tabla
para evitar el error: conserva WITH junto a su SELECT final.
La CTE permite calcular tasas sobre nombres ya definidos sin repetir agregados.

</details>

## E — Comprobar una cadena de CTE

1. Ejecuta REPORT_CTE con octubre y umbral 30.
2. Inspecciona corte, detalle y resumen cambiando el SELECT final y conservando
   el WITH correspondiente. Anota la unidad de cada etapa.
3. Concilia las observaciones originales y saldos conocidos antes de agrupar.
4. Compara el reporte con REPORT_DERIVED y con los cálculos Python del script.
5. Explica qué significa cada NULL de educacion.

<details>
<summary>Ver solución razonada de E</summary>

Etapas: corte 24 observaciones; detalle las mismas 24, con segmento; resumen
cuatro filas; salida final cuatro segmentos. La clave del detalle para esta
fecha es id_credito; si incluyeras varias fechas, necesitarías crédito/fecha.
Compara todos los campos conservados, no solo la cantidad.

| Segmento | Registros | Saldos conocidos | Suma conocida MXN | Atrasos conocidos | Confirmados | Tasa entre conocidos |
| --- | --- | --- | --- | --- | --- | --- |
| comercio | 5 | 5 | 15 500 | 5 | 2 | 40 % |
| consumo | 10 | 10 | 15 900 | 9 | 4 | ≈ 44.44 % |
| educacion | 3 | 0 | NULL | 2 | 1 | 50 % |
| servicios | 6 | 6 | 15 300 | 5 | 2 | 40 % |

Los conteos suman 24 registros, 21 saldos conocidos, 21 atrasos conocidos y
9 confirmados. La suma conocida es 46 700 MXN. La tasa conjunta se obtiene
de 9/21, no promediando porcentajes. educacion tiene saldo desconocido en sus
tres filas, pero dos atrasos conocidos: las ausencias dependen de la columna.

El script compara ambas versiones con expected_report, calculado desde los
CSV. Conserva orden y multiplicidad; convertir resultados a set podría ocultar
duplicados. Comprueba importes enteros exactamente y tasas reales con tolerancia.

</details>

## F — Vacíos, fechas y filtros coherentes

1. Repite las consultas con septiembre y con 2099-01-31.
2. Cambia el umbral de octubre a 100 en todas las versiones de presencia/reporte.
3. Explica por qué el filtro sobre promedio no cambia al modificar el umbral.
4. Comprueba que repetir no modifica las entradas.

<details>
<summary>Ver solución razonada de F</summary>

Septiembre tiene once saldos sobre su promedio conocido: 013–023. Los clientes
con atraso confirmado son C002, C005, C007, C010 y C011. El reporte tiene cuatro
grupos; educacion tiene tres registros, cero atrasos conocidos y tasa NULL.

Una fecha inexistente produce cero créditos sobre promedio, cero clientes
con coincidencia y cero grupos. NOT EXISTS devuelve los 16 clientes: ninguno
tiene evidencia de coincidencia en esa fecha. La referencia AVG sin GROUP BY
devuelve una fila con valor NULL, no cero filas.

En octubre, umbral 100 produce cero confirmados pero mantiene los cuatro
segmentos, cobertura y sumas. Como cada segmento tiene atraso conocido en ese
corte, la tasa es 0 %; no cambia los desconocidos ni garantiza sus valores.
El filtro de saldo usa una fecha y promedio de saldo, no la regla de atraso.

</details>

## G — Extensión: comparar contra el promedio de su segmento

Pregunta diferente de A: ¿qué saldos de octubre superan el promedio conocido
del segmento al que pertenece el crédito? Define las CTE detalle y promedios;
une por segmento y comprueba una sola referencia por observación.

<details>
<summary>Ver solución razonada de la extensión</summary>

```sql
WITH detalle AS (
    SELECT o.id_credito, o.saldo_mxn, c.segmento
    FROM cortes AS o
    INNER JOIN creditos AS c ON c.id_credito = o.id_credito
    WHERE o.fecha_corte = '2026-10-31'
), promedios AS (
    SELECT segmento, AVG(saldo_mxn) AS promedio_conocido
    FROM detalle
    GROUP BY segmento
)
SELECT d.id_credito, d.segmento, d.saldo_mxn, p.promedio_conocido
FROM detalle AS d
INNER JOIN promedios AS p ON p.segmento = d.segmento
WHERE d.saldo_mxn > p.promedio_conocido
ORDER BY d.id_credito;
```

Promedios: consumo 1 590, servicios 2 550 y comercio 3 100 MXN; educacion NULL.
Pasan 005–010, 014–016 y 020–021: once créditos, pero no son los mismos once
de A. Coincidir en cantidad no demuestra igualdad de preguntas ni resultados.
019, con 3 100, iguala el promedio de comercio y no lo supera.
Cada grupo produce una sola referencia por segmento; el join no debe multiplicar
observaciones. educacion no aporta ningún saldo conocido para su promedio.

</details>

## Evidencia, reflexión y siguiente paso

Conserva SQL, parámetros, resultados ordenados y las comprobaciones de cada
etapa. Tu nota debe identificar qué devuelve cada subconsulta, dónde hay
correlación, por qué conserva su unidad y cómo verificaste NULL y vacíos.
Explica: ¿cuándo prefieres EXISTS a un join? ¿Por qué una CTE no es una tabla
guardada? ¿Cómo puede una coincidencia en conteos esconder resultados distintos?
¿Qué dato necesitarías para clasificar a alguien sin atraso conocido?

Registra evidencia y dudas en PROGRESS.md; ejecutar el ejemplo no acredita por
sí solo el criterio de aprendizaje. No hay checkpoint de proyecto implementado.
Continúa con el [03.07 — Ventanas para comparar registros](../../../curriculum/03_sql_databases/07_windows/README.md).

# Lab 03.02 — Primeras consultas

## Entrada, actividad y resultado

Lee la [lección 03.02](../../../curriculum/03_sql_databases/02_first_queries/README.md)
y completa 03.01. Recibes su base ficticia: clientes, creditos y cortes. Conserva
las entradas y consulta en solo lectura. Produce un pequeño script con tus
consultas y una nota con preguntas, resultados y explicación. Puedes copiar
[first_queries.py](../../../curriculum/03_sql_databases/02_first_queries/first_queries.py)
para adaptarlo en tu carpeta de práctica; conserva el original.
Si mueves el script, indica la base mediante --database porque su ruta predeterminada
se calcula desde la ubicación del archivo. No necesitas exportar ni modificar la base.

Ejecuta los comandos de la lección con tu entorno elegido. Guarda SQL y parámetros
por separado y utiliza try/finally para cerrar la conexión. Trabaja por partes;
una sesión puede cubrir solo A y B.

## A — Seleccionar y ordenar

1. Escribe con tus palabras qué representa una fila de cortes.
2. Recupera id_credito como credito y saldo_mxn de octubre.
3. Ordena por id_credito y limita a las primeras tres filas.
4. Explica qué cambia AS y qué requisito se pierde si quitas ORDER BY.

<details>
<summary>Ver solución razonada de A</summary>

```sql
SELECT id_credito AS credito, saldo_mxn
FROM cortes
WHERE fecha_corte = '2026-10-31'
ORDER BY id_credito
LIMIT 3;
```

Resultado: ('001', 1300), ('002', 1400), ('003', 1500). Una fila representa una
observación crédito/fecha. El alias cambia el encabezado del resultado; la base
conserva id_credito. Sin ORDER BY no se garantiza cuáles son las primeras tres.

</details>

## B — Condiciones, empates y frontera

1. Selecciona ID, saldo y atraso de octubre con al menos 30 días de atraso.
2. Ordena atraso descendente y luego ID ascendente.
3. Antes de ejecutar, identifica qué ocurre con 30 exactos y con NULL.
4. Cambia >= por > y compara los identificadores, sin atribuir a NULL un atraso cero.

<details>
<summary>Ver solución razonada de B</summary>

```sql
SELECT id_credito, saldo_mxn, dias_atraso
FROM cortes
WHERE fecha_corte = '2026-10-31' AND dias_atraso >= 30
ORDER BY dias_atraso DESC, id_credito;
```

Nueve filas: 004, 009, 014, 019 tienen 40 días; 003, 008, 013, 018, 023 tienen 30.
La segunda columna de orden desempata. > 30 devuelve las primeras cuatro;
>= incluye la frontera. Las comparaciones con NULL no son verdaderas y WHERE
excluye esos registros. El saldo cero de 004 no impide que tenga atraso conocido.

</details>

## C — Ausente, cero y conocido

1. Recupera IDs sin saldo de octubre usando IS NULL.
2. Recupera por separado los de saldo cero y los de saldo conocido (IS NOT NULL).
3. Comprueba en Python las cantidades y que los grupos ausente/conocido no se
   superpongan; entre ambos deben cubrir los 24 IDs de octubre.
4. Compara `saldo_mxn = NULL` con IS NULL y explica la diferencia.

<details>
<summary>Ver solución razonada de C</summary>

```sql
SELECT id_credito FROM cortes
WHERE fecha_corte = '2026-10-31' AND saldo_mxn IS NULL ORDER BY id_credito;
```

Ausentes: 022, 023, 024 (3); cero: 004 (1); conocidos: 21. Cambia solo la segunda
condición por `saldo_mxn = 0` y por `saldo_mxn IS NOT NULL` para las otras consultas.
El cero está dentro de conocidos. `= NULL` devuelve cero filas porque la comparación
produce desconocido. Comprobar `len(filas)` no requiere aún COUNT de SQL.

Con listas de tuplas de una columna, comprueba los grupos en Python:

```python
assert len(ausentes) == 3 and len(conocidos) == 21
assert set(ausentes).isdisjoint(conocidos)
assert set(ausentes) | set(conocidos) == set(octubre)
```

octubre es el resultado de seleccionar todos sus IDs sin condición de saldo.
Estas comprobaciones aplican a la muestra original, no a cualquier cartera real.

</details>

## D — Paréntesis y DISTINCT

1. Recupera octubre con atraso cero o al menos 30 días. Usa paréntesis.
2. Compara con la consulta sin paréntesis presentada en la lección. Selecciona
   también fecha_corte para detectar qué filas no pertenecen a octubre.
3. Recupera fechas distintas; después pares distintos de ID/fecha.
4. Explica por qué no son el mismo resultado ni la misma unidad.

<details>
<summary>Ver solución razonada de D</summary>

```sql
SELECT id_credito, fecha_corte, dias_atraso FROM cortes
WHERE fecha_corte = '2026-10-31'
  AND (dias_atraso = 0 OR dias_atraso >= 30)
ORDER BY id_credito;
```

Son 13 filas: 003, 004, 005, 008, 009, 010, 013, 014, 015, 018, 019, 020, 023.
Sin paréntesis se añaden seis atrasos de septiembre: 004, 009, 013, 014, 018, 019,
porque AND se evalúa antes de OR. Las fechas distintas son dos; los pares distintos,
48. DISTINCT compara todas las columnas seleccionadas; no conserva solo el ID.

```sql
SELECT DISTINCT fecha_corte FROM cortes ORDER BY fecha_corte;
SELECT DISTINCT id_credito, fecha_corte FROM cortes ORDER BY id_credito, fecha_corte;
```

</details>

## E — Parámetros y resultado vacío

1. Consulta IDs de una fecha y atraso mayor que un umbral con dos `?`.
2. Usa octubre y 100: predice la lista recuperada y muestra un mensaje si está vacía.
3. Prueba un valor de fecha que no exista: debe producir una selección vacía.
4. Explica por qué no necesitas rellenar con ceros ni volver a crear la base.

<details>
<summary>Ver solución razonada de E</summary>

```python
sql = """SELECT id_credito FROM cortes
         WHERE fecha_corte = ? AND dias_atraso > ? ORDER BY id_credito"""
filas = conexion.execute(sql, ("2026-10-31", 100)).fetchall()
if not filas:
    print("Sin filas para estas condiciones")
```

El orden de la tupla corresponde al de los marcadores. Devuelve [] porque los
atrasos conocidos no superan 40. Una fecha inexistente también produce []. Un
resultado vacío es distinto de una fila con saldo NULL: no hay registros que
respondan a la pregunta. La consulta no debe cambiar la fuente.

</details>

## Evidencia, reflexión y siguiente paso

Conserva tu script, SQL, parámetros, cantidades e IDs esperados; incluye una nota
que explique la frontera de 30, los paréntesis, el desempate y NULL frente a cero.
Repite la ejecución: el resultado ordenado debe ser el mismo y la base debe seguir
intacta. ¿Qué dato necesitarías para clasificar un atraso desconocido? ¿Qué pregunta
responde una lista de fechas distintas? No hay checkpoint implementado todavía.

Continúa con la [lección 03.03 — Crear tablas y cargar datos](../../../curriculum/03_sql_databases/03_create_load/README.md).

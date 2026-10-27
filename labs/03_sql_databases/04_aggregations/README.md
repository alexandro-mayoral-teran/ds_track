# Lab 03.04 — Agregaciones e indicadores

## Entrada, actividad y resultado

Lee la [lección 03.04](../../../curriculum/03_sql_databases/04_aggregations/README.md)
y completa 03.01–03.03 con sus labs. Recibes la base ficticia de 03.01, sus CSV
y el ejemplo [aggregations.py](../../../curriculum/03_sql_databases/04_aggregations/aggregations.py).
Produce consultas y una nota con universo, unidad, numeradores, denominadores,
cobertura y resultados comprobados. Conserva fuentes y base; consulta archivos
en solo lectura. No necesitas exportar tablas ni instalar paquetes.

Ejecuta los comandos de la lección con tu entorno elegido. Puedes adaptar el
script con otro nombre en su misma carpeta, conservando el original, y elegir
una copia existente con --database. Si lo mueves, adapta SOURCE: su ruta depende
de la ubicación del script. En el bloque de main con la conexión memory abierta
puedes añadir tus consultas por segmento sobre detalle antes de finally.
En los ejercicios SQL, cambia las fechas y umbrales por marcadores ? al ejecutar
desde Python; conserva los valores en una tupla separada.
Una sesión puede cubrir A–B; C–E completan el criterio esencial.

## A — Unidad y conteos

1. Explica qué representa una fila de cortes y qué representa una fila agrupada
   por fecha.
2. Cuenta observaciones, saldos conocidos y créditos distintos en octubre.
3. Repite sobre las dos fechas sin filtrar y explica la diferencia.

<details>
<summary>Ver solución razonada de A</summary>

```sql
SELECT COUNT(*) AS observaciones,
       COUNT(saldo_mxn) AS saldos_conocidos,
       COUNT(DISTINCT id_credito) AS creditos_distintos
FROM cortes
WHERE fecha_corte = '2026-10-31';
```

Octubre devuelve (24, 21, 24). Sin WHERE devuelve (48, 42, 24): cada crédito
tiene dos observaciones. Un grupo por fecha es un resumen, no un crédito ni
un cliente. COUNT(saldo_mxn) incluye el cero conocido de 004 en octubre.

</details>

## B — Suma, promedio y cobertura

1. Calcula suma, promedio, mínimo y máximo conocidos de octubre.
2. Agrupa por fecha y concilia filas, conocidos y suma con el detalle.
3. Explica por qué el promedio usa 21 y no 24 como denominador.

<details>
<summary>Ver solución razonada de B</summary>

```sql
SELECT fecha_corte, COUNT(*) AS observaciones,
       COUNT(saldo_mxn) AS saldos_conocidos,
       SUM(saldo_mxn) AS suma_conocida_mxn,
       AVG(saldo_mxn) AS promedio_conocido_mxn,
       MIN(saldo_mxn) AS minimo_conocido_mxn,
       MAX(saldo_mxn) AS maximo_conocido_mxn
FROM cortes
GROUP BY fecha_corte
ORDER BY fecha_corte;
```

| Fecha | Filas | Conocidos | Suma MXN | Promedio MXN | Mínimo MXN | Máximo MXN |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | 24 | 21 | 47 200 | ≈ 2 247.62 | 1 100 | 3 300 |
| 2026-10-31 | 24 | 21 | 46 700 | ≈ 2 223.81 | 0 | 3 300 |

Promedio = suma / conocidos. Hay tres saldos ausentes por fecha, que no
imputamos como cero. La cobertura de saldo es 21/24 = 87.5 % en ambas fechas.
Los grupos completos suman 48 filas, 42 conocidos y 93 900 MXN conocidos.
La suma de dos cortes no es el saldo de una única fecha: solo sirve aquí para
conciliar la partición del histórico. Una variación del saldo conocido tampoco
prueba por sí sola una variación del saldo completo.

</details>

## C — Grupos y HAVING

1. En detalle de la conexión temporal, resume por fecha y segmento.
2. Concilia los cuatro grupos de octubre con su total.
3. Filtra octubre en WHERE y grupos con al menos 5 registros en HAVING.
4. Cambia >= 5 por > 5 y explica qué ocurre con comercio.

<details>
<summary>Ver solución razonada de C</summary>

```sql
SELECT fecha_corte, segmento, COUNT(*) AS registros,
       COUNT(saldo_mxn) AS saldos_conocidos,
       SUM(saldo_mxn) AS suma_conocida_mxn
FROM detalle
GROUP BY fecha_corte, segmento
ORDER BY fecha_corte, segmento;
```

Octubre:

| Segmento | Registros | Saldos conocidos | Suma conocida MXN |
| --- | --- | --- | --- |
| comercio | 5 | 5 | 15 500 |
| consumo | 10 | 10 | 15 900 |
| educacion | 3 | 0 | NULL |
| servicios | 6 | 6 | 15 300 |

La suma de valores conocidos de los grupos es 46 700, con 21 saldos conocidos
de 24 registros. educacion sigue presente; su suma NULL no significa saldo cero.
HAVING COUNT(*) >= 5 conserva comercio, consumo y servicios. > 5 conserva
solo consumo y servicios: comercio tiene cinco exactos. WHERE filtra filas;
HAVING filtra los resultados de grupo.

</details>

## D — CASE y tasa con base explícita

1. Clasifica el atraso en desconocido, al menos 30 y menos de 30.
2. Obtén confirmados, atrasos conocidos, cobertura y tasa entre conocidos.
3. Compara la tasa 9/21 con la proporción 9/24; nombra ambas correctamente.
4. Consulta educacion en septiembre y explica por qué la tasa es NULL.

<details>
<summary>Ver solución razonada de D</summary>

```sql
SELECT COUNT(*) AS registros,
       COUNT(dias_atraso) AS atrasos_conocidos,
       COUNT(CASE WHEN dias_atraso >= 30 THEN 1 END) AS confirmados,
       100.0 * COUNT(dias_atraso) / NULLIF(COUNT(*), 0) AS cobertura_pct,
       100.0 * COUNT(CASE WHEN dias_atraso >= 30 THEN 1 END)
           / NULLIF(COUNT(dias_atraso), 0) AS tasa_conocidos_pct
FROM cortes
WHERE fecha_corte = '2026-10-31';
```

Octubre: 24 registros, 21 conocidos y 9 confirmados. Cobertura 87.5 %; tasa
entre conocidos ≈ 42.86 %. 37.5 % corresponde a confirmados/todos los registros;
no clasifica los tres desconocidos. Para educacion en septiembre usa detalle
con WHERE fecha_corte = ? AND segmento = ?: 3 registros, 0 conocidos, 0
confirmados, cobertura 0 % y tasa NULL. No hay evidencia para clasificar atrasos.

La frontera incluye los 30 exactos. COUNT de CASE sin ELSE omite filas que no
cumplen; con ELSE 0 contaría también ceros y daría 24 en octubre.

</details>

## E — Vacío, desconocido y cero

1. Consulta una fecha inexistente con agregados sin GROUP BY y después con
   GROUP BY fecha_corte. Predice las dos salidas.
2. Revisa los cuatro casos temporales de check_edge_cases del ejemplo.
3. Comprueba 29 frente a 30 y explica el denominador en el caso con atraso NULL.
4. Repite el script; el resultado debe coincidir y la fuente quedar intacta.

<details>
<summary>Ver solución razonada de E</summary>

Con COUNT(*), COUNT(saldo_mxn) y SUM(saldo_mxn), sin GROUP BY, una fecha
inexistente devuelve [(0, 0, None)]. Con GROUP BY fecha_corte devuelve [].
Dos filas con todos los valores desconocidos dan conteo 2, saldos conocidos 0
y SUM/AVG NULL. Una fila de saldo cero y atraso cero da suma 0, promedio 0.0,
conocidos 1 y tasa 0 %, con cobertura 100 %.

En frontera_30 hay tres registros: atraso 29, 30 y NULL. Dos atrasos conocidos
y uno confirmado: tasa 50 %, cobertura ≈ 66.67 %. El desconocido se conserva
como parte del universo, pero no entra en el denominador de la tasa entre
conocidos. Los dos saldos conocidos de 100 suman 200; no uses SUM(DISTINCT saldo)
para quitar importes iguales pertenecientes a observaciones distintas.

</details>

## Extensión — Combinar tasas correctamente

Para octubre, los pares confirmados/conocidos son comercio 2/5, consumo 4/9,
educacion 1/2 y servicios 2/5. Suma numeradores y denominadores: 9/21.
Compara con el promedio simple de sus porcentajes y explica por qué responde
a una medida diferente. Conserva precisión en el cálculo y redondea al mostrar.
Esta extensión no bloquea el siguiente tema.

## Evidencia, reflexión y siguiente paso

Conserva SQL y parámetros, tablas de resultados, reglas de indicadores y
conciliación contra detalle. Registra dudas y evidencia en tu bitácora personal junto a la práctica sin
marcar aprendizaje completado solo porque ejecutaste el ejemplo.
Explica: ¿qué cambia COUNT(columna) frente a COUNT(*)? ¿Qué población cambia
si filtras los NULL antes de agrupar? ¿Qué demuestra cobertura cero?
¿Por qué una suma conocida necesita su cantidad de conocidos?

No hay checkpoint de proyecto implementado. Continúa con el
[03.05 — Relacionar tablas con joins](../../../curriculum/03_sql_databases/05_joins/README.md).

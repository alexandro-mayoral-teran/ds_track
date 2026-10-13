# Lab 03.07 — Ventanas para comparar registros

## Entrada, actividad y resultado

Lee la [lección 03.07](../../../curriculum/03_sql_databases/07_windows/README.md)
y completa 03.04–03.06 con sus prerrequisitos. Recibes la base ficticia de 03.01,
sus CSV y [windows.py](../../../curriculum/03_sql_databases/07_windows/windows.py).
Produce consultas con ventanas, comprobaciones y una nota que justifique
partición, orden, marco y cobertura de las comparaciones. Conserva todas las
entradas; consulta archivos en solo lectura. Los casos nuevos viven en memoria.

Ejecuta el recorrido de tu shell y gestor de la lección. Puedes adaptar el script
con otro nombre en su misma carpeta, conservando el original; si lo mueves,
adapta SOURCE y usa --database para señalar una copia compatible existente.
Las constantes SQL están al principio; fechas y límites son parámetros con
nombre. Añade tus consultas dentro del bloque con conexión abierta, antes de
finally. No necesitas guardar posiciones ni cambios en la base.

Sesiones sugeridas: A–B para particiones y posiciones; C–D para comparación
temporal; E–F para marcos y casos límite. G es una extensión opcional.
Predice las salidas antes de abrir las soluciones.

## A — Detalle con referencias del corte

1. Ejecuta el resumen GROUP BY por fecha y después la consulta TOTALS del script.
2. Compara cantidad y unidad de filas en ambas versiones.
3. Verifica que cada fila de octubre reciba conteo 24, conocidos 21 y suma 46 700.
4. Explica qué ocurriría al sumar esa suma repetida en todas sus filas.

<details>
<summary>Ver solución razonada de A</summary>

GROUP BY entrega dos filas, una por corte; TOTALS entrega las 48 observaciones
con una referencia por fecha. La clave del detalle sigue siendo crédito/fecha.
Octubre repite (24, 21, 46700) en sus 24 filas. Septiembre repite (24, 21, 47200).

Sumar la columna de referencia de octubre daría 1 120 800 MXN: 24 veces el
mismo total. Esa columna no es la aportación de la fila. Para conciliar utiliza
un resumen por fecha y compara su valor con la referencia de cada fila, además
de comprobar que los campos originales se conserven.

</details>

## B — Posiciones, última observación y top por grupo

1. Ejecuta LATEST. Comprueba una fila por crédito y su fecha más reciente.
2. Explica qué ocurre con 022–024 y por qué no eliminamos saldo NULL antes de numerar.
3. Ejecuta TOP con octubre y limite = 3. Explica la ausencia de educacion.
4. Cambia limite a 1 y predice los IDs; repite con una fecha inexistente.
5. Explica qué función cumple el desempate id_credito.

<details>
<summary>Ver solución razonada de B</summary>

LATEST devuelve 24 créditos, todos con octubre; 022–024 mantienen saldo NULL.
Si filtras saldo conocido antes de ROW_NUMBER, 022 y 023 mostrarían septiembre
y 024 desaparecería. Estarías buscando última observación **con saldo conocido**,
otra pregunta.

TOP con tres devuelve nueve filas: comercio 021/020/019, consumo 010/009/008
y servicios 016/015/014. educacion tiene tres registros con saldo desconocido;
no participa en un orden de saldos conocidos. Con limite = 1 quedan 021, 010 y
016 en sus segmentos; una fecha inexistente devuelve []. Si usas limite = 0
el filtro exterior no conserva posiciones.

id_credito ordena de forma reproducible los empates de saldo cuando la pregunta
pide una cantidad de filas. No convierte a un crédito en económicamente mejor
ni sirve como sustituto de una regla que pida conservar todos los empates.

</details>

## C — Fila anterior y ubicación del filtro

1. Ejecuta HISTORY sobre todos los cortes y revisa las dos filas de 001 y 005.
2. Ejecuta COMPARISON con octubre y explica fecha_anterior y saldo_anterior.
3. Filtra octubre en el bloque que calcula LAG y compara los valores previos.
4. Explica por qué ambas versiones pueden tener 24 filas y responder preguntas distintas.

<details>
<summary>Ver solución razonada de C</summary>

001: septiembre 1100 no tiene fila previa; octubre 1300 recupera septiembre/1100.
005: octubre tiene fecha previa septiembre y saldo previo NULL. La fecha permite
distinguir «no hay observación anterior» de «su importe es desconocido».

Si aplicas WHERE fecha_corte = octubre antes de LAG, cada partición conserva
solo una fila y todos los previos son NULL. Si calculas LAG sobre el histórico
en la CTE y filtras fuera, conservas septiembre como referencia. La cantidad
de salida no detecta la diferencia: compara clave, fecha y valor anterior.

Una partición por fecha en lugar de crédito tampoco expresa la historia de cada
crédito; podría comparar IDs distintos de un mismo corte. Define primero la
unidad y el vínculo temporal, después escribe OVER.

</details>

## D — Cambios y base comparable

1. Revisa 001, 004, 005, 022 y 024 en la comparación de octubre.
2. Cuenta pares conocidos en ambos cortes y conserva los no comparables aparte.
3. Concilia suma de cambios con suma actual menos suma anterior de esos mismos pares.
4. Compara con 46 700 − 47 200 y explica por qué no son el mismo resultado.

<details>
<summary>Ver solución razonada de D</summary>

001 cambia 200 MXN (≈ 18.18 %). 004 cambia −1400 MXN (−100 %): actual cero
es conocido. 005 no permite diferencia porque septiembre es desconocido;
022 no permite diferencia porque octubre es desconocido; 024 tiene ambos
desconocidos. No rellenamos ninguno con cero.

Hay 19 pares comparables de los 24 créditos. Sus sumas son actual 42 900,
anterior 40 700 y cambio 2 200 MXN. La constante PAIRED_TOTALS del script
expresa la conciliación; estas consultas deben usar el histórico antes de filtrar.
Los cinco no comparables son 005, 009, 022, 023 y 024.

Los totales conocidos de cada fecha se calculan sobre 21 créditos, pero sus IDs
son distintos. Su diferencia −500 MXN mezcla la variación comparable con cambios
de cobertura; no mide solo los 19 pares. La cobertura de comparación es
19/24 ≈ 79.17 %. Conserva también los casos ausentes para explicar el resultado.

No promedies cambios porcentuales para afirmar un cambio porcentual del total.
Primero define universo y ponderación; un porcentaje agregado usaría sumas de
la misma base. Un saldo anterior cero permite cambio absoluto, pero su cambio
porcentual sigue indefinido.

</details>

## E — Acumulado conocido y marco explícito

1. Ejecuta RUNNING para octubre y comprueba las primeras cuatro filas.
2. Revisa las últimas tres, con saldo NULL, y explica conteo y suma.
3. Construye en memoria el caso de movimientos M1/M2/M3 de la lección; compara
   el marco predeterminado con ROWS y fecha/ID.
4. Explica por qué sumar saldos de un crédito en varias fechas no es acumular movimientos.

<details>
<summary>Ver solución razonada de E</summary>

Octubre acumula 1300, 2700, 4200 y 4200 al recorrer 001–004; conocidos = 1, 2,
3 y 4. El saldo cero contribuye cero, pero sí es conocido. 022–024 mantienen
el acumulado conocido en 46 700 y el conteo en 21: no añaden importe conocido.
Eso no imputa cero a sus saldos.

Para crear el caso separado:

```python
conexion = sqlite3.connect(":memory:")
conexion.execute("CREATE TABLE movimientos (id TEXT PRIMARY KEY NOT NULL, fecha TEXT, importe_mxn INTEGER)")
conexion.executemany("INSERT INTO movimientos VALUES (?, ?, ?)",
                    [("M1", "2026-10-01", 10), ("M2", "2026-10-01", 20),
                     ("M3", "2026-10-02", 5)])
```

Usa import sqlite3 y cierra en finally, como en el script. La consulta de la
sección 8 produce predeterminado 30/30/35 frente a ROWS 10/30/35. RANGE
por fecha incluye los pares de la misma fecha; ROWS con fecha/ID define cada
posición. Ambos son correctos para preguntas distintas.

RUNNING sobre créditos de octubre acumula aportaciones al total de esa fecha.
El saldo es una existencia observada, no un flujo entre fechas; sumar dos
cortes del mismo crédito contaría dos observaciones de su existencia.

</details>

## F — Huecos, base cero y desconocidos en memoria

En una conexión nueva en memoria, crea cortes con su clave y cuatro campos:

```python
conexion.execute("""CREATE TABLE cortes (
    id_credito TEXT NOT NULL, fecha_corte TEXT NOT NULL,
    saldo_mxn INTEGER, dias_atraso INTEGER,
    PRIMARY KEY (id_credito, fecha_corte))""")
filas = [
    ("A", "2026-09-30", 100, 0),
    ("A", "2026-10-31", None, 0),
    ("A", "2026-12-31", 130, 0),
    ("B", "2026-09-30", 0, 0),
    ("B", "2026-10-31", 50, 0),
    ("C", "2026-10-31", None, None),
]
conexion.executemany("INSERT INTO cortes VALUES (?, ?, ?, ?)", filas)
```

1. Predice fecha y saldo anterior de A en diciembre; consulta HISTORY.
2. Consulta COMPARISON para octubre y diciembre con sus parámetros.
3. Explica cambio absoluto y porcentual de B en octubre.
4. Compara LAG(saldo_mxn) con LAG(saldo_mxn, 1, 0) para A y C.
5. Cierra la base temporal; no agregues estas filas al archivo original.

<details>
<summary>Ver solución razonada de F</summary>

A en diciembre recupera octubre/NULL, aunque no tenga noviembre. LAG usa
observación anterior disponible; no salta NULL ni busca automáticamente un mes
exacto. El cambio de A queda desconocido.

B en octubre recupera septiembre/0 y cambia 50 MXN. Su porcentaje es NULL:
la base cero no define una variación porcentual. Su estado es comparable para
el cambio absoluto, porque ambos saldos son conocidos.

C tiene su primera observación en octubre: fecha anterior NULL y saldo anterior
NULL; estado sin_anterior. Para C, el tercer argumento 0 de LAG proporciona
cero por falta de fila, pero falsearía nuestro contrato si lo interpretamos
como saldo anterior observado. Para A en diciembre, LAG con ese tercer argumento
sigue dando NULL: la fila anterior existe y su saldo es desconocido.

Revisa también un acumulado de saldos conocidos de A en el orden disponible:
100, 100, 230. No representa saldo final ni flujo temporal; solo demostraría
cómo SUM ignora NULL al acumular esas observaciones. El saldo observado de
diciembre sigue siendo 130.

</details>

## G — Extensión: empates y promedios móviles

En memoria prepara tres IDs con saldos 100, 100 y 80. Compara ROW_NUMBER con
desempate por ID, RANK y DENSE_RANK ordenados solo por saldo descendente.
Explica qué conservaría top 2 filas frente a top 2 niveles distintos.
Después compara un AVG de hasta dos posiciones con COUNT de conocidos.

<details>
<summary>Ver solución razonada de la extensión</summary>

ROW_NUMBER entrega 1/2/3; RANK 1/1/3; DENSE_RANK 1/1/2. Top 2 filas con
ROW_NUMBER entrega dos IDs; top 2 niveles con DENSE_RANK conserva los tres.
Si añades ID al orden de RANK o DENSE_RANK, los IDs diferentes dejan de empatar.

Para una media sobre la fila actual y hasta una anterior:

```sql
SELECT id_credito, fecha_corte, saldo_mxn,
       AVG(saldo_mxn) OVER (
           PARTITION BY id_credito ORDER BY fecha_corte
           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
       ) AS promedio_hasta_dos_observaciones,
       COUNT(saldo_mxn) OVER (
           PARTITION BY id_credito ORDER BY fecha_corte
           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
       ) AS conocidos_en_marco
FROM cortes
ORDER BY id_credito, fecha_corte;
```

En el caso A de F, los promedios son 100, 100 y 130, cada uno con un conocido.
Octubre/diciembre no aportan dos saldos conocidos aunque el marco tenga dos
posiciones. No es una media de dos meses consecutivos: faltan períodos y medidas.
En la muestra original, 001 en octubre promedia (1100 + 1300)/2 = 1200,
con dos saldos conocidos. Esta extensión no bloquea el siguiente tema.

</details>

## Evidencia, reflexión y siguiente paso

Conserva SQL, parámetros, filas ordenadas y comprobaciones de cada consulta.
Tu nota debe declarar unidad, partición, orden, marco cuando corresponda y
cobertura de comparación. Registra evidencia y dudas en PROGRESS.md: ejecutar
el ejemplo no acredita por sí solo el aprendizaje.

Explica: ¿por qué dos consultas con 24 filas pueden recuperar previos diferentes?
¿Qué significa anterior cuando falta un período? ¿Por qué un acumulado con
empates puede saltar? ¿Cómo evitas sumar una referencia repetida?
¿Qué información conserva fecha_anterior que no conserva saldo_anterior?

No hay checkpoint de proyecto implementado. Continúa con el
[03.08 — Escrituras y transacciones](../../../curriculum/03_sql_databases/08_transactions/README.md).

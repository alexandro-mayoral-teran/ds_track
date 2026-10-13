# Lab 03.03 — Crear tablas y cargar datos

## Entrada, actividad y resultado

Completa la [lección 03.03](../../../curriculum/03_sql_databases/03_create_load/README.md)
y las prácticas 03.01–03.02. Recibes los tres CSV ficticios de 03.01 y el
[esquema](../../../curriculum/03_sql_databases/03_create_load/schema.sql).
Produce una base de práctica nueva, un script y una nota que explique las reglas,
los rechazos y la comprobación de persistencia. Conserva las fuentes y la base
de 03.01. Ejecuta los recorridos de la lección con tu entorno elegido.

Puedes adaptar [create_load.py](../../../curriculum/03_sql_databases/03_create_load/create_load.py)
en la misma carpeta con otro nombre, conservando el original, y elegir una ruta
distinta mediante --database. Sus fuentes y esquema dependen de la ubicación del
script; si lo llevas a otra carpeta, adapta HERE y DATA antes de ejecutarlo.
Trabaja por partes: una sesión puede cubrir A y B.

## A — Leer el contrato

1. Explica qué identifica cada clave y por qué cortes requiere dos columnas.
2. Predice si se acepta saldo cero, NULL, -1 y 1.5.
3. Explica qué reglas sobre fechas y CSV se comprueban en Python.

<details>
<summary>Ver solución razonada de A</summary>

Clientes y créditos tienen claves simples; cortes identifica crédito/fecha.
001 puede aparecer en septiembre y octubre, pero una combinación no se repite.
Cero y NULL se aceptan con significados distintos; -1 y 1.5 se rechazan.
Python verifica encabezados, número de campos, formato y validez de fechas y
conversión numérica. TEXT NOT NULL no valida una fecha del calendario.

</details>

## B — Construir y cargar

1. Ejecuta el ejemplo con una ruta nueva dentro de output.
2. Identifica en el código CREATE TABLE, activación de relaciones y orden de carga.
3. Recupera las filas con SELECT y compáralas con las entradas convertidas.
4. Cierra, reconecta en lectura y repite la comprobación.

<details>
<summary>Ver solución razonada de B</summary>

Se esperan 16 clientes, 24 créditos y 48 cortes. El orden es clientes → créditos
→ cortes. create_schema ejecuta las definiciones; enable_foreign_keys activa y
comprueba relaciones antes de BEGIN. load_rows utiliza columnas explícitas y
executemany con valores separados. verify compara cada fila y valor con la
fuente; prepare repite la comparación después de cerrar y reconectar.
Contar filas por sí solo no detectaría un saldo cambiado.

</details>

## C — Rechazos y fronteras en memoria

1. Revisa los seis casos de check_rejections; predice la regla que falla.
2. En una base en memoria con esquema y fuentes cargadas, prueba atraso -1 y
   atraso 1.5. Deben producir IntegrityError.
3. Prueba un corte nuevo para 001 con saldo cero y atraso None. Usa parámetros.
4. Recupera esa fila y comprueba que cero y None se conservan. Cierra la base temporal.

<details>
<summary>Ver solución razonada de C</summary>

Los seis casos prueban claves simple/compuesta, NOT NULL, FOREIGN KEY y dos
fronteras de CHECK. Para extender la prueba, usa sqlite3.connect(':memory:',
isolation_level=None), activa relaciones y llama create_schema y load_rows.

```python
sql = "INSERT INTO cortes VALUES (?, ?, ?, ?)"
conexion.execute(sql, ("001", "2026-11-30", 0, None))
fila = conexion.execute(
    "SELECT saldo_mxn, dias_atraso FROM cortes WHERE id_credito = ? AND fecha_corte = ?",
    ("001", "2026-11-30"),
).fetchone()
assert fila == (0, None)
```

Para cada caso inválido usa una fecha nueva y captura solo IntegrityError;
si se acepta, la comprobación debe fallar. El corte aceptado es adicional a la
muestra original: no llames verify con las fuentes originales después de añadirlo
sin ajustar el resultado esperado. Estas pruebas no modifican la base guardada.

</details>

## D — UNIQUE y afinidad

1. En memoria, ejecuta el ejemplo fuentes de la lección y comprueba el rechazo
   del segundo codigo_origen repetido.
2. Explica por qué no imponemos UNIQUE a region.
3. Prueba saldo '10' en un corte nuevo y consulta typeof(saldo_mxn).

<details>
<summary>Ver solución razonada de D</summary>

El código de origen es obligatorio y único según ese ejemplo; dos clientes sí
pueden compartir región. La afinidad INTEGER convierte '10' a entero; typeof
devuelve 'integer' y CHECK lo acepta. Esto no demuestra que la entrada original
ya fuera un entero de Python. No copies esta conversión como regla de limpieza
sin definir el contrato. Usa otra base en memoria para conservar la independencia
entre actividades.

</details>

## E — Repetición y conservación

1. Repite el script sobre la misma ruta: debe comprobar sin recargar.
2. En memoria, inicia BEGIN, crea tablas y provoca un rechazo de carga; ejecuta
   ROLLBACK y comprueba que tampoco quedaron las tablas creadas dentro del BEGIN.
3. Explica qué harías si una base existente difiere de las fuentes.

<details>
<summary>Ver solución razonada de E</summary>

La segunda ejecución informa base existente comprobada y mantiene 16/24/48.
Para el paso 2 usa una conexión nueva con isolation_level=None,
activa relaciones antes de BEGIN, y utiliza execute para crear las tablas.
Después de ROLLBACK:

```python
tablas = conexion.execute(
    "SELECT name FROM sqlite_master WHERE type = 'table'"
).fetchall()
assert tablas == []
```

Una base distinta se conserva para revisarla; el programa se detiene. Una nueva
práctica utiliza otra ruta. No borres cambios ni vuelvas a cargar automáticamente.

</details>

## Evidencia, reflexión y siguiente paso

Conserva esquema, script, ruta relativa de práctica y nota con filas comparadas,
rechazos, fronteras y persistencia. Las bases locales de output no se versionan.
Explica: ¿por qué declarar una relación no basta? ¿Qué comprueba el esquema y
qué comprueba Python? ¿Por qué UNIQUE debe venir del contrato? ¿Cómo sabes que
los datos persistieron y que repetir no duplicó filas?

No hay checkpoint de proyecto implementado. Continúa con el
[03.04 — Agregaciones e indicadores](../../../curriculum/03_sql_databases/04_aggregations/README.md).

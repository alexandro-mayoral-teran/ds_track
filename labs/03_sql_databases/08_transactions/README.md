# Lab 03.08 — Escrituras y transacciones

## Entrada, actividad y resultado

Lee la [lección 03.08](../../../curriculum/03_sql_databases/08_transactions/README.md)
y completa los prerrequisitos. Recibes la base ficticia de 03.01, los CSV y
[transactions.py](../../../curriculum/03_sql_databases/08_transactions/transactions.py).
Produce una copia de práctica, tu script y una nota con selección previa,
valores posteriores, decisiones de confirmación/reversión y verificación al
reconectar. Conserva la fuente: ninguna escritura se hace sobre ella.

Primero ejecuta la demostración completa con los comandos de la lección.
Después practica A–F manualmente con otra copia. G es una extensión en memoria.
Sesiones sugeridas: A–B, C–D y E–F. No necesitas completar todo en una sesión.
Los archivos generados en output no se versionan; conserva evidencia textual.

## A — Crear y revisar una copia manual

1. Ejecuta el programa completo y anota su estado final 16/24/49.
2. Repite: debe comprobar la copia existente sin nuevas escrituras.
3. Crea mi_lab.py en la carpeta de esta lección, sin modificar transactions.py,
   con este inicio para preparar otra copia:

```python
from transactions import connect, copy_new, source_rows, DEFAULT_SOURCE, HERE

ruta = HERE / "output" / "lab_manual.sqlite"
original = source_rows()
creada = copy_new(DEFAULT_SOURCE, ruta, original)
if not creada:
    raise ValueError("Elige otra ruta nueva para comenzar una práctica manual")
```

El helper conserva archivos existentes; si encuentra una práctica parcial o
distinta también se detiene sin sobrescribirla. Para retomar tu propia copia,
consulta su estado conscientemente: no vuelvas a crearla ni la reinicies.
Si guardas mi_lab.py en otra carpeta, adapta las importaciones y rutas antes
de ejecutarlo. Añade las actividades siguientes al script en orden, por sesiones.

4. Abre la copia con connect(ruta) y consulta 001/octubre antes de escribir.
5. Comprueba claves foráneas activas y que fuente y copia sean rutas distintas.

<details>
<summary>Ver solución razonada de A</summary>

La demostración completa confirma 1350 en 001/octubre y conserva noviembre
de 001; deja 49 cortes. La copia manual recién creada, en cambio, comienza
con la muestra original: 48 cortes y 1300 en 001/octubre. Son dos archivos
distintos para dos recorridos; no confundas sus estados esperados.

connect(ruta) abre el archivo existente en escritura, con control explícito,
y activa claves foráneas. copy_new comprueba fuente antes de crear el destino
y no sobrescribe archivos. El archivo fuente sigue consultándose en lectura.
Un archivo cuya ruta coincida con la fuente se rechaza.

</details>

## B — Ensayar UPDATE y después confirmar

1. En la copia manual de A, inicia BEGIN IMMEDIATE y selecciona 001/octubre.
2. Cambia temporalmente su saldo a 999 con clave completa; comprueba una fila afectada.
3. Consulta el valor en esa conexión y en otra conexión de lectura.
4. Revierte y comprueba 1300 otra vez.
5. En otra transacción, aplica la corrección 1350 exigiendo el valor previo 1300.
6. Comprueba atraso intacto, confirma, cierra y reconecta.

<details>
<summary>Ver solución razonada de B</summary>

Durante el ensayo, la conexión escritora ve 999 y una conexión separada normal
ve 1300. Cierra el lector antes de terminar la transacción escritora.
Después de rollback ambas recuperan 1300. Para la corrección:

```python
conexion = connect(ruta)
try:
    conexion.execute("BEGIN IMMEDIATE")
    previa = conexion.execute(
        "SELECT saldo_mxn, dias_atraso FROM cortes WHERE id_credito = ? AND fecha_corte = ?",
        ("001", "2026-10-31"),
    ).fetchone()
    if previa != (1300, 10):
        raise ValueError("Estado previo distinto del revisado")
    cursor = conexion.execute(
        """UPDATE cortes SET saldo_mxn = ?
           WHERE id_credito = ? AND fecha_corte = ? AND saldo_mxn = ?""",
        (1350, "001", "2026-10-31", 1300),
    )
    if cursor.rowcount != 1:
        raise ValueError("Alcance de UPDATE inesperado")
    posterior = conexion.execute(
        "SELECT saldo_mxn, dias_atraso FROM cortes WHERE id_credito = ? AND fecha_corte = ?",
        ("001", "2026-10-31"),
    ).fetchone()
    if posterior != (1350, 10):
        raise ValueError("Resultado inesperado")
    conexion.commit()
except Exception:
    if conexion.in_transaction:
        conexion.rollback()
    raise
finally:
    conexion.close()
```

Después abre connect(ruta, readonly=True), consulta esa fila y cierra en finally.
Esperas (1350, 10) y 48 cortes; la fuente conserva (1300, 10).
Repetir la misma sentencia condicionada al previo 1300 afecta cero filas:
debes revisar el estado, no afirmar que se aplicó una nueva corrección.

</details>

## C — Fallo a mitad de una transacción

Para aislar el mecanismo sin cambiar la copia manual, crea este caso en memoria:

```python
import sqlite3

conexion = sqlite3.connect(":memory:", isolation_level=None)
conexion.execute("PRAGMA foreign_keys = ON")
assert conexion.execute("PRAGMA foreign_keys").fetchone() == (1,)
conexion.execute("CREATE TABLE clientes (id TEXT PRIMARY KEY NOT NULL)")
conexion.execute("CREATE TABLE creditos (id TEXT PRIMARY KEY NOT NULL, cliente TEXT NOT NULL REFERENCES clientes(id))")
conexion.execute("INSERT INTO clientes VALUES (?)", ("P",))
```

En Python >= 3.12, añade autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL a esa
llamada, como explica la lección, para fijar el mismo modo. En 3.11 conserva
isolation_level=None sin ese argumento.

1. Inicia BEGIN. Inserta K1 con cliente P y después K2 con cliente inexistente.
2. Captura el IntegrityError esperado. Antes de rollback, observa si K1 sigue
   dentro de la conexión y si in_transaction sigue verdadero.
3. Revierte todo y comprueba que no quedó ningún crédito.
4. Repite sin BEGIN, en otra base temporal equivalente, y explica la diferencia.

<details>
<summary>Ver solución razonada de C</summary>

El esquema usa referencias inmediatas y la política normal. La inserción K2
falla, pero K1 sigue pendiente en la transacción; in_transaction es verdadero.
ROLLBACK devuelve la tabla creditos al estado vacío. No confirmes después de
capturar ese error si el contrato requería ambas filas como una unidad.

Sin BEGIN, en nuestro modo explícito, K1 se confirma al completar su sentencia.
El error de K2 y un rollback posterior no borran K1 ya confirmado. Así se ve
por qué una llamada a executemany o un bloque with no sustituyen declarar
los límites de la decisión. Cierra siempre la base temporal en finally.

</details>

## D — Carga repetible y conflicto

1. En la copia manual que ya tiene la corrección de B, abre otra conexión.
2. Importa BATCH y load_batch desde transactions y carga las dos filas de noviembre.
3. Repite el lote; comprueba cero inserciones y los mismos valores.
4. Prueba un lote vacío y uno con un registro nuevo seguido de una clave conflictiva.
5. Comprueba que el conflicto no deje el registro nuevo de forma parcial.

<details>
<summary>Ver solución razonada de D</summary>

load_batch(conexion, BATCH) devuelve 2 en la primera ejecución, 0 en la segunda
y load_batch(conexion, []) devuelve 0. La copia tiene 50 cortes, con noviembre
de 001 = (1400, 0) y 002 = (1500, 0). La clave completa identifica cada registro.

```python
conflictivo = [
    ("003", "2026-11-30", 1600, 0),
    ("001", "2026-11-30", 999, 0),
]
```

La segunda fila difiere del valor 1400 existente y produce ValueError.
El rollback del lote también elimina la inserción nueva de 003. Se conservan
50 cortes y ambos registros de noviembre anteriores. Captura el ValueError
esperado para comprobar; propaga cualquier error inesperado y cierra la conexión.

No basta con contar 50: compara filas y valores. Repetición exacta, clave
conflictiva y corrección deliberada son tres decisiones distintas.
Un lote con None conserva NULL, no cero; un saldo negativo se rechaza antes
de comenzar la carga por la validación de entrada y también por el contrato SQL.

</details>

## E — DELETE, reversión y relaciones

1. Selecciona noviembre de 002 en la copia manual de D; predice alcance y resultado.
2. Inicia BEGIN IMMEDIATE, elimina solo esa fila y verifica ausencia.
3. Revierte y comprueba que reaparece con sus valores originales.
4. Selecciona otra vez, elimina, confirma y verifica al reconectar.
5. Ensaya DELETE de C001 en una transacción aparte y explica el rechazo.

<details>
<summary>Ver solución razonada de E</summary>

```sql
SELECT id_credito, fecha_corte, saldo_mxn, dias_atraso
FROM cortes WHERE id_credito = '002' AND fecha_corte = '2026-11-30';
```

Devuelve (002, 2026-11-30, 1500, 0). Dentro de la transacción:

```sql
DELETE FROM cortes
WHERE id_credito = '002' AND fecha_corte = '2026-11-30';
```

Comprueba rowcount = 1 y SELECT vacío. Tras rollback reaparece; después del
commit de la segunda transacción desaparece al reconectar. Quedan 49 cortes,
con 001/noviembre y la corrección 1350 de B. El resto se conserva.

C001 tiene créditos 001 y 002; el esquema no declara cascada. Con foreign_keys
activo, DELETE del cliente falla por referencia y se revierte. No desactives
la regla para lograr el borrado. No se elimina la fila de cliente ni sus créditos.

</details>

## F — Persistencia y límites de rollback

1. Comprueba todas las filas de la copia manual contra final_rows(original) del script.
2. Inicia un cambio temporal sobre 001/octubre y cierra sin confirmar; consulta
   con otra conexión y explica por qué sigue 1350.
3. Explica qué harías si una sesión se interrumpe después de un commit.
4. Vuelve a ejecutar el programa sobre su copia de demostración; comprueba
   que solo verifica y no inicia otro recorrido de escrituras.

<details>
<summary>Ver solución razonada de F</summary>

Puedes importar final_rows y verify_file desde transactions y ejecutar
verify_file(ruta, final_rows(original)). La copia manual de A–E coincide con el
estado final de la demostración: 16/24/49, corrección de octubre y noviembre
de 001. La fuente sigue siendo la muestra original.

En este modo, un cambio con BEGIN pendiente se descarta al cerrar; el patrón
recomendado expresa rollback antes de close, en vez de usar el cierre como
la decisión implícita. Si ya hubo commit, cerrar o llamar a rollback no vuelve
al estado anterior confirmado. Conserva la copia para investigar y documenta
una corrección o empieza otro ensayo en una ruta nueva; no borres trabajo previo.

Si una copia existente difiere de lo esperado, el programa la rechaza en
lectura y la conserva. No acredita finalización solo por abrir el archivo:
compara claves, valores, restricciones y persistencia.

</details>

## G — Extensión: SAVEPOINT dentro de una transacción

En otra base en memoria, comienza con una fila de valor 10 y prueba la secuencia:

```sql
CREATE TABLE ensayo (id INTEGER PRIMARY KEY, valor INTEGER NOT NULL);
INSERT INTO ensayo VALUES (1, 10);
BEGIN;
UPDATE ensayo SET valor = 20 WHERE id = 1;
SAVEPOINT opcion;
UPDATE ensayo SET valor = 99 WHERE id = 1;
ROLLBACK TO opcion;
RELEASE opcion;
SELECT valor FROM ensayo WHERE id = 1;
ROLLBACK;
SELECT valor FROM ensayo WHERE id = 1;
```

Ejecuta cada sentencia con execute sobre una conexión en isolation_level=None;
no pases todo a executescript dentro de otra transacción pendiente. Cierra en finally.
Predice ambos valores y explica qué decisión conserva o descarta cada nivel.

<details>
<summary>Ver solución razonada de la extensión</summary>

Tras ROLLBACK TO opcion, el valor es 20: se descartó el cambio posterior a 99,
pero no la escritura previa al savepoint. RELEASE retira ese punto y no confirma
el BEGIN exterior. El primer SELECT devuelve 20; tras ROLLBACK exterior, el
segundo devuelve 10. El INSERT inicial estaba confirmado antes de BEGIN en
este modo. No uses reversión parcial si tu contrato exige atomicidad de todo
el lote: en ese caso revierte la transacción completa.

</details>

## Evidencia, reflexión y siguiente paso

Conserva script, consultas y una nota con filas seleccionadas antes/después,
alcance, errores esperados, decisión de commit/rollback y comprobación al
reconectar. No publiques las bases locales de output. Registra evidencia y
dudas en PROGRESS.md; ejecutar la demostración no acredita aprendizaje por sí solo.

Explica: ¿por qué el fallo de una sentencia no garantiza revertir las anteriores?
¿Qué diferencia hay entre repetir un lote y sobrescribir una clave conflictiva?
¿Por qué cerrar no sustituye confirmar? ¿Qué protege la condición del valor previo?
¿Qué cambios quedan si la ejecución falla entre dos decisiones ya confirmadas?

No hay checkpoint de proyecto implementado. Continúa con el
[03.09 — Integración pandas y SQL](../../../curriculum/03_sql_databases/09_pandas_sql/README.md).

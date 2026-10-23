# 10.06 — DuckDB: SQL sobre Parquet

## Propósito y prerrequisitos

Consultar archivos Parquet directamente con SQL, conservar el contrato de datos
y distinguir un plan previsto de una ejecución observada. DuckDB es un motor
analítico que aquí se ejecuta dentro de Python; no necesitamos un servidor.

Necesitas reconocer tablas, claves y filtros. Puedes repasar
[SQL](../../03_sql_databases/README.md) y
[Parquet](../../09_arrow_parquet/01_csv_parquet_arrow/README.md), pero esta
lección presenta todos sus datos, reglas y resultados. No exige entregas
anteriores. La [extensión streaming 10.05](../05_streaming_memory/README.md)
es opcional y no bloquea esta sección.

**Esencial:** SQL sobre Parquet, esquema, filtros/agregaciones, varios archivos,
EXPLAIN y EXPLAIN ANALYZE, valores conciliados. **Práctica:** frontera, vacío y
errores fuera del filtro. **Ampliación:** unión con un catálogo pequeño.
Python sirve de ejecutor mínimo; los clientes Python/R se profundizan en 10.07.
No hacemos un benchmark ni medimos RAM o I/O físico.

## Objetivos

- Diferenciar motor, conexión, archivo Parquet y base persistente.
- Escribir SELECT/FROM/WHERE/GROUP BY/ORDER BY con una pregunta concreta.
- Conservar ID textual, fecha e importe entero y comprobar tipos de agregación.
- Explicar filtros/proyecciones y estimaciones frente a filas observadas.
- Auditar todas las partes y comparar cada valor con CSV externo.

## Entorno y archivos

Referencia ejecutada: **Python 3.12.12 / DuckDB 2.0.0**. DuckDB se incorpora
ahora como dependencia exacta en [`pyproject.toml`](../../../pyproject.toml) y
[`uv.lock`](../../../uv.lock), conservando los registros anteriores salvo la
dependencia del proyecto. No se requieren pandas, Polars o PyArrow para estos
ejemplos DuckDB, aunque siguen declarados para sus propias secciones.

Sigue un [recorrido completo](recorridos.md) con tu gestor. Preparar entorno
es distinto de necesitar entregas previas. Abre la raíz en el editor y elige
ese intérprete. Los bloques Python van en un script/consola Python, no en
PowerShell; SQL se envía como texto a la conexión, sin instalar una CLI aparte.

| Archivo | Función |
| --- | --- |
| [muestra.csv](muestra.csv) | Fuente autónoma completa |
| [seleccion.sql](seleccion.sql) | Consulta con parámetros de archivos, fecha y umbral |
| [resumen.sql](resumen.sql) | Resumen por fecha |
| [consultas_duckdb.py](consultas_duckdb.py) | Preparación, auditoría, ejecución y contraste estándar |
| [recorridos.md](recorridos.md) | Instalación/comprobación y sesiones nuevas |
| [Lab 10.06](../../../labs/10_polars_duckdb/06_duckdb_parquet/README.md) | Actividad, evidencia y soluciones |

## 1. Pregunta, datos y contrato completos

Una financiera ficticia registra saldos de tres créditos en dos cortes.
**¿Qué créditos tienen al menos 2000 MXN el 31 de octubre de 2026?** Después
contaremos registros y sumaremos cada corte completo.

| id_credito | fecha_corte | saldo_mxn |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Unidad: **crédito/corte**, clave ID/fecha única. ID textual de tres dígitos;
fecha válida entre 1900 y 2100; saldo entero 0–2147483647 MXN, sin ausencias.
Se rechaza toda la fuente ante una incidencia, incluso fuera del filtro.
No se imputan ceros ni se deduplican registros.

Respuesta manual: octubre ≥ 2000 deja `003/2600`, uno/2600 MXN. Septiembre
≥ 2000 deja `002/2000` y `003/2500`, dos/4500. Los cortes completos tienen
tres registros y 4500/4600 MXN. Sumar fechas distintas no representa un saldo
de cartera en una fecha única. Noviembre no tiene registros.

## 2. Motor, archivo y base: responsabilidades distintas

| Elemento | Papel |
| --- | --- |
| Parquet | Archivo con columnas, tipos y metadatos; no ejecuta SQL |
| DuckDB | Motor que interpreta SQL y lee/procesa los datos |
| Conexión `:memory:` | Sesión/base en memoria para este recorrido |
| Archivo `.duckdb` | Base persistente que se puede abrir con una conexión |

Consultar `read_parquet(...)` no convierte el archivo en una base `.duckdb`
ni requiere cargarlo primero en pandas. El motor sí utiliza memoria de trabajo
para lectores y operaciones. Con `fetchall()` recogemos todos los resultados
restantes en objetos Python: lo hacemos porque la salida es pequeña.

`CREATE TABLE ... AS SELECT ...` copia resultados a una tabla de la base;
una vista sobre `read_parquet` conserva una definición que depende de archivos
externos. Guardar una vista en una base no incorpora automáticamente sus
archivos. Esta sección abre `:memory:` y no modifica bases persistentes.
La [API de conexiones](https://duckdb.org/docs/2.0/clients/python/overview)
explica ambos modos; no se exige un servidor o servicio para continuar.

## 3. Ejemplo autónomo: preparar y consultar directamente

El bloque contiene toda la muestra. Crea una carpeta nueva, una tabla de
preparación y un Parquet. No depende de funciones del curso:

```python
from datetime import date
from pathlib import Path
import duckdb

carpeta = Path("output/duckdb_1006_ejemplo")
carpeta.mkdir(parents=True, exist_ok=False)
archivo = carpeta / "saldos.parquet"

with duckdb.connect(":memory:") as con:
    con.execute("CREATE TABLE saldos(id_credito VARCHAR, fecha_corte DATE, saldo_mxn INTEGER)")
    con.execute("""
        INSERT INTO saldos VALUES
        ('001', DATE '2026-09-30', 0),
        ('002', DATE '2026-09-30', 2000),
        ('003', DATE '2026-09-30', 2500),
        ('001', DATE '2026-10-31', 100),
        ('002', DATE '2026-10-31', 1900),
        ('003', DATE '2026-10-31', 2600)
    """)
    con.execute("COPY saldos TO ? (FORMAT PARQUET, COMPRESSION ZSTD)", [str(archivo)])

sql = """
    SELECT id_credito, saldo_mxn
    FROM read_parquet(?)
    WHERE fecha_corte = ? AND saldo_mxn >= ?
    ORDER BY id_credito
"""
parametros = [str(archivo), date(2026, 10, 31), 2000]
with duckdb.connect(":memory:") as con:
    con.execute(sql, parametros)
    esquema = [(d[0], str(d[1])) for d in con.description]
    pares = con.fetchall()
assert esquema == [("id_credito", "VARCHAR"), ("saldo_mxn", "INTEGER")]
assert pares == [("003", 2600)]
print(pares)
```

`VARCHAR` representa texto; `DATE`, fecha sin hora; `INTEGER`, entero firmado
de 32 bits. El ID conserva ceros. `DATE '2026-09-30'` es un literal SQL de
fecha, distinto de una cadena sin tipo. `INSERT ... VALUES` declara las seis
filas; esta preparación pequeña no es una recomendación de carga masiva.

`COPY ... TO` escribe un archivo. La carpeta exclusiva evita reutilizar la
entrega anterior: en DuckDB 2.0.0, COPY de archivo único puede sobrescribir un
destino existente. Por eso no repetimos escrituras sobre el mismo nombre ni
activamos opciones de borrado. El preparador integrado aplica la misma política
de carpeta nueva. Consulta [COPY](https://duckdb.org/docs/2.0/sql/statements/copy).

El contexto `with` cierra cada conexión al salir. La segunda no contiene la
tabla `saldos`: aun así lee el Parquet escrito por la primera. Esto demuestra
qué datos sobrevivieron fuera de la base en memoria.

### Leer la consulta en orden de significado

1. `FROM read_parquet(?)` establece la fuente de filas.
2. `WHERE` conserva fecha y umbral; `AND` exige ambas condiciones y `>=` incluye 2000.
3. `SELECT` elige ID/saldo para responder la pregunta.
4. `ORDER BY` fija el orden de presentación; sin él no suponemos orden estable.

El orden de escritura de SQL y el orden físico que el motor decide no son lo
mismo. Los `?` son posiciones para valores; el segundo argumento de `execute`
los proporciona por orden. La ruta es un valor de `read_parquet`, no el nombre
de una tabla SQL. No concatenamos rutas/fechas en SQL. La
[DB API](https://duckdb.org/docs/2.0/clients/python/dbapi)
documenta esa separación. `execute` inicia la sentencia; `fetchall` consume
el resultado restante. Un error de ejecución puede aparecer también al recuperar
filas. No confundimos `execute` con construir solamente un plan lazy.

## 4. Esquema, agregación y cobertura

Continuación; el archivo sigue existiendo, no necesitamos la tabla de preparación:

```python
with duckdb.connect(":memory:") as con:
    descripcion = con.execute("DESCRIBE SELECT * FROM read_parquet(?)", [str(archivo)]).fetchall()
    assert [(f[0], f[1]) for f in descripcion] == [
        ("id_credito", "VARCHAR"), ("fecha_corte", "DATE"), ("saldo_mxn", "INTEGER")
    ]
    con.execute("""
        SELECT fecha_corte, COUNT(*) AS registros, SUM(saldo_mxn) AS saldo_mxn
        FROM read_parquet(?) GROUP BY fecha_corte ORDER BY fecha_corte
    """, [str(archivo)])
    tipos_resumen = [(d[0], str(d[1])) for d in con.description]
    resumen = con.fetchall()
assert tipos_resumen == [("fecha_corte", "DATE"), ("registros", "BIGINT"), ("saldo_mxn", "HUGEINT")]
assert resumen == [(date(2026, 9, 30), 3, 4500), (date(2026, 10, 31), 3, 4600)]
```

`GROUP BY` cambia la unidad a un corte; `COUNT(*)` cuenta filas. `SUM(INTEGER)`
devuelve HUGEINT en esta versión, un entero más amplio: no copiamos la suposición
de que la suma seguirá siendo Int32. En Python se recupera como `int`.
`description` inspecciona nombres/tipos SQL antes de adaptar los resultados.

`DESCRIBE` informa el esquema del lector, no certifica valores ni clave única.
Puede informar columnas anulables aunque nuestros datos no tengan ausencias;
eso no acredita el contrato de no ausencia ni un esquema Arrow no anulable.
El verificador revisa también todas las filas y cada valor contra CSV externo.

Con valores ausentes, `COUNT(columna)` cuenta solo no NULL y `SUM` omite NULL;
sin valores no nulos, SUM devuelve NULL. Una agrupación de entrada vacía no
inventa cortes; una agregación global puede devolver una fila con conteo cero
y suma NULL. Nuestra fuente monetaria no admite ausencias y el control de
selección vacía usa cero registros/suma cero de una lista vacía; no imputa
un saldo faltante. Repasa [10.04](../04_types_missing_joins/README.md) para
separar esas situaciones.

## 5. EXPLAIN frente a EXPLAIN ANALYZE

```python
with duckdb.connect(":memory:") as con:
    plan = con.execute("EXPLAIN " + sql, parametros).fetchall()
    analisis = con.execute("EXPLAIN ANALYZE " + sql, parametros).fetchall()
    for clave, texto in plan + analisis:
        print(clave)
        print(texto)
    reales = con.execute(sql, parametros).fetchall()
assert reales == [("003", 2600)]
```

| Petición | Qué aporta | Qué falta |
| --- | --- | --- |
| EXPLAIN | Plan físico previsto y cardinalidades estimadas | Ejecutar y comprobar valores |
| EXPLAIN ANALYZE | Ejecuta, muestra filas observadas y tiempos del perfil | Comprobar valores y definir una comparación de costos válida |
| SELECT + recuperación | Devuelve los datos | Conciliar tipos y cada par con la referencia |

Aquí ANALYZE se aplica **solo a nuestro SELECT**: no es una inspección inocua
de cualquier sentencia, porque ejecuta lo que se le pasa. Después ejecutamos
SELECT otra vez para obtener sus filas: no contamos eso como una única ejecución
medida. [EXPLAIN](https://duckdb.org/docs/2.0/guides/meta/explain) describe el
plan sin ejecutar la consulta; puede necesitar metadatos para planificar.
[EXPLAIN ANALYZE](https://duckdb.org/docs/2.0/guides/meta/explain_analyze)
añade observaciones de ejecución, no garantiza corrección de los importes.

En el plan de esta muestra, busca desde la fuente hacia la salida:

- `Read Parquet`/`READ_PARQUET`: lector de archivo.
- `Filters`: fecha y umbral acercados al lector, cuando el optimizador los conserva.
- `Projections`: columnas requeridas; fecha puede usarse en un filtro aunque no salga.
- `Projection` y `Order By`: forma y presentación de salida.
- `~... rows`: estimaciones; las filas sin `~` en el perfil son observaciones del nodo.

Los nombres, orden interno, compresiones y estimaciones pueden cambiar. El
optimizador puede quitar un filtro ya garantizado por estadísticas o producir
`EMPTY_RESULT` si sabe que no habrá filas. No exigimos un texto literal ni que
cada consulta muestre los mismos nodos. La
[lectura parcial de Parquet](https://duckdb.org/docs/2.0/data/parquet/overview)
explica filtros/proyección y el posible uso de estadísticas para omitir partes.

La salida de 2.0.0 puede incluir archivos, grupos leídos y `Data Read`. Son
métricas reportadas por el motor; no las convertimos en prueba de I/O físico
del dispositivo, ausencia de caché o RAM acotada. Los tiempos pueden redondearse
a cero, incluyen una ejecución concreta y no son un ranking entre motores.
10.09 desarrollará mediciones comparables. No sumes tiempos paralelos de nodos
como si fueran necesariamente el tiempo total transcurrido.

## 6. Varios archivos y auditoría completa

Un conjunto de partes es una sola tabla lógica si sus filas y esquemas cumplen
un contrato común. Leer completo **y** partes juntos repetiría las mismas filas.
No pases una carpeta genérica con archivos auxiliares como si cualquier contenido
fuera parte del dataset. En esta práctica usamos una lista explícita.

Recorrido integrado, desde una sesión Python nueva en la raíz:

```python
from pathlib import Path
import sys

modulos = Path("curriculum/10_polars_duckdb/06_duckdb_parquet").resolve()
sys.path.insert(0, str(modulos))
from consultas_duckdb import preparar, ejecutar

archivos = preparar("output/duckdb_1006_integrado")
completo = ejecutar(archivos["completo"])
partes = ejecutar(archivos["partes"])
assert completo["seleccion"] == partes["seleccion"] == [("003", 2600)]
assert completo["resumen"] == partes["resumen"]
assert partes["control"]["saldo_mxn"] == 2600
print(partes["resumen"])
```

El preparador valida el CSV propio con Python estándar y crea completo/partes
nuevos por fecha; para fuente vacía crea una parte vacía tipada. El ejecutor
revisa esquema **de cada archivo**, reconstruye la referencia del CSV externo,
audita todas las filas juntas y luego consulta. Esto detecta claves repetidas
entre partes y alteraciones compensadas que conservan suma/conteo.

En SQL, `read_parquet(?)` acepta también la lista de rutas como un valor; por
eso al ejecutar se pasa `[lista_de_rutas, fecha, umbral]`. No usamos
`union_by_name` para ocultar columnas faltantes ni hacemos casts para disimular
esquemas incompatibles. La [guía de varios archivos](https://duckdb.org/docs/2.0/data/multiple_files/overview)
explica las fuentes múltiples. La auditoría completa materializa datos; no es
un pipeline con RAM acotada ni parte de un benchmark selectivo.

El verificador solo lee fuentes/archivos y perfila SELECT. Conserva las fuentes
sin cambios durante las lecturas: no promete una instantánea transaccional si
otro proceso modifica el Parquet entre comprobaciones.

### Ampliación: unión sobre la fuente Parquet

Este catálogo completo y estático tiene una fila por crédito: 001/Personal,
002/Comercio y 004/Vivienda. No contiene 003. Suponemos producto estable en los
dos cortes. Sobre `archivo` del ejemplo autónomo:

```python
with duckdb.connect(":memory:") as con:
    unida = con.execute("""
        WITH catalogo(id_credito, producto) AS (
            VALUES ('001','Personal'), ('002','Comercio'), ('004','Vivienda')
        )
        SELECT s.id_credito, s.fecha_corte, s.saldo_mxn, c.producto,
               c.id_credito IS NOT NULL AS coincide_catalogo
        FROM read_parquet(?) AS s
        LEFT JOIN catalogo AS c ON s.id_credito = c.id_credito
        ORDER BY s.fecha_corte, s.id_credito
    """, [str(archivo)]).fetchall()
assert len(unida) == 6
assert [f[3] for f in unida] == ["Personal", "Comercio", None] * 2
assert [f[4] for f in unida] == [True, True, False] * 2
assert [f[2] for f in unida] == [0, 2000, 2500, 100, 1900, 2600]
```

`WITH` nombra una tabla auxiliar; `AS s/c` abrevia nombres. `LEFT JOIN` conserva
créditos/cortes; una clave derecha repetida multiplicaría filas. Aquí las tres
claves son únicas por construcción; un catálogo real necesita validación completa,
como se desarrolló en [10.04](../04_types_missing_joins/README.md). `IS NOT NULL`
marca correspondencia, sin inventar un producto para 003. No entra 004 como
nuevo saldo. Esta unión no exige importar todo el Parquet primero a pandas.

## Práctica y criterio de salida

Realiza el [lab 10.06](../../../labs/10_polars_duckdb/06_duckdb_parquet/README.md).
Puedes explicar archivo/base/motor, ejecutar y conciliar selección/resumen,
identificar estimación frente a observación y detectar duplicados fuera del
filtro. Puedes justificar por qué leer varios archivos no basta para acreditar
claves únicas ni esquemas homogéneos.

No hay proyecto/checkpoint activo: `04_large_credit_dataset` sigue previsto
en [proyectos](../../../projects/README.md). Registra evidencia y dudas según
[PROGRESS.md](../../../PROGRESS.md); desarrollar material no acredita aprendizaje.

Siguiente: [10.07 — DuckDB desde Python y R](../07_duckdb_python_r/README.md).
Esta sección 10.06 no incorpora paquetes R ni modifica renv.

## Referencias primarias

Consultadas el 2026-10-23 y APIs ejecutadas con DuckDB 2.0.0. Se enlaza la
documentación de esa serie; los ejemplos y datos son propios.

- [Distribución Python 2.0.0](https://pypi.org/project/duckdb/2.0.0/).
- [Python/conexiones](https://duckdb.org/docs/2.0/clients/python/overview) y
  [DB API](https://duckdb.org/docs/2.0/clients/python/dbapi).
- [Parquet](https://duckdb.org/docs/2.0/data/parquet/overview),
  [varios archivos](https://duckdb.org/docs/2.0/data/multiple_files/overview) y
  [COPY](https://duckdb.org/docs/2.0/sql/statements/copy).
- [EXPLAIN](https://duckdb.org/docs/2.0/guides/meta/explain) y
  [EXPLAIN ANALYZE](https://duckdb.org/docs/2.0/guides/meta/explain_analyze).

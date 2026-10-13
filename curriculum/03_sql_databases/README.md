# 03 — SQL y bases de datos

## Propósito y prerrequisitos

Pasar de archivos a tablas relacionadas, consultar indicadores y comprobar
escrituras. Reutilizar el análisis de [pandas](../02_pandas/README.md), separando
qué se pregunta de cómo se expresa la consulta.

**Estado:** [01 — Modelo relacional y SQLite](01_relational_sqlite/README.md) y su
lab están disponibles, junto con [02 — Primeras consultas](02_first_queries/README.md)
y el lab 03.02. También están disponibles [03 — Crear tablas y cargar datos](03_create_load/README.md)
y el lab 03.03. [04 — Agregaciones e indicadores](04_aggregations/README.md)
y el lab 03.04 también están disponibles, junto con
[05 — Relacionar tablas con joins](05_joins/README.md) y su lab.
[06 — Subconsultas y CTE](06_subqueries_cte/README.md) y su lab también están disponibles.
[07 — Ventanas para comparar registros](07_windows/README.md) y su lab también están disponibles.
Las secciones 08–09 están planificadas; sus enlaces internos
describen el alcance previsto. Usamos SQLite y el módulo sqlite3 de Python; un
servidor PostgreSQL y una aplicación gráfica no son requisitos.

Se prevén tablas sintéticas de clientes, créditos y cortes. Antes de consultar
se explicará qué representa una fila: un crédito no es lo mismo que un registro
crédito/corte. Dinero en unidades explícitas y fechas con un formato acordado.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Modelo relacional y SQLite](01_relational_sqlite/README.md) | Esencial | Explicar tablas, relaciones y unidad de registro |
| 2 | [Primeras consultas](02_first_queries/README.md) | Esencial | Seleccionar, filtrar y ordenar datos |
| 3 | [Crear tablas y cargar datos](03_create_load/README.md) | Esencial | Construir una base con restricciones comprobadas |
| 4 | [Agregaciones e indicadores](04_aggregations/README.md) | Esencial | Obtener un resumen con denominadores claros |
| 5 | [Relacionar tablas con joins](05_joins/README.md) | Esencial | Unir datos conservando su cardinalidad |
| 6 | [Subconsultas y CTE](06_subqueries_cte/README.md) | Práctica | Dividir una consulta en pasos legibles |
| 7 | [Ventanas para comparar registros](07_windows/README.md) | Práctica | Comparar cortes sin perder el detalle |
| 8 | [Escrituras y transacciones](#08-escrituras-y-transacciones) | Esencial | Confirmar o revertir cambios de forma explícita |
| 9 | [Integración pandas y SQL](#09-integracion-pandas-y-sql) | Práctica de cierre | Conciliar un indicador entre herramientas |

## Alcance de cada sección

<a id="01-modelo-relacional-y-sqlite"></a>

### 01 — Modelo relacional y SQLite

- Base, tabla, fila, columna, clave primaria y foránea; relaciones uno a muchos.
- Diagrama pequeño de entidades y normalización básica para evitar inconsistencias.
  Práctica prevista: distinguir crédito, cliente y corte antes de escribir joins.

<a id="02-primeras-consultas"></a>

### 02 — Primeras consultas

- Conectar y cerrar explícitamente; consultar una base didáctica preparada.
  SELECT, FROM, WHERE, alias, ORDER BY, LIMIT y DISTINCT.
- NULL e IS NULL, lógica de condiciones y comparación con faltantes de pandas.
  Práctica prevista: recuperar un conjunto conocido; orden explícito cuando importe.

<a id="03-crear-tablas-y-cargar-datos"></a>

### 03 — Crear tablas y cargar datos

- CREATE TABLE, tipos de SQLite, PRIMARY KEY, NOT NULL, UNIQUE, CHECK y FOREIGN KEY.
  No asumir que declarar un tipo aplica todas las reglas del contrato.
- Activar y comprobar claves foráneas por conexión antes de las escrituras.
  INSERT y parámetros desde Python, sin interpolar valores en SQL; comprobar
  filas cargadas y rechazo de una relación inexistente.

<a id="04-agregaciones-e-indicadores"></a>

### 04 — Agregaciones e indicadores

- COUNT(*) frente a COUNT(columna), SUM, AVG, GROUP BY y HAVING; efecto de NULL.
- CASE y porcentajes con numerador/denominador definidos. Práctica prevista:
  conciliar un indicador por segmento y tratar el caso sin filas o denominador cero.

<a id="05-relacionar-tablas-con-joins"></a>

### 05 — Relacionar tablas con joins

- INNER JOIN y LEFT JOIN con condiciones explícitas; registros sin correspondencia.
- Detectar multiplicación de filas, no usar DISTINCT para esconder una unión
  incorrecta. Práctica prevista: comparar conteos y saldo antes y después del join.

<a id="06-subconsultas-y-cte"></a>

### 06 — Subconsultas y CTE

- Subconsultas, EXISTS y WITH para separar selección, agregación y presentación.
- Práctica prevista: expresar una misma pregunta de dos formas y comprobar
  resultados equivalentes. CTE recursivas quedan como profundización.

<a id="07-ventanas-para-comparar-registros"></a>

### 07 — Ventanas para comparar registros

- OVER, PARTITION BY, ORDER BY, ROW_NUMBER y LAG con una pregunta concreta.
- Diferenciar ventana y GROUP BY; ordenar empates y explicar el marco de un
  acumulado. Práctica prevista: comparar el saldo de un crédito entre cortes.

<a id="08-escrituras-y-transacciones"></a>

### 08 — Escrituras y transacciones

- UPDATE y DELETE sobre una copia de práctica; revisar previamente las filas
  afectadas. commit, rollback y límites de la transacción.
- Repetir una carga sin duplicar registros y comprobar persistencia al reconectar.
  Explicitar el control de transacciones de la versión Python utilizada; el bloque
  with de una conexión sqlite3 no sustituye el cierre de esa conexión.

<a id="09-integracion-pandas-y-sql"></a>

### 09 — Integración pandas y SQL

- Ejecutar consultas desde Python y recuperar tablas con pandas; mantener parámetros.
- Reconstruir una base sintética, conciliar al menos un indicador con pandas y
  reutilizar una gráfica. Conservar SQL, entradas y pasos de ejecución.

## Prácticas, proyecto y criterio de salida

Se prevén labs 03.01–03.09. El [lab 03.01](../../labs/03_sql_databases/01_relational_sqlite/README.md)
y el [lab 03.02](../../labs/03_sql_databases/02_first_queries/README.md)
y el [lab 03.03](../../labs/03_sql_databases/03_create_load/README.md)
y el [lab 03.04](../../labs/03_sql_databases/04_aggregations/README.md)
y el [lab 03.05](../../labs/03_sql_databases/05_joins/README.md)
y el [lab 03.06](../../labs/03_sql_databases/06_subqueries_cte/README.md)
y el [lab 03.07](../../labs/03_sql_databases/07_windows/README.md)
están disponibles; 03.08–03.09 están pendientes de desarrollo.
El proyecto previsto 02_credit_database aparece en [proyectos](../../projects/README.md);
su carpeta y checkpoints están por implementar.

Checkpoints propuestos: CP-01, esquema y carga (01–03); CP-02, indicadores y
relaciones (04–05); CP-03, consultas por pasos y comparación entre cortes (06–07);
CP-04, transacciones e integración reproducible (08–09).

Para avanzar necesitas demostrar diseño básico, consultas, uniones correctas,
escrituras controladas y conciliación pandas/SQL. CTE y ventanas se practican
con preguntas pequeñas; su profundización no bloquea el cierre esencial.
Índices y EXPLAIN QUERY PLAN se estudiarán ante una limitación medible.
PostgreSQL, administración de servidores y optimización avanzada quedan como extensiones.

## Continuidad y referencias

Comienza por [01 — Modelo relacional y SQLite](01_relational_sqlite/README.md)
y su lab. Después del cierre, continúa con
[04 — Visualización en Python](../04_visualization_python/README.md).

El diseño toma como referencia [el lenguaje SQL de SQLite](https://www.sqlite.org/lang.html),
[claves foráneas](https://www.sqlite.org/foreignkeys.html),
[funciones de ventana](https://www.sqlite.org/windowfunctions.html) y
[sqlite3 de Python](https://docs.python.org/3.12/library/sqlite3.html).

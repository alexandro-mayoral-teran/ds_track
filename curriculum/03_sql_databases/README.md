# 03 — SQL y bases de datos

[Inicio](../../README.md) / [Módulos](../README.md) / **03 — SQL y bases de datos**

**Organiza tablas relacionadas y responde preguntas con SQL.**

[**Empezar por 03.01 →**](01_relational_sqlite/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 9 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Pasar de archivos a tablas relacionadas, consultar indicadores y comprobar escrituras. Reutiliza un análisis conocido y distingue la pregunta de la consulta que la expresa.

## Antes de empezar

Completa [02 — pandas](../02_pandas/README.md). Se usa SQLite con sqlite3 de Python; no hace falta un servidor PostgreSQL ni una aplicación gráfica. Cada muestra distingue cliente, crédito y registro de crédito/corte.

## Qué vas a aprender

- Reconocer entidades, claves y relaciones.
- Seleccionar, agrupar y relacionar tablas con consultas.
- Construir indicadores y comparaciones con cobertura explícita.
- Controlar escrituras y transacciones.
- Conciliar resultados entre pandas y SQLite.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **03.01** · [Modelo relacional y SQLite](01_relational_sqlite/README.md) | [Lab 03.01](../../labs/03_sql_databases/01_relational_sqlite/README.md) | Explicar tablas, relaciones y unidad de registro |
| **03.02** · [Primeras consultas](02_first_queries/README.md) | [Lab 03.02](../../labs/03_sql_databases/02_first_queries/README.md) | Seleccionar, filtrar y ordenar datos |
| **03.03** · [Crear tablas y cargar datos](03_create_load/README.md) | [Lab 03.03](../../labs/03_sql_databases/03_create_load/README.md) | Construir una base con restricciones comprobadas |
| **03.04** · [Agregaciones e indicadores](04_aggregations/README.md) | [Lab 03.04](../../labs/03_sql_databases/04_aggregations/README.md) | Obtener un resumen con denominadores claros |
| **03.05** · [Relacionar tablas con joins](05_joins/README.md) | [Lab 03.05](../../labs/03_sql_databases/05_joins/README.md) | Unir datos conservando su cardinalidad |
| **03.06** · [Subconsultas y CTE](06_subqueries_cte/README.md) | [Lab 03.06](../../labs/03_sql_databases/06_subqueries_cte/README.md) | Dividir una consulta en pasos legibles |
| **03.07** · [Ventanas para comparar registros](07_windows/README.md) | [Lab 03.07](../../labs/03_sql_databases/07_windows/README.md) | Comparar cortes sin perder el detalle |
| **03.08** · [Escrituras y transacciones](08_transactions/README.md) | [Lab 03.08](../../labs/03_sql_databases/08_transactions/README.md) | Confirmar o revertir cambios de forma explícita |
| **03.09** · [Integración pandas y SQL](09_pandas_sql/README.md) | [Lab 03.09](../../labs/03_sql_databases/09_pandas_sql/README.md) | Conciliar un indicador entre herramientas |

<a id="alcance-de-cada-sección"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

<a id="01-modelo-relacional-y-sqlite"></a>

### 01 — Modelo relacional y SQLite

- Base, tabla, fila, columna, clave primaria y foránea; relaciones uno a muchos.
- Diagrama pequeño de entidades y normalización básica para evitar inconsistencias.
  Práctica: distinguir crédito, cliente y corte antes de escribir joins.

<a id="02-primeras-consultas"></a>

### 02 — Primeras consultas

- Conectar y cerrar explícitamente; consultar una base didáctica preparada.
  SELECT, FROM, WHERE, alias, ORDER BY, LIMIT y DISTINCT.
- NULL e IS NULL, lógica de condiciones y comparación con faltantes de pandas.
  Práctica: recuperar un conjunto conocido; orden explícito cuando importe.

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
- CASE y porcentajes con numerador/denominador definidos. Práctica:
  conciliar un indicador por segmento y tratar el caso sin filas o denominador cero.

<a id="05-relacionar-tablas-con-joins"></a>

### 05 — Relacionar tablas con joins

- INNER JOIN y LEFT JOIN con condiciones explícitas; registros sin correspondencia.
- Detectar multiplicación de filas, no usar DISTINCT para esconder una unión
  incorrecta. Práctica: comparar conteos y saldo antes y después del join.

<a id="06-subconsultas-y-cte"></a>

### 06 — Subconsultas y CTE

- Subconsultas, EXISTS y WITH para separar selección, agregación y presentación.
- Práctica: expresar una misma pregunta de dos formas y comprobar
  resultados equivalentes. CTE recursivas quedan como profundización.

<a id="07-ventanas-para-comparar-registros"></a>

### 07 — Ventanas para comparar registros

- OVER, PARTITION BY, ORDER BY, ROW_NUMBER y LAG con una pregunta concreta.
- Diferenciar ventana y GROUP BY; ordenar empates y explicar el marco de un
  acumulado. Práctica: comparar el saldo de un crédito entre cortes.

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

</details>

## Cómo trabajar este módulo

Empieza por la unidad de cada tabla y sus claves. Comprueba uniones y agregaciones con ejemplos pequeños antes de escribir datos. CTE y ventanas se practican gradualmente; administración de servidores, PostgreSQL e índices avanzados son extensiones.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Esquema y consultas | Claves, relaciones y pregunta respondida |
| Resultados conciliados | Conteos e indicadores frente a la referencia |
| Registro de transacciones | Escrituras y recuperación ante una operación fallida |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Puedes explicar un diseño relacional básico, consultar y unir sin duplicar indicadores y demostrar escrituras controladas. Reconstruye la referencia pandas/SQL y explica una discrepancia deliberada.

02_credit_database está previsto en [proyectos](../../projects/README.md); su carpeta y checkpoints siguen pendientes.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, esquema y carga (01–03); CP-02, indicadores y
relaciones (04–05); CP-03, consultas por pasos y comparación entre cortes (06–07);
CP-04, transacciones e integración reproducible (08–09).

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 03.01](01_relational_sqlite/README.md) y realiza su lab.

**Al cerrar:** continúa con [04 — Visualización en Python](../04_visualization_python/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

El diseño toma como referencia [el lenguaje SQL de SQLite](https://www.sqlite.org/lang.html),
[claves foráneas](https://www.sqlite.org/foreignkeys.html),
[funciones de ventana](https://www.sqlite.org/windowfunctions.html) y
[sqlite3 de Python](https://docs.python.org/3.12/library/sqlite3.html).

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_relational_sqlite/README.md)

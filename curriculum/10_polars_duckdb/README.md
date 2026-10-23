# 10 — Polars y DuckDB

## Propósito y prerrequisitos

Procesar los datos conocidos con otros motores, comprender sus formas de
ejecución y elegir con evidencia. Retoma los conceptos de
[09 — Arrow y Parquet](../09_arrow_parquet/README.md), contratos y referencias.
Las nuevas lecciones presentan su contexto, datos y resultados completos;
no exigen entregas personales anteriores para comprender los ejemplos.

**Estado:** [10.01 — Pregunta, contrato y referencia](01_question_contract_reference/README.md)
dispone de lección, muestra propia, referencias Python estándar/R base,
generador opcional y lab. [10.02 — Polars: tablas y expresiones](02_polars_tables_expressions/README.md)
añade lección, CSV autónomo, funciones, recorridos y lab con Polars 2.0.0.
[10.03 — Polars lazy y planes de consulta](03_polars_lazy_plans/README.md)
añade ejemplos autónomos, preparación Parquet, planes, ejecución conciliada y lab.
[10.04 — Tipos, faltantes y uniones](04_types_missing_joins/README.md)
añade ejemplos completos, catálogo propio, cobertura y cardinalidad con lab.
[10.05 — Streaming y límites de memoria](05_streaming_memory/README.md)
añade la extensión opcional de lotes, sink, plan físico y pico residente observado.
[10.06 — DuckDB: SQL sobre Parquet](06_duckdb_parquet/README.md)
añade DuckDB 2.0.0, SQL, planes y ejecución conciliada con lección/lab.
10.07–10.10 siguen planificadas: sus enlaces internos describen el alcance previsto.

Polars se enseñará principalmente desde Python, con su interfaz R como comparación
opcional. DuckDB se enseñará desde SQL, con recorridos separados para Python y R.
El objetivo no es repetir toda la teoría en cada lenguaje ni elegir un ganador
universal: verificaremos el resultado antes de comparar costos.

## Qué se compara

| Herramienta | Papel previsto |
| --- | --- |
| pandas / tidyverse | Análisis conocido y resultados de referencia |
| Polars | Expresiones sobre tablas, ejecución inmediata y consultas diferidas |
| DuckDB | Motor SQL analítico que se utiliza desde Python y R |
| Arrow / Parquet | Intercambio y almacenamiento comunes, introducidos en 09 |

Polars no es exclusivo de Python: existe una interfaz para R. No exigiremos
aprender ambas APIs para cerrar el módulo. DuckDB reutiliza conocimientos SQL;
DBI y el cliente R se explicarán antes de pedir una consulta desde ese lenguaje.

## Orden de desarrollo

| Orden | Sección | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta, contrato y referencia](01_question_contract_reference/README.md) | Esencial | Definir resultados equivalentes para comparar |
| 2 | [Polars: tablas y expresiones](02_polars_tables_expressions/README.md) | Esencial | Seleccionar, transformar y resumir una muestra |
| 3 | [Polars lazy y planes de consulta](03_polars_lazy_plans/README.md) | Esencial | Explicar scan, collect y un plan optimizado |
| 4 | [Tipos, faltantes y uniones](04_types_missing_joins/README.md) | Esencial | Conservar semántica e indicadores al cambiar de motor |
| 5 | [Streaming y límites de memoria](05_streaming_memory/README.md) | Extensión | Comprobar cómo se ejecuta una consulta por lotes |
| 6 | [DuckDB: SQL sobre Parquet](06_duckdb_parquet/README.md) | Esencial | Consultar archivos sin cargar primero todo en pandas |
| 7 | [DuckDB desde Python y R](#07-duckdb-desde-python-y-r) | Práctica | Reutilizar una consulta desde ambos lenguajes |
| 8 | [Intercambio entre motores](#08-intercambio-entre-motores) | Práctica | Verificar conversiones y materialización de resultados |
| 9 | [Comparar tiempo y memoria](#09-comparar-tiempo-y-memoria) | Práctica | Producir mediciones interpretables y repetibles |
| 10 | [Cierre y elección de herramienta](#10-cierre-y-eleccion-de-herramienta) | Práctica de cierre | Resolver una pregunta y justificar el motor elegido |

## Alcance de cada sección

<a id="01-pregunta-contrato-y-referencia"></a>

### 01 — Pregunta, contrato y referencia

- Definir entrada, corte, filtros, llaves, faltantes, unidades y resultado esperado.
  Separar costo de lectura, transformación y exportación.
- Disponible: [lección, muestra y referencias](01_question_contract_reference/README.md)
  y [lab 10.01](../../labs/10_polars_duckdb/01_question_contract_reference/README.md).
  Seis filas autónomas, pregunta/contrato, respuesta manual y comparación por
  ID/importe con Python estándar y contraste opcional R base. Generador
  determinista de hasta 1998 filas, con ejemplos de 40/400 y claves conservadas;
  conexión opcional con 28 filas incluidas, sin necesitar entregas anteriores.
  Vacíos, fronteras y errores compensados comprobados; no ejecuta motores,
  instala paquetes ni mide rendimiento. 10.02 inicia Polars.

<a id="02-polars-tablas-y-expresiones"></a>

### 02 — Polars: tablas y expresiones

- DataFrame, esquema, col, select, with_columns, filter y group_by/agg.
  Comparar las expresiones con pandas, sin trasladar mecánicamente sus índices.
- Disponible: [lección, muestra, funciones y recorridos](02_polars_tables_expressions/README.md)
  y [lab 10.02](../../labs/10_polars_duckdb/02_polars_tables_expressions/README.md).
  Seis observaciones completas, tipos explícitos y operaciones inmediatas;
  selección 003/2600, resumen por corte 4500/4600 MXN y derivada en miles.
  Esquema/valores conciliados con Python estándar; vacío, fronteras, errores
  compensados y suma Int64 comprobados. Escalas 40/400 y base común contrastadas.
  Polars 2.0.0 declarado, instalación y segunda reconstrucción uv locales;
  no introduce lazy, DuckDB ni mediciones de rendimiento.

<a id="03-polars-lazy-y-planes-de-consulta"></a>

### 03 — Polars lazy y planes de consulta

- DataFrame frente a LazyFrame; scan_parquet frente a lectura inmediata, collect
  y explain. Revisar proyección y filtros en el plan.
- Disponible: [lección, muestra, funciones y recorridos](03_polars_lazy_plans/README.md)
  y [lab 10.03](../../labs/10_polars_duckdb/03_polars_lazy_plans/README.md).
  Ejemplo autónomo en memoria y Parquet nuevo, esquema y planes sin optimizar/
  optimizado; dependencias de columnas, filtros/proyección y collect real.
  Seis filas, 003/2600 y resumen 4500/4600 MXN conciliados con CSV externo.
  Auditoría completa separada; vacío, fronteras, errores compensados y fuera
  del filtro comprobados. Sin dependencias nuevas ni mediciones de rendimiento;
  una consulta diferida no garantiza memoria acotada.

<a id="04-tipos-faltantes-y-uniones"></a>

### 04 — Tipos, faltantes y uniones

- Conversión y esquema; null frente a NaN, agregaciones y claves sin correspondencia.
  Tipos de join, cardinalidad y registros que pueden multiplicar el resultado.
- Disponible: [lección, fuentes, funciones y recorridos](04_types_missing_joins/README.md)
  y [lab 10.04](../../labs/10_polars_duckdb/04_types_missing_joins/README.md).
  Conversiones con originales, null/NaN y agregaciones con cobertura en muestras
  independientes. Seis saldos y catálogo de tres claves; left m:1 conserva
  4500/4600 MXN, distingue cuatro coincidencias/dos etiquetas conocidas sobre
  seis observaciones. Inner/semi/anti y full opcional, multiplicación, claves
  ausentes y diferencias pandas/SQL. Campos conciliados con Python estándar,
  pandas y SQLite; vacío, fronteras y duplicados sin uso comprobados.
  Sin dependencias nuevas ni mediciones de rendimiento.

<a id="05-streaming-y-limites-de-memoria"></a>

### 05 — Streaming y límites de memoria

- Ejecución por lotes, operaciones que retienen estado y salida materializada.
  Consultar soporte y comportamiento del motor para la versión elegida.
- Disponible como extensión opcional: [lección, muestra y scripts](05_streaming_memory/README.md)
  y [lab 10.05](../../labs/10_polars_duckdb/05_streaming_memory/README.md).
  Ejemplos autónomos de collect streaming, consumo de lotes sin lista y sink
  Parquet a destino nuevo; plan físico DOT sin Graphviz y trazas de ejecución.
  Seis filas, octubre uno/2600 o tres/4600 MXN conciliados por clave; vacío,
  fronteras, suma amplia y escalas 40/400/1998 comprobados. Procesos nuevos
  observan PeakWorkingSetSize en Windows, con auditoría fuera del trabajador.
  Sin dependencias nuevas, benchmark ni promesa de RAM acotada para todo el recorrido.

<a id="06-duckdb-sql-sobre-parquet"></a>

### 06 — DuckDB: SQL sobre Parquet

- read_parquet, filtros, agregaciones y joins; consultar varios archivos con el
  contrato de 09. EXPLAIN y EXPLAIN ANALYZE para relacionar consulta y ejecución.
- Disponible: [lección, muestra, SQL y ejecutor](06_duckdb_parquet/README.md)
  y [lab 10.06](../../labs/10_polars_duckdb/06_duckdb_parquet/README.md).
  Datos completos, preparación propia y conexión en memoria; selección 003/2600,
  resumen 4500/4600 MXN, unión pequeña y tipos SQL/HUGEINT comprobados.
  EXPLAIN frente a EXPLAIN ANALYZE; completo/partes con auditoría de cada
  esquema y todos los valores. DuckDB 2.0.0 declarado y dos entornos uv locales
  comprobados, registros previos conservados. Vacío, fronteras, duplicados
  fuera del filtro y saldos compensados; sin paquetes R ni benchmark.

<a id="07-duckdb-desde-python-y-r"></a>

### 07 — DuckDB desde Python y R

- Python: conexión, consultas parametrizadas y recuperación de resultados.
  R: DBI/duckdb, conexión, parámetros y cierre explícito.
- Práctica prevista: ejecutar la misma consulta en apartados separados y conciliar
  resultados. duckplyr/dbplyr serán alternativas opcionales, no requisitos iniciales.

<a id="08-intercambio-entre-motores"></a>

### 08 — Intercambio entre motores

- Conversiones entre pandas, Arrow, Polars y resultados DuckDB según las interfaces
  disponibles. Diferenciar entregar una consulta de materializar una tabla.
- Práctica prevista: comparar esquema y valores después de convertir, midiendo
  el costo si importa. No prometer intercambio sin copias para cualquier operación.
  Polars en R se ofrece como ampliación sobre este mismo ejemplo.

<a id="09-comparar-tiempo-y-memoria"></a>

### 09 — Comparar tiempo y memoria

- Datos y resultado equivalentes; versiones, hardware, hilos, caché, repeticiones
  y métricas de memoria con un método explícito. Contar la ejecución completa:
  preparar un plan lazy no equivale a ejecutarlo.
- Práctica prevista: medir lectura, consulta y exportación por separado y de extremo
  a extremo; conciliar antes de comparar. DuckDB puede usar disco temporal según
  operación y configuración: medir también ese costo cuando corresponda.

<a id="10-cierre-y-eleccion-de-herramienta"></a>

### 10 — Cierre y elección de herramienta

- Resolver el mismo problema con pandas, Polars y DuckDB; reutilizar la referencia R
  cuando ayude a comprobar semántica o interoperabilidad.
- Práctica prevista: entregar indicadores conciliados, mediciones y una decisión
  justificada por volumen, claridad, entorno y costos, incluyendo límites del experimento.

## Prácticas, proyecto y criterio de salida

Están disponibles los [labs 10.01](../../labs/10_polars_duckdb/01_question_contract_reference/README.md),
[10.02](../../labs/10_polars_duckdb/02_polars_tables_expressions/README.md),
[10.03](../../labs/10_polars_duckdb/03_polars_lazy_plans/README.md),
[10.04](../../labs/10_polars_duckdb/04_types_missing_joins/README.md),
[10.05](../../labs/10_polars_duckdb/05_streaming_memory/README.md)
y [10.06](../../labs/10_polars_duckdb/06_duckdb_parquet/README.md);
10.07–10.10 siguen previstos. 10.05 y Polars en R son opcionales.
El proyecto previsto 04_large_credit_dataset aparece en
[proyectos](../../projects/README.md), sin carpeta ni checkpoints implementados.

Checkpoints propuestos: CP-01, contrato y referencia (01); CP-02, consulta Polars
conciliada (02–04); CP-03, consulta DuckDB y lectura desde ambos lenguajes (06–08);
CP-04, mediciones y decisión documentada (09–10). Procesamiento mayor que memoria
ampliará CP-02/CP-03 solo con una necesidad y recursos adecuados.

Para avanzar debes explicar cuándo se ejecutan las consultas, conservar resultados
y justificar una comparación reproducible. No se exige demostrar que un motor
siempre gana, instalar servidores ni procesar un volumen que desborde tu equipo.
SQL avanzado, ajuste fino de hilos y particiones no bloquean el cierre esencial.

## Continuidad y referencias

Continúa con [11 — Reportes con Quarto](../11_reporting_quarto/README.md),
reutilizando tablas y figuras verificadas en lugar de recalcular sin controles.

- Polars: [ejecución lazy](https://docs.pola.rs/user-guide/lazy/using/),
  [optimizaciones](https://docs.pola.rs/user-guide/lazy/optimizations/),
  [faltantes](https://docs.pola.rs/user-guide/expressions/missing-data/) y
  [streaming](https://docs.pola.rs/user-guide/concepts/streaming/).
- [Interfaz R de Polars](https://pola-rs.github.io/r-polars/), como ampliación.
- DuckDB: [SQL sobre Parquet](https://duckdb.org/docs/current/data/parquet/overview),
  [cliente Python](https://duckdb.org/docs/current/clients/python/overview),
  [cliente R](https://duckdb.org/docs/current/clients/r) y
  [consideraciones de rendimiento](https://duckdb.org/docs/current/guides/performance/how_to_tune_workloads).

Las versiones, capacidades y dependencias se comprobarán al implementar cada
práctica; la investigación y planificación no instalan herramientas adicionales.
10.01 se comprueba con Python 3.12.12 y R 4.6.1 usando solo sus bibliotecas
estándar/base. 10.02 incorpora Polars 2.0.0 a pyproject/uv.lock y se comprueba
con Python 3.12.12 en dos entornos uv locales. Los registros previos del lockfile
se conservan; no cambia renv, Conda ni bibliotecas globales.
10.03 usa esos mismos entornos para comprobar planes y ejecución desde procesos
nuevos, sin añadir dependencias ni cambiar lockfiles.
10.04 conserva esos entornos, añade contraste con pandas 2.3.3/SQLite estándar
y verifica valores/tipos/cobertura sin nuevas dependencias ni archivos de entorno.
10.05 usa Polars 2.0.0 y biblioteca estándar para lotes, sink y observación
exploratoria del pico residente en procesos nuevos Windows; sin paquetes nuevos
ni cambios de configuración global. No mide rendimiento ni acredita RAM acotada.
10.06 incorpora DuckDB 2.0.0 a pyproject/uv.lock sin alterar otros registros
salvo la dependencia del proyecto; instalación y segunda reconstrucción local
desde caché comprobadas. No cambia entornos globales, Conda, renv ni venv raíz.

# 10 — Polars y DuckDB

## Propósito y prerrequisitos

Procesar los datos conocidos con otros motores, comprender sus formas de
ejecución y elegir con evidencia. Completa [09 — Arrow y Parquet](../09_arrow_parquet/README.md)
y reutiliza sus archivos, contrato e indicadores de referencia de pandas/SQL/R.

**Estado:** diez secciones planificadas; lecciones, ejemplos y labs por desarrollar.
Los enlaces internos describen el alcance previsto.

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

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta, contrato y referencia](#01-pregunta-contrato-y-referencia) | Esencial | Definir resultados equivalentes para comparar |
| 2 | [Polars: tablas y expresiones](#02-polars-tablas-y-expresiones) | Esencial | Seleccionar, transformar y resumir una muestra |
| 3 | [Polars lazy y planes de consulta](#03-polars-lazy-y-planes-de-consulta) | Esencial | Explicar scan, collect y un plan optimizado |
| 4 | [Tipos, faltantes y uniones](#04-tipos-faltantes-y-uniones) | Esencial | Conservar semántica e indicadores al cambiar de motor |
| 5 | [Streaming y límites de memoria](#05-streaming-y-limites-de-memoria) | Extensión | Comprobar cómo se ejecuta una consulta por lotes |
| 6 | [DuckDB: SQL sobre Parquet](#06-duckdb-sql-sobre-parquet) | Esencial | Consultar archivos sin cargar primero todo en pandas |
| 7 | [DuckDB desde Python y R](#07-duckdb-desde-python-y-r) | Práctica | Reutilizar una consulta desde ambos lenguajes |
| 8 | [Intercambio entre motores](#08-intercambio-entre-motores) | Práctica | Verificar conversiones y materialización de resultados |
| 9 | [Comparar tiempo y memoria](#09-comparar-tiempo-y-memoria) | Práctica | Producir mediciones interpretables y repetibles |
| 10 | [Cierre y elección de herramienta](#10-cierre-y-eleccion-de-herramienta) | Práctica de cierre | Resolver una pregunta y justificar el motor elegido |

## Alcance de cada sección

<a id="01-pregunta-contrato-y-referencia"></a>

### 01 — Pregunta, contrato y referencia

- Definir entrada, corte, filtros, llaves, faltantes, unidades y resultado esperado.
  Separar costo de lectura, transformación y exportación.
- Práctica prevista: un filtro y resumen sobre una muestra conocida; generar luego
  varias escalas sintéticas reproducibles sin exigir que superen la RAM disponible.

<a id="02-polars-tablas-y-expresiones"></a>

### 02 — Polars: tablas y expresiones

- DataFrame, esquema, col, select, with_columns, filter y group_by/agg.
  Comparar las expresiones con pandas, sin trasladar mecánicamente sus índices.
- Práctica prevista: reproducir un indicador conocido con operaciones nativas;
  evitar funciones Python por fila cuando una expresión resuelva la necesidad.

<a id="03-polars-lazy-y-planes-de-consulta"></a>

### 03 — Polars lazy y planes de consulta

- DataFrame frente a LazyFrame; scan_parquet frente a lectura inmediata, collect
  y explain. Revisar proyección y filtros en el plan.
- Práctica prevista: construir una consulta, inspeccionarla y después ejecutarla.
  Una consulta diferida no garantiza por sí sola procesamiento con memoria acotada.

<a id="04-tipos-faltantes-y-uniones"></a>

### 04 — Tipos, faltantes y uniones

- Conversión y esquema; null frente a NaN, agregaciones y claves sin correspondencia.
  Tipos de join, cardinalidad y registros que pueden multiplicar el resultado.
- Práctica prevista: conciliar con pandas/SQL, incluidos vacíos y claves repetidas;
  documentar diferencias semánticas antes de medir rendimiento.

<a id="05-streaming-y-limites-de-memoria"></a>

### 05 — Streaming y límites de memoria

- Ejecución por lotes, operaciones que retienen estado y salida materializada.
  Consultar soporte y comportamiento del motor para la versión elegida.
- Práctica prevista: ejecutar una consulta compatible, observar su plan y memoria
  y escribir una salida sin recoger un resultado enorme innecesariamente.
  Streaming no promete que cualquier consulta o resultado quepa en cualquier RAM.

<a id="06-duckdb-sql-sobre-parquet"></a>

### 06 — DuckDB: SQL sobre Parquet

- read_parquet, filtros, agregaciones y joins; consultar varios archivos con el
  contrato de 09. EXPLAIN y EXPLAIN ANALYZE para relacionar consulta y ejecución.
- Práctica prevista: obtener el mismo indicador directamente de Parquet y revisar
  proyección/filtros. Distinguir archivo Parquet de una base persistente .duckdb.

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

Se prevén labs 10.01–10.10; todavía no existen. 10.05 y Polars en R son opcionales.
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

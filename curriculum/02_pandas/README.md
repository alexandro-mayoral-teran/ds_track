# 02 — pandas

[Inicio](../../README.md) / [Módulos](../README.md) / **02 — pandas**

**Pasa de registros a tablas con reglas y resultados comprobables.**

[**Empezar por 02.01 →**](01_series_dataframe/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 10 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-punto-de-partida"></a>

## Propósito

Cargar, inspeccionar, seleccionar, transformar y resumir tablas con pandas. Empieza con ventas ficticias y después introduce una cartera sintética con diccionario de datos, sin presuponer conocimientos financieros.

## Antes de empezar

Completa [01 — Python fundamental](../01_python_foundations/README.md). Usa tu entorno de estudio; la primera lección explica cómo comprobar pandas y su versión de referencia. No necesitas preparar gráficos antes de esa lección.

## Qué vas a aprender

- Interpretar filas, columnas, índice y tipos.
- Seleccionar y transformar datos preservando sus originales.
- Justificar faltantes, duplicados y reglas de calidad.
- Combinar y resumir tablas conciliando claves, filas e indicadores.
- Reconstruir un análisis pequeño y explicar su primera gráfica.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **02.01** · [Series y DataFrame](01_series_dataframe/README.md) | [Lab 02.01](../../labs/02_pandas/01_series_dataframe/README.md) | Interpretar filas, columnas, índice y tipos |
| **02.02** · [Leer, inspeccionar y exportar](02_read_inspect_export/README.md) | [Lab 02.02](../../labs/02_pandas/02_read_inspect_export/README.md) | Cargar un CSV y verificar una salida |
| **02.03** · [Seleccionar, filtrar y ordenar](03_select_filter_sort/README.md) | [Lab 02.03](../../labs/02_pandas/03_select_filter_sort/README.md) | Responder una pregunta con un subconjunto |
| **02.04** · [Tipos y columnas calculadas](04_types_calculated_columns/README.md) | [Lab 02.04](../../labs/02_pandas/04_types_calculated_columns/README.md) | Convertir datos y calcular sin ciclos por fila |
| **02.05** · [Faltantes, duplicados y reglas](05_missing_duplicates_rules/README.md) | [Lab 02.05](../../labs/02_pandas/05_missing_duplicates_rules/README.md) | Conservar aceptados y rechazos con motivos |
| **02.06** · [Texto y fechas](06_text_dates/README.md) | [Lab 02.06](../../labs/02_pandas/06_text_dates/README.md) | Normalizar campos y comparar cortes |
| **02.07** · [Agrupar y resumir](07_group_summarize/README.md) | [Lab 02.07](../../labs/02_pandas/07_group_summarize/README.md) | Conciliar indicadores por segmento |
| **02.08** · [Combinar tablas](08_combine_tables/README.md) | [Lab 02.08](../../labs/02_pandas/08_combine_tables/README.md) | Unir datos sin multiplicar filas por accidente |
| **02.09** · [Cambiar la forma de una tabla](09_reshape_tables/README.md) | [Lab 02.09](../../labs/02_pandas/09_reshape_tables/README.md) | Pasar de formato largo a ancho y viceversa |
| **02.10** · [Análisis y primera gráfica](10_analysis_plot/README.md) | [Lab 02.10](../../labs/02_pandas/10_analysis_plot/README.md) | Reconstruir un análisis y explicar un hallazgo |

<a id="alcance-de-cada-sección"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

<a id="01-series-y-dataframe"></a>

### 01 — Series y DataFrame

- Crear una tabla desde una lista de diccionarios; distinguir Series y DataFrame.
- Leer shape, columnas, índice y dtypes. El índice no es automáticamente la clave
  de negocio. Práctica: reproducir las ventas y localizar un dato.

<a id="02-leer-inspeccionar-y-exportar"></a>

### 02 — Leer, inspeccionar y exportar

- read_csv, head, info y describe; revisar separador, codificación y tipos esperados.
- to_csv y control del índice exportado. Comparar filas, columnas y valores al
  volver a leer; introducir el diccionario de la muestra crediticia.

<a id="03-seleccionar-filtrar-y-ordenar"></a>

### 03 — Seleccionar, filtrar y ordenar

- Columnas, loc frente a iloc, máscaras booleanas, condiciones con paréntesis,
  sort_values y selección vacía. Explicar etiquetas frente a posiciones.
- Práctica: seleccionar un segmento y explicar cuántos registros conserva.

<a id="04-tipos-y-columnas-calculadas"></a>

### 04 — Tipos y columnas calculadas

- Conversión explícita, to_numeric, tipos que admiten faltantes y operaciones
  vectorizadas. Documentar qué ocurre con los valores que no se pueden convertir.
- Asignar con loc sobre el objeto previsto y estudiar copias y Copy-on-Write con
  la versión elegida; evitar asignación encadenada. Práctica: calcular y conciliar
  un importe o indicador con el ejemplo de Python estándar.

<a id="05-faltantes-duplicados-y-reglas"></a>

### 05 — Faltantes, duplicados y reglas

- isna, claves, duplicated y condiciones de validez; distinguir dato ausente,
  valor cero y conversión fallida. fillna y dropna solo con una decisión documentada.
- Práctica: una tabla de aceptados y otra de rechazos, conservando fuente
  y motivos; explicar qué significa duplicado antes de eliminarlo.

<a id="06-texto-y-fechas"></a>

### 06 — Texto y fechas

- Métodos str para espacios y categorías; to_datetime, fechas inválidas y
  componentes de fecha. Diferenciar fecha de corte y fecha de un evento.
- Práctica: normalizar un segmento y seleccionar un corte conocido,
  registrando los valores que no se pudieron interpretar.

<a id="07-agrupar-y-resumir"></a>

### 07 — Agrupar y resumir

- groupby y agg; contar filas frente a valores no faltantes, sumar y definir
  denominadores de porcentajes. Explicitar cómo tratar grupos con claves faltantes.
- Práctica: saldo y número de créditos por segmento, conciliando con
  el detalle. Ventanas rolling y acumulados serán ampliación posterior.

<a id="08-combinar-tablas"></a>

### 08 — Combinar tablas

- concat frente a merge; claves, inner/left, cardinalidad y registros sin coincidencia.
- validate e indicator para verificar una unión. Práctica: agregar un
  catálogo y demostrar que no se infló el saldo por claves repetidas.

<a id="09-cambiar-la-forma-de-una-tabla"></a>

### 09 — Cambiar la forma de una tabla

- melt, pivot y pivot_table; distinguir reorganizar de agregar. Comprobar qué
  combinación de claves identifica una celda y qué pasa si se repite.
- Práctica: comparar segmentos entre cortes conservando indicadores.

<a id="10-analisis-y-primera-grafica"></a>

### 10 — Análisis y primera gráfica

- Integrar carga, limpieza, resumen y exportación; notebook para explorar y
  funciones para reutilizar. Reiniciar y ejecutar desde cero.
- Introducir una figura sencilla con Matplotlib, unidades y explicación del hallazgo.
  Diseñar gráficos y Altair se profundizan en el módulo 04.

</details>

## Cómo trabajar este módulo

Lee el contrato de cada muestra antes de operar. Separa aceptados y rechazos y conserva cobertura de valores ausentes; no reemplaces por cero ni elimines duplicados sin una regla. MultiIndex, ventanas avanzadas y optimización son profundización, no condiciones para pasar a SQL.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Entradas, diccionario y reglas | Qué representa cada fila y qué se valida |
| Tablas y resúmenes | Conteos, claves, rechazos e indicadores conciliados |
| Código, gráfica e interpretación | Reconstrucción y explicación del análisis |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Puedes limpiar una muestra, justificar sus reglas y reconstruir el resultado con filas y totales conciliados. Explica qué muestra la gráfica y qué no se puede concluir de ella.

El proyecto 01_clean_credit_data sigue previsto en [proyectos](../../projects/README.md); su carpeta y checkpoints no están implementados.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, perfil y contrato de entrada (secciones 01–02);
CP-02, limpieza y rechazos (03–06); CP-03, indicadores y uniones verificadas
(07–09); CP-04, ejecución reproducible y primera figura (10). Estos nombres
se concretarán al desarrollar el proyecto, sin crear otra práctica obligatoria.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 02.01](01_series_dataframe/README.md) y realiza su lab.

**Al cerrar:** continúa con [03 — SQL y bases de datos](../03_sql_databases/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

La estructura adapta los [tutoriales introductorios de pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
al proyecto y a sus comprobaciones. Para desarrollar las secciones se consultarán
[las uniones](https://pandas.pydata.org/docs/user_guide/merging.html),
[Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) y
[los faltantes](https://pandas.pydata.org/docs/user_guide/missing_data.html).

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_series_dataframe/README.md)

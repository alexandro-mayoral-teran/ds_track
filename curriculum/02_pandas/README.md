# 02 — pandas

## Propósito y punto de partida

Pasar de listas de registros a tablas: cargar datos, seleccionar, transformar,
validar y resumir con pandas. Conservaremos las comprobaciones aprendidas en
[Python fundamental](../01_python_foundations/README.md).

**Estado:** la [lección 01 — Series y DataFrame](01_series_dataframe/README.md)
y su [lab 02.01](../../labs/02_pandas/01_series_dataframe/README.md) están disponibles.
Las secciones 02–10 están por desarrollar; sus enlaces describen el alcance previsto.

Primero reutilizaremos las ventas ficticias para comparar resultados con Python
estándar. Después introduciremos una cartera sintética con diccionario de datos:
qué representa cada fila, identificadores, fechas, unidades y significado del saldo.
No se presupone conocimiento financiero. La primera lección explica cómo preparar
pandas 2.3.3 en el entorno elegido; esa versión se declara en la configuración raíz.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Series y DataFrame](01_series_dataframe/README.md) | Esencial | Interpretar filas, columnas, índice y tipos |
| 2 | [Leer, inspeccionar y exportar](#02-leer-inspeccionar-y-exportar) | Esencial | Cargar un CSV y verificar una salida |
| 3 | [Seleccionar, filtrar y ordenar](#03-seleccionar-filtrar-y-ordenar) | Esencial | Responder una pregunta con un subconjunto |
| 4 | [Tipos y columnas calculadas](#04-tipos-y-columnas-calculadas) | Esencial | Convertir datos y calcular sin ciclos por fila |
| 5 | [Faltantes, duplicados y reglas](#05-faltantes-duplicados-y-reglas) | Esencial | Conservar aceptados y rechazos con motivos |
| 6 | [Texto y fechas](#06-texto-y-fechas) | Esencial | Normalizar campos y comparar cortes |
| 7 | [Agrupar y resumir](#07-agrupar-y-resumir) | Esencial | Conciliar indicadores por segmento |
| 8 | [Combinar tablas](#08-combinar-tablas) | Esencial | Unir datos sin multiplicar filas por accidente |
| 9 | [Cambiar la forma de una tabla](#09-cambiar-la-forma-de-una-tabla) | Práctica | Pasar de formato largo a ancho y viceversa |
| 10 | [Análisis y primera gráfica](#10-analisis-y-primera-grafica) | Práctica de cierre | Reconstruir un análisis y explicar un hallazgo |

## Alcance de cada sección

<a id="01-series-y-dataframe"></a>

### 01 — Series y DataFrame

- Crear una tabla desde una lista de diccionarios; distinguir Series y DataFrame.
- Leer shape, columnas, índice y dtypes. El índice no es automáticamente la clave
  de negocio. Práctica prevista: reproducir las ventas y localizar un dato.

<a id="02-leer-inspeccionar-y-exportar"></a>

### 02 — Leer, inspeccionar y exportar

- read_csv, head, info y describe; revisar separador, codificación y tipos esperados.
- to_csv y control del índice exportado. Comparar filas, columnas y valores al
  volver a leer; introducir el diccionario de la muestra crediticia.

<a id="03-seleccionar-filtrar-y-ordenar"></a>

### 03 — Seleccionar, filtrar y ordenar

- Columnas, loc frente a iloc, máscaras booleanas, condiciones con paréntesis,
  sort_values y selección vacía. Explicar etiquetas frente a posiciones.
- Práctica prevista: seleccionar un segmento y explicar cuántos registros conserva.

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
- Práctica prevista: una tabla de aceptados y otra de rechazos, conservando fuente
  y motivos; explicar qué significa duplicado antes de eliminarlo.

<a id="06-texto-y-fechas"></a>

### 06 — Texto y fechas

- Métodos str para espacios y categorías; to_datetime, fechas inválidas y
  componentes de fecha. Diferenciar fecha de corte y fecha de un evento.
- Práctica prevista: normalizar un segmento y seleccionar un corte conocido,
  registrando los valores que no se pudieron interpretar.

<a id="07-agrupar-y-resumir"></a>

### 07 — Agrupar y resumir

- groupby y agg; contar filas frente a valores no faltantes, sumar y definir
  denominadores de porcentajes. Explicitar cómo tratar grupos con claves faltantes.
- Práctica prevista: saldo y número de créditos por segmento, conciliando con
  el detalle. Ventanas rolling y acumulados serán ampliación posterior.

<a id="08-combinar-tablas"></a>

### 08 — Combinar tablas

- concat frente a merge; claves, inner/left, cardinalidad y registros sin coincidencia.
- validate e indicator para verificar una unión. Práctica prevista: agregar un
  catálogo y demostrar que no se infló el saldo por claves repetidas.

<a id="09-cambiar-la-forma-de-una-tabla"></a>

### 09 — Cambiar la forma de una tabla

- melt, pivot y pivot_table; distinguir reorganizar de agregar. Comprobar qué
  combinación de claves identifica una celda y qué pasa si se repite.
- Práctica prevista: comparar segmentos entre cortes conservando indicadores.

<a id="10-analisis-y-primera-grafica"></a>

### 10 — Análisis y primera gráfica

- Integrar carga, limpieza, resumen y exportación; notebook para explorar y
  funciones para reutilizar. Reiniciar y ejecutar desde cero.
- Introducir una figura sencilla con Matplotlib, unidades y explicación del hallazgo.
  Diseñar gráficos y Altair se profundizan en el módulo 04.

## Prácticas, proyecto y criterio de salida

Se prevé un lab por sección (02.01–02.10), con soluciones desplegables y
comprobaciones conocidas. El lab 02.01 está disponible; 02.02–02.10 están pendientes.
El proyecto previsto es 01_clean_credit_data, registrado en
[proyectos](../../projects/README.md), aún sin carpeta implementada.

Checkpoints propuestos: CP-01, perfil y contrato de entrada (secciones 01–02);
CP-02, limpieza y rechazos (03–06); CP-03, indicadores y uniones verificadas
(07–09); CP-04, ejecución reproducible y primera figura (10). Estos nombres
se concretarán al desarrollar el proyecto, sin crear otra práctica obligatoria.

Podrás cerrar el módulo al limpiar una muestra, justificar las reglas, conciliar
filas y totales, reconstruir el resultado y explicar una gráfica. No es necesario
dominar MultiIndex, optimización o ventanas avanzadas para pasar a SQL.

## Continuidad y referencias

Comienza por la [lección 01](01_series_dataframe/README.md) y su lab. Después del cierre, continúa con
[03 — SQL y bases de datos](../03_sql_databases/README.md).

La estructura adapta los [tutoriales introductorios de pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
al proyecto y a sus comprobaciones. Para desarrollar las secciones se consultarán
[las uniones](https://pandas.pydata.org/docs/user_guide/merging.html),
[Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) y
[los faltantes](https://pandas.pydata.org/docs/user_guide/missing_data.html).

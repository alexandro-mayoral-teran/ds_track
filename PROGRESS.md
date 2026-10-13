# Progreso de aprendizaje

Este archivo registra dónde estamos y qué sigue. El plan completo vive en
[`ROADMAP.md`](ROADMAP.md); aquí solo se actualiza el avance real.

## En este momento

- **Módulo activo de desarrollo:** `04_visualization_python`
- **Estado:** en curso
- **Sesión de desarrollo:** 2026-10-13, sección 04.05 disponible con lección y lab.
  El módulo 04 continúa en desarrollo.
- **Foco de desarrollo del material:** escalas, etiquetas, cobertura y accesibilidad.
  Próxima sección por implementar:
  [04.06 — Composición y exportación](curriculum/04_visualization_python/README.md#06-composicion-y-exportacion).
- **Estado del contenido:** nivel 0 disponible y las seis lecciones de Python
  fundamental con sus labs. Esto no acredita finalización del estudiante.
  Los módulos 02–05 tienen un plan de 39 secciones. Las diez de pandas y sus
  labs están disponibles; también SQL 03.01–03.09 con base local y labs.
  04.01–04.05 tienen lecciones y labs; 04.06–04.09 y el módulo 05 están por desarrollar. Los módulos 06–08 tienen
  un plan adicional de 28 secciones y lecturas abiertas. Los módulos 09–10 tienen
  19 secciones planificadas y 11–14 añaden 37. La planificación de 02–14 está
  detallada; 02.01–02.10 ya disponen de lección y lab dentro de esos módulos.
- **Referencia de estudio, pendiente de evidencia:** leer la
  [lección de modelo relacional y SQLite](curriculum/03_sql_databases/01_relational_sqlite/README.md) y realizar
  el [lab 03.01](labs/03_sql_databases/01_relational_sqlite/README.md), después de
  completar las prácticas previas.

### Para retomar el desarrollo

El último material disponible es
[04.05 — Escalas, etiquetas y accesibilidad](curriculum/04_visualization_python/05_scales_labels_accessibility/README.md)
con su [lab](labs/04_visualization_python/05_scales_labels_accessibility/README.md).
Las secciones 04.06–04.09 aún son planes. Retomar con 04.06: vistas múltiples,
ejes comparables, anotaciones, tamaño, resolución y exportación PNG/SVG.
Reutilizar las figuras y las tablas comprobadas de 04.02–04.05.

Los proyectos y checkpoints asociados siguen pendientes. No se cambió el
estado del estudiante sin evidencia de las prácticas.

## Estados

- `No iniciado`: todavía no se trabaja el módulo.
- `En curso`: existe trabajo activo, aunque falten actividades.
- `En pausa`: se conserva el avance, pero no es el foco actual.
- `Completado`: se alcanzó el criterio de salida definido en el roadmap.

## Avance por módulo

Esta tabla registra el aprendizaje del estudiante según sus evidencias;
la disponibilidad del material se resume arriba y no modifica estos estados.

| Nivel | Módulo | Estado | Evidencia de finalización |
| --- | --- | --- | --- |
| 00 | Entorno de aprendizaje | En curso | Pendiente |
| 01 | Python fundamental | No iniciado | — |
| 02 | pandas | No iniciado | — |
| 03 | SQL y bases de datos | No iniciado | — |
| 04 | Visualización en Python | No iniciado | — |
| 05 | Python aplicado | No iniciado | — |
| 06 | R fundamental | No iniciado | — |
| 07 | tidyverse | No iniciado | — |
| 08 | Visualización en R | No iniciado | — |
| 09 | Arrow y Parquet | No iniciado | — |
| 10 | Polars y DuckDB | No iniciado | — |
| 11 | Reportes con Quarto | No iniciado | — |
| 12 | Streamlit | No iniciado | — |
| 13 | Shiny y fundamentos web | No iniciado | — |
| 14 | Proyecto reproducible | No iniciado | — |

## Bitácora

### 2026-10-13

- Se desarrolló 04.05: límites y origen de barras, escala lineal/logarítmica,
  exclusiones trazables, unidades, cobertura, formas/tramas y descripción textual.
  Incluye cuatro figuras, cinco CSV reconstruibles y lab con soluciones razonadas.
  Se verificaron medianas contra los CSV originales, coordenadas, ceros, ausencias,
  vacíos, partición log y conservación de fuentes/salidas. Runtime local: pandas
  2.3.3 y Matplotlib 3.10.6; referencia 3.10.7 conservada. Sigue 04.06;
  la disponibilidad del material no acredita aprendizaje del estudiante.

- Se cerró la sesión con revisión documental: índices generales, navegación de
  visualización y punto de retorno a 04.05. Se completó el índice de labs SQL
  03.03–03.09 y se distinguieron material disponible, planes y evidencias del
  estudiante. Se comprobaron enlaces locales y fragmentos de los 109 documentos
  Markdown versionados fuera de las plantillas, junto con git diff --check.
  AGENTS.md permanece local e ignorado; no se versionan salidas de práctica.

- Se desarrolló 04.04: histogramas e intervalos, cuartiles/cajas/bigotes, valores
  exteriores y dispersión con pares conocidos, sin atribución causal. Incluye
  cuatro figuras, script con siete tablas de comprobación y lab con soluciones.
  Se verificaron frecuencias, cuartiles, coordenadas, exclusiones, fronteras,
  vacíos, ausencias/cero, exportaciones y fuentes intactas. Runtime local:
  pandas 2.3.3 y Matplotlib 3.10.6; referencia 3.10.7 conservada. Sigue 04.05;
  el material disponible no acredita aprendizaje.

### 2026-10-12

- Se desarrolló 04.03: barras agrupadas, medidas y denominadores, fechas, pares
  comparables y huecos sin imputación, con tres figuras y lab razonado. Se
  comprobaron sumas, tasas, pares, cero/ausencia, calendario, exportaciones y
  entradas intactas con pandas 2.3.3 y Matplotlib 3.10.6 locales; referencia
  Matplotlib 3.10.7 conservada. Sigue 04.04; el estudiante requiere evidencia.

- Se desarrolló 04.02: Figure/Axes/Axis, interfaz explícita, dibujo reutilizable,
  guardado y cierre, con resumen derivado de SQL, figuras y lab. Se verificaron
  ausencia/cero/vacío, aislamiento de figuras y conservación de entradas/salidas
  con pandas 2.3.3 y Matplotlib 3.10.6 locales, manteniendo referencia 3.10.7.
  El siguiente desarrollo es 04.03; el aprendizaje requiere evidencia.

- Se desarrolló 04.01: pregunta, público, población, unidad y medida; elección
  entre categorías, tiempo, distribución y relación. Se añadieron vistas propias
  con bases comprobadas, ficha y lab; la regeneración es opcional. Se revisaron
  figuras, ausencias, vacíos y conservación de entradas, con las bibliotecas locales
  disponibles. El siguiente desarrollo es 04.02; el aprendizaje requiere evidencia.

- Se desarrolló SQL 03.09: base reconstruible, read_sql_query parametrizado,
  referencia independiente desde CSV/pandas, tipos y conciliación de detalle/grupos;
  exportaciones recargadas y figura con cobertura. SQL tiene nueve lecciones y labs;
  el estudiante aún requiere evidencias. El siguiente desarrollo es 04.01.
  Se verificó con pandas 2.3.3 y Matplotlib 3.10.6 disponibles, contrastando la API
  de referencia 3.10.7; no se modificó el entorno local incompleto ni las dependencias.

- Se desarrolló SQL 03.08: copia separada, UPDATE/DELETE con selección previa,
  control explícito, commit/rollback, carga repetible y conflictos; lección amplia
  y lab con SAVEPOINT opcional. Se comprobó persistencia, reversión de lotes,
  relaciones, archivos existentes y conservación de fuentes. El siguiente
  desarrollo es 03.09; la disponibilidad del material no acredita aprendizaje.

- Se desarrolló SQL 03.07: OVER, particiones, ROW_NUMBER, LAG y marcos, con
  explicación gradual, diagramas y lab. Se comprobó la comparación de 19 pares
  conocidos, selección con empates, vacíos, huecos temporales y base cero;
  también se conciliaron acumulados y cobertura conservando las fuentes.
  El siguiente desarrollo es 03.08; el aprendizaje requiere evidencia.

- Se desarrolló SQL 03.06 con explicación gradual de subconsultas escalares, IN,
  EXISTS/NOT EXISTS, correlación, tablas derivadas y CTE por etapas; lab amplio
  con equivalencia y referencias globales/por grupo. Se contrastaron resultados
  con los CSV y se comprobaron NULL, vacíos y conservación de fuentes.
  El siguiente desarrollo es 03.07; el aprendizaje requiere evidencia.

- Se completó SQL 03.05: INNER/LEFT JOIN, cardinalidad, ON/WHERE, antiunión y
  claves compuestas, con diagramas, resumen regional y lab. Se conciliaron
  claves y valores contra los CSV y se verificaron casos sin correspondencia,
  multiplicación y vacíos conservando las entradas. El siguiente desarrollo
  es 03.06; la disponibilidad del material no acredita aprendizaje.

- Se desarrolló SQL 03.04: COUNT/SUM/AVG, grupos, HAVING, CASE, tasas y cobertura,
  con script de solo lectura y detalle temporal por segmento. Se conciliaron
  ocho grupos contra cálculos Python sobre los CSV y se comprobaron vacíos,
  desconocidos, cero y frontera 30. El siguiente desarrollo es 03.05;
  el borrador local de joins aún no está publicado ni cuenta como material disponible.

- Se desarrolló SQL 03.03: esquema, tipos y restricciones, INSERT con parámetros,
  carga desde los CSV existentes y lab con soluciones. Se comprobaron rechazos,
  persistencia, repetición sin cambios y conservación de entradas. El siguiente
  desarrollo es 03.04; el aprendizaje sigue pendiente de evidencia.

- Se desarrolló SQL 03.02: SELECT, filtros, alias, orden y desempates, LIMIT,
  DISTINCT, NULL y parámetros; script de solo lectura y lab con resultados conocidos.
  Se comprobó conservación de la base, fronteras y selecciones vacías. El siguiente
  desarrollo es 03.03; el avance del estudiante sigue pendiente de evidencia.

### 2026-10-11

- Se desarrolló SQL 03.01: modelo relacional, claves y relaciones con diagramas;
  base local de 16 clientes, 24 créditos y 48 cortes ficticios. Se verificaron
  restricciones, persistencia, repetición sin cambios y exploración de solo lectura.

- Se desarrolló pandas 02.10: análisis integrado, rechazos trazables, resumen
  conciliado, primera figura Matplotlib y notebook con funciones compartidas.
  Se completó el material de diez lecciones/labs; el aprendizaje requiere evidencia.

- Se desarrolló pandas 02.09: pivot, melt y pivot_table, con diagramas y
  conservación de presencia para distinguir celdas ausentes de importes desconocidos.
  Se verificó la vuelta exacta y el resumen por corte; se agregó lab y navegación.

- Se desarrolló pandas 02.08: concat, tipos de merge, validate, indicator y
  comparación por ID sobre una base común. Tres diagramas Mermaid explican las
  operaciones y la multiplicación de filas; se agregó lab con comprobaciones.

- Se desarrolló pandas 02.07 con 48 observaciones: groupby/agg, size/count/nunique,
  grupos con NA, cobertura y tasas con bases explícitas. Los 10 grupos se verificaron
  contra cálculos independientes; se agregó lab y transform como ampliación.

- Se desarrolló pandas 02.06 con 48 registros de dos cortes: normalización
  trazable, formatos temporales explícitos, NaT, relaciones de fechas y claves
  posteriores a la limpieza. Se agregó lab y comparación de períodos comprobada.

- Se desarrolló pandas 02.05: 44 registros sintéticos, reglas explícitas, claves
  repetidas apartadas para revisión y múltiples motivos por registro. El script
  concilia la partición y comprueba exportaciones; se agregó lab y navegación.

- Se desarrolló pandas 02.04 con 40 filas sintéticas: conversión trazable, tipos
  nullable, operaciones entre columnas, asignación con loc y conciliación sobre
  la misma base. Se agregó el lab con soluciones desplegables y navegación.

- Se desarrolló pandas 02.03: loc/iloc, máscaras, condiciones combinadas, NA,
  orden y desempates, con selección vacía y exportación comprobada. Se agregó
  el lab y se conservó la fuente de la lección anterior.

- Se desarrolló pandas 02.02 con muestra crediticia ficticia y diccionario: lectura
  tipada, head/info/describe, exportación y comparación de la tabla recargada.
  Se agregó su lab y se enlazó desde la primera lección.

- Se depuraron las instrucciones locales de agentes, separando reglas vigentes
  de historial. Se crearon plantillas generales de agentes y arquitectura, con
  instrucciones para copiarlas y adaptarlas a proyectos de otros temas.
- Se revisaron las instrucciones locales y el roadmap: estado real de pandas,
  alcances opcionales, proyectos aún por implementar y pendientes de R aplicado
  y terminal avanzada. Se alineó el flujo de estudio con checkpoints opcionales.

- Se investigaron y definieron Quarto (9 secciones), Streamlit (9), Shiny (10)
  y proyecto reproducible (9). El recorrido numerado completo tiene planes
  detallados; se retoma la implementación por pandas 02.02 en la siguiente sesión.

- Se investigaron fuentes oficiales y se organizaron Arrow/Parquet (9 secciones)
  y Polars/DuckDB (10), con intercambio Python/R, consultas verificables y mediciones.
  Se mantuvo la numeración y se separaron particiones y streaming como ampliaciones.

- Se investigaron libros abiertos de Hadley Wickham y documentación oficial para
  definir R fundamental (9 secciones), tidyverse (10) y visualización R (9).
  Se agregó una guía de lecturas y se mantuvo pendiente la numeración de R aplicado.

- Se desarrolló 02.01 — Series y DataFrame, con script y lab; pandas 2.3.3 se
  declaró en pyproject.toml y se resolvió en uv.lock. Se verificó el ejemplo
  en un entorno aislado y se actualizaron navegación y arquitectura.

- Se investigó documentación oficial y se organizaron las secciones de pandas (10),
  SQL (9), visualización Python (9) y Python aplicado (11), con prácticas y cierres
  propuestos. Se distinguió el recorrido esencial de las ampliaciones opcionales.
- Se desarrolló la lección 06 de Python fundamental y su lab: reglas, excepciones,
  rechazos trazables y resumen conciliado. El módulo dispone de seis lecciones;
  la finalización del aprendizaje sigue pendiente de evidencias.

- Se desarrolló la lección 05 de Python fundamental y su lab: lectura CSV,
  conversión, escritura y comprobación de registros e importes, conservando la entrada.
- Se revisaron las instrucciones locales, la arquitectura y los diagramas:
  flujo lección/lab, avances de contenido y diferencia entre muestras iniciales
  de ventas y dominio crediticio posterior.
- Se desarrolló la lección 04 de Python fundamental y su lab: parámetros,
  retorno, alcance y reutilización de filtros y resúmenes.
- Se desarrolló la lección 03 de Python fundamental: condiciones, recorrido,
  acumuladores y selección de registros, con script y lab verificables.
- Se desarrolló la lección 02 de Python fundamental y su lab: listas,
  diccionarios, registros, mutabilidad y copias.
- Se inició Python fundamental con la lección y lab de variables, tipos y
  operaciones. Se registró R aplicado como consideración para la próxima revisión.
- Se integraron las rutas en un flujo numerado 00–14; visualización y Python aplicado
  ahora tienen ubicación y prerrequisitos, con Streamlit/Shiny como elección de aplicación.

- Se revisó el track completo: comunicación y calidad tempranas, cierre integrado
  antes de R y separación de contenidos esenciales y avanzados sin renumerar niveles.
- Se creó la lección 06, el notebook de ejemplo y su lab: selección de kernel,
  celdas, estado en memoria y ejecución desde cero.
- Se dividió la lección 05 en dos sesiones: preparación del entorno y gestión
  de dependencias, con teoría específica de requirements.txt y archivos de configuración.
- Se separó la teoría de entornos de tres recorridos prácticos: Conda, venv + pip
  y uv, con una demostración común de instalación e importación de una biblioteca.
- Se adaptó la lección 05 a Anaconda/Conda como recorrido principal, con uv como
  alternativa y un solo entorno requerido en el lab.
- Se creó la lección 05 y su lab: intérpretes, venv, pip y entorno del proyecto
  con uv, conservando recorridos por shell y soluciones desplegables.
- Se desarrollaron las primeras tres lecciones y sus labs, con explicaciones
  por pasos y soluciones desplegables.
- Se preparó la lección 04 y un primer script sin paquetes externos; la
  preparación del entorno queda para la lección 05.
- Se creó el repositorio privado de DS Track y se publicó el material inicial.
- Se incorporó el perfil de GitHub como práctica inicial del nivel 0, con
  Markdown y actualización desde Git. La práctica de terminal se conserva.
- Se alineó la numeración con el orden de estudio y se agregó una plantilla
  editable para el README del perfil.
- Se separaron las lecciones 01 y 03: creación desde la web y actualización con
  Git, cada una con su propio documento y lab.

### 2026-10-08

- Se definió la arquitectura del repositorio.
- Se creó el roadmap por niveles.
- Se prepararon plantillas para módulos y proyectos.
- Se estableció la política de datos sintéticos.
- Se inició el módulo `00_getting_started`.
- Se creó la primera lección y su lab sobre terminal, rutas y entorno.
- Se agregaron equivalencias PowerShell–Unix para preparar el uso de Git,
  servidores y entornos de nube.

## Cómo actualizar este archivo

Al terminar una sesión:

1. Actualiza el siguiente paso con una acción pequeña y concreta.
2. Registra uno o dos resultados en la bitácora, no cada comando ejecutado.
3. Cambia un módulo a `Completado` solo cuando exista evidencia de su criterio
   de salida.
4. Enlaza la evidencia: ejercicio, script, notebook, reporte o proyecto.

# Arquitectura del repositorio

La arquitectura separa enseñanza, práctica, integración y publicación. Esto
evita que un notebook aislado tenga que funcionar al mismo tiempo como lección,
ejercicio, solución y producto final.

Las [plantillas para nuevos proyectos](../templates/learning-project/README.md)
separan instrucciones de agentes y método de diseño del recorrido. Esta
arquitectura documenta su aplicación específica a DS Track.

## Flujo del conocimiento

```text
lección → lab asociado → comprobar y explicar → evidencia → PROGRESS.md
   ↑          │
   └──────────┴── siguiente lección

cuando corresponda: lab → checkpoint de proyecto → resultado → showcase
datos de entrada: muestras de la lección o datasets
```

Las reglas concretas de conexión están en
[`learning-workflow.md`](learning-workflow.md).

## Responsabilidad de cada área

### `curriculum/`

Contenido secuencial. Explica conceptos y presenta ejemplos mínimos. Los
módulos están numerados porque tienen prerrequisitos deliberados.

### `labs/`

Práctica breve. Un lab debe poder terminarse sin construir un proyecto entero y
debe declarar qué módulo refuerza.

### `projects/`

Integra varias capacidades alrededor de una pregunta o producto. Cada proyecto
es autocontenido y debe documentar entradas, transformaciones y salidas.

### `datasets/`

Contiene únicamente muestras pequeñas, datos sintéticos, generadores y
diccionarios. Los datos de trabajo voluminosos se regeneran localmente y no se
versionan.

### `templates/`

Reduce decisiones repetidas. Aquí viven las estructuras base para crear nuevos
módulos, proyectos, reportes o aplicaciones.

### `showcase/`

Contiene resultados terminados y seguros para compartir: reportes renderizados,
capturas, demostraciones o enlaces. No es un directorio de trabajo.

## Dependencias

Python usa un `pyproject.toml` y un `uv.lock` en la raíz. Esa configuración
describe el recorrido alternativo con uv. Para quienes ya usan Anaconda, la
lección 05 enseña Conda como recorrido principal y cómo exportar su configuración;
los archivos de uv no describen automáticamente un entorno Conda.
El proyecto declara pandas 2.3.3 desde la lección 02.01; uv.lock conserva sus
dependencias resueltas. Conda y pip preparan la misma versión de referencia según
su recorrido. El mini proyecto uv del nivel 0 sigue siendo una práctica separada. R adoptará `renv` dentro del material de R cuando se introduzca
reproducibilidad. No se crearán entornos independientes por cada ejercicio salvo
que exista una incompatibilidad concreta.

## Datos del recorrido

Las primeras lecciones de Python utilizan ventas ficticias pequeñas para aprender
sin introducir vocabulario de otro dominio. La lección 05 conecta lectura CSV,
conversión y escritura; la 06 desarrolla validación y resumen con rechazos y controles explícitos. Después, el
dominio común será una cartera crediticia completamente sintética. Su escala
crecerá de manera intencional:

1. CSV pequeño para Python y pandas.
2. Varias tablas para SQL.
3. Histórico de cortes para R y visualización.
4. Dataset Parquet particionado para Polars y DuckDB.
5. Tablas analíticas para Quarto y Shiny.

## Rutas de profundización previstas

El recorrido se reorganiza en niveles 00–14 para integrar estas capacidades
con prerrequisitos visibles. El nivel 00 tiene sus seis lecciones y labs;
el nivel 01 tiene sus seis lecciones y labs, incluyendo validación y resumen. SQL dispone de sus nueve lecciones y labs con base local, integración y gráfica;
los niveles 04–14 conservan planificación, salvo 04.01–04.05, disponibles con lecciones y labs;
pandas dispone de sus diez lecciones y labs, con notebook y gráfica de cierre. Python aplicado
está después de pandas, SQL y visualización básica: no bloquea el inicio de pandas.

### Desarrollo previsto de los módulos 02–05

Los README de cada módulo contienen el orden numerado y el alcance de cada
sección. Los módulos 02 y 03 disponen de sus lecciones y labs; 04.01–04.05 están disponibles con lecciones y labs; las demás secciones de 04–05
conservan planes de desarrollo. pandas 02.10 también dispone de notebook.
SQL 03.01 tiene diagrama relacional, esquema
preparado y tres CSV que generan una base SQLite local. SQL 03.02 consulta esa
base en solo lectura, con filtros, orden, parámetros y tratamiento de NULL; usa sqlite3 estándar, sin
servidor ni nuevas dependencias. La exploración se hace en solo lectura y la
preparación comprueba bases existentes sin reiniciarlas.
SQL 03.03 construye una base de práctica separada desde las mismas fuentes,
comprueba restricciones en memoria y conserva bases existentes en solo lectura.
SQL 03.04 resume fechas y segmentos con conteos, agregados, CASE y bases
explícitas; consulta el archivo en solo lectura y construye un detalle en memoria
mediante claves en Python para no adelantar joins SQL. Comprueba resultados
contra cálculos independientes sobre los CSV, incluyendo vacíos y desconocidos.
SQL 03.05 relaciona cortes, créditos y clientes en solo lectura; contrasta
claves y saldos contra los CSV y demuestra ON/WHERE, ausencia de correspondencia
y multiplicación por claves incompletas con ejemplos adicionales en memoria.
SQL 03.06 distingue subconsultas escalares, listas, presencia correlacionada y
tablas derivadas; las CTE separan selección, relación, resumen e indicadores.
Compara consultas equivalentes y referencias Python sobre los mismos CSV,
con NULL y vacíos comprobados. El archivo SQLite se conserva en solo lectura;
los casos adicionales se crean en memoria. La recursión sigue como profundización.
SQL 03.07 conserva detalle mediante ventanas, particiones y orden; compara
observaciones con LAG, selecciona posiciones con ROW_NUMBER y explica marcos
ROWS/RANGE. Contrasta contra recorridos Python y separa cobertura, saldos
y movimientos aditivos; las consultas al archivo siguen en solo lectura.
SQL 03.08 conserva la fuente en lectura y escribe sobre una copia nueva con
backup de SQLite. Usa control explícito compatible con Python 3.11 y 3.12+,
selección previa, UPDATE/DELETE, confirmación/reversión y carga repetible exacta.
Las copias existentes solo se comprueban; no se reinician ni se reescriben.
SQL 03.09 reconstruye una base separada con el preparador de 03.03 y la consulta
en lectura con pandas. Concilia detalle y grupos con referencias desde CSV/merge,
con tipos y ausencias explícitos; exporta CSV comprobados y una gráfica de saldos
conocidos con cobertura en carpetas nuevas, sin sobrescribir entregas.
Visualización 04.01 explica pregunta, población, unidad y medida antes de elegir
una figura. Reutiliza los CSV de SQL, con bases explícitas para categorías,
comparación temporal, distribución y relación; la regeneración es opcional
y no exige aprender APIs que se profundizan en 04.02–04.04.
04.02 distingue Figure, Axes y Axis con un resumen pequeño derivado del cierre
SQL. Separa lectura, dibujo sobre un Axes y guardado/cierre; conserva categorías
con suma desconocida y permite dos paneles como extensión. No agrega dependencias.
04.03 compara categorías con orden común y cortes con bases explícitas; separa
importe, tasa y cobertura. Lee las fuentes originales y exporta tablas y tres
figuras en una carpeta nueva. Una serie didáctica independiente muestra huecos
mensuales, presencia de fila y cero sin imputar saldos. No agrega dependencias.
04.04 conserva el detalle conocido al explorar variabilidad: histogramas con
bordes comprobados, cajas con cuartiles/bigotes y puntos, dispersión con variables
conocidas del mismo registro. Exporta exclusiones por variable y no confunde
un valor exterior con un error ni asociación con causa. No agrega dependencias.
04.05 reutiliza lectura y cuartiles de 04.04 para revisar límites, escala log,
etiquetas, cobertura y accesibilidad. Conserva ceros y ausencias en una partición
con motivos, compara barras recortadas con origen cero y usa formas además de
color. Incluye figuras, tablas y descripciones textuales; no agrega dependencias.
La configuración raíz incluye Matplotlib 3.10.7
y un grupo notebooks con ipykernel 6.30.1, además de pandas 2.3.3.
No se crean carpetas vacías ni labs antes de implementar el contenido.

| Módulo | Secciones previstas | Cierre |
| --- | --- | --- |
| [02 — pandas](../curriculum/02_pandas/README.md) | 10: tablas, lectura, selección, tipos, calidad, texto/fechas, agrupación, uniones, reshape y análisis | Dataset limpio, indicadores conciliados y primera figura |
| [03 — SQL](../curriculum/03_sql_databases/README.md) | 9: modelo, consultas, carga, indicadores, joins, CTE, ventanas, transacciones e integración | Base reconstruible y conciliación pandas/SQL |
| [04 — Visualización](../curriculum/04_visualization_python/README.md) | 9: pregunta, Matplotlib, comparaciones, distribuciones, diseño, exportación, Altair, interacción y cierre | Figuras e interpretación sobre el mismo análisis |
| [05 — Python aplicado](../curriculum/05_python_applied/README.md) | 11: módulos, configuración, errores, pruebas, contratos, clases, generadores, decoradores, medición, APIs y cierre | Análisis organizado y comprobado |

Pandas comienza sobre las ventas conocidas y presenta después el vocabulario de
la cartera sintética. SQL introduce claves y cardinalidad; visualización reutiliza
sus indicadores; Python aplicado reorganiza ese mismo resultado. Los checkpoints
propuestos pertenecen a los proyectos previstos 01_clean_credit_data y
02_credit_database, todavía sin carpetas implementadas.

La interacción de Altair es opcional. En Python aplicado, 01–04 y los contratos
de 05 preparan el cierre 11; las ampliaciones 06–10 no bloquean R. Las dependencias
y versiones se elegirán al implementar cada herramienta, verificando la API vigente.

### Python aplicado: del notebook al proyecto

Ocupa el nivel 05, después de pandas, SQL y visualización en Python, reutilizando un problema conocido.
Los contenidos se organizarán por necesidades, no como una lista de sintaxis:

| Bloque | Conceptos previstos | Resultado observable |
| --- | --- | --- |
| Organización | Módulos, paquetes, configuración y logging | Extraer transformaciones de un notebook a código reutilizable |
| Funciones e iteración | Funciones como valores, iteradores, generadores y decoradores | Procesar por lotes y reutilizar comportamientos |
| Diseño de estructuras | Clases, composición, dataclasses y anotaciones de tipos | Representar registros o configuración con claridad |
| Robustez | Excepciones propias, gestores de contexto y pruebas | Manejar errores y recursos con casos verificables |
| Rendimiento | Medición de tiempo/memoria, profiling y complejidad básica | Localizar un cuello de botella antes de optimizar |
| Integración | APIs HTTP, paginación, tiempos de espera y reintentos | Obtener y validar datos de un servicio |

Foundations conserva funciones, mutabilidad, módulos, errores y el uso de `with`
al leer archivos. Crear decoradores o gestores de contexto y diseñar clases se
profundizará después. Herencia se tratará cuando haga falta; composición y
funciones son opciones iniciales. Concurrencia, asincronía y metaprogramación
quedan como temas avanzados sujetos a una necesidad concreta.

### Visualización: entender antes de construir aplicaciones

La primera gráfica y su interpretación aparecen en pandas. Una ruta posterior
profundizará en pregunta analítica, elección de gráfico, escalas, unidades,
agregación, etiquetas, color accesible y comunicación de incertidumbre.
Reutilizará datos e indicadores ya comprobados, comparando representaciones
sin repetir todo el análisis para cada biblioteca.

| Etapa | Python | R | Evidencia prevista |
| --- | --- | --- | --- |
| Base estática | Matplotlib: Figure/Axes, barras, líneas, distribuciones y exportación | ggplot2: datos, estéticas, geometrías, escalas y facetas | Una figura legible con interpretación y unidades |
| Composición e interacción | Altair: marcas, codificaciones, tipos y selecciones | Profundización de ggplot2 y composición de figuras; interacción como extensión | Comparar el mismo indicador en varias vistas |
| Producto interactivo | Streamlit: inputs, tablas, gráficas, reruns, estado y caché | Shiny: UI, servidor, reactividad, estado y módulos | Explorador de datos con filtros y resultados verificables |

Matplotlib y Altair son herramientas de gráficos del nivel 04; Streamlit es un framework
para aplicaciones del nivel 12. En R, ggplot2 básico aparece en tidyverse (07),
se profundiza en visualización R (08), y Shiny (13) convierte el análisis en una aplicación. No exigir todas las herramientas
para cada ejercicio: se puede elegir un ecosistema y comparar el otro después.

Para Streamlit se aprenderá primero su modelo de reejecución y después estado
y caché. Usar un decorador existente, por ejemplo para caché, no exige desarrollar
decoradores personalizados. En Shiny, enseñar reactividad antes de ampliar la UI.
En ambos casos separar transformación y validación de datos de la interfaz.

### Desarrollo previsto de los módulos 06–08

Los planes de R contienen 28 secciones, todavía sin lecciones ejecutables ni labs:

| Módulo | Secciones | Secuencia y cierre |
| --- | --- | --- |
| [06 — R fundamental](../curriculum/06_r_foundations/README.md) | 9 | Sesión, vectores, selección, faltantes, tablas, funciones, archivos, renv y conciliación con Python |
| [07 — tidyverse](../curriculum/07_tidyverse/README.md) | 10 | Importación, verbos, reglas, grupos, uniones, reshape, categorías, fechas y primera figura |
| [08 — Visualización en R](../curriculum/08_visualization_r/README.md) | 9 | Gramática, geometrías, estéticas, escalas, facetas, comunicación, composición, exportación y cierre |

R fundamental utiliza el análisis conocido como referencia, pero enseña el modelo
propio de vectores y NA. renv se introduce en 06 y se conserva en el proyecto que
crecerá con tidyverse. La primera figura de 07 evita posponer comunicación;
08 profundiza su diseño. Los checkpoints de 03_portfolio_analysis_r son propuestas,
aún sin implementar.

La [guía de lecturas abiertas](r-reading-guide.md) ubica R for Data Science,
Advanced R, el libro de ggplot2 y R Packages. Se consultan capítulos por necesidad;
objetos avanzados, metaprogramación y creación de paquetes no bloquean 06–08.
No se instalan paquetes ni se fija una versión de R por esta planificación.

### Almacenamiento y procesamiento previstos: 09–10

Se conserva el orden: después del análisis Python/R, el 09 define los archivos
compartidos y el 10 compara motores sobre esos mismos datos. Sus README contienen
19 secciones planificadas, todavía sin scripts ni labs.

| Módulo | Secciones | Papel y cierre |
| --- | --- | --- |
| [09 — Arrow y Parquet](../curriculum/09_arrow_parquet/README.md) | 9 | Teoría común, tipos, Python, R, intercambio, lectura selectiva, metadatos, particiones opcionales y contrato compartido |
| [10 — Polars y DuckDB](../curriculum/10_polars_duckdb/README.md) | 10 | Referencia, Polars inmediato/lazy, semántica, streaming opcional, SQL/DuckDB, clientes, intercambio, medición y decisión |

Parquet es almacenamiento; Arrow aporta representación e interfaces; Polars y
DuckDB procesan los datos. En 09, teoría una vez y prácticas completas Python/R:
escribir en un lenguaje y leer en el otro, verificando claves, registros, tipos,
faltantes e indicadores en ambas direcciones. No asumir precisión o equivalencia
de clases sin comprobar el contrato.

En 10, Polars se enseña principalmente desde Python, con R como ampliación;
DuckDB reutiliza SQL y ofrece recorridos para ambos lenguajes. El proyecto previsto
04_large_credit_dataset integra contrato, consultas y mediciones; sus checkpoints
se concretarán al implementarlo. No se exige superar la RAM del equipo para cerrar.
Particionamiento y streaming se estudian cuando una consulta los justifique.

Los planes de consulta y las mediciones deben distinguir preparación, ejecución,
materialización y exportación. Cambiar de motor no garantiza menos memoria o más
velocidad; el criterio es resultado equivalente y costo medido. No se agregan
paquetes ni datos voluminosos por la planificación. La ruta futura de R aplicado
sigue pendiente y esta decisión no renumera el track.

### Entrega prevista del producto: 11–14

Los cuatro módulos tienen 37 secciones planificadas y referencias oficiales,
aún sin lecciones/labs. El flujo es reporte → una app elegida → integración final;
no se exige completar las dos aplicaciones.

| Módulo | Secciones | Cierre esencial |
| --- | --- | --- |
| [11 — Quarto](../curriculum/11_reporting_quarto/README.md) | 9 | HTML regenerable con indicadores, figuras y narrativa del corte |
| [12 — Streamlit](../curriculum/12_streamlit/README.md) | 9 | Explorador Python local, probado y con filtros conciliados |
| [13 — Shiny](../curriculum/13_shiny_web/README.md) | 10 | Explorador R local, probado y con dependencias reactivas explícitas |
| [14 — Proyecto reproducible](../curriculum/14_reproducible_projects/README.md) | 9 | Reconstrucción independiente de datos, reporte y una app |

Quarto comparte teoría de documento y separa recorridos Python/Jupyter y R/knitr.
HTML y un motor bastan para el cierre; PDF, dashboards y publicación son ampliaciones.
Caché/freeze requieren un criterio de actualización de datos, no solo un render exitoso.

Streamlit distingue reejecución, estado de sesión y caché; Shiny distingue dependencias
reactivas, consumidores y estado por sesión. Ambos reutilizan funciones de datos;
se prueban indicadores, conjuntos vacíos y descargas sobre el mismo universo filtrado.
Mastering Shiny se incorpora a las lecturas abiertas del recorrido R.

El 14 amplía los proyectos existentes: contrato, configuración, entornos, pipeline,
pruebas, trazabilidad y entrega. No agrega una pila de herramientas nueva para el
cierre. Los proyectos 05_monthly_report y 06_shiny_portfolio_app y la alternativa
Streamlit son productos previstos, todavía sin carpetas implementadas.

La entrega esencial puede comprobarse localmente con datos sintéticos; despliegue,
autenticación y CI se añaden si responden a una necesidad. Los entornos y versiones
se fijarán al implementar. El diagrama general conserva sus niveles 00–14 y la
bifurcación de aplicación; los planes detallados no acreditan avance del estudiante.

### R aplicado: consideración para el próximo ajuste

Se contempla un puente después de visualización R (08) y antes de Parquet:
organizar scripts y funciones, reutilizar transformaciones, gestionar proyectos
y paquetes, comprobar resultados, manejar errores y medir rendimiento. Los
sistemas de objetos y otras especializaciones se tratarían cuando aporten claridad.
La meta sería convertir el análisis R conocido en código reconstruible, de forma
equivalente al cierre de Python aplicado.

Su integración en la numeración se decidirá en el próximo ajuste del track.
Todavía no hay carpeta, lecciones ni labs; esta consideración no renumera los
módulos mientras se inicia Python fundamental.

### Ubicación actual de módulos y proyectos

- Nivel 2: primera gráfica con Matplotlib y una explicación del hallazgo.
- Nivel 03: modelar y consultar los datos; conciliar indicadores con pandas.
- Nivel 04: representar ese análisis con Matplotlib y Altair.
- Nivel 05: organizar el análisis y sus comprobaciones antes de cambiar de lenguaje.
- Niveles 06–08: R fundamental, tidyverse y visualización con ggplot2.
- Niveles 09–10: Parquet y procesamiento con Polars/DuckDB.
- Nivel 11: reutilizar figuras e interpretaciones en reportes Quarto.
- Niveles 12–13: Streamlit en Python y Shiny en R. Elegir una aplicación y
  pasar al proyecto final; la otra puede estudiarse después para comparar.
- Nivel 14: integrar las prácticas de organización y robustez que ya se hayan
  introducido. El proyecto final no es la primera ocasión de validar o documentar.

Cada ruta tendrá lecciones, labs y checkpoints cuando se desarrolle. Mantener
los requisitos del gestor elegido actualizados al introducir bibliotecas; no
agregar dependencias ni crear esqueletos vacíos por anticipación.

Fuentes para desarrollar las herramientas:
[Matplotlib](https://matplotlib.org/stable/users/getting_started/),
[Altair](https://altair-viz.github.io/),
[ggplot2](https://ggplot2.tidyverse.org/) y
[Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts).

## Registro de decisiones

Las decisiones importantes se documentarán en `docs/decisions/` usando notas
breves: contexto, decisión, consecuencias y fecha. No se agregará infraestructura
solo para anticipar necesidades hipotéticas.

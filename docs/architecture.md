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
su recorrido. El mini proyecto uv del nivel 0 sigue siendo una práctica separada.
09.03 añade PyArrow 21.0.0 a esos requisitos y comprueba el lockfile en entornos
uv locales, conservando las versiones previas y sin modificar Conda base.
09.04 incorpora arrow de R al lockfile del proyecto de práctica, con respaldo
y restauración local comprobada, conservando los registros anteriores.
R utiliza `renv` desde 06.08 en copias autocontenidas de práctica, con biblioteca
y estado locales; no se inicializa renv en la raíz de DS Track. Las dos copias
permiten comprobar reconstrucción: no exigen una biblioteca nueva por cada
ejercicio del recorrido.

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
visualización dispone de 04.01–04.09 con lecciones y labs (04.08 opcional);
05.01–05.11 disponen de lección/lab y paquete local; 06.01–06.09 tienen lecciones/scripts/labs;
07.01–07.10, 08.01–08.09 y 09.01–09.09 tienen lecciones/scripts/labs;
10.01–10.10 tienen lección/muestra/funciones/lab (10.05 opcional); 11.01–11.04 tienen material,
11.05–11.09 y 12–14 conservan planificación;
pandas dispone de sus diez lecciones y labs, con notebook y gráfica de cierre. Python aplicado
está después de pandas, SQL y visualización básica: no bloquea el inicio de pandas.

### Desarrollo previsto de los módulos 02–05

Los README de cada módulo contienen el orden numerado y el alcance de cada
sección. Los módulos 02, 03 y 04 disponen de sus lecciones y labs;
05.01 tiene lección/lab, paquete, script y notebook; 05.02 agrega configuración
y logging sobre ese paquete; 05.03 desarrolla errores y recursos;
05.04 añade pruebas de función, archivos e integración con unittest;
05.05 documenta firmas/contratos y valida conteos/opciones de revisión;
05.06 incorpora clases y dataclasses como ampliación opcional por composición;
05.07 desarrolla iteradores y generadores con lotes y conciliación;
05.08 incorpora funciones como valores y una envoltura de registro comprobada.
05.09 incorpora mediciones repetidas, perfiles y comparación de memoria/tiempo
con contratos conservados. 05.10 incorpora paginación, respuestas locales y
normalización conciliada, con transporte HTTPS probado sin red. 05.11 integra
ejecución, figura, verificación y reconstrucción; el material del módulo está disponible.
pandas 02.10 también dispone de notebook.
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
04.06 compone medianas entre cortes con ejes comunes y mediana/cobertura con
unidades separadas. Reutiliza la misma lectura, añade anotación comprobable y
exporta una Figure en PNG a dos resoluciones y en SVG, junto con tablas,
registro de tamaños y nota textual. Conserva entregas previas, cierra solo sus
figuras y no agrega dependencias.
04.07 declara marcas, canales y tipos N/O/Q/T en Altair 6.3.0, reutilizando
las tablas de 04.06 y pares de 04.04. Conserva ausencias, tramos ordenados y
fechas comprobadas; compara medianas preparadas y agregación desde detalle.
Exporta JSON/HTML; el grupo opcional chart-export con vl-convert-python
1.9.0.post1 permite HTML con bibliotecas incorporadas y PNG/SVG. Las entregas
requieren carpeta nueva; fuentes y SQLite permanecen intactos. Interacción
y selecciones se desarrollan en 04.08, disponible como extensión opcional.
04.08 incorpora menú con parámetro variable, selección por segmento con
resaltado y un intervalo que filtra otra vista. Conserva bases y dominios
explícitos, opciones sin pares y restablecimiento; la mediana de cada segmento
usa sus saldos conocidos, no solo los pares. Los controles actúan en el
navegador sobre datos incorporados y no reejecutan Python ni escriben CSV.
HTML conserva interacción; PNG/SVG representan estados iniciales. Las capturas
requieren registrar estado y bases. No agrega dependencias.
04.09 integra la tabla de medianas/cobertura en Matplotlib y Altair, con
referencia independiente CSV/statistics, veinte comprobaciones, informe e
instrucciones. Conserva copias de cortes/créditos, reconstruye desde ellas
y usa carpetas nuevas. El informe no acredita revisión visual ni aprendizaje;
HTML incorporado y explorador son ampliaciones. No requiere Quarto ni un
proyecto adicional; prepara el análisis que se reorganizará en 05.
05.01 introduce módulos/importaciones antes de separar el análisis de 04.09
en un paquete regular local: entrada, transformación, comprobación,
presentación y coordinación. Script y notebook consumen las mismas funciones,
sin modificar sys.path ni leer CSV/exportar al importar. Conserva referencia
independiente, medianas/cobertura, fuentes y figuras del cierre esencial.
Interacción y HTML incorporado se conservan en 04.08/04.09, fuera de esta
primera reorganización. No agrega dependencias; reutiliza notebooks cuando
se ejecuta ese consumidor.
05.02 conserva las entradas anteriores y agrega ejecutar_configurado.py y
analisis_cartera.cli, con configuración y registro mediante biblioteca estándar.
Combina predeterminados → JSON → opciones explícitas, distinguiendo rutas del
archivo y del directorio de trabajo. Valida antes de exportar; configura logging
solo en la entrada y guarda valores efectivos, procedencia, reglas y versiones.
El registro final sucede después del cierre de export: una falla puede dejar
entrega.json sin ejecucion.json. No promete atomicidad sobre la carpeta.
05.03 conserva esos consumidores y agrega ejecutar_seguro.py, recursos y cierre:
with para archivos, closing para conexión SQLite en memoria y JSON con temporal
local/cierre/reemplazo. Simula fallas después de exportar, durante el registro
y antes del cierre; conserva carpetas parciales. cierre.json se publica después
de registro e instrucciones, con archivos requeridos comprobados. El inspector
verifica etapa/presencia, no integridad completa ni aprendizaje. Un reemplazo
atómico de JSON no hace transaccionales los CSV/figuras ni garantiza durabilidad
ante pérdida de energía; limpieza fallida informa el temporal sin ocultar la causa.
05.04 conserva el paquete y los consumidores; pruebas_0504 vive junto al paquete
para importarlo desde su directorio sin modificar sys.path. Las fixtures pequeñas
separan tabla tipada y CSV temporales; la colección comprueba resultados manuales,
claves, ausencias, tipos, conservación, reconstrucción y fallas por etapas.
No agrega dependencias ni sustituye validación de datos, revisión visual o
evidencia de aprendizaje. El lab añade un caso que distingue mediana de promedio.
05.05 anota y documenta las entradas, transformación y coordinación conocidas.
contratos.coverage_pct explicita conteos y cobertura sin base; summarize la
reutiliza conservando resultados. revision.review_summary permite revisar
segmentos sin exportar, con None/todos y lista vacía/ninguno, conservando orden
y validación de fuentes. normalize_cut asigna None al corte didáctico fijo.
Las doce pruebas nuevas comprueban sus límites; las veintiuna de 05.04 siguen
separadas. No incorpora checker, stubs ni esquemas tabulares; el análisis estático
queda opcional y las anotaciones no sustituyen validación ni conciliación.
05.06 añade objetos.py sin modificar consumidores ni algoritmos anteriores.
CoverageCounts ilustra estado mutable y métodos; ReviewOptions conserva corte
y tupla de segmentos con validación explícita y frozen. ReviewJob contiene
fuente/opciones y delega en review_summary; no guarda tablas ni recursos, no
exporta y relee las fuentes al ejecutar summary. replace crea variaciones
validadas, sin modificar el original. Trece pruebas y lab opcionales comprueban
alias, estado, composición, vacíos y conservación. No exige herencia, clases
para DataFrames ni dependencias nuevas; el cierre esencial sigue siendo 05.11.
05.07 añade iteracion.py y ejecutar_lotes.py sin cambiar consumidores anteriores.
iter_batches entrega listas nuevas y conserva el último lote corto; validación
y errores ocurren al consumir el generador. batch_indicators recorre cortes.csv
con csv.DictReader/islice, valida también otros cortes y conserva el catálogo,
un conjunto de claves global y saldos conocidos para mediana. No reúne todos
los diccionarios ni el detalle pandas, pero tampoco garantiza memoria constante.
Retorna cinco grupos de indicadores al terminar, sin exportar; el script concilia
con la lectura completa. Contrato CSV explícito de enteros decimales no negativos
y archivos bajo with; quince pruebas y lab de extensión protegen resultados,
recursos y errores tardíos. Sin dependencias nuevas ni mediciones anticipadas.
05.08 añade instrumentacion.py sin modificar consumidores o algoritmos anteriores.
log_call recibe funciones normales, prepara una envoltura con wraps y registra
inicio/fin/falla al llamar; reenvía argumentos, retorna el mismo objeto y propaga
la misma excepción/causa. No configura logging al importar y no registra valores
de argumentos/resultados. logged_indicators delega a 05.07 y el script nuevo
concilia con la lectura completa sin exportar. No consume iteradores retornados;
rechaza funciones generadoras/async declaradas como tales. Trece pruebas y lab
de extensión comprueban contrato, metadatos y límites. No añade caché, reintentos,
medición ni dependencias; la fiabilidad del backend logging queda como supuesto.
05.09 añade medicion.py y ejecutar_medicion.py sobre el mismo paquete, sin cambiar
los algoritmos anteriores. Compara validación por aparición/reutilización local
de fechas con contratos equivalentes, tamaños y diversidad explícitos. Guarda
tiempos crudos con calentamiento/orden alterno, memoria trazada y perfiles en
llamadas separadas; las fases del análisis son fronteras solapadas, no sumables.
Trece pruebas nuevas protegen equivalencia, fallas y sesiones ajenas de instrumentos,
incluido cProfile de CPython 3.12. La salida requiere carpeta nueva y puede quedar
parcial ante fallas de escritura; no sustituye el cierre de entrega de 05.03.
No instala dependencias ni promete memoria total acotada o mejoras universales.
05.10 añade api.py y ejecutar_api.py con muestras de las mismas 48 observaciones
en tres páginas y configuración local. fetch_detail recibe un transporte inyectable,
valida estado/JSON/esquema/claves/total, conserva ausencias y enteros precisos,
y retorna solo una tabla completa. Reintentos limitados de GET para timeout/503
sin Retry-After; otros estados/fallas se comunican sin datos parciales de éxito.
El script simulado concilia con CSV, registra intentos/pausas y escribe JSON final
atómico, sin hacer atómica la carpeta. urllib cierra respuestas y HTTPError,
limita bytes y usa timeout explícito; el adaptador se prueba con sustitutos locales.
Dieciocho pruebas nuevas y lab de extensión, sin credenciales, servicios reales
obligatorios ni nuevas dependencias. No implementa snapshots ni un cliente universal.
05.11 reutiliza ejecutar_seguro.py/run_delivery con configuración de cierre,
sin duplicar cálculos. auditoria.py y verificar_entrega.py recalculan desde
fuentes copiadas, contrastan cinco tablas en la frontera CSV y la especificación
Altair, y comprueban propiedades de PNG/SVG. Comparan reconstrucciones por corte,
hashes de fuentes, tablas y especificación, sin exigir imágenes de bytes idénticos.
Diez pruebas nuevas y lab de cierre, incluida falla controlada y revisión visual.
El verificador es de solo lectura y no acredita revisión visual ni aprendizaje;
no exige ampliaciones opcionales ni crea proyectos/checkpoints pendientes.
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

### Recorrido de los módulos 06–08

Los planes de R contienen 28 secciones; las nueve de 06 tienen lecciones,
scripts y labs; las diez de 07 y las nueve de 08 también están disponibles.
Proyecto y checkpoints siguen pendientes:

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
06.01 usa una venta escalar propia y diagnóstico de sesión con paquetes incluidos;
distingue R/editor/terminal, source frente a proceso nuevo y uso frente a instalación
de paquetes. Se verificó con R 4.6.1 ya instalado, sin cambiar Conda, PATH ni
bibliotecas. RStudio es opcional; renv y paquetes externos siguen en sus secciones.
Se contrastan R4DS segunda edición, documentación de R y guía oficial de Posit.
06.02 amplía la venta escalar con cuatro observaciones alineadas por posición.
ventas_vectores.R conserva el cálculo correcto (660 MXN, 594 con descuento);
riesgos_vectores.R separa reciclaje silencioso/parcial, coerción a texto y
truncamiento como demostraciones no aceptadas. Tipos/clases, vacío y correspondencia
explícitos, sin adelantar selección/tablas ni instalar paquetes. Ejemplos y lab
comprobados con R 4.6.1, Advanced R como lectura puntual y documentación oficial.
06.03 conserva las cuatro ventas y añade seleccionar_ventas.R: posiciones,
nombres/máscaras, correspondencia y modificación de copia. Introduce una lista
mínima antes de usar $ y distingue [ de [[ según objeto y contenido; dimensiones
con matriz/drop son ampliación opcional. Faltantes y lógica solo se anticipan con
explicación; el detalle de tablas queda en 06.05. Script/lab comprobados con R 4.6.1,
sin modificar fuentes ni instalar paquetes.

06.04 añade logica_faltantes.R con dos ventas incompletas además de las cuatro
anteriores. Conserva tres grupos y concilia sus conteos; diferencia máscaras
vectoriales de preguntas escalares con any/all y cortocircuito. NA, NaN, NULL y
cero explícitos, suma/media observadas con cobertura y fronteras de vacío/todos
faltantes; una confirmación se realiza sobre copia. Lección, script y lab
comprobados con R 4.6.1 y documentación oficial; R4DS segunda edición como lectura
puntual, sin paquetes externos ni cambios en las fuentes previas.
06.05 añade listas_tablas.R: listas con componentes distintos, tabla de seis ventas,
tipos por columna y selección que conserva dimensiones con drop = FALSE. Conserva
pendientes e identidad, contrasta vacío con faltantes y modifica una copia con
recálculo explícito. Demuestra reciclaje incorrecto por separado y nombres exactos;
lab con variante independiente. Advanced R y ayuda de R 4.6.1 contrastados, incluido
el valor predeterminado stringsAsFactors desde R 4.0; sin paquetes externos.
06.06 separa funciones_ventas.R (definiciones sin ejecución de análisis) y
ejecutar_funciones.R (muestra, llamadas y presentación). Funciones pequeñas validan
vectores numéricos ordinarios, rechazan reciclaje e importes no finitos, calculan
por posición y devuelven un resumen con cobertura. Vacío y todos faltantes producen
indicadores NA, distintos del cero observado; total solo con registros completos.
Retorno y alcance local, if escalar, stop y for/seq_along explicados; tryCatch es
extensión para un rechazo esperado. Script/lab comprobados con R 4.6.1, fuentes
previas conservadas y referencias de R4DS/Advanced R contrastadas. Sin paquetes
externos ni validación de archivos anticipada.
06.07 incorpora un CSV propio de 14 registros que conserva las seis ventas previas.
funciones_archivos.R separa lectura textual/estructura, conversión, validación y
exportación; ejecutar_archivos.R coordina con el resumen de 06.06. Rechaza todas
las apariciones de identificadores repetidos y conserva texto/posición/motivos;
faltantes numéricos permitidos siguen pendientes, sin imputación. Concilia 14/8/6
y cobertura 6/8, suma observada 765.5; exige destino nuevo y relee identidad, notas,
importes e indicadores. CSV con un registro por línea, UTF-8 y gramática numérica
explícita; no es un lector universal ni una entrega atómica. Vacíos y errores
estructurales comprobados con R 4.6.1; locale UTF-8 solo en procesos de revisión,
sin paquetes externos ni cambios globales. readr y renv siguen en sus secciones.
06.08 añade preparador y plantilla con DESCRIPTION, lockfile y activador generado
por renv 1.3.1. Las copias reciben funciones y CSV de 06.06/06.07; no dependen de
rutas hacia otras lecciones. withr 3.0.3 presenta el resumen con opciones temporales
sin redondear los datos guardados. Perfil de proyecto, biblioteca/estado locales,
snapshot explícito y restore separados de R y de .RData. --vanilla requiere la
activación explícita que realizan los scripts. Dos bibliotecas restauradas, tablas
equivalentes y recuperación de paquete retirado comprobadas con R 4.6.1. El
proyecto de práctica prepara la organización para tidyverse; no implementa el
proyecto integrador ni instala paquetes del módulo 07.
06.09 integra funciones y datos de 06.06/06.07 con el lockfile de 06.08 en una
copia de cierre. Una referencia Python de biblioteca estándar calcula el mismo
contrato de ventas; no reutiliza sin adaptar las reglas diferentes de 01.06 ni
lee salidas R. El comparador R conserva texto/identidad/motivos, exige conteos y
máscaras de faltantes exactos y usa tolerancia absoluta 1e-9 para valores numéricos.
Contexto y huella de fuente previenen referencias antiguas; 36 controles en memoria
y 36 tras releer CSV. El verificador recalcula y compara sin escribir y exige
los archivos finales, sin confiar en el informe como prueba de corrección.
R 4.6.1/Python 3.12.12 comprobados; renv/withr conservados, sin dependencias nuevas.
Las nueve secciones de R fundamental tienen material; no acreditan aprendizaje
ni completan el proyecto integrador pendiente.

07.01 incorpora readr 2.2.0/tibble 3.3.1 en el mismo proyecto renv de práctica.
El preparador respalda los metadatos 06.09 antes de actualizar DESCRIPTION/lock;
conserva perfil, funciones de ventas y salidas. No reinicializa renv. El lockfile
fue generado y restaurado realmente; no modifica la semilla de 06.08 ni instala
el metapaquete tidyverse. Reutiliza el CSV y diccionario de pandas 02.02: seis
créditos por corte, claves de texto, fecha aún character, double/integer y NA
explícitos. Separa parseo de reglas de dominio, detiene problemas, comprueba
esquema/valores conocidos y fuente intacta. Pipe nativo sin verbos adelantados;
no exporta ni grafica; el integrador sigue pendiente.
La 07.01 prioriza RStudio/IDE: el preparador define una función al usar source(),
y solo interpreta argumentos al ejecutarse por terminal. Apertura del proyecto,
restauración y comprobación completa desde R; terminal opcional al final.

07.02 añade dplyr 1.2.1/generics 0.1.4 al lockfile del mismo proyecto con
respaldo de metadatos 07.01 y preparación por función desde R. Conserva lector,
datos, scripts y versiones previas. select/rename/filter/arrange sobre tablas
locales sin agrupar; no introduce mutate ni resúmenes agrupados. Script y lab
comprueban selección 002/003/006, subtotal 2750 con cobertura 3/3 y partición
3 confirmados/2 no cumplen/1 pendiente. Evalúa la condición completa, con lógica
de tres valores y sin imputar cero. Empates, NA al ordenar, vacío tipado, claves,
objeto/fuente intactos y equivalencia con pandas/SQLite sobre el mismo CSV.
Recorrido IDE: bloques y reinicio/Source; no requiere terminal ni exporta.
07.03 reutiliza el lockfile y biblioteca de 07.02 sin dependencias nuevas. Su
preparador añade funciones, ejecutor y el CSV de 40 filas de pandas 02.04;
conserva muestras y scripts previos. Inicia con ejemplos pequeños y después
interpreta texto, marca incompatibilidades de tipo/rango y conserva _texto.
No trunca fracciones; distingue parseo, requisito entero y reglas de dominio.
mutate/if_else/case_when mantienen filas y explican tipos, prioridad y NA.
Porcentaje con denominador positivo antes de dividir; resta double para evitar
desbordamiento integer. 40 × 15 con 36 restas/35 porcentajes evaluables, base
común 217750 − 6600 = 211150 MXN y etiquetas 21/16/3. Conciliación con pandas
por clave/campo, tolerancia absoluta 1e-10 en porcentajes; R integer e Int64 no
se equiparan fuera de este contrato. RStudio/IDE con reinicio/Source y advertencias
esperadas visibles; no exporta ni decide aceptación de registros.
07.04 reutiliza la lectura/conversión de 07.03 y el lockfile de 07.02, sin
instalar ni cambiar metadatos. Su preparador añade funciones, ejecutor y el
CSV de 44 registros de pandas 02.05. Reglas de presencia, entero, no negatividad,
catálogo, pago ≤ saldo y unicidad de ID/corte completo. Marca todas las
apariciones de claves repetidas con duplicated en ambos sentidos; distinct
solo se usa para explicar su reducción y dependencia de la primera fila.
Mantiene numero_registro, tres textos numéricos y todos los motivos; banderas
sin NA gracias a reglas explícitas de ausencia/incompatibilidad. 44 × 12 en
trabajo, 44 × 15 en banderas; 29 aceptados/15 rechazados y 19 incidencias.
Reconstrucción por bind_rows/orden y comparación de todas las columnas, claves
aceptadas y motivos frente a banderas. Saldo interpretable 234900 = 177250 +
57650 MXN con cobertura 42/44 y dos saldos sin interpretar; no es total limpio
de créditos únicos. Conciliación exacta con pandas de filas, partes y reglas;
fronteras y particiones alteradas comprobadas. RStudio/IDE con reinicio/Source,
sin exportar ni imputar.
07.05 añade funciones, ejecutor, preparador y lección/lab para resumir esos
29 aceptados por corte/segmento: cuatro grupos, 177250 MXN, 18 atrasos ≥ 30.
Conserva datos/lockfile/biblioteca; solo añade dos archivos a la práctica.
Distingue estado de agrupación, suma observada/total completo, tasas entre
conocidos y cobertura. Una muestra analítica mínima independiente permite NA
sin cambiar las reglas de aceptación de 07.04; vacío y factores opcionales
aclaran grupos sin observaciones. Revisión de claves, tipos y todos los valores,
con conciliación pandas sobre la misma población. IDE con reinicio/Source;
no exporta ni grafica.
07.06 añade funciones, ejecutor, catálogo y lección/lab; preparador desde R
incorpora tres archivos al mismo proyecto sin cambiar los anteriores ni paquetes.
Unión estática de los 29 aceptados con una fila por segmento: 29 × 14, saldo
177250 MXN conservado, 19 coincidencias/10 sin catálogo y seis etiquetas ausentes
a pesar de coincidir. Salud queda sin uso; educacion sin correspondencia.
left/inner y semi/anti, claves compuestas, relación muchos a uno y NA que no
coinciden; cardinalidad y cobertura son controles distintos. Catálogo completo
validado, incluidas claves sin uso; identidad, columnas, orden e indicadores
comprobados. Conciliación pandas/SQLite sobre la misma población y políticas
de NA, multiplicación incorrecta y casos vacíos. IDE con reinicio/Source;
sin exportar ni graficar.
07.07 añade lección/lab, lector, funciones y ejecutor de cambio de forma.
Reutiliza la muestra analítica de pandas 02.07 (48 observaciones/24 IDs),
distinta de los 29 aceptados previos. Proyección ID/corte/saldo: 48 × 3 → 24 × 3
→ 48 × 3, tipos y seis NA conservados; 47200/46700 MXN, cobertura 21/24 por corte.
Claves únicas antes del pivot, esquema vacío estable e inventario explícito
para distinguir combinaciones ausentes de NA en una observación. No reconstruye
segmento/atraso desde la proyección; mantiene la fuente completa intacta.
Preparador respalda metadatos 07.06 y añade tres archivos; lockfile generado
con tidyr 1.3.2, purrr 1.2.2, stringr 1.6.0 y stringi 1.8.9, preservando registros
anteriores. Restauración en biblioteca local, sin cambiar entornos globales.
Revisión de vuelta, fronteras y alteraciones con conciliación pandas independiente.
07.08 añade lección/lab, funciones, ejecutor y preparador desde R con respaldo
07.07. Reutiliza las 48 entradas de pandas 02.06; solo normaliza segmento,
conservando ID, fechas y cantidades. Origen, texto recortado/normalizado,
estado y marca de cambio: 48 × 10, 45 reconocidos/3 pendientes, dos ausencias
y una categoría fuera de catálogo. Suma de registros 112800 = 105800 + 7000 MXN,
sin presentarla como saldo a una fecha única ni aceptación completa.
Factores estrictos solo para reconocidos, niveles nominales y orden manual
frente a orden por medida; grupos vacíos y niveles descartados explícitos.
Stringr 1.6.0 pasa a dependencia directa y se añade forcats 1.0.1 sin cambiar
registros anteriores del lockfile; restauración local comprobada. Comparación
independiente pandas de texto, estados, partes y resumen; fronteras y alteraciones.
No grafica ni valida fechas/IDs.
07.09 continúa sobre la fuente de texto de 07.08, sin filtrar previamente sus
pendientes. ID/segmento normalizados y fechas Date bajo forma ISO, calendario
y años 1900–2100; originales y todos los motivos conservados. Alta ≤ corte y
clave ID/corte única después de interpretar: trabajo 48 × 15, 36 aceptados/
12 rechazados; suma de registros 112800 = 81400 + 31400 MXN, no saldo a una fecha.
Diferencia explícita en días, componentes y clave mensual Date; períodos con
fin exclusivo. Dos cortes de 18 aceptados no implican mismos IDs: base común
14, saldos 29000/31800 MXN y diferencia 2800; no coincidentes conservados.
Lubridate 1.9.5/timechange 0.4.0 añadidos con registros previos del lockfile
intactos, respaldo 07.08 y restauración local comprobada. Revisión pandas de
columnas, banderas, motivos, selecciones y base común; calendario con datetime.
07.09 no grafica; 07.10 reconstruye sus reglas y la base común desde el CSV.
Conserva 36 aceptados/12 rechazos y ocho aceptados sin pareja; dos filas de
saldos 29000/31800 MXN alimentan geom_col. ggplot/aes/capas, diferencia frente
a conteo, ejes desde cero, etiquetas y ggsave con objeto explícito. Entrega en
carpeta nueva: siete CSV, RDS con tipos/originales, PNG y diagnóstico de sesión.
El verificador reconstruye tablas desde la fuente y relee los CSV; firma/presencia
PNG no sustituyen inspección visual. ggplot2 4.0.3 y ocho dependencias nuevas con
lockfile real, respaldo 07.09 y registros anteriores intactos; restauración local
comprobada. Datos, pares e indicadores conciliados con pandas/SQLite. Las diez
secciones tienen material; proyecto/checkpoints permanecen pendientes, según
[el cierre de 07](tidyverse-closure.md).
La planificación restante no instala paquetes ni fija versiones por anticipación.

08.01 desarrolla pregunta y gramática sobre el mismo cierre de 07.10, sin
copiar fuentes ni modificar funciones anteriores o metadatos renv. Lección,
script y lab distinguen crédito/corte de fila resumida, mapeos de posición,
geometrías, herencia y componentes. La variante de una etiqueta usa datos locales
a una capa sin filtrar las barras. Scripts por bloques y reconstrucción completa
desde sesión nueva; no agrega dependencias ni exige otra exportación.
08.02 amplía geometrías y estadísticas sobre los mismos 14 IDs: resumen de dos
filas, 14 pares y detalle de 28 observaciones conciliados. Barras/conteos,
líneas, dispersión, histograma de septiembre con bordes/cierre explícitos y
cajas con cuartiles tipo 7/bigotes 1.5 IQR. Figuras y cálculos por capa comprobados;
lab con cambio de intervalos y muestra independiente con exterior conservado.
Proporciones y huecos de línea son ampliaciones. No cambia funciones anteriores,
fuentes o lockfile ni agrega dependencias.
08.03 añade lección/script/lab y figura: mapeos frente a propiedades constantes,
leyenda accidental, relleno/borde, formas/tamaños y agrupación explícita por ID.
Conserva 14 pares, 28 observaciones y 29000/31800 MXN; mapeos locales separan
color de puntos por fecha e identidad de líneas. Sin dependencias nuevas.
08.04 añade lección/script/lab y figuras: escalas continuas/discretas/Date,
unidades, marcas y etiquetas, límite de escala frente a ventana de coordenadas.
Cajas tipo 7 de 14/10 saldos con mediana 2050/1750; el zoom conserva el cálculo.
Log10 sobre positivos y proporción fija en dispersión; conserva 14 pares y
29000/31800 MXN sin nuevas dependencias ni cambios de fuentes o lockfile.
08.05 añade lección/script/lab y figuras: wrap/grid, escalas compartidas/libres
y capas con claves de faceta. Selecciona del detalle aceptado los mismos 14 IDs,
con segmento estable comprobado: ocho sumas y 29000/31800 MXN, cuatro/cuatro/
tres/tres créditos por corte y denominador común 14. Ocho cajas y 28 puntos;
muestra independiente con cero, saldo NA y combinaciones sin registro, sin
imputar ni modificar fuentes/lockfile.
08.06 añade lección/script/lab y figuras: mensaje derivado de las dos sumas,
labels frente a temas/capas, anotación local y tema local sin cambiar la sesión.
Conserva 29000/31800 MXN, +2800 y cobertura 14/18; color/forma y variante de
color único, descripción alternativa recuperable y tabla de lectura. Contraste
y revisión del destino sin certificar accesibilidad completa; fuentes/lockfile
intactos y sin nuevas dependencias.
08.07 añade lección/script/lab y figuras de composición: resumen de dos sumas
y detalle de 28 observaciones, 14 pares y 29000/31800 MXN conciliados.
Patchwork 1.3.2 se incorpora al mismo proyecto renv, con respaldo 08.06; los
43 registros anteriores del lockfile siguen idénticos. Disposición, guías
compatibles y ejes explícitos; anidación con proporción fija como ampliación.
Restauración real en otra copia sin biblioteca, sin cambiar Conda ni paquetes
globales; fuentes y funciones previas intactas.
08.08 añade lección/script/lab y figura: PNG esencial de 9 × 6 pulgadas a 144 dpi,
configuración, descripción, huellas y tablas reconstruidas; verificación de solo
lectura, dimensiones y revisión al tamaño final. Doble dpi y SVG/PDF con
dispositivos incluidos en R son ampliaciones; sin dependencias nuevas.
08.09 añade lección, scripts R/Python, figuras y lab. Reconstruye el CSV original
por rutas independientes y concilia campos de auditoría de aceptados/rechazos,
sin pareja/fuera de cortes, pares y resumen antes de dibujar. Reutiliza la entrega
de 07.10; 14 IDs, 29000/31800 MXN y 9.66% sobre el saldo inicial. Denominadores
y alcance explícitos, sin comparar píxeles ni cambiar dependencias.
Las nueve secciones de 08 tienen material; el proyecto integrador continúa pendiente.

### Almacenamiento y procesamiento: 09–10

Se conserva el orden: después del análisis Python/R, el 09 define los archivos
compartidos y el 10 compara motores sobre esos mismos datos. Sus README contienen
19 secciones; 09.01–09.09 y 10.01–10.10 disponen de lección/lab y scripts;
10.05 es opcional; proyectos/checkpoints y práctica siguen pendientes.
09.01 distingue formato, representación y biblioteca con una proyección de 28
observaciones de los mismos 14 IDs y 29000/31800 MXN. CSV/Parquet reales e
inventario conservados; inspección esencial Python estándar/R base y lectura
Parquet opcional de autoría con PyArrow 21.0.0 ya existente. No se incorporan
paquetes en esa introducción ni se acredita lectura Parquet en R. Los tamaños de disco y buffers
no se presentan como RAM del proceso ni como benchmark.
La introducción incluye comparación conceptual por filas/columnas, codificación
frente a compresión y selección lógica frente a lectura física, antes de las
APIs y mediciones posteriores. Conserva el esencial sin paquetes externos.
09.02 define el contrato de esas tres columnas, sin modificar la muestra ni
dependencias. Python estándar/R base evalúan 23 casos separados con originales
y motivos conservados: 5 aceptados/18 rechazados. Distingue ausencia/vacío/cero,
tipo/dominio/clave, calendario, rango/precisión, unidades, instantes y categorías;
no acredita conversión ni lectura Parquet en R.
09.03 añade lección, recorridos, módulo reutilizable y lab de escritura/relectura
Python. Declara PyArrow 21.0.0 y regenera uv.lock sin alterar los registros
previos, salvo la dependencia del proyecto. Conserva pandas 2.3.3; instalación
y reconstrucción uv locales comprobadas. CSV validado, pandas tipado, esquema
Arrow string/date32/int32 no anulable, índice omitido y Parquet nuevo con
relectura por clave; mantiene 28 registros y 29000/31800 MXN. Verificador de
solo lectura, límites/vacío/alteraciones y destinos ocupados; no cambia datos
previos, Conda ni bibliotecas globales.
09.04 incorpora arrow 25.0.1/assertthat 0.2.1 al mismo proyecto renv, con respaldo
08.09, 44 registros anteriores idénticos y restauración local desde biblioteca
vacía. Ejemplo pequeño completo, sin depender de entregas Python o de objetos
previos; base común y evaluador copiados sin cambios. Lectura del esquema real
antes de convertir a R, contrato string/date32/int32 no anulable, comparación
por clave, entrega nueva y verificador de solo lectura. Mantiene los 28 registros
y 29000/31800 MXN. Sesiones nuevas, fronteras y contraste Python comprobados;
09.05 integra escritores y verificadores de 09.03/09.04 sin cambiar algoritmos
ni lockfiles. Dos carpetas nuevas, lectura en el otro lenguaje y referencias
reconstruidas; base común de 28 registros y 29000/31800 MXN, más muestra propia
de tres filas con texto acentuado, vacío/ausencia y cero. Contrato independiente
anulable en etiqueta/importe, suma observada 10 y cobertura 2/3. Preparador
solo añade script y ruta local compartida; no exige entregas anteriores.
Sesiones nuevas, tipos/nulabilidad, valores por clave, fronteras y alteraciones
compensadas comprobados en ambos lectores.
09.06 añade Dataset/Scanner y consultas dplyr sobre partes Parquet, sin cambiar
fuentes, dependencias ni lockfiles. Ejemplo completo de cuatro filas y base
común de 28 filas en dos partes; inspección del esquema de cada archivo antes
de abrir el dataset. Auditoría completa en memoria separada de la consulta
selectiva y referencia independiente CSV en Python/R base. Octubre ≥ 2000:
nueve IDs y 24100 MXN. El lab muestra que una consulta correcta no certifica
filas excluidas: duplicar septiembre mantiene la selección de octubre, pero
la auditoría global rechaza claves repetidas. Vacíos, fronteras, partes
incompletas/esquemas distintos y conservación comprobados; no acredita I/O
medido, rendimiento ni memoria total acotada.
09.07 añade metadatos, grupos y comparación de cuatro variantes equivalentes,
con tres repeticiones y una modificación respecto de la base por comparación.
Ejemplos iniciales autónomos de cuatro filas; base común de 28 filas y
29000/31800 MXN reconstruida desde CSV, sin requerir entregas anteriores.
Python inspecciona estadísticas/códecs/codificaciones por bloque, incluso de
archivos R; arrow 25.0.1 expone esquema/conteos y lectura de grupos, no ese
detalle de metadatos. Tiempos de escritura/lectura separados de validación,
notas crudas y verificadores de solo lectura. Sin dependencias ni cambios de
lockfiles; no acredita I/O físico, RAM ni rendimiento general.
09.08 implementa la ampliación opcional de particiones Hive, con ejemplos
autónomos y comparación plana/por corte. Etiqueta auxiliar textual, tres columnas
físicas conservadas y auditoría de correspondencia de rutas antes de conciliar
por clave. Base común de 28 filas, 29000/31800 MXN y selección de nueve IDs/
24100 MXN; demostración de 28 particiones por clave frente a dos cortes.
Duplicados, etiquetas falsas, vacíos y esquemas de todas las partes comprobados
con lectura cruzada Python/R y sesiones nuevas. Destinos nuevos y política error,
sin sobrescrituras, borrados, dependencias nuevas ni cambios de lockfiles.
El inventario/candidatos no acredita I/O físico, tiempo o RAM.
09.09 integra fuente/contrato, Parquet completo/partes planas y exportaciones
con notas/huellas. Ambos escritores y lectores verifican la misma estructura,
reconstruyen la fuente externa y comparan todos los valores por clave, resumen,
selección e inventario. Mantiene 28 registros y 29000/31800 MXN, nueve IDs/
24100 MXN en la consulta; copias con alteraciones compensadas rechazadas aun
actualizando huellas. Reconstrucción y cruces desde procesos nuevos, sin
dependencias nuevas ni entregas previas; particiones opcionales no requeridas.
Las nueve secciones de 09 tienen material; proyectos/checkpoints y práctica
del estudiante siguen pendientes.
10.01 inicia el procesamiento con pregunta, contrato y referencia antes de
introducir motores. Muestra autónoma de seis filas y comparación de pares
con Python estándar; R base opcional aporta referencia independiente. Fuente
entera validada con las reglas reutilizadas, sin necesitar entregas anteriores.
Vacío, fronteras, tipos, agregados amplios y errores compensados comprobados.
Generador opcional determinista de 1–999 créditos/dos cortes, 40/400 filas como
ejemplos y máximo 1998; la cota conserva IDs de tres dígitos. Se distingue
adaptación de resultados de inspección del esquema y ejecución de mediciones.
10.01 no incorpora motores ni cambia lockfiles. 10.02 introduce Polars 2.0.0
declarado en pyproject/uv.lock, con runtime estándar y registros previos intactos;
instalación y segunda reconstrucción uv locales con Python 3.12.12.
DataFrame/Series/expresiones, select/with_columns/filter/group_by/agg, tipos
explícitos y suma ampliada antes de reducir. Muestra propia de seis filas,
003/2600 y resumen 4500/4600 MXN; derivada Float64 en miles solo para presentación.
Auditoría completa y conciliación independiente por pares/corte; vacío,
fronteras, errores compensados y escalas 40/400 comprobados. Los controles
materializan registros Python y no constituyen ejecución con memoria acotada.
No incorpora DuckDB, cambia renv ni afirma rendimiento.
10.03 desarrolla DataFrame/LazyFrame, scan/collect_schema/explain/collect con
ejemplos autónomos de seis filas y Parquet nuevo. Plan lógico sin optimizar/
optimizado, dependencias de filtro/proyección y ejecución real conciliada por
clave con CSV externo: 003/2600 y resumen 4500/4600 MXN. Auditoría completa
separada de consulta nativa; vacío, fronteras, errores compensados/fuera del
filtro y suma amplia comprobados en procesos nuevos. Sin nuevas dependencias
ni cambios de lockfiles; el plan no mide I/O físico, tiempo ni memoria acotada.
10.04 añade tipos/conversión con originales, null/NaN y agregaciones con
cobertura en muestras independientes, además de seis saldos y catálogo propio
de tres claves. Left m:1 conserva 4500/4600 MXN, cuatro coincidencias y dos
productos conocidos sobre seis observaciones; distingue etiqueta pendiente
de falta de catálogo. Inner/semi/anti y full opcional, duplicados sin uso,
claves ausentes y vacío comprobados. Referencia Python estándar y contraste
de seis campos por fila con pandas/SQLite; sin nuevas dependencias ni mediciones.
10.05 desarrolla la extensión opcional de collect streaming, lotes consumidos
sin acumular y sink Parquet con destinos nuevos. Plan físico DOT y trazas;
seis filas, uno/2600 o tres/4600 MXN conciliados por clave. Auditoría completa
separada; vacío, fronteras, sumas amplias y escalas 40/400/1998 comprobados.
Observador en procesos nuevos Windows con PeakWorkingSetSize en bytes,
incluye arranque/consulta/escritura sin auditoría del padre. Sin dependencias
nuevas, benchmark, medición I/O físico ni promesa de RAM acotada; soporte de
estado/fallback según operación y versión.
10.06 incorpora DuckDB 2.0.0 con lockfile y dos entornos uv locales, sin alterar
registros previos salvo la dependencia del proyecto. SQL sobre Parquet completo/
partes y unión pequeña; fuente autónoma de seis filas, 003/2600 y resumen
4500/4600 MXN. Esquema de cada archivo y valores auditados contra CSV externo;
EXPLAIN/EXPLAIN ANALYZE distinguen plan/ejecución, sin acreditar I/O físico ni
RAM acotada. Vacío, fronteras, sumas amplias, partes omitidas/duplicadas y
alteraciones comprobados. 10.06 no modifica renv ni incorpora cliente R.
10.07 incorpora recorridos autónomos Python/R con SQL parametrizado compartido,
tipos/clases nativas, páginas y cierre de resultados/conexiones ante errores.
Conserva seis filas, 003/2600 y resumen 4500/4600 MXN como texto decimal exacto;
auditoría completa y lectura cruzada, sin compartir base persistente entre versiones.
Python DuckDB 2.0.0 permanece; R DuckDB 1.5.6/DBI 1.3.0 se registran junto con
dbplyr 2.6.0/blob 1.3.0 inferidos por renv. Respaldo del mismo proyecto, 46 registros
previos idénticos y segunda restauración vacía comprobados. No cambia bibliotecas
globales ni acredita RAM acotada.
10.08 desarrolla pandas/Arrow/Polars/DuckDB en memoria con ocho etapas conciliadas:
esquemas antes de adaptar, equivalencia string/large_string acotada y comparación
por clave. Mantiene seis filas, 003/2600 y 4500/4600 MXN; muestra independiente
de ausencia/vacío/cero (suma 10, cobertura 2/3), índice e integer/float.
Relación/registro frente a Table y lector; no acredita ausencia de copias ni RAM
acotada. R opcional registra Arrow y recupera por DBI antes de reconstruir Arrow.
Sin paquetes ni lockfiles nuevos; procesos nuevos y ambos entornos Python/R
existentes comprobados.
10.09 mide el mismo Parquet/pregunta/salida JSON en pandas/Polars/DuckDB:
tres observaciones por motor en procesos nuevos con orden rotado y pools a uno.
Seis fases, consulta/intervalo/proceso y pico residente absoluto Windows, sin
confundirlos con I/O físico o RAM exclusiva del motor. CSV externo y exportaciones
conciliados fuera del trabajador; crudas/resumen y verificador de solo lectura.
Mantiene seis filas/003/2600; vacíos, precisión y alteraciones comprobados.
Caché SO sin vaciar y entrada leída en auditoría; medición local sin generalización.
R opcional system.time es un protocolo distinto de tabla en memoria/DBI.
Sin paquetes/lockfiles nuevos.
10.10 integra selección/resumen en los tres motores con cuarenta filas propias,
fuente/contrato, seis Parquet de resultados y verificador de solo lectura.
Seis seleccionados/14061 MXN y grupos 26030/27690; Int64 antes de sumar, con cota
didáctica de 1998 filas. Referencia Python estándar/R base y relectura por clave.
Mediciones nuevas de selección con protocolo 10.09; no se atribuyen al resumen
o entrega completa. Decisión editable con campos/evidencia revisados y argumento
para revisión humana; huellas no autentican tiempos. Las diez secciones tienen
material, sin activar proyecto/checkpoints. La 11.01 ya inicia la preparación editorial.
Los ejemplos conservan contexto propio.
El estado y las condiciones pendientes están en [cierre de almacenamiento](storage-closure.md).

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

Los cuatro módulos tienen 37 secciones y referencias oficiales; 11.01–11.04 disponen
de lección/lab y las otras 33 siguen planificadas.
El flujo es reporte → una app elegida → integración final;
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

[11.01](../curriculum/11_reporting_quarto/01_report_source_render/README.md) usa
seis filas propias para tres créditos en dos cortes (6000/6300 MXN, +300 y 5%).
Preparadores independientes Python estándar/R base validan las seis claves y
generan copia de entrada, pares, resumen y borrador Markdown con cifras insertadas.
Es preparación editorial, no render Quarto; no añade dependencias ni modifica
entornos. El lab cambia una copia de entrada y conserva ambas preparaciones.
El primer `.qmd`/HTML está implementado en 11.02; ejecución Jupyter/knitr en 11.03.
El proyecto y sus checkpoints siguen pendientes.

[11.02](../curriculum/11_reporting_quarto/02_first_document/README.md) incorpora
un primer documento de texto y otro preparado desde seis filas propias, con
reglas/narrativa de 11.01 reutilizadas sin exigir entregas previas. Python/R
calculan y escriben el `.qmd`; Quarto 1.9.38/Pandoc 3.8.3 incluidos en RStudio
renderizan HTML con recursos de presentación incluidos. YAML, Markdown, código
mostrado frente a ejecutable, render/preview y distribución local. No hay
bloques ejecutables ni nuevas dependencias: cambiar CSV exige preparar de nuevo
y después renderizar. La ejecución Jupyter/knitr se desarrolla en 11.03.

[11.03](../curriculum/11_reporting_quarto/03_execution_python_r/README.md) usa
documentos separados que leen un CSV propio y ejecutan funciones desde cero.
Grupo Python notebooks con nbclient 0.10.2/nbformat 5.10.4/PyYAML 6.0.3 e
ipykernel 6.30.1 conservado. R incorpora knitr 1.52/rmarkdown 2.32 con lockfile
real; preserva 50 registros y añade 21. Extensión del proyecto renv con respaldo
o arranque autónomo desde su configuración local, sin exigir entregas previas.
Comprobaciones del intérprete real del kernel y del proyecto/biblioteca R;
sin caché ni daemon Python. El render lee datos de nuevo; errores detienen
la ejecución. No modifica entornos globales ni activa proyecto/checkpoints.

[11.04](../curriculum/11_reporting_quarto/04_tables_figures_references/README.md)
reutiliza las funciones/entornos de 11.03 con CSV propio y sin exigir entregas.
Párrafo con código en línea, tabla por crédito y barras del agregado desde el
mismo resultado. Matplotlib/IPython y ggplot2/knitr ya declarados; sin paquetes
ni cambios de metadatos. Identificadores, captions, texto alternativo, referencias
cruzadas y bibliografía local, separada de la procedencia de datos sintéticos.
Los renders deben revisarse también por advertencias de referencias/citas:
una salida exitosa no garantiza que esas claves estén resueltas.

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
módulos vigentes. Su integración requiere revisar prerrequisitos y referencias.

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

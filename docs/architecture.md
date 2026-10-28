# Arquitectura del repositorio

La arquitectura separa enseñanza, práctica, integración y publicación. Esto
evita que un notebook aislado tenga que funcionar al mismo tiempo como lección,
ejercicio, solución y producto final.

Las [plantillas para nuevos proyectos](../templates/learning-project/README.md)
separan instrucciones de agentes y método de diseño del recorrido. Esta
arquitectura documenta su aplicación específica a DS Track.

## Flujo del conocimiento

```text
lección → lab asociado → comprobar y explicar → evidencia → bitácora personal
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

Orienta sobre fuentes compartidas. Las muestras actuales y sus diccionarios
están junto a las lecciones; crear un catálogo o generadores centrales cuando
exista una necesidad real. Los datos voluminosos se regeneran localmente.

### `templates/`

Reduce decisiones repetidas. Aquí viven las estructuras base para crear nuevos
módulos, proyectos, reportes o aplicaciones.

### `showcase/`

Contiene resultados terminados y seguros para compartir: reportes renderizados,
capturas, demostraciones o enlaces. No es un directorio de trabajo.

## Dependencias

Los requisitos Python vigentes se declaran en [pyproject.toml](../pyproject.toml)
y su resolución está en [uv.lock](../uv.lock). Las lecciones explican el camino
Conda, venv + pip o uv cuando corresponde; elegir uno no implica practicar los tres.
El mini proyecto uv de 00.05 es independiente del proyecto raíz usado con pandas.

R utiliza renv desde [06.08](../curriculum/06_r_foundations/08_projects_renv/README.md)
en copias autocontenidas, con biblioteca y estado locales. El mismo proyecto de
práctica crece con los módulos posteriores; sus preparadores conservan metadatos
y entregas previas. No se inicializa renv en la raíz ni se modifican bibliotecas
globales para revisar documentación. Verificar reconstrucción cuando cambien
dependencias; no instalar herramientas solo por planificar.

## Datos del recorrido

Comenzar con ventas ficticias para introducir texto, tipos, rutas y cálculos.
Después usar una cartera completamente sintética, con unidad de fila, claves,
diccionario y reglas explícitas. Las muestras viven junto a las lecciones;
reutilizarlas mediante enlaces sin exigir entregas personales previas.

Preservar originales y motivos de rechazo; no imputar, truncar ni eliminar
duplicados sin una regla. Separar observaciones aceptadas, cobertura y resultados
conocidos. Las reglas para fuentes y generadores están en la
[política de datos](data-policy.md).

## Rutas de profundización previstas

El orden vigente es 00–14. [ROADMAP.md](../ROADMAP.md) define capacidades y
prerrequisitos; los [índices de módulo](../curriculum/README.md) contienen el
alcance por sección. La disponibilidad y la bitácora de comprobaciones están en
[PROGRESS.md](../PROGRESS.md), sin repetir aquí el inventario de cada desarrollo.

### Desarrollo previsto de los módulos 02–05

- [02 — pandas](../curriculum/02_pandas/README.md): tablas, contratos, selección,
  transformación y resumen; cierre con notebook y primera gráfica.
- [03 — SQL](../curriculum/03_sql_databases/README.md): modelo relacional,
  consultas, uniones, ventanas, transacciones e integración con pandas.
- [04 — Visualización Python](../curriculum/04_visualization_python/README.md):
  pregunta, geometrías, escalas, comunicación, composición e interacción opcional.
- [05 — Python aplicado](../curriculum/05_python_applied/README.md): código
  reutilizable y comprobable. Su profundización no bloquea empezar pandas.

Los cuatro módulos tienen material; sus proyectos/checkpoints no se activan por
tener lecciones disponibles. Los ejemplos concretos y sus resultados viven en
las lecciones y labs, no en una segunda descripción técnica de cada sección.

### Python aplicado: del notebook al proyecto

Python fundamental conserva tipos, colecciones, condiciones, funciones,
lectura CSV y validación. El módulo 05 profundiza organización en módulos y
paquetes, configuración, registro, recursos, pruebas y contratos; incorpora
extensiones de objetos por composición, iteración, decoradores, medición y APIs.
Funciones y composición preceden a especializaciones de objetos. Concurrencia,
asincronía, metaprogramación y herencia necesitan una justificación concreta.

El notebook apoya exploración; las transformaciones reutilizables se separan de
la presentación y de la interfaz. La disponibilidad de un paquete o prueba de
referencia no sustituye una implementación propia explicada.

### Visualización: entender antes de construir aplicaciones

La primera gráfica aparece en pandas. [04](../curriculum/04_visualization_python/README.md)
y [08](../curriculum/08_visualization_r/README.md) profundizan la comunicación
del mismo análisis: población, medida, agregación, escalas, etiquetas, alternativas
al color, composición y exportación. Cambiar de biblioteca no exige repetir toda
la limpieza ni altera por sí solo el universo del indicador.

Matplotlib/Altair y ggplot2 son las rutas de gráficos. Después se elige una
aplicación: Streamlit cuenta con 12.01–12.09; la ruta
Shiny dispone de 13.01–13.06; el resto conserva planes. Ambas separan transformación y validación de la interfaz;
elegir una aplicación es suficiente. El [estado de Streamlit](streamlit-closure.md)
distingue material disponible, práctica y evidencia de cierre.

### Recorrido de los módulos 06–08

[06 — R fundamental](../curriculum/06_r_foundations/README.md) enseña su modelo de
vectores y faltantes, funciones, archivos y reconstrucción del entorno.
[07 — tidyverse](../curriculum/07_tidyverse/README.md) amplía importación,
transformación, calidad, relaciones, categorías, fechas y primera figura.
[08 — Visualización R](../curriculum/08_visualization_r/README.md) profundiza
gramática, escalas, paneles, comunicación, composición y entrega visual.

El recorrido principal de R utiliza el IDE elegido: editar, ejecutar bloques,
inspeccionar objetos y repetir el script completo tras reiniciar sesión.
Rscript sirve cuando el objetivo lo requiere o como apoyo. Las lecturas y sus
autorías están en la [guía de R](r-reading-guide.md); los criterios de práctica e
integración están en [cierre de tidyverse](tidyverse-closure.md).

### Almacenamiento y procesamiento: 09–10

[09 — Arrow/Parquet](../curriculum/09_arrow_parquet/README.md) trata contratos,
lectura/escritura, intercambio Python/R, datasets, metadatos y entrega verificable.
[10 — Polars/DuckDB](../curriculum/10_polars_duckdb/README.md) compara operaciones,
ejecución, intercambio y costos con la misma pregunta y una referencia externa.

Comparar tipos antes de adaptar y valores por clave después de releer; las sumas
iguales no bastan. Separar auditoría completa de proyección/filtro y los tiempos
de consulta de validación/escritura. Lazy, streaming, un plan o una muestra pequeña
no demuestran RAM acotada, I/O físico ni rendimiento general. Los límites de
medición y criterios de integración están en [cierre de almacenamiento](storage-closure.md).

### Entrega prevista del producto: 11–14

[11 — Quarto](../curriculum/11_reporting_quarto/README.md) dispone de reportes con
texto, código, tablas y figuras reconstruibles; un motor y HTML bastan para el
cierre esencial. PDF, publicación y autenticación son ampliaciones.
[12 — Streamlit](../curriculum/12_streamlit/README.md) dispone de 12.01–12.09;
incluye pruebas de funciones/AppTest y entrega local reconstruible (12.09), con referencia externa por clave.
[13 — Shiny](../curriculum/13_shiny_web/README.md) dispone de 13.01–13.06: primeras apps
con proyecto renv independiente y biblioteca local, sin exigir entregas del
proyecto de análisis previo. 13.02 conecta entradas/salidas y 13.03 introduce dependencias, invalidación y demanda. 13.04 comparte selección/indicadores sobre una cartera de seis observaciones, con los mismos metadatos de app. 13.05 incorpora aplicación por evento y estado por sesión; 13.06 distingue rechazo, vacío, falta de universo y fallas de fuente con recuperación. 13.07–13.10 y
[14 — Proyectos reproducibles](../curriculum/14_reproducible_projects/README.md)
conservan planes. Elegir 12 o 13 antes de integrar 14, sin exigir dos aplicaciones.

El [cierre de reportes](reporting-closure.md) separa material, práctica y proyecto.
El portal local facilita lectura y práctica acompañada; no implementa esos
proyectos ni acredita aprendizaje por una visita o respuesta guardada.

### R aplicado: consideración para el próximo ajuste

Sigue pendiente decidir un puente de organización, funciones reutilizables,
errores, pruebas y medición en R después de visualización. No tiene módulo ni
numeración nueva: antes de integrarlo hay que revisar prerrequisitos y referencias.
Terminal avanzada también permanece pendiente de diseño.

### Ubicación actual de módulos y proyectos

La secuencia completa y sus alternativas están en el
[índice del curriculum](../curriculum/README.md). Los
[proyectos](../projects/README.md) son planes hasta que exista una práctica
integradora con entradas, producto, rúbrica y checkpoints enlazados.

Los índices orientan; las lecciones explican; los labs ejercitan; los documentos
de cierre reúnen criterios de integración. Crear contenido útil antes de añadir
carpetas o dependencias. Material terminado y aprendizaje demostrado son estados
distintos.

## Registro de decisiones

### Portal local: entrada, módulo inicial y prueba 02.01

[portal/](../portal/README.md) contiene una capa Quarto sobre curriculum/labs existentes.
La navegación distingue portada, contenido 00–14 y primer módulo 00. Sus seis
lecciones/labs y apoyos se generan desde los originales; 00.05 conserva A/B y
recorridos por gestor. La sesión acompañada 02.01 permanece como prueba adicional.
Catálogos explícitos seleccionan fuentes y descargas; la generación adapta enlaces
y escribe una copia nueva bajo output, excluida de Git. No ejecuta ejemplos ni
instala paquetes. Las fuentes de consulta fuera del piloto se ofrecen con su
ubicación en el clon y descarga, sin convertir todo el curriculum.

El notebook vive junto a su lab y viaja con el script auxiliar. Una preparación
protegida o el ZIP crea la copia personal. El servidor sirve únicamente el sitio
generado en 127.0.0.1; no publica ni añade backend de aprendizaje. La bitácora
usa guardado explícito en el navegador y exportación Markdown, sin sincronización.
PROGRESS.md conserva estado editorial; la evidencia personal del portal va en
la copia de cada participante. El código se versiona; salidas y datos personales no.
El arranque detecta fuentes cambiadas y selecciona o prepara una copia actualizada,
conservando las anteriores. Prueba técnica disponible, revisión del contenido y
observación de sesión real pendientes. La [propuesta de publicación](portal-publication.md)
documenta etapas y decisiones; no se ha desplegado un servicio en Internet.

Registrar las decisiones vigentes en esta arquitectura o en su guía responsable,
con contexto y consecuencias cuando aporten información. El historial de cambios
y comprobaciones permanece en PROGRESS.md y Git; no mantener otro registro vacío
ni agregar infraestructura por anticipación.

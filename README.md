# DS Track

Ruta de aprendizaje práctica para manipulación, análisis, almacenamiento y
comunicación de datos.

El repositorio está diseñado para avanzar por etapas. Los fundamentos aparecen
antes que las herramientas de mayor escala, y cada nivel termina con un
resultado observable. Git ayuda a publicar y conservar el material, pero no es
un requisito para estudiar: el contenido también debe funcionar al descargarlo
como ZIP.

## Empieza aquí

Estudia una lección a la vez. Sigue este flujo en cada sesión:

1. **Comprende:** lee la lección y conversa sobre los conceptos y ejemplos.
   Anota lo que no entiendas para revisarlo con quien te acompaña.
2. **Practica:** realiza el lab asociado. Intenta resolverlo y usa la lección
   como referencia cuando lo necesites.
3. **Comprueba:** compara tu resultado con la evidencia y el criterio de salida
   del lab. Revisa los errores y vuelve a intentarlo si hace falta.
4. **Explica:** responde las preguntas de reflexión con tus propias palabras.
   Cuenta qué hiciste, por qué y cómo sabes que funcionó.
5. **Registra y continúa:** anota tu evidencia, dudas y siguiente paso en
   [PROGRESS.md](PROGRESS.md). Avanza cuando puedas demostrar la habilidad;
   si quedan conceptos esenciales pendientes, repásalos antes.

Si estudian juntos, quien acompaña puede explicar y dar pistas; quien aprende
realiza la práctica y explica su resultado. Cada sesión puede cubrir solo una
parte de la lección: no necesitas terminar un módulo de una vez.

### Tu primera sesión

Tu primera meta es escribir tu presentación en Markdown y crear tu perfil en
GitHub. Para esta primera lección solo necesitas un editor de texto y, si vas
a publicar el perfil, una cuenta de GitHub.

1. Lee [01 — Markdown y tu perfil en GitHub](curriculum/00_getting_started/01_github_profile/README.md)
   para entender Git, GitHub y los archivos `.md`.
2. Copia la [plantilla del perfil](templates/github-profile/PROFILE.md) y
   personaliza tu nombre, usuario y objetivos.
3. Completa el [lab 00.01 — Markdown y perfil](labs/00_getting_started/01_github_profile/README.md)
   y comprueba que tu README se ve correctamente.
4. Registra tu resultado y tus dudas en [PROGRESS.md](PROGRESS.md).

Después continúa con [02 — Terminal y rutas](curriculum/00_getting_started/02_terminal_paths/README.md)
y luego con [03 — Git e historial](curriculum/00_getting_started/03_git_workflow/README.md).
Consulta el [índice del nivel 0](curriculum/00_getting_started/README.md) para
seguir la secuencia completa.

## Principios

- Bases antes que herramientas: Python, pandas, SQL y modelado primero.
- Una sola historia de datos: la cartera sintética crece con el recorrido.
- Aprender haciendo: explicación breve, práctica guiada, reto y proyecto.
- Comparar con evidencia: rendimiento, memoria, claridad y mantenibilidad.
- Datos seguros: nunca se versionan datos reales, secretos ni PII.
- Complejidad gradual: R, Parquet, Polars, DuckDB, Quarto y Shiny se incorporan
  cuando resuelven una necesidad ya entendida.

## Mapa del repositorio

| Ruta | Propósito |
| --- | --- |
| [`curriculum/`](curriculum/) | Módulos ordenados de aprendizaje |
| [`PROGRESS.md`](PROGRESS.md) | Módulo activo, siguiente paso y bitácora |
| [`labs/`](labs/) | Ejercicios breves y deliberados |
| [`projects/`](projects/) | Proyectos que integran varios módulos |
| [`datasets/`](datasets/) | Datos pequeños y sintéticos, generadores y diccionarios |
| [`templates/`](templates/) | Plantillas reutilizables para nuevo material |
| [`showcase/`](showcase/) | Resultados terminados para compartir |
| [`docs/`](docs/) | Arquitectura, reglas de contenido y seguridad |

La relación entre lecciones, práctica y proyectos se explica en
[`docs/learning-workflow.md`](docs/learning-workflow.md).

## Recorrido de aprendizaje

Cada paso desarrolla una capacidad que se aplica en el siguiente. El recorrido
empieza con tu perfil y termina con un proyecto que puedes reconstruir y explicar.

![Recorrido de DS Track: fundamentos, análisis y construcción de productos](docs/assets/learning-roadmap.svg)

La publicación del perfil y el uso de Git son prácticas recomendadas. También
puedes seguir el recorrido con el material descargado como ZIP.

Consulta [`ROADMAP.md`](ROADMAP.md) para ver los resultados y criterios de
avance de cada nivel.

## Cómo estudiar

Como apoyo, la [guía de Visual Studio Code](docs/vscode-guide.md) explica cómo
editar, previsualizar Markdown y ejecutar comandos, con atajos para Windows.

El recorrido también está pensado para aprender acompañado: una persona realiza
las prácticas y otra explica conceptos, revisa resultados y ayuda a resolver dudas.

Para cada módulo:

1. Lee sus objetivos y conceptos.
2. Ejecuta los ejemplos.
3. Resuelve los ejercicios sin mirar la solución.
4. Aplica lo aprendido al checkpoint de proyecto cuando exista.
5. Registra la evidencia y las dudas pendientes en `PROGRESS.md`.
6. Avanza cuando cumplas el criterio de salida, no solo por haber leído todo.

En una sesión acompañada, empieza con una explicación breve, realiza la práctica
y cierra explicando con tus propias palabras qué hiciste y por qué. Usa las
preguntas del lab para conversar y comprobar lo aprendido.

## Estado actual

El nivel 0 dispone de sus seis lecciones y labs para revisión y práctica. Python
fundamental dispone de sus seis lecciones, desde
[variables y tipos](curriculum/01_python_foundations/01_variables_types/README.md)
hasta [validación y resumen](curriculum/01_python_foundations/06_validation_summary/README.md).
pandas comienza con [Series y DataFrame](curriculum/02_pandas/01_series_dataframe/README.md),
[Leer, inspeccionar y exportar](curriculum/02_pandas/02_read_inspect_export/README.md),
[Seleccionar, filtrar y ordenar](curriculum/02_pandas/03_select_filter_sort/README.md),
[Tipos y columnas calculadas](curriculum/02_pandas/04_types_calculated_columns/README.md),
[Faltantes, duplicados y reglas](curriculum/02_pandas/05_missing_duplicates_rules/README.md),
[Texto y fechas](curriculum/02_pandas/06_text_dates/README.md),
[Agrupar y resumir](curriculum/02_pandas/07_group_summarize/README.md),
[Combinar tablas](curriculum/02_pandas/08_combine_tables/README.md),
[Cambiar la forma de una tabla](curriculum/02_pandas/09_reshape_tables/README.md) y
[Análisis y primera gráfica](curriculum/02_pandas/10_analysis_plot/README.md), con sus labs.
El módulo pandas tiene sus diez lecciones disponibles. SQL dispone de [sus nueve lecciones y labs](curriculum/03_sql_databases/README.md),
desde el modelo relacional hasta [Integración pandas y SQL](curriculum/03_sql_databases/09_pandas_sql/README.md),
con indicadores conciliados y gráfica. Visualización dispone de
[04.01 — Pregunta y elección de gráfico](curriculum/04_visualization_python/01_question_chart/README.md),
[04.02 — Matplotlib: Figure y Axes](curriculum/04_visualization_python/02_figure_axes/README.md),
[04.03 — Comparaciones y evolución](curriculum/04_visualization_python/03_comparisons_evolution/README.md),
[04.04 — Distribuciones y relaciones](curriculum/04_visualization_python/04_distributions_relationships/README.md),
[04.05 — Escalas, etiquetas y accesibilidad](curriculum/04_visualization_python/05_scales_labels_accessibility/README.md),
[04.06 — Composición y exportación](curriculum/04_visualization_python/06_composition_export/README.md),
[04.07 — Altair: visualización declarativa](curriculum/04_visualization_python/07_altair_declarative/README.md),
[04.08 — Interacción con Altair (opcional)](curriculum/04_visualization_python/08_altair_interaction/README.md) y
[04.09 — Cierre visual del análisis](curriculum/04_visualization_python/09_visual_closure/README.md),
con sus labs. Las nueve secciones de visualización están disponibles, con
interacción opcional. Python aplicado comienza con
[05.01 — Del notebook a módulos](curriculum/05_python_applied/01_notebook_to_modules/README.md),
con paquete local, script, notebook y lab, y
[05.02 — Configuración y registro](curriculum/05_python_applied/02_configuration_logging/README.md),
con argumentos, JSON, logging y lab, y
[05.03 — Errores y recursos](curriculum/05_python_applied/03_errors_resources/README.md),
con fallas controladas, cierre de recursos, JSON atómico y lab.
[05.04 — Pruebas de código y datos](curriculum/05_python_applied/04_testing/README.md)
añade unittest, casos conocidos, fronteras, vacíos, fallas e integración, con lab.
[05.05 — Tipos y contratos](curriculum/05_python_applied/05_types_contracts/README.md)
añade anotaciones, docstrings, parámetros opcionales y validación explícita,
con ejemplos comprobados y lab.
[05.06 — Clases, composición y dataclasses](curriculum/05_python_applied/06_classes_composition/README.md)
añade una ampliación opcional con objetos pequeños, configuración y lab.
[05.07 — Iteradores y generadores](curriculum/05_python_applied/07_iterators_generators/README.md)
añade consumo por lotes, conciliación, recursos y límites de memoria, con lab
opcional. [05.08 — Funciones como valores y decoradores](curriculum/05_python_applied/08_functions_decorators/README.md)
añade reenvío de argumentos, wraps y registro de etapas con errores conservados,
con lección/lab de extensión.
[05.09 — Medir antes de optimizar](curriculum/05_python_applied/09_measure_optimize/README.md)
añade mediciones repetidas, perfiles, memoria y comparación de contratos con lab
de extensión.
[05.10 — Integración con APIs](curriculum/05_python_applied/10_api_integration/README.md)
añade páginas JSON simuladas, límites, reintentos y normalización conciliada,
con pruebas y lab de extensión.
[05.11 — Cierre del proyecto Python](curriculum/05_python_applied/11_project_closure/README.md)
integra ejecución, figura, verificación de archivos y reconstrucción con lab.
Las once secciones de Python aplicado tienen material disponible.
El nivel 06 dispone de [06.01 — R, editor, scripts y paquetes](curriculum/06_r_foundations/01_r_session/README.md),
con script y lab, y de [06.02 — Objetos, vectores y tipos](curriculum/06_r_foundations/02_objects_vectors/README.md),
con ventas vectorizadas, coerción y reciclaje.
[06.03 — Seleccionar elementos](curriculum/06_r_foundations/03_subsetting/README.md)
añade posiciones, nombres, máscaras y estructura devuelta, con script y lab.
[06.04 — Lógica y valores faltantes](curriculum/06_r_foundations/04_logic_missing/README.md)
añade condiciones, pendientes y resúmenes con cobertura, con script y lab.
06.05–06.09 y los niveles 07–08 conservan sus planes y
[lecturas abiertas de R](docs/r-reading-guide.md). Los niveles 09–10 tienen planes
de Arrow/Parquet y Polars/DuckDB; los niveles 11–14 tienen secciones definidas
para reportes, una aplicación elegida y proyecto final. El
avance del material no acredita finalización de las prácticas del estudiante.
El [índice del curriculum](curriculum/README.md) incluye las rutas previstas de
Python aplicado, visualización y aplicaciones en Python y R en su orden de estudio. El
avance diario y el siguiente paso se mantienen en [`PROGRESS.md`](PROGRESS.md).

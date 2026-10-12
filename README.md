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
pandas comienza con [Series y DataFrame](curriculum/02_pandas/01_series_dataframe/README.md)
y su lab. Las secciones restantes de 02–05 conservan su plan para desarrollar una por una;
los niveles 06–08 también tienen secciones definidas y
[lecturas abiertas de R](docs/r-reading-guide.md). Los niveles 09–14 conservan
su planificación general. El
avance del material no acredita finalización de las prácticas del estudiante.
El [índice del curriculum](curriculum/README.md) incluye las rutas previstas de
Python aplicado, visualización y aplicaciones en Python y R en su orden de estudio. El
avance diario y el siguiente paso se mantienen en [`PROGRESS.md`](PROGRESS.md).

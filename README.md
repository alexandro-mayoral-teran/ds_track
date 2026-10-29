# ![](docs/assets/ds-track-icon.svg)DS Track

**Aprende a trabajar con datos, paso a paso y en compañía.**

Un recorrido práctico para manipular, analizar, almacenar y comunicar datos.
Puedes estudiar directamente desde este repositorio o desde una copia descargada.
Cada lección conecta explicación, práctica, comprobación y evidencia.

[**Empieza aquí**](#empieza-aqui) · [**Ver módulos**](curriculum/README.md) · [**Cómo estudiar**](#como-estudiar) · [**Mapa**](#mapa-del-recorrido)

> **Tu punto de partida:** [00 — Entorno de aprendizaje](curriculum/00_getting_started/README.md).
> No necesitas experiencia previa con terminal o programación. Git y la
> publicación del perfil son prácticas recomendadas; también puedes estudiar con un ZIP.

## Mapa del recorrido

![Recorrido de DS Track: fundamentos y análisis en Python; R y procesamiento; reportes, una aplicación y proyecto final](docs/assets/learning-roadmap.svg)

| Etapa | Qué construirás | Módulos |
| --- | --- | --- |
| **Prepara y analiza** | Entorno, programas, tablas, consultas y gráficas | [00–05](curriculum/README.md) |
| **Amplía tus herramientas** | Análisis en R e intercambio/procesamiento de datos | [06–10](curriculum/README.md) |
| **Comunica e integra** | Reportes, una aplicación y proyecto reproducible | [11–14](curriculum/README.md) |

**Material:** la base de lecciones y labs de 00–14 está disponible, incluida la
[revisión final de 14.09](curriculum/14_reproducible_projects/09_final_review_defense/README.md).
Streamlit (12) y Shiny (13) son alternativas: basta una antes de 14. La práctica
y la [depuración transversal](docs/reproducible-projects-closure.md) continúan.
Los proyectos y checkpoints requieren consultar su estado en
[proyectos](projects/README.md). Material disponible no significa práctica completada.

<a id="empieza-aqui"></a>

## Empieza aquí

| Si estás en este punto… | Abre… |
| --- | --- |
| **Es mi primera sesión** | [00.01 — Markdown y tu perfil](curriculum/00_getting_started/01_github_profile/README.md) y su [lab](labs/00_getting_started/01_github_profile/README.md) |
| **Quiero ver el orden del primer módulo** | [00 — Entorno de aprendizaje](curriculum/00_getting_started/README.md) |
| **Ya conozco las bases y busco un tema** | [Índice de módulos](curriculum/README.md) |
| **Quiero encontrar una práctica** | [Índice de labs](labs/README.md), después de la lección correspondiente |
| **Quiero retomar lo que hice** | Mi copia de práctica y mi nota de evidencia; para empezar, [plantilla de 00](templates/learning-session/bitacora-00.md) |

La primera práctica es una presentación en Markdown. Basta un editor de texto;
si eliges publicarla como perfil, necesitarás una cuenta de GitHub. Las demás
herramientas se introducen cuando hacen falta.

<a id="como-estudiar"></a>

## Cómo estudiar

| Paso | Tu acción | Con tu compañero |
| --- | --- | --- |
| **1 · Comprende** | Lee la lección y predice el resultado | Conversen sobre el ejemplo |
| **2 · Practica** | Haz el lab en tu propia copia | Una persona escribe; la otra pregunta |
| **3 · Comprueba** | Contrasta valores, estructura y errores | Revisen las reglas y cambien de papel |
| **4 · Explica** | Justifica el resultado y prueba una variante | Cada persona explica con sus palabras |
| **5 · Registra** | Guarda archivo, dudas y siguiente paso | Acuerden qué falta antes de continuar |

Una sesión puede cubrir solo parte de una lección. Usa las pistas cuando hagan
falta y abre las soluciones después de intentar la práctica. Avanza cuando
puedas demostrar y explicar la habilidad, no solo por haber leído la página.

Para la muestra 00.01 conserva tu presentación y una nota personal. El
[flujo de aprendizaje](docs/learning-workflow.md) explica la relación entre
lecciones, labs y evidencia. [PROGRESS.md](PROGRESS.md) registra el estado editorial
del proyecto; no es un porcentaje de aprendizaje de cada participante.

## Encuentra el material

| Quiero… | Dónde |
| --- | --- |
| Seguir el recorrido | [curriculum/](curriculum/README.md) |
| Practicar una habilidad | [labs/](labs/README.md) |
| Consultar una integración o checkpoint | [projects/](projects/README.md) |
| Entender capacidades y prerrequisitos | [ROADMAP.md](ROADMAP.md) |
| Ver el estado del material | [PROGRESS.md](PROGRESS.md) |

<details>
<summary><strong>Apoyos de estudio y portal local</strong></summary>

- [Guía de VS Code](docs/vscode-guide.md): apoyo opcional para editar y previsualizar.
- [Datos sintéticos](datasets/README.md): muestras, generadores y diccionarios.
- [Plantillas](templates/): archivos reutilizables.
- [Portal local](portal/README.md): otra forma de leer el contenido; el repo permite estudiar por sí mismo.

El portal se abre desde la raíz con `python portal/servir.py --abrir`.
Su código está versionado; las prácticas y evidencias personales quedan fuera de Git.

</details>

<details>
<summary><strong>Para quien crea o revisa material</strong></summary>

- [Cómo contribuir](CONTRIBUTING.md).
- [Índice de documentación](docs/README.md): guías vigentes y responsabilidad de cada una.
- [Guía de autoría](docs/authoring-guide.md).
- [Presentación y navegación en Markdown](docs/markdown-study-guide.md).
- [Arquitectura del recorrido](docs/architecture.md).
- [Resultados para compartir](showcase/).

Conserva datos sintéticos y originales; no publiques secretos, datos reales o
información personal. Las fuentes educativas están en curriculum/ y labs/.
Las muestras empiezan con ventas ficticias y después introducen otros dominios.

</details>

[Volver al inicio ↑](#ds-track)

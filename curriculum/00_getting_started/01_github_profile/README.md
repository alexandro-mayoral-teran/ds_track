# 00.01 — Markdown y tu perfil en GitHub

<a id="01--markdown-y-tu-perfil-en-github"></a>

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.01**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Presentarte con Markdown y distinguir Git de GitHub |
| **Necesitas** | Editor de texto; cuenta de GitHub solo si publicas |
| **Evidencia** | README previsualizado y una explicación con tus palabras |

[Material de apoyo](#material-de-apoyo) · [Conceptos](#en-esta-lección) · [Ir al lab](../../../labs/00_getting_started/01_github_profile/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

> **Antes de empezar:** esta es la lección 00.01, dentro de Entorno de aprendizaje.
> Los comandos de Git llegan en 00.03. Puedes realizar la práctica sin publicar un perfil.

## Propósito

Escribir y previsualizar Markdown, distinguir Git de GitHub y crear una
presentación desde la web. Los comandos de Git se estudian en la lección 03.

<a id="prerrequisitos"></a>

## Antes de empezar

Basta con un editor de texto. La publicación requiere una cuenta de GitHub.
No necesitas usar la terminal ni instalar Git para esta lección.

Trabaja en un archivo de texto llamado `README.md` y utiliza una vista previa
de Markdown. Si eliges hacerlo desde GitHub, puedes escribir y previsualizar
en su editor web. No necesitas publicar para completar la práctica.

## Qué vas a aprender

- Distinguir Git de GitHub y una copia local de una remota.
- Escribir títulos, listas, énfasis y enlaces en Markdown y comprobar su vista previa.
- Adaptar una presentación con tus objetivos reales de aprendizaje.
- Explicar otro uso de Markdown y qué tendrías que comprobar al usarlo con IA.

## Material de apoyo

Abre cada recurso cuando aparezca en el recorrido. Puedes consultarlos de nuevo
desde esta tabla; no necesitas descargar todo para comenzar.

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Vista previa de Markdown](../../../docs/vscode-guide.md#4-leer-markdown-con-vista-previa) | Comparar fuente y resultado en VS Code | Apoyo si eliges ese editor |
| [Plantilla de perfil](../../../templates/github-profile/PROFILE.md) | Copiar una base y adaptarla en tu README | Para la actividad del perfil |
| [Cómo adaptar la plantilla](../../../templates/github-profile/README.md) | Revisar qué sustituir y cómo presentar tus aprendizajes | Consulta opcional |
| [Bitácora personal de 00](../../../templates/learning-session/bitacora-00.md) | Anotar evidencia, dudas y revisión con tu compañero | Formato opcional; también sirve una nota propia |

Aquí trabajarás con texto Markdown. Los notebooks y scripts se incorporan en
las lecciones que los necesitan. Las fuentes para profundizar están en
[Referencias](#referencias).

## En esta lección

1. [Markdown: qué es, para qué sirve y cómo probarlo](#1-markdown-escribir-y-dar-estructura).
   [Otros casos de uso](#otros-casos-de-uso), incluidos prompts y skills como introducción.
2. [Git y GitHub: conservar y compartir](#2-git-y-github-conservar-y-compartir).
3. [Crear tu perfil desde la web](#crear-el-perfil-desde-la-web).

<a id="2-markdown-escribir-y-dar-estructura"></a>

## 1. Markdown: escribir y dar estructura

<a id="un-archivo-de-texto-que-puedes-leer-sin-herramientas-especiales"></a>

### Qué es Markdown

**Markdown** es un lenguaje de marcado ligero: permite organizar texto plano
con marcas sencillas para que una herramienta lo presente con formato. `.md`
es la extensión habitual del archivo. El editor muestra el texto fuente y la
vista previa lo presenta con formato. `README.md` suele explicar qué contiene un
repositorio y cómo usarlo.

Puedes abrirlo con un editor de texto y leerlo incluso sin vista previa. Las
marcas describen la estructura: `#` introduce un título, `-` una lista y los
corchetes con paréntesis un enlace. Cambiar la extensión de un documento de Word
a `.md` no lo convierte en Markdown: su contenido debe ser texto plano.

Markdown estructura el documento; no ejecuta programas. Un bloque con comandos
los muestra como ejemplo, pero debes ejecutarlos por separado si la actividad lo pide.

### Para qué sirve y qué problemas resuelve

Sirve para escribir documentos fáciles de leer, revisar y reutilizar. Por
ejemplo, una nota puede explicar qué hiciste, qué necesitas y qué sigue; un
README puede orientar a quien abre tu proyecto por primera vez.

| Problema al compartir información | Cómo ayuda Markdown |
| --- | --- |
| Todo aparece como un bloque de texto | Los títulos y las listas separan temas y pasos |
| Se confunden explicación, ejemplo y código | Las secciones y las marcas permiten distinguirlos |
| Quieres revisar o adaptar el documento en otro editor | El contenido es texto plano que puedes leer y modificar |

Imagina que entregas un archivo sin explicar qué contiene. Un README con
«Propósito», «Archivos» y «Cómo empezar» ayuda a otra persona a orientarse.
Markdown aporta la estructura; tú decides qué información necesita quien lee.
No tienes que empezar por un perfil público: también sirve para tus apuntes.

### Primera prueba: escribir y previsualizar

Ahora prueba esas marcas en un documento pequeño. Crea tu propio archivo
README.md y copia estas cinco líneas:

```markdown
# Mi presentación

Estoy aprendiendo Markdown.

- Quiero documentar mis prácticas.
```

Si usas VS Code, abre la paleta de comandos y busca **Markdown: Open Preview
to the Side** para mantener fuente y vista previa juntas. La
[guía de vista previa](../../../docs/vscode-guide.md#4-leer-markdown-con-vista-previa)
explica cómo abrirla. Si ya elegiste el editor web de GitHub, usa su vista previa.
Elige una opción: para este ejercicio basta un archivo .md; el notebook llega
en 00.06 y no es necesario preparar Python ni un kernel aquí.

**Resultado de esas mismas líneas:**

> # Mi presentación
>
> Estoy aprendiendo Markdown.
>
> - Quiero documentar mis prácticas.

Compara ambos: el signo # produce el título y el guion produce una viñeta.
Cambia una palabra, guarda y observa la vista previa. Después cambia # por ##:
¿qué diferencia ves? Conserva el texto y explica qué marca produce cada cambio.

### Las marcas que usarás primero

| Quieres escribir | Texto fuente | Qué verás en la vista previa |
| --- | --- | --- |
| Título principal | `# Mi perfil` | Un encabezado de primer nivel |
| Sección | `## Mis objetivos` | Un encabezado de segundo nivel |
| Énfasis | `**Python**` | **Python** |
| Lista | `- Aprender SQL` | Un elemento con viñeta |
| Enlace | `[GitHub](https://github.com)` | [GitHub](https://github.com) |
| Código en línea | `` `README.md` `` | `README.md` |

Deja líneas en blanco entre párrafos, encabezados y listas. Para mostrar varias
líneas de código, enciérralas entre dos líneas de tres acentos graves, como el
ejemplo siguiente.

### Texto fuente y resultado

Copia este ejemplo en un archivo `.md` o en el editor de GitHub. Alterna entre
edición y vista previa: identifica qué marca produce cada parte del resultado.

```markdown
# Hola, soy Tu Nombre

Estoy aprendiendo análisis de datos.

## Lo que quiero aprender

- Python y SQL.
- Documentar y reproducir mis análisis.

## Mi recorrido

Puedes visitar [DS Track](https://github.com/alexandro-mayoral-teran/ds_track).

Mi primer comando será `git status`.
```

**Así se presenta el ejemplo anterior:**

> # Hola, soy Tu Nombre
>
> Estoy aprendiendo análisis de datos.
>
> ## Lo que quiero aprender
>
> - Python y SQL.
> - Documentar y reproducir mis análisis.
>
> ## Mi recorrido
>
> Puedes visitar [DS Track](https://github.com/alexandro-mayoral-teran/ds_track).
>
> Mi primer comando será `git status`.

Comprueba que el título, las dos viñetas, el enlace y el código en línea
corresponden al texto fuente. git status se muestra como texto: no hay que
ejecutarlo en esta práctica. Los colores y tamaños pueden variar según el editor.

El nombre `README.md` es una convención: indica el documento que conviene leer
primero. En un proyecto suele explicar su propósito, cómo ejecutarlo y dónde
encontrar ejemplos; en tu perfil, sirve para presentarte.

> **Para comprobar:** cambia un título de `#` a `##` y observa la vista previa.
> Después explica qué cambió en la estructura del documento.

<a id="3-otros-usos-del-perfil-a-tus-proyectos"></a>

### Otros casos de uso

La presentación es una primera aplicación. La misma estructura de texto sirve
para organizar información en situaciones distintas:

| Caso | Qué información puedes organizar |
| --- | --- |
| Apuntes y bitácoras de aprendizaje | Qué intentaste, qué comprobaste, dudas y siguiente paso |
| README de un proyecto | Propósito, archivos necesarios e instrucciones para empezar |
| Diccionario de datos | Columnas, significado, unidades y valores ausentes |
| Notas de reunión o decisiones | Acuerdos, motivos y tareas por realizar |
| Explicaciones en un notebook | Pregunta, interpretación y conclusiones junto al código |
| Sitio de documentación | Páginas que una herramienta transforma en un sitio navegable |
| Plantillas de colaboración | Qué cambió, por qué y qué debe revisar otra persona |
| Contexto e instrucciones para IA | Objetivo, datos de contexto, ejemplos y cómo comprobar la respuesta |

Por ejemplo, [Jupyter](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html)
admite celdas Markdown, [MkDocs](https://www.mkdocs.org/user-guide/writing-your-docs/)
construye documentación a partir de archivos Markdown y
[GitHub](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
permite plantillas Markdown para proponer cambios. Son casos para reconocer;
no necesitas preparar esas herramientas en esta lección.

#### Organizar contexto e instrucciones para IA

Un **prompt** es la petición que pasas a una herramienta de IA. Puede incluir
qué necesitas, el contexto y cómo quieres comprobar el resultado. Markdown
ayuda a separar esas partes, como explica la
[documentación de prompts de OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering):

```markdown
# Objetivo
Explícame la diferencia entre # y ## en Markdown.

## Contexto
Estoy escribiendo mi primera presentación.

## Cómo lo comprobaré
Dame un ejemplo breve y pídeme que prediga cómo se verá antes de mostrarlo.
```

Puedes guardar y reutilizar esa petición. Una **skill** agrupa instrucciones
reutilizables y, cuando hacen falta, recursos para una tarea. Por ejemplo,
revisar varios README con los mismos criterios. En herramientas compatibles,
como Codex, esas instrucciones se describen en un archivo `SKILL.md` y pueden
acompañarse de plantillas o ejemplos. La
[documentación de skills de OpenAI](https://developers.openai.com/plugins/concepts/skills)
muestra cómo se organiza ese material.

Aquí basta con reconocer la conexión: escribir con estructura puede ayudarte
a comunicarte con personas y a pasar contexto a una IA. Un archivo .md no se
carga automáticamente en cualquier herramienta ni garantiza una respuesta
correcta. Escribe y explica el ejemplo; crear una skill o instalar una IA queda
fuera de esta primera práctica.

> **Para explorar:** elige otro caso de uso. ¿Quién leería ese documento y qué
> información necesitaría para utilizarlo?

<a id="1-git-y-github-conservar-y-compartir"></a>

## 2. Git y GitHub: conservar y compartir

### Git: entender cómo cambió un archivo

**Git** es un sistema de control de versiones: registra cambios en archivos y
permite consultar su historial. Un **repositorio** reúne archivos y ese historial.
Un **commit** guarda los cambios preparados con un mensaje que explica la intención.
Git puede funcionar localmente sin conexión a GitHub.

Imagina que hoy escribes tu presentación y mañana cambias tus objetivos. Podrías
guardar archivos como `perfil_final.md` y `perfil_final_ahora_si.md`, pero pronto
sería difícil saber cuál usar y qué cambió. Con Git mantienes el nombre del
archivo y registras versiones en su historial.

Un commit puede incluir cambios en varios archivos. Su mensaje describe el
motivo: por ejemplo, «Agrega mis objetivos de aprendizaje». Así puedes comparar
versiones, consultar cómo era el contenido antes y recuperar cambios anteriores.

### GitHub: compartir el repositorio y trabajar juntos

**GitHub** es una plataforma para alojar repositorios Git, compartir trabajo y
colaborar. El repositorio de tu computadora es **local**; el alojado en GitHub es
**remoto**. Guardar un archivo, crear un commit y subirlo son acciones diferentes.

En GitHub puedes leer documentación, explorar el historial e invitar a alguien
a colaborar. También existen **issues**, para registrar preguntas o tareas, y
**pull requests**, para proponer cambios y revisarlos antes de integrarlos.
Por ahora basta con reconocer estas posibilidades; las practicarás más adelante.

| Concepto | Qué representa | Ejemplo en tu perfil |
| --- | --- | --- |
| Git | Herramienta para controlar versiones | Conservar cambios del README |
| GitHub | Plataforma para alojar y colaborar | Mostrar tu presentación en la web |
| Repositorio | Archivos y su historial | El repositorio con tu nombre de usuario |
| Commit | Registro de cambios seleccionados | «Agrega mis objetivos» |
| Local | Repositorio en tu computadora | La copia que editarás en la lección 03 |
| Remoto | Repositorio accesible por una conexión | La copia alojada en GitHub |

Cuando editas y guardas desde GitHub, la plataforma crea un commit en el
repositorio remoto. En la lección 03 harás el proceso desde tu computadora.

> **Para conversar:** si editas un archivo en tu computadora, ¿cambia
> automáticamente la copia de GitHub? Explica tu respuesta.

<details>
<summary>Pista para contrastar tu explicación</summary>

Piensa dónde se guardó el cambio: en tu computadora o en el repositorio remoto.
Guardar un archivo local no modifica automáticamente GitHub. Más adelante
aprenderás a registrar y enviar cambios; aquí basta distinguir ambas copias.

</details>

## Crear el perfil desde la web

1. Identifica tu nombre de usuario de GitHub.
2. Crea un repositorio **público** con exactamente ese nombre y agrega un README.
   Para `alexandro-mayoral-teran`, el repositorio es `alexandro-mayoral-teran`.
   Si ya existe, edita su README.
3. Copia la [plantilla de perfil](../../../templates/github-profile/PROFILE.md)
   al README. Sustituye los datos de ejemplo y adapta tu presentación, lo que
   estás aprendiendo y un objetivo concreto. Las
   [instrucciones de la plantilla](../../../templates/github-profile/README.md)
   explican qué conservar.
4. Usa la vista previa para comprobar títulos, listas y enlaces.
5. Guarda con un mensaje de commit descriptivo y visita tu perfil.

Este repositorio del perfil es distinto del repositorio privado `ds_track`.
Puedes completar la práctica sin cuenta guardando y previsualizando el README
localmente. Los iconos, tarjetas de estadísticas y automatizaciones son extensiones.

<a id="práctica-y-criterio-de-salida"></a>

## Práctica

Realiza el [lab 00.01](../../../labs/00_getting_started/01_github_profile/README.md).
Crearás una presentación propia y contrastarás el texto fuente con su vista previa.

## Evidencia y criterio de salida

Puedes avanzar cuando expliques Git frente a GitHub y fuente frente a vista previa,
y tu README muestre la presentación y los objetivos con formato correcto.
Si eliges publicarlo, comprueba que aparece en tu perfil.

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Tu README adaptado | Títulos, listas, énfasis y enlaces se presentan como esperabas | Qué cambia entre texto fuente y vista previa |
| Una nota breve | Distingues Git, GitHub y copia local/remota | Por qué guardar localmente no actualiza GitHub |
| Tus objetivos de aprendizaje | Sustituiste el texto de ejemplo y abriste los enlaces | Qué quieres aprender y cómo se reconoce en tu presentación |
| Otro uso de Markdown | Puedes describir quién leería ese documento y para qué | Qué información necesita; si usas IA, cómo comprobarías su respuesta |

Quien aprende modifica el README y explica el resultado. Su compañero revisa
un enlace y pide un cambio pequeño, como convertir un título en una sección.
Para registrar la revisión puedes copiar la
[bitácora personal de 00](../../../templates/learning-session/bitacora-00.md)
o escribir una nota propia junto al README. La evidencia personal no se guarda
en la bitácora editorial del curso.

No hay proyecto de datos asociado todavía; el README es la primera evidencia.

## Referencias

- [Git: fundamentos del control de versiones](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones).
- [README de perfil de GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).
- [Sintaxis de Markdown en GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [Markdown: presentación original de John Gruber](https://daringfireball.net/projects/markdown/).
- Los casos de uso y la introducción a prompts/skills enlazan sus fuentes primarias en [Otros casos de uso](#otros-casos-de-uso).

<a id="siguiente-lección"></a>

## Siguiente paso

Después del lab y su comprobación, continúa con
[00.02 — Terminal y rutas](../02_terminal_paths/README.md).
Después aprenderás a actualizar el perfil con Git en la lección 03.

[← Módulo 00](../README.md) · [Practicar: lab 00.01](../../../labs/00_getting_started/01_github_profile/README.md) · [Siguiente: 00.02 →](../02_terminal_paths/README.md)

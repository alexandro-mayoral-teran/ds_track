# 01 — Markdown y tu perfil en GitHub

[Inicio](../../../README.md) / [Módulo 00](../README.md) / **Lección 00.01**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Presentarte con Markdown y distinguir Git de GitHub |
| **Necesitas** | Editor de texto; cuenta de GitHub solo si publicas |
| **Evidencia** | README previsualizado y una explicación con tus palabras |

[Conceptos](#en-esta-lección) · [Crear el perfil](#crear-el-perfil-desde-la-web) · [Ir al lab](../../../labs/00_getting_started/01_github_profile/README.md) · [Comprobar](#práctica-y-criterio-de-salida)

> **Antes de empezar:** esta es la lección 00.01, dentro de Entorno de aprendizaje.
> Los comandos de Git llegan en 00.03. Puedes realizar la práctica sin publicar un perfil.

## Propósito

Escribir y previsualizar Markdown, distinguir Git de GitHub y crear una
presentación desde la web. Los comandos de Git se estudian en la lección 03.

## Prerrequisitos

Basta con un editor de texto. La publicación requiere una cuenta de GitHub.
No necesitas usar la terminal ni instalar Git para esta lección.

## En esta lección

1. [Git y GitHub: conservar y compartir](#1-git-y-github-conservar-y-compartir).
2. [Markdown: escribir y dar estructura](#2-markdown-escribir-y-dar-estructura).
3. [Otros usos: del perfil a tus proyectos](#3-otros-usos-del-perfil-a-tus-proyectos).
4. [Crear tu perfil desde la web](#crear-el-perfil-desde-la-web).

## 1. Git y GitHub: conservar y compartir

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

## 2. Markdown: escribir y dar estructura

### Un archivo de texto que puedes leer sin herramientas especiales

**Markdown** es una forma de estructurar texto plano con marcas sencillas. `.md`
es la extensión habitual del archivo. El editor muestra el texto fuente y la
vista previa lo presenta con formato. `README.md` suele explicar qué contiene un
repositorio y cómo usarlo.

Puedes abrirlo con un editor de texto y leerlo incluso sin vista previa. Las
marcas describen la estructura: `#` introduce un título, `-` una lista y los
corchetes con paréntesis un enlace. Cambiar la extensión de un documento de Word
a `.md` no lo convierte en Markdown: su contenido debe ser texto plano.

Markdown es un lenguaje de marcado ligero. Te permite estructurar un documento;
no ejecuta programas. Un bloque con comandos los muestra como ejemplo, pero
debes ejecutarlos por separado si la actividad lo pide.

### Las marcas que usarás primero

| Quieres escribir | Texto fuente | Qué verás en la vista previa |
| --- | --- | --- |
| Título principal | `# Mi perfil` | Un encabezado de primer nivel |
| Sección | `## Mis objetivos` | Un encabezado de segundo nivel |
| Énfasis | `**Python**` | **Python** |
| Lista | `- Aprender SQL` | Un elemento con viñeta |
| Enlace | `[GitHub](https://github.com)` | [GitHub](https://github.com) |
| Código en línea | Una palabra entre acentos graves | `README.md` |

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

El nombre `README.md` es una convención: indica el documento que conviene leer
primero. En un proyecto suele explicar su propósito, cómo ejecutarlo y dónde
encontrar ejemplos; en tu perfil, sirve para presentarte.

> **Para comprobar:** cambia un título de `#` a `##` y observa la vista previa.
> Después explica qué cambió en la estructura del documento.

## 3. Otros usos: del perfil a tus proyectos

El perfil es una primera aplicación. Los mismos conceptos te servirán cuando
empieces a analizar datos o a construir programas.

### Documentar y organizar el aprendizaje

Puedes escribir apuntes, instrucciones de instalación, diccionarios de datos
y explicaciones de tus decisiones en Markdown. Al guardarlos en Git, también
puedes consultar cómo evolucionaron esas explicaciones.

| Situación | Qué puedes construir con lo aprendido |
| --- | --- |
| Terminas una práctica | Una nota con resultado, dudas y siguiente paso |
| Compartes un script | Un README que explique qué hace y cómo ejecutarlo |
| Preparas datos | Un diccionario con columnas, tipos y significado |
| Encuentras un error | Un issue con pasos para reproducirlo y el resultado esperado |
| Trabajas con otra persona | Una propuesta de cambio que puedan revisar juntos |

### Organizar contexto e instrucciones para IA

Markdown también puede ayudarte a ordenar una petición para una herramienta de
IA. Separar objetivo, contexto y resultado esperado facilita leer, revisar y
reutilizar la petición. Por ejemplo:

```markdown
# Objetivo
Ayúdame a comprender la diferencia entre Git y GitHub.

## Contexto
Estoy creando mi primer perfil y todavía no he usado la terminal.

## Cómo quiero practicar
- Explica con un ejemplo basado en un README.
- Hazme dos preguntas antes de mostrar las respuestas.

## Cómo comprobaré lo aprendido
Debo poder explicar qué hace Git y qué aporta GitHub con mis propias palabras.
```

Puedes conservar este texto como un apunte y adaptarlo para otros temas. En
herramientas que lo admiten, también existen archivos de instrucciones de
proyecto; GitHub Copilot, por ejemplo, utiliza
[`.github/copilot-instructions.md`](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

La estructura ayuda a expresar la petición, pero la precisión depende de lo
que escribas. Un archivo `.md` no se carga automáticamente en cualquier IA y
la respuesta debe comprobarse. Para esta lección basta con escribir y explicar
el ejemplo; no necesitas instalar una herramienta de IA.

> **Para explorar:** elige un uso distinto del perfil y cuenta qué documento
> crearías, quién lo leería y qué información necesitaría.

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

## Práctica y criterio de salida

Realiza el [lab 00.01](../../../labs/00_getting_started/01_github_profile/README.md).
Puedes avanzar cuando expliques Git frente a GitHub y fuente frente a vista previa,
y tu README muestre la presentación y los objetivos con formato correcto.
Si eliges publicarlo, comprueba que aparece en tu perfil.

| Comprueba | Cómo lo reconoces |
| --- | --- |
| Fuente y vista previa | Identificas las marcas Markdown y su presentación |
| Git y GitHub | Explicas herramienta, plataforma y copia local/remota |
| Presentación propia | Sustituiste los ejemplos por objetivos reales de aprendizaje |
| Enlaces | Abren el destino que esperabas |

No hay proyecto de datos asociado todavía; el README es la primera evidencia.

## Siguiente lección

Continúa con [02 — Terminal y rutas](../02_terminal_paths/README.md).
Después aprenderás a actualizar el perfil con Git en la lección 03.

## Referencias

- [Git: fundamentos del control de versiones](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones).
- [README de perfil de GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).
- [Sintaxis de Markdown en GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [Instrucciones de repositorio para Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

---

[← Módulo 00](../README.md) · [Practicar: lab 00.01](../../../labs/00_getting_started/01_github_profile/README.md) · [Siguiente: 00.02 →](../02_terminal_paths/README.md)

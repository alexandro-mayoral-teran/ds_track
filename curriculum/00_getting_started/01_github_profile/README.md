# Git, GitHub, Markdown y tu primer perfil

## Propósito

Crear una presentación que pueda crecer con tus proyectos mientras aprendes a
documentar y conservar cambios. Esta práctica se divide en dos sesiones: primero
el README desde la web; después, su actualización desde la terminal.

## Prerrequisitos

Para la primera parte basta con un editor de texto. La publicación requiere una
cuenta de GitHub. Para la segunda parte completa la
[lección de terminal y rutas](../02_terminal_paths/README.md) e instala Git.

## Conceptos

**Git** es un sistema de control de versiones: registra cambios en archivos y
permite consultar su historial. Un **repositorio** reúne archivos y ese historial.
Un **commit** guarda los cambios preparados con un mensaje que explica la intención.
Git puede funcionar localmente sin conexión a GitHub.

**GitHub** es una plataforma para alojar repositorios Git, compartir trabajo y
colaborar. El repositorio de tu computadora es **local**; el alojado en GitHub es
**remoto**. Guardar un archivo, crear un commit y subirlo son acciones diferentes.

**Markdown** es una forma de estructurar texto plano con marcas sencillas. `.md`
es la extensión habitual del archivo. El editor muestra el texto fuente y la
vista previa lo presenta con formato. `README.md` suele explicar qué contiene un
repositorio y cómo usarlo.

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

El repositorio de DS Track es privado: su enlace solo permite acceder a personas
autorizadas. Puedes mencionar el recorrido sin incluir un enlace por ahora.

## Markdown e IA

Los títulos, listas y bloques de código permiten organizar contexto, requisitos
y ejemplos en documentos que pueden leer tanto personas como herramientas de IA.
Por ejemplo, GitHub Copilot admite instrucciones de repositorio en
`.github/copilot-instructions.md`.

El formato ayuda a separar ideas, pero no garantiza que una IA las siga ni que
su respuesta sea correcta. Un archivo Markdown tampoco se vuelve una instrucción
activa por existir: la herramienta debe admitirlo y cargarlo. Practica escribiendo
un objetivo concreto, los datos disponibles y cómo comprobar el resultado.

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

## Actualizar desde la terminal

Después de la práctica de terminal, clona el repositorio del perfil en una carpeta
separada de DS Track. Como ya lo creaste con un README, clonar conserva su historial.
Sustituye `TU_USUARIO` por tu usuario real:

```text
git clone https://github.com/TU_USUARIO/TU_USUARIO.git
cd TU_USUARIO
git status
```

Edita el README y luego ejecuta:

```text
git diff
git add README.md
git diff --staged
git commit -m "Describe mis objetivos de aprendizaje"
git push
git status
```

`diff` permite revisar antes de guardar. `add` prepara los cambios; `commit`
los registra localmente; `push` los envía al remoto. La autenticación puede
solicitarse al clonar o publicar. Si Git pide tu identidad de autor, configura
tu nombre y un correo verificado o el correo privado de GitHub antes del commit.

Si `push` indica que hay cambios remotos pendientes, consulta `git status` y
el historial antes de continuar. No uses `--force` como solución inicial.

## Práctica y criterio de salida

Realiza primero la parte A del [lab `00.01`](../../../labs/00_getting_started/01_github_profile/README.md).
Después completa la lección y el lab de terminal antes de volver a la parte B.
Puedes avanzar cuando expliques Git frente a GitHub, fuente frente a vista previa
y archivo guardado frente a commit. Si publicas el perfil, comprueba también
que tu actualización aparece en GitHub.

No hay proyecto de datos asociado todavía; el README es la primera evidencia.

## Referencias

- [Git: fundamentos del control de versiones](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones).
- [README de perfil de GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).
- [Sintaxis de Markdown en GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [Instrucciones de repositorio para Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

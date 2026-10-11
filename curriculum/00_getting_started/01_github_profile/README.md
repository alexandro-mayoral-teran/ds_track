# 01 — Markdown y tu perfil en GitHub

## Propósito

Escribir y previsualizar Markdown, distinguir Git de GitHub y crear una
presentación desde la web. Los comandos de Git se estudian en la lección 03.

## Prerrequisitos

Basta con un editor de texto. La publicación requiere una cuenta de GitHub.
No necesitas usar la terminal ni instalar Git para esta lección.

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

## Práctica y criterio de salida

Realiza el [lab 00.01](../../../labs/00_getting_started/01_github_profile/README.md).
Puedes avanzar cuando expliques Git frente a GitHub y fuente frente a vista previa,
y tu README muestre la presentación y los objetivos con formato correcto.
Si eliges publicarlo, comprueba que aparece en tu perfil.

No hay proyecto de datos asociado todavía; el README es la primera evidencia.

## Siguiente lección

Continúa con [02 — Terminal y rutas](../02_terminal_paths/README.md).
Después aprenderás a actualizar el perfil con Git en la lección 03.

## Referencias

- [Git: fundamentos del control de versiones](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones).
- [README de perfil de GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).
- [Sintaxis de Markdown en GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [Instrucciones de repositorio para Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

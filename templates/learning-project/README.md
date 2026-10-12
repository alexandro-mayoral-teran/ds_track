# Bases para un nuevo proyecto de lecciones

Estas plantillas recogen el método del recorrido y se pueden adaptar a otros temas.
No contienen el historial, las versiones, la numeración o las autorizaciones
particulares de DS Track.

| Plantilla | Copiar en el nuevo proyecto como | Función |
| --- | --- | --- |
| [AGENTS.template.md](AGENTS.template.md) | AGENTS.md, en la raíz | Cómo debe trabajar el agente y qué decisiones respetar |
| [ARCHITECTURE.template.md](ARCHITECTURE.template.md) | docs/architecture.md | Cómo diseñar el recorrido y documentar su arquitectura |

## Cómo usarlas

1. Copia ambos archivos en el nuevo proyecto con los nombres de destino indicados.
   Crea docs si hace falta; no necesitas copiar todas las carpetas de este repositorio.
2. Completa los campos {{...}}: tema, público, conocimientos previos, modalidad,
   resultado final, límites y forma de comprobarlo. Elimina lo que no corresponda.
3. Decide si AGENTS.md será local o versionado. Para conservarlo solo en ese
   checkout Git, añade la línea /AGENTS.md a .git/info/exclude y comprueba
   git check-ignore AGENTS.md. Esa exclusión no se transmite al clonar.
   Para una política compartida, define expresamente qué se versionará.
4. Pide al agente que lea AGENTS.md y docs/architecture.md antes de trabajar.
   La forma de cargar instrucciones depende de la herramienta utilizada;
   conservar un Markdown no lo activa automáticamente en cualquier aplicación.
5. Investiga y define el mapa de módulos, secciones y prácticas. Después crea
   README.md, ROADMAP.md y el registro de estado que se haya elegido.
6. Revisa el orden y comienza por una lección concreta. Crea ejemplos, labs y
   proyectos cuando se implemente contenido real, sin carpetas vacías anticipadas.

## Solicitud inicial de ejemplo

```text
Lee AGENTS.md y docs/architecture.md de este proyecto.
Quiero un recorrido de lecciones sobre [tema] para [público y nivel],
con el objetivo de que pueda [capacidad observable].
Investiga fuentes reconocidas y propone módulos, prerrequisitos, secciones,
prácticas y criterios de cierre. Distingue lo esencial de las ampliaciones.
Deja la arquitectura, el roadmap y los índices coherentes, con material futuro
marcado como planificación. Después desarrollaremos las lecciones una por una.
```

Sustituye el tema y el resultado antes de usarlo. Las decisiones de gestores,
lenguajes, duración y publicación deben corresponder al nuevo proyecto.

## Qué copiar después, si hace falta

Las plantillas [de módulo](../module/README.md), [lab](../lab/README.md) y
[proyecto](../project/README.md) ayudan a desarrollar contenido. Las guías actuales
[de autoría](../../docs/authoring-guide.md) y
[de flujo de aprendizaje](../../docs/learning-workflow.md) sirven como referencia;
adaptar sus ejemplos y enlaces al nuevo tema.

La [arquitectura de DS Track](../../docs/architecture.md) muestra una aplicación
concreta del método. Usa las dos plantillas para comenzar otro proyecto y evita
copiar como reglas generales sus herramientas, rutas o decisiones específicas.

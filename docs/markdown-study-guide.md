# Presentación y navegación para estudiar desde Markdown

## Propósito y alcance

Que el repositorio sirva como material de estudio sin necesitar el portal.
Aplicar una jerarquía visual y una navegación repetibles, conservando las fuentes
educativas y la lectura como texto. Acuerdo de trabajo: 2026-10-27.

La portada, los índices y las lecciones disponibles aplican el patrón documentado.
Consulta la [cobertura vigente](README.md#cobertura-de-las-plantillas-y-del-portal)
para distinguir páginas adaptadas, labs conservados y material integrado en el
portal. La [lección/lab 00.01](../curriculum/00_getting_started/01_github_profile/README.md)
sigue como referencia inicial; 12.01–12.09 aplican la plantilla a material nuevo y
13.01–13.10 también tienen material nuevo; 14.01–14.05 tienen material de diseño, estructura, entornos, reprocesamiento y pruebas; 14.06–14.09 conservan su plan.

## Niveles de navegación

| Nivel | Debe resolver | Presentación |
| --- | --- | --- |
| Portada del repo | Qué es, por dónde empezar y dónde encontrar el material | Descripción breve, accesos directos, mapa y ruta inicial |
| Índice del curriculum | Encontrar módulos y elegir la siguiente etapa | Tablas por etapas, ruta inicial y estado breve; detalle editorial fuera de la introducción |
| Índice de módulo | Prerrequisitos, orden y producto de cada práctica | Ficha breve y tabla lección/lab/resultado |
| Lección y lab | Ubicación, tarea, comprobación y continuidad | Navegación, ficha, índice y cierre reconocibles |

Los detalles de autoría, herramientas opcionales y enlaces administrativos
pueden quedar en desplegables. No esconder preparación necesaria, actividad,
criterio de salida ni siguiente lección. El estado editorial vive en PROGRESS.md;
evitar volver a enumerar cada avance de desarrollo en la portada.

## Patrón de página de módulo

La [guía de página de módulo](module-page-guide.md) define la cabecera y ocho
secciones comunes, con su propósito, contenido y límites. Usa la
[plantilla](../templates/module/README.md) y el índice 00 como referencia aplicada.
Esa estructura organiza el módulo; no sustituye la explicación de cada lección.

Los índices 00–14 incluyen el desplegable común **Ver el alcance de las secciones**
después de su tabla. Está cerrado por defecto y complementa la elección de
lecciones; no oculta preparación ni cierre. En las secciones 14.06–14.09 pendientes, la planificación se indica
también fuera del desplegable. Los detalles de esta regla están en la guía de módulo.

## Patrón de lección

La [guía de lección](lesson-page-guide.md) desarrolla este patrón con una
evaluación de muestra, elementos comunes y variantes por actividad. La
[plantilla de lección](../templates/lesson/README.md) permite reutilizarlo.
La cobertura de lecciones y labs se mantiene en el índice de documentación;
no se deduce solo de la existencia de una plantilla.

1. Título y ubicación con módulo/número de lección.
2. Ficha breve: meta, preparación y evidencia esperada.
3. Accesos a conceptos, práctica y comprobación; índice si la página lo necesita.
4. Explicación gradual y ejemplos con resultado conocido.
5. Tablas para contrastes; imagen o esquema solo si aclara algo concreto.
6. Preguntas de predicción, pistas y errores frecuentes cuando aporten valor.
7. Acceso al lab y criterio de salida explícito.
8. Navegación final: módulo, lab y siguiente lección.

Si hay archivos de apoyo, añadir «Material de apoyo» después de los objetivos:
recurso, finalidad y uso necesario u opcional. Repetir el enlace donde se utiliza
con una instrucción concreta. La primera prueba 00.01 aplica ya el patrón de
lección y reúne sus plantillas; el material nuevo conserva esos elementos comunes.

Antes de la primera lección, el enlace de regreso lleva al módulo. En lecciones
posteriores puede añadirse la anterior. No confundir el módulo 00 con la lección
01 ni cambiar identificadores para ajustar la presentación.

## Patrón de lab

Mostrar relación con su lección, entrada, actividad, resultado y comprobación.
Reservar los desplegables para ayuda voluntaria y soluciones; cerrarlos por defecto.
La revisión por otra persona debe incluir explicación, no solo formato o conteos.
El siguiente paso enlaza una lección, no otro lab.

Las casillas, si se usan, son una guía personal. No marcar aprendizaje completado
en un archivo compartido ni generar porcentajes a partir de páginas visitadas.
Para 00.01, la evidencia va en la copia personal del README y su nota; no en el
registro editorial del proyecto.

## Recursos visuales y portabilidad

- Usar encabezados jerárquicos, listas cortas y tablas de pocas columnas.
- Preferir enlaces descriptivos y relativos; facilitar volver al módulo.
- Mantener el mapa SVG existente y una alternativa textual por etapas.
- Usar bloques destacados breves: `> **Antes de empezar:** ...` es legible en
  GitHub, otros visores y texto plano. No depender de CSS para transmitir significado.
- Usar details/summary con etiquetas claras, sin ocultar la actividad principal.
- Evitar tablas enormes, insignias decorativas, iconos sin texto y HTML complejo.
- No convertir todos los párrafos en recuadros ni añadir un diagrama por obligación.

GitHub admite avisos especiales, pero su apariencia puede variar en otros visores.
La muestra usa citas estándar con etiquetas en negrita. El portal sigue leyendo
los mismos Markdown: comprobar anclas, tablas y desplegables después de cambiar
la estructura; no crear una segunda lección para cada salida.

## Comprobación al aplicar el patrón

1. Verificar rutas y fragmentos, lección ↔ lab y continuidad.
2. Comprobar bloques de código, tablas, imágenes y cierre de desplegables.
3. Revisar el resultado renderizado y una ventana estrecha; registrar qué visor
   se utilizó. Un render local no acredita una inspección del GitHub remoto.
4. Si el material está integrado en el portal, ajustar su catálogo explícito
   para los enlaces nuevos y comprobar la generación sin ejecutar ejemplos.
5. Conservar contratos, datos, numeración y rutas anteriores salvo decisión explícita.

Esta guía complementa la [guía de autoría](authoring-guide.md) y el
[flujo de aprendizaje](learning-workflow.md). No sustituye sus criterios educativos.

## Referencias primarias

- [Sintaxis y enlaces en GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [Secciones desplegables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).

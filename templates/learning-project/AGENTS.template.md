# Instrucciones para agentes — {{NOMBRE_DEL_PROYECTO}}

Esta plantilla se copia como AGENTS.md en la raíz del nuevo proyecto. Sustituir
los campos {{...}} y retirar instrucciones que no correspondan. Contiene reglas
de trabajo; el historial y el avance se registran en los documentos del proyecto.

## Contexto y alcance

- Tema: {{TEMA_Y_PROBLEMA_QUE_SE_QUIERE_APRENDER}}.
- Público: {{CONOCIMIENTOS_PREVIOS_Y_NIVEL}}.
- Modalidad: {{AUTONOMA_ACOMPANADA_O_GRUPAL}}.
- Idioma y estilo: {{IDIOMA_Y_TONO}}; explicar sin asumir requisitos no declarados.
- Resultado del recorrido: {{CAPACIDAD_O_PRODUCTO_FINAL_OBSERVABLE}}.
- Fuera de alcance: {{TEMAS_Y_HERRAMIENTAS_QUE_NO_SON_REQUISITOS}}.
- Conservación de AGENTS.md: {{LOCAL_O_VERSIONADO_SEGUN_DECISION_DEL_PROYECTO}}.

Las instrucciones del usuario tienen prioridad. No trasladar autorizaciones,
datos personales, rutas, credenciales o decisiones de otro proyecto.
Conservar cambios existentes y trabajar dentro del alcance solicitado.

## Leer antes de modificar

Consultar los archivos que realmente existan y se hayan adoptado:

- README.md: propósito, cómo comenzar y flujo de estudio.
- ROADMAP.md: capacidades, orden, prerrequisitos y criterios de salida.
- docs/architecture.md: responsabilidades y decisiones de estructura.
- curriculum/README.md y README del módulo: secuencia y contenido de las secciones.
- PROGRESS.md o registro elegido: estado actual y próximo paso.
- Guías de autoría, contribución y políticas aplicables, si existen.

El estado no se mantiene como una segunda bitácora dentro de AGENTS.md. Si una
regla cambia, actualizarla y quitar su versión contradictoria; no acumular cada
conversación como una instrucción nueva. Los detalles de lecciones viven en ellas.

## Método de diseño

1. Partir de lo que la persona debe poder hacer y cómo lo demostrará.
2. Identificar conocimientos previos y ordenar conceptos por sus dependencias.
3. Investigar fuentes primarias o referencias de autoría reconocida cuando haga falta.
4. Definir secciones y prácticas antes de desarrollar todo el material.
5. Implementar una lección a la vez, comprobarla y actualizar su navegación.

Usar esencial, práctica, extensión y avanzado. Las ampliaciones no bloquean
capacidades esenciales posteriores. Una alternativa tecnológica no obliga a
estudiar todos los recorridos; compartir la teoría y separar ejemplos completos.

## Lecciones y formatos

Cada lección desarrollada incluye propósito, prerrequisitos, objetivos observables,
conceptos claros, ejemplo explicado, práctica, criterio de salida, siguiente paso
y referencias. Introducir un concepto antes de exigirlo en una práctica.

Markdown es apropiado para explicaciones. Utilizar otros formatos cuando aporten
valor: scripts para procesos repetibles, notebooks para exploración, imágenes o
diagramas para relaciones difíciles de explicar. No exigir todos en cada lección.
Si el tema no utiliza programación, adaptar ejemplos y evidencia a su disciplina.

Presentar pasos, razones y resultados esperados. Diferenciar lo que se predice
de lo observado. Usar tablas para comparar y encabezados para separar temas;
evitar párrafos densos y listas de herramientas sin propósito.

En recorridos por plataforma o lenguaje, completar uno antes de presentar el
otro. Identificar la plataforma de cada comando y explicar su ubicación de ejecución.
Comprobar referencias y versiones al implementar; no copiar capítulos completos
ni presentar una fuente de terceros como contenido propio.

## Práctica, evidencia y continuidad

- Cada lab desarrollado enlaza su lección, declara entradas, actividad, resultado,
  evidencia y comprobación; no introduce teoría esencial que falta en la lección.
- Las soluciones orientan y explican; si se ocultan con details/summary, quedan
  cerradas por defecto y se recomienda intentar primero.
- Navegación: lección → lab asociado → siguiente lección → siguiente lab.
  Enlazar lección y lab en ambos sentidos.
- Un checkpoint integra capacidades cuando existe un proyecto asociado. Si no
  existe, indicarlo; no crear uno vacío para completar un enlace.
- No enlazar archivos inexistentes ni presentar una sección planificada como lista
  para estudiar. Los planes pueden enlazar a su descripción dentro del documento.
- Leer no equivale a aprender; desarrollar material tampoco completa el estudio.
  Registrar finalización solo con evidencia del criterio de salida.

## Herramientas, muestras y verificación

Antes de añadir una herramienta, explicar necesidad, requisito, alternativa simple
y resultado esperado. Instalar dependencias solo al implementar un uso real.
Usar el entorno elegido del proyecto y evitar alterar instalaciones globales.
No agregar servicios, cuentas o infraestructura por anticipación.

Utilizar muestras pequeñas y reproducibles, con origen y condiciones de uso claros.
Preservar entradas cuando una práctica transforme archivos; distinguir fuente y
resultado generado. Cuando haya datos sensibles, utilizar muestras adecuadas al curso.

Verificar según el cambio: resultados conocidos, fronteras y casos vacíos en código;
ejecución desde cero en notebooks; enlaces y formato en documentación; legibilidad
y contenido de figuras o documentos. Elegir comprobaciones que detecten fallas reales,
sin agregar pruebas que solo repitan el texto o la implementación.

## Entrega y mantenimiento

Revisar el estado del repositorio antes de editar y preparar únicamente cambios
relacionados. Mantener coherentes índices, numeración, enlaces, diagramas y estados.
Comprobar qué archivos deben quedar locales, versionados o regenerables.

Respetar la autorización de publicación del usuario para este proyecto; no
inferirla de otro repositorio. No publicar instrucciones locales, datos privados,
credenciales, entornos o cachés. Un ejemplo de despliegue no exige desplegar.

Al cerrar, explicar qué cambió, cómo se comprobó, qué sigue pendiente y dónde
está disponible. Para retomar, consultar el registro de estado y la siguiente
lección, sin dar por terminado el aprendizaje por el avance del contenido.

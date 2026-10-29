# Guía para crear material

Para comenzar otro proyecto o tema, utiliza las
[plantillas de agentes y arquitectura](../templates/learning-project/README.md).
Esta guía orienta la autoría de contenido dentro del recorrido ya diseñado.

Para presentación y navegación, aplica la
[guía de estudio desde Markdown](markdown-study-guide.md). El
[índice de documentación](README.md#cobertura-de-las-plantillas-y-del-portal)
mantiene la cobertura por módulo; no dar por revisada toda la teoría al extender
una plantilla. El estado editorial y sus comprobaciones viven en PROGRESS.md.

## Estructura de un módulo

Usa la [plantilla de página de módulo](../templates/module/README.md) y la
[guía de sus ocho secciones](module-page-guide.md). El README del módulo orienta
el recorrido; las lecciones explican y los labs plantean la práctica.

```text
curriculum/NN_modulo/
  README.md              # Página de módulo
  01_tema/
    README.md            # Lección y ejemplos
labs/NN_modulo/
  01_tema/
    README.md            # Lab asociado
```

No es necesario crear todas las carpetas desde el primer momento. Deben aparecer
cuando contengan material útil.

## Estructura de una lección

Usa la [plantilla de lección](../templates/lesson/README.md) y la
[guía de sus elementos comunes](lesson-page-guide.md). La guía documenta una
evaluación de muestra y propone cabecera, propósito, preparación, objetivos,
material de apoyo cuando exista, desarrollo adaptable, práctica,
evidencia/comprobación, referencias y continuidad.
Las lecciones disponibles aplican la plantilla según la [cobertura vigente](README.md#cobertura-de-las-plantillas-y-del-portal).
El material nuevo debe partir de ella; adaptar la presentación no acredita una revisión completa de la teoría.

Cuando haya recursos de apoyo, reunirlos después de los objetivos en una tabla
«Recurso / Para qué sirve / Uso» y enlazarlos también justo antes de usarlos.
Identificar lo necesario y lo opcional; incluir solo archivos útiles y existentes,
sin exigir notebooks, scripts ni datos en todas las lecciones. Primera prueba
aplicada en [00.01](../curriculum/00_getting_started/01_github_profile/README.md).

### Contenido mínimo del README de lección

- Propósito.
- Prerrequisitos.
- Objetivos observables.
- Conceptos.
- Actividades.
- Criterio de salida.
- Referencias primarias.

## Ejemplos comprensibles por sección

Cada sección nueva presenta el contexto, los datos, las reglas y los resultados
necesarios para entender sus ejemplos sin recordar un ejercicio anterior.
Cuando sea posible, comenzar con una muestra pequeña definida en la propia
lección; después conectar con la base común para conciliar. Mantener enlaces
a conceptos previos y reutilizar funciones verificadas sin duplicar algoritmos.
Distinguir prerrequisitos conceptuales y preparación de entorno de la necesidad
de ejecutar entregas de capítulos anteriores. La revisión retroactiva del
material existente queda pendiente con el usuario.

## Diseño de ejercicios

Un ejercicio debe indicar:

- Qué se recibe.
- Qué se espera producir.
- Restricciones relevantes.
- Cómo comprobar el resultado.
- Pistas opcionales separadas de la solución.

Los labs se crean a partir de [`templates/lab/`](../templates/lab/) y deben
enlazar la lección que refuerzan. La lección debe enlazar el lab de regreso.

## Conexión con proyectos

Cuando una habilidad se aplique a un proyecto implementado, identifica un
checkpoint concreto. Si el proyecto todavía es un plan, indícalo sin inventar
un checkpoint disponible. No uses solamente frases generales como "se utilizará después".

Ejemplo de relación prevista, todavía sin proyecto implementado:

```text
Proyecto: 01_clean_credit_data
Checkpoint: CP-02 — Tratamiento de valores faltantes
```

Consulta [`learning-workflow.md`](learning-workflow.md) para las reglas de
enlace y seguimiento.

## Niveles de alcance

Marca cada sección como esencial, práctica, extensión o avanzada. Las secciones
de extensión y avanzadas nunca deben bloquear un módulo posterior esencial.

## Notebooks

- Reiniciar y ejecutar todas las celdas antes de publicar.
- Evitar estados ocultos y rutas absolutas.
- Explicar por qué se realiza cada transformación importante.
- Trasladar lógica repetida a funciones cuando ese aprendizaje ya se haya
  presentado.

## Ejecución en R e IDE

En las lecciones de R, el recorrido principal utiliza RStudio o el IDE elegido:
abrir el proyecto, editar un script, ejecutar bloques, inspeccionar objetos y
comprobar resultados. Distinguir la consola de R dentro del IDE de una terminal
del sistema; indicar dónde se ejecuta cada ejemplo.

Introducir terminal y Rscript cuando respondan a una necesidad concreta, como
automatizar o comprobar una ejecución completa desde una sesión nueva. Si son
una alternativa, presentarlos como apoyo opcional sin desplazar el objetivo de
la lección ni repetir recorridos de shell innecesariamente. La reproducibilidad
también se practica reiniciando la sesión del IDE y ejecutando el script completo.

Aplicar este criterio al material nuevo. Shiny 13.01–13.10 incluye recorridos
de IDE/consola R y alternativas de terminal; eso no acredita haber comprobado
toda la interfaz del IDE. Distinguir la ejecución con Rscript, la revisión en
navegador y la operación real en el IDE. La revisión retroactiva del recorrido
R se conserva como pendiente; no darla por completada por tener estos apoyos.

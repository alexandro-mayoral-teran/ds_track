# Guía para crear material

Para comenzar otro proyecto o tema, utiliza las
[plantillas de agentes y arquitectura](../templates/learning-project/README.md).
Esta guía orienta la autoría de contenido dentro del recorrido ya diseñado.

## Estructura de un módulo

Usa [`templates/module/`](../templates/module/) como punto de partida.

```text
module_name/
├── README.md
├── examples/
├── exercises/
├── challenge/
└── solutions/
```

No es necesario crear todas las carpetas desde el primer momento. Deben aparecer
cuando contengan material útil.

## Contenido mínimo del README

- Propósito.
- Prerrequisitos.
- Objetivos observables.
- Conceptos.
- Actividades.
- Criterio de salida.
- Referencias primarias.

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

Cuando una habilidad se aplique a un proyecto, identifica un checkpoint
concreto. No uses solamente frases generales como "se utilizará después".

Ejemplo:

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

Aplicar este criterio al material nuevo. La 07.01 y su lab ya se adaptaron;
las demás lecciones implementadas quedan para una revisión posterior.

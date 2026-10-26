# Flujo de aprendizaje

Este documento define cómo se conectan el curriculum, los labs, los proyectos y
el registro de progreso.

## Ciclo de trabajo

```text
curriculum
  explica y demuestra
        ↓
lab
  practica una habilidad aislada
        ↓
comprobar y explicar
  verificar resultados y justificar decisiones
        ↓
evidencia
  script, consulta, notebook, reporte o aplicación
        ↓
PROGRESS.md
  registra el resultado y el siguiente paso

cuando existe: lab → checkpoint de proyecto → evidencia integrada
continuidad: lab → siguiente lección → siguiente lab
```

Las muestras de lección y los datasets apoyan el recorrido. El checkpoint es
opcional hasta que exista un proyecto asociado. `showcase/` recibe únicamente
resultados terminados y seguros para compartir.

## Reglas de enlace

Los enlaces deben funcionar en ambas direcciones:

1. Una lección enlaza sus labs asociados.
2. Un lab enlaza la lección que refuerza.
3. Cuando aplica, la lección y el lab enlazan un checkpoint de proyecto.
4. El proyecto indica qué módulos y labs preparan cada checkpoint.
5. `PROGRESS.md` enlaza la evidencia producida, no copia toda la explicación.

Si todavía no existe proyecto asociado, se indica explícitamente. No se crea una
carpeta vacía solo para completar el enlace.

## Identificadores

Usaremos identificadores predecibles:

- Módulo: `00_getting_started`.
- Lección: `02_terminal_paths`.
- Lab: `00.01` en el título y una carpeta descriptiva.
- Proyecto: `01_clean_credit_data`.
- Checkpoint: `CP-01`, `CP-02`, etc., dentro del README del proyecto.

Los identificadores sirven para relacionar contenido; no representan una nota o
calificación.

## Qué pertenece en cada lugar

### Curriculum

- Explicación de conceptos.
- Ejemplos mínimos.
- Errores comunes.
- Referencias.
- Criterio de salida y enlaces de práctica.

### Lab

- Una habilidad principal.
- Entrada y resultado esperados.
- Instrucciones o restricciones.
- Preguntas de reflexión.
- Forma objetiva de validación.

Un lab no debe introducir teoría esencial que no exista en el curriculum.

### Proyecto

- Un problema con contexto.
- Preguntas que admiten decisiones justificadas.
- Varios checkpoints incrementales.
- Datos, ejecución, pruebas y resultado compartible.

Un proyecto no tiene que esperar a que termine todo el módulo. Puede crecer un
checkpoint a la vez.

## Ejemplo futuro

```text
curriculum/02_pandas/05_missing_duplicates_rules
        ↕
labs/02_pandas/05_missing_duplicates_rules
        ↕
projects/01_clean_credit_data — CP-02
        ↓
projects/01_clean_credit_data/output/quality_summary
        ↓
PROGRESS.md
```

## Fuente de verdad del avance

[`PROGRESS.md`](../PROGRESS.md) mantiene el estado actual del material y los puntos
de reanudación del proyecto. El curriculum describe el orden y los proyectos sus
checkpoints; ninguno debe duplicar la bitácora editorial diaria.

## Bitácora personal en el piloto 02.01

El [portal local](../portal/README.md) añade una copia personal del notebook y una
[plantilla de bitácora](../templates/learning-session/bitacora.md). Para esta prueba,
cada participante registra predicción, comprobaciones, explicación, ayudas y
evidencia en su carpeta excluida de Git. El formulario del portal conserva un
solo borrador por sesión en ese navegador; exportarlo no modifica automáticamente
la nota del paquete ni PROGRESS.md.

Esta separación está implementada para el piloto, sin migrar registros previos
del resto del recorrido. La comprobación técnica del material y el estado
declarado por la persona se registran por separado: no equivalen a aprendizaje
observado. Una sesión real de pareja sigue siendo necesaria para evaluar la
experiencia antes de extender el portal.


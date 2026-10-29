# Flujo de aprendizaje

Este documento define cómo se conectan el curriculum, los labs, los proyectos y
la evidencia personal y el estado editorial.

## Ciclo de trabajo

```text
curriculum
  explica y demuestra
        ↓
lab
  practica una capacidad o un cierre acotado
        ↓
comprobar y explicar
  verificar resultados y justificar decisiones
        ↓
evidencia
  script, consulta, notebook, reporte o aplicación
        ↓
bitácora personal
  registra comprobación, dudas y siguiente paso del estudiante

cuando existe: lab → checkpoint de proyecto → evidencia integrada
continuidad: lab → siguiente lección → siguiente lab
```

Las muestras de lección y los datasets apoyan el recorrido. Solo se enlaza un
checkpoint cuando existe el proyecto y el checkpoint está implementado; los
planes se identifican como tales. `showcase/` recibe únicamente
resultados terminados y seguros para compartir.

## Reglas de enlace

Los enlaces deben funcionar en ambas direcciones:

1. Una lección enlaza sus labs asociados.
2. Un lab enlaza la lección que refuerza.
3. Cuando aplica, la lección y el lab enlazan un checkpoint de proyecto.
4. El proyecto indica qué módulos y labs preparan cada checkpoint.
5. La bitácora personal identifica la evidencia y las dudas del estudiante;
   `PROGRESS.md` registra desarrollo y comprobaciones de autoría del material.

Si todavía no existe proyecto asociado, se indica explícitamente. No se crea una
carpeta vacía solo para completar el enlace.

## Identificadores

Usaremos identificadores predecibles:

- Módulo: `00_getting_started`.
- Lección: `00.02`, en la carpeta `02_terminal_paths` del módulo 00.
- Lab: el mismo identificador `00.02` y carpeta de la lección asociada.
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

- Una capacidad principal o un cierre acotado de capacidades ya enseñadas.
- Entrada y resultado esperados.
- Instrucciones o restricciones.
- Preguntas de reflexión.
- Forma objetiva de validación.

Un lab no debe introducir teoría esencial que no exista en el curriculum.
Un cierre puede reunir varias comprobaciones y ocupar varias sesiones sin
convertirse por eso en un proyecto o checkpoint implementado.

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
bitácora personal del estudiante
```

## Fuente de verdad del avance

[`PROGRESS.md`](../PROGRESS.md) mantiene el estado actual del material y los puntos
de reanudación del proyecto. El curriculum describe el orden y los proyectos sus
checkpoints; ninguno debe duplicar la bitácora editorial diaria.

<a id="bitácora-personal-en-el-portal"></a>

## Bitácora personal y portal

Estudiar desde el repositorio también requiere conservar evidencia en la copia
personal; no depende de utilizar el portal. PROGRESS.md no es el expediente del
estudiante ni se modifica para registrar cada práctica individual.

El [portal local](../portal/README.md) ofrece una
[plantilla del módulo 00](../templates/learning-session/bitacora-00.md) y conserva
la copia del notebook y la [bitácora de 02.01](../templates/learning-session/bitacora.md).
En estas prácticas,
cada participante registra predicción, comprobaciones, explicación, ayudas y
evidencia en su carpeta excluida de Git. El formulario del portal conserva un
solo borrador para 02.01 en ese navegador; el módulo 00 usa un archivo Markdown.
Exportar no modifica automáticamente
la nota del paquete ni PROGRESS.md.

Esta separación está implementada para 00 y 02.01, sin migrar registros previos
del resto del recorrido. La comprobación técnica del material y el estado
declarado por la persona se registran por separado: no equivalen a aprendizaje
observado. Una sesión real de pareja sigue siendo necesaria para evaluar la
experiencia antes de extender el portal.


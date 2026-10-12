# Progreso de aprendizaje

Este archivo registra dónde estamos y qué sigue. El plan completo vive en
[`ROADMAP.md`](ROADMAP.md); aquí solo se actualiza el avance real.

## En este momento

- **Módulo activo de desarrollo:** `01_python_foundations`
- **Estado:** en curso
- **Foco de desarrollo del material:** listas y diccionarios.
- **Estado del contenido:** nivel 0 disponible y primeras dos lecciones de Python
  fundamental con sus labs. Esto no acredita finalización del estudiante.
- **Siguiente paso de estudio:** leer la
  [lección de listas y diccionarios](curriculum/01_python_foundations/02_lists_dicts/README.md) y realizar
  el [lab 01.02](labs/01_python_foundations/02_lists_dicts/README.md), después de
  completar las prácticas previas.

## Estados

- `No iniciado`: todavía no se trabaja el módulo.
- `En curso`: existe trabajo activo, aunque falten actividades.
- `En pausa`: se conserva el avance, pero no es el foco actual.
- `Completado`: se alcanzó el criterio de salida definido en el roadmap.

## Avance por módulo

| Nivel | Módulo | Estado | Evidencia de finalización |
| --- | --- | --- | --- |
| 00 | Entorno de aprendizaje | En curso | Pendiente |
| 01 | Python fundamental | No iniciado | — |
| 02 | pandas | No iniciado | — |
| 03 | SQL y bases de datos | No iniciado | — |
| 04 | Visualización en Python | No iniciado | — |
| 05 | Python aplicado | No iniciado | — |
| 06 | R fundamental | No iniciado | — |
| 07 | tidyverse | No iniciado | — |
| 08 | Visualización en R | No iniciado | — |
| 09 | Arrow y Parquet | No iniciado | — |
| 10 | Polars y DuckDB | No iniciado | — |
| 11 | Reportes con Quarto | No iniciado | — |
| 12 | Streamlit | No iniciado | — |
| 13 | Shiny y fundamentos web | No iniciado | — |
| 14 | Proyecto reproducible | No iniciado | — |

## Bitácora

### 2026-10-11

- Se desarrolló la lección 02 de Python fundamental y su lab: listas,
  diccionarios, registros, mutabilidad y copias.
- Se inició Python fundamental con la lección y lab de variables, tipos y
  operaciones. Se registró R aplicado como consideración para la próxima revisión.
- Se integraron las rutas en un flujo numerado 00–14; visualización y Python aplicado
  ahora tienen ubicación y prerrequisitos, con Streamlit/Shiny como elección de aplicación.

- Se revisó el track completo: comunicación y calidad tempranas, cierre integrado
  antes de R y separación de contenidos esenciales y avanzados sin renumerar niveles.
- Se creó la lección 06, el notebook de ejemplo y su lab: selección de kernel,
  celdas, estado en memoria y ejecución desde cero.
- Se dividió la lección 05 en dos sesiones: preparación del entorno y gestión
  de dependencias, con teoría específica de requirements.txt y archivos de configuración.
- Se separó la teoría de entornos de tres recorridos prácticos: Conda, venv + pip
  y uv, con una demostración común de instalación e importación de una biblioteca.
- Se adaptó la lección 05 a Anaconda/Conda como recorrido principal, con uv como
  alternativa y un solo entorno requerido en el lab.
- Se creó la lección 05 y su lab: intérpretes, venv, pip y entorno del proyecto
  con uv, conservando recorridos por shell y soluciones desplegables.
- Se desarrollaron las primeras tres lecciones y sus labs, con explicaciones
  por pasos y soluciones desplegables.
- Se preparó la lección 04 y un primer script sin paquetes externos; la
  preparación del entorno queda para la lección 05.
- Se creó el repositorio privado de DS Track y se publicó el material inicial.
- Se incorporó el perfil de GitHub como práctica inicial del nivel 0, con
  Markdown y actualización desde Git. La práctica de terminal se conserva.
- Se alineó la numeración con el orden de estudio y se agregó una plantilla
  editable para el README del perfil.
- Se separaron las lecciones 01 y 03: creación desde la web y actualización con
  Git, cada una con su propio documento y lab.

### 2026-10-08

- Se definió la arquitectura del repositorio.
- Se creó el roadmap por niveles.
- Se prepararon plantillas para módulos y proyectos.
- Se estableció la política de datos sintéticos.
- Se inició el módulo `00_getting_started`.
- Se creó la primera lección y su lab sobre terminal, rutas y entorno.
- Se agregaron equivalencias PowerShell–Unix para preparar el uso de Git,
  servidores y entornos de nube.

## Cómo actualizar este archivo

Al terminar una sesión:

1. Actualiza el siguiente paso con una acción pequeña y concreta.
2. Registra uno o dos resultados en la bitácora, no cada comando ejecutado.
3. Cambia un módulo a `Completado` solo cuando exista evidencia de su criterio
   de salida.
4. Enlaza la evidencia: ejercicio, script, notebook, reporte o proyecto.

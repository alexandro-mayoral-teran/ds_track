# Progreso de aprendizaje

Este archivo registra dónde estamos y qué sigue. El plan completo vive en
[`ROADMAP.md`](ROADMAP.md); aquí solo se actualiza el avance real.

## En este momento

- **Módulo activo de desarrollo:** `02_pandas`
- **Estado:** en curso
- **Foco de desarrollo del material:** combinación de tablas con pandas.
  Próxima lección por implementar: 02.09 — Cambiar la forma de una tabla.
- **Estado del contenido:** nivel 0 disponible y las seis lecciones de Python
  fundamental con sus labs. Esto no acredita finalización del estudiante.
  Los módulos 02–05 tienen un plan de 39 secciones. Las ocho primeras de pandas y sus
  labs están disponibles; las demás están por desarrollar. Los módulos 06–08 tienen
  un plan adicional de 28 secciones y lecturas abiertas. Los módulos 09–10 tienen
  19 secciones planificadas y 11–14 añaden 37. La planificación de 02–14 está
  detallada; 02.01–02.08 ya disponen de lección y lab dentro de esos módulos.
- **Siguiente paso de estudio:** leer la
  [lección de combinación de tablas](curriculum/02_pandas/08_combine_tables/README.md) y realizar
  el [lab 02.08](labs/02_pandas/08_combine_tables/README.md), después de
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

- Se desarrolló pandas 02.08: concat, tipos de merge, validate, indicator y
  comparación por ID sobre una base común. Tres diagramas Mermaid explican las
  operaciones y la multiplicación de filas; se agregó lab con comprobaciones.

- Se desarrolló pandas 02.07 con 48 observaciones: groupby/agg, size/count/nunique,
  grupos con NA, cobertura y tasas con bases explícitas. Los 10 grupos se verificaron
  contra cálculos independientes; se agregó lab y transform como ampliación.

- Se desarrolló pandas 02.06 con 48 registros de dos cortes: normalización
  trazable, formatos temporales explícitos, NaT, relaciones de fechas y claves
  posteriores a la limpieza. Se agregó lab y comparación de períodos comprobada.

- Se desarrolló pandas 02.05: 44 registros sintéticos, reglas explícitas, claves
  repetidas apartadas para revisión y múltiples motivos por registro. El script
  concilia la partición y comprueba exportaciones; se agregó lab y navegación.

- Se desarrolló pandas 02.04 con 40 filas sintéticas: conversión trazable, tipos
  nullable, operaciones entre columnas, asignación con loc y conciliación sobre
  la misma base. Se agregó el lab con soluciones desplegables y navegación.

- Se desarrolló pandas 02.03: loc/iloc, máscaras, condiciones combinadas, NA,
  orden y desempates, con selección vacía y exportación comprobada. Se agregó
  el lab y se conservó la fuente de la lección anterior.

- Se desarrolló pandas 02.02 con muestra crediticia ficticia y diccionario: lectura
  tipada, head/info/describe, exportación y comparación de la tabla recargada.
  Se agregó su lab y se enlazó desde la primera lección.

- Se depuraron las instrucciones locales de agentes, separando reglas vigentes
  de historial. Se crearon plantillas generales de agentes y arquitectura, con
  instrucciones para copiarlas y adaptarlas a proyectos de otros temas.
- Se revisaron las instrucciones locales y el roadmap: estado real de pandas,
  alcances opcionales, proyectos aún por implementar y pendientes de R aplicado
  y terminal avanzada. Se alineó el flujo de estudio con checkpoints opcionales.

- Se investigaron y definieron Quarto (9 secciones), Streamlit (9), Shiny (10)
  y proyecto reproducible (9). El recorrido numerado completo tiene planes
  detallados; se retoma la implementación por pandas 02.02 en la siguiente sesión.

- Se investigaron fuentes oficiales y se organizaron Arrow/Parquet (9 secciones)
  y Polars/DuckDB (10), con intercambio Python/R, consultas verificables y mediciones.
  Se mantuvo la numeración y se separaron particiones y streaming como ampliaciones.

- Se investigaron libros abiertos de Hadley Wickham y documentación oficial para
  definir R fundamental (9 secciones), tidyverse (10) y visualización R (9).
  Se agregó una guía de lecturas y se mantuvo pendiente la numeración de R aplicado.

- Se desarrolló 02.01 — Series y DataFrame, con script y lab; pandas 2.3.3 se
  declaró en pyproject.toml y se resolvió en uv.lock. Se verificó el ejemplo
  en un entorno aislado y se actualizaron navegación y arquitectura.

- Se investigó documentación oficial y se organizaron las secciones de pandas (10),
  SQL (9), visualización Python (9) y Python aplicado (11), con prácticas y cierres
  propuestos. Se distinguió el recorrido esencial de las ampliaciones opcionales.
- Se desarrolló la lección 06 de Python fundamental y su lab: reglas, excepciones,
  rechazos trazables y resumen conciliado. El módulo dispone de seis lecciones;
  la finalización del aprendizaje sigue pendiente de evidencias.

- Se desarrolló la lección 05 de Python fundamental y su lab: lectura CSV,
  conversión, escritura y comprobación de registros e importes, conservando la entrada.
- Se revisaron las instrucciones locales, la arquitectura y los diagramas:
  flujo lección/lab, avances de contenido y diferencia entre muestras iniciales
  de ventas y dominio crediticio posterior.
- Se desarrolló la lección 04 de Python fundamental y su lab: parámetros,
  retorno, alcance y reutilización de filtros y resúmenes.
- Se desarrolló la lección 03 de Python fundamental: condiciones, recorrido,
  acumuladores y selección de registros, con script y lab verificables.
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

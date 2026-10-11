# DS Track

Ruta de aprendizaje práctica para manipulación, análisis, almacenamiento y
comunicación de datos.

El repositorio está diseñado para avanzar por etapas. Los fundamentos aparecen
antes que las herramientas de mayor escala, y cada nivel termina con un
resultado observable. Git ayuda a publicar y conservar el material, pero no es
un requisito para estudiar: el contenido también debe funcionar al descargarlo
como ZIP.

## Principios

- Bases antes que herramientas: Python, pandas, SQL y modelado primero.
- Una sola historia de datos: la cartera sintética crece con el recorrido.
- Aprender haciendo: explicación breve, práctica guiada, reto y proyecto.
- Comparar con evidencia: rendimiento, memoria, claridad y mantenibilidad.
- Datos seguros: nunca se versionan datos reales, secretos ni PII.
- Complejidad gradual: R, Parquet, Polars, DuckDB, Quarto y Shiny se incorporan
  cuando resuelven una necesidad ya entendida.

## Mapa del repositorio

| Ruta | Propósito |
| --- | --- |
| [`curriculum/`](curriculum/) | Módulos ordenados de aprendizaje |
| [`PROGRESS.md`](PROGRESS.md) | Módulo activo, siguiente paso y bitácora |
| [`labs/`](labs/) | Ejercicios breves y deliberados |
| [`projects/`](projects/) | Proyectos que integran varios módulos |
| [`datasets/`](datasets/) | Datos pequeños y sintéticos, generadores y diccionarios |
| [`templates/`](templates/) | Plantillas reutilizables para nuevo material |
| [`showcase/`](showcase/) | Resultados terminados para compartir |
| [`docs/`](docs/) | Arquitectura, reglas de contenido y seguridad |

La relación entre lecciones, práctica y proyectos se explica en
[`docs/learning-workflow.md`](docs/learning-workflow.md).

## Recorrido de aprendizaje

Cada paso desarrolla una capacidad que se aplica en el siguiente. El recorrido
empieza con tu perfil y termina con un proyecto que puedes reconstruir y explicar.

```mermaid
flowchart TD
    subgraph foundations["Preparar y comprender"]
        A["00 · Entorno de aprendizaje<br/>Markdown y perfil en GitHub → terminal → Git<br/>Primer script → dependencias → notebook"]
        B["01 · Python fundamental<br/>Leer archivos, validar registros y crear funciones"]
        C["02 · pandas<br/>Limpiar, transformar y resumir datos"]
        D["03 · SQL y bases de datos<br/>Modelar tablas y consultar indicadores"]
        A --> B --> C --> D
    end

    subgraph analysis["Analizar y procesar"]
        E["04 · R fundamental<br/>Reproducir un análisis en otro lenguaje"]
        F["05 · tidyverse<br/>Transformar datos y comunicar con gráficas"]
        G["06 · Arrow y Parquet<br/>Diseñar almacenamiento columnar"]
        H["07 · Polars y DuckDB<br/>Procesar más datos y comparar rendimiento"]
        E --> F --> G --> H
    end

    subgraph products["Comunicar y construir"]
        I["08 · Quarto<br/>Generar reportes reproducibles"]
        J["09 · Shiny y fundamentos web<br/>Crear un explorador interactivo"]
        K["10 · Proyecto reproducible<br/>Integrar código, datos, pruebas y documentación"]
        I --> J --> K
    end

    D --> E
    H --> I

    classDef foundation fill:#dbeafe,stroke:#2563eb,color:#172554;
    classDef processing fill:#dcfce7,stroke:#16a34a,color:#14532d;
    classDef product fill:#fef3c7,stroke:#d97706,color:#78350f;
    class A,B,C,D foundation;
    class E,F,G,H processing;
    class I,J,K product;
```

La publicación del perfil y el uso de Git son prácticas recomendadas. También
puedes seguir el recorrido con el material descargado como ZIP.

Consulta [`ROADMAP.md`](ROADMAP.md) para ver los resultados y criterios de
avance de cada nivel.

## Cómo estudiar

El recorrido también está pensado para aprender acompañado: una persona realiza
las prácticas y otra explica conceptos, revisa resultados y ayuda a resolver dudas.

Para cada módulo:

1. Lee sus objetivos y conceptos.
2. Ejecuta los ejemplos.
3. Resuelve los ejercicios sin mirar la solución.
4. Aplica lo aprendido al checkpoint de proyecto cuando exista.
5. Registra la evidencia y las dudas pendientes en `PROGRESS.md`.
6. Avanza cuando cumplas el criterio de salida, no solo por haber leído todo.

En una sesión acompañada, empieza con una explicación breve, realiza la práctica
y cierra explicando con tus propias palabras qué hiciste y por qué. Usa las
preguntas del lab para conversar y comprobar lo aprendido.

## Estado actual

La arquitectura inicial está lista y `00_getting_started` está en curso. El
avance diario y el siguiente paso se mantienen en [`PROGRESS.md`](PROGRESS.md).

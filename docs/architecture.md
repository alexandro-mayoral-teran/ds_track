# Arquitectura del repositorio

La arquitectura separa enseñanza, práctica, integración y publicación. Esto
evita que un notebook aislado tenga que funcionar al mismo tiempo como lección,
ejercicio, solución y producto final.

## Flujo del conocimiento

```text
curriculum → labs → checkpoint de proyecto → evidencia → PROGRESS.md
      ↑                  ↓
      └──── datasets     └──── resultado terminado → showcase
```

Las reglas concretas de conexión están en
[`learning-workflow.md`](learning-workflow.md).

## Responsabilidad de cada área

### `curriculum/`

Contenido secuencial. Explica conceptos y presenta ejemplos mínimos. Los
módulos están numerados porque tienen prerrequisitos deliberados.

### `labs/`

Práctica breve. Un lab debe poder terminarse sin construir un proyecto entero y
debe declarar qué módulo refuerza.

### `projects/`

Integra varias capacidades alrededor de una pregunta o producto. Cada proyecto
es autocontenido y debe documentar entradas, transformaciones y salidas.

### `datasets/`

Contiene únicamente muestras pequeñas, datos sintéticos, generadores y
diccionarios. Los datos de trabajo voluminosos se regeneran localmente y no se
versionan.

### `templates/`

Reduce decisiones repetidas. Aquí viven las estructuras base para crear nuevos
módulos, proyectos, reportes o aplicaciones.

### `showcase/`

Contiene resultados terminados y seguros para compartir: reportes renderizados,
capturas, demostraciones o enlaces. No es un directorio de trabajo.

## Dependencias

Python usa un `pyproject.toml` y un `uv.lock` en la raíz. Esa configuración
describe el recorrido alternativo con uv. Para quienes ya usan Anaconda, la
lección 05 enseña Conda como recorrido principal y cómo exportar su configuración;
los archivos de uv no describen automáticamente un entorno Conda.
El lockfile no incorpora bibliotecas externas y se actualizará al agregar dependencias
reales. R adoptará `renv` dentro del material de R cuando se introduzca
reproducibilidad. No se crearán entornos independientes por cada ejercicio salvo
que exista una incompatibilidad concreta.

## Datos del recorrido

El dominio común será una cartera crediticia completamente sintética. Su escala
crecerá de manera intencional:

1. CSV pequeño para Python y pandas.
2. Varias tablas para SQL.
3. Histórico de cortes para R y visualización.
4. Dataset Parquet particionado para Polars y DuckDB.
5. Tablas analíticas para Quarto y Shiny.

## Decisiones futuras

Las decisiones importantes se documentarán en `docs/decisions/` usando notas
breves: contexto, decisión, consecuencias y fecha. No se agregará infraestructura
solo para anticipar necesidades hipotéticas.

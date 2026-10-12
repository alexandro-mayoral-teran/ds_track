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

## Rutas de profundización previstas

El recorrido principal conserva los niveles 00–10. Estas rutas amplían las
capacidades cuando ya existe un análisis que mejorar; no bloquean el paso de
Python fundamental a pandas. Son planificación: todavía no hay lecciones ni
carpetas de ejercicios para estos bloques.

### Python aplicado: del notebook al proyecto

Se introducirá después de pandas y SQL, reutilizando un problema conocido.
Los contenidos se organizarán por necesidades, no como una lista de sintaxis:

| Bloque | Conceptos previstos | Resultado observable |
| --- | --- | --- |
| Organización | Módulos, paquetes, configuración y logging | Extraer transformaciones de un notebook a código reutilizable |
| Funciones e iteración | Funciones como valores, iteradores, generadores y decoradores | Procesar por lotes y reutilizar comportamientos |
| Diseño de estructuras | Clases, composición, dataclasses y anotaciones de tipos | Representar registros o configuración con claridad |
| Robustez | Excepciones propias, gestores de contexto y pruebas | Manejar errores y recursos con casos verificables |
| Rendimiento | Medición de tiempo/memoria, profiling y complejidad básica | Localizar un cuello de botella antes de optimizar |
| Integración | APIs HTTP, paginación, tiempos de espera y reintentos | Obtener y validar datos de un servicio |

Foundations conserva funciones, mutabilidad, módulos, errores y el uso de `with`
al leer archivos. Crear decoradores o gestores de contexto y diseñar clases se
profundizará después. Herencia se tratará cuando haga falta; composición y
funciones son opciones iniciales. Concurrencia, asincronía y metaprogramación
quedan como temas avanzados sujetos a una necesidad concreta.

### Visualización: entender antes de construir aplicaciones

La primera gráfica y su interpretación aparecen en pandas. Una ruta posterior
profundizará en pregunta analítica, elección de gráfico, escalas, unidades,
agregación, etiquetas, color accesible y comunicación de incertidumbre.
Reutilizará datos e indicadores ya comprobados, comparando representaciones
sin repetir todo el análisis para cada biblioteca.

| Etapa | Python | R | Evidencia prevista |
| --- | --- | --- | --- |
| Base estática | Matplotlib: Figure/Axes, barras, líneas, distribuciones y exportación | ggplot2: datos, estéticas, geometrías, escalas y facetas | Una figura legible con interpretación y unidades |
| Composición e interacción | Altair: marcas, codificaciones, tipos y selecciones | Profundización de ggplot2 y composición de figuras; interacción como extensión | Comparar el mismo indicador en varias vistas |
| Producto interactivo | Streamlit: inputs, tablas, gráficas, reruns, estado y caché | Shiny: UI, servidor, reactividad, estado y módulos | Explorador de datos con filtros y resultados verificables |

Matplotlib y Altair son herramientas de gráficos; Streamlit es un framework
para aplicaciones. En R, ggplot2 es la base de visualización del módulo tidyverse,
y Shiny convierte el análisis en una aplicación. No exigir todas las herramientas
para cada ejercicio: se puede elegir un ecosistema y comparar el otro después.

Para Streamlit se aprenderá primero su modelo de reejecución y después estado
y caché. Usar un decorador existente, por ejemplo para caché, no exige desarrollar
decoradores personalizados. En Shiny, enseñar reactividad antes de ampliar la UI.
En ambos casos separar transformación y validación de datos de la interfaz.

### Conexión con los niveles y proyectos

- Nivel 2: primera gráfica con Matplotlib y una explicación del hallazgo.
- Niveles 3–5: cierre analítico conocido, Python aplicado como profundización y
  visualización equivalente con ggplot2 en tidyverse.
- Nivel 8: reutilizar figuras e interpretaciones en reportes Quarto.
- Nivel 9: conservar Shiny en el recorrido principal y contemplar Streamlit como
  ruta de aplicación en Python; no exigir construir ambas aplicaciones.
- Nivel 10: integrar las prácticas de organización y robustez que ya se hayan
  introducido. El proyecto final no es la primera ocasión de validar o documentar.

Cada ruta tendrá lecciones, labs y checkpoints cuando se desarrolle. Mantener
los requisitos del gestor elegido actualizados al introducir bibliotecas; no
agregar dependencias ni crear esqueletos vacíos por anticipación.

Fuentes para desarrollar las herramientas:
[Matplotlib](https://matplotlib.org/stable/users/getting_started/),
[Altair](https://altair-viz.github.io/),
[ggplot2](https://ggplot2.tidyverse.org/) y
[Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts).

## Registro de decisiones

Las decisiones importantes se documentarán en `docs/decisions/` usando notas
breves: contexto, decisión, consecuencias y fecha. No se agregará infraestructura
solo para anticipar necesidades hipotéticas.

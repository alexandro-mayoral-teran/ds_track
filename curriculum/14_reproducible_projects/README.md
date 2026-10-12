# 14 — Proyecto reproducible

## Propósito y prerrequisitos

Integrar el recorrido en un producto que otra persona pueda reconstruir:
datos, código, indicadores, reporte y una aplicación elegida. Completa
[11 — Quarto](../11_reporting_quarto/README.md) y
[12 — Streamlit](../12_streamlit/README.md) **o**
[13 — Shiny](../13_shiny_web/README.md). No es obligatorio construir ambas apps.

**Estado:** nueve secciones planificadas; lecciones y labs por desarrollar.
Los enlaces internos describen el alcance previsto.

Se reutilizarán los proyectos anteriores. No comenzaremos un problema o una pila
nueva de herramientas para demostrar integración. Calidad, documentación y
comprobaciones ya se practican desde Python; aquí se consolidan y automatizan.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Pregunta y contrato del producto](#01-pregunta-y-contrato-del-producto) | Esencial | Definir entradas, resultados y aceptación |
| 2 | [Estructura y configuración](#02-estructura-y-configuracion) | Esencial | Localizar responsabilidades y parámetros |
| 3 | [Entornos y ejecución reconstruible](#03-entornos-y-ejecucion-reconstruible) | Esencial | Preparar y ejecutar desde instrucciones explícitas |
| 4 | [Pipeline y reprocesamiento](#04-pipeline-y-reprocesamiento) | Esencial | Repetir un corte sin duplicar o mezclar resultados |
| 5 | [Pruebas y calidad de datos](#05-pruebas-y-calidad-de-datos) | Esencial | Detectar fallas relevantes antes de entregar |
| 6 | [Trazabilidad y recuperación de fallas](#06-trazabilidad-y-recuperacion-de-fallas) | Esencial | Explicar qué se ejecutó y qué resultados son válidos |
| 7 | [Integración de reporte y app](#07-integracion-de-reporte-y-app) | Práctica | Conciliar el mismo corte en todos los productos |
| 8 | [Entrega y automatización opcional](#08-entrega-y-automatizacion-opcional) | Práctica / Extensión | Compartir una entrega reconstruible; CI opcional |
| 9 | [Revisión final y defensa de decisiones](#09-revision-final-y-defensa-de-decisiones) | Práctica de cierre | Demostrar reconstrucción y justificar límites |

## Alcance de cada sección

<a id="01-pregunta-y-contrato-del-producto"></a>

### 01 — Pregunta y contrato del producto

- Público, pregunta, fuentes sintéticas, corte, llaves, unidades, reglas y productos.
  Definir qué significa éxito, incluyendo conteos y resultados esperados.
- Práctica prevista: una especificación breve que reutilice preguntas anteriores;
  no añadir modelado o infraestructura que no se haya aprendido.

<a id="02-estructura-y-configuracion"></a>

### 02 — Estructura y configuración

- Separar entrada preservada, transformaciones y salidas regenerables;
  módulos/funciones, parámetros y documentación del recorrido.
- Práctica prevista: organizar el código existente y eliminar dependencias de
  rutas personales o estado oculto sin modificar los indicadores.

<a id="03-entornos-y-ejecucion-reconstruible"></a>

### 03 — Entornos y ejecución reconstruible

- Configuración Python del gestor elegido, renv para R y versión de Quarto.
  Instalar lo necesario y registrar también herramientas de sistema.
- Práctica prevista: reconstruir en un directorio limpio siguiendo instrucciones.
  Un lockfile conserva dependencias, pero no garantiza por sí solo datos,
  herramientas externas o igualdad de resultados en todos los equipos.

<a id="04-pipeline-y-reprocesamiento"></a>

### 04 — Pipeline y reprocesamiento

- Orden de pasos, dependencias de datos, corte y destinos de salida.
  Repetición sin duplicados y comprobación antes de dar un resultado por terminado.
- Práctica prevista: ejecutar dos veces el mismo corte y después otro corte;
  verificar indicadores y salidas. Escrituras temporales y reemplazo controlado
  según necesidad; atomicidad de un archivo no garantiza una transacción de todo el pipeline.

<a id="05-pruebas-y-calidad-de-datos"></a>

### 05 — Pruebas y calidad de datos

- Pruebas unitarias, integración y controles de esquema, claves, faltantes,
  rangos, conteos e indicadores. Muestras pequeñas y casos límite conocidos.
- Práctica prevista: introducir una falla controlada y demostrar que las pruebas
  la detectan. Reutilizar unittest o la herramienta ya elegida; pytest/testthat
  son opciones al ampliar, no paquetes obligatorios solo por este plan.

<a id="06-trazabilidad-y-recuperacion-de-fallas"></a>

### 06 — Trazabilidad y recuperación de fallas

- Identificar entrada, corte, configuración, versión, resultado y etapa fallida.
  Logs y estado de ejecución; diferenciar resultado anterior de ejecución actual.
- Práctica prevista: interrumpir un paso y revisar qué se puede reutilizar y qué
  debe regenerarse. No prometer recuperación automática o reintentar cualquier operación.

<a id="07-integracion-de-reporte-y-app"></a>

### 07 — Integración de reporte y app

- Compartir indicadores verificados entre tablas, Quarto y Streamlit/Shiny.
  Explicitar cortes, filtros y fecha de actualización en cada producto.
- Práctica prevista: conciliar un caso extremo y uno habitual; revisar que caché,
  salidas congeladas o filtros no presenten datos de otra ejecución.

<a id="08-entrega-y-automatizacion-opcional"></a>

### 08 — Entrega y automatización opcional

- README con preparación y ejecución, diccionario de datos, decisiones y producto
  de muestra. Entregar solo datos sintéticos, sin credenciales ni rutas personales.
- Práctica prevista: preparar una entrega local y distinguir fuente de salidas
  regenerables. GitHub Actions puede ejecutar controles como extensión; publicar
  una app o habilitar una automatización real no es requisito del cierre.

<a id="09-revision-final-y-defensa-de-decisiones"></a>

### 09 — Revisión final y defensa de decisiones

- Ejecutar desde cero, revisar pruebas y abrir reporte y app; comprobar un corte
  conocido y explicar elección de motor, formatos, reglas y limitaciones.
- Práctica prevista: otra persona sigue el README y reconstruye los productos;
  registrar evidencia y pendientes, evitando confundir implementación con aprendizaje.

## Prácticas y checkpoints de integración

Se prevén labs 14.01–14.09 y revisión final; todavía no existen. La integración
amplía los proyectos previstos en [proyectos](../../projects/README.md).
No se ha creado un proyecto final ni sus checkpoints ejecutables.

Checkpoints propuestos: CP-01, contrato y estructura (01–02); CP-02, ejecución y
reprocesamiento (03–04); CP-03, pruebas y trazabilidad (05–06); CP-04, productos
conciliados y entrega (07–08); CP-05, reconstrucción independiente (09).

El cierre requiere datos regenerables, controles que detecten una falla relevante,
reporte HTML y una app local comprobada, con instrucciones reproducibles.
No exige completar todas las extensiones, dominar ambos frameworks, instalar
orquestadores o publicar el producto en Internet.

## Cierre y referencias

Este módulo cierra el recorrido. Registra las evidencias en
[PROGRESS.md](../../PROGRESS.md) y los productos terminados apropiados en
[showcase](../../showcase/README.md). Un módulo se marca completado cuando se
alcanza su criterio de salida, no por tener un plan o material desarrollado.

Fuentes para preparar las prácticas: [entornos uv](https://docs.astral.sh/uv/concepts/projects/sync/),
[renv](https://rstudio.github.io/renv/articles/renv.html),
[organización de pruebas pytest](https://docs.pytest.org/en/stable/explanation/goodpractices.html),
[pruebas R](https://r-pkgs.org/testing-basics.html),
[ejecución de Quarto](https://quarto.org/docs/projects/code-execution.html) y
[GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions).
Las dependencias se elegirán al implementar, conservando el gestor del estudiante.

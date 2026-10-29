# 14 — Proyecto reproducible

[Inicio](../../README.md) / [Módulos](../README.md) / **14 — Proyecto reproducible**

**Integra datos, código, reporte y una aplicación en un producto reconstruible.**

[**Empezar por 14.01 →**](01_product_question_contract/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** 14.01–14.02 con lecciones/labs, contrato, referencias y estructura/configuración.
> 14.03–14.09 siguen planificadas; no hay producto integrado final ni checkpoints implementados.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Consolidar el recorrido en un producto que otra persona pueda reconstruir y evaluar.
14.01 define pregunta/contrato y 14.02 organiza responsabilidades/parámetros con una muestra conocida; las secciones
posteriores conservan su plan. Aún no hay proyecto final ejecutable.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y una ruta de aplicación:
[12 — Streamlit](../12_streamlit/README.md) o [13 — Shiny](../13_shiny_web/README.md).
Las tres rutas tienen lecciones, labs y cierre local disponibles; basta una
aplicación. Revisa la práctica de cierre de [Streamlit](../../docs/streamlit-closure.md)
o [Shiny](../../docs/shiny-closure.md). 14.01–14.02 permiten trabajar diseño y estructura sin
paquetes nuevos ni entregas anteriores. No instales orquestadores por las secciones pendientes.

## Qué vas a aprender

14.01–14.02 permiten definir el contrato, organizar responsabilidades y configurar una consulta. El recorrido completo prevé:

- Declarar contrato, fuentes, configuración y criterios de aceptación.
- Reconstruir entornos y reprocesar sin mezclar resultados.
- Detectar fallas de datos y explicar trazabilidad y recuperación.
- Conciliar reporte y aplicación y defender decisiones y límites.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección o alcance | Práctica | Resultado que se comprobará |
| --- | --- | --- |
| **14.01** · [Pregunta y contrato del producto](01_product_question_contract/README.md) | [Lab 14.01](../../labs/14_reproducible_projects/01_product_question_contract/README.md) | Definir entradas, resultados y aceptación |
| **14.02** · [Estructura y configuración](02_structure_configuration/README.md) | [Lab 14.02](../../labs/14_reproducible_projects/02_structure_configuration/README.md) | Localizar responsabilidades y parámetros |
| **14.03** · [Entornos y ejecución reconstruible](#03-entornos-y-ejecucion-reconstruible) | Pendiente | Preparar y ejecutar desde instrucciones explícitas |
| **14.04** · [Pipeline y reprocesamiento](#04-pipeline-y-reprocesamiento) | Pendiente | Repetir un corte sin duplicar o mezclar resultados |
| **14.05** · [Pruebas y calidad de datos](#05-pruebas-y-calidad-de-datos) | Pendiente | Detectar fallas relevantes antes de entregar |
| **14.06** · [Trazabilidad y recuperación de fallas](#06-trazabilidad-y-recuperacion-de-fallas) | Pendiente | Explicar qué se ejecutó y qué resultados son válidos |
| **14.07** · [Integración de reporte y app](#07-integracion-de-reporte-y-app) | Pendiente | Conciliar el mismo corte en todos los productos |
| **14.08** · [Entrega y automatización opcional](#08-entrega-y-automatizacion-opcional) — opcional | Pendiente | Compartir una entrega reconstruible; CI opcional |
| **14.09** · [Revisión final y defensa de decisiones](#09-revision-final-y-defensa-de-decisiones) | Pendiente | Demostrar reconstrucción y justificar límites |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado:** 14.01–14.02 están disponibles. Las secciones 14.03–14.09 describen prácticas por desarrollar.

<a id="01-pregunta-y-contrato-del-producto"></a>

### 01 — Pregunta y contrato del producto

[Lección 14.01](01_product_question_contract/README.md) y [lab](../../labs/14_reproducible_projects/01_product_question_contract/README.md)
disponibles: pregunta/público, contrato de datos/cálculo/producto, estados y
aceptación. Seis observaciones, nueve casos y referencias Python estándar/R base;
diseño y aritmética no acreditan integración de reporte/app. Sin paquetes nuevos.

<a id="02-estructura-y-configuracion"></a>

### 02 — Estructura y configuración

[Lección 14.02](02_structure_configuration/README.md) y [lab](../../labs/14_reproducible_projects/02_structure_configuration/README.md)
disponibles: copia organizada de trece archivos, raíz explícita, configuración
CSV validada y consulta Python/R sin escribir resultados. Datos, reglas e
indicadores conservados; app/reporte y entornos quedan para secciones posteriores.

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

</details>

## Cómo trabajar este módulo

La práctica prevista integra el análisis, un reporte y una aplicación elegida. Calidad y documentación se consolidan, no se introducen por primera vez. Se comprobarán fallas, reconstrucción independiente y revisión del producto. CI, publicación y automatización real serán extensiones, no requisitos del cierre local.

Empieza con 14.01 y su lab: redacta el contrato, predice los casos y revisa sus
límites. Continúa con 14.02 para organizar y configurar la consulta. Las actividades 14.03–14.09 siguen como propuesta; no intentes ejecutar
todavía un pipeline o producto final inexistente.

## Qué conservar

| Evidencia prevista | Qué permite revisar |
| --- | --- |
| Contrato y casos de 14.01 | Pregunta, unidades, claves, reglas y aceptación revisables |
| Estructura/configuración de 14.02 | Responsabilidades, raíz explícita y parámetros conciliados |
| Pruebas y registros | Detección de fallas y trazabilidad |
| Reporte, app e instrucciones futuras | Reconstrucción independiente y decisiones defendidas |

En 14.01–14.02 conserva contrato, configuraciones, resultados por crédito y revisión
humana. Añade una nota con comprobación, ayudas, dudas y siguiente paso en tu
copia personal. PROGRESS.md registra material; no es un porcentaje de aprendizaje.

<a id="prácticas-y-checkpoints-de-integración"></a>

## Criterio de salida

Cuando se implemente, otra persona deberá regenerar datos, ejecutar controles que detecten una falla y reconstruir un reporte HTML y una app local. Deberás justificar herramientas, contratos y límites. El plan no acredita esa integración ni el aprendizaje.

No se ha creado un proyecto final ni sus checkpoints ejecutables. La integración ampliará los proyectos previstos, cuya disponibilidad debe revisarse antes de exigirlos.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, contrato y estructura (01–02); CP-02, ejecución y
reprocesamiento (03–04); CP-03, pruebas y trazabilidad (05–06); CP-04, productos
conciliados y entrega (07–08); CP-05, reconstrucción independiente (09).

</details>

<a id="cierre-y-referencias"></a>

## Siguiente paso

Empieza por [14.01 — Pregunta y contrato del producto](01_product_question_contract/README.md).
Continúa con [14.02 — Estructura y configuración](02_structure_configuration/README.md).
Después consulta [14.03 — Entornos y ejecución reconstruible](#03-entornos-y-ejecucion-reconstruible), todavía planificado. No hay integración final ni checkpoints listos.

Este plan cierra el recorrido. No hay un módulo 15 definido. Cuando exista una entrega verificada, conserva evidencia y revisa qué resultados son apropiados para [showcase](../../showcase/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Fuentes para preparar las prácticas: [entornos uv](https://docs.astral.sh/uv/concepts/projects/sync/),
[renv](https://rstudio.github.io/renv/articles/renv.html),
[organización de pruebas pytest](https://docs.pytest.org/en/stable/explanation/goodpractices.html),
[pruebas R](https://r-pkgs.org/testing-basics.html),
[ejecución de Quarto](https://quarto.org/docs/projects/code-execution.html) y
[GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions).
Las dependencias se elegirán al implementar, conservando el gestor del estudiante.

### Apoyos relacionados

- [proyectos](../../projects/README.md)
- [Estado editorial del material](../../PROGRESS.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Volver al plan de secciones ↑](#lecciones-y-labs)

# 14 — Proyecto reproducible

[Inicio](../../README.md) / [Módulos](../README.md) / **14 — Proyecto reproducible**

**Integra datos, código, reporte y una aplicación en un producto reconstruible.**

[**Empezar por 14.01 →**](01_product_question_contract/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** 14.01–14.09 con lecciones/labs, contrato, configuración, entornos, pipeline, pruebas, trazabilidad, integración local y entrega opcional.
> 14.09 aporta revisión final y defensa; 14.08 es opcional. Práctica personal, proyectos/checkpoints y depuración siguen pendientes.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Consolidar el recorrido en un producto que otra persona pueda reconstruir y evaluar.
14.01 define pregunta/contrato, 14.02 organiza responsabilidades/parámetros,
14.03 reconstruye entornos locales, 14.04 produce/reutiliza entregas, 14.05 prueba reglas y calidad de datos;
14.06 registra intentos y practica recuperación con evidencia conservada, y 14.07
concilia la consulta, un reporte y una app local. 14.08 añade entrega local
opcional y reconstrucción desde fuentes. 14.09 añade revisión final y defensa con evidencia propia.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y una ruta de aplicación:
[12 — Streamlit](../12_streamlit/README.md) o [13 — Shiny](../13_shiny_web/README.md).
Las tres rutas tienen lecciones, labs y cierre local disponibles; basta una
aplicación. Revisa la práctica de cierre de [Streamlit](../../docs/streamlit-closure.md)
o [Shiny](../../docs/shiny-closure.md). 14.01–14.09 permiten trabajar diseño,
configuración, entornos, reprocesamiento, pruebas, trazabilidad, integración
y entrega opcional con una interfaz local declarada, sin exigir entregas anteriores. No se requieren orquestadores para este cierre local.

## Qué vas a aprender

14.01–14.09 permiten definir el contrato, configurar una consulta, reconstruir
su entorno local, producir entregas separadas, repetir sin duplicados, detectar
fallas con pruebas, decidir cómo recuperar una ejecución, conciliar sus productos, compartir una entrega opcional y defender decisiones. El recorrido permite:

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
| **14.03** · [Entornos y ejecución reconstruible](03_reconstructible_environments/README.md) | [Lab 14.03](../../labs/14_reproducible_projects/03_reconstructible_environments/README.md) | Preparar y ejecutar desde instrucciones explícitas |
| **14.04** · [Pipeline y reprocesamiento](04_pipeline_reprocessing/README.md) | [Lab 14.04](../../labs/14_reproducible_projects/04_pipeline_reprocessing/README.md) | Repetir un corte sin duplicar o mezclar resultados |
| **14.05** · [Pruebas y calidad de datos](05_tests_data_quality/README.md) | [Lab 14.05](../../labs/14_reproducible_projects/05_tests_data_quality/README.md) | Detectar fallas relevantes antes de entregar |
| **14.06** · [Trazabilidad y recuperación de fallas](06_traceability_recovery/README.md) | [Lab 14.06](../../labs/14_reproducible_projects/06_traceability_recovery/README.md) | Explicar qué se ejecutó y qué resultados son válidos |
| **14.07** · [Integración de reporte y app](07_report_app_integration/README.md) | [Lab 14.07](../../labs/14_reproducible_projects/07_report_app_integration/README.md) | Conciliar el mismo corte en todos los productos |
| **14.08** · [Entrega y automatización opcional](08_delivery_optional_automation/README.md) — opcional | [Lab 14.08](../../labs/14_reproducible_projects/08_delivery_optional_automation/README.md) | Compartir una entrega reconstruible; CI opcional |
| **14.09** · [Revisión final y defensa de decisiones](09_final_review_defense/README.md) | [Lab 14.09](../../labs/14_reproducible_projects/09_final_review_defense/README.md) | Demostrar reconstrucción y justificar límites |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado:** 14.01–14.09 están disponibles. 14.08 es opcional; material desarrollado no acredita aprendizaje.

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

[Lección 14.03](03_reconstructible_environments/README.md) y [lab](../../labs/14_reproducible_projects/03_reconstructible_environments/README.md)
disponibles: 26 fuentes, Python/uv o R/renv locales, versiones declaradas,
lockfiles mínimos y evidencia nueva del entorno/consulta. Reconstrucción desde
fuentes en otra carpeta; Quarto se registra si está en PATH, sin renderizar.
No añade paquetes de análisis ni implementa todavía pipeline/reporte/app.

<a id="04-pipeline-y-reprocesamiento"></a>

### 04 — Pipeline y reprocesamiento

[Lección 14.04](04_pipeline_reprocessing/README.md) y [lab](../../labs/14_reproducible_projects/04_pipeline_reprocessing/README.md)
disponibles: 28 fuentes, pipeline Python/R sin paquetes nuevos, selección/contexto,
insumos y marca comprobados. Repetición sin escribir, otro corte en destino nuevo,
fallo temporal conservado y reintento. No reemplaza entregas ni garantiza una
transacción completa. La recuperación se trabaja en
[14.06](06_traceability_recovery/README.md) y la integración de productos en
[14.07](07_report_app_integration/README.md).

<a id="05-pruebas-y-calidad-de-datos"></a>

### 05 — Pruebas y calidad de datos

[Lección 14.05](05_tests_data_quality/README.md) y [lab](../../labs/14_reproducible_projects/05_tests_data_quality/README.md)
disponibles: 31 fuentes, siete grupos Python/unittest o R base, nueve criterios
literales y catorce fuentes inválidas. Integración/repetición, vacío, rechazo de
duplicados fuera del corte y alteraciones compensadas. Defecto controlado,
falla y restauración; sin paquetes nuevos ni afirmación de cobertura completa.

<a id="06-trazabilidad-y-recuperacion-de-fallas"></a>

### 06 — Trazabilidad y recuperación de fallas

[Lección 14.06](06_traceability_recovery/README.md) y [lab](../../labs/14_reproducible_projects/06_traceability_recovery/README.md)
disponibles: 33 fuentes, registros exclusivos por intento, etapas, configuración,
huellas y diagnóstico Python/R. Fallos antes y después de publicar, recuperación
por recálculo y reutilización comprobada; estado incompleto indeterminado.
Conserva parciales y pipeline; sin recuperación automática ni paquetes nuevos.

<a id="07-integracion-de-reporte-y-app"></a>

### 07 — Integración de reporte y app

[Lección 14.07](07_report_app_integration/README.md) y [lab](../../labs/14_reproducible_projects/07_report_app_integration/README.md)
disponibles: 53 fuentes, cálculo compartido, lector de solo lectura, tres reportes
Quarto preparados y una app Streamlit/Shiny con entorno separado. Identidad,
valores por crédito y denominadores conciliados; borrador, vacío, rechazo y
fuente cambiada. Fotografía estática y comprobación actual diferenciadas, sin
caché de cálculo ni despliegue. Entrega opcional en 14.08; defensa final en 14.09.

<a id="08-entrega-y-automatizacion-opcional"></a>

### 08 — Entrega y automatización opcional

[Lección 14.08](08_delivery_optional_automation/README.md) y [lab](../../labs/14_reproducible_projects/08_delivery_optional_automation/README.md)
disponibles, opcionales: 60 fuentes, paquete de 90 archivos y tres casos de
muestra. Revisor externo de solo lectura, referencia CSV externa y copia de
fuentes para reconstruir entornos, pruebas, consultas y reportes. Catálogo
explícito y huellas sin autenticidad; código recibido no ejecutado al verificar.
CI manual como plantilla inactiva, sin despliegue ni dependencias nuevas.

<a id="09-revision-final-y-defensa-de-decisiones"></a>

### 09 — Revisión final y defensa de decisiones

[Lección 14.09](09_final_review_defense/README.md) y [lab](../../labs/14_reproducible_projects/09_final_review_defense/README.md)
disponibles: reconstrucción desde las 53 fuentes de 14.07, sin exigir 14.08.
Tres casos y rechazo sin universo, contraste externo, falla controlada, revisión
personal, decisiones argumentadas y acta con pendientes. Sin paquetes nuevos ni
activación de proyectos/checkpoints. Completa la base de material del recorrido.

</details>

## Cómo trabajar este módulo

La práctica prevista integra el análisis, un reporte y una aplicación elegida. Calidad y documentación se consolidan, no se introducen por primera vez. Se comprobarán fallas, reconstrucción independiente y revisión del producto. CI, publicación y automatización real serán extensiones, no requisitos del cierre local.

Empieza con 14.01 y su lab: redacta el contrato, predice los casos y revisa sus
límites. Continúa con 14.02 para configurar, 14.03 para reconstruir el entorno,
14.04 para ejecutar el pipeline, 14.05 para comprobar sus reglas y 14.06 para
registrar y recuperar intentos fallidos; continúa con 14.07 para conciliar
reporte y app. 14.08 añade entrega opcional y reconstrucción desde fuentes.
14.09 permite demostrar la reconstrucción y defender decisiones con otra persona.

## Qué conservar

| Evidencia prevista | Qué permite revisar |
| --- | --- |
| Contrato y casos de 14.01 | Pregunta, unidades, claves, reglas y aceptación revisables |
| Estructura/configuración de 14.02 | Responsabilidades, raíz explícita y parámetros conciliados |
| Entornos y evidencia de 14.03 | Dos copias reconstruidas, versiones y resultados comparados |
| Pruebas y registros | Detección de fallas y trazabilidad |
| Reportes/app de 14.07 y entrega opcional de 14.08 | Valores conciliados, reconstrucción y defensa con evidencia personal en 14.09 |

En 14.01–14.09 conserva contrato, configuraciones, resultados por crédito,
resúmenes de pruebas y revisión humana. Añade una nota con comprobación, ayudas, dudas y siguiente paso en tu
copia personal. PROGRESS.md registra material; no es un porcentaje de aprendizaje.

<a id="prácticas-y-checkpoints-de-integración"></a>

## Criterio de salida

Para cerrar el recorrido, otra persona deberá regenerar datos, ejecutar controles que detecten una falla y reconstruir un reporte HTML y una app local. Deberás justificar herramientas, contratos y límites. 14.07 aporta integración local y 14.08 entrega opcional; la revisión de cierre y el aprendizaje necesitan evidencia propia.

La práctica integrada de 14.07 está disponible; no se han activado proyectos de projects/ ni sus checkpoints. La entrega opcional de 14.08 está disponible; la revisión final y sus plantillas están disponibles en 14.09. La práctica requiere evidencia propia.

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
Sigue con [14.03 — Entornos y ejecución reconstruible](03_reconstructible_environments/README.md).
Después realiza [14.04 — Pipeline y reprocesamiento](04_pipeline_reprocessing/README.md),
[14.05 — Pruebas y calidad de datos](05_tests_data_quality/README.md),
[14.06 — Trazabilidad y recuperación de fallas](06_traceability_recovery/README.md) y
[14.07 — Integración de reporte y app](07_report_app_integration/README.md), disponibles con sus labs.
Puedes ampliar con [14.08 — Entrega y automatización opcional](08_delivery_optional_automation/README.md) y su lab.
Cierra con [14.09 — Revisión final y defensa de decisiones](09_final_review_defense/README.md) y su lab.
La base de material está disponible; retoma práctica y [depuración transversal](../../docs/reproducible-projects-closure.md). Proyectos/checkpoints siguen pendientes.

Esta base de material cierra el recorrido numerado. No hay un módulo 15 definido. Cuando exista una entrega verificada, conserva evidencia y revisa qué resultados son apropiados para [showcase](../../showcase/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Fuentes para preparar las prácticas: [entornos uv](https://docs.astral.sh/uv/concepts/projects/sync/),
[renv](https://rstudio.github.io/renv/articles/renv.html),
[organización de pruebas pytest](https://docs.pytest.org/en/stable/explanation/goodpractices.html),
[pruebas R](https://r-pkgs.org/testing-basics.html),
[ejecución de Quarto](https://quarto.org/docs/projects/code-execution.html) y
[GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions).
14.01–14.06 conservan los entornos de cálculo mínimos; 14.07 añade interfaces
locales con versiones ya usadas en el curso. 14.08 conserva esos metadatos. Se usa unittest o R base para pruebas. pytest/testthat son ampliaciones opcionales. 14.09 reutiliza esa integración sin nuevas dependencias; futuras ampliaciones
requieren una decisión de alcance, conservando el gestor elegido.

### Apoyos relacionados

- [proyectos](../../projects/README.md)
- [Estado editorial del material](../../PROGRESS.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Volver al plan de secciones ↑](#lecciones-y-labs)

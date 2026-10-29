# 13 — Shiny y fundamentos web

[Inicio](../../README.md) / [Módulos](../README.md) / **13 — Shiny y fundamentos web**

**Ruta de aplicación R: un explorador reactivo con resultados conciliados.**

[**Empezar por 13.01 →**](01_web_first_app/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** las diez secciones con lecciones, apps locales y labs; entrega local en 13.10.
> Material disponible no acredita aprendizaje ni un proyecto de aplicación completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Convertir el análisis R conocido en una aplicación Shiny con resultados comprobables y dependencias reactivas explícitas. 13.01 introduce navegador, interfaz, servidor y primera ejecución; 13.02 conecta entradas con salidas y 13.03 explica dependencias, invalidación y demanda; 13.04 comparte filtros e indicadores y 13.05 controla eventos/estado de sesión; 13.06 valida y explica casos sin datos; 13.07 concilia gráfica y descargas; 13.08 reutiliza UI/servidor en módulos y 13.09 comprueba cálculos/transiciones y detecta regresiones. 13.10 reúne una entrega local reconstruible.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y las bases de R/tidyverse/ggplot2. [12 — Streamlit](../12_streamlit/README.md) es alternativa, no requisito. 13.01 usa el IDE de R elegido y prepara un proyecto renv independiente con Shiny 1.14.0; 13.02–13.06 conservan sus metadatos; 13.07 añade ggplot2 en su propio lockfile y 13.08–13.10 lo conservan sin cambios. No exige entregas anteriores ni modifica bibliotecas globales. El cierre no añade paquetes.

## Qué vas a aprender

Las secciones permiten construir consultas reactivas, aplicarlas por sesión y conciliar mensajes, tabla, gráfica y descargas, reutilizar UI/servidor sin mezclar instancias y comprobar el flujo con pruebas y reconstruir una entrega local. El recorrido completo prevé:

- Separar interfaz, cálculo y dependencias reactivas.
- Usar entradas, filtros y estado sin mezclar sesiones.
- Conciliar tabla, figura y descarga.
- Comprobar lógica y entregar una app local reproducible.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección o alcance | Práctica | Resultado que se comprobará |
| --- | --- | --- |
| **13.01** · [Web básica y primera app](01_web_first_app/README.md) | [Lab 13.01](../../labs/13_shiny_web/01_web_first_app/README.md) | Explicar navegador, UI, servidor y ejecución local |
| **13.02** · [Entradas y salidas](02_inputs_outputs/README.md) | [Lab 13.02](../../labs/13_shiny_web/02_inputs_outputs/README.md) | Vincular un control con una salida |
| **13.03** · [Modelo de reactividad](03_reactivity/README.md) | [Lab 13.03](../../labs/13_shiny_web/03_reactivity/README.md) | Explicar dependencias e invalidación |
| **13.04** · [Filtros e indicadores compartidos](04_shared_filters/README.md) | [Lab 13.04](../../labs/13_shiny_web/04_shared_filters/README.md) | Reutilizar un conjunto filtrado entre salidas |
| **13.05** · [Eventos y estado de sesión](05_events_session/README.md) | [Lab 13.05](../../labs/13_shiny_web/05_events_session/README.md) | Controlar acciones sin mezclar sesiones |
| **13.06** · [Validación y mensajes](06_validation_messages/README.md) | [Lab 13.06](../../labs/13_shiny_web/06_validation_messages/README.md) | Atender datos ausentes e interacciones inválidas |
| **13.07** · [Gráficos, tablas y descargas](07_outputs_downloads/README.md) | [Lab 13.07](../../labs/13_shiny_web/07_outputs_downloads/README.md) | Entregar evidencia correspondiente a los filtros |
| **13.08** · [Organización y módulos](08_organization_modules/README.md) | [Lab 13.08](../../labs/13_shiny_web/08_organization_modules/README.md) | Reutilizar una parte de UI y servidor |
| **13.09** · [Pruebas y observación del flujo](09_tests_flow/README.md) | [Lab 13.09](../../labs/13_shiny_web/09_tests_flow/README.md) | Comprobar cálculos reactivos y casos límite |
| **13.10** · [Cierre y entrega local](10_local_delivery/README.md) | [Lab 13.10](../../labs/13_shiny_web/10_local_delivery/README.md) | Reconstruir una app R con indicadores conciliados |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado por sección:** 13.01–13.10 están disponibles. La práctica personal y los proyectos/checkpoints requieren evidencia propia.

<a id="01-web-basica-y-primera-app"></a>

### 01 — Web básica y primera app

Disponible: [lección 13.01](01_web_first_app/README.md) y
[lab 13.01](../../labs/13_shiny_web/01_web_first_app/README.md). Navegador/proceso R,
HTML/CSS/JavaScript como contexto; mínimo y cuatro ventas ficticias, 660 MXN y
variante 690. UI/server/objeto app, preparación/sesión/salida, inicio/detención
y reinicio. Proyecto independiente con renv/lockfile real, biblioteca local y
recorrido principal en IDE. No implementa controles, filtros, estado propio,
descargas ni pruebas como tema; no exige construir un servidor web o una API.

<a id="02-entradas-y-salidas"></a>

### 02 — Entradas y salidas

Disponible: [lección 13.02](02_inputs_outputs/README.md) y
[lab 13.02](../../labs/13_shiny_web/02_inputs_outputs/README.md). Mínimo de texto,
selector de una venta/todas y casilla de detalle; ID/etiqueta/valor, tipos y
parejas output/render. Misma muestra de cuatro ventas/660 MXN; V003 conserva
una fila/0, ocultar no cambia consulta. Variantes de etiqueta e inicio V004/120,
metadatos de 13.01 intactos y sin paquetes nuevos. No implementa reactive()
compartido, eventos propios, persistencia ni validación general de fuentes.

<a id="03-modelo-de-reactividad"></a>

### 03 — Modelo de reactividad

Disponible: [lección 13.03](03_reactivity/README.md) y
[lab 13.03](../../labs/13_shiny_web/03_reactivity/README.md). Número/doble y nota
independiente, grafo por lecturas, invalidación frente a demanda, cache y ramas.
Consulta compartida con las mismas cuatro ventas/660 MXN; observe de diagnóstico,
sin estado propio. Preparador nuevo con funciones/metadatos previos intactos y
sin paquetes nuevos. Filtros e indicadores de cartera corresponden a 13.04.

<a id="04-filtros-e-indicadores-compartidos"></a>

### 04 — Filtros e indicadores compartidos

Disponible: [lección 13.04](04_shared_filters/README.md) y
[lab 13.04](../../labs/13_shiny_web/04_shared_filters/README.md). Mínimo de tres
filas y cartera de seis observaciones: fuente/universo/selección, corte,
segmentos y saldo mínimo inclusivo. Tabla/cantidad/saldo/cobertura comparten
selección; denominador de tres créditos por corte, vacío y cero diferenciados.
Funciones R corrientes, CSV y metadatos anteriores conservados; sin paquetes
nuevos. No implementa eventos propios, gráficas, descargas ni flujo de mensajes.

<a id="05-eventos-y-estado-de-sesion"></a>

### 05 — Eventos y estado de sesión

Disponible: [lección 13.05](05_events_session/README.md) y
[lab 13.05](../../labs/13_shiny_web/05_events_session/README.md). Mínimo con número
editado/guardado; bindEvent, botón y reactiveVal por sesión. Consulta completa
con filtros/filas/medidas aplicada solo tras éxito; borrador y contexto aplicado
separados. Rechazo conserva consulta, casilla no envía y dos sesiones no mezclan
estado. Mismos datos/metadatos sin paquetes nuevos; sin persistencia ni autenticación.

<a id="06-validacion-y-mensajes"></a>

### 06 — Validación y mensajes

Disponible: [lección 13.06](06_validation_messages/README.md) y
[lab 13.06](../../labs/13_shiny_web/06_validation_messages/README.md). req/validate/
need, mínimo textual y mensajes con acción. Rechazo conserva consulta aplicada;
fuente ausente/inválida retira cifras. Vacío sobre universo, saldo cero y corte
sin universo diferenciados; relectura completa por aplicación y recuperación.
Mismas funciones/fuente/metadatos, sin paquetes nuevos ni monitor automático.

<a id="07-graficos-tablas-y-descargas"></a>

### 07 — Gráficos, tablas y descargas

Disponible: [lección 13.07](07_outputs_downloads/README.md) y
[lab 13.07](../../labs/13_shiny_web/07_outputs_downloads/README.md). Barras ggplot2,
tabla, alt y dos CSV de selección/contexto desde la consulta aplicada. Cero,
vacío exportable y bloqueo diferenciados; descargas reales releídas por clave.
ggplot2 4.0.3 directo en lockfile de 42 registros, con 31 anteriores intactos.
Sin filtros nuevos ni cambios globales; los dos archivos no son entrega completa.

<a id="08-organizacion-y-modulos"></a>

### 08 — Organización y módulos

Disponible: [lección 13.08](08_organization_modules/README.md) y
[lab 13.08](../../labs/13_shiny_web/08_organization_modules/README.md). Mínimo de
dos instancias y módulo de consulta con UI/servidor, NS/session$ns y estado propio.
Ruta explícita y lectura reactiva para el padre; ID renombrado sin editar módulo.
A/B y sus CSV conservan cifras de 13.07; funciones/metadatos intactos sin paquetes
nuevos. Instancia, sesión y fuente compartida diferenciadas.

<a id="09-pruebas-y-observacion-del-flujo"></a>

### 09 — Pruebas y observación del flujo

[Lección 13.09](09_tests_flow/README.md) y [lab](../../labs/13_shiny_web/09_tests_flow/README.md)
disponibles. Expectativas independientes, funciones R y testServer, transiciones
de consulta y casos límite; mínimo con mensajes y regresión de salida antigua.
App modular anterior conservada, catorce CSV temporales releídos y revisión
complementaria en navegador. Sin paquetes nuevos; reactlog es ampliación opcional.

<a id="10-cierre-y-entrega-local"></a>

### 10 — Cierre y entrega local

[Lección 13.10](10_local_delivery/README.md) y [lab](../../labs/13_shiny_web/10_local_delivery/README.md)
disponibles. Entrega de fuentes/contrato/entorno y seis casos, verificador de
solo lectura con CSV externo y reconstrucción en otra carpeta con biblioteca
local nueva. Demostración de la app y descargas aparte de los archivos en lote.
Sin dependencias nuevas; despliegue y autenticación son extensiones.

</details>

## Cómo trabajar este módulo

Se avanza desde UI/reactividad a filtros, validación, organización y pruebas. RStudio o el IDE elegido es el recorrido de trabajo principal. Mastering Shiny de Hadley Wickham es la lectura abierta de apoyo. Shiny para Python no añade otra ruta obligatoria; despliegue y autenticación son extensiones.

Empieza por 13.01 y su lab, después continúa con 13.02–13.10. Cierra la práctica con reconstrucción y demostración; consulta los [criterios de Shiny](../../docs/shiny-closure.md).

## Qué conservar

| Evidencia disponible y prevista para el recorrido | Qué permite revisar |
| --- | --- |
| App/proyecto/metadatos de 13.01 | Navegador, UI, servidor y reconstrucción de la primera ejecución |
| Consultas y variantes de 13.02 | ID/etiqueta/valor, salidas y visibilidad sin cambiar datos |
| Grafos y predicciones de 13.03 | Dependencias, ramas, cache y demanda |
| Selección e indicadores de 13.04 | Filas por clave, suma y denominador |
| Transiciones y sesiones de 13.05 | Borrador, aplicación, rechazo y recarga |
| Mensajes y recuperación de 13.06 | Entradas, vacío, fuente y retirada de cifras |
| Gráfica y CSV de 13.07 | Alturas, filas, filtros y medidas de la consulta aplicada |
| Instancias y API de 13.08 | UI/servidor, namespaces y estado independiente |
| Pruebas y regresión de 13.09 | Funciones, transiciones, salida desactualizada y límites de cada capa |
| Entrega local de 13.10 | Fuentes, entorno, seis casos, contraste externo y reconstrucción |

En 13.01–13.10 conserva archivos, cálculo por venta, variantes, consultas, grafos y observaciones de consola/reinicio. Guarda una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje. Los filtros compartidos se practican en 13.04; la entrega completa se practica en 13.10.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

El cierre requiere explicar las dependencias reactivas y demostrar que tabla, figura y descarga reflejan los mismos filtros. Una app local reconstruida y comprobada basta. Las diez secciones ofrecen material, incluida la entrega de 13.10; disponer de ellas no acredita práctica completada.

06_shiny_portfolio_app está previsto en [proyectos](../../projects/README.md), sin carpeta ni checkpoints implementados.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, UI y reactividad (01–03); CP-02, filtros, estado
y validación (04–06); CP-03, presentación y organización (07–08); CP-04, pruebas
y entrega (09–10). Sus nombres se concretarán al desarrollar el proyecto.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

Empieza por [13.01 — Web básica y primera app](01_web_first_app/README.md), continúa con [13.02 — Entradas y salidas](02_inputs_outputs/README.md) y consulta después [13.03 — Modelo de reactividad](03_reactivity/README.md). Sigue con [13.04 — Filtros e indicadores compartidos](04_shared_filters/README.md); continúa con [13.05 — Eventos y estado de sesión](05_events_session/README.md). Sigue con [13.06 — Validación y mensajes](06_validation_messages/README.md). Continúa con [13.07 — Gráficos, tablas y descargas](07_outputs_downloads/README.md). Continúa con [13.08 — Organización y módulos](08_organization_modules/README.md). Continúa con [13.09 — Pruebas y observación del flujo](09_tests_flow/README.md). Continúa con [13.10 — Cierre y entrega local](10_local_delivery/README.md).

Cuando cierres la práctica de esta ruta, sigue con [14.01 — Pregunta y contrato del producto](../14_reproducible_projects/01_product_question_contract/README.md), disponible con lección y lab; 14.02–14.05 también tienen lecciones/labs y 14.06–14.09 siguen planificadas. La otra aplicación queda como comparación opcional.

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Lecturas: [Mastering Shiny](https://mastering-shiny.org/) y su capítulo de
[reactividad básica](https://mastering-shiny.org/basic-reactivity.html).
Documentación oficial: [primeros pasos](https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/),
[módulos](https://shiny.posit.co/r/articles/improve/modules/) y
[testServer](https://shiny.posit.co/r/reference/shiny/latest/testserver.html).
No se instalan paquetes ni servicios por planificar este módulo.

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Volver al plan de secciones ↑](#lecciones-y-labs)

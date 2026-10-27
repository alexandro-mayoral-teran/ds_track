# 13 — Shiny y fundamentos web

[Inicio](../../README.md) / [Módulos](../README.md) / **13 — Shiny y fundamentos web**

**Ruta de aplicación R: un explorador reactivo con resultados conciliados.**

[Ver primera sección prevista →](#01-web-basica-y-primera-app) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Planificado:** 10 secciones previstas; sus lecciones y labs aún no están implementados.
> Los enlaces de esta tabla describen el alcance del plan, no una práctica lista para ejecutar.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Convertir el análisis R conocido en una aplicación Shiny con resultados comprobables y dependencias reactivas explícitas. Las secciones y labs siguen planificados.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y las bases de R/tidyverse/ggplot2. [12 — Streamlit](../12_streamlit/README.md) es alternativa, no requisito. Usa el IDE y entorno R elegidos cuando se implemente; la planificación no instala paquetes.

## Qué vas a aprender

Objetivos previstos para cuando se implemente:

- Separar interfaz, cálculo y dependencias reactivas.
- Usar entradas, filtros y estado sin mezclar sesiones.
- Conciliar tabla, figura y descarga.
- Comprobar lógica y entregar una app local reproducible.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección prevista | Práctica | Resultado previsto |
| --- | --- | --- |
| **13.01** · [Web básica y primera app](#01-web-basica-y-primera-app) | Pendiente | Explicar navegador, UI, servidor y ejecución local |
| **13.02** · [Entradas y salidas](#02-entradas-y-salidas) | Pendiente | Vincular un control con una salida |
| **13.03** · [Modelo de reactividad](#03-modelo-de-reactividad) | Pendiente | Explicar dependencias e invalidación |
| **13.04** · [Filtros e indicadores compartidos](#04-filtros-e-indicadores-compartidos) | Pendiente | Reutilizar un conjunto filtrado entre salidas |
| **13.05** · [Eventos y estado de sesión](#05-eventos-y-estado-de-sesion) | Pendiente | Controlar acciones sin mezclar sesiones |
| **13.06** · [Validación y mensajes](#06-validacion-y-mensajes) | Pendiente | Atender datos ausentes e interacciones inválidas |
| **13.07** · [Gráficos, tablas y descargas](#07-graficos-tablas-y-descargas) | Pendiente | Entregar evidencia correspondiente a los filtros |
| **13.08** · [Organización y módulos](#08-organizacion-y-modulos) | Pendiente | Reutilizar una parte de UI y servidor |
| **13.09** · [Pruebas y observación del flujo](#09-pruebas-y-observacion-del-flujo) | Pendiente | Comprobar cálculos reactivos y casos límite |
| **13.10** · [Cierre y entrega local](#10-cierre-y-entrega-local) | Pendiente | Reconstruir una app R con indicadores conciliados |

<a id="alcance-de-cada-sección"></a>

### Alcance previsto por sección

<a id="01-web-basica-y-primera-app"></a>

### 01 — Web básica y primera app

- Cliente/navegador y proceso R servidor; HTML/CSS como contexto de presentación.
  UI, server y app.R; distinguir código que prepara datos y código por sesión.
- Práctica prevista: iniciar una app mínima y reconocer sus piezas. No se exige
  construir un servidor web, aprender JavaScript ni diseñar una API.

<a id="02-entradas-y-salidas"></a>

### 02 — Entradas y salidas

- Identificadores, controles, output, render y funciones de presentación.
  Etiquetas claras y correspondencia entre UI y servidor.
- Práctica prevista: mostrar un valor elegido y una tabla conocida, comprobando
  nombres y tipos antes de incorporar varios filtros.

<a id="03-modelo-de-reactividad"></a>

### 03 — Modelo de reactividad

- Expresiones reactivas, consumidores, dependencias e invalidación; diferenciar
  reactive, render y observe. No tratar la app como un script lineal de una sola ejecución.
- Práctica prevista: dibujar un flujo pequeño y verificar qué resultados cambian
  al modificar una entrada. Las APIs se comprobarán para la versión elegida.

<a id="04-filtros-e-indicadores-compartidos"></a>

### 04 — Filtros e indicadores compartidos

- Expresión reactiva para seleccionar datos y funciones comunes para calcular;
  evitar filtros distintos en tabla, gráfica e indicador.
- Práctica prevista: cambiar corte/segmento y conciliar todas las salidas contra
  el análisis conocido. No mezclar la lógica de datos con funciones de UI.

<a id="05-eventos-y-estado-de-sesion"></a>

### 05 — Eventos y estado de sesión

- Botones, ejecución vinculada a eventos y reactiveVal/reactiveValues cuando
  sean necesarios. Distinguir estado de sesión de objetos globales compartidos.
- Práctica prevista: aplicar filtros mediante una acción y comprobar independencia
  entre sesiones. Caché y tareas asíncronas quedan para necesidades posteriores.

<a id="06-validacion-y-mensajes"></a>

### 06 — Validación y mensajes

- req, validate y need para condiciones de entrada/salida, con mensajes de contexto.
  Diferenciar dato desconocido, conjunto vacío y error inesperado.
- Práctica prevista: datos ausentes y filtro sin coincidencias sin publicar cifras
  engañosas ni ocultar una falla del programa.

<a id="07-graficos-tablas-y-descargas"></a>

### 07 — Gráficos, tablas y descargas

- ggplot2, tablas legibles y downloadHandler; filtros, corte y unidades explícitos.
- Práctica prevista: verificar que lo descargado coincide con lo presentado.
  Tablas avanzadas y uploads serán ampliaciones cuando aporten valor.

<a id="08-organizacion-y-modulos"></a>

### 08 — Organización y módulos

- Funciones de datos fuera del servidor; módulo UI/servidor con namespace.
  moduleServer y composición para una parte repetida de la app.
- Práctica prevista: extraer un filtro/resumen sin alterar sus resultados. Una app
  pequeña no necesita dividir cada widget en un módulo para estar bien organizada.

<a id="09-pruebas-y-observacion-del-flujo"></a>

### 09 — Pruebas y observación del flujo

- Casos de funciones y testServer para lógica reactiva; cambios de entradas,
  resultados vacíos y fallas esperadas. Observación del flujo cuando ayude a depurar.
- Práctica prevista: detectar un indicador desactualizado; complementar con revisión
  en navegador. Pruebas completas de navegador son una ampliación posterior.

<a id="10-cierre-y-entrega-local"></a>

### 10 — Cierre y entrega local

- Proyecto renv, datos reconstruibles, instrucciones y demostración de filtros.
- Práctica prevista: ejecutar desde una sesión limpia y conciliar un caso conocido.
  Despliegue, autenticación, CSS avanzado y escalabilidad son extensiones; no
  se requiere un servicio de pago para cerrar el módulo.

## Cómo trabajar este módulo

Se prevé avanzar desde UI/reactividad a filtros, validación, organización y pruebas. RStudio o el IDE elegido será el recorrido de trabajo principal. Mastering Shiny de Hadley Wickham es la lectura abierta de apoyo. Shiny para Python no añade otra ruta obligatoria; despliegue y autenticación son extensiones.

Las actividades anteriores son una propuesta. No hay instrucciones ejecutables ni comprobaciones de aprendizaje disponibles todavía para estas secciones.

## Qué conservar

| Evidencia prevista | Qué permite revisar |
| --- | --- |
| Código y dependencias previstas | Responsabilidades y reactividad |
| Casos de prueba | Filtros, errores y sesiones |
| Entrega local futura | Reconstrucción de tabla, figura y descarga |

Cuando exista la práctica, conserva los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Cuando se implemente, deberás explicar las dependencias reactivas y demostrar que tabla, figura y descarga reflejan los mismos filtros. Una app local comprobada bastará; hoy no hay una entrega ejecutable ni práctica completada por disponer del plan.

06_shiny_portfolio_app está previsto en [proyectos](../../projects/README.md), sin carpeta ni checkpoints implementados.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Checkpoints propuestos: CP-01, UI y reactividad (01–03); CP-02, filtros, estado
y validación (04–06); CP-03, presentación y organización (07–08); CP-04, pruebas
y entrega (09–10). Sus nombres se concretarán al desarrollar el proyecto.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

Por ahora puedes [consultar el primer alcance previsto](#01-web-basica-y-primera-app). No hay lecciones ni labs listos en este módulo.

Cuando esta ruta esté implementada y cierres la práctica, sigue con [14 — Proyecto reproducible](../14_reproducible_projects/README.md), también planificado. La otra aplicación queda como comparación opcional.

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

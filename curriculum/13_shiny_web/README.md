# 13 — Shiny y fundamentos web

## Propósito y prerrequisitos

Convertir el análisis R conocido en un explorador reactivo con resultados
comprobables. Completa [11 — Reportes con Quarto](../11_reporting_quarto/README.md)
y las bases de R/tidyverse/ggplot2. El nivel 12 no es un prerrequisito: Streamlit
es la ruta alternativa Python y basta elegir una aplicación.

**Estado:** diez secciones planificadas; lecciones y labs por desarrollar.
Los enlaces internos describen el alcance previsto.

Trabajaremos con Shiny para R y datos sintéticos locales. Mastering Shiny,
de Hadley Wickham, será la lectura abierta de apoyo. Shiny para Python se
reconoce como otra opción, pero no añade una tercera ruta obligatoria al track.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Web básica y primera app](#01-web-basica-y-primera-app) | Esencial | Explicar navegador, UI, servidor y ejecución local |
| 2 | [Entradas y salidas](#02-entradas-y-salidas) | Esencial | Vincular un control con una salida |
| 3 | [Modelo de reactividad](#03-modelo-de-reactividad) | Esencial | Explicar dependencias e invalidación |
| 4 | [Filtros e indicadores compartidos](#04-filtros-e-indicadores-compartidos) | Esencial | Reutilizar un conjunto filtrado entre salidas |
| 5 | [Eventos y estado de sesión](#05-eventos-y-estado-de-sesion) | Práctica | Controlar acciones sin mezclar sesiones |
| 6 | [Validación y mensajes](#06-validacion-y-mensajes) | Esencial | Atender datos ausentes e interacciones inválidas |
| 7 | [Gráficos, tablas y descargas](#07-graficos-tablas-y-descargas) | Práctica | Entregar evidencia correspondiente a los filtros |
| 8 | [Organización y módulos](#08-organizacion-y-modulos) | Práctica | Reutilizar una parte de UI y servidor |
| 9 | [Pruebas y observación del flujo](#09-pruebas-y-observacion-del-flujo) | Esencial | Comprobar cálculos reactivos y casos límite |
| 10 | [Cierre y entrega local](#10-cierre-y-entrega-local) | Práctica de cierre | Reconstruir una app R con indicadores conciliados |

## Alcance de cada sección

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

## Prácticas, proyecto y criterio de salida

Se prevén labs 13.01–13.10; todavía no existen. El proyecto previsto
06_shiny_portfolio_app está en [proyectos](../../projects/README.md), sin carpeta implementada.

Checkpoints propuestos: CP-01, UI y reactividad (01–03); CP-02, filtros, estado
y validación (04–06); CP-03, presentación y organización (07–08); CP-04, pruebas
y entrega (09–10). Sus nombres se concretarán al desarrollar el proyecto.

Para avanzar debes explicar las dependencias reactivas y demostrar que tabla,
figura y descarga reflejan los mismos filtros. La app local comprobada es suficiente;
no hace falta crear también Streamlit ni dominar objetos avanzados de R.

## Continuidad y referencias

Continúa con [14 — Proyecto reproducible](../14_reproducible_projects/README.md).
Puedes estudiar [12 — Streamlit](../12_streamlit/README.md) después como comparación.

Lecturas: [Mastering Shiny](https://mastering-shiny.org/) y su capítulo de
[reactividad básica](https://mastering-shiny.org/basic-reactivity.html).
Documentación oficial: [primeros pasos](https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/),
[módulos](https://shiny.posit.co/r/articles/improve/modules/) y
[testServer](https://shiny.posit.co/r/reference/shiny/latest/testserver.html).
La planificación no instala paquetes ni servicios.

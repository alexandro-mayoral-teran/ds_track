# 12 — Streamlit

[Inicio](../../README.md) / [Módulos](../README.md) / **12 — Streamlit**

**Ruta de aplicación Python: un explorador verificable con Streamlit.**

[**Empezar por 12.01 →**](01_first_app_execution/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** 12.01 con lección, dos apps locales y lab. 12.02–12.09 siguen planificadas.
> Disponer de material no acredita aprendizaje ni un proyecto de aplicación completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Crear un explorador de datos con filtros, indicadores y figuras comprobables, reutilizando funciones del análisis conocido. 12.01 inicia con ejecución y reejecución; los filtros y demás capacidades se desarrollarán después.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y las bases Python del recorrido. [13 — Shiny](../13_shiny_web/README.md) es alternativa, no prerrequisito. Para 12.01, sigue su preparación con Streamlit 1.66.1 en un entorno local; el resto del módulo conserva su plan.

## Qué vas a aprender

12.01 permite iniciar/detener una app y observar sus pasadas. El recorrido completo prevé:

- Explicar reejecución, estado de sesión y caché.
- Separar cálculo comprobable e interfaz.
- Conectar filtros, tablas, figuras y descarga del mismo universo.
- Probar entradas inválidas, selección vacía y reconstrucción local.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección o alcance | Práctica | Resultado que se comprobará |
| --- | --- | --- |
| **12.01** · [Primera app y modelo de ejecución](01_first_app_execution/README.md) | [Lab 12.01](../../labs/12_streamlit/01_first_app_execution/README.md) | Ejecutar una app y explicar sus reejecuciones |
| **12.02** · [Entradas, filtros y presentación](#02-entradas-filtros-y-presentacion) | Pendiente | Conectar widgets con un subconjunto verificable |
| **12.03** · [Separar datos e interfaz](#03-separar-datos-e-interfaz) | Pendiente | Reutilizar transformaciones fuera de la app |
| **12.04** · [Estado de sesión y formularios](#04-estado-de-sesion-y-formularios) | Pendiente | Conservar elecciones y controlar cuándo aplicarlas |
| **12.05** · [Caché de datos y recursos](#05-cache-de-datos-y-recursos) | Pendiente | Evitar trabajo repetido sin mostrar resultados obsoletos |
| **12.06** · [Mensajes y casos sin datos](#06-mensajes-y-casos-sin-datos) | Pendiente | Explicar entradas inválidas y filtros vacíos |
| **12.07** · [Tablas, gráficos y descarga](#07-tablas-graficos-y-descarga) | Pendiente | Presentar y exportar el mismo universo filtrado |
| **12.08** · [Pruebas de la aplicación](#08-pruebas-de-la-aplicacion) | Pendiente | Comprobar indicadores y comportamiento de widgets |
| **12.09** · [Cierre y entrega local](#09-cierre-y-entrega-local) | Pendiente | Reconstruir y usar un explorador comprobado |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado por sección:** 12.01 está disponible. 12.02–12.09 describen el alcance previsto; no son lecciones o labs listos.

<a id="01-primera-app-y-modelo-de-ejecucion"></a>

### 01 — Primera app y modelo de ejecución

Disponible: [lección 12.01](01_first_app_execution/README.md) y
[lab 12.01](../../labs/12_streamlit/01_first_app_execution/README.md). Mínimo de
300 MXN y cuatro ventas ficticias con total 660; casilla, botón, variable local
y marcas de pasada. Entorno/comandos por gestor y shell; Streamlit 1.66.1 en
grupo propio, sin instalar globalmente. Variante 690 y nuevo arranque; no exige
CSV, estado propio, caché, filtros de negocio ni despliegue.

<a id="02-entradas-filtros-y-presentacion"></a>

### 02 — Entradas, filtros y presentación

- Widgets con etiquetas claras, opciones, valores iniciales, sidebar y áreas de salida.
  Distinguir variable de entrada y resultado filtrado.
- Práctica prevista: filtrar corte/segmento y conciliar cantidad e indicador con
  una función conocida. No introducir nuevos cálculos financieros desde la interfaz.

<a id="03-separar-datos-e-interfaz"></a>

### 03 — Separar datos e interfaz

- Lectura, validación y cálculo en funciones importables; la app coordina y presenta.
  Configuración y rutas sin depender de la ubicación accidental de la terminal.
- Práctica prevista: utilizar la misma transformación en app y script y demostrar
  que devuelve el mismo resultado.

<a id="04-estado-de-sesion-y-formularios"></a>

### 04 — Estado de sesión y formularios

- session_state, claves de widgets y formularios para agrupar cambios.
  Diferenciar estado de una sesión, variables del script y persistencia externa.
- Práctica prevista: conservar filtros entre reejecuciones y aplicar una combinación
  solo al enviar un formulario, explicando qué ocurre al abrir otra sesión.

<a id="05-cache-de-datos-y-recursos"></a>

### 05 — Caché de datos y recursos

- cache_data frente a cache_resource; parámetros, vigencia e invalidación cuando
  cambia la fuente. Los recursos compartidos requieren revisar uso concurrente.
- Práctica prevista: evitar una lectura repetida y comprobar que un cambio de corte
  o versión de datos actualiza el resultado. Caché no equivale a estado privado de sesión.

<a id="06-mensajes-y-casos-sin-datos"></a>

### 06 — Mensajes y casos sin datos

- Mostrar carga, datos ausentes, entradas inválidas y filtros sin coincidencias.
  No presentar cero como indicador válido cuando el dato es desconocido.
- Práctica prevista: probar una entrada incorrecta y un resultado vacío, con
  mensajes útiles y sin continuar hacia un cálculo que no tiene significado.

<a id="07-tablas-graficos-y-descarga"></a>

### 07 — Tablas, gráficos y descarga

- Tabla, métricas y Matplotlib/Altair sobre la misma selección; leyendas y unidades.
  Descarga de una salida con nombre/corte explícitos y contenido comprobado.
- Práctica prevista: comparar lo mostrado con lo descargado y con el indicador
  de referencia. Archivos arbitrarios del usuario serán una ampliación, no el inicio.

<a id="08-pruebas-de-la-aplicacion"></a>

### 08 — Pruebas de la aplicación

- Pruebas de funciones y AppTest para entradas, salidas y excepciones; sesión
  nueva, filtro vacío y cambio de corte. La revisión visual complementa las pruebas.
- Práctica prevista: detectar una regresión que desajuste tabla, indicador y descarga.
  Las versiones y capacidades del framework de prueba se verificarán al implementar.

<a id="09-cierre-y-entrega-local"></a>

### 09 — Cierre y entrega local

- Instrucciones, versiones, datos regenerables y catálogo de filtros/indicadores.
- Práctica prevista: iniciar desde un entorno limpio, reproducir un caso conocido
  y entregar una demostración. Multipágina, fragments, autenticación y despliegue
  en línea quedan como extensiones según una necesidad concreta.

</details>

## Cómo trabajar este módulo

Recorrido previsto: empezar con una app local pequeña, incorporar entradas y estado, comprobar caché y casos vacíos, y cerrar con pruebas y entrega. No exige login, alojamiento ni conocimientos avanzados de HTML/CSS/JavaScript. Basta elegir esta ruta o Shiny.

Empieza por 12.01 y su lab. Las actividades de 12.02–12.09 siguen siendo una propuesta; no intentes ejecutar todavía esos alcances.

## Qué conservar

| Evidencia prevista | Qué permite revisar |
| --- | --- |
| Fuentes y funciones previstas | Separación de datos e interfaz |
| Casos y resultados esperados | Coherencia de filtros y manejo de vacío |
| Instrucciones y app local futura | Reconstrucción y explicación del comportamiento |

En 12.01 conserva tu copia de la app, predicciones y observaciones. Para el recorrido completo, conserva los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Cuando se implemente, el cierre requerirá explicar reejecución, estado y caché y demostrar indicadores verificables con filtros. Publicar en Internet no será requisito; hoy este criterio es previsto, no una práctica acreditable.

No hay proyecto integrador ni checkpoint de aplicación Streamlit implementado; 12.01 es una práctica introductoria. Sus hitos se definirán como alternativa a la ruta Shiny.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Hitos propuestos: app mínima (01–02), lógica y estado (03–04), actualización y
casos límite (05–06), presentación verificada (07), pruebas y entrega (08–09).

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

Empieza por [12.01 — Primera app y modelo de ejecución](01_first_app_execution/README.md). Después del lab, consulta el [alcance de 12.02](#02-entradas-filtros-y-presentacion), aún planificado.

Cuando esta ruta esté implementada y cierres la práctica, sigue con [14 — Proyecto reproducible](../14_reproducible_projects/README.md), también planificado. La otra aplicación queda como comparación opcional.

<details>
<summary><strong>Referencias y apoyos</strong></summary>

Documentación oficial: [modelo de ejecución](https://docs.streamlit.io/develop/concepts/architecture),
[estado de sesión](https://docs.streamlit.io/develop/concepts/architecture/session-state),
[caché](https://docs.streamlit.io/develop/concepts/architecture/caching) y
[pruebas de apps](https://docs.streamlit.io/develop/concepts/app-testing).
12.01 registra su grupo de dependencias; las secciones restantes no añaden paquetes solo por planificar.

### Apoyos relacionados

- [proyectos](../../projects/README.md)

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Volver al plan de secciones ↑](#lecciones-y-labs)

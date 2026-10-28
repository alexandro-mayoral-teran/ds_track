# 12 — Streamlit

[Inicio](../../README.md) / [Módulos](../README.md) / **12 — Streamlit**

**Ruta de aplicación Python: un explorador verificable con Streamlit.**

[**Empezar por 12.01 →**](01_first_app_execution/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** 12.01–12.06 con lecciones, apps locales y labs. 12.07–12.09 siguen planificadas.
> Disponer de material no acredita aprendizaje ni un proyecto de aplicación completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Crear un explorador de datos con filtros, indicadores y figuras comprobables,
reutilizando funciones del análisis conocido. El recorrido conecta entradas,
estado, caché y mensajes; después incorporará presentación y entrega verificadas.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y las bases Python del recorrido. [13 — Shiny](../13_shiny_web/README.md) es alternativa, no prerrequisito. Para 12.01, sigue su preparación con Streamlit 1.66.1 en un entorno local; 12.02–12.06 reutilizan ese entorno; 12.07–12.09 conservan su plan.

## Qué vas a aprender

Las secciones disponibles permiten iniciar una app, filtrar, reutilizar funciones,
controlar estado y caché, y explicar errores y vacíos. El recorrido completo prevé:

- Explicar reejecución, estado de sesión y caché.
- Separar cálculo comprobable e interfaz.
- Conectar filtros, tablas, figuras y descarga del mismo universo.
- Probar entradas inválidas, selección vacía y reconstrucción local.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección o alcance | Práctica | Resultado que se comprobará |
| --- | --- | --- |
| **12.01** · [Primera app y modelo de ejecución](01_first_app_execution/README.md) | [Lab 12.01](../../labs/12_streamlit/01_first_app_execution/README.md) | Ejecutar una app y explicar sus reejecuciones |
| **12.02** · [Entradas, filtros y presentación](02_inputs_filters_presentation/README.md) | [Lab 12.02](../../labs/12_streamlit/02_inputs_filters_presentation/README.md) | Conectar widgets con un subconjunto verificable |
| **12.03** · [Separar datos e interfaz](03_data_interface/README.md) | [Lab 12.03](../../labs/12_streamlit/03_data_interface/README.md) | Reutilizar transformaciones fuera de la app |
| **12.04** · [Estado de sesión y formularios](04_session_state_forms/README.md) | [Lab 12.04](../../labs/12_streamlit/04_session_state_forms/README.md) | Conservar elecciones y controlar cuándo aplicarlas |
| **12.05** · [Caché de datos y recursos](05_data_resource_cache/README.md) | [Lab 12.05](../../labs/12_streamlit/05_data_resource_cache/README.md) | Evitar trabajo repetido sin mostrar resultados obsoletos |
| **12.06** · [Mensajes y casos sin datos](06_messages_empty_cases/README.md) | [Lab 12.06](../../labs/12_streamlit/06_messages_empty_cases/README.md) | Explicar entradas inválidas y filtros vacíos |
| **12.07** · [Tablas, gráficos y descarga](#07-tablas-graficos-y-descarga) | Pendiente | Presentar y exportar el mismo universo filtrado |
| **12.08** · [Pruebas de la aplicación](#08-pruebas-de-la-aplicacion) | Pendiente | Comprobar indicadores y comportamiento de widgets |
| **12.09** · [Cierre y entrega local](#09-cierre-y-entrega-local) | Pendiente | Reconstruir y usar un explorador comprobado |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado por sección:** 12.01–12.06 están disponibles. 12.07–12.09 describen el alcance previsto; no son lecciones o labs listos.

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

Disponible: [lección 12.02](02_inputs_filters_presentation/README.md) y
[lab 12.02](../../labs/12_streamlit/02_inputs_filters_presentation/README.md).
Seis observaciones propias de créditos/cortes: selectbox, multiselect y mínimo
entero en sidebar; universo antes de segmento/mínimo, pares y métricas desde
la misma selección. Octubre ≥ 2000: 003/2600, 1 de 3 (33.33%); septiembre: dos/4500.
Frontera 2000/2001, ningún segmento, vacío y recuperación, sin dependencias nuevas.
La separación en funciones importables está disponible en [12.03](03_data_interface/README.md); no se dan por
implementados en 12.02 estado, caché, descarga o validación general de fuentes externas.

<a id="03-separar-datos-e-interfaz"></a>

### 03 — Separar datos e interfaz

Disponible: [lección 12.03](03_data_interface/README.md) y
[lab 12.03](../../labs/12_streamlit/03_data_interface/README.md). CSV autónomo de
seis filas; módulo sin Streamlit para lectura/validación/análisis, configuración
con ruta propia y consumidores app/JSON. Misma selección e indicadores; variante
2600 → 2800 y universo 4600 → 4800, validación completa antes del filtro,
importación sin lectura y ejecución desde otra carpeta. Sin paquetes nuevos,
estado propio ni caché; no exige entregas anteriores.

<a id="04-estado-de-sesion-y-formularios"></a>

### 04 — Estado de sesión y formularios

Disponible: [lección 12.04](04_session_state_forms/README.md) y
[lab 12.04](../../labs/12_streamlit/04_session_state_forms/README.md). Contador mínimo,
claves de widgets y propias, formulario con envío explícito y copia de filtros
aplicados; otra pasada conserva elecciones, otra sesión vuelve al inicio.
Preparador a destino nuevo reutiliza funciones/CSV de 12.03 sin duplicar algoritmos.
Octubre 003/2600 → septiembre 003/2500 al confirmar; variante 2800/4800 releída
sin nuevo envío. Sin caché, persistencia en disco ni dependencias nuevas.

<a id="05-cache-de-datos-y-recursos"></a>

### 05 — Caché de datos y recursos

Disponible: [lección 12.05](05_data_resource_cache/README.md) y
[lab 12.05](../../labs/12_streamlit/05_data_resource_cache/README.md). Cache_data
para el análisis, con registros completos, filtros y versión; lectura/validación
antes de caché. TTL 60, ocho entradas y limpieza por función, sin persistencia
en disco. Variante 2800/4800, rechazo fuera del filtro, caducidad y copias; mínimo
cache_resource de lectura distingue identidad compartida de estado de sesión.
No acredita evitar la lectura, acelerar seis filas ni acotar RAM; sin paquetes nuevos.

<a id="06-mensajes-y-casos-sin-datos"></a>

### 06 — Mensajes y casos sin datos

Disponible: [lección 12.06](06_messages_empty_cases/README.md) y
[lab 12.06](../../labs/12_streamlit/06_messages_empty_cases/README.md). Mensajes con
efecto/acción, spinner breve, diagnóstico y stop. Texto del mínimo validado antes
de aplicar; intento rechazado conserva los filtros válidos identificados.
Fuente ausente/inválida, encabezado sin filas y corte sin registros detienen
métricas; selección vacía válida y cero observado se distinguen. Reintento y
recuperación sin cifras anteriores, avisos independientes de ocultar la tabla.
Reutiliza funciones/caché de 12.03/12.05; sin dependencias nuevas.

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

Empieza por 12.01 y su lab. Las actividades de 12.07–12.09 siguen siendo una propuesta; no intentes ejecutar todavía esos alcances.

## Qué conservar

| Evidencia prevista | Qué permite revisar |
| --- | --- |
| Fuentes y funciones previstas | Separación de datos e interfaz |
| Casos y resultados esperados | Coherencia de filtros y manejo de vacío |
| Instrucciones y app local futura | Reconstrucción y explicación del comportamiento |

En 12.01–12.06 conserva tu copia, parámetros efectivos, predicciones y resultados:
filas, indicadores, estado, reutilización y mensajes deben poder explicarse.
Guarda una nota con comprobaciones, ayudas, dudas y siguiente paso en tu copia
personal. PROGRESS.md registra desarrollo del material, no porcentaje de aprendizaje.

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

Empieza por [12.01 — Primera app y modelo de ejecución](01_first_app_execution/README.md)
y sigue el orden de [lecciones y labs](#lecciones-y-labs). El último material
disponible es [12.06 — Mensajes y casos sin datos](06_messages_empty_cases/README.md).

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

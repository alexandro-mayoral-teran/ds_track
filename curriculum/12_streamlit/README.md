# 12 — Streamlit

[Inicio](../../README.md) / [Módulos](../README.md) / **12 — Streamlit**

**Ruta de aplicación Python: un explorador verificable con Streamlit.**

[**Empezar por 12.01 →**](01_first_app_execution/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Disponible:** las nueve secciones 12.01–12.09, con lecciones, apps locales y labs.
> Disponer de material no acredita aprendizaje ni un proyecto de aplicación completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Crear un explorador de datos con filtros, indicadores y figuras comprobables,
reutilizando funciones del análisis conocido. El recorrido conecta entradas,
estado, caché, mensajes, presentación conciliada, pruebas y entrega local.

## Antes de empezar

Completa [11 — Quarto](../11_reporting_quarto/README.md) y las bases Python del recorrido. [13 — Shiny](../13_shiny_web/README.md) es alternativa, no prerrequisito. Para 12.01, sigue su preparación con Streamlit 1.66.1 en un entorno local; 12.02–12.09 reutilizan ese entorno. El cierre también explica cómo reconstruirlo en otra copia.

## Qué vas a aprender

Las secciones disponibles permiten iniciar una app, filtrar, reutilizar funciones,
controlar estado y caché, explicar errores y vacíos, conciliar tabla, gráfico y descarga, probar cálculos y transiciones, y entregar una copia reconstruible. El recorrido permite practicar:

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
| **12.07** · [Tablas, gráficos y descarga](07_tables_charts_download/README.md) | [Lab 12.07](../../labs/12_streamlit/07_tables_charts_download/README.md) | Presentar y exportar el mismo universo filtrado |
| **12.08** · [Pruebas de la aplicación](08_app_testing/README.md) | [Lab 12.08](../../labs/12_streamlit/08_app_testing/README.md) | Comprobar indicadores y comportamiento de widgets |
| **12.09** · [Cierre y entrega local](09_local_delivery/README.md) | [Lab 12.09](../../labs/12_streamlit/09_local_delivery/README.md) | Reconstruir y usar un explorador comprobado |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

**Estado por sección:** las nueve secciones 12.01–12.09 están disponibles. La práctica personal y los proyectos/checkpoints se revisan por separado.

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

Disponible: [lección 12.07](07_tables_charts_download/README.md) y
[lab 12.07](../../labs/12_streamlit/07_tables_charts_download/README.md). Tabla,
Altair y CSV desde la misma selección; IDs nominales, pesos, etiquetas y alternativa
textual. Contexto JSON con filtros/universo/indicadores y huella del CSV; descargas
preparadas en memoria y revisor de solo lectura. Vacío válido exporta encabezado;
intento rechazado bloquea botones y fuente/corte ausente no ofrece archivos.
Descarga real, borrador, variante y móvil conciliados; sin dependencias nuevas.

<a id="08-pruebas-de-la-aplicacion"></a>

### 08 — Pruebas de la aplicación

Disponible: [lección 12.08](08_app_testing/README.md) y
[lab 12.08](../../labs/12_streamlit/08_app_testing/README.md). Mínimo autónomo,
pruebas de funciones y AppTest, expectativas por clave, errores tratados,
fronteras, vacío, recuperación y sesión nueva. Regresión deliberada en copia
independiente y protocolo de revisión en navegador/descarga real. CSV temporal,
configuración restaurada y limpieza de caché; sin dependencias nuevas. Inspección
del protocolo del gráfico como ampliación ligada a Streamlit 1.66.1.

<a id="09-cierre-y-entrega-local"></a>

### 09 — Cierre y entrega local

Disponible: [lección 12.09](09_local_delivery/README.md) y
[lab 12.09](../../labs/12_streamlit/09_local_delivery/README.md). Entrega local
con fuente/contrato, código/pruebas, metadatos bloqueados, seis análisis y cinco
pares CSV/JSON calculados. Constructor exclusivo y revisor de solo lectura
contra CSV externo por ID/corte; reconstrucción y demostración real separadas
de las huellas. No requiere entregas previas ni dependencias nuevas. Multipágina,
fragments, autenticación y despliegue son ampliaciones; no activa proyectos/checkpoints.

</details>

## Cómo trabajar este módulo

Recorrido: empezar con una app local pequeña, incorporar entradas y estado, comprobar caché y casos vacíos, y cerrar con pruebas y entrega. No exige login, alojamiento ni conocimientos avanzados de HTML/CSS/JavaScript. Basta elegir esta ruta o Shiny.

Empieza por 12.01 y su lab. En 12.09 reconstruye una entrega en otra carpeta y contrástala con una referencia externa antes de demostrarla.

## Qué conservar

| Evidencia de las secciones disponibles | Qué permite revisar |
| --- | --- |
| Copia preparada y funciones reutilizadas | Separación de datos e interfaz |
| Casos, parámetros y resultados | Coherencia de filtros, estado, caché y vacío |
| CSV y contexto JSON descargados | Correspondencia entre filas, gráfico e indicadores |
| Instrucciones y app local | Reconstrucción y explicación del comportamiento |

En 12.01–12.09 conserva tu copia, parámetros efectivos, predicciones y resultados:
filas, indicadores, estado, reutilización, mensajes, descargas y pruebas deben poder explicarse.
Guarda una nota con comprobaciones, ayudas, dudas y siguiente paso en tu copia
personal. PROGRESS.md registra desarrollo del material, no porcentaje de aprendizaje.

<a id="prácticas-proyecto-y-criterio-de-salida"></a>

## Criterio de salida

Reconstruye la entrega de 12.09 en otra carpeta, verifica datos por ID/corte contra una referencia externa, ejecuta pruebas y demuestra filtros, errores, vacío, recuperación y descargas reales. Explica reejecución, estado, caché y límites de las huellas; conserva evidencia y ayudas recibidas. Publicar en Internet no es requisito. El criterio se evalúa en la práctica personal, no por disponer del material.

Consulta el [estado y punto de reanudación](../../docs/streamlit-closure.md) para
retomar la práctica de cierre y distinguir controles de autoría de aprendizaje.

No hay proyecto integrador ni checkpoint de aplicación Streamlit implementado; 12.01 es una práctica introductoria. Sus hitos se definirán como alternativa a la ruta Shiny.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Tramos del material: app mínima (01–02), lógica y estado (03–04), actualización y
casos límite (05–06), presentación verificada (07), pruebas y entrega (08–09).

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

Empieza por [12.01 — Primera app y modelo de ejecución](01_first_app_execution/README.md)
y sigue el orden de [lecciones y labs](#lecciones-y-labs). El último material
disponible es [12.09 — Cierre y entrega local](09_local_delivery/README.md).

Cuando cierres tu práctica, consulta el alcance de [14 — Proyecto reproducible](../14_reproducible_projects/README.md): 14.01–14.08 tienen lecciones/labs disponibles y 14.09 sigue planificada. La otra aplicación queda como comparación opcional; no es requisito completar ambas.

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

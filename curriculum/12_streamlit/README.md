# 12 — Streamlit

## Propósito y prerrequisitos

Crear un explorador de datos en Python con filtros, indicadores y figuras
verificables. Completa [11 — Reportes con Quarto](../11_reporting_quarto/README.md)
y reutiliza funciones y gráficos de los módulos Python.

**Estado:** nueve secciones planificadas; lecciones y labs por desarrollar.
Los enlaces internos describen el alcance previsto.

Esta es la ruta de aplicación Python. [Shiny](../13_shiny_web/README.md) es la
alternativa en R; no necesitas construir ambas. La primera entrega se ejecutará
localmente, con datos sintéticos, sin login ni servicio de alojamiento.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Primera app y modelo de ejecución](#01-primera-app-y-modelo-de-ejecucion) | Esencial | Ejecutar una app y explicar sus reejecuciones |
| 2 | [Entradas, filtros y presentación](#02-entradas-filtros-y-presentacion) | Esencial | Conectar widgets con un subconjunto verificable |
| 3 | [Separar datos e interfaz](#03-separar-datos-e-interfaz) | Esencial | Reutilizar transformaciones fuera de la app |
| 4 | [Estado de sesión y formularios](#04-estado-de-sesion-y-formularios) | Esencial | Conservar elecciones y controlar cuándo aplicarlas |
| 5 | [Caché de datos y recursos](#05-cache-de-datos-y-recursos) | Práctica | Evitar trabajo repetido sin mostrar resultados obsoletos |
| 6 | [Mensajes y casos sin datos](#06-mensajes-y-casos-sin-datos) | Esencial | Explicar entradas inválidas y filtros vacíos |
| 7 | [Tablas, gráficos y descarga](#07-tablas-graficos-y-descarga) | Práctica | Presentar y exportar el mismo universo filtrado |
| 8 | [Pruebas de la aplicación](#08-pruebas-de-la-aplicacion) | Esencial | Comprobar indicadores y comportamiento de widgets |
| 9 | [Cierre y entrega local](#09-cierre-y-entrega-local) | Práctica de cierre | Reconstruir y usar un explorador comprobado |

## Alcance de cada sección

<a id="01-primera-app-y-modelo-de-ejecucion"></a>

### 01 — Primera app y modelo de ejecución

- Navegador, servidor Streamlit y script; arranque con streamlit run.
  Modelo de reejecución ante interacciones y diferencia con ejecutar un script una vez.
- Práctica prevista: una app mínima y observar qué cambia al interactuar. Instalación
  y versión se incorporarán al entorno elegido al implementar esta sección.

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

## Prácticas, proyecto y criterio de salida

Se prevén labs 12.01–12.09; aún no existen. Se reutilizarán los datos y funciones
conocidos. El checkpoint de aplicación Python se definirá al implementar esta ruta,
como alternativa al proyecto Shiny previsto en [proyectos](../../projects/README.md);
no hay una carpeta de proyecto Streamlit implementada ni es necesario crear dos apps.

Hitos propuestos: app mínima (01–02), lógica y estado (03–04), actualización y
casos límite (05–06), presentación verificada (07), pruebas y entrega (08–09).

Para avanzar debes explicar reejecución, estado y caché, y demostrar que los
filtros conservan indicadores verificables. Publicar en Internet no es requisito.
No hace falta dominar HTML/CSS/JavaScript o crear decoradores personalizados.

## Continuidad y referencias

Continúa con [14 — Proyecto reproducible](../14_reproducible_projects/README.md).
Puedes estudiar después [13 — Shiny](../13_shiny_web/README.md) para comparar.

Documentación oficial: [modelo de ejecución](https://docs.streamlit.io/develop/concepts/architecture),
[estado de sesión](https://docs.streamlit.io/develop/concepts/architecture/session-state),
[caché](https://docs.streamlit.io/develop/concepts/architecture/caching) y
[pruebas de apps](https://docs.streamlit.io/develop/concepts/app-testing).
No se instalan dependencias por esta planificación.

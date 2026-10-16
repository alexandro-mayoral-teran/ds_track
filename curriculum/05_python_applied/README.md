# 05 — Python aplicado

## Propósito y prerrequisitos

Convertir el análisis conocido de pandas, SQL y visualización en código
reutilizable, comprobable y reconstruible. Completar primero
[04 — Visualización en Python](../04_visualization_python/README.md), incluido
su [cierre 04.09](../04_visualization_python/09_visual_closure/README.md).
La interacción de 04.08 es opcional. Conserva la entrega reconstruible para
reorganizar ese mismo análisis. Las ocho primeras secciones tienen material disponible; 05.06–05.08 son opcionales.

**Estado:** [05.01 — Del notebook a módulos](01_notebook_to_modules/README.md)
dispone de lección, paquete local, script, notebook y lab;
[05.02 — Configuración y registro de ejecución](02_configuration_logging/README.md)
añade argumentos, JSON y logging;
[05.03 — Errores y gestión de recursos](03_errors_resources/README.md)
añade cierre por etapas y demostraciones de recursos sobre el mismo paquete.
[05.04 — Pruebas de código y datos](04_testing/README.md) añade una colección
unittest, casos conocidos, fronteras, vacíos e integración, con lab.
[05.05 — Tipos y contratos](05_types_contracts/README.md) incorpora anotaciones,
docstrings, validación de conteos, parámetros opcionales y revisión del resumen,
con pruebas y lab.
[05.06 — Clases, composición y dataclasses](06_classes_composition/README.md)
añade objetos pequeños, configuración y revisión por composición, con pruebas
y lab opcionales.
[05.07 — Iteradores y generadores](07_iterators_generators/README.md) incorpora
consumo, yield, CSV por lotes y conciliación con memoria/recursos explícitos,
con pruebas y lab de extensión.
[05.08 — Funciones como valores y decoradores](08_functions_decorators/README.md)
añade funciones como argumentos/retorno, envolturas, wraps y registro del análisis,
con pruebas y lab de extensión. Las secciones 09–11
siguen planificadas; sus enlaces internos describen el alcance pendiente.
La disponibilidad del material no acredita aprendizaje del estudiante.

El núcleo es organización, configuración, errores y pruebas. Clases, generadores,
decoradores, rendimiento y APIs amplían esa base; no son requisitos para poder
limpiar datos ni para iniciar pandas. El mismo análisis permite evaluar si una
abstracción aporta claridad en lugar de introducirla por costumbre.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Del notebook a módulos](01_notebook_to_modules/README.md) | Esencial | Importar y reutilizar transformaciones |
| 2 | [Configuración y registro de ejecución](02_configuration_logging/README.md) | Esencial | Ejecutar con entradas y parámetros explícitos |
| 3 | [Errores y gestión de recursos](03_errors_resources/README.md) | Esencial | Comunicar fallas sin dejar resultados engañosos |
| 4 | [Pruebas de código y datos](04_testing/README.md) | Esencial | Detectar regresiones con casos significativos |
| 5 | [Tipos y contratos de funciones](05_types_contracts/README.md) | Práctica | Hacer explícitas entradas y salidas |
| 6 | [Clases, composición y dataclasses](06_classes_composition/README.md) | Práctica opcional | Representar estructuras cuando resulte útil |
| 7 | [Iteradores y generadores](07_iterators_generators/README.md) | Extensión | Procesar lotes sin reunir toda la entrada |
| 8 | [Funciones como valores y decoradores](08_functions_decorators/README.md) | Extensión | Reutilizar un comportamiento transversal |
| 9 | [Medir antes de optimizar](#09-medir-antes-de-optimizar) | Extensión | Localizar un costo y comprobar una mejora |
| 10 | [Integración con APIs](#10-integracion-con-apis) | Extensión | Obtener datos externos con controles explícitos |
| 11 | [Cierre del proyecto Python](#11-cierre-del-proyecto-python) | Práctica de cierre | Reconstruir indicadores y figura con una ejecución |

## Alcance de cada sección

<a id="01-del-notebook-a-modulos"></a>

### 01 — Del notebook a módulos

- Separar exploración, transformación y presentación; importaciones, módulos,
  paquetes básicos, main y punto de entrada sin efectos al importar.
- [Lección disponible](01_notebook_to_modules/README.md) y
  [lab 05.01](../../labs/05_python_applied/01_notebook_to_modules/README.md):
  módulo pequeño, paquete del análisis de 04.09 y reutilización desde script
  y notebook, conservando resultados sin agregar rutas manuales a sys.path.

<a id="02-configuracion-y-registro-de-ejecucion"></a>

### 02 — Configuración y registro de ejecución

- Rutas, parámetros de corte, configuración y argumentos con argparse.
  Separar valores configurables de la lógica y conservar versiones de dependencias.
- logging frente a print, niveles y contexto de ejecución.
- [Lección disponible](02_configuration_logging/README.md) y
  [lab 05.02](../../labs/05_python_applied/02_configuration_logging/README.md):
  ejecutar dos cortes, comprobar precedencia y rutas, y explicar qué entrada,
  reglas y salida se utilizaron mediante el registro efectivo.

<a id="03-errores-y-gestion-de-recursos"></a>

### 03 — Errores y gestión de recursos

- Excepciones específicas, propagación y mensajes útiles; archivos y conexiones
  cerrados explícitamente. Reutilizar with antes de diseñar gestores propios.
- [Lección disponible](03_errors_resources/README.md) y
  [lab 05.03](../../labs/05_python_applied/03_errors_resources/README.md):
  simular fallas sin anunciar cierre ni confundir salidas previas, comprobar
  recursos y conservación de un JSON anterior. Escritura atómica de un archivo
  y sus límites; excepciones propias y gestores personalizados como ampliación.

<a id="04-pruebas-de-codigo-y-datos"></a>

### 04 — Pruebas de código y datos

- Casos conocidos, fronteras, colecciones vacías, fallas esperadas y conservación
  de entradas; pruebas de una función frente a integración del recorrido.
- Empezar con unittest de la biblioteca estándar; fixtures pequeñas y directorios
  temporales. [Lección disponible](04_testing/README.md) y
  [lab 05.04](../../labs/05_python_applied/04_testing/README.md): interpretar una
  falla, comprobar conservación y agregar un caso que distinga mediana de promedio.
  La validación de entradas no debe depender exclusivamente de assert.

<a id="05-tipos-y-contratos-de-funciones"></a>

### 05 — Tipos y contratos de funciones

- Anotaciones, docstrings, argumentos opcionales y estructuras esperadas.
  Las anotaciones por sí solas no validan datos durante la ejecución.
- [Lección disponible](05_types_contracts/README.md) y
  [lab 05.05](../../labs/05_python_applied/05_types_contracts/README.md): leer
  firmas, documentar estructuras y unidades, distinguir None/cero/vacío y
  comprobar límites de contratos sobre el paquete. Análisis estático opcional,
  sin nuevas dependencias ni promesa de validación por las anotaciones.

<a id="06-clases-composicion-y-dataclasses"></a>

### 06 — Clases, composición y dataclasses

- Instancias, atributos, métodos y responsabilidades; comparar una función,
  un diccionario y una clase. dataclass para registros o configuración.
- [Lección disponible](06_classes_composition/README.md) y
  [lab 05.06](../../labs/05_python_applied/06_classes_composition/README.md),
  opcionales: comparar representaciones, estado/alias y composición de fuente
  y opciones; dataclasses con validación, frozen y replace. No envolver cada
  DataFrame en una clase ni duplicar el cálculo de las funciones.

<a id="07-iteradores-y-generadores"></a>

### 07 — Iteradores y generadores

- Iterables, iteradores, consumo, yield y procesamiento por lotes.
- [Lección disponible](07_iterators_generators/README.md) y
  [lab 05.07](../../labs/05_python_applied/07_iterators_generators/README.md),
  de extensión: consumo único, último lote, errores diferidos y recursos; CSV
  por lotes con claves/valores conservados y conciliación de indicadores.
  Catálogo, claves y saldos para mediana siguen en memoria; no se promete
  memoria constante ni se promedian medianas de lotes.

<a id="08-funciones-como-valores-y-decoradores"></a>

### 08 — Funciones como valores y decoradores

- Pasar una función, envolver un comportamiento y conservar metadatos con wraps.
  Diferenciar utilizar un decorador existente de desarrollar uno propio.
- [Lección disponible](08_functions_decorators/README.md) y
  [lab 05.08](../../labs/05_python_applied/08_functions_decorators/README.md),
  de extensión: funciones como valores, cierre, reenvío, @ y wraps; registro
  de llamadas con resultado/error preservados y límites frente a generadores.
  Caché, reintentos y decoradores complejos requieren otra necesidad/contrato.

<a id="09-medir-antes-de-optimizar"></a>

### 09 — Medir antes de optimizar

- Tiempo, memoria, mediciones repetidas y profiling; identificar el cuello de
  botella. Complejidad básica con tamaños y casos comparables.
- Práctica prevista: comparar dos implementaciones conservando resultados y
  explicar el costo en claridad. La optimización no sustituye la validación.

<a id="10-integracion-con-apis"></a>

### 10 — Integración con APIs

- HTTP, respuesta JSON, códigos de estado, paginación, tiempos de espera y
  reintentos limitados cuando sean adecuados; configuración fuera del código.
- Práctica prevista: procesar respuestas locales simuladas, incluidos errores,
  sin exigir credenciales ni un servicio activo. Una consulta real será opcional;
  normalizar y validar datos antes de incorporarlos al análisis.

<a id="11-cierre-del-proyecto-python"></a>

### 11 — Cierre del proyecto Python

- Reconstruir el análisis de pandas/SQL y su figura con instrucciones explícitas,
  salidas regenerables y comprobaciones automatizadas.
- Práctica prevista: ejecutar desde un estado limpio y conciliar con la versión
  anterior, documentando decisiones y límites del producto.

## Recorrido esencial y profundización

Para el cierre esencial, realiza 01–04, aplica los contratos de 05 y pasa a 11.
Las secciones 06–10 pueden estudiarse en orden cuando se quiera profundizar;
no bloquean el paso a R. Herencia avanzada, concurrencia, asincronía y
metaprogramación quedan estacionadas hasta que exista una necesidad verificable.

Los labs 05.01–05.08 están disponibles (05.06–05.08 opcionales); los labs 05.09–05.11 siguen previstos,
señalando los opcionales cuando se desarrollen.
Se reutilizarán los proyectos previstos 01_clean_credit_data y 02_credit_database,
registrados en [proyectos](../../projects/README.md); no se exige crear otro.
Checkpoint de organización propuesto: ejecución reconstruible, controles,
configuración e instrucciones, conservando indicadores y figura. Se concretará
al implementar los proyectos.

Podrás cerrar el módulo cuando otra persona ejecute el análisis con las mismas
entradas y reconstruya el resultado, y cuando puedas demostrar que las pruebas
encuentran una falla relevante. No se exige aplicar todas las abstracciones.

## Continuidad y referencias

Después del cierre esencial, continúa con
[06 — R fundamental](../06_r_foundations/README.md) sobre un problema ya conocido.

El diseño se apoya en [módulos de Python](https://docs.python.org/3/tutorial/modules.html),
[logging](https://docs.python.org/3/howto/logging.html),
[unittest](https://docs.python.org/3/library/unittest.html) y
[dataclasses](https://docs.python.org/3/library/dataclasses.html).
Para las ampliaciones se consultarán las referencias específicas al implementar
cada ejemplo y se registrarán las dependencias que realmente se utilicen.

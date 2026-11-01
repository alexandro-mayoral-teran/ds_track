# 05 — Python aplicado

[Inicio](../../README.md) / [Módulos](../README.md) / **05 — Python aplicado**

**Organiza un análisis para que pueda ejecutarse, comprobarse y retomarse.**

[**Empezar por 05.01 →**](01_notebook_to_modules/README.md) · [Lecciones y labs](#lecciones-y-labs) · [Criterio de salida](#criterio-de-salida)

> **Material disponible:** 11 lecciones y sus labs. Esto no acredita aprendizaje ni proyecto completado.

<a id="propósito-y-prerrequisitos"></a>

## Propósito

Convertir el análisis conocido de pandas, SQL y visualización en código reutilizable, comprobable y reconstruible, conservando sus indicadores y figura.

## Antes de empezar

Retoma los conceptos de [04 — Visualización en Python](../04_visualization_python/README.md),
incluido [04.09](../04_visualization_python/09_visual_closure/README.md); 04.08 es opcional.
El paquete utiliza los CSV sintéticos incluidos en SQL 03.01 y puede producir
una entrega nueva sin archivos personales de capítulos anteriores. Si conservas
tu entrega de 04.09, úsala para comparar el mismo análisis sobre iguales fuentes
y fecha. Necesitas el entorno de pandas/visualización ya preparado.

## Qué vas a aprender

- Separar cálculo reutilizable, entrada y ejecución.
- Usar configuración, logging y gestión de errores.
- Comprobar contratos con pruebas relevantes.
- Reconstruir una entrega y justificar las abstracciones elegidas.

<a id="orden-de-desarrollo"></a>

## Lecciones y labs

| Lección | Práctica | Resultado que comprobarás |
| --- | --- | --- |
| **05.01** · [Del notebook a módulos](01_notebook_to_modules/README.md) | [Lab 05.01](../../labs/05_python_applied/01_notebook_to_modules/README.md) | Importar y reutilizar transformaciones |
| **05.02** · [Configuración y registro de ejecución](02_configuration_logging/README.md) | [Lab 05.02](../../labs/05_python_applied/02_configuration_logging/README.md) | Ejecutar con entradas y parámetros explícitos |
| **05.03** · [Errores y gestión de recursos](03_errors_resources/README.md) | [Lab 05.03](../../labs/05_python_applied/03_errors_resources/README.md) | Comunicar fallas sin dejar resultados engañosos |
| **05.04** · [Pruebas de código y datos](04_testing/README.md) | [Lab 05.04](../../labs/05_python_applied/04_testing/README.md) | Detectar regresiones con casos significativos |
| **05.05** · [Tipos y contratos de funciones](05_types_contracts/README.md) | [Lab 05.05](../../labs/05_python_applied/05_types_contracts/README.md) | Hacer explícitas entradas y salidas |
| **05.06** · [Clases, composición y dataclasses](06_classes_composition/README.md) — opcional | [Lab 05.06](../../labs/05_python_applied/06_classes_composition/README.md) | Representar estructuras cuando resulte útil |
| **05.07** · [Iteradores y generadores](07_iterators_generators/README.md) — opcional | [Lab 05.07](../../labs/05_python_applied/07_iterators_generators/README.md) | Procesar lotes sin reunir toda la entrada |
| **05.08** · [Funciones como valores y decoradores](08_functions_decorators/README.md) — opcional | [Lab 05.08](../../labs/05_python_applied/08_functions_decorators/README.md) | Reutilizar un comportamiento transversal |
| **05.09** · [Medir antes de optimizar](09_measure_optimize/README.md) — opcional | [Lab 05.09](../../labs/05_python_applied/09_measure_optimize/README.md) | Localizar un costo y comprobar una mejora |
| **05.10** · [Integración con APIs](10_api_integration/README.md) — opcional | [Lab 05.10](../../labs/05_python_applied/10_api_integration/README.md) | Obtener datos externos con controles explícitos |
| **05.11** · [Cierre del proyecto Python](11_project_closure/README.md) | [Lab 05.11](../../labs/05_python_applied/11_project_closure/README.md) | Reconstruir indicadores y figura con una ejecución |

<a id="alcance-de-cada-sección"></a>

<a id="alcance-de-las-secciones"></a>

<details>
<summary><strong>Ver el alcance de las secciones</strong></summary>

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

- Tiempo, memoria trazada, mediciones repetidas y perfiles; definir fronteras
  y localizar trabajo antes de cambiarlo. Tamaño/diversidad y complejidad básica.
- [Lección disponible](09_measure_optimize/README.md) y
  [lab 05.09](../../labs/05_python_applied/09_measure_optimize/README.md),
  de extensión: comparar validación de fechas por aparición/reutilización local,
  conservando conteos, errores y consumo. Instrumentos separados, evidencia
  cruda, costo de memoria y decisión sin prometer velocidad universal.

<a id="10-integracion-con-apis"></a>

### 10 — Integración con APIs

- HTTP, respuesta JSON, códigos de estado, paginación, tiempos de espera y
  reintentos limitados cuando sean adecuados; configuración fuera del código.
- [Lección disponible](10_api_integration/README.md) y
  [lab 05.10](../../labs/05_python_applied/10_api_integration/README.md),
  de extensión: procesar tres páginas locales, incluidos errores tardíos y
  reintentos acotados, sin credenciales ni servicio activo. Normalizar, validar
  y conciliar con las fuentes anteriores; adaptador HTTPS probado sin red.

<a id="11-cierre-del-proyecto-python"></a>

### 11 — Cierre del proyecto Python

- Reconstruir el análisis de pandas/SQL y su figura con instrucciones explícitas,
  salidas regenerables y comprobaciones automatizadas.
- [Lección disponible](11_project_closure/README.md) y
  [lab 05.11](../../labs/05_python_applied/11_project_closure/README.md): ejecutar,
  verificar cinco tablas/20 controles, reconstruir desde fuentes copiadas y
  demostrar una falla. Revisión visual y comparación con el recorrido anterior;
  no se exigen APIs reales ni todas las ampliaciones opcionales.

</details>

<a id="recorrido-esencial-y-profundización"></a>

## Cómo trabajar este módulo

Para el recorrido esencial realiza 05.01–05.04, aplica los contratos de 05.05 y pasa al cierre 05.11. Las secciones 05.06–05.10 son ampliaciones opcionales. No hace falta usar todas las abstracciones ni estudiar herencia avanzada, asincronía o metaprogramación para continuar a R.

Lee, predice, practica en tu copia, comprueba y explica. En pareja, una persona escribe y la otra contrasta; cambien de papeles por bloques. Conserva los originales y vuelve a ejecutar desde una sesión nueva antes del cierre.

## Qué conservar

| Evidencia personal | Qué permite revisar |
| --- | --- |
| Paquete, scripts y configuración | Responsabilidades y ejecución explícitas |
| Pruebas y casos de frontera | Fallos relevantes detectados, no solo ejecución exitosa |
| Entrega e instrucciones | Resultado y figura reconstruidos con las mismas entradas |

Guarda los archivos y una nota con predicción, comprobación, ayudas, dudas y siguiente paso en tu copia personal. PROGRESS.md registra el desarrollo del material; no es un porcentaje de aprendizaje.

## Criterio de salida

Otra persona puede ejecutar el análisis con las mismas entradas y reconstruir su resultado. Demuestra que los controles detectan una falla relevante y explica qué organización elegiste y por qué.

Se reutilizarán los proyectos previstos de limpieza y base de datos; el checkpoint de organización se concretará al implementarlos. No hay checkpoint activo para acreditar aquí.

<details>
<summary><strong>Notas de integración y alcance del cierre</strong></summary>

Los labs 05.01–05.11 están disponibles (05.06–05.10 opcionales).
Se reutilizarán los proyectos previstos 01_clean_credit_data y 02_credit_database,
registrados en [proyectos](../../projects/README.md); no se exige crear otro.
Checkpoint de organización propuesto: ejecución reconstruible, controles,
configuración e instrucciones, conservando indicadores y figura. Se concretará
al implementar los proyectos.

</details>

<a id="continuidad-y-referencias"></a>

## Siguiente paso

**Para empezar:** [lee 05.01](01_notebook_to_modules/README.md) y realiza su lab.

**Al cerrar:** continúa con [06 — R fundamental](../06_r_foundations/README.md).

<details>
<summary><strong>Referencias y apoyos</strong></summary>

El diseño se apoya en [módulos de Python](https://docs.python.org/3/tutorial/modules.html),
[logging](https://docs.python.org/3/howto/logging.html),
[unittest](https://docs.python.org/3/library/unittest.html) y
[dataclasses](https://docs.python.org/3/library/dataclasses.html).
Cada ampliación enlaza sus referencias específicas e indica los requisitos
que utiliza. No se instalan paquetes por consultar una ampliación opcional.

</details>

---

[← Inicio](../../README.md) · [Todos los módulos](../README.md) · [Primera lección →](01_notebook_to_modules/README.md)

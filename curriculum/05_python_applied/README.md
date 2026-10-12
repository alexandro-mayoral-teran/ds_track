# 05 — Python aplicado

## Propósito y prerrequisitos

Convertir el análisis conocido de pandas, SQL y visualización en código
reutilizable, comprobable y reconstruible. Completar primero
[04 — Visualización en Python](../04_visualization_python/README.md).

**Estado:** secciones planificadas; lecciones y labs por desarrollar. Los enlaces
internos describen su alcance. No se agregarán paquetes ni infraestructura hasta
que se implemente una necesidad concreta.

El núcleo es organización, configuración, errores y pruebas. Clases, generadores,
decoradores, rendimiento y APIs amplían esa base; no son requisitos para poder
limpiar datos ni para iniciar pandas. El mismo análisis permite evaluar si una
abstracción aporta claridad en lugar de introducirla por costumbre.

## Orden de desarrollo

| Orden | Sección prevista | Alcance | Resultado observable |
| --- | --- | --- | --- |
| 1 | [Del notebook a módulos](#01-del-notebook-a-modulos) | Esencial | Importar y reutilizar transformaciones |
| 2 | [Configuración y registro de ejecución](#02-configuracion-y-registro-de-ejecucion) | Esencial | Ejecutar con entradas y parámetros explícitos |
| 3 | [Errores y gestión de recursos](#03-errores-y-gestion-de-recursos) | Esencial | Comunicar fallas sin dejar resultados engañosos |
| 4 | [Pruebas de código y datos](#04-pruebas-de-codigo-y-datos) | Esencial | Detectar regresiones con casos significativos |
| 5 | [Tipos y contratos de funciones](#05-tipos-y-contratos-de-funciones) | Práctica | Hacer explícitas entradas y salidas |
| 6 | [Clases, composición y dataclasses](#06-clases-composicion-y-dataclasses) | Práctica opcional | Representar estructuras cuando resulte útil |
| 7 | [Iteradores y generadores](#07-iteradores-y-generadores) | Extensión | Procesar lotes sin reunir toda la entrada |
| 8 | [Funciones como valores y decoradores](#08-funciones-como-valores-y-decoradores) | Extensión | Reutilizar un comportamiento transversal |
| 9 | [Medir antes de optimizar](#09-medir-antes-de-optimizar) | Extensión | Localizar un costo y comprobar una mejora |
| 10 | [Integración con APIs](#10-integracion-con-apis) | Extensión | Obtener datos externos con controles explícitos |
| 11 | [Cierre del proyecto Python](#11-cierre-del-proyecto-python) | Práctica de cierre | Reconstruir indicadores y figura con una ejecución |

## Alcance de cada sección

<a id="01-del-notebook-a-modulos"></a>

### 01 — Del notebook a módulos

- Separar exploración, transformación y presentación; importaciones, módulos,
  paquetes básicos, main y punto de entrada sin efectos al importar.
- Práctica prevista: extraer funciones del análisis y reutilizarlas desde script
  y notebook, conservando resultados y sin agregar rutas manuales a sys.path.

<a id="02-configuracion-y-registro-de-ejecucion"></a>

### 02 — Configuración y registro de ejecución

- Rutas, parámetros de corte, configuración y argumentos con argparse.
  Separar valores configurables de la lógica y conservar versiones de dependencias.
- logging frente a print, niveles y contexto de ejecución. Práctica prevista:
  ejecutar dos cortes y explicar qué entrada, reglas y salida se utilizaron.

<a id="03-errores-y-gestion-de-recursos"></a>

### 03 — Errores y gestión de recursos

- Excepciones específicas, propagación y mensajes útiles; archivos y conexiones
  cerrados explícitamente. Reutilizar with antes de diseñar gestores propios.
- Práctica prevista: simular una falla y comprobar que no se anuncia éxito ni se
  confunden salidas anteriores con nuevas. Escritura atómica de un archivo y sus
  límites; excepciones propias y gestores personalizados como ampliación.

<a id="04-pruebas-de-codigo-y-datos"></a>

### 04 — Pruebas de código y datos

- Casos conocidos, fronteras, colecciones vacías, fallas esperadas y conservación
  de entradas; pruebas de una función frente a integración del recorrido.
- Empezar con unittest de la biblioteca estándar; fixtures pequeñas y directorios
  temporales. Práctica prevista: detectar un cambio que altera un total o una unión.
  La validación de entradas no debe depender exclusivamente de assert.

<a id="05-tipos-y-contratos-de-funciones"></a>

### 05 — Tipos y contratos de funciones

- Anotaciones, docstrings, argumentos opcionales y estructuras esperadas.
  Las anotaciones por sí solas no validan datos durante la ejecución.
- Práctica prevista: documentar transformaciones conocidas y diferenciar
  comprobaciones de datos de análisis estático opcional.

<a id="06-clases-composicion-y-dataclasses"></a>

### 06 — Clases, composición y dataclasses

- Instancias, atributos, métodos y responsabilidades; comparar una función,
  un diccionario y una clase. dataclass para registros o configuración.
- Práctica prevista: representar una configuración y justificar si mejora la
  claridad. Composición antes de jerarquías; no envolver cada DataFrame en una clase.

<a id="07-iteradores-y-generadores"></a>

### 07 — Iteradores y generadores

- Iterables, iteradores, consumo, yield y procesamiento por lotes.
- Práctica prevista: resumir una entrada por lotes, conciliar con el resultado
  completo y explicar qué sigue ocupando memoria. No prometer memoria constante
  si se retienen todos los resultados o grupos.

<a id="08-funciones-como-valores-y-decoradores"></a>

### 08 — Funciones como valores y decoradores

- Pasar una función, envolver un comportamiento y conservar metadatos con wraps.
  Diferenciar utilizar un decorador existente de desarrollar uno propio.
- Práctica prevista: instrumentar una función sin alterar su retorno ni ocultar
  excepciones. Caché y decoradores complejos se introducen solo con una necesidad.

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

Se prevén labs 05.01–05.11, señalando los opcionales. Aún no existen.
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

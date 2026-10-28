# 13.09 — Pruebas y observación del flujo

[Inicio](../../../README.md) / [Módulo 13](../README.md) / **Lección 13.09**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Detectar resultados incorrectos o desactualizados con casos reproducibles |
| **Necesitas** | R, tu IDE y los conceptos de funciones, reactividad, eventos y módulos |
| **Evidencia** | Predicciones, pruebas que pasan, un fallo provocado y explicado, revisión en navegador |

[Empezar](#antes-de-empezar) · [Ir al lab](../../../labs/13_shiny_web/09_tests_flow/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Una app puede abrir sin errores y mostrar una cifra antigua. También puede
sumar correctamente después de excluir el crédito equivocado. Necesitamos
comprobar qué sucede antes y después de una acción, con resultados esperados
que podamos justificar fuera del código que estamos probando.

Una **prueba** fija entradas, realiza una acción y compara una observación con
una expectativa. Una **regresión** ocurre cuando un cambio rompe un comportamiento
que antes funcionaba. Observar mensajes ayuda a localizar la causa; una prueba
repetible ayuda a impedir que el error vuelva.

## Antes de empezar

- Revisa [13.03 — Reactividad](../03_reactivity/README.md),
  [13.05 — Eventos](../05_events_session/README.md),
  [13.06 — Validación](../06_validation_messages/README.md) y
  [13.08 — Módulos](../08_organization_modules/README.md).
- Prepara una carpeta nueva siguiendo [recorridos.md](recorridos.md). No se
  requieren entregas anteriores. La app y el módulo de 13.08 se copian intactos.
- Usamos R base y `shiny::testServer()`, incluido en Shiny: no hace falta
  añadir testthat ni un paquete de automatización de navegador. Conservamos
  DESCRIPTION/lockfile de 13.07, con 42 registros y ggplot2 4.0.3.

## Qué vas a aprender

- Escribir una expectativa independiente y leer el primer fallo útil.
- Probar funciones, después transiciones del servidor y finalmente la interfaz.
- Distinguir una edición pendiente de una consulta aplicada desactualizada.
- Observar ejecución por demanda sin imponer un orden global de mensajes.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [preparar_app.R](preparar_app.R), [recorridos.md](recorridos.md) | Copia independiente de veinte archivos y entorno local | Necesario; elige IDE o terminal |
| [minimo.R](minimo.R) | Número/doble y nota independiente, con mensaje de cálculo | Primera actividad |
| [pruebas_minimo.R](pruebas_minimo.R) | Detectar salida que dejó de actualizarse | Primera prueba reactiva |
| [pruebas_funciones.R](pruebas_funciones.R) | Fuente, fronteras, valores por crédito, CSV y capas de gráfica | Pruebas sin sesión Shiny |
| [pruebas_servidor.R](pruebas_servidor.R) | Transiciones, recuperación, dos instancias y API | Pruebas con sesión simulada |
| [ejecutar_pruebas.R](ejecutar_pruebas.R) | Ejecutar el conjunto esencial y detenerse ante un fallo | Ejecutar desde la copia |
| [App](../08_organization_modules/app.R), [módulo](../08_organization_modules/consulta_module.R) | Interfaz comprobada, conservada de 13.08 | Se copian automáticamente |
| [Funciones](../04_shared_filters/cartera.R), [consulta](../05_events_session/consulta.R), [validación](../06_validation_messages/validacion.R), [presentación](../07_outputs_downloads/presentacion.R) | Separar cálculo, estado y representación | Se copian sin modificar |
| [CSV](../../12_streamlit/03_data_interface/cartera.csv), [lockfile](../07_outputs_downloads/renv.lock) | Datos y entorno reconstruibles | Sin dependencias nuevas |

## 1. Empezar con una predicción pequeña

El mínimo tiene un número entero de 0 a 10 y una nota independiente. Al cambiar
el número, su doble debe actualizarse inmediatamente: **3 → 6**, **7 → 14**,
**0 → 0**. Editar la nota solo cambia su eco. Aquí no hay botón Aplicar ni
instantánea guardada; esa diferencia con la app de cartera será importante.

En la copia preparada, abre minimo.R y ejecútalo desde la consola R:

```r
source("iniciar.R")
iniciar_app("minimo.R")
```

Observa la página y la consola. Al demandar un resultado nuevo, la expresión
doble emite un mensaje como `[doble] calcular numero=7`. Editar la nota no
debería volver a calcular ese doble. Leer un valor ya calculado puede utilizar
su caché hasta que cambie una dependencia. No cuentes mensajes de arranque ni
supongas un orden exacto entre salidas; tampoco son mediciones de rendimiento.

Detén el servidor con Stop/Esc antes de continuar. Las pruebas siguientes se
ejecutan en R sin ocupar un puerto HTTP ni abrir una página.

## 2. Una expectativa que puede fallar

Este ejemplo autónomo solo necesita R:

```r
doblar <- function(x) x * 2
stopifnot("Tres debe dar seis" = identical(doblar(3), 6))
```

`stopifnot()` detiene la ejecución si una condición no es TRUE; el nombre
explica qué esperábamos. `identical()` compara valores, tipos y atributos:
`identical(3L, 3)` es FALSE porque distingue entero y double. Usaremos esa
precisión deliberadamente en IDs textuales, saldos y estados conocidos.

Para un porcentaje calculado usamos
`isTRUE(all.equal(obtenido, esperado))`: all.equal puede devolver un texto
explicando diferencias, por eso no basta usarla directamente como condición.
Su tolerancia sirve para representación numérica; no justifica aceptar IDs,
unidades o denominadores diferentes.

Una expectativa se llama también **oráculo de prueba**. Si esperas
`sum(seleccion$saldo_mxn)` y la selección ya está mal, puedes aceptar el mismo
error dos veces. Primero escribe qué créditos deberían aparecer y sus importes.

## 3. testServer: entradas y resultados sin navegador

Shiny ofrece una sesión simulada que permite fijar entradas e inspeccionar
objetos del servidor o de un módulo. Carga Shiny y el mínimo en un entorno
propio para no reemplazar el server de otra app:

```r
library(shiny)
entorno <- new.env(parent = globalenv())
source("minimo.R", local = entorno)
testServer(entorno$dobleServer, {
  session$setInputs(numero = 3, nota = "inicio")
  stopifnot(identical(doble(), 6))
  stopifnot(identical(output$resultado, "Doble: 6."))
  session$setInputs(numero = 7)
  stopifnot(identical(doble(), 14))
  stopifnot(identical(output$resultado, "Doble: 14."))
})
```

Dentro del bloque puedes leer doble, definido dentro del módulo: testServer
expone ese entorno para la prueba; no es una variable global de la aplicación.
Al probar directamente un módulo, usa nombres locales (`numero`); al probar
la app padre, las entradas llevan el namespace (`izquierda-corte`).

Un parámetro ordinario del módulo se pasa con args: las pruebas de cartera
usan `testServer(consultaServer, args = list(ruta = ruta), { ... })` para apuntar
a su CSV temporal propio. Para la integración se carga app.R en un entorno
local y se pasa el objeto app a testServer; no se inicia un servidor HTTP.

`session$setInputs()` ya procesa una ronda de trabajo reactivo al terminar.
No necesita sleep. `session$flushReact()` permite procesar trabajo pendiente
en situaciones más específicas; no corrige una dependencia ausente. Leer
`doble()` u `output$resultado` permite demandar/comprobar esos resultados.

La sesión simulada **no monta la UI**. Debes establecer las entradas necesarias;
no obtiene por sí sola los valores iniciales declarados en numericInput o
selectInput. Un botón de acción empieza sin pulsar; las pruebas representan
su cero inicial con `structure(0L, class = "shinyActionButtonValue")`, dejan
inicializar el servidor y después envían 1L, 2L… como pulsaciones separadas.
Enviar el primer clic junto con la primera inicialización puede ocultarlo
cuando el observador usa ignoreInit.

## 4. El fallo: cálculo correcto, texto antiguo

En una copia de trabajo del mínimo, el lab propone aislar la lectura dentro
de renderText:

```r
output$resultado <- renderText({ paste0("Doble: ", isolate(doble()), ".") })
```

Esta salida lee el doble sin registrar la dependencia. La prueba puede encontrar
doble igual a 14 y, a la vez, texto igual a `Doble: 6.`. El fallo **Texto actualizado**
localiza la desconexión entre cálculo y salida. Quita ese isolate de la salida
y repite desde una sesión nueva.

isolate tiene usos válidos, como lecturas que no deben activar un observador.
La regla aquí depende del comportamiento deseado: una salida que debe cambiar
con doble necesita esa dependencia. En la cartera, conservar una consulta
después de editar un borrador es intencional hasta pulsar Aplicar.

## 5. Casos conocidos de la cartera

Cada fila es un crédito en una fecha, con saldo en pesos enteros:

| Crédito | Segmento | Septiembre 2026-09-30 | Octubre 2026-10-31 |
| --- | --- | ---: | ---: |
| 001 | comercio | 0 | 100 |
| 002 | servicios | 2000 | 1900 |
| 003 | comercio | 2500 | 2600 |

Son seis observaciones, clave ID/corte. La fuente completa se valida antes de
filtrar. El universo de cada corte tiene tres créditos, con 4500 y 4600 MXN.
Se selecciona por segmentos y `saldo_mxn >= minimo_mxn`. No elegir segmentos
selecciona cero filas; 0 conocido no equivale a ausencia.

| Corte / segmentos / mínimo | IDs esperados | Saldo seleccionado | Cobertura |
| --- | --- | ---: | ---: |
| Septiembre / ambos / 2000 | 002, 003 | 4500 | 2/3 |
| Octubre / ambos / 2000 | 003 | 2600 | 1/3 |
| Septiembre / comercio / 0 | 001, 003 | 2500 | 2/3 |
| Septiembre / comercio / 1 | 003 | 2500 | 1/3 |
| Octubre / servicios / 1900 | 002 | 1900 | 1/3 |
| Octubre / servicios / 1901 | Ninguno | 0 | 0/3 |
| Septiembre / ninguno / 0 | Ninguno | 0 | 0/3 |

Estas siete consultas comprueban la frontera inclusiva, el cero y el vacío.
Noviembre no tiene universo: porcentaje ausente y sin exportación. No se
convierte en 0%. Dos saldos erróneos pueden sumar el total correcto; por eso
las pruebas comparan primero valores por crédito, además de suma y cobertura.

## 6. Separar las capas de comprobación

| Capa | Qué hace el material | Qué debes complementar |
| --- | --- | --- |
| Funciones R | Fuente literal, siete consultas, tipos/IDs, rechazos; relectura de 14 CSV temporales y alturas/etiquetas de capas ggplot | Interpretación de reglas y unidades |
| Servidor | Inicio, borrador, aplicación, rechazo, bloqueo/recuperación; dos instancias y lectura del padre | Valores iniciales, acciones reales de usuario |
| UI estática | IDs presentes y únicos; HTML de botones dinámicos con namespace | Conexión del botón en una página real |
| Navegador | Lista manual del lab | Descarga HTTP real, dibujo, foco, recarga y sesión nueva |

Los 14 CSV de la prueba son escritos por las funciones de exportación en
archivos temporales, después releídos y eliminados; **no son descargas HTTP**.
ggplot_build comprueba datos de capas; no sustituye mirar la gráfica renderizada.
Inspeccionar HTML tampoco demuestra que un control esté conectado en navegador.

Ejecuta desde la copia preparada:

```r
source("ejecutar_pruebas.R")
```

El ejecutor carga funciones y corre mínimo → funciones → servidor. Un fallo
detiene el conjunto: corrige su causa y repite completo; ver un OK de un archivo
anterior no significa que el conjunto terminó. En una ejecución correcta verás
`OK conjunto esencial. Falta complementar con la lista de navegador del lab.`
Los diagnósticos `[fuente]` por duplicado/ausencia son provocados por las pruebas,
que usan un CSV temporal y lo limpian; la cartera de la copia permanece intacta.

Las pruebas de servidor comprueban que editar octubre mantiene septiembre
hasta Aplicar, y que entonces pasa a 2600. Un rechazo de entrada conserva la
consulta; una fuente inválida la retira. Añadir un duplicado de octubre debe
bloquear incluso la solicitud de septiembre: el contrato abarca toda la fuente.

## 7. Observar para explicar, no para adivinar

Al depurar: reproduce una sola acción, escribe qué debería invalidarse,
observa su resultado y compara con la expectativa. El mínimo distingue
número → doble → resultado de nota → eco; la cartera distingue borrador de
aplicada. No deduzcas de la cantidad de mensajes una garantía de orden,
memoria o velocidad. Un mensaje confirma que se pasó por ese punto; no
demuestra por sí solo que la salida sea correcta.

**Ampliación opcional:** reactlog ofrece un visor del grafo. No se añade al
lockfile de esta práctica ni bloquea avanzar. La referencia oficial actual
utiliza el paquete reactlog; comprueba su disponibilidad antes de intentar
`reactlog::reactlog_enable()`. No lo instales en bibliotecas globales para
seguir este esencial. Si exploras en otro proyecto local preparado, activa
el registro en una sesión nueva, ejecuta pocas acciones y usa
`shiny::reactlogShow()`; cierra esa sesión después. El registro puede reunir
actividad de varias sesiones del proceso, crecer y mostrar código: úsalo
solo en desarrollo local. Aquí comprobamos trazas de consola y pruebas,
no acreditamos un recorrido del visor interactivo.

## Práctica

Continúa con el [lab 13.09](../../../labs/13_shiny_web/09_tests_flow/README.md):
predice, ejecuta, provoca el texto desactualizado, corrige y revisa la app real.

## Evidencia y criterio de salida

Conserva una nota personal con entradas y expectativas, primer fallo obtenido,
causa/corrección y resultado completo posterior. Añade evidencia del navegador
que distinga aplicada/borrador, cero/vacío, rechazo y una nueva sesión.
Explica qué cubre cada capa y qué queda fuera. Pasar pruebas no demuestra
ausencia de todos los errores ni acredita automáticamente aprendizaje.

## Siguiente paso

Después del lab continúa con [13.10 — Cierre y entrega local](../10_local_delivery/README.md),
disponible con lección y lab. Proyecto/checkpoints y práctica personal siguen pendientes.

## Referencias primarias

Ejemplos propios; APIs contrastadas para Shiny 1.14.0. Referencias de apoyo:

- [Posit: testServer](https://shiny.posit.co/r/reference/shiny/latest/testserver.html): alcance, args y entorno de prueba.
- [Posit: pruebas del servidor](https://shiny.posit.co/r/articles/improve/server-function-testing/): sesión simulada y entradas.
- [Posit: panorama de pruebas](https://shiny.posit.co/r/articles/improve/testing-overview/): funciones, servidor y navegador.
- [Posit: registro reactivo](https://shiny.posit.co/r/reference/shiny/latest/reactlog.html): visor opcional y límites.
- [R: stopifnot](https://stat.ethz.ch/R-manual/R-devel/library/base/html/stopifnot.html) y [all.equal](https://stat.ethz.ch/R-manual/R-devel/library/base/html/all.equal.html): expectativas y comparación.
- [Hadley Wickham, Mastering Shiny: Testing](https://mastering-shiny.org/scaling-testing.html): lectura abierta de profundización.

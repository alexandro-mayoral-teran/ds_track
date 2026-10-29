# 14.01 — Pregunta y contrato del producto

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **Lección 14.01**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Definir qué producto construir y cómo reconocer un resultado aceptable |
| **Necesitas** | Contratos de datos, indicadores, Quarto y una ruta de app ya practicada |
| **Evidencia** | Contrato revisado, elección de una app y casos esperados justificados |

[Empezar](#antes-de-empezar) · [Ir al lab](../../../labs/14_reproducible_projects/01_product_question_contract/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Antes de organizar carpetas o conectar herramientas, hay que acordar una
pregunta y cómo se evaluará su respuesta. «Hacer un dashboard» describe una
forma de presentación; no define qué pregunta responde, qué datos utiliza
ni qué cifra sería correcta.

Un **contrato del producto** reúne público, necesidad, entradas, reglas,
productos, límites y criterios de aceptación. Es un acuerdo revisable de diseño,
no un contrato jurídico ni una prueba automática de que todo está implementado.
Aquí lo escribiremos antes de construir el pipeline del módulo.

## Antes de empezar

- Revisa los cierres de [11 — Quarto](../../11_reporting_quarto/README.md) y una
  app: [12 — Streamlit](../../12_streamlit/README.md) o [13 — Shiny](../../13_shiny_web/README.md).
  Basta una alternativa; no se exige repetir ambas ni conservar entregas previas.
- Recuerda [validación de datos](../../02_pandas/05_missing_duplicates_rules/README.md),
  el significado de claves/ausencias y la [política de datos](../../../docs/data-policy.md).
- Sigue [recorridos.md](recorridos.md) para una copia nueva. La actividad principal
  es leer, calcular y escribir Markdown; las referencias de código son apoyo.
  Python estándar y R base bastan, sin paquetes, lockfiles o servicios nuevos.

## Qué vas a aprender

- Convertir una intención amplia en una pregunta verificable.
- Separar contrato de datos, reglas de cálculo y aceptación del producto.
- Definir universo, selección, denominador y estados sin ambigüedad.
- Justificar casos esperados antes de implementar una interfaz o pipeline.
- Distinguir especificación, comprobación numérica e integración demostrada.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [ESPECIFICACION.md](ESPECIFICACION.md) | Contrato completo del ejemplo, con estado real de aceptación | Lectura esencial |
| [plantilla_contrato.md](plantilla_contrato.md) | Redactar tu copia y registrar dudas | Actividad principal |
| [cartera.csv](cartera.csv) | Seis observaciones sintéticas, conservadas de la muestra 12.03 | Entrada autocontenida |
| [criterios.csv](criterios.csv) | Nueve preguntas con expectativas explícitas | Predecir y contrastar |
| [referencia.py](referencia.py), [referencia.R](referencia.R) | Recalcular independientemente los casos, sin escribir salidas | Apoyo; elige un lenguaje |
| [recorridos.md](recorridos.md) | Copia nueva, IDE y terminales opcionales | Preparación |

## 1. De «hacer una app» a responder una pregunta

Comienza con una muestra pequeña: dos ventas V01=100 y V02=200 MXN. Si preguntas
«¿qué ventas tienen importe >= 200?», la respuesta es V02, una venta y 200 MXN.
Su proporción por cantidad es 1/2=50%; por importe sería 200/300≈66.67%.
Ambas cifras pueden calcularse correctamente y responder preguntas distintas.

Por eso la pregunta debe declarar **población, condición y medida**. Añade
quién la necesita y para qué revisión. Evita empezar eligiendo biblioteca,
colores o alojamiento: esas decisiones no resuelven un denominador ambiguo.

El caso de este módulo pregunta: **para un corte, unos segmentos y un saldo
mínimo, ¿qué créditos cumplen la regla, cuántos son, cuánto saldo suman y qué
porcentaje de los créditos del corte representan?** Su público es una persona
que revisa datos y necesita conciliar reporte y app, no decidir riesgo real.

## 2. Tres acuerdos diferentes

| Acuerdo | Pregunta que resuelve | Ejemplo |
| --- | --- | --- |
| Contrato de datos | ¿Qué entrada puedo utilizar? | Clave ID/corte única; saldo entero conocido |
| Regla de cálculo | ¿Cómo respondo la pregunta? | Corte → segmentos y saldo >= mínimo → indicadores |
| Aceptación del producto | ¿Qué debe poder demostrar quien recibe el trabajo? | Mismo corte/filtros y valores en reporte y app, reconstrucción explicada |

Un CSV con esquema válido puede contener una suma seleccionada incorrecta.
Una suma correcta puede presentarse con otro corte o un porcentaje mal definido.
Una captura correcta tampoco demuestra que otra persona pueda reconstruirla.
Los tres acuerdos se complementan.

Abre ESPECIFICACION.md y localiza necesidad, diccionario, reglas y aceptación.
Su estado inicial dice diseño revisable: no da por implementado el producto.
Conserva esa distinción al rellenar tu plantilla.

## 3. Datos completos, unidad y clave

La muestra local reproduce los seis registros conocidos, sin exigir una entrega:

| Crédito / segmento | 2026-09-30 | 2026-10-31 |
| --- | ---: | ---: |
| 001 / comercio | 0 | 100 |
| 002 / servicios | 2000 | 1900 |
| 003 / comercio | 2500 | 2600 |

Cada celda de importe corresponde a una fila crédito/corte. Son **seis
observaciones**, no seis créditos distintos: los mismos tres aparecen dos veces.
ID por sí solo no es la clave. No sumes los cortes para describir el saldo a una
fecha ni conviertas 001 en 1 al leer identificadores.

El universo de septiembre tiene tres créditos/4500 MXN; octubre, tres/4600 MXN.
La fuente admite hasta 10000 observaciones, saldo entero 0..1000000, categorías
exactas y fechas válidas 1900–2100. No admite ausencias ni claves repetidas.
Se valida toda la fuente antes de seleccionar un corte, incluso filas que
no aparecerán en el resultado. Estas reglas no equivalen a una limpieza general.

## 4. Escribir el indicador antes del código

Sea U el conjunto de créditos del corte y S la selección por segmento y saldo
>= mínimo. Entonces:

- Cantidad seleccionada = número de créditos de S.
- Saldo seleccionado = suma de pesos enteros de S.
- Cobertura de créditos = 100 × cantidad de S / cantidad de U, si U existe.

Septiembre/ambos/2000 selecciona 002 y 003: 4500 MXN y 2/3≈66.67%. El 100%
de saldo seleccionado sobre saldo del universo es otra medida; no sustituye
la cobertura por cantidad. La presentación puede redondear porcentajes,
pero el cálculo y la conciliación conservan su precisión.

Comercio/0 conserva 001 y 003, con 0/2500 MXN. Comercio/1 conserva solo 003:
misma suma, distinta cantidad. Un caso de cero permite descubrir errores
que una prueba del total no detectaría.

## 5. Vacío, ausencia, rechazo y bloqueo

Ningún segmento seleccionado significa cero filas, no todos los segmentos.
Sobre un universo de tres, la cobertura es 0/3=0%. Noviembre no tiene filas:
no existe denominador y no debe publicarse una cobertura inventada.

Si el mínimo es 1.5, la entrada se rechaza; no se trunca a 1. Si hay una clave
repetida, falla la fuente completa; no se oculta para obtener una selección.
Un resultado anterior visible necesita identificación propia, sin presentarlo
como respuesta válida del intento rechazado.

criterios.csv describe **el resultado nuevo publicable**, no el historial de una
sesión. Sus campos vacíos en rechazo/sin_universo indican medidas no publicables.
Un contador interno de filas puede registrar 0 sin que una cobertura se convierta
en 0%. El formato de auditoría del futuro pipeline aún no se define aquí.

## 6. Criterios que se puedan refutar

«La app funciona» no indica qué observar. Un criterio útil conecta entrada,
resultado y forma de revisión. Por ejemplo:

> Dado octubre, ambos segmentos y mínimo 2000, el resultado válido contiene
> solo 003/2600 MXN, universo de tres créditos/4600 MXN y cobertura 100/3.

El archivo de criterios añade septiembre, cero, frontera 0/1, frontera de
servicios 1900/1901, ningún segmento, corte ausente y mínimo decimal rechazado.
Predice los nueve casos antes de usar las referencias. Añadir expectativas
después de copiar la salida del mismo programa puede conservar su error.

Con los recorridos puedes ejecutar una referencia Python o R. Ambas solo leen
CSV y muestran coincidencias o el primer desacuerdo. No producen HTML, app,
carpetas de entrega, entorno restaurado ni evidencia de una sesión web.
Un OK numérico tampoco revisa si la pregunta es útil, si el texto es claro
o si los productos futuros se reconstruyen: eso requiere revisión humana.

## 7. Alcance esencial y compromisos futuros

El producto previsto tendrá **un reporte HTML Quarto y una app local elegida**.
Ambos deberán mostrar el mismo corte/filtros y conciliar filas, universo y
medidas. Fuentes, contrato, entorno e instrucciones permitirán reconstruirlos.
No necesitas otra app, otro motor de reporte, alojamiento, CI o autenticación.

En esta sección se entrega el **diseño** y su referencia numérica. Estructura,
configuración, entornos, pipeline, pruebas e integración se desarrollarán después,
según el índice del módulo. No creamos un proyecto ejecutable en projects/ ni
checkpoints para marcar planes como terminados.

Si una regla cambia —por ejemplo >= por >—, identifica qué criterios dejarían
de cumplirse, versiona el contrato y revisa la decisión. No cambies la expectativa
solo para aceptar una implementación equivocada. Conserva la versión anterior.

## Práctica

Continúa con el [lab 14.01](../../../labs/14_reproducible_projects/01_product_question_contract/README.md):
redactar un contrato, justificar casos y revisar una ambigüedad con otra persona.

## Evidencia y criterio de salida

Conserva tu contrato completado, app elegida y razones, predicciones/casos,
un desacuerdo detectado y su explicación, más dudas abiertas. Otra persona
debe poder identificar pregunta, clave, unidad, denominador y estados sin
adivinarlos del código. Distingue criterios comprobados hoy y compromisos futuros.

## Siguiente paso

Consulta [14.02 — Estructura y configuración](../README.md#02-estructura-y-configuracion),
todavía planificado. El contrato se revisará al implementar; no acredita una
integración de reporte/app ni el aprendizaje por disponer del ejemplo.

## Referencias primarias

Ejemplos y contrato propios. Lecturas de apoyo consultadas al desarrollar:

- [The Turing Way: diseño de proyectos](https://book.the-turing-way.org/project-design/pd-overview/pd-overview-planning/): propósito, pregunta, público y recursos.
- [The Turing Way: documentación colaborativa](https://book.the-turing-way.org/project-design/pd-overview/pd-overview-repro/): decisiones recuperables para quienes colaboran.
- [The Turing Way: reproducibilidad](https://book.the-turing-way.org/reproducible-research/reproducible-research/): datos y código para repetir un análisis; no sustituye aceptación del producto.

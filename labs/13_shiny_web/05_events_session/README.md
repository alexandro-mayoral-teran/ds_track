# Lab 13.05 — Eventos y estado de sesión

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.05**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Separar edición, aplicación y estado de cada sesión |
| **Entrada** | Copia nueva con mínimo y la cartera de seis observaciones de 13.04 |
| **Evidencia** | Transiciones previstas/observadas, cifras por clave y dos sesiones independientes |

[Lección 13.05](../../../curriculum/13_shiny_web/05_events_session/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Refuerza [13.05 — Eventos y estado de sesión](../../../curriculum/13_shiny_web/05_events_session/README.md).
Sigue [preparación y arranque](../../../curriculum/13_shiny_web/05_events_session/recorridos.md)
desde tu IDE, en una carpeta nueva. No exige entregas previas ni tiene proyecto/
checkpoint implementado. Trabaja en la copia, conservando fuentes y muestras anteriores.

La fuente contiene los mismos tres créditos en septiembre y octubre. Saldos
001/002/003: 0/2000/2500 MXN en septiembre; 100/1900/2600 en octubre. Cada fila
es un crédito en un corte; el denominador de cobertura son sus tres créditos.
Se conserva saldo >= mínimo y ningún segmento selecciona cero filas.

## Actividad

### 1. Predecir el mínimo

Abre minimo.R e inicia con iniciar_app desde la consola R de tu copia. Completa
antes de probar: valor editado, valor guardado y doble guardado en cada paso.

1. Inicio con 2, sin pulsar Guardar numero.
2. Cambia a 3, sin pulsar.
3. Pulsa Guardar numero.
4. Cambia a 7 y sal del control sin guardar.
5. Guarda, luego guarda otra vez sin cambiar número.
6. Cambia a 0 y guarda.

Señala la lectura y escritura de guardado en el archivo. Explica por qué el
contador del botón no es el número guardado. No modifiques input desde R.

### 2. Distinguir contexto aplicado y borrador

Detén el mínimo e inicia app.R. Antes de cada acción predice las cifras y el
contexto aplicado, no solo lo que muestran los controles:

| Paso | Acción | Qué registrar |
| --- | --- | --- |
| 1 | Inicio, sin aplicar | Ausencia de consulta/cifras aplicadas |
| 2 | Aplicar septiembre/ambos/2000 | IDs, cantidad, saldo y cobertura |
| 3 | Editar octubre sin aplicar | Aviso de pendientes y contexto/cifras anteriores |
| 4 | Ocultar/recuperar tabla | Qué consulta reaparece y por qué no se envió borrador |
| 5 | Aplicar octubre | Nueva consulta coherente en todas las salidas |
| 6 | Editar septiembre, luego regresar a octubre sin aplicar | Coincidencia con la consulta aplicada |
| 7 | Aplicar otra vez sin cambios | Acción nueva, contenido igual |

En el paso 3 prueba Enter **dentro del control numérico**, no sobre el botón:
no debería aplicar. Un botón con foco sí puede activarse con teclado. Distingue
foco/acción, no prometas que cualquier tecla Enter tiene el mismo efecto.

### 3. Vacío, cero y un intento rechazado

Aplica septiembre/comercio/0: deben estar 001 y 003. Prepara mínimo 1 sin aplicar
y confirma que todavía hay dos filas. Al aplicar quedan 003 y 2500 MXN: la suma
es igual, pero el conteo y porcentaje cambian.

Desmarca ambos segmentos y aplica: cero filas, saldo 0, cobertura 0% sobre tres.
Recupera ambos, aplica mínimo 2000 y conserva la consulta 002/003, 2/4500/66.67%.

Edita mínimo 1900.5 y aplica. Debe aparecer rechazo; consulta, contexto, tabla y
cifras conservan la aplicación anterior. Corrige a 2000: corregir tampoco aplica
por sí solo. Pulsa de nuevo para reemplazar el aviso de rechazo. Explica dónde
se calcula la consulta nueva y dónde se escribe el estado, y por qué importa su orden.

### 4. Dos sesiones y una recarga

En A aplica octubre/ambos/2000. Abre B en otra pestaña con la misma URL:
inicia sin consulta aplicada. En B aplica septiembre/ambos/2000. Alterna entre
las pestañas y verifica A 003/2600, B 002/003/4500. Los porcentajes son 33.33%
y 66.67%, respectivamente. Editar A tampoco debe modificar el borrador de B.

Recarga A: vuelve a los controles iniciales y sin consulta aplicada. B conserva
su consulta mientras su sesión siga conectada. Detener el proceso R termina
ambas sesiones: no detengas el servidor para simular solo recargar una pestaña.

### 5. Explicar el alcance sin introducir estado global

Localiza dónde se crean cartera, aplicada y aviso. Señala cuál es referencia
de lectura y cuáles se crean por sesión. Dibuja controles → borrador, botón →
acción → consulta aplicada → salidas; distingue la lectura aislada del borrador.

**Ampliación opcional:** explica qué pasaría si aplicada se creara fuera de
server. No necesitas hacer esa modificación ni mezclar sesiones reales para
justificar el problema. reactiveValues sería otra representación del estado;
no hace falta reescribir una solución coherente solo para usar ambas APIs.

<details>
<summary>Ver una pista</summary>

Una salida que lee input$corte sigue al borrador. Una salida que lee
aplicada()$filtros$corte describe la consulta guardada. Revisa el contexto junto
con la tabla: cifras correctas con una etiqueta de otro corte también son un error.

</details>

## Resultado y comprobación

Puedes explicar cuándo se aplica, qué conserva un rechazo y por qué las sesiones
son independientes. Las cifras siempre corresponden a los filtros aplicados;
mostrar tabla es presentación, no envío. Contrasta por ID/corte, además del total.

<details>
<summary>Ver solución razonada</summary>

En el mínimo, inicio/edición no guardan; al guardar 3 muestra 3/6 y editar 7
conserva 3/6 hasta pulsar otra vez. Guardar 7 muestra 7/14; repetir deja contenido
igual. Guardar cero muestra 0/0, que es distinto de no tener número guardado.

En la app, inicio no consulta. Primera aplicación: septiembre, 002/003, 2/4500,
66.67%. Editar octubre deja todo eso aplicado hasta pulsar. Entonces cambia a
octubre, 003, 1/2600 y 33.33%. Ocultar tabla no envía filtros. Regresar el borrador
a los valores guardados elimina pendientes; aplicar una consulta idéntica no
necesita generar cifras distintas.

Septiembre/comercio/0 da 001/003, 2/2500/66.67%; con 1 da 003, 1/2500/33.33%.
Ningún segmento da vacío con 0/0/0%. Rechazar un mínimo decimal no escribe aplicada.
Cada server crea su propio reactiveVal; recargar inicia otra sesión y no recupera
lo guardado. Esto no acredita identidad de usuario ni persistencia en disco.

</details>

## Evidencia y reflexión

Guarda en tu copia personal predicciones/observaciones, el esquema y un contraste
de A/B antes/después de recargar. Incluye ayudas, dudas y siguiente paso; no uses
PROGRESS.md para registrar aprendizaje. Quien acompaña propone un cambio y pide
predecirlo antes de probarlo.

- ¿Qué diferencia hay entre evento nuevo y valor nuevo?
- ¿Por qué guardar solo el corte y calcular el resto desde controles vivos mezclaría consultas?
- ¿Qué ocurre si falta un estado aplicado válido y se rechaza el primer intento?
- ¿Por qué una pestaña no equivale a una identidad autenticada?

## Siguiente paso

Continúa con [13.06 — Validación y mensajes](../../../curriculum/13_shiny_web/06_validation_messages/README.md),
ya disponible.

[← Lección 13.05](../../../curriculum/13_shiny_web/05_events_session/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)

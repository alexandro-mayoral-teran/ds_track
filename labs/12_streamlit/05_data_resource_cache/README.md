# Lab 12.05 — Reutilizar sin perder vigencia

[Inicio](../../../README.md) / [Labs](../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.05**

## Propósito

Comprobar que la caché reutiliza la pregunta correcta y deja de hacerlo al cambiar
sus entradas o su vigencia. Distinguir copia de datos, recurso compartido y filtros.

## Entradas y preparación

- [Lección 12.05](../../../curriculum/12_streamlit/05_data_resource_cache/README.md)
  y [recorridos por shell](../../../curriculum/12_streamlit/05_data_resource_cache/recorridos.md).
- Mismo entorno local de 12.01, sin nuevas dependencias ni entregas previas obligatorias.
- Prepara una carpeta nueva, por ejemplo `output/practica_1205`. Conserva prácticas
  anteriores. Ejecuta mínimo y app desde esa copia; no alteres las fuentes del repo.
- Para comparar llamadas sin caducidad, realiza los primeros controles antes de
  60 segundos. Si necesitas repetir, limpia solo la caché del análisis y vuelve a anotar la marca.

## Predicción

1. Si editas una copia de datos, ¿debe cambiar una nueva llamada igual?
2. ¿Qué entradas de la pregunta deben cambiar la clave?
3. Si cambias el contenido pero no la ruta del CSV, ¿qué debe suceder?
4. ¿Qué filtros quedan después de limpiar la caché? ¿Basta esperar para actualizar la pantalla?

## Actividad

1. Ejecuta el mínimo. Revisa `[100, 200, 999]` frente a `[100, 200]` y las preguntas
   de identidad. Cambia la casilla. Limpia datos y recurso por separado; registra
   qué marca cambia en cada caso.
2. Abre la app completa. Anota octubre/ambos/2000, detalle 003/2600, universo
   3/4600, porcentaje 33.33% y marca en «Observa la caché». Oculta y muestra
   detalle antes de 60 segundos: debe recuperar la misma ejecución.
3. Prepara septiembre y mínimo 2001. Sin enviar, conserva las cifras aplicadas.
   Confirma: obtén 003/2500, universo 4500 y otra marca. Oculta/muestra detalle
   y comprueba reutilización. Vuelve al caso inicial y verifica si su entrada
   aún estaba vigente; explica si hubo caducidad o limpieza.
4. Pulsa «Limpiar caché del análisis». Debe cambiar la marca y conservar los
   filtros aplicados y el número de envíos. No uses «Clear cache» del menú.
5. Con octubre/ambos/2000 ya aplicados, cambia en el CSV de tu copia solo el saldo
   de 003/octubre: 2600 → 2800. Provoca otra pasada con la casilla, sin reenviar.
   Contrasta marca, saldo, universo y envíos con tu predicción. Comprueba la misma
   variante mediante ejecutar.py, sin argumentos.
6. Agrega en tu copia la fila repetida de 001/septiembre. Pregunta por octubre:
   debe rechazarse la fuente completa, aunque antes hubiera resultado en caché.
   Retira solo la fila agregada y comprueba recuperación.
7. Para observar caducidad sin esperar un minuto, detén tu servidor y cambia
   `TTL_SEGUNDOS = 60` a `TTL_SEGUNDOS = 5` en el cache_analisis.py de **tu copia**. Reinicia. Anota la
   marca; espera más de cinco segundos sin modificar la fuente, y provoca otra
   pasada. Debe cambiar la marca y conservar las cifras. La pantalla no se
   actualiza sola al cumplirse los cinco segundos. El texto de observación toma
   el TTL de esa misma constante y debe mostrar 5.
8. Abre otra pestaña. Sus filtros empiezan desde el inicio; puede reutilizar
   la caché global para una pregunta igual si sigue vigente. La limpieza de
   esa función afecta sus entradas comunes, sin cambiar los filtros de la otra sesión.

## Resultado y comprobación

| Caso | Resultado esperado |
| --- | --- |
| Dos llamadas iguales antes del TTL | Misma marca; cifras y detalle correctos |
| Septiembre ≥ 2001 aplicado | 003/2500, universo 3/4500, 33.33% |
| Limpiar análisis | Nueva marca; mismos filtros y envíos |
| Variante 2800 | 003/2800, universo 3/4800, 33.33%; nueva marca sin nuevo envío |
| Duplicado fuera del filtro | Error, sin cifras anteriores presentadas como válidas |
| TTL vencido y nueva pasada | Otra ejecución; mismas cifras si datos y parámetros no cambiaron |
| Mínimo | Datos copiados; el recurso es el mismo objeto de lectura |

<details>
<summary><strong>Ver solución razonada</strong></summary>

El resultado se guarda con los registros completos, filtros y versión de reglas.
Editar una copia de cache_data no cambia el valor guardado. cache_resource
recupera el mismo objeto; el mínimo evita mutarlo mediante una vista de lectura.

Cambiar el saldo modifica las entradas aunque el nombre de archivo permanezca.
El importe sube 200 MXN tanto en la selección como en el universo; continúa un
crédito de tres, por eso el porcentaje no cambia. El CSV se lee y valida antes
de consultar caché: un duplicado de otro corte no queda oculto por un acierto.

TTL decide si una entrada puede reutilizarse al volver a llamarla. No dispara
la pasada. Limpiar por función elimina sus entradas, pero no modifica las claves
de filtros de session_state. Otra sesión puede compartir un resultado y mantener
elecciones diferentes.

</details>

## Evidencia y reflexión

Conserva tu carpeta y una tabla con datos/versión/filtros, marca, detalle, cifras
y acción de actualización. La marca observa ejecución; no demuestra que el
cálculo sea correcto ni que sea más rápido. Revisa también las referencias manuales.

- ¿Qué trabajo continúa ocurriendo en cada pasada de esta app?
- ¿Por qué no bastan ruta y totales como versión de una fuente?
- ¿Qué pasaría si un argumento necesario empezara con `_` y quedara fuera del hash?
- ¿Por qué un recurso compartido mutable necesita revisar concurrencia?
- ¿Cuándo preferirías no usar caché para una muestra pequeña?

Revisa con tu compañero y registra ayudas, dudas y siguiente paso en tu bitácora
personal. PROGRESS.md registra autoría, no aprendizaje. No hay proyecto ni
checkpoint asociado todavía.

## Siguiente paso

Vuelve al [criterio de salida](../../../curriculum/12_streamlit/05_data_resource_cache/README.md#evidencia-y-criterio-de-salida)
y después consulta [12.06 — Mensajes y casos sin datos](../../../curriculum/12_streamlit/README.md#06-mensajes-y-casos-sin-datos),
todavía planificado.

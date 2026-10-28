# Lab 12.04 — Preparar, aplicar y conservar

[Inicio](../../../README.md) / [Labs](../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.04**

## Propósito

Comprobar el límite entre editar entradas, aplicarlas y recordar una selección
durante una sesión. Contrastar esa memoria con datos que se leen de nuevo.

## Entradas y preparación

- [Lección 12.04](../../../curriculum/12_streamlit/04_session_state_forms/README.md)
  y sus [recorridos](../../../curriculum/12_streamlit/04_session_state_forms/recorridos.md).
- Mismo entorno local de 12.01; no hay dependencias nuevas ni entregas previas obligatorias.
- Ejecuta el preparador **desde el repositorio** con un destino nuevo, por ejemplo
  `output/practica_1204`. Trabaja sobre esa copia de seis archivos, no sobre fuentes.
  Si ya existe, elige otra carpeta y conserva la anterior.
- Primero ejecuta el contador mínimo; después detén ese servidor y abre la app
  completa. No uses el app.py fuente de 12.04 sin preparar los módulos hermanos.

## Predicción

Antes de probar, escribe:

1. Después de dos clics y de cambiar la casilla del mínimo, ¿qué contador queda?
2. Si la app muestra octubre y preparas septiembre ≥ 2001 sin enviar, ¿qué saldo ves?
3. Después de aplicar septiembre, ¿qué cambia al ocultar y mostrar detalle?
4. ¿Qué filtros tendrá una pestaña nueva? ¿Qué ocurre al recargar la primera?

## Actividad

1. En el mínimo pulsa «Sumar uno» dos veces. Cambia la casilla. Contrasta variable
   local y contador de sesión; abre otra pestaña para comprobar el inicio nuevo.
2. En la app completa identifica el estado inicial: octubre, ambos segmentos,
   mínimo 2000; un crédito, 2600 MXN, 33.33% y cero envíos.
3. Prepara septiembre y mínimo 2001. Sal del campo con Tab; todavía **no** pulses
   «Aplicar filtros». Los resultados deben seguir en octubre. En esta app Enter
   tampoco envía el formulario.
4. Pulsa «Aplicar filtros». Registra filtros efectivos, ID, segmento, fecha,
   saldo y universo. Oculta y muestra el detalle: la selección aplicada y el
   número de envíos deben conservarse.
5. En otra pestaña abre la URL y compara con la primera. Después recarga la
   primera: registra que vuelve a los valores iniciales, no al último envío.
6. Aplica estos casos: septiembre ≥ 2000 con ambos segmentos; octubre ≥ 2000
   solo servicios; octubre ≥ 1900 solo servicios; lista de segmentos vacía.
   Compara el detalle y el denominador, y recupera el estado inicial mediante
   otro envío. No basta editar los campos.
7. En tu copia cambia **solo** el saldo de 003 en octubre, 2600 → 2800. Con
   octubre/ambos/2000 ya aplicados, provoca otra pasada ocultando o mostrando
   detalle, **sin reenviar**. Comprueba 2800 MXN y universo 4800, con el mismo
   contador de envíos. Los filtros permanecen; los datos se leen de nuevo.
8. Contrasta esa variante mediante el ejecutar.py de tu copia, sin argumentos.
   Detén y reinicia tu servidor; comprueba filtros predeterminados y cero envíos,
   pero conserva la variante del CSV en disco (2800/4800).

No dependas de un borrador pendiente después de accionar otro control: los
cambios del formulario se envían juntos al confirmar. Revisa sus campos antes
de cada envío. No alteres los CSV ni funciones originales de 12.03.

## Resultado y comprobación

| Situación | Resultado esperado |
| --- | --- |
| Contador tras dos clics y casilla | Variable local 1, contador 2; pestaña nueva 0 |
| Preparar septiembre ≥ 2001 sin enviar | Sigue octubre: 003/2600, universo 4600, cero envíos |
| Aplicar ese formulario | 003/2500, universo 4500, 33.33%, un envío |
| Ocultar y mostrar detalle | Misma selección aplicada y un envío |
| Pestaña nueva / página recargada | Configuración inicial y cero envíos |
| Septiembre ≥ 2000, ambos | 002/2000 y 003/2500, 2 de 3, 66.67% |
| Octubre servicios ≥ 2000 / ≥ 1900 | Vacío / 002 con 1900; universo 3/4600 en ambos |
| Ningún segmento | Ninguna fila; 0% con universo del corte conservado |
| Variante del CSV, siguiente pasada | 003/2800, universo 3/4800, 33.33%; no cuenta otro envío |
| Reinicio tras la variante | Filtros iniciales, cero envíos, CSV modificado conservado |

<details>
<summary><strong>Ver solución razonada</strong></summary>

El `if clave not in st.session_state` inicializa una vez por sesión. El clic
actualiza el contador, mientras que una casilla simplemente causa otra pasada.
La variable local vuelve a asignarse en todas ellas.

El formulario no envía cada edición al servidor. Al confirmar se copian sus
campos a `filtros_aplicados`; las pasadas siguientes leen esa copia, incluso si
`enviado` vuelve a False. La casilla de detalle no modifica esa clave. Otra
pestaña empieza otra sesión y una recarga no conserva esta memoria.

El cambio de 2600 a 2800 no altera cuántos créditos cumplen: sigue uno de tres.
El saldo seleccionado y el del universo aumentan 200 MXN, el porcentaje permanece
en 33.33% y el contador de envíos no aumenta porque no confirmaste otro lote.
Conservamos parámetros, no resultados ni una copia congelada del CSV. Reiniciar
el servidor pierde los parámetros de sesión, pero no borra el archivo en disco.

</details>

## Evidencia y reflexión

Conserva la carpeta preparada, una tabla de predicción/resultado y parámetros
efectivos de cada caso. Una captura antes/después puede ayudar; no sustituye
el detalle por crédito ni exige capturar todas las combinaciones.

- ¿Qué diferencia hay entre la key de un widget y una clave propia de sesión?
- ¿Qué fallaría al inicializar filtros sin comprobar si ya existen?
- ¿Por qué la tabla no debe vivir únicamente dentro de `if enviado`?
- ¿Guardar filtros evita leer el CSV en la siguiente pasada?
- ¿Qué evidencia necesitas fuera de la sesión para retomar mañana?

Revisa las respuestas con tu compañero y guarda ayudas, dudas y siguiente paso
en tu bitácora personal. PROGRESS.md registra desarrollo del material. No hay
proyecto ni checkpoint asociado todavía.

## Siguiente paso

Vuelve al [criterio de salida de la lección](../../../curriculum/12_streamlit/04_session_state_forms/README.md#evidencia-y-criterio-de-salida).
Después consulta [12.05 — Caché de datos y recursos](../../../curriculum/12_streamlit/README.md#05-cache-de-datos-y-recursos),
todavía planificado.

# Contrato del producto — ejemplo resuelto 14.01

Versión de reglas: **1401-v1**. Estado: diseño revisable, con referencia aritmética;
reporte y aplicación integrados todavía no implementados. Datos completamente
sintéticos; no usar este ejemplo para decidir sobre créditos reales.

## Público, necesidad y pregunta

Una persona revisora de datos necesita consultar un corte y comprobar que reporte
y app describen la misma selección. Pregunta: **para una fecha de corte, unos
segmentos y un saldo mínimo, ¿qué créditos cumplen la regla, cuántos son, cuánto
saldo suman y qué porcentaje de los créditos del corte representan?**

El producto describe registros; no estima riesgo, causalidad, rentabilidad ni
predice incumplimiento. No utiliza datos reales ni requiere servicios externos.

## Entrada y diccionario

cartera.csv es una copia de la muestra sintética de 12.03, sin modificar el
original. Seis filas, tres créditos por corte; una fila significa crédito/corte.
Clave compuesta id_credito/fecha_corte. CSV UTF-8, encabezado exacto y columnas
en este orden. Todos los campos son sintéticos y no sensibles:

| Campo | Tipo lógico | Unidad / valores | Ausencia | Regla |
| --- | --- | --- | --- | --- |
| id_credito | Texto | Tres dígitos | No | Conservar 001, no convertir a 1 |
| segmento | Categoría nominal | comercio, servicios | No | Coincidencia exacta |
| fecha_corte | Fecha representada como texto | YYYY-MM-DD | No | Calendario válido, años 1900–2100 |
| saldo_mxn | Entero | MXN, 0..1000000 | No | Texto canónico, sin signos/decimales/espacios |

Hasta 10000 observaciones; saldo acumulado máximo 10000000000 MXN, exacto
en enteros Python y en double R bajo este contrato. No es una prueba de escala.
Fuente completa validada antes de filtrar, incluso filas de otro corte. No
reparar duplicados, imputar ausencias o redondear importes para admitirlos.

## Parámetros y reglas

- corte: fecha válida YYYY-MM-DD dentro del rango del contrato.
- segmentos: comercio y/o servicios. En criterios.csv se separan con `|`;
  `ninguno` representa selección vacía, no todos. Sin repeticiones ni etiquetas extra.
- minimo_texto: entero canónico 0..1000000, sin signos, espacios, ceros iniciales
  salvo 0, decimales o notación científica. No corregir 1.5 a 1.

1. Validar toda la fuente. Si falla, bloquear la solicitud actual y no publicar
   medidas como si fuera una selección vacía.
2. Validar parámetros. Si se rechazan, no producir resultado nuevo. En la app,
   cualquier consulta anterior visible debe identificarse como anterior y mantener
   su propio corte/filtros; su interacción exacta se implementará posteriormente.
3. Universo: todos los créditos de la fecha solicitada. Nunca sumar cortes.
4. Selección: segmento elegido **y saldo_mxn >= mínimo**. Orden final por ID.
5. Cantidad: número de créditos seleccionados; saldo: suma de sus pesos enteros.
6. Cobertura: 100 × cantidad seleccionada / cantidad del universo del corte.
   No es porcentaje de saldo ni proporción de toda la fuente de dos fechas.

## Estados y publicación

| Estado | Condición | Resultado nuevo publicable |
| --- | --- | --- |
| ok | Universo existente y selección no vacía | Filas, cantidad, saldo y cobertura |
| vacio | Universo existente, ninguna fila cumple | Tabla sin filas, cantidad/saldo/cobertura 0; sin barras inventadas |
| sin_universo | Ninguna fila en el corte | Corte/diagnóstico, sin medidas ni exportación de vista |
| rechazo | Parámetros inválidos | Motivo, sin nuevo resultado válido |
| bloqueo de fuente | Esquema/clave/tipo/archivo inválido | Diagnóstico, sin nuevo resultado válido |

En criterios.csv, campos vacíos de medidas significan **no publicables**, no
ceros. Para vacio se conserva el universo. Un contador interno de filas del corte
puede ser 0 en sin_universo: eso no convierte la cobertura en 0%. Este archivo
es una matriz de aceptación del resultado nuevo, no un formato final de auditoría
ni una simulación del estado de una sesión previa.

## Productos previstos

Un reporte HTML Quarto y **una** app local, Streamlit o Shiny, deberán describir
el mismo corte/filtros y conciliar valores por ID, universo e indicadores. Elegir
la ruta que ya practicaste; no desarrollar dos apps ni dos motores de reporte.
Cada producto mostrará unidades, filtro >=, denominador y estado de resultado.
Tabla/figura/descarga deberán proceder de la misma selección identificada.

La entrega futura incluirá fuente, reglas, configuración, código, entorno e
instrucciones de reconstrucción. No se fija todavía una estructura de carpetas,
orquestador o CLI final: corresponde a las siguientes secciones. Alojamiento,
autenticación, CI y automatización real quedan fuera del cierre esencial.

## Criterios de aceptación

A1. Para fuente válida, cada fila de criterios.csv coincide en estado, IDs,
universo, cantidades, saldos y cobertura; se comparan valores por crédito además
de totales. Cero conocido conserva crédito; vacío/sin universo no se confunden.
ids y saldos_mxn usan listas separadas por `|`, en el mismo orden por ID;
por ejemplo 002|003 corresponde a 2000|2500.

A2. Fuente inválida fuera del corte también bloquea: introducir un duplicado de
octubre y solicitar septiembre debe detectarse antes del filtro.

A3. Reporte y app futuros mostrarán el mismo corte/filtros y resultados bajo el
mismo contrato. No compararlos si sus preguntas efectivas difieren.

A4. Cambiar datos/parámetros requerirá un resultado identificable de esa ejecución;
no aceptar como actual un reporte congelado o consulta anterior sin explicarlo.

A5. Otra persona deberá reconstruir el producto desde fuentes/instrucciones y
explicar un caso habitual, uno vacío y uno inválido. Una captura, huella o OK
aritmético no demuestra por sí solo esa reconstrucción.

Hoy A1 puede contrastarse con las referencias de esta lección; A2 se puede
ensayar en una copia. A3–A5 son compromisos de aceptación futura, pendientes
de implementación/evidencia. No son pruebas de integración ya pasadas.

## Revisión humana y cambios

Revisar que público/pregunta/reglas respondan a la necesidad, que la elección de
una app sea suficiente y que el alcance sea viable. Registrar en la copia
personal quién revisó, dudas y decisiones, sin publicar datos personales.

Si cambia >= por >, denominador, unidad o tratamiento de ausencia, cambiar versión
de reglas, criterios y explicación antes de implementar. Conservar el contrato
anterior; no modificar expectativas únicamente para que pase un resultado erróneo.

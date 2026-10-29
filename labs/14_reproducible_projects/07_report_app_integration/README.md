# Lab 14.07 — Conciliar entrega, reporte y aplicación

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.07**

## Relación y objetivo

Refuerza [14.07 — Integración de reporte y app](../../../curriculum/14_reproducible_projects/07_report_app_integration/README.md).
Objetivo: demostrar que los tres productos representan la misma consulta y
reconocer cuándo una vista conserva una fotografía anterior. Proyectos y
checkpoints siguen pendientes; basta una aplicación elegida.

## Entrada

Usa las 53 fuentes del [preparador y recorrido elegido](../../../curriculum/14_reproducible_projects/07_report_app_integration/recorridos.md).
Trabaja en una copia nueva. Elige Python/Streamlit o R/Shiny; conserva fuentes,
intentos, entregas y reportes. No necesitas salidas personales de secciones previas.

La muestra sintética tiene tres créditos por corte, saldos MXN enteros y clave
ID/fecha. Ambos segmentos y mínimo inclusivo 2000 seleccionan 003/2600 en
octubre, sobre universo 3/4600; septiembre selecciona 002/2000 y 003/2500, sobre
3/4500. Servicios de octubre con mínimo 1901 da cero seleccionados sobre
universo válido. Noviembre no tiene universo y no produce entrega.

## 1. Predecir la conciliación

Antes de ejecutar, prepara una tabla con configuración, IDs/saldos esperados,
universo, saldo seleccionado y cobertura. Añade columnas para reporte y app.
Tu acompañante elige una fila para que expliques el denominador. La referencia
debe salir del contrato/datos anteriores, no de copiar el texto que muestre la app.

## 2. Producir y revisar tres casos

Realiza el recorrido completo de tu ruta: pruebas heredadas, tres intentos,
tres entregas, preparación/render de tres reportes e inicio local de la app.
Guarda comandos y versiones. En cada caso:

1. Aplica la configuración y abre el reporte correspondiente.
2. Compara corte, segmentos, mínimo, versión de reglas, destino y revisión.
3. Revisa cada crédito y saldo en la tabla y en las etiquetas de las barras.
4. Comprueba conteos, sumas y cobertura. Para porcentajes usa tolerancia de
   1e-10 puntos porcentuales si comparas las representaciones decimales.
5. Explica por qué las horas de comprobación pueden diferir aunque los datos coincidan.

No compares revisiones MD5 entre Python y R si eliges explorar ambos: sus
insumos y motores son distintos. El criterio analítico son claves y valores.

<details>
<summary><strong>Pista: distinguir cantidades</strong></summary>

Octubre tiene tres créditos en el universo y uno seleccionado. El saldo del
universo es 4600 y el seleccionado 2600. La cobertura es 1/3 de los créditos,
no 2600/4600 del saldo ni 1/1 de los seleccionados.

</details>

## 3. Separar borrador, aplicación y rechazo

Aplica octubre. Cambia la opción a septiembre sin pulsar el botón y anota qué
configuración muestra la vista. Debe conservar octubre con aviso de borrador
distinto. Pulsa Comprobar entrega y concilia septiembre.

Aplica Selección vacía y explica por qué sí hay universo, cero seleccionados y
un reporte válido sin barras. Después aplica Sin universo: la app debe rechazar
y retirar los indicadores anteriores. No intentes crear una salida vacía para
hacer desaparecer ese rechazo. Abre otra sesión o recarga; no debe heredar tu
consulta aplicada.

## 4. Un reporte anterior no se actualiza solo

Deja el reporte de septiembre abierto mientras aplicas octubre en la app.
Describe la diferencia con sus filtros y cortes visibles. Luego usa la misma
configuración en ambos y concilia. No cambies un total a mano para que coincidan.

Ahora considera una actualización del CSV después de preparar los reportes.
Sin modificar todavía archivos, responde:

- ¿Cuándo se enteraría la app? ¿Qué debe pasar al pulsar Comprobar entrega si
  la entrega anterior ya no coincide con el CSV actual?
- ¿Qué mostraría el HTML ya abierto? ¿Por qué renderizar el mismo .qmd no
  vuelve a calcular los valores de su fotografía?
- ¿Qué archivos nuevos y qué comprobaciones necesitarías para una actualización válida?

<details>
<summary><strong>Ampliación opcional: observar una fuente cambiada</strong></summary>

Haz este ensayo en otra copia nueva del producto y completa primero su entrega,
reporte y app de octubre. Conserva una copia de la fuente antes de cambiarla.
En el editor cambia solo el saldo de 003 de octubre de 2600 a 2800 y guarda.
Pulsa Comprobar entrega: debe rechazar y retirar las cifras, porque la entrega
anterior no coincide con el cálculo actual. El HTML ya preparado sigue siendo
histórico; el verificador debe rechazar su uso como reporte actual.

No renueves marcas a mano. Conserva evidencia del rechazo y restaura la fuente
desde su respaldo para recuperar la consulta anterior mediante una comprobación
nueva. Para una actualización definitiva se necesita configuración/salida/reporte
nuevos y una opción explícita de app que apunte a esa configuración.

</details>

## Resultado esperado y solución razonada

<details>
<summary><strong>Ver solución después de comprobar</strong></summary>

| Caso | Detalle | Indicadores y presentación |
| --- | --- | --- |
| Octubre | 003/2600 | Universo 3/4600, uno seleccionado, 2600 MXN y 1/3; una barra |
| Septiembre | 002/2000 y 003/2500 | Universo 3/4500, dos seleccionados, 4500 MXN y 2/3; dos barras |
| Vacío | Ninguna fila | Universo 3/4600, cero seleccionados, 0 MXN y 0%; encabezados y sin barras |
| Sin universo | Sin entrega | Rechazo y retirada de la vista anterior |

El borrador cambia una opción, no la consulta aplicada. El botón vuelve a
validar y sustituye la vista solo con un resultado comprobado; en esta práctica
un rechazo la retira. Las horas de comprobación son distintas de los cortes y
pueden diferir entre consumidores. La revisión debe coincidir dentro de una
ruta si ambos muestran la misma entrega; MD5 no autentica ni sustituye revisar
los valores. Tampoco se comparan longitudes de barras entre vistas con escalas locales.

El HTML es una fotografía preparada; ni abrirlo ni renderizar su mismo .qmd lo
sincronizan con un CSV cambiado. Una consulta actual exige otra comprobación y,
cuando cambian insumos, otra entrega y otro reporte conservando los anteriores.

</details>

## Evidencia y criterio de salida

Conserva tu tabla de predicciones/comparaciones, comandos/versiones, intentos,
entregas, tres reportes y una nota de borrador, vacío, rechazo y sesión nueva.
Una captura puede complementar, pero no sustituye los archivos y valores por ID.
Explica la actualización y las limitaciones de reloj, MD5 y revisión automática.
La persona que acompaña debe poder elegir un caso y conciliarlo en los productos.

Guarda la práctica en tu copia personal; PROGRESS.md registra desarrollo del
material. No hay proyecto/checkpoint implementado, automatización ni despliegue.

Siguiente lección: [14.08 — Entrega y automatización opcional](../../../curriculum/14_reproducible_projects/08_delivery_optional_automation/README.md),
disponible como ampliación opcional con su lab. [Volver a 14.07](../../../curriculum/14_reproducible_projects/07_report_app_integration/README.md).

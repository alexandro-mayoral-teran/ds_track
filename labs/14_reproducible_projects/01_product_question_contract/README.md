# Lab 14.01 — Definir la pregunta y la aceptación del producto

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.01**

[Volver a la lección](../../../curriculum/14_reproducible_projects/01_product_question_contract/README.md)

## Objetivo y entrada

Escribir un contrato que otra persona pueda revisar antes de construir reporte
y app. Prepara tu copia según los [recorridos](../../../curriculum/14_reproducible_projects/01_product_question_contract/recorridos.md).
Recibes ejemplo resuelto, plantilla, seis filas sintéticas y nueve criterios.
No necesitas entregas previas, paquetes nuevos ni dos rutas de aplicación.

## 1. Precisar la necesidad

Transforma «quiero un dashboard de cartera» en una pregunta verificable.
Completa público, necesidad, población/corte, filtro, medida y límite en la
plantilla de tu copia. Elige Streamlit o Shiny según la ruta practicada.
Explica por qué una sola app y un reporte HTML bastan para el producto previsto.

Compara después con ESPECIFICACION.md. Puedes conservar el caso común; no es
necesario inventar otro dominio o cambiar la fuente para demostrar comprensión.

## 2. Predecir antes de ejecutar

Sin usar los scripts, explica estos resultados:

| Caso | IDs | Saldo | Créditos / universo |
| --- | --- | ---: | ---: |
| Septiembre / ambos / 2000 | 002, 003 | 4500 | 2/3 |
| Octubre / ambos / 2000 | 003 | 2600 | 1/3 |
| Septiembre / comercio / 0 | 001, 003 | 2500 | 2/3 |
| Septiembre / comercio / 1 | 003 | 2500 | 1/3 |

Resuelve los otros cinco casos de criterios.csv. Distingue vacío sobre universo,
corte ausente y entrada rechazada; explica los campos de medidas no publicables.
Aclara por qué contar las seis filas como seis créditos o dividir entre seis
cambiaría la pregunta.

Si utilizas una referencia, ejecuta solo Python o R siguiendo el recorrido y
contrasta sus nueve resultados con tu predicción. Un OK no revisa tu redacción.

## 3. Detectar una especificación ambigua

Una revisión propone: «porcentaje seleccionado = saldo seleccionado / saldo
del corte». Compárala con el contrato de cobertura de créditos. Para septiembre
con ambos segmentos/mínimo 2000, calcula ambos porcentajes. Explica cuál responde
a la pregunta acordada y qué habría que renombrar si se quisiera publicar el otro.

En una copia de criterios.csv, cambia el porcentaje de septiembre a 100,
sin modificar fuente ni reglas. Predice el desacuerdo y ejecuta tu referencia.
Restaura el criterio 100 × 2/3. No cambies el código para ocultar la diferencia.

## 4. Añadir una frontera justificada

En criterios.csv de tu copia añade **septiembre, servicios, mínimo 2001**,
con nombre de caso único. Escribe estado, IDs, universo y medidas antes de
ejecutar. Debe ser una selección vacía sobre un universo existente.

Revisa con la referencia elegida. ¿Por qué cambiar el filtro de >= a > sería
una modificación de reglas y no una corrección de presentación?

Como caso de fuente, duplica una fila de octubre en otra copia del CSV y pide
septiembre: explica por qué debe bloquearse antes del filtro. Conserva la
fuente original y registra el diagnóstico si ensayas la referencia.

## 5. Revisar la aceptación futura

Intercambia tu contrato con otra persona. Sin abrir código, debe localizar:

- Clave, unidad, categorías/ausencias, límites y validación de fuente completa.
- Numerador, denominador, frontera y significado de ningún segmento.
- Qué se publica ante cero, vacío, sin universo, rechazo y fuente inválida.
- Qué debe coincidir entre reporte y app, con el mismo corte/filtros efectivos.
- Cómo distinguir un resultado nuevo de otro anterior y cómo se reconstruirá.

Marca los criterios por su estado real: diseño revisado, aritmética comprobada
o integración pendiente. No marques reporte/app/reconstrucción como implementados.
No crees un checkpoint de proyecto inexistente para rellenar una tabla.

## Ayudas y solución razonada

<details>
<summary>Ver denominadores y frontera adicional</summary>

Septiembre selecciona dos de tres créditos, por eso su cobertura es 66.67%.
Su saldo seleccionado coincide con los 4500 MXN del universo, por lo que la
proporción de saldo sería 100%. Son medidas distintas.

La fila adicional de criterios.csv es:

```csv
servicios_septiembre,2026-09-30,servicios,2001,vacio,,,3,0,4500,0,0
```

002 tiene 2000 y no cumple >= 2001. El universo no desaparece. Para noviembre
se informa sin universo, sin publicar una cobertura 0%; para 1.5 se rechaza
el parámetro sin truncarlo. Un duplicado de octubre invalida toda la fuente.

</details>

<details>
<summary>Ver qué está comprobado al terminar esta sección</summary>

Se ha redactado/revisado un diseño y, si ejecutaste la referencia, se contrastó
su aritmética. Aún faltan estructura, configuración, entornos, pipeline,
integración de productos y reconstrucción final. La matriz de aceptación fija
expectativas para ese trabajo; no afirma que ya exista.

</details>

## Evidencia y criterio de salida

Guarda contrato completado, ruta elegida y razones, predicciones/casos, fallo
detectado, frontera añadida y revisión humana. Registra dudas y siguiente paso
en tu copia personal. La evidencia debe permitir explicar las reglas sin
depender de recordar cómo estaba configurada una app anterior.

## Siguiente paso

Consulta [14.02 — Estructura y configuración](../../../curriculum/14_reproducible_projects/README.md#02-estructura-y-configuracion),
todavía planificado. No hay proyecto final ni checkpoints implementados.

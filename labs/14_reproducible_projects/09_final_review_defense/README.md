# Lab 14.09 — Demostrar y defender el cierre

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.09**

## Relación y objetivo

Refuerza [14.09 — Revisión final y defensa de decisiones](../../../curriculum/14_reproducible_projects/09_final_review_defense/README.md).
Objetivo: reconstruir el producto desde fuentes, demostrar sus casos y explicar
elecciones y límites con otra persona. Es la última práctica de la base del
recorrido; no activa proyectos ni checkpoints.

## Entrada

Elige Python/Streamlit o R/Shiny. Usa las 53 fuentes reunidas por el preparador
de 14.07 y los [recorridos completos](../../../curriculum/14_reproducible_projects/09_final_review_defense/recorridos.md).
No necesitas entregas personales anteriores ni completar la sección opcional
14.08. Conserva el [CSV original externo](../../../curriculum/14_reproducible_projects/01_product_question_contract/cartera.csv)
y trabaja en una carpeta nueva. No copies bibliotecas instaladas ni resultados.

La base es sintética: 001, 002 y 003 por cada corte. Septiembre: 0, 2000 y
2500 MXN; octubre: 100, 1900 y 2600. Clave ID/corte, IDs textuales, saldos
enteros, fuente completa válida antes de filtrar. La cobertura cuenta créditos
seleccionados respecto a los créditos del corte.

Copia estas plantillas a tus notas personales, sin completar los originales:
[revisión](../../../curriculum/14_reproducible_projects/09_final_review_defense/plantillas/REVISION.md),
[decisiones](../../../curriculum/14_reproducible_projects/09_final_review_defense/plantillas/DECISIONES.md)
y [acta](../../../curriculum/14_reproducible_projects/09_final_review_defense/plantillas/ACTA_CIERRE.md).
Registra quién te acompaña y qué ayuda utilizas. Se puede dividir la práctica
en varias sesiones; al retomar, identifica los resultados de cada una.

## 1. Predecir antes de ejecutar

Completa la predicción de octubre, septiembre, vacío y sin universo en tu
registro. Indica IDs, saldo, universo y cobertura esperada. Explica por qué
septiembre distingue `>= 2000` de `> 2000` y por qué noviembre no admite
publicar una cobertura cero como si existiera población.

Quien acompaña elige un caso; justifica su denominador con las filas de origen.
No sustituyas esa explicación por una suma coincidente.

## 2. Reconstruir desde fuentes

Sigue el recorrido elegido: prepara copia nueva, revisa los metadatos, restaura
el cálculo y ejecuta los siete grupos de pruebas. Traza las tres consultas y
genera/renderiza sus tres reportes. Conserva comandos y diagnósticos.

Comprueba las seis filas fuente contra el CSV externo, por clave y campo.
Después revisa resultados por crédito, filtros, unidades, contexto y marcas.
Si dos importes cambian pero mantienen la suma, esa comparación debe distinguirlos.
Los verificadores de 14.07 usan la fuente actual del proyecto: no confundir su
aprobación con haber contrastado ya el original externo.

## 3. Observar reporte y aplicación

Abre los tres HTML nuevos. Restaura por separado la interfaz elegida e iníciala
solo en localhost. Demuestra:

- Una sesión nueva sin cifras aplicadas.
- Octubre y septiembre con detalle, barras, filtros y cobertura conciliados.
- Borrador de otro caso sin aplicar, identificado y sin cambiar las cifras aplicadas.
- Vacío válido con contexto y sin barras inventadas.
- Sin universo con rechazo y retiro de cifras anteriores.
- Otra sesión que no hereda la selección aplicada.

Distingue fecha de corte, hora de comprobación y momento del render. Explica
qué actualizarías si cambia la fuente y por qué un HTML histórico no se vuelve
actual al abrirlo. Detén la app al terminar.

## 4. Mostrar un control que detecte una falla

Como indica el recorrido, copia el reporte de octubre a la carpeta nueva
reportes/ensayo_saldo. Solo en su seleccion.csv cambia 003/2600 a 003/2700.
Predice el rechazo, ejecuta el verificador sobre el ensayo e identifica el motivo.
La tabla distinta debe detectarse; un fallo de entorno, ruta o sintaxis no cuenta.

Verifica después el reporte original. Debe seguir aprobando. Conserva el ensayo
rechazado y el diagnóstico. Explica qué parte se comprobó y qué fallas todavía
no están cubiertas por esta demostración.

<details>
<summary><strong>Contraste de los casos y de la falla</strong></summary>

Octubre: 003/2600, universo 3/4600 y cobertura 1/3. Septiembre: 002/2000 y
003/2500, universo 3/4500 y cobertura 2/3. Vacío: octubre/servicios/mínimo 1901,
sin seleccionados y cobertura 0% sobre tres créditos. Sin universo: noviembre,
sin medidas nuevas válidas. El ensayo debe señalar que la tabla del reporte
es distinta de la entrega; aprobar el original no convierte el ensayo en válido.

</details>

## 5. Defender tres decisiones

Completa tres registros: lenguaje/app, representación/validación y separación
de cálculo/presentación o recuperación. Para cada uno presenta necesidad,
alternativas, elección, evidencia, consecuencias y cuándo reconsiderarlo.

Quien acompaña plantea una objeción, por ejemplo: «¿por qué no usar otro motor?»
o «¿por qué validar filas que no se seleccionan?». Contesta con el contrato y
evidencia. Si hace falta una medición que no tienes, regístrala como pendiente;
no inventes un argumento de rendimiento.

## 6. Acordar el acta y el siguiente paso

Completa cada punto esencial del acta con evidencia y explicación. Si alguno
falla o falta, el resultado sigue siendo cierre pendiente. Solo cuando todos
estén observados puede registrarse una demostración realizada en ese alcance.
Indica ayudas, dudas y límites, aunque la demostración haya sido satisfactoria.
No usar no aplica para omitir un requisito esencial.

Acuerden un pendiente de práctica o depuración con responsable, acción y
comprobación esperada. CI y 14.08 pueden quedar fuera con motivo; proyectos y
checkpoints conservan su disponibilidad real en el índice.

## Evidencia y criterio de salida

Conserva registro de revisión, tres decisiones y acta; copia reconstruida,
versiones/comandos, comparación externa, pruebas, tres consultas/reportes y
ensayo rechazado. Quien acompaña debe poder seguir un crédito desde el CSV
hasta el reporte y la app, y discutir una decisión sin depender de una afirmación
de «ya funciona». Una plantilla marcada no autentica esa sesión ni certifica aprendizaje.

No hay siguiente lección numerada. Continúa con la práctica o depuración acordada
en [cierre y reanudación](../../../docs/reproducible-projects-closure.md).
[Volver a la lección](../../../curriculum/14_reproducible_projects/09_final_review_defense/README.md)
· [Módulos](../../../curriculum/README.md).

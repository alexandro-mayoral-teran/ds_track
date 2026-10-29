# 14.09 — Revisión final y defensa de decisiones

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **Lección 14.09**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Demostrar reconstrucción y explicar decisiones, evidencia y límites |
| **Necesitas** | 14.01–14.07, Quarto y una aplicación elegida: Streamlit o Shiny |
| **Evidencia** | Revisión por casos, decisión argumentada y acta con pendientes reales |

[**Hacer el lab 14.09 →**](../../../labs/14_reproducible_projects/09_final_review_defense/README.md) · [Recorridos completos](recorridos.md)

## Propósito

Llegamos al cierre del material del recorrido. Ahora una persona debe poder
seguir las instrucciones, reconstruir un producto y explicar por qué sus
resultados son válidos para la pregunta acordada. Una carpeta ordenada o un
HTML que abre ayudan, pero la revisión necesita conectar datos, reglas,
ejecución, presentación y decisiones.

La defensa es una conversación apoyada en evidencia: puedes consultar el
contrato, el código y tus notas. Explicar una duda o un límite permite decidir
qué falta comprobar. No hace falta aparentar certeza ni memorizar comandos.

Esta sección cierra la **base de lecciones y labs**. Desarrollar ese material
no completa por sí solo la práctica del estudiante, los proyectos de projects/
ni sus checkpoints. La depuración transversal y las sesiones con personas que
aprenden continúan después de este cierre editorial.

## Antes de empezar

Revisa [14.01 — Contrato](../01_product_question_contract/README.md),
[14.05 — Pruebas](../05_tests_data_quality/README.md),
[14.06 — Recuperación](../06_traceability_recovery/README.md) y
[14.07 — Integración](../07_report_app_integration/README.md).
Elige **una** ruta. Quien trabaja con R usa el IDE y consola R como recorrido
principal; las terminales son alternativas explícitas.

No se exigen entregas personales anteriores. El preparador de 14.07 reúne las
53 fuentes de referencia en otra carpeta; aquí se reutilizan sin cambiar modelos,
datos ni lockfiles. [14.08](../08_delivery_optional_automation/README.md) permite
ampliar con paquete y revisor externo, pero no bloquea este cierre.
No se añaden dependencias ni se requiere CI, despliegue o un segundo lenguaje.

## Qué vas a aprender

- Separar predicción, ejecución observada y explicación del resultado.
- Reconstruir desde fuentes y metadatos, sin copiar una biblioteca instalada.
- Conciliar filas, unidades y denominadores entre cálculo, reporte y app.
- Mostrar un control que detecte una falla y conservar su diagnóstico.
- Defender una decisión considerando alternativas, consecuencias y límites.
- Emitir un acta que distinga lo demostrado de lo pendiente.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Recorridos](recorridos.md) | Preparación nueva y ejecución completa por ruta | Elegir uno |
| [Registro de revisión](plantillas/REVISION.md) | Relacionar predicción, observación y evidencia | Copia personal |
| [Registro de decisiones](plantillas/DECISIONES.md) | Argumentar una elección y cuándo revisarla | Copia personal |
| [Acta de cierre](plantillas/ACTA_CIERRE.md) | Declarar resultado de la revisión y pendientes | Completar al final |
| [Preparador Python](../07_report_app_integration/preparar.py) / [R](../07_report_app_integration/preparar.R) | Reunir las mismas 53 fuentes verificadas | Sin instalar al copiar |
| [Contrato](../01_product_question_contract/ESPECIFICACION.md) y [CSV externo](../01_product_question_contract/cartera.csv) | Contrastar reglas y los seis registros de referencia | Mantener originales |
| [Estado y reanudación del módulo](../../../docs/reproducible-projects-closure.md) | Distinguir material disponible y trabajo posterior | Consulta |

## 1. Un ejemplo mínimo: un número correcto puede estar mal explicado

Supón un corte con tres créditos: A/0, B/2000 y C/2500 MXN. La regla es saldo
mayor o igual a 2000. Se seleccionan B y C: dos créditos, 4500 MXN y cobertura
de créditos 2/3, aproximadamente 66.67%.

El saldo seleccionado también representa 100% del saldo del corte: el crédito
excluido tiene saldo cero. Ambos porcentajes son aritméticamente posibles,
pero contestan preguntas diferentes. Nuestro contrato pide **cobertura de
créditos**, no proporción del saldo. Ver 4500 en dos pantallas no resuelve esa
diferencia; hay que leer unidades, población y denominador.

Predice qué ocurre si la regla cambia de `>=` a `>`: B deja de cumplir, queda
C/2500 y la cobertura baja a 1/3. La frontera de 2000 permite detectar el cambio.
Una prueba que solo usa octubre podría no detectarlo, porque allí ningún saldo
es exactamente 2000. Por eso se revisan varios casos y sus detalles.

## 2. Qué significa reconstruir en este cierre

Reconstruir es preparar fuentes en una carpeta nueva, restaurar los entornos
locales declarados y volver a producir resultados. Se conserva la carpeta de
origen, pero no se trasladan su .venv, renv/library, salidas, reportes ni cachés
como sustituto de la ejecución nueva. Una caché de instaladores puede servir
para restaurar; no equivale a copiar una biblioteca instalada.

El [recorrido](recorridos.md) empieza con una copia nueva de las fuentes, ejecuta
siete grupos de pruebas, traza tres consultas y genera/renderiza tres reportes.
Después restaura la interfaz elegida y permite observarla. Hay dos entornos
separados: cálculo y aplicación. Quarto es una instalación existente y explícita.
Los lockfiles no contienen el sistema operativo ni garantizan descargas futuras.

Repetir en otra carpeta del mismo equipo comprueba independencia de esa carpeta;
no demuestra por sí solo ejecución en Linux, otro equipo ni ausencia de toda
dependencia externa. Una revisión acompañada tampoco equivale a autonomía sin
ayuda: registra el tipo de ayuda que necesitaste.

## 3. Revisar un caso de punta a punta

La referencia completa tiene seis registros sintéticos, tres créditos por
fecha. ID como texto de tres dígitos, clave ID/corte, segmentos comercio y
servicios, saldos enteros MXN, fechas válidas y sin ausencias. En septiembre:
001/0, 002/2000 y 003/2500; en octubre: 001/100, 002/1900 y 003/2600.
Se valida toda la fuente antes de seleccionar, incluso otros cortes.

| Caso | Parámetros | Selección esperada | Universo y cobertura |
| --- | --- | --- | --- |
| Octubre | Ambos segmentos, mínimo 2000 | 003/2600 MXN | 3 créditos, 4600 MXN; 1/3 |
| Septiembre | Ambos segmentos, mínimo 2000 | 002/2000 y 003/2500 MXN | 3 créditos, 4500 MXN; 2/3 |
| Vacío | Octubre, servicios, mínimo 1901 | Ninguno; saldo 0 MXN | 3 créditos, 4600 MXN; 0% |
| Sin universo | Noviembre, ambos, mínimo 2000 | Sin resultado nuevo válido | No hay créditos en ese corte; cobertura no publicable |

Los tres primeros tienen entregas y reportes; el cuarto se demuestra en la app
y mediante las pruebas de rechazo. Un vacío válido y un corte sin universo
requieren mensajes distintos. No convertir ausencia de población en una cifra cero.

Para cada caso, quien revisa pide localizar:

1. El CSV fuente y el contrato que definen la unidad y la clave.
2. El archivo config del caso y sus filtros efectivos.
3. Selección por crédito, contexto, insumos y marca de la entrega.
4. El intento trazado y el diagnóstico de sus etapas.
5. Las tablas, el .qmd preparado y el HTML del reporte.
6. El caso aplicado en la app, distinguido de un borrador sin aplicar.

Compara primero claves/campos y después totales. Sumar saldos de fechas distintas
mezclaría observaciones de un mismo crédito; no es el saldo de una fecha única.
Las cantidades, IDs, fechas y pesos enteros coinciden exactamente. Para las
representaciones numéricas de cobertura se conserva la tolerancia de 1e-10
puntos porcentuales; el texto visible puede redondear a dos decimales.

## 4. Mostrar una falla detectada

En los [recorridos](recorridos.md) se copia el reporte de octubre a
reportes/ensayo_saldo, un destino nuevo. Solo allí se cambia 003/2600 por
003/2700 en seleccion.csv. El verificador debe rechazar **esa tabla distinta de
la entrega**; el reporte original debe seguir aprobando.

No cuentes un error de ruta, entorno o sintaxis como detección del importe:
comprueba que el diagnóstico corresponde a la alteración. Conserva la copia
fallida. Recuperar esta demostración consiste en volver al reporte original
verificado, sin borrar el ensayo ni sobrescribirlo como si nunca hubiera fallado.

Esto muestra un control concreto. No demuestra que todas las fallas posibles
se detecten. Si dos saldos cambian compensando la suma, la comparación por fila
con referencia externa sigue siendo necesaria; las huellas no autentican datos.
En la ampliación de 14.08 esa comparación externa está automatizada. En esta
ruta esencial, quien revisa contrasta las seis filas con el CSV externo y deja
constancia de ello: los verificadores de 14.07 contrastan con la fuente actual
del proyecto, y no sustituyen ese contraste independiente.

## 5. Observar el producto y explicar sus tiempos

Abre los tres HTML nuevos y la app local elegida. Comprueba tablas, etiquetas,
barras y denominadores. Al seleccionar otro caso sin pulsar Comprobar entrega,
la vista aplicada anterior sigue identificada y aparece el aviso de borrador.
Al aplicar el vacío hay contexto, pero ninguna barra. Al aplicar Sin universo
se retiran las cifras y se muestra rechazo. Otra sesión empieza sin consulta.

El corte describe los datos. La hora UTC registra una comprobación. El HTML
es una fotografía preparada; renderizar transforma el .qmd, no vuelve a calcular
la consulta. La app comprueba al pulsar y no vigila cambios de disco por sí sola.
No hay sincronización automática entre el HTML histórico y la app actual.
Explica qué repetirías si cambian datos, configuración o código: entrega y reporte
nuevos con evidencia propia, conservando los anteriores.

## 6. Defender decisiones con una razón comprobable

Una decisión se entiende mejor al enlazar **necesidad → alternativas → elección
→ evidencia → consecuencias**. La [plantilla](plantillas/DECISIONES.md) adapta
esa estructura al tamaño de esta práctica; no requiere un documento extenso.

Ejemplo de argumento acotado:

> Necesitamos revisar seis registros en un equipo local. Elegimos el cálculo
> estándar de Python y Streamlit porque podemos ejecutar sus pruebas y mantener
> el cálculo fuera de la interfaz. R/Shiny sería una alternativa válida si el
> equipo trabaja principalmente en R. No medimos rendimiento comparativo aquí;
> no afirmamos que una opción sea más rápida. Revisaríamos la elección al cambiar
> público, volumen, restricciones de despliegue o mantenimiento.

Explica además por qué el CSV pequeño conserva IDs textuales y saldos enteros,
por qué validar antes de filtrar y por qué compartir reglas entre reporte y app.
Relaciona con [formatos](../../09_arrow_parquet/README.md) y
[motores](../../10_polars_duckdb/README.md) sin convertir sus prácticas en un
benchmark de este producto.

Estas son preguntas útiles para la conversación:

| Pregunta de quien revisa | Evidencia que ayuda a contestar |
| --- | --- |
| ¿Qué significa exactamente un registro? | Clave, fecha, diccionario y CSV |
| ¿Por qué septiembre incluye 002? | Frontera de 2000 y comparación `>=` |
| ¿De dónde sale la cobertura? | Cantidad seleccionada / créditos del corte |
| ¿Cómo sabes que no reutilizaste resultados viejos? | Destino nuevo, comandos y archivos producidos |
| ¿Qué falla mostraste y cómo la recuperaste? | Ensayo separado, diagnóstico y original verificado |
| ¿Qué no puedes afirmar? | Alcance del entorno, pruebas, referencia y observación humana |
| ¿Qué harías si el proyecto crece? | Condición de revisión de la decisión y mediciones necesarias |

## 7. Emitir un acta honesta

El [acta](plantillas/ACTA_CIERRE.md) reúne revisión, decisiones y pendientes.
Cada punto queda **observado**, **falló**, **pendiente** o **no aplica con motivo**.
Solo marca observado cuando puedas señalar evidencia y explicar la comparación.
No uses no aplica para omitir reconstrucción, casos o defensa esenciales.

Puede quedar «demostración del cierre esencial realizada en el alcance descrito»
cuando todos sus puntos esenciales estén observados. Si algo falla o falta,
declara «cierre pendiente» y anota el próximo paso. No se calcula una nota global
ni se emite automáticamente una certificación de aprendizaje. El acta tiene
responsables, fecha, ayudas y evidencia: una casilla marcada no prueba una sesión
histórica ni sustituye la revisión de otra persona.

## Práctica, evidencia y criterio de salida

Realiza el [lab 14.09](../../../labs/14_reproducible_projects/09_final_review_defense/README.md).
Conserva fuentes originales, copia reconstruida, versiones/comandos, pruebas,
tres consultas y reportes, ensayo rechazado y las tres notas personales.
Quien acompaña debe poder elegir un caso, seguir su dato por las capas y pedir
una justificación. Un pendiente debe tener siguiente acción y comprobación esperada.

La evidencia personal se guarda en tu copia. PROGRESS.md registra desarrollo
del material, no tu aprendizaje. CI, despliegue y paquete de 14.08 siguen siendo
opcionales; no hay proyectos/checkpoints activados por cerrar esta lección.

## Referencias primarias

- [uv: bloqueo y sincronización](https://docs.astral.sh/uv/concepts/projects/sync/): conservar el lockfile y restaurar el entorno del proyecto.
- [renv: restore](https://pkgs.rstudio.com/renv/reference/restore.html): reconstruir la biblioteca declarada del proyecto.
- [Quarto: gestión de ejecución](https://quarto.org/docs/projects/code-execution.html): distinguir render, ejecución y reutilización de resultados; aquí se renderiza texto preparado.
- [Michael Nygard: Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions): contexto, decisión y consecuencias; base para nuestra plantilla breve de argumentación.

## Siguiente paso

Terminaste la última lección de la base del recorrido. Realiza su
[lab](../../../labs/14_reproducible_projects/09_final_review_defense/README.md),
revisa el [cierre y trabajo posterior](../../../docs/reproducible-projects-closure.md)
y acuerda qué depurar o practicar. No hay módulo 15 definido. Consulta
[proyectos](../../../projects/README.md) y [showcase](../../../showcase/README.md)
según su disponibilidad; no los des por implementados ni publiques evidencia
personal sin revisarla. [Volver al módulo](../README.md).

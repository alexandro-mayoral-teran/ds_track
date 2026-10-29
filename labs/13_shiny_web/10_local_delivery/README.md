# Lab 13.10 — Reconstruir y demostrar una entrega Shiny

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.10**

[Volver a la lección](../../../curriculum/13_shiny_web/10_local_delivery/README.md)

## Objetivo y entrada

Entregar un explorador que otra persona pueda reconstruir, comprobar y explicar.
El resultado es una carpeta con fuentes/resultados y evidencia humana separada.
No se publica un servidor ni se implementa el proyecto del módulo 14.

Usa [recorridos](../../../curriculum/13_shiny_web/10_local_delivery/recorridos.md)
para preparar una práctica nueva con sus 24 fuentes. No necesitas entregas
previas. El entorno Shiny/ggplot2 se restaura localmente con el mismo lockfile;
no se añaden paquetes. Conserva originales y elige nombres nuevos en cada fase.

## 1. Predecir qué hace falta

Antes de crear archivos, responde en tu nota personal:

- Si recibes solo seleccion_2026-09-30.csv, ¿puedes reconstruir el universo?
- Si recibes solo app.R, ¿de dónde saldrán datos, funciones y paquetes?
- Si recibes una URL 127.0.0.1, ¿a qué equipo apunta cuando la abres tú?
- ¿Qué demostraría una captura y qué necesitas volver a ejecutar?

Lee LEEME.md, CONTRATO.md y casos.csv en tu práctica. Explica el crédito/corte,
los pesos y la frontera >= antes de mirar cifras calculadas.

## 2. Construir una entrega nueva

Restaura, ejecuta las pruebas de 13.09 y crea/verifica la entrega siguiendo el
recorrido. Predice los seis resultados antes de abrir resumen.csv:

| Caso | Resultado que debes justificar |
| --- | --- |
| septiembre | 002/003; 4500 MXN; 2 de 3 créditos |
| octubre | 003; 2600 MXN; 1 de 3 |
| cero | 001/003; 2500 MXN; 2 de 3 |
| frontera | 003; 2500 MXN; 1 de 3 |
| vacio | Sin IDs; 0 MXN; 0 de 3 |
| sin_universo | Corte sin filas; medidas ausentes y sin exportación de vista |

Comprueba 41 archivos en la entrega base. Revisa cinco selecciones CSV, cinco
contextos y cuatro PNG. Vacío conserva encabezado y una fila de contexto;
noviembre no tiene CSV de vista ni figura. Explica por qué cero/frontera suman
igual y tienen distinta cobertura. Abre las cuatro figuras y contrástalas
con sus tablas; la firma PNG no basta para revisar el contenido.

Revisa que no se copiaron biblioteca, cachés, .RData, tus notas u otros archivos
privados. El constructor copia una lista; vuelve a revisar lo que compartirás
si luego añades archivos manualmente. No edites huellas para ocultar un error.

## 3. Verificar y entender sus límites

Desde la práctica, carga entrega.R y verifica con cartera.csv externo a la
entrega. Conserva el OK o el primer fallo y explica su alcance. No uses como
referencia el mismo CSV que estás verificando.

En **otra copia de la entrega**, cambia el saldo de 002 de 2000 a 2001 y el de
003 de 2500 a 2499 en resultados/septiembre_seleccion.csv. No cambies la fuente.
La suma sigue siendo 4500: predice si el verificador lo aceptará y ejecútalo
desde un entrega.R revisado externo. Debe rechazar los valores por crédito.
Conserva el mensaje y la copia alterada separada; la entrega original permanece
intacta. Esta prueba no requiere actualizar huellas: el contraste de tablas
ocurre antes de revisarlas.

Explica qué pasaría si alguien actualizara también las huellas. ¿Por qué una
referencia externa revisada sigue siendo necesaria? ¿El verificador puede
certificar la lógica de todo código recibido o una demostración pasada?

## 4. Reconstruir en otra carpeta

Usa el bloque de recorridos para copiar únicamente las 24 fuentes declaradas,
incluidos .Rprofile y renv/activate.R/settings.json. No copies biblioteca ni
resultados. Abre el nuevo proyecto, reinicia R y restaura desde su biblioteca
local nueva; ejecuta las pruebas completas.

Crea una entrega recalculada en otro destino nuevo. Verifícala con cartera.csv
de la entrega recibida como referencia externa. No dependas del repositorio
original ni de objetos de la sesión anterior. Compara los seis casos y abre
las cuatro figuras nuevas. No confundas diferencias de bytes de PNG, fuentes o
nota de generación con diferencias de datos: explica lo observado.

Si la restauración falla, conserva diagnóstico/versión y revisa la causa.
No sustituyas el lockfile silenciosamente ni presentes esa fase como comprobada.
Si el destino existe, consérvalo y elige otro; una copia parcial no es nueva.

## 5. Demostrar la app reconstruida

Inicia app.R de la reconstrucción. Una persona ejecuta y explica; la otra revisa:

1. Inicio sin consultas. Aplica septiembre/ambos/2000 en A y octubre/ambos/2000
   en B. Comprueba IDs, saldos, porcentajes, tablas, figuras y lectura del padre.
2. Edita A a otro corte sin aplicar. Explica qué permanece y qué aviso cambia.
   Oculta tabla: la consulta/figura/descargas conservan los datos aplicados.
3. Descarga selección/contexto de A, completando ambas antes de aplicar otra
   consulta. Relee los CSV por crédito; comprueba corte, filtros y universo.
   Son descargas HTTP actuales, distintas de los archivos generados en lote.
4. Aplica comercio/mínimo 0 y después 1. Justifica misma suma, diferente
   cantidad y el crédito cero. Aplica sin segmentos y noviembre: distingue
   selección vacía sobre universo de ausencia de universo.
5. Intenta mínimo 1.5 tras una consulta válida. Explica rechazo con instantánea
   anterior; la validación de fuente tiene otra política, probada en 13.09.
6. Recarga y abre una sesión nueva: ambas comienzan sin aplicadas. Detén tu
   servidor y explica por qué la URL local ya no responde.

No es obligatorio usar los dos paneles como un informe comparativo: cada uno
tiene corte, denominador y escala propios. No sumes sus cifras como si fueran
créditos distintos ni compares alturas sin leer unidades/ejes.

## Ayudas y solución razonada

<details>
<summary>Ver qué cuenta como reconstrucción</summary>

La entrega no lleva paquetes instalados. Debes copiar fuentes a otro destino,
activar/restaurar el entorno local, ejecutar pruebas, recalcular los seis casos
y demostrar la app. La fuente de contraste queda fuera de lo verificado. Una
carpeta con resultados copiados no demuestra que pudiste generarlos de nuevo.

</details>

<details>
<summary>Ver por qué los errores compensados se rechazan</summary>

El contraste externo conserva 002=2000 y 003=2500 en septiembre. La suma de
2001 y 2499 coincide, pero esos valores no coinciden por crédito con la
referencia. El verificador compara columnas/filas antes de huellas; actualizar
MD5 no arreglaría los datos. Una fuente externa también alterada podría debilitar
la comprobación: la confianza depende de qué referencia/código has revisado.

</details>

## Evidencia y criterio de salida

Conserva entrega original, reconstrucción y entrega recalculada. En tu bitácora
personal separada registra entorno real, ejecución completa, seis casos,
error provocado, descargas releídas, capturas/observaciones, ayudas y dudas.
Explica los límites de huellas, registro generado, pruebas simuladas y navegador.

El material de las diez secciones está disponible; practicar este lab y justificar
su resultado requiere tu evidencia. Proyecto/checkpoints siguen pendientes.

## Siguiente paso

Revisa los [criterios de cierre de Shiny](../../../docs/shiny-closure.md).
Después de completar la práctica consulta [14.01 — Pregunta y contrato del producto](../../../curriculum/14_reproducible_projects/01_product_question_contract/README.md),
disponible con lección y lab; 14.02–14.09 también tienen lecciones/labs. La base de material del recorrido está disponible. Streamlit es alternativa, sin exigir otra app completa.

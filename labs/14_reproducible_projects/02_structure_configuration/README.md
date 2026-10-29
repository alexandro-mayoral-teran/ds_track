# Lab 14.02 — Organizar responsabilidades y parámetros

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.02**

[Volver a la lección](../../../curriculum/14_reproducible_projects/02_structure_configuration/README.md)

## Objetivo y entrada

Preparar una copia organizada, cambiar parámetros sin alterar reglas y demostrar
que las rutas se interpretan desde la raíz acordada. Sigue los
[recorridos](../../../curriculum/14_reproducible_projects/02_structure_configuration/recorridos.md).
Recibes trece archivos; elige Python estándar o R base, sin instalar paquetes.
No necesitas una entrega previa ni implementar reporte/app todavía.

## 1. Localizar antes de ejecutar

Lee el LEEME de la copia. Señala sin abrir todas las funciones:

- Dónde está la entrada preservada y cuál es su clave/unidad.
- Dónde se define el significado de los indicadores y sus casos esperados.
- Dónde cambiar corte/segmentos/mínimo y dónde cambiar una regla como >=.
- Dónde deberían quedar resultados regenerables, sin reemplazar la entrada.

Explica por qué referencia/criterios.csv no debe utilizarse como dato para
fabricar el resultado. ¿Qué diferencia hay entre código reutilizable y punto
de entrada? ¿Abrir revisar.py cambia por sí solo la carpeta actual?

## 2. Revisar el caso inicial

Predice octubre/ambos/2000 antes de ejecutar. Comprueba parámetros efectivos,
003/2600 MXN, universo 3/4600 y cobertura 100/3. Verifica que no apareció un
archivo de resultado ni la carpeta salidas/octubre. Explica por qué una ruta
declarada no demuestra una entrega generada.

## 3. Cambiar la pregunta sin cambiar el código

Copia config/consulta.csv como config/septiembre.csv, conservando la inicial.
Cambia corte a 2026-09-30 y salida a salidas/septiembre; predice y revisa.
Comprueba 002=2000 y 003=2500, saldo 4500 y cobertura 2/3.

Ahora cambia app de shiny a streamlit en otra variante: los indicadores deben
permanecer iguales. Explica por qué elegir una ruta no inicia/instala una app.
No sustituyas >= por > para variar una consulta: eso modifica el contrato.

## 4. Ejecutar desde otro lugar

Conserva la raíz absoluta de la copia. Abre otra consola o cambia a otra carpeta;
ejecuta revisar.py por ruta absoluta, o carga revisar.R y pasa la raíz absoluta.
Selecciona config/septiembre.csv y comprueba los mismos valores.

Copia después la práctica completa a otro destino nuevo con espacios en el nombre.
Repite sin modificar rutas dentro del CSV. Identifica qué ruta inicial debes
ajustar para encontrar el punto de entrada, y cuáles siguen siendo relativas
a la raíz del proyecto. No copies únicamente revisar.py/R.

## 5. Provocar errores que no se oculten

En variantes separadas, predice y provoca al menos tres de estos casos:

| Cambio | Qué debe pasar |
| --- | --- |
| Clave minimo_texto ausente o repetida | Rechazo de configuración |
| Clave desconocida | Rechazo, sin ignorarla |
| minimo_texto=2000.0 o 01 | Rechazo sin truncar/normalizar |
| version_reglas desconocida | Rechazo, sin fingir otro contrato |
| entrada=../cartera.csv | Rechazo de ruta |
| salida=datos/entrada/cartera.csv | Rechazo antes de cualquier escritura |
| Destino de salida ya ocupado | Rechazo; conserva esa carpeta/archivo |

Para el último caso, usa únicamente una carpeta de práctica tuya y crea allí el
destino previsto; no borres ni reemplaces trabajo previo para hacer pasar la
revisión. Elige otro nombre de salida después y conserva el diagnóstico.

Como contraste de datos, duplica una fila de octubre en una copia de la fuente,
apunta una variante de entrada a ese CSV y solicita septiembre. Debe fallar por
la fuente completa antes del filtro. No alteres el original del repositorio.

## Ayudas y solución razonada

<details>
<summary>Ver por qué la carpeta actual no cambia el resultado</summary>

Python ancla la raíz al archivo revisar.py; R recibe la raíz explícitamente.
Ambos resuelven config/ y datos/entrada desde esa raíz. La ruta para encontrar
el script puede ser distinta en la nueva consola, pero los valores dentro de
la configuración no se reinterpretan desde ella. Una ruta relativa no es
portable si no acuerdas su punto de partida.

</details>

<details>
<summary>Ver configuración frente a reglas y productos</summary>

Cambiar octubre por septiembre modifica una consulta y conserva la regla >=
y el denominador del corte. Cambiar >= por > exige revisar versión/contrato y
criterios. El código muestra la alternativa de app elegida, pero no la arranca.
salidas/septiembre es solo un destino previsto: la revisión no crea ni reserva
esa carpeta y no demuestra un pipeline de reprocesamiento.

</details>

## Evidencia y criterio de salida

Conserva configuraciones, predicciones/resultados por crédito, diagnósticos y
una nota de ejecución desde otra carpeta/copia movida. Explica responsabilidades,
raíz frente a directorio actual, parámetros frente a reglas y qué falta para
producir resultados reconstruibles. No marques integraciones/checkpoints como listos.

## Siguiente paso

Continúa con [14.03 — Entornos y ejecución reconstruible](../../../curriculum/14_reproducible_projects/03_reconstructible_environments/README.md),
disponible con lección y lab. El producto integrado sigue pendiente.

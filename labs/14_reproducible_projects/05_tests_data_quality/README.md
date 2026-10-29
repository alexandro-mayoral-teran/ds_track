# Lab 14.05 — Detectar fallas antes de entregar

[Volver a la lección](../../../curriculum/14_reproducible_projects/05_tests_data_quality/README.md) · [Módulo 14](../../../curriculum/14_reproducible_projects/README.md)

## Propósito, entrada y preparación

Demostrar que una prueba protege una regla concreta y detectar un defecto
introducido deliberadamente. Recibes seis filas sintéticas, nueve criterios
literales, catorce casos inválidos y suites Python/R de siete grupos.
No hay proyecto asociado ni checkpoint implementado.

Lee la lección y sigue un [recorrido completo](../../../curriculum/14_reproducible_projects/05_tests_data_quality/recorridos.md)
en copia nueva. Elige un lenguaje; no necesitas entregas anteriores ni paquetes nuevos.
Tiempo orientativo: 60–90 minutos, divisible en dos sesiones.

## 1. Predecir antes de ejecutar

Sin llamar al modelo, escribe los IDs y saldos esperados para septiembre,
ambos segmentos, mínimo 2000. Explica si entra el saldo exactamente igual al
mínimo y cuál es el denominador. Después revisa el criterio literal:
002/2000 y 003/2500, universo tres y porcentaje 100 × 2 / 3.

## 2. Ejecutar la suite válida

Restaura y ejecuta según el recorrido. Conserva comando/llamada, versiones y
resumen: siete grupos aprobados. Localiza una fixture inválida, la llamada al
validador y la expectativa de error. Explica por qué el error del CSV inválido
hace **aprobar esa prueba** y no toda la suite automáticamente.

Comprueba también la salida de integración de septiembre/octubre. Las carpetas
terminadas en alterado son ensayos deliberadamente inválidos: no las presentes
como entregas correctas. La fuente inicial debe seguir intacta.

## 3. Introducir y detectar un defecto

Prepara otra copia nueva como indica el recorrido. Conserva respaldo del modelo;
en esa copia cambia solo ≥ por > en el filtro de saldo. Predice qué crédito se
perderá. Guarda y ejecuta la suite: debe fallar por los resultados modificados.

Registra al menos una comparación: esperado 002|003 y obtenido 003 para
septiembre con mínimo 2000. No cambies criterios para acomodar el defecto.
Si el fallo proviene del entorno o de una ruta incorrecta, todavía no demostraste
que la prueba detecta el comparador. Corrige la preparación y repite.

Restaura el modelo desde el respaldo. Ejecuta en un proceso/sesión limpio y
exige nuevamente siete grupos aprobados. Conserva ambas salidas.

## 4. Añadir una prueba con propósito

En esa copia ya restaurada, añade **un caso nuevo**, sin tocar los casos previos:
con segmento servicios en octubre, mínimo 1900 incluye 002/1900; mínimo 1901
produce selección vacía, universo tres y saldo universo 4600.

Aunque esos límites están en criterios.csv, escribir esta prueba pequeña te
permite explicar su preparación, llamada y comparación. Es práctica de autoría,
no una afirmación de cobertura nueva por repetir una condición existente.
En Python usa un método test_* nuevo; en R usa un caso adicional dentro del
ejecutor o un bloque stopifnot tras source del modelo. Distingue el nuevo número
de métodos/grupos de la suite original. Ejecuta y revisa el resultado.

<details>
<summary>Ver una orientación para contrastar tu explicación</summary>

El saldo igual al mínimo cumple ≥. El 002 pertenece a servicios y tiene 1900 en
octubre. Al pedir 1901, deja de estar seleccionado; el universo sigue incluyendo
los tres créditos del corte porque se determina antes de filtrar segmento/saldo.
Si usas la selección como denominador, una prueba de IDs puede pasar mientras
el porcentaje queda mal: agrega una expectativa explícita del universo.

</details>

## 5. Explicar los límites

Elige dos grupos y explica el fallo que detectan. Después da un ejemplo de dato
que podría pasar las reglas de formato y aun ser falso en la realidad. Distingue:

- Fixture aprobada frente a validación del CSV que realmente vas a entregar.
- Código de salida esperado de una prueba negativa frente a una suite fallida.
- Suma correcta frente a valores correctos por crédito.
- Siete grupos aprobados frente a cobertura completa o aprendizaje demostrado.

## Evidencia y criterio de salida

Guarda nota con pregunta/regla, comandos y versiones, resumen inicial aprobado,
defecto introducido, falla correspondiente y aprobación tras restaurar. Añade tu
caso nuevo y una explicación de su resultado. No es necesario publicar todas las
fixtures ni rutas de tu equipo. La persona que acompaña debe poder reconstruir
qué cambió y por qué la prueba lo detectó.

Siguiente lección: [14.06 — Trazabilidad y recuperación de fallas](../../../curriculum/14_reproducible_projects/README.md#06-trazabilidad-y-recuperacion-de-fallas),
aún planificada. Vuelve a la [lección](../../../curriculum/14_reproducible_projects/05_tests_data_quality/README.md) para repasar.

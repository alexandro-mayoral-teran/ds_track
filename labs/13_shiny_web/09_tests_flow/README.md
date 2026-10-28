# Lab 13.09 — Pruebas y observación del flujo

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.09**

[Volver a la lección](../../../curriculum/13_shiny_web/09_tests_flow/README.md)

## Objetivo y entrada

Comprobar resultados y transiciones de una app; provocar una salida antigua,
encontrar qué expectativa falla y corregir su dependencia. Trabaja en una copia
nueva preparada según [recorridos](../../../curriculum/13_shiny_web/09_tests_flow/recorridos.md).
No necesitas una entrega anterior ni instalar paquetes adicionales.

La copia contiene el mínimo número/doble/nota, las funciones de cartera, la
app modular de 13.08, tres archivos de pruebas y su ejecutor. Conserva los
originales del repositorio. Primero predice en una nota personal, después ejecuta.

## 1. Predecir y observar el mínimo

Inicia minimo.R desde tu consola R siguiendo el recorrido. Anota qué esperas
para 3, después 7 y finalmente 0. Edita la nota entre los dos últimos cambios.

- Compara doble, texto de la salida y mensaje de cálculo de la consola.
- Explica por qué la nota tiene otra dependencia y no debe recalcular el doble.
- Detén el servidor. En una sesión R nueva, desde la copia, ejecuta
  `source("ejecutar_pruebas.R")` y busca el OK final del conjunto.

Resultado conocido: 6 → 14 → 0; la nota cambia solo su eco. La prueba no abre
la UI: haberla visto antes ayuda a entender qué representa cada entrada simulada.

## 2. Provocar una regresión y leer el fallo

En **tu copia** de minimo.R, cambia únicamente esta línea:

```r
output$resultado <- renderText({ paste0("Doble: ", doble(), ".") })
```

por:

```r
output$resultado <- renderText({ paste0("Doble: ", isolate(doble()), ".") })
```

Antes de ejecutar, escribe si fallará el cálculo, el texto o ambos. Guarda,
reinicia R y ejecuta el conjunto. Conserva el primer mensaje de fallo y el
paso en que apareció; no cambies la expectativa 14 para acomodar el error.

Abre pruebas_minimo.R: comprueba que se demanda primero el cálculo y después
el texto. Explica por qué comprobar solo doble no detectaría este problema.
Restaura la línea original, reinicia R y ejecuta todo hasta el OK final.
Opcionalmente mira el mínimo defectuoso en navegador antes de restaurarlo.

## 3. Leer pruebas de funciones y añadir una frontera

En pruebas_funciones.R localiza fuente literal, casos, porcentajes, exportaciones
y rechazos. Sin llamar a la función que estás probando, justifica:

| Caso | IDs | Saldo | Universo |
| --- | --- | ---: | ---: |
| Septiembre, ambos, mínimo 2000 | 002, 003 | 4500 | 3 |
| Octubre, ambos, mínimo 2000 | 003 | 2600 | 3 |
| Octubre, servicios, mínimo 1901 | Ninguno | 0 | 3 |

Añade a la lista casos de tu copia una frontera **septiembre, servicios,
mínimo 2001**. Escribe primero sus IDs, saldos, suma y porcentaje esperados.
Reejecuta. Compara con mínimo 2000: ¿por qué se excluye 002?

Explica por qué el cero de 001 conserva un crédito, mientras que una selección
vacía conserva cero créditos. Noviembre no tiene universo y no permite exportar:
¿por qué su porcentaje es ausente en vez de 0%?

Los CSV de estas pruebas se escriben y releen en rutas temporales propias.
No los presentes como descargas reales del navegador.

## 4. Comprobar secuencias, no solo estados aislados

En pruebas_servidor.R señala dónde ocurre cada transición:

| Secuencia | Resultado esperado |
| --- | --- |
| Iniciar | Ninguna consulta aplicada |
| Aplicar septiembre/ambos/2000 | 002, 003; 4500 MXN |
| Editar octubre sin aplicar | Sigue septiembre; aviso de pendiente |
| Aplicar octubre | 003; 2600 MXN |
| Intentar mínimo 1.5 | Rechazo; conserva la consulta anterior |
| Aplicar sin segmentos | Vacío con universo, saldo 0 y cobertura 0% |
| Aplicar noviembre | Sin universo; porcentaje ausente |
| Duplicado de octubre y pedir septiembre | Fuente bloqueada, retira consulta |
| Restaurar fuente y aplicar | Recuperación explícita |

Predice el efecto de enviar el primer clic en la misma primera setInputs que
inicializa el servidor con ignoreInit. Explica por qué el material separa el
cero inicial y el primer clic. ¿La simulación lee los valores iniciales de la UI?

## 5. Complementar con el navegador real

Con la fuente original y el mínimo corregido, inicia app.R. Realiza esta lista
en tu copia y conserva una captura o nota de resultados:

1. Verifica que A y B empiezan sin consulta aplicada. Aplica septiembre/ambos/2000
   en A y octubre/ambos/2000 en B. Deben mostrar 4500 y 2600 MXN; el padre
   identifica cada selección.
2. Edita A a octubre sin aplicar. A conserva septiembre, B conserva octubre.
   Oculta la tabla de A: gráfica y consulta conservan los datos aplicados.
3. Descarga selección y contexto de A antes de cambiar su consulta. Abre o
   relee ambos como CSV: IDs textuales 002/003, 4500 MXN, corte septiembre,
   universo 3, selección 2 y porcentaje 100 × 2/3. No uses el borrador de octubre.
4. Aplica comercio/mínimo 0 en A: 001 y 003, con saldos 0/2500. Después aplica
   sin segmentos: selección vacía, gráfica sin barras inventadas y CSV selección
   con encabezado; contexto con una fila de ceros sobre universo 3.
5. Revisa rechazo 1.5 y corte noviembre; en este último no debe ofrecer descargas.
   B sigue independiente. Recarga la página y comprueba que las consultas se
   pierden. Una sesión nueva también empieza sin aplicadas.

Detén tu servidor. No cierres procesos ajenos. Esta lista comprueba conexión,
descarga real y dibujo; los controles testServer no sustituyen esa evidencia.

## Ayudas y solución razonada

<details>
<summary>Ver cómo localizar la regresión</summary>

La expectativa del cálculo 14 pasa. La siguiente, **Texto actualizado**, falla:
renderText leyó doble mediante isolate y no se vinculó a sus cambios. Retira
solo ese isolate de la salida, guarda, reinicia R y repite el conjunto. No cambies
la función de doblar ni el valor esperado. Una app de borrador/aplicada puede
conservar valores intencionalmente; el mínimo actualiza inmediatamente.

</details>

<details>
<summary>Ver la frontera adicional y los denominadores</summary>

La fila añadida es:

```r
list("2026-09-30", "servicios", "2001", character(), numeric(), 0)
```

Pon una coma entre los elementos de la lista; no después del último. 002 tiene
2000 y no cumple >= 2001. El universo sigue siendo tres, por eso la cobertura
es 0/3 = 0%. Noviembre tiene denominador cero: el porcentaje no se define.
Comparar únicamente las sumas de comercio/mínimos 0 y 1 ocultaría el cambio
de cantidad: 001 aporta cero y sigue siendo un crédito conocido.

</details>

## Evidencia y reflexión

Conserva en tu bitácora personal predicciones, ejecución completa, mensaje de
la regresión, corrección y frontera añadida, más evidencia de navegador/CSV.
Explica una cosa que prueba cada capa y una que no puede probar. No marques
todo el módulo completado por ver un OK: faltan la entrega y su reconstrucción.

## Siguiente paso

Continúa con [13.10 — Cierre y entrega local](../../../curriculum/13_shiny_web/10_local_delivery/README.md),
disponible con lección y lab. El proyecto y sus checkpoints siguen pendientes.

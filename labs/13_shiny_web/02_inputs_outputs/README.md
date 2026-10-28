# Lab 13.02 — Conectar una elección con texto y tabla

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.02**

| Tu práctica | Qué debes producir |
| --- | --- |
| **Meta** | Explicar las conexiones de entradas/salidas y comprobar las cinco consultas |
| **Necesitas** | [Lección 13.02](../../../curriculum/13_shiny_web/02_inputs_outputs/README.md) y proyecto Shiny local |
| **Evidencia** | Predicciones por venta, observaciones y variantes de etiqueta/valor inicial |

## Antes de empezar

Sigue los [recorridos](../../../curriculum/13_shiny_web/02_inputs_outputs/recorridos.md)
en el IDE de R elegido. El preparador crea una carpeta nueva sin exigir salidas
anteriores; reutiliza los metadatos de 13.01 y restaura una biblioteca local.
No cambia la muestra previa ni instala dependencias nuevas. La terminal es
opcional y no constituye otro recorrido que debas completar.

## Entradas y resultado esperado

El mínimo recibe texto. La app recibe una clave de venta o `todas` y un valor
lógico para mostrar el detalle. Conserva cuatro ventas ficticias:

| Venta | Unidades | Precio MXN | Importe MXN |
| --- | ---: | ---: | ---: |
| V001 | 4 | 75 | 300 |
| V002 | 2 | 120 | 240 |
| V003 | 0 | 50 | 0 |
| V004 | 3 | 40 | 120 |

Una fila por venta, claves distintas e importes conocidos calculados como
unidades por precio. Esperas cuatro filas/660 para todas; una fila y su importe
para cada clave. V003 conserva una fila aunque el importe sea cero.

## Actividades

1. **Predice antes de ejecutar.** Escribe para las cinco opciones el valor que
   recibirá R, cantidad de filas e importe. Para `todas` anota además los cuatro
   registros completos. Distingue etiqueta del menú y clave recibida.
2. **Prueba el mínimo.** Prepara/restaura tu copia y abre minimo.R. Cambia el
   texto a «Otra nota», vacíalo y escribe `<b>ventas</b>`. Comprueba la salida,
   incluida la presentación literal de esos caracteres. Señala mensaje/eco en
   la UI y sus conexiones dentro de server.
3. **Comprueba la app.** Detén el mínimo e inicia app.R. Recorre todas/V001/V002/
   V003/V004. Contrasta el resumen con tu predicción y los cuatro campos de la
   tabla con los datos. Explica por qué no hay botón de envío.
4. **Separa visibilidad y consulta.** Con V003 seleccionada, oculta el detalle.
   Anota qué desaparece y qué conserva el resumen. Recupera la tabla y después
   elige V002 mientras está oculta: al mostrarla deben aparecer V002/2/120/240.
5. **Cambia una etiqueta.** En tu copia, sustituye «Todas las ventas» por
   «Conjunto completo» conservando su valor `todas`. Detén, guarda y reinicia la
   sesión R. La etiqueta cambia; consultar ese conjunto sigue devolviendo
   cuatro filas/660 y valor recibido `todas`.
6. **Cambia el valor inicial.** Cambia solo `selected` de `todas` a `V004`.
   Reconstruye desde una sesión nueva: al abrir debe verse V004, una fila y
   120 MXN. Elige otra venta, recarga y comprueba que vuelve al inicio V004.
   No cambies datos o cálculo para conseguir ese resultado.
7. **Revisa conexiones con tu compañero.** Señala los tres tipos de entrada y
   las dos parejas de salida. Tu compañero elige un control para manejarlo con
   teclado, propone otra consulta y te pide explicar ID, etiqueta, valor y tipo.
   Repite la lectura en una ventana estrecha y registra problemas o límites.

Puedes pausar después del paso 4. Detén tu servidor y guarda carpeta, resultados
y siguiente paso. No prepares encima de tu copia; para una referencia nueva,
elige otro destino.

## Comprobación

| Caso | Resultado exigido |
| --- | --- |
| Mínimo con texto ordinario/vacío | Prefijo y texto recibido; vacío no se convierte en cero |
| Mínimo con `<b>ventas</b>` | Caracteres literales, sin HTML añadido a la página |
| Todas | Cuatro filas; importes 300/240/0/120 y suma 660 MXN |
| V003 | Una fila V003/0/50/0 y resumen de una venta/0 MXN |
| Ocultar, cambiar a V002 y recuperar | Resumen de V002/240 aun sin tabla; al recuperar, misma fila completa |
| Etiqueta global cambiada | Valor `todas`, cuatro filas/660, datos intactos |
| Nuevo inicio V004 | Una fila/120, detalle marcado; recarga vuelve a ese valor inicial |

No aceptes solo un total correcto: si V001 y V002 intercambian importes la suma
permanece en 660, pero las filas son incorrectas. Los controles de autoría de
esta sección son opcionales y no sustituyen las acciones reales en navegador.

<details>
<summary><strong>Pista: escribe las conexiones antes de editar</strong></summary>

`selectInput("venta_elegida", ...)` conecta con `input$venta_elegida`.
`checkboxInput("mostrar_detalle", ...)` conecta con un valor lógico.
La etiqueta visible es una explicación para la persona; `selected` elige un
valor de choices. Escribe las parejas textOutput/renderText y tableOutput/
renderTable con el mismo ID de salida y localízalas en la app.

</details>

<details>
<summary><strong>Solución razonada: cambiar presentación e inicio</strong></summary>

La tabla de consulta es:

| Valor recibido | Filas | Importe MXN |
| --- | ---: | ---: |
| todas | 4 | 660 |
| V001 | 1 | 300 |
| V002 | 1 | 240 |
| V003 | 1 | 0 |
| V004 | 1 | 120 |

Para cambiar la etiqueta conservando los datos, edita solo el nombre de la
opción global:

```r
opciones_venta <- c("Conjunto completo" = "todas",
                    setNames(ventas$venta_id, ventas$venta_id))
```

El servidor sigue recibiendo `todas`, porque el valor a la derecha no cambió.
Para cambiar el inicio, modifica el argumento del selector:

```r
selected = "V004"
```

Ambas modificaciones pertenecen a la UI. La muestra y consultar_venta no cambian.
Al iniciar una nueva sesión, V004 tiene tres unidades, precio 40 e importe 120.
Recargar crea otra sesión con el valor inicial; no es almacenamiento de una
elección anterior.

La casilla controla la tabla, no la consulta. Desmarcarla no elimina V003 ni
transforma su cero en dato faltante. Cambiar a V002 mientras el detalle está
oculto actualiza el resumen y, al recuperarlo, muestra la consulta vigente.

</details>

## Evidencia y reflexión

Conserva los scripts de tu copia, predicciones de las cinco consultas,
observaciones del mínimo y las dos variantes. En tu nota personal registra
entorno, navegador/ancho, acciones con teclado, comprobaciones por venta,
ayudas recibidas, dudas y siguiente paso.

- ¿Por qué cambiar una etiqueta no requiere cambiar el valor recibido?
- ¿Qué distingue el texto `"TRUE"` de un verdadero lógico de la casilla?
- ¿Por qué una fila/0 MXN no es una selección sin registros?
- ¿Qué ocurre con el detalle si cambias la selección mientras está oculto?
- ¿Qué dos cosas deben coincidir para conectar una salida con su lugar en UI?

No hay proyecto integrador ni checkpoints implementados por este lab.
PROGRESS.md registra autoría, no tus respuestas ni aprendizaje.

## Siguiente paso

Revisa el [criterio de salida](../../../curriculum/13_shiny_web/02_inputs_outputs/README.md#evidencia-y-criterio-de-salida)
y consulta [13.03 — Modelo de reactividad](../../../curriculum/13_shiny_web/03_reactivity/README.md),
ya disponible.

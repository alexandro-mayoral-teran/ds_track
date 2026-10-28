# Lab 13.01 — Ubicar, iniciar y reconstruir la primera app

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.01**

| Tu práctica | Qué debes producir |
| --- | --- |
| **Meta** | Explicar navegador/UI/servidor y comprobar una variante de ventas |
| **Necesitas** | [Lección 13.01](../../../curriculum/13_shiny_web/01_web_first_app/README.md), R y proyecto local |
| **Evidencia** | Código, cálculos por venta y observaciones de arranque/sesiones/reinicio |

## Antes de empezar

Sigue los [recorridos](../../../curriculum/13_shiny_web/01_web_first_app/recorridos.md)
en RStudio o tu IDE de R. Basta un recorrido; la terminal es opcional. No necesitas
haber realizado Streamlit ni conservar entregas previas. Trabaja en una carpeta
nueva; no modifiques las fuentes del curso ni instales en bibliotecas globales.

## Entradas y resultado esperado

Recibes minimo.R, app.R, metadatos reales de renv y scripts de preparación/
restauración/arranque. app.R incluye cuatro ventas ficticias completas:

| Venta | Unidades | Precio unitario MXN | Importe MXN |
| --- | ---: | ---: | ---: |
| V001 | 4 | 75 | 300 |
| V002 | 2 | 120 | 240 |
| V003 | 0 | 50 | 0 |
| V004 | 3 | 40 | 120 |

Una fila es una venta; claves distintas y valores conocidos. La regla es
unidades por precio. No hay ausencias ni filtros: V003 se conserva aunque su
importe sea cero. Esperas cuatro filas y 660 MXN; cambiar V004 a precio 50
produce importe 150 y total 690 sin alterar las otras tres ventas.

## Actividades

1. **Predice y prepara.** Calcula los importes y total en una nota antes de
   ejecutar. Prepara una copia nueva, abre su proyecto, reinicia R y restaura
   las dependencias locales. Registra versión R/Shiny y biblioteca utilizada.
2. **Reconoce el mínimo.** Abre minimo.R y señala ui, server y shinyApp.
   Inícialo con el iniciador. Identifica proceso R, navegador y URL local.
   Explica por qué la consola está ocupada y detén la app hasta recuperar `>`.
3. **Contrasta ventas.** Inicia app.R. Compara cada una de las cuatro filas y
   el texto 660 con tu cálculo. Señala los dos IDs de salida y sus parejas
   textOutput/renderText y tableOutput/renderTable. No añadas controles todavía.
4. **Observa otra sesión.** Conecta otra pestaña a la misma URL sin editar el
   archivo. Observa los mensajes de preparación/sesión/salida de consola y
   los resultados de ambas páginas. Explica por qué otra sesión no implica
   otro intérprete R. No afirmes que implementaste estado de usuario por esto.
5. **Reconstruye una variante.** Detén la app; cambia el precio de V004 a 50 y
   el título para identificar tu copia. Guarda, reinicia R y arranca de nuevo.
   Comprueba V004/150, V001/300, V002/240, V003/0 y total 690; conserva cuatro filas.
6. **Detén y recupera.** Detén tu servidor. Observa qué conserva la pestaña y
   qué ocurre al recargar. Después reinicia la app desde los archivos guardados.
   Tu compañero elige una fila para contrastarla y te pide explicar las piezas.

Puedes pausar tras el paso 3: detén tu servidor y guarda carpeta, dudas y
próximo paso. Para retomar abre el proyecto, reinicia R y carga iniciar.R;
no prepares encima de esa carpeta ni reinstales si el entorno ya es adecuado.

## Comprobación

| Caso | Resultado que debes demostrar |
| --- | --- |
| Mínimo | Título/párrafo, sin filtros ni resultados de ventas |
| Base | Cuatro filas, importes 300/240/0/120 y total 660 MXN |
| Otra pestaña | Misma app/resultado, nueva conexión observada en consola |
| Variante guardada en sesión nueva | Cuatro filas, importes 300/240/0/150 y total 690 MXN |
| Título cambiado | Presentación identificable; importes determinados por datos/cálculo |
| Servidor detenido y luego reiniciado | Conexión interrumpida y app recuperada desde sus fuentes |

Un total correcto no sustituye comprobar valores por venta. Una captura de 690
tampoco demuestra que el servidor siga activo o que puedas reconstruirlo.
Si ejecutas el control opcional de autoría, recuerda que espera la muestra base:
no debe aprobar la variante 690 con expectativas 660.

<details>
<summary><strong>Pista: sigue cada responsabilidad</strong></summary>

Busca los datos antes de ui y server. El cálculo de importe se aplica a los
vectores de unidades/precio. En la UI se reserva el lugar con un ID; en server
la salida del mismo ID define el cálculo que lo llenará. El iniciador llama
runApp; shinyApp reúne las piezas en un objeto.

</details>

<details>
<summary><strong>Solución razonada: qué cambia y por qué</strong></summary>

En la copia, cambia el último precio:

```r
precio_mxn = c(75L, 120L, 50L, 50L)
```

El último 50 corresponde a V004, que tiene tres unidades. Su importe pasa de
3 × 40 = 120 a 3 × 50 = 150, diferencia 30. El total pasa de 660 a 690.
V003 también tiene precio 50 pero cero unidades: su importe sigue en cero;
no elimines esa fila ni cambies sus unidades para conseguir el total.

El título de h1 identifica la presentación. No interviene en la multiplicación.
Para mostrar el cambio debes guardar e iniciar la copia modificada; reiniciar
la sesión elimina objetos de memoria anteriores y permite reconstruirla.

Cada nueva sesión invoca server y obtiene las salidas. La muestra global de
ventas se consulta sin mutación por sesión; eso no convierte cualquier global
en almacenamiento privado. El modelo de reactividad y el estado se desarrollan
después. En este lab no implementas filtros ni guardas elecciones de usuarios.

</details>

## Evidencia y reflexión

Conserva tu proyecto, variante, cálculos por venta y nota personal: entorno,
predicción, observación de consola, URL temporal usada, arranque/detención,
ayudas, dudas y siguiente paso. Una captura es apoyo opcional, no toda la evidencia.

- ¿Dónde se evalúa sum: navegador o proceso R?
- ¿Qué hace cada una de ui, server y shinyApp?
- ¿Qué diferencia preparar/restaurar/iniciar y qué repetirías al retomar?
- ¿Por qué la página puede conservar texto aunque el servidor esté detenido?
- ¿Qué comprobaste por venta que no demostraría únicamente el total?

Tu compañero plantea una variante y revisa una explicación. No hay proyecto/
checkpoints implementados por esta práctica; PROGRESS.md registra autoría,
no el aprendizaje ni las respuestas de cada participante.

## Siguiente paso

Revisa el [criterio de salida](../../../curriculum/13_shiny_web/01_web_first_app/README.md#evidencia-y-criterio-de-salida)
y continúa después con [13.02 — Entradas y salidas](../../../curriculum/13_shiny_web/02_inputs_outputs/README.md).
13.03–13.06 también están disponibles; 13.07–13.10 conservan su plan.

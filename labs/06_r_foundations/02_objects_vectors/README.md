# Lab 06.02 — Calcular ventas y explicar sus tipos

## Propósito, entradas y resultado

Este lab acompaña [06.02 — Objetos, vectores y tipos](../../../curriculum/06_r_foundations/02_objects_vectors/README.md).
Recibes cuatro ventas ficticias alineadas por posición, el
[script correcto](../../../curriculum/06_r_foundations/02_objects_vectors/ventas_vectores.R)
y [demostraciones de riesgo](../../../curriculum/06_r_foundations/02_objects_vectors/riesgos_vectores.R).
Usa R y sus paquetes incluidos con los recorridos completos de tu shell en la
lección. No necesitas instalaciones, tablas, selección de elementos ni bucles.

Entrega una nota con predicciones, tipos/longitudes, resultados y explicación
de un caso incorrecto. Añade una variante propia reconstruible. Guarda tu práctica
en output con nombres nuevos, conservando los originales y las evidencias de
06.01. No hay proyecto/checkpoint implementado asociado; una sesión puede cubrir
parte del lab.

## A. Predecir longitud, tipo y clase

Antes de ejecutar, predice length, typeof y class para estos objetos:

```r
cantidades <- c(4L, 2L, 0L, 3L)
precios <- c(75, 120, 50, 40)
identificadores <- c("V001", "V002", "V003", "V004")
confirmaciones <- c(TRUE, FALSE, TRUE, TRUE)
```

Consulta cada propiedad con la función correspondiente. Explica por qué precios
se imprime sin decimales y aun así no tiene typeof integer. ¿Qué diferencia hay
entre TRUE y "TRUE"? No es necesario construir todavía condiciones lógicas.

<details>
<summary>Resultados y explicación</summary>

Los cuatro objetos tienen longitud 4. cantidades es integer y clase integer;
precios es double y clase numeric; identificadores es character y clase character;
confirmaciones es logical y clase logical. L declara los literales enteros.
La apariencia de un número impreso no identifica su tipo. TRUE es lógico,
mientras "TRUE" es texto. Cada vector atómico utiliza un tipo común.

</details>

## B. Conciliar el cálculo correcto y conservar cero

Calcula a mano los cuatro importes y el total. Ejecuta ventas_vectores.R en un
proceso nuevo con el recorrido de tu shell. Comprueba importes, total y descuento,
y registra el código de salida junto a la versión de R.

Explica qué cambia al pasar de importe_mxn a sum(importe_mxn) y por qué la venta
de cero unidades debe seguir contándose. No confundas estos datos con la única
venta de 300 MXN de 06.01: aquella es la primera observación de esta muestra.

<details>
<summary>Comprobación</summary>

Los importes son 300, 240, 0 y 120; suman 660 MXN. importe_mxn tiene longitud 4
y su suma longitud 1. El factor 0.9 produce 270, 216, 0 y 108; total 594.
El script termina con código 0. Cero unidades es un valor observado, no falta de
observaciones. No se descarta esa venta para calcular el número de registros.

</details>

## C. Investigar coerción sin perder la entrada

Predice tipo y resultado de c(TRUE, 4L), c(4L, 75) y c(75, "120"). Comprueba
con typeof. Explica si la última mezcla conserva un número y un texto de manera
independiente. En una consola, prueba multiplicar esa mezcla por 2 y conserva el
mensaje de error; no lo añadas al script correcto.

Después convierte c("75", "120", "50", "40") a valores numéricos bajo un nombre
nuevo. Comprueba el tipo resultante y que la entrada original sigue siendo texto.
¿Por qué as.integer(c(75.9, 120.1)) no sería una validación aceptable de precios?

<details>
<summary>Una interpretación razonada</summary>

La primera combinación es integer con valores 1 y 4; la segunda double con 4 y 75;
la tercera character con "75" y "120". Ese vector character no admite la
multiplicación aritmética por 2 y R informa un error. No se convierte solo porque
su contenido parezca numérico.

Una conversión explícita, conservando la entrada, es:

```r
precios_texto <- c("75", "120", "50", "40")
precios_convertidos <- as.numeric(precios_texto)
print(typeof(precios_texto))       # character
print(typeof(precios_convertidos)) # double
print(precios_convertidos)        # 75 120 50 40
```

Esos textos concretos se pueden interpretar; convertirlos no valida por sí solo
la unidad, el signo, el orden ni que sean los precios esperados. as.integer
trunca 75.9 y 120.1 a 75 y 120, sin redondear ni avisar en ese caso. No debes
perder sus decimales para conseguir que un cálculo se ejecute.

</details>

## D. Detectar un resultado incorrecto con código 0

Ejecuta riesgos_vectores.R con el recorrido completo de tu shell. Antes, predice
qué precios utilizará para las posiciones 1–4 cuando solo haya dos precios.
Explica el total observado. Después compara con el caso de tres precios y lee
el aviso. Conserva ambos resultados como demostraciones incorrectas del análisis.

¿Qué diferencia hay entre una regla explícita de factor único y reciclar precios
faltantes? ¿Por qué no basta con mirar el código de salida o esperar que R avise?

<details>
<summary>Comprobación y corrección</summary>

Con dos precios se usan 75, 120, 75, 120: importes 300, 240, 0, 360 y total 900.
No aparece aviso porque la longitud 4 es múltiplo de 2. Con tres precios se usan
75, 120, 50, 75: importes 300, 240, 0, 225 y aviso de reciclaje parcial.
En condiciones normales el archivo puede terminar con código 0 en ambos casos.

La corrección es recuperar los cuatro precios acordados —75, 120, 50, 40— en
el orden de las ventas y recalcular 660. Repetir precios o quitar cantidades
solo para igualar longitudes no recupera datos. Un factor único 0.9 sí representa
una regla compartida para todas las ventas; su longitud uno es deliberada.

</details>

## E. La misma longitud no garantiza correspondencia

Sin cambiar unidades ni identificadores, imagina precios en el orden
c(40, 50, 120, 75). Calcula el total por posición y comprueba si R detecta que
el orden no corresponde a nuestras ventas. Explica qué información necesitas
antes de combinar vectores procedentes de fuentes distintas.

<details>
<summary>Resultado y límite de la operación</summary>

Los importes serían 160, 100, 0 y 225; total 485. Las longitudes coinciden y R
no compara las identidades de ventas: id_venta no participa en esa multiplicación.
La corrección exige conservar o recuperar la correspondencia correcta, no solo
comprobar cuatro elementos. En esta muestra se conoce por construcción; con
fuentes externas se necesitarán claves y reglas de unión cuando estudiemos tablas.

</details>

## F. Variante propia y caso vacío

Copia ventas_vectores.R a output/mi_venta_vectorial.R con tu editor. Cambia solo
el cuarto precio a 60, escribiendo nuevamente el vector completo; selección y
modificación con índices llegarán en 06.03. Actualiza los comentarios de resultados
esperados en tu copia, predice el total y ejecútala desde una sesión nueva.

En la consola prueba length(numeric(0)) y sum(numeric(0)). Explica por qué obtener
una suma cero no demuestra haber observado una venta de cero unidades.

<details>
<summary>Una solución y su interpretación</summary>

Conserva las demás entradas y el diagnóstico del script; las líneas relevantes son:

```r
unidades <- c(4L, 2L, 0L, 3L)
precio_mxn <- c(75, 120, 50, 60)
importe_mxn <- unidades * precio_mxn
print(importe_mxn)      # 300 240 0 180
print(sum(importe_mxn)) # 720
print(sum(importe_mxn * 0.9)) # 648
```

El cuarto importe sube de 120 a 180; el total aumenta 60 MXN. No se cambia a mano
el resultado final para lograr 720. El vector vacío tiene longitud 0 y suma 0;
no contiene una observación. Por eso el conteo acompaña al total en la evidencia.

</details>

## Evidencia, reflexión y continuidad

Conserva predicciones, consultas de tipo/clase/longitud, cálculo de 660, descuento
de 594, demostraciones incorrectas y variante de 720. Anota versión, códigos y
avisos; revisa rutas personales antes de compartirlos.

- ¿Qué cambia al combinar un número con texto dentro de c?
- ¿Qué comprueba length y qué no comprueba sobre las ventas?
- ¿Por qué transformar a integer puede perder información sin avisar?
- ¿Qué distingue total cero observado de ausencia de observaciones?

Puedes cerrar la práctica cuando reconstruyas los resultados y expliques los
errores con tus palabras. Registra evidencia real y dudas en PROGRESS.md;
desarrollar este material no acredita aprendizaje.

Continúa con el [plan 06.03 — Seleccionar elementos](../../../curriculum/06_r_foundations/README.md#03-seleccionar-elementos),
todavía pendiente. Volver a la [lección 06.02](../../../curriculum/06_r_foundations/02_objects_vectors/README.md).

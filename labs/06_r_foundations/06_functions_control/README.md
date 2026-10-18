# Lab 06.06 — Reutilizar cálculos y decidir con cobertura

**Tiempo orientativo:** 75–120 minutos, repartibles entre varias sesiones.

## Propósito, entradas y preparación

Aplica la [lección 06.06](../../../curriculum/06_r_foundations/06_functions_control/README.md).
Necesitas vectores, lógica y tablas de 06.02–06.05. Trabaja con las seis ventas
conocidas y funciones de R base, sin archivos de datos ni paquetes externos.
No hay proyecto/checkpoint implementado asociado.

Primero predice los resultados. Después ejecuta el recorrido completo de la
lección en una sesión nueva. Para desarrollar tu lab, inicia otra sesión y
carga **solo las funciones**, desde la raíz:

```r
source("curriculum/06_r_foundations/06_functions_control/funciones_ventas.R", encoding = "UTF-8")
```

Este archivo define funciones, sin crear ventas ni mostrar resúmenes. Guarda
tu script personal bajo `output/` de este lab, ignorado por Git. Conserva las
fuentes del curso y no copies los errores deliberados al script correcto.

## 1. Identificar entradas, retorno y alcance

Escribe una función `calcular_doble` que reciba `x`, guarde `x * 2` en un
nombre local `valor` y lo devuelva. Antes crea `valor <- 999` fuera. Guarda
el resultado para `x = 150` y preséntalo después de llamar la función.
Explica cuál es el parámetro, cuál es el argumento y por qué el `valor` externo
debe seguir siendo 999. Escribe otra versión con retorno por último valor.

<details>
<summary>Solución razonada: retornar datos sin cambiar el nombre externo</summary>

```r
valor <- 999
calcular_doble <- function(x) {
  valor <- x * 2
  return(valor)
}
resultado_doble <- calcular_doble(x = 150)
cat("Resultado del lab:\n")
print(resultado_doble) # 300
print(valor) # 999
doble_ultimo <- function(x) { x * 2 }
print(doble_ultimo(150)) # 300
```

`x` es el parámetro; `150`, el argumento de esta llamada. La asignación interna
no modifica `valor` externo. Esta función de sintaxis no valida sus entradas;
las funciones del ejercicio de ventas sí tienen un contrato explícito.

</details>

## 2. Calcular y resumir sin depender de una demostración previa

Construye `ventas_lab` con los seis identificadores, unidades y precios de
06.05. Calcula importes con `calcular_importes`, guarda el resumen y luego
muéstralo. No uses `source` sobre `ejecutar_funciones.R` para obtener la tabla:
debe ser una entrada explícita de tu archivo. Comprueba manualmente los
importes, conteos, cobertura, suma y media. ¿Por qué el total completo es `NA`?

<details>
<summary>Solución razonada: funciones reutilizables y presentación aparte</summary>

```r
ventas_lab <- data.frame(
  id_venta = c("V001", "V002", "V003", "V004", "V005", "V006"),
  unidades = c(4L, 2L, 0L, 3L, NA, 2L),
  precio_mxn = c(75, 120, 50, 40, 100, NA),
  stringsAsFactors = FALSE
)
ventas_lab$importe_mxn <- calcular_importes(ventas_lab$unidades, ventas_lab$precio_mxn)
resumen_lab <- resumir_importes(ventas_lab$importe_mxn)
print(ventas_lab$importe_mxn) # 300 240 0 120 NA NA
print(resumen_lab) # 6 registros, 4 conocidos, 2 faltantes; grupos 2/2/2.
print(resumen_lab$n_cumplen + resumen_lab$n_no_cumplen + resumen_lab$n_pendientes) # 6
```

Los cuatro importes observados suman 660 MXN; su media es 165 y su cobertura
4/6, aproximadamente 66.67%. El cero de V003 sí participa. Faltan dos importes;
no hay evidencia para informar un total de las seis ventas. Una función que
imprimiera solamente «660» perdería esa información.

</details>

## 3. Elegir ramas para vacío, faltantes y cero

Consulta el resumen de `numeric(0)`, dos `NA_real_`, un cero y los cuatro
importes completos de la muestra anterior a 06.04. Predice registros,
conocidos, cobertura, suma observada, media y total. Explica qué `if` impide
dividir por cero y cuál impide informar una suma sin observaciones.

<details>
<summary>Solución razonada: cuatro casos con significados distintos</summary>

```r
vacio_lab <- resumir_importes(numeric(0))
faltantes_lab <- resumir_importes(c(NA_real_, NA_real_))
cero_lab <- resumir_importes(0)
completo_lab <- resumir_importes(c(300, 240, 0, 120))
print(vacio_lab) # 0/0; cobertura, suma, media y total NA; grupos 0/0/0.
print(faltantes_lab) # 2/0; cobertura 0; suma/media/total NA; grupos 0/0/2.
print(cero_lab) # 1/1; cobertura 100; suma/media/total 0; grupos 0/1/0.
print(completo_lab) # 4/4; cobertura 100; suma/total 660; media 165.
```

`n_registros > 0L` protege el denominador; `n_conocidos > 0L` protege la
interpretación de suma y media. El total exige registros y cobertura completa.
El contrato devuelve faltantes explícitos en los casos no calculables; no
altera lo que hacen `sum` o `mean` por separado. El conteo de pendientes se
refiere a la condición por venta, no a un error de programa.

</details>

## 4. Confirmar un precio y reutilizar el cálculo

En una copia confirma **60 MXN** como precio de V006, comprueba que seleccionas
una fila y vuelve a usar las funciones. Espera cinco importes conocidos,
cobertura 5/6, suma 780 y media 156. Consulta con umbral **120** y concilia
cumplen/no cumplen/pendientes. Demuestra que `ventas_lab` sigue intacta.

<details>
<summary>Solución razonada: misma función, otra entrada</summary>

```r
confirmadas_lab <- ventas_lab
fila_lab <- confirmadas_lab$id_venta == "V006"
print(sum(fila_lab)) # 1
confirmadas_lab$precio_mxn[fila_lab] <- 60
confirmadas_lab$importe_mxn <- calcular_importes(confirmadas_lab$unidades, confirmadas_lab$precio_mxn)
resumen_confirmado_lab <- resumir_importes(confirmadas_lab$importe_mxn, umbral = 120)
print(resumen_confirmado_lab) # 6/5/1; suma 780; media 156; total NA; grupos 4/1/1.
print(ventas_lab[ventas_lab$id_venta == "V006", , drop = FALSE]) # V006 2 NA NA
print(resumir_importes(ventas_lab$importe_mxn)$suma_observada_mxn) # 660
```

El umbral incluye la frontera: los importes 120 de V004 y V006 cumplen.
V003 no cumple y V005 sigue pendiente. Cambiar el precio sin volver a llamar
el cálculo dejaría un importe viejo; una columna calculada no es una fórmula
que se ejecute sola.

</details>

## 5. Repetir preguntas con una secuencia segura

Con la tabla **original**, recorre umbrales `0, 120, 240, 500`, conserva sus
conteos en el mismo orden y presenta una tabla. Debes obtener `4, 3, 2, 0`;
siempre hay dos pendientes. Repite con un vector de umbrales vacío, cambiando
también la reserva de salida. Explica por qué no usarías `1:length(umbrales_lab)`.

<details>
<summary>Solución razonada: posiciones válidas y salida vacía</summary>

```r
umbrales_lab <- c(0, 120, 240, 500)
conteos_lab <- integer(length(umbrales_lab))
for (i in seq_along(umbrales_lab)) {
  resumen_i_lab <- resumir_importes(ventas_lab$importe_mxn, umbral = umbrales_lab[i])
  conteos_lab[i] <- resumen_i_lab$n_cumplen
}
print(data.frame(umbral = umbrales_lab, n_cumplen = conteos_lab)) # 4 3 2 0
umbrales_vacios_lab <- numeric(0)
conteos_vacios_lab <- integer(length(umbrales_vacios_lab))
for (i in seq_along(umbrales_vacios_lab)) {
  conteos_vacios_lab[i] <- resumir_importes(ventas_lab$importe_mxn, umbral = umbrales_vacios_lab[i])$n_cumplen
}
print(length(conteos_vacios_lab)) # 0
```

El umbral cero incluye V003, que tiene cero conocido. `seq_along` entrega cero
posiciones cuando la entrada está vacía; `1:0` daría dos valores, 1 y 0.
La comparación por venta dentro de cada resumen sigue siendo vectorizada.

</details>

## 6. Comprobar rechazos y explicar su causa

Prueba **por separado** longitudes diferentes, texto numérico, negativo,
`NaN`, `Inf` y umbral desconocido o de longitud dos. Predice qué validación
falla. No corrijas estas entradas automáticamente ni mezcles sus errores con
el recorrido correcto. Contrasta un `NA_real_` permitido con un `NaN` rechazado.

<details>
<summary>Solución razonada: errores visibles, no importes inventados</summary>

Los siguientes son ejemplos de errores independientes. Ejecuta una línea
por vez; un script se detendría en la primera. Las líneas quedan separadas
de la solución correcta para conservar el código de salida no cero.

```r
# Error deliberado: longitudes diferentes.
calcular_importes(c(2, 3), 100)
```

```r
# Error deliberado: texto, aunque parezca un numero.
calcular_importes("2", 100)
```

```r
# Error deliberado: negativo.
resumir_importes(c(100, -5))
```

```r
# Error deliberado: resultado indefinido.
resumir_importes(NaN)
```

```r
# Error deliberado: infinito.
resumir_importes(Inf)
```

```r
# Error deliberado: umbral desconocido.
resumir_importes(numeric(0), umbral = NA_real_)
```

```r
# Error deliberado: umbral con longitud dos.
resumir_importes(100, umbral = c(100, 200))
```

`calcular_importes(NA_real_, 100)` devuelve un importe faltante, sin error.
Una longitud vacía en ambos argumentos también está permitida. Una entrada
incompatible es otro caso: `stop` informa el rechazo y no devuelve datos de
éxito. Las mismas longitudes tampoco detectan precios desordenados; revisa la
correspondencia por venta antes de llamar.

</details>

## Extensión opcional: manejar un rechazo esperado

Adapta el `tryCatch` de la lección a `resumir_importes(c(100, -5))`. Conserva
`ok = FALSE`, `valor = NULL` y el mensaje; explica por qué ese estado no debe
entrar en una tabla de importes como cero. No hace falta esta extensión para
cerrar la práctica esencial.

<details>
<summary>Solución razonada: diagnóstico explícito</summary>

```r
intento_lab <- tryCatch(
  {
    valor <- resumir_importes(c(100, -5))
    list(ok = TRUE, valor = valor, mensaje = NULL)
  },
  error = function(e) {
    list(ok = FALSE, valor = NULL, mensaje = conditionMessage(e))
  }
)
print(intento_lab) # FALSE, NULL, "No se permiten valores negativos."
```

El cálculo no se reanuda donde falló. Este manejador es amplio dentro de su
bloque y podría capturar también un defecto; no lo uses para ocultar errores
inesperados del análisis completo.

</details>

## Evidencia, comprobación y reflexión

Conserva tu script, versión/sesión y resultados: original 660/165 con cuatro
conocidos, variante 780/156 con cinco, grupos 4/1/1 con umbral 120, recorrido
de umbrales 4/3/2/0 y vacío sin iteraciones. Añade la explicación de los cuatro
casos frontera y los rechazos ejecutados por separado. Reinicia y ejecuta tu
archivo correcto desde cero con el recorrido de Rscript de la lección,
sustituyendo la ruta por la de tu copia; debe terminar con código 0.

Reflexiona:

1. ¿Qué resultado puede reutilizar otra función sin leer la salida de consola?
2. ¿Qué cambiaría si una función dependiera de un precio global de otra sesión?
3. ¿Por qué `if` no puede decidir con una condición por cada venta?
4. ¿Cómo distinguiste ausencia de registros, falta de datos y cero observado?
5. ¿Qué error detecta la igualdad de longitudes y cuál no puede detectar?

Cierra cuando puedas justificar esas decisiones y reproducir los resultados.
Registra evidencia real y dudas en [PROGRESS.md](../../../PROGRESS.md), sin
confundir material disponible con aprendizaje acreditado. Después continúa
con el [06.07 — Archivos y validación básica](../../../curriculum/06_r_foundations/07_files_validation/README.md). Volver a la [lección 06.06](../../../curriculum/06_r_foundations/06_functions_control/README.md).

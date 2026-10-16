# Lab 06.04 — Condiciones con información pendiente

## Propósito, entradas y preparación

Aplica la [lección 06.04 — Lógica y valores faltantes](../../../curriculum/06_r_foundations/04_logic_missing/README.md).
Necesitas haber practicado 06.02 y 06.03: vectores, tipos, máscaras y copias.
La entrada es la muestra de seis ventas del
[script de la lección](../../../curriculum/06_r_foundations/04_logic_missing/logica_faltantes.R):
cuatro conocidas, V005 sin unidades y V006 sin precio. No hay lectura de archivos,
paquetes externos ni proyecto/checkpoint implementado asociado.

Trabaja en una sesión nueva desde la raíz. Predice los resultados antes de
ejecutar el script con uno de los recorridos completos de la lección. Después,
en consola R, carga sus objetos:

```r
source("curriculum/06_r_foundations/04_logic_missing/logica_faltantes.R", encoding = "UTF-8")
```

Guarda tus variantes en una copia personal, por ejemplo bajo `output/` de este
lab, que está ignorado por Git. Conserva intactos el script original y las
muestras 06.01–06.03. Puedes repartir el lab entre varias sesiones.

## 1. Predecir una condición por venta

Sin ejecutar todavía, escribe los seis resultados de `importe_mxn >= 200` y de
`(importe_mxn >= 100) & (importe_mxn <= 250)`. Explica el cero de V003 y las dos
respuestas desconocidas. Después consulta `typeof` y `length` de cada máscara.
Comprueba también `FALSE & NA`, `TRUE & NA`, `TRUE | NA` y `FALSE | NA`.

<details>
<summary>Solución razonada: máscaras y lógica</summary>

```r
print(importe_mxn >= 200) # TRUE TRUE FALSE FALSE NA NA
print((importe_mxn >= 100) & (importe_mxn <= 250)) # FALSE TRUE FALSE TRUE NA NA
print(typeof(cumple_umbral)) # "logical"
print(length(cumple_umbral)) # 6
print(c(FALSE & NA, TRUE & NA, TRUE | NA, FALSE | NA)) # FALSE NA TRUE NA
```

V003 tiene importe conocido igual a cero. V005/V006 no tienen importe conocido:
no podemos contestar sus comparaciones. Una condición suficiente o una necesaria
ya fallida puede decidir el resultado aunque el otro operando sea desconocido.

</details>

## 2. Conservar tres grupos, incluidos los pendientes

Construye máscaras sin `NA` para cumplen, no cumplen con importe conocido y
pendientes. Recupera los identificadores y concilia los conteos con seis ventas.
Contrasta `id_venta[cumple_umbral]` con los identificadores pendientes explícitos.
¿Por qué `importe_mxn == NA` no encuentra los dos faltantes?

<details>
<summary>Solución razonada: no perder la identidad de los pendientes</summary>

```r
conocida <- !is.na(cumple_umbral)
cumplen <- conocida & cumple_umbral
no_cumplen <- conocida & !cumple_umbral
pendientes <- is.na(cumple_umbral)
print(id_venta[cumplen]) # V001 V002
print(id_venta[no_cumplen]) # V003 V004
print(id_venta[pendientes]) # V005 V006
print(sum(cumplen) + sum(no_cumplen) + sum(pendientes)) # 6
print(id_venta[cumple_umbral]) # V001 V002 NA NA
print(importe_mxn == NA) # Seis NA.
print(is.na(importe_mxn)) # FALSE FALSE FALSE FALSE TRUE TRUE
```

Los `NA` de la selección directa no identifican las ventas pendientes.
`is.na` detecta faltantes; comparar con lo desconocido no determina igualdad.
Las tres máscaras cubren cada venta una vez. No agrupamos los pendientes como
incumplimientos confirmados ni tratamos un importe bajo como un error de datos.

</details>

## 3. Informar un resumen con cobertura

Calcula registros, importes conocidos, faltantes, cobertura, suma y media
observadas. Escribe una frase que incluya su denominador. Explica qué ocurriría
si reemplazaras los dos faltantes por cero. Cambia el umbral a 100 en una nueva
máscara: ¿cuántos cumplen, no cumplen y quedan pendientes? ¿Cambió la fuente?

<details>
<summary>Solución razonada: una suma parcial y una condición diferente</summary>

```r
print(length(importe_mxn)) # 6
print(sum(!is.na(importe_mxn))) # 4
print(sum(is.na(importe_mxn))) # 2
print(100 * sum(!is.na(importe_mxn)) / length(importe_mxn)) # 66.66667 aprox.
print(sum(importe_mxn, na.rm = TRUE)) # 660
print(mean(importe_mxn, na.rm = TRUE)) # 165
condicion_100 <- importe_mxn >= 100
conocida_100 <- !is.na(condicion_100)
print(id_venta[conocida_100 & condicion_100]) # V001 V002 V004
print(id_venta[conocida_100 & !condicion_100]) # V003
print(id_venta[is.na(condicion_100)]) # V005 V006
```

«Se observaron cuatro de seis importes (66.67%); suman 660 MXN y su media es
165 MXN; dos importes están pendientes y el total de seis ventas es desconocido».
Imputar cero daría una media 660/6 = 110 y convertiría dos respuestas pendientes
en incumplimientos aparentes. No contamos con una regla que autorice esa imputación.
Con umbral 100 los conteos son 3/1/2; no cambió ningún importe ni su cobertura.

</details>

## 4. Resolver un faltante en una copia

Supón que se confirmó **una unidad** para V005. Copia `unidades`, modifica solo
su quinta posición y recalcula los importes con los precios originales. Usa el
umbral 200, conserva los tres grupos y resume la cobertura. Comprueba que la
quinta posición original sigue siendo `NA`. V006 todavía no tiene precio.

<details>
<summary>Solución razonada: una confirmación no completa toda la muestra</summary>

```r
unidades_confirmadas <- unidades
unidades_confirmadas[5] <- 1L
importes_confirmados <- unidades_confirmadas * precio_mxn
condicion_confirmada <- importes_confirmados >= 200
conocida_confirmada <- !is.na(condicion_confirmada)
print(importes_confirmados) # 300 240 0 120 100 NA
print(id_venta[conocida_confirmada & condicion_confirmada]) # V001 V002
print(id_venta[conocida_confirmada & !condicion_confirmada]) # V003 V004 V005
print(id_venta[is.na(condicion_confirmada)]) # V006
print(c(sum(!is.na(importes_confirmados)), sum(is.na(importes_confirmados)))) # 5 1
print(100 * sum(!is.na(importes_confirmados)) / length(importes_confirmados)) # 83.33333 aprox.
print(sum(importes_confirmados, na.rm = TRUE)) # 760 observados.
print(mean(importes_confirmados, na.rm = TRUE)) # 152: 760 / 5.
print(is.na(unidades[5])) # TRUE: fuente intacta.
```

Los grupos concilian 2 + 3 + 1 = 6. El total sigue desconocido: falta V006.
No confundir una copia con información hipotética con una corrección de la fuente.

</details>

## 5. Preguntar por el conjunto y revisar fronteras

Explica por qué `any(cumple_umbral)` es `TRUE` y `all(cumple_umbral)` es `FALSE`
aunque quedan pendientes. Compara con `any(c(FALSE, NA))` y `all(c(TRUE, NA))`.
Después prueba por separado, fuera del script correcto, `cumple_umbral && TRUE`:
registra el error de longitud de tu versión. Reescribe una pregunta escalar:
«hay registros y todos sus importes están presentes».

Construye un vector con dos `NA_real_` y otro vacío con `numeric(0)`. Informa
registros y valores conocidos antes de mirar `sum(..., na.rm = TRUE)` y
`mean(..., na.rm = TRUE)`. ¿Aceptarías ese cero como importe observado?
Comprueba qué devuelve `all` sobre un vector lógico vacío.

<details>
<summary>Solución razonada: un TRUE o un cero no bastan para validar datos</summary>

```r
print(c(any(cumple_umbral), all(cumple_umbral))) # TRUE FALSE
print(any(c(FALSE, NA))) # NA
print(all(c(TRUE, NA))) # NA
print((length(importe_mxn) > 0L) && all(!is.na(importe_mxn))) # FALSE
solo_faltantes <- c(NA_real_, NA_real_)
vacio <- numeric(0)
print(c(length(solo_faltantes), sum(!is.na(solo_faltantes)))) # 2 0
print(c(length(vacio), sum(!is.na(vacio)))) # 0 0
print(sum(solo_faltantes, na.rm = TRUE)) # 0: no quedan valores.
print(mean(solo_faltantes, na.rm = TRUE)) # NaN
print(sum(vacio, na.rm = TRUE)) # 0
print(mean(vacio, na.rm = TRUE)) # NaN
print(all(logical(0))) # TRUE
print((length(vacio) > 0L) && all(!is.na(vacio))) # FALSE
```

Un verdadero confirmado decide `any`; un falso confirmado decide `all`. Los
otros dos ejemplos siguen desconocidos. `&&` requiere operandos escalares en
R 4.6.1: no pregunta por cada venta ni resume automáticamente un vector.
En las fronteras no hay valores observados: reporta esa situación y distingue
dos registros incompletos de cero registros. La cobertura del vacío no es 0%:
no hay denominador. `all` sobre un vacío no verifica que haya llegado información.

</details>

## 6. Diferenciar representaciones

Compara cero, `NA_real_`, `NaN`, `NULL` y `"NA"` con `is.na`, `is.nan`,
`is.null` y `length`. Explica por qué `c(75, NULL, 40)` no conserva tres posiciones.
Ampliación opcional: revisa `is.na(Inf)` e `is.finite(Inf)`; ¿basta con que un dato
esté presente para considerarlo válido?

<details>
<summary>Solución razonada: presencia y validez son comprobaciones distintas</summary>

```r
print(is.na(c(0, NA_real_, NaN))) # FALSE TRUE TRUE
print(is.nan(c(NA_real_, NaN))) # FALSE TRUE
print(is.null(NULL)) # TRUE
print(length(NULL)) # 0
print(length(c(75, NULL, 40))) # 2
print(length(c(75, NA, 40))) # 3
print(is.na("NA")) # FALSE
print(is.na(Inf)) # FALSE
print(is.finite(Inf)) # FALSE
```

Cero es un valor observado, `NA_real_` ocupa una posición faltante, `NaN` indica
un resultado numérico indefinido y también lo detecta `is.na`. `NULL` tiene longitud
cero, mientras que `"NA"` es texto. Un infinito está presente pero no es finito;
una regla de calidad también necesita significado, unidad y rango admitido.

</details>

## Resultado, evidencia y reflexión

Conserva el script personal, salida de una sesión nueva, versión de R y una
explicación de los conteos 2/2/2, 3/1/2 y 2/3/1. Añade los resúmenes con cobertura,
la comprobación de la fuente intacta y el error deliberado separado del script.
No publiques rutas personales ni archivos de sesión. No agregues `output/` con `git add -f`.

Criterio de salida: justificas el tratamiento de desconocidos, recuperas sus
identificadores, concilias conteos y diferencias una suma observada de un total
completo, también ante todos faltantes o vacío. Reflexiona: ¿qué afirmación falsa
haría un informe que mostrara únicamente 660 o únicamente `all(...) = TRUE`?
Registra lo que efectivamente realizaste y las dudas; este material no completa
por sí mismo el módulo ni cambia tu estado de aprendizaje.

Siguiente: [plan 06.05 — Listas y data frames](../../../curriculum/06_r_foundations/README.md#05-listas-y-data-frames),
todavía pendiente. Volver a la [lección 06.04](../../../curriculum/06_r_foundations/04_logic_missing/README.md)
y al [índice de labs](../../README.md).

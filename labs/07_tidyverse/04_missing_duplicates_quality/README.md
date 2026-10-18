# Lab 07.04 — Conservar aceptados y rechazos con motivos

## Propósito, entradas y resultado

Practica la [lección 07.04](../../../curriculum/07_tidyverse/04_missing_duplicates_quality/README.md)
en el mismo proyecto RStudio/IDE. Prepara una sola vez sus archivos según la
lección: CSV de 44 registros, funciones y ejecutor; no hay paquetes nuevos.
Las muestras de seis y 40 filas y sus resultados se conservan.

Entrega un script propio y una explicación del contrato, repeticiones y
partición. Mantén las 44 entradas, textos y todos los motivos, aunque solo
29 se acepten. No se pide exportar ni crear un checkpoint integrador, todavía
pendiente. Puedes dividir el lab en diagnóstico (1–3) y comprobación (4–6).

## 1. Anticipar decisiones

Antes de ejecutar, lee el contrato de la lección y los registros 005, 014,
023, 028 y 041. Recuerda que 041 es un identificador; ocupa el registro 43.
Escribe qué puedes afirmar sobre ausencia, conversión, rango y relación pago/saldo.
Explica además por qué el mismo ID en otro corte no implica repetición.

<details>
<summary>Comprobar el razonamiento</summary>

005 tiene saldo ausente; 014 contiene error y falla la conversión. En 023,
3.5 es numérico pero no entero. 028 tiene saldo/pago cero presentes: pasa
esas reglas. El registro 43, ID 041, tiene tres negativos y −50 > −100:
cuatro incumplimientos. La clave contiene ID y corte, no solo ID.

Los seis campos son obligatorios en este contrato. No basta con calcular
una resta para aceptar una fila ni se decide imputar cero a un dato desconocido.

</details>

## 2. Cargar y explorar las repeticiones

Abre el mismo proyecto de práctica y comprueba getwd() en Console. Crea
output/mi_calidad.R y conserva la raíz de la práctica como directorio. Inicio:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
fuente <- leer_texto_conversion("datos/cartera_calidad.csv")
original <- fuente
```

Ejecuta por bloques con Run. Inspecciona la tabla en Environment/visor y deja
los controles en el script. Marca las filas exactamente iguales sobre las
seis columnas y todas las apariciones de claves repetidas completas.

<details>
<summary>Una solución posible</summary>

which devuelve las posiciones donde una máscara es TRUE. Permite comprobar
qué registros se marcaron sin cambiar la tabla.

```r
exactos <- duplicated(fuente) | duplicated(fuente, fromLast = TRUE)
claves <- fuente[c("id_credito", "fecha_corte")]
completa <- !is.na(fuente$id_credito) & !is.na(fuente$fecha_corte)
repetidos <- completa & (duplicated(claves) | duplicated(claves, fromLast = TRUE))
stopifnot(identical(which(exactos), c(1L, 41L)),
          identical(which(repetidos), c(1L, 2L, 41L, 42L)))
print(fuente[repetidos, ])
```

Retoma la diferencia entre posiciones y selección lógica de
[06.03](../../../curriculum/06_r_foundations/03_subsetting/README.md).
Las dos filas exactas son parte de las cuatro filas con clave repetida:
no sumes 2 + 4 como si fueran seis registros diferentes.

</details>

Ahora prueba distinct sobre las dos versiones de 002 en ambos órdenes.
¿Selecciona siempre el mismo pago? Conserva estos objetos como ensayo;
no los uses como tabla aceptada.

<details>
<summary>Demostrar la dependencia del orden</summary>

```r
versiones <- fuente[c(2L, 42L), ]
primera <- versiones |> dplyr::distinct(id_credito, fecha_corte, .keep_all = TRUE)
otra_primera <- versiones[c(2L, 1L), ] |>
  dplyr::distinct(id_credito, fecha_corte, .keep_all = TRUE)
stopifnot(identical(primera$pago_mxn, "200"),
          identical(otra_primera$pago_mxn, "250"))
```

Ambas salidas tienen una fila y una clave única, pero el orden decidió qué
versión quedó. Eso no demuestra cuál pago es correcto. Nuestra política
aparta las dos versiones para revisión con evidencia.

</details>

## 3. Evaluar y conservar todos los motivos

Llama evaluar_calidad y conserva sus cinco componentes. Comprueba el tamaño
de trabajo/banderas, las dos partes y las posiciones de los rechazos.
Inspecciona especialmente los motivos del registro 43 y del 44.

<details>
<summary>Una solución posible</summary>

```r
revision <- evaluar_calidad(fuente)
trabajo <- revision$trabajo
aceptados <- revision$aceptados
rechazados <- revision$rechazados
banderas <- revision$banderas
stopifnot(identical(dim(trabajo), c(44L, 12L)),
          identical(dim(banderas), c(44L, 15L)),
          nrow(aceptados) == 29L, nrow(rechazados) == 15L,
          sum(as.matrix(banderas)) == 19L,
          identical(rechazados$numero_registro,
            c(1L, 2L, 5L, 9L, 14L, 18L, 21L, 23L, 31L, 33L, 38L, 41L, 42L, 43L, 44L)))
print(rechazados |> dplyr::select(numero_registro, id_credito, motivos), n = 15, width = Inf)
stopifnot(trabajo$motivos[43] == paste(
  "saldo_mxn_negativo", "pago_mxn_negativo", "dias_atraso_negativo", "pago_supera_saldo",
  sep = "; "), trabajo$motivos[44] == "id_credito_ausente; segmento_ausente")
```

Las advertencias de conversión por error/pendiente/no_dato son esperadas.
No se descartan sus filas. case_when con primera coincidencia no conservaría
por sí solo los cuatro motivos de 43; por eso se registran banderas separadas.
En 005, comparar pago > saldo no confirma un incumplimiento, pero la bandera
de ausencia de saldo sí obliga al rechazo. Ningún importe se rellena con cero.

</details>

## 4. Probar la clave y un caso de catálogo

Crea una muestra en memoria a partir de dos filas válidas. Dales el mismo ID
y cortes distintos: ambas deben aceptarse. Después usa el mismo corte: ambas
deben rechazarse por clave_repetida. Prueba por separado una categoría fuera
del catálogo, sin cambiar el archivo ni fuente.

<details>
<summary>Una solución posible</summary>

```r
mini <- fuente[c(3L, 4L), ]
mini$id_credito <- c("A", "A")
mini$fecha_corte <- c("2026-09-30", "2026-10-31")
distintos_cortes <- evaluar_calidad(mini)
stopifnot(nrow(distintos_cortes$aceptados) == 2L)
misma_clave <- mini
misma_clave$fecha_corte <- c("2026-09-30", "2026-09-30")
conflicto <- evaluar_calidad(misma_clave)
stopifnot(nrow(conflicto$rechazados) == 2L,
          all(conflicto$rechazados$motivos == "clave_repetida"))
otro_segmento <- mini
otro_segmento$segmento[1] <- "otro"
catalogo <- evaluar_calidad(otro_segmento)
stopifnot(nrow(catalogo$rechazados) == 1L,
          catalogo$rechazados$motivos == "segmento_fuera_catalogo",
          identical(fuente, original))
```

Este contrato exige presencia, pero no un formato de tres dígitos del ID;
por eso A pasa. La fecha es texto: cambiar el corte distingue la clave, sin
demostrar que ya validamos calendarios. No normalizamos categorías para hacerlas
encajar; una corrección debe tener evidencia. Las reglas adicionales se declaran.

</details>

## 5. Reconstruir, conciliar y detectar una alteración

Comprueba la partición y los controles de saldo. Después reúne las partes,
ordena por numero_registro y compara todas las columnas con trabajo.

<details>
<summary>Comprobación</summary>

```r
comprobar_particion(trabajo, aceptados, rechazados, banderas)
juntos <- dplyr::bind_rows(aceptados, rechazados) |> dplyr::arrange(numero_registro)
stopifnot(identical(as.list(juntos), as.list(trabajo)),
          identical(revision$controles$saldo_observado_mxn, c(234900, 177250, 57650)),
          identical(revision$controles$saldos_conocidos, c(42L, 29L, 13L)),
          identical(revision$controles$saldos_sin_interpretar, c(2L, 0L, 2L)))
vacia <- evaluar_calidad(fuente[0, ])
stopifnot(nrow(vacia$aceptados) == 0L, nrow(vacia$rechazados) == 0L,
          all(is.na(vacia$controles$saldo_observado_mxn)))
```

234900 es saldo interpretable de registros de entrada, incluyendo repeticiones
y negativos. No es saldo limpio de créditos únicos. Dos saldos siguen sin
interpretarse; aceptados tiene cobertura 29/29. Una entrada vacía no informa
un saldo observado cero.

</details>

En otro archivo o bloque aislado, crea una copia alterada de aceptados y
reemplaza su primera fila por la segunda. El conteo no cambia, pero se pierde
un registro y se duplica otro. La comprobación debe dar **error esperado**:

```r
alterados <- aceptados
alterados[1, ] <- alterados[2, ]
stopifnot(nrow(alterados) == nrow(aceptados))
comprobar_particion(trabajo, alterados, rechazados, banderas)
```

No repares trabajo para hacer pasar ese ensayo. Conserva aceptados intacto y
deja el bloque de error fuera del script de reconstrucción correcta.

## 6. Reiniciar y registrar evidencia

Guarda output/mi_calidad.R con los bloques correctos y el error deliberado
aparte. Usa Session > Restart R y conserva el mismo proyecto; comprueba que
no se recuperan objetos de un workspace anterior. En Console, desde la raíz
de la práctica:

```r
source("output/mi_calidad.R", encoding = "UTF-8")
source("revisar_calidad.R", encoding = "UTF-8")
```

También puedes usar Source sobre el archivo abierto, manteniendo ese directorio.
No se requiere Terminal. La carga, reglas y controles deben reconstruirse;
las advertencias conocidas se justifican. El ejecutor comprueba la huella de
entrada y no exporta ni reemplaza salidas anteriores.

Conserva script, versiones, contrato y evidencia de 44 = 29 + 15, 19 incidencias,
motivos múltiples y reconstrucción exacta. Anota cobertura y conciliación del
saldo sin presentarlo como total completo. output/ está ignorado: no agregues
con fuerza bibliotecas o resultados de práctica. Puedes comparar con
[pandas 02.05](../../../curriculum/02_pandas/05_missing_duplicates_rules/README.md)
sin necesitar Python para completar este lab.

Responde con tus palabras:

1. ¿Qué distingue un vacío, error, 3.5 y cero conocido?
2. ¿Qué perderías al quedarte con una primera versión de 002 sin evidencia?
3. ¿Por qué 19 motivos no significan 19 registros rechazados?
4. ¿Por qué FALSE en una bandera no autoriza por sí solo a aceptar la fila?
5. ¿Qué detecta la reconstrucción que el conteo no pudo detectar?
6. Si falta una combinación crédito/corte entera, ¿por qué is.na no basta?

Puedes avanzar cuando expliques las decisiones, conserves cada registro y
sus motivos y compruebes desde una sesión nueva. Registra evidencia y dudas
en [PROGRESS.md](../../../PROGRESS.md); material disponible no acredita aprendizaje.
No hay checkpoint integrador implementado asociado.

Siguiente: [07.05 — Agrupar y resumir](../../../curriculum/07_tidyverse/README.md#05-agrupar-y-resumir),
todavía planificada. Volver a la [lección 07.04](../../../curriculum/07_tidyverse/04_missing_duplicates_quality/README.md).

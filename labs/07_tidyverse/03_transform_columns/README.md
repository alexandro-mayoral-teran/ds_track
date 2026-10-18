# Lab 07.03 — Calcular columnas con reglas explícitas

## Propósito, entradas y resultado

Practica la [lección 07.03](../../../curriculum/07_tidyverse/03_transform_columns/README.md)
en el mismo proyecto RStudio/IDE de 07.02. Prepara sus archivos una sola vez
según la lección: recibes el CSV conocido de seis filas, la muestra de 40,
las funciones de conversión y el script de comprobación. No instales paquetes.

Resultado: un script propio y una explicación de unidades, tipos, reglas y base
de cálculo. Conserva las 40 filas, textos originales y marcas. No se pide
imputación, eliminación de filas, exportación ni proyecto/checkpoint integrador,
todavía pendiente. Puedes trabajar las actividades 1–3 y 4–7 en sesiones distintas.

## 1. Agregar sin reemplazar

Abre el proyecto de práctica, comprueba getwd() en Console y crea
output/mis_columnas.R. Su directorio de trabajo sigue siendo la raíz de la
práctica. Ejecuta por bloques con Run; usa el visor para explorar y deja
comprobaciones en el script. Inicio:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_importacion.R", encoding = "UTF-8")
source("R/funciones_transformacion.R", encoding = "UTF-8")
cartera <- leer_cartera("datos/cartera_demo.csv")
original_seis <- cartera
```

Añade saldo_miles_mxn y una etiqueta de atraso con if_else: desde 30 inclusive,
menos de 30 o sin dato evaluable. Mantén saldo_mxn y dias_atraso. Predice las
salidas de 003, 004 y 005 antes de ejecutar.

<details>
<summary>Una solución posible</summary>

```r
calculada <- cartera |>
  dplyr::mutate(
    saldo_miles_mxn = saldo_mxn / 1000,
    etiqueta = dplyr::if_else(dias_atraso >= 30L,
                             "30 dias o mas", "menos de 30 dias",
                             missing = "sin dato evaluable")
  )
print(calculada, n = 6, width = Inf)
stopifnot(identical(dim(calculada), c(6L, 7L)),
          calculada$saldo_miles_mxn[3] == 0.75,
          calculada$etiqueta[3] == "30 dias o mas",
          calculada$saldo_mxn[4] == 0,
          calculada$etiqueta[5] == "sin dato evaluable",
          is.na(calculada$dias_atraso[5]), identical(cartera, original_seis))
```

003 conserva 750 MXN y muestra 0.75 miles de MXN. El cero de 004 es conocido.
En 005 la etiqueta explica la ausencia, pero no rellena dias_atraso. Cambiar
el nombre o la unidad de una columna calculada requiere explicar esa decisión.

</details>

## 2. Probar prioridad y tipos

Construye días c(0L, 29L, 30L, 31L, NA_integer_) y clasifícalos con case_when.
La regla ≥ 30 debe incluir la frontera. Explica qué pasaría si una primera
regla >= 0 asignara a todos esos valores conocidos la etiqueta menor de 30.

<details>
<summary>Solución y explicación</summary>

```r
fronteras <- tibble::tibble(dias_atraso = c(0L, 29L, 30L, 31L, NA_integer_)) |>
  dplyr::mutate(
    estado = dplyr::case_when(
      is.na(dias_atraso) ~ "sin dato evaluable",
      dias_atraso >= 30L ~ "30 dias o mas",
      .default = "menos de 30 dias"
    )
  )
stopifnot(identical(fronteras$estado,
  c("menos de 30 dias", "menos de 30 dias", "30 dias o mas",
    "30 dias o mas", "sin dato evaluable")))
```

La primera coincidencia gana: una condición amplia al comienzo puede ocultar
las posteriores. Sin tratar NA explícitamente, .default también lo recibiría.
Esto no valida rangos de negocio: negativos caerían entre los menores de 30.

</details>

Ejecuta aparte este **error esperado** de tipos; no lo guardes en el script
que debe reconstruirse completo:

```r
dplyr::if_else(c(TRUE, FALSE), "si", 0)
```

Explica por qué dos resultados de texto serían coherentes y mezclar texto
con una cantidad no lo es. No corrijas el error convirtiendo cantidades reales
a texto si el objetivo posterior es operar con ellas.

## 3. Auditar conversiones antes de calcular

Interpreta c("1250", "error", NA_character_, "3.5", "0") con convertir_entero.
Comprueba valor, incompatible y problemas. Anticipa qué diferencia hay entre
el tercer y cuarto elemento: ambos quedan NA, pero por motivos distintos.

<details>
<summary>Una solución posible</summary>

```r
ensayo <- convertir_entero(c("1250", "error", NA_character_, "3.5", "0"))
print(ensayo$problemas)
stopifnot(identical(ensayo$valor, c(1250L, NA_integer_, NA_integer_, NA_integer_, 0L)),
          identical(ensayo$incompatible, c(FALSE, TRUE, FALSE, TRUE, FALSE)),
          nrow(ensayo$problemas) == 1L)
```

La advertencia corresponde al texto error. El tercer elemento estaba ausente;
3.5 se interpreta como double, pero no satisface el contrato entero. problems
del lector no sustituye nuestra marca de incompatibilidad. El cero permanece
conocido. No silencies la advertencia ni pierdas el texto que permite revisarla.

</details>

## 4. Transformar las 40 filas y revisar casos concretos

Carga datos/cartera_conversion.csv con leer_texto_conversion, conserva una
referencia original y llama transformar_columnas. Comprueba 40 × 15, orden de
claves 001–040 y origen intacto. Localiza 005/009/014/018/023/028/033/038 con
filter y `%in%`, como en el [comparador de 06.09](../../../curriculum/06_r_foundations/09_known_result/README.md).
Cuenta ausentes de entrada e incompatibles de salida por separado.

<details>
<summary>Solución orientativa</summary>

```r
entrada <- leer_texto_conversion("datos/cartera_conversion.csv")
original_cuarenta <- entrada
resultado <- transformar_columnas(entrada)
stopifnot(identical(dim(resultado), c(40L, 15L)),
          identical(resultado$id_credito, sprintf("%03d", 1:40)),
          identical(entrada, original_cuarenta))
casos <- resultado |>
  dplyr::filter(id_credito %in% c("005", "009", "014", "018", "023", "028", "033", "038"))
print(casos, n = 8, width = Inf)
stopifnot(sum(is.na(entrada$saldo_mxn)) == 1L,
          sum(resultado$saldo_mxn_incompatible) == 1L,
          sum(is.na(entrada$pago_mxn)) == 1L,
          sum(resultado$pago_mxn_incompatible) == 1L,
          sum(is.na(entrada$dias_atraso)) == 1L,
          sum(resultado$dias_atraso_incompatible) == 2L)
```

El saldo vacío 005 y saldo error 014 quedan numéricamente ausentes, pero solo
014 es incompatible. En 018 falta atraso; aún se puede restar 5500 − 300.
En 023 no puede clasificarse el atraso entero, pero sí restar 6750 − 300.
Los compañeros _texto e _incompatible explican estas diferencias. Las tres
advertencias de parseo por error, pendiente y no_dato son esperadas.

</details>

## 5. Denominador y resultados que no deben recortarse

Predice resta y porcentaje en esta tabla adicional, sin reemplazar resultado:

```r
prueba_pago <- tibble::tibble(
  saldo_mxn = c(100, 0, 100, NA_real_, 100),
  pago_mxn = c(25, 0, 150, 10, NA_real_)
)
```

Aplica la misma resta y el denominador positivo. ¿Qué diferencia hay entre
resta cero y porcentaje desconocido? ¿Por qué el caso 100/150 no debe ocultarse?

<details>
<summary>Comprobación</summary>

```r
prueba_calculada <- prueba_pago |>
  dplyr::mutate(
    saldo_despues_pago_mxn = saldo_mxn - pago_mxn,
    porcentaje_pago = pago_mxn /
      dplyr::if_else(saldo_mxn > 0, saldo_mxn, NA_real_) * 100
  )
stopifnot(identical(prueba_calculada$saldo_despues_pago_mxn, c(75, 0, -50, NA, NA)),
          identical(prueba_calculada$porcentaje_pago, c(25, NA, 150, NA, NA)))
```

0 − 0 = 0, pero 0/0 no da un porcentaje observado. 100 − 150 = −50 y el pago
representa 150 % del saldo; recortarlos introduciría una regla que no acordamos.
La calidad del caso se revisará con reglas explícitas en 07.04. Un pago o saldo
ausente impide el cálculo que lo necesita, sin implicar automáticamente nada
sobre otros campos.

</details>

## 6. Conciliar la misma base y comprobar un vacío

Con resultado, delimita las filas con resta evaluable antes de sumar saldo,
pago y resta. Comprueba las cifras de la lección; anota cuántas observaciones
apoyan cada indicador. Después transforma una entrada con cero filas y revisa
que conserve el esquema de salida. No interpretes la suma vacía como saldo
observado. Agrupar y resumir por segmento se desarrolla en 07.05.

<details>
<summary>Una solución posible</summary>

```r
base_resta <- resultado |> dplyr::filter(!is.na(saldo_despues_pago_mxn))
stopifnot(nrow(base_resta) == 36L,
          sum(base_resta$saldo_mxn) == 217750,
          sum(base_resta$pago_mxn) == 6600,
          sum(base_resta$saldo_despues_pago_mxn) == 211150,
          sum(!is.na(resultado$porcentaje_pago)) == 35L,
          sum(resultado$estado_atraso == "sin dato evaluable") == 3L)
vacia <- transformar_columnas(entrada[0, ])
stopifnot(identical(dim(vacia), c(0L, 15L)),
          identical(names(vacia), names(resultado)),
          identical(vapply(vacia, typeof, character(1)),
                    vapply(resultado, typeof, character(1))))
```

Las 36 filas tienen ambos operandos de resta; 028 no aporta porcentaje por
saldo cero, de modo que quedan 35 porcentajes evaluables. Las 40 filas siguen
en resultado. La tabla vacía mantiene tipos, pero no aporta observaciones.

</details>

## 7. Reconstruir y registrar evidencia

Guarda el script propio con los bloques correctos, dejando el error de tipos
en un archivo aparte. Usa Session > Restart R, conserva abierto el proyecto
y comprueba que no se restauran objetos de un workspace anterior. Desde la raíz
de la práctica, ejecuta en Console:

```r
source("output/mis_columnas.R", encoding = "UTF-8")
source("transformar_cartera.R", encoding = "UTF-8")
```

También puedes usar Source sobre el script abierto, conservando el directorio.
No hace falta Terminal. Deben reconstruirse los resultados y pasar los controles;
las advertencias conocidas se leen y se justifican, no se ocultan. El ejecutor
incluido comprueba la huella del CSV y no escribe una exportación.

Conserva script, versiones, casos revisados y una explicación de la conciliación
217750 − 6600 = 211150 sobre 36 filas. output/ está ignorado; no agregues con
fuerza bibliotecas o salidas. La comparación con pandas 02.04 es de significado
y valores, no de identidad entre sus tipos enteros y los de R.

Responde con tus palabras:

1. ¿Qué cambia mutate y qué conserva? ¿Cuándo reemplaza una columna?
2. ¿Por qué dos NA pueden tener orígenes distintos y cómo los rastreas?
3. ¿Qué resuelve missing y qué resuelve .default? ¿Cómo influye la prioridad?
4. ¿Por qué 3.5 no debe truncarse a 3 para hacer coincidir un tipo?
5. ¿Por qué hay 36 restas y 35 porcentajes evaluables?
6. ¿Qué sigue pendiente antes de decidir aceptar o rechazar una fila?

Puedes avanzar cuando reconstruyas, expliques unidades/tipos/faltantes y
denominador, pruebes fronteras y conserves fuente y textos de origen. Registra
evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md); no se acredita aprendizaje
por estar disponible el material. No hay checkpoint integrador implementado.

Siguiente: [07.04 — Faltantes, duplicados y calidad](../../../curriculum/07_tidyverse/04_missing_duplicates_quality/README.md),
con lección y lab disponibles. Volver a la [lección 07.03](../../../curriculum/07_tidyverse/03_transform_columns/README.md).

# Lab 07.08 — Normalizar categorías y controlar sus niveles

## Propósito, entradas y resultado

Practica la [lección 07.08](../../../curriculum/07_tidyverse/08_text_categories_factors/README.md)
en el mismo proyecto RStudio/IDE. Prepara los archivos y restaura su lockfile:
stringr pasa a dependencia directa y forcats se añade a la biblioteca local.
Los metadatos anteriores quedan respaldados; no cambies Conda ni bibliotecas globales.

Usa datos/cartera_texto.csv: copia de las 48 entradas de pandas 02.06, distinta
de la fuente de 07.07. Entrega output/mi_texto.R, controles y una explicación
de equivalencias, pendientes y niveles. Las fechas e IDs permanecen sin
normalizar ni validar. No se pide figura, exportación ni checkpoint integrador,
todavía pendiente.

## 1. Acordar equivalencias

Antes de ejecutar, predice el resultado de " Consumo ", "Educación", "   ",
NA_character_, "educación superior", "consu mo" y "NA". ¿Qué convertirías en
ausencia? ¿Qué valores conservarías como desconocidos?

<details>
<summary>Comprobar el razonamiento</summary>

consumo y educacion quedan reconocidos. El texto en blanco y NA original
son ausentes por motivos distintos que puedes consultar en el origen.
educación superior, consu mo y na quedan presentes pero fuera del catálogo.
La equivalencia con acento es del valor completo educación. No se declararon
otras equivalencias ni un grupo «otros» que pueda absorber valores desconocidos.

</details>

## 2. Leer y conservar la fuente

Abre la práctica, reinicia R y comprueba getwd() en Console. Crea el script en
el editor manteniendo la raíz del proyecto como directorio. Ejecuta por bloques:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
original <- fuente
```

Inspecciona el registro 5, el 9 y el 48. Distingue número de registro de ID:
el 48 tiene ID 024. Explica por qué todavía no puedes afirmar que todas las
fechas o claves sean válidas.

## 3. Normalizar y conservar pendientes

Escribe las cuatro etapas de normalización en un vector separado: str_trim,
na_if, str_to_lower con locale y equivalencia exacta. Después compara con la
función del curso y conserva las dos partes:

```r
resultado <- preparar_segmentos(fuente)
comprobar_segmentos(fuente, resultado)
trabajo <- resultado$trabajo
reconocidos <- resultado$reconocidos
pendientes <- resultado$pendientes
resumen <- resultado$resumen
```

<details>
<summary>Una solución y sus controles</summary>

```r
limpio <- stringr::str_trim(fuente$segmento)
limpio <- dplyr::na_if(limpio, "")
propio <- stringr::str_to_lower(limpio, locale = "es")
propio <- dplyr::if_else(propio == "educación", "educacion", propio)
stopifnot(identical(propio, trabajo$segmento_normalizado),
          identical(trabajo$segmento, fuente$segmento),
          identical(resultado$controles$registros, c(48L, 45L, 3L)),
          identical(resultado$controles$saldo_observado_mxn, c(112800, 105800, 7000)),
          identical(pendientes$numero_registro, c(5L, 9L, 48L)),
          sum(trabajo$texto_modificado) == 46L)
```

45 segmentos reconocidos, dos ausentes y microcredito fuera del catálogo.
Todos los registros y cantidades se conservan. Es reconocimiento de segmento,
no aceptación completa de la cartera. Las sumas recorren fechas aún no
interpretadas; no son saldo de una cartera en una única fecha.

</details>

Reproduce la búsqueda de la sección 5 de la lección. Contrasta fragmento
literal, patrón ^consumo$ y pertenencia al catálogo. Explica el NA del resultado
de str_detect antes de usarlo para filtrar.

## 4. Crear el factor sin perder desconocidos

Comprueba etiquetas, niveles y carácter nominal del factor de reconocidos.
Contrasta con convertir directamente c("consumo", "microcredito", NA_character_)
mediante factor(..., levels = niveles_segmento).

<details>
<summary>Comprobaciones y explicación</summary>

```r
stopifnot(identical(levels(reconocidos$segmento_factor), niveles_segmento),
          !is.ordered(reconocidos$segmento_factor),
          !anyNA(reconocidos$segmento_factor),
          identical(as.character(reconocidos$segmento_factor), reconocidos$segmento_normalizado))
silencioso <- factor(c("consumo", "microcredito", NA_character_), levels = niveles_segmento)
stopifnot(identical(is.na(silencioso), c(FALSE, TRUE, TRUE)))
```

La conversión directa mezcla un desconocido presente con una ausencia original.
El recorrido conserva ambos casos en pendientes antes de crear el factor.
El orden de niveles no declara que un sector sea mayor o menor que otro.

</details>

En un bloque aislado, prueba el **error esperado** de la alternativa estricta.
Déjalo fuera del script de reconstrucción correcta:

```r
# ERROR ESPERADO: ejecutar por separado.
forcats::fct(c("consumo", "microcredito", NA_character_), levels = niveles_segmento)
```

No conviertas microcredito en NA para silenciarlo ni amplíes el catálogo sin
una decisión respaldada. Explica por qué los códigos del factor tampoco son
importes ni una medida de riesgo.

## 5. Preparar dos órdenes y revisar niveles vacíos

Muestra primero educacion/comercio/servicios/consumo con fct_relevel. Luego
prepara un orden descendente por el saldo ya agregado mediante fct_reorder.
Usa arrange para imprimir las filas según el factor.

<details>
<summary>Solución razonada</summary>

```r
manual <- resumen |>
  dplyr::mutate(segmento_factor = forcats::fct_relevel(
    segmento_factor, "educacion", "comercio", "servicios", "consumo"))
por_saldo <- resumen |>
  dplyr::mutate(segmento_factor = forcats::fct_reorder(
    segmento_factor, saldo_observado_mxn, .fun = sum, .desc = TRUE))
stopifnot(identical(as.character(manual$segmento_factor), as.character(resumen$segmento_factor)),
          identical(por_saldo$saldo_observado_mxn, resumen$saldo_observado_mxn),
          identical(levels(por_saldo$segmento_factor),
                    c("comercio", "servicios", "educacion", "consumo")))
print(manual |> dplyr::arrange(segmento_factor), width = Inf)
print(por_saldo |> dplyr::arrange(segmento_factor), width = Inf)
```

En el orden original los conteos son 10/12/12/11 y las sumas 23000/27600/28800/26400.
Las etiquetas de cada fila y sus indicadores no cambian al reordenar niveles.
Cambiar niveles y ordenar filas son operaciones diferentes.

</details>

Reproduce el caso de solo_consumo de la sección 9: cuatro niveles, uno observado.
Explica la diferencia entre .drop = FALSE y fct_drop, y por qué un grupo sin
filas no tiene un saldo cero observado.

## 6. Reiniciar y conservar evidencia

Guarda output/mi_texto.R con carga, normalización, partes, factores y controles
correctos; conserva aparte el error esperado. Usa Session > Restart R sin
recuperar el workspace. En Console, desde la raíz de la práctica:

```r
source("output/mi_texto.R", encoding = "UTF-8")
source("revisar_texto.R", encoding = "UTF-8")
stopifnot(identical(fuente, original), identical(huella, tools::md5sum(ruta)))
```

También puedes usar Source desde el editor. Conserva script, versiones,
metadatos respaldados, equivalencias, pendientes y controles 48 = 45 + 3 y
112800 = 105800 + 7000 MXN. output/ y las bibliotecas están ignorados; no los
agregues con fuerza al repositorio.

Responde con tus palabras:

1. ¿Qué regla autoriza cada cambio de escritura? ¿Cuál no se autorizó?
2. ¿Qué distingue ausente de fuera_catalogo?
3. ¿Por qué no conviene convertir a factor antes de investigar desconocidos?
4. ¿Qué diferencia hay entre niveles, etiquetas y códigos internos?
5. ¿Por qué reconocido no equivale aquí a registro completamente válido?
6. ¿Qué datos y resultados se conservan al cambiar el orden de presentación?

Puedes avanzar cuando expliques esas decisiones y reconstruyas el resultado
sin perder origen, pendientes ni indicadores. Registra evidencia y dudas en
[PROGRESS.md](../../../PROGRESS.md); disponer del material no acredita aprendizaje.
No hay checkpoint integrador implementado asociado.

Siguiente: [07.09 — Fechas y cortes](../../../curriculum/07_tidyverse/09_dates_cutoffs/README.md). Volver a la [lección 07.08](../../../curriculum/07_tidyverse/08_text_categories_factors/README.md).

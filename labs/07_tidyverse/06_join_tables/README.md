# Lab 07.06 — Agregar un catálogo sin inflar la cartera

## Propósito, entradas y resultado

Practica la [lección 07.06](../../../curriculum/07_tidyverse/06_join_tables/README.md)
en el mismo proyecto RStudio/IDE. Prepara una vez sus tres archivos según la
lección: funciones, ejecutor y catálogo sintético. No hay paquetes nuevos.
Usa los 29 aceptados de 07.04 y conserva las 44 entradas y sus rechazos.

Entrega output/mis_uniones.R con las tablas y comprobaciones reproducibles,
además de una explicación de claves, cardinalidad y cobertura. Mantén aparte
el error deliberado. No se pide exportar ni crear una figura. El proyecto y
checkpoint integrador siguen pendientes.

## 1. Predecir antes de unir

Lee las dos tablas. Identifica sus unidades, claves únicas y clave de unión.
Anticipa qué pasará con educacion, servicios y salud en left, inner y anti.
¿La presencia de servicios prueba que conocemos su etiqueta?

<details>
<summary>Comprobar el razonamiento</summary>

El detalle tiene un registro por ID/corte; el catálogo, uno por segmento.
Unimos por segmento, con relación muchos a uno desde el detalle. Left mantiene
los 29 aceptados. Inner conserva 19 coincidencias; anti desde el detalle devuelve
los 10 de educacion. Servicios coincide, pero su etiqueta queda NA en seis
registros. Anti desde el catálogo devuelve salud, una fila sin uso. Son unidades
distintas: una etiqueta de catálogo no es un crédito adicional.

</details>

## 2. Reconstruir las entradas

Abre el proyecto, reinicia R y comprueba getwd() en Console. Crea el script
en el editor, conserva la raíz de la práctica como directorio y ejecuta por bloques:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_transformacion.R", encoding = "UTF-8")
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_resumen.R", encoding = "UTF-8")
source("R/funciones_uniones.R", encoding = "UTF-8")
rutas <- c("datos/cartera_calidad.csv", "datos/catalogo_etiquetas.csv")
huellas <- tools::md5sum(rutas)
fuente <- leer_texto_conversion(rutas[1])
original <- fuente
revision <- evaluar_calidad(fuente)
detalle <- revision$aceptados
detalle_original <- detalle
catalogo <- leer_catalogo(rutas[2])
catalogo_original <- catalogo
```

Comprueba 29 aceptados, 15 rechazos y el catálogo único, sin normalizar texto
ni rellenar su etiqueta ausente. Explica las advertencias conocidas de 07.04.

<details>
<summary>Comprobación posible</summary>

```r
stopifnot(nrow(detalle) == 29L, nrow(revision$rechazados) == 15L,
          !anyDuplicated(detalle[c("id_credito", "fecha_corte")]),
          nrow(catalogo) == 4L, !anyNA(catalogo$segmento),
          !anyDuplicated(catalogo$segmento),
          is.na(catalogo$etiqueta_segmento[catalogo$segmento == "servicios"]))
```

El catálogo de etiquetas no cambia las reglas de aceptación de la cartera.
Conocer un saldo no significa conocer una etiqueta de presentación.

</details>

## 3. Investigar la cobertura y agregar columnas

Escribe semi_join y anti_join desde el detalle; luego invierte anti_join para
identificar claves sin uso. Declara by y na_matches en cada caso. Haz una unión
izquierda con marca de existencia y relación explícita, como en la lección.
Después compara con la función reutilizable:

```r
resultado <- unir_catalogo(detalle, catalogo)
comprobar_union(detalle, catalogo, resultado)
ampliado <- resultado$ampliado
print(resultado$controles, width = Inf)
```

<details>
<summary>Una solución y sus controles</summary>

```r
con_catalogo <- dplyr::semi_join(detalle, catalogo,
                                by = "segmento", na_matches = "never")
sin_catalogo <- dplyr::anti_join(detalle, catalogo,
                                by = "segmento", na_matches = "never")
sin_uso <- dplyr::anti_join(catalogo, detalle,
                            by = "segmento", na_matches = "never")
marcado <- catalogo |> dplyr::mutate(en_catalogo = TRUE)
propio <- detalle |>
  dplyr::left_join(marcado, by = "segmento", na_matches = "never",
                   relationship = "many-to-one") |>
  dplyr::mutate(en_catalogo = dplyr::coalesce(en_catalogo, FALSE))
stopifnot(nrow(con_catalogo) == 19L, nrow(sin_catalogo) == 10L,
          identical(sin_uso$segmento, "salud"),
          identical(as.list(propio), as.list(ampliado)),
          identical(resultado$controles$registros, c(29L, 19L, 10L)),
          identical(resultado$controles$saldo_observado_mxn, c(177250, 120250, 57000)),
          identical(as.list(ampliado[names(detalle)]), as.list(detalle)))
```

La unión conserva las 12 columnas originales y añade dos: 29 × 14. Las
dos partes conservan columnas originales; no son dos copias del detalle completo.
La marca distingue seis etiquetas desconocidas de diez faltas de coincidencia.

</details>

Calcula cobertura del catálogo y de etiqueta conocida respecto de los 29 registros.
Después escribe un inner_join y explica el cambio de población y saldo.

<details>
<summary>Resultados esperados</summary>

```r
cobertura_catalogo <- sum(ampliado$en_catalogo) / nrow(ampliado) * 100
cobertura_etiqueta <- sum(!is.na(ampliado$etiqueta_segmento)) / nrow(ampliado) * 100
interseccion <- dplyr::inner_join(detalle, catalogo,
                                  by = "segmento", na_matches = "never",
                                  relationship = "many-to-one")
stopifnot(abs(cobertura_catalogo - 19 / 29 * 100) < 1e-10,
          abs(cobertura_etiqueta - 13 / 29 * 100) < 1e-10,
          nrow(interseccion) == 19L, suma_observada(interseccion$saldo_mxn) == 120250)
```

Coberturas aproximadas: 65.52 % y 44.83 %. La cobertura de saldo sigue siendo
100 %. Inner responde sobre 19 coincidencias, deja fuera 10 registros y
57000 MXN. No prueba que esos créditos sean incorrectos.

</details>

## 4. Detectar la multiplicación

Crea catalogo_repetido añadiendo otra vez comercio. En un ensayo separado
del resultado correcto, ejecuta left_join sin relationship, lee la advertencia
y comprueba por qué aparecen 37 filas y 224250 MXN. No modifiques el catálogo original.

<details>
<summary>Ensayo incorrecto para diagnosticar</summary>

```r
catalogo_repetido <- dplyr::bind_rows(catalogo, catalogo[1, ])
inflado <- dplyr::left_join(detalle, catalogo_repetido,
                           by = "segmento", na_matches = "never")
stopifnot(nrow(inflado) == 37L, suma_observada(inflado$saldo_mxn) == 224250,
          identical(catalogo, catalogo_original))
```

Ocho filas de comercio encuentran dos coincidencias; sus 47000 MXN se cuentan
dos veces. La advertencia señala muchos a muchos. Sin embargo, una relación
uno a muchos puede ampliar filas sin esa advertencia predeterminada. La
prevención depende del contrato declarado y de validar el catálogo completo.

</details>

Este bloque aislado debe producir **error esperado**. Déjalo fuera del script
de reconstrucción correcta:

```r
# ERROR ESPERADO: ejecutar por separado.
dplyr::left_join(detalle, catalogo_repetido, by = "segmento",
                  na_matches = "never", relationship = "many-to-one")
```

No elimines filas con distinct ni selecciones una primera coincidencia para
hacer pasar el control. Explica qué evidencia necesitarías si hubiera dos
etiquetas distintas para el mismo segmento.

## 5. Probar ausencia y estabilidad

Reproduce las dos demostraciones pequeñas de la sección 8 de la lección en
objetos separados: ID sin corte genera cuatro combinaciones; NA con NA depende
de la política. No agregues esas filas a la cartera.

Luego invierte las filas del catálogo: las etiquetas asignadas a cada crédito
deben permanecer iguales. Prueba también un detalle vacío:

```r
invertido <- unir_catalogo(detalle, catalogo[nrow(catalogo):1, ])
stopifnot(identical(as.list(invertido$ampliado), as.list(ampliado)))
vacio <- unir_catalogo(detalle[0, ], catalogo)
comprobar_union(detalle[0, ], catalogo, vacio)
stopifnot(nrow(vacio$ampliado) == 0L,
          nrow(vacio$catalogo_sin_uso) == 4L,
          all(is.na(vacio$controles$saldo_observado_mxn)))
```

El vacío no informa saldo observado cero. No tiene créditos y todas las filas
de catálogo quedan sin uso. Invertir un catálogo único no cambia correspondencias.

**Ampliación opcional:** consulta unmatched = "error" en la lección. Explica
por qué en left_join controlaría salud sin uso y no exigiría coincidencia para
educacion. Para exigir cobertura completa del detalle, ¿qué resultado de anti_join
necesitarías comprobar? No es necesario convertir este ejercicio en cobertura completa.

## 6. Reiniciar y registrar evidencia

Guarda el script correcto y conserva el bloque de error aparte. Usa Session >
Restart R sin recuperar objetos anteriores. Desde Console en la raíz de la práctica:

```r
source("output/mis_uniones.R", encoding = "UTF-8")
source("unir_cartera.R", encoding = "UTF-8")
stopifnot(identical(fuente, original), identical(detalle, detalle_original),
          identical(catalogo, catalogo_original), identical(huellas, tools::md5sum(rutas)))
```

También puedes usar Source desde el editor. Conserva script, versiones,
contrato, coincidencias/no coincidencias y conciliación 29 = 19 + 10 y
177250 = 120250 + 57000 MXN. Las advertencias de conversión y del ensayo
inflado se explican. output/ está ignorado; no agregues con fuerza resultados
ni bibliotecas al repositorio.

Responde con tus palabras:

1. ¿Por qué segmento es clave del catálogo y no clave única del detalle?
2. ¿Qué distingue seis etiquetas ausentes de diez faltas de coincidencia?
3. ¿Qué conserva un semi_join que podría multiplicarse en un inner_join?
4. ¿Por qué relationship no garantiza cobertura completa?
5. ¿Por qué omitir corte puede relacionar una fila con otra fecha?
6. ¿Qué no comprobarías si solo revisaras que la suma global coincide?

Puedes avanzar cuando reconstruyas la unión, justifiques claves y política de NA,
detectes multiplicidad y conserves toda la evidencia. Registra resultado y dudas
en [PROGRESS.md](../../../PROGRESS.md); disponer del material no acredita aprendizaje.
No hay checkpoint integrador implementado asociado.

Siguiente: [07.07 — Datos ordenados y reshape](../../../curriculum/07_tidyverse/07_tidy_reshape/README.md). Volver a la [lección 07.06](../../../curriculum/07_tidyverse/06_join_tables/README.md).

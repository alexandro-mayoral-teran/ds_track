# Lab 07.09 — Interpretar fechas y comparar cortes con la misma base

## Propósito, entradas y resultado

Practica la [lección 07.09](../../../curriculum/07_tidyverse/09_dates_cutoffs/README.md)
en el mismo proyecto RStudio/IDE. Prepara sus dos archivos y restaura el lockfile:
lubridate/timechange se añaden a la biblioteca local, con respaldo de metadatos.
No se modifica Conda ni se inicializa otro proyecto renv.

Usa las 48 entradas de datos/cartera_texto.csv, conservadas desde 07.08. Entrega
output/mis_fechas.R, tablas, comprobaciones y una explicación de fechas, claves,
fronteras y población comparable. No partas solo de los 45 segmentos reconocidos.
No se pide exportar, graficar ni crear un checkpoint integrador, todavía pendiente.

## 1. Predecir antes de convertir

Clasifica "2026-09-30", "2026-09-31", "2026-10-3", "30/09/2026", "   " y
NA_character_. Añade "2101-01-01". Explica qué diferencia hay entre calendario
válido, forma acordada y rango didáctico. ¿Puede una fecha válida fallar otra regla?

<details>
<summary>Comprobar el razonamiento</summary>

Solo la primera pasa el contrato de ejemplo. El día 31 no existe en septiembre;
las dos escrituras siguientes incumplen YYYY-MM-DD; blanco/NA son ausentes;
2101 está fuera del rango 1900–2100. Un alta posterior al corte falla la relación
aunque ambas fechas existan. Una clave repetida también debe investigarse.

</details>

## 2. Reconstruir desde la fuente original

Abre la práctica, reinicia R y comprueba getwd() en Console. Crea el script
en el editor manteniendo la raíz de la práctica como directorio:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
ruta <- "datos/cartera_texto.csv"
huella <- tools::md5sum(ruta)
fuente <- leer_texto_segmentos(ruta)
original <- fuente
resultado <- preparar_fechas(fuente)
trabajo <- resultado$trabajo
aceptados <- resultado$aceptados
rechazados <- resultado$rechazados
```

Inspecciona los cuatro textos *_original y las dos fechas Date. Lee las
advertencias esperadas de calendario inválido; consulta sus filas y motivos.

## 3. Conservar todas las reglas y las dos partes

Explica los casos 12, 14, 18, 43 y 44. Comprueba conteos, importes y la
reconstrucción, sin reparar las entradas para hacerlas pasar.

<details>
<summary>Controles y razonamiento</summary>

```r
comprobar_fechas(fuente, resultado)
stopifnot(identical(dim(trabajo), c(48L, 15L)),
          identical(resultado$controles$registros, c(48L, 36L, 12L)),
          identical(resultado$controles$saldo_observado_mxn, c(112800, 81400, 31400)),
          sum(as.matrix(resultado$banderas)) == 12L,
          identical(rechazados$numero_registro, c(5L,9L,12L,14L,18L,23L,30L,33L,43L,44L,47L,48L)))
```

12 tiene alta posterior al corte y diferencia −1 día; 14 tiene fecha imposible;
18 no tiene corte. 43/44 colisionan después de recortar ID, con igual corte:
se rechazan ambas apariciones, no una primera por conveniencia. Los 36 aceptados
pasaron este contrato declarado; los 12 rechazados conservan texto y motivos.
La suma de partes incluye varios cortes y no es saldo de una única fecha.

</details>

Calcula aparte los días desde 2026-08-01 hasta 2026-09-30 y el inicio del mes
del corte. Explica por qué esos 60 días no representan días de atraso.

## 4. Seleccionar períodos con límites explícitos

Selecciona septiembre y octubre de 2026 con inicio incluido y fin excluido.
Resume por fecha interpretada y comprueba cuántas diferencias de días son conocidas.

<details>
<summary>Solución razonada</summary>

```r
septiembre <- seleccionar_periodo(aceptados,
  lubridate::ymd("2026-09-01"), lubridate::ymd("2026-10-01"))
octubre <- seleccionar_periodo(aceptados,
  lubridate::ymd("2026-10-01"), lubridate::ymd("2026-11-01"))
resumen <- resumir_cortes_fechas(aceptados)
stopifnot(identical(resumen$registros, c(18L, 18L)),
          identical(resumen$saldo_observado_mxn, c(39900, 41500)),
          identical(resumen$dias_conocidos, c(18L, 18L)),
          sum(!is.na(trabajo$dias_desde_alta)) == 42L)
```

En el trabajo hay 42 diferencias evaluables; en aceptados, 36/36. No se usa
una ausencia como cero días. Las medias aceptadas son aproximadamente 48.83
y 80.94 días por corte, con base 18 cada una. Son antigüedades observadas de
esas poblaciones, no tasas de atraso ni prueba de que ambas contengan los mismos IDs.

</details>

Reproduce la demostración de fronteras de la sección 7 de la lección. Anticipa
qué pasa con el 1 de octubre y con el 1 de noviembre. Este bloque aislado
produce **error esperado**, por usar texto en los límites; déjalo fuera del
script correcto:

```r
# ERROR ESPERADO: ejecutar por separado.
seleccionar_periodo(aceptados, "2026-10-01", "2026-11-01")
```

## 5. Comparar los mismos IDs

Construye una tabla con un saldo de septiembre y otro de octubre por ID.
Exige uno a uno y conserva los IDs sin correspondencia por ambos lados.
Calcula la diferencia como octubre menos septiembre, sobre la misma base.

<details>
<summary>Una solución y sus límites</summary>

```r
comparables <- dplyr::inner_join(
  septiembre |> dplyr::select(id_credito, saldo_sep = saldo_mxn),
  octubre |> dplyr::select(id_credito, saldo_oct = saldo_mxn),
  by = "id_credito", relationship = "one-to-one", na_matches = "never"
) |> dplyr::mutate(diferencia_mxn = as.double(saldo_oct) - saldo_sep)
solo_sep <- dplyr::anti_join(septiembre, octubre, by = "id_credito", na_matches = "never")
solo_oct <- dplyr::anti_join(octubre, septiembre, by = "id_credito", na_matches = "never")
stopifnot(nrow(comparables) == 14L, nrow(solo_sep) == 4L, nrow(solo_oct) == 4L,
          sum(comparables$saldo_sep) == 29000,
          sum(comparables$saldo_oct) == 31800,
          sum(comparables$diferencia_mxn) == 2800)
```

Son 14 de los 18 IDs aceptados por corte. El cambio de 2800 MXN describe esa
base común; no es la diferencia de 1600 entre las sumas de dos poblaciones
distintas. Las cuatro observaciones sin correspondencia por lado no son
automáticamente altas/bajas reales: conserva su evidencia y explica la selección.

</details>

No unas todo el histórico solo por ID. La selección de un corte por tabla y
la clave única comprobada son lo que permite aquí una relación uno a uno.

## 6. Reiniciar y conservar evidencia

Guarda output/mis_fechas.R con carga, reglas, selecciones y comparación correctas;
conserva el error esperado aparte. Usa Session > Restart R, sin recuperar objetos
anteriores. Desde Console en la raíz de la práctica:

```r
source("output/mis_fechas.R", encoding = "UTF-8")
source("revisar_fechas.R", encoding = "UTF-8")
stopifnot(identical(fuente, original), identical(huella, tools::md5sum(ruta)))
```

También puedes usar Source desde el editor. Conserva script, versiones,
metadatos respaldados, textos originales, motivos, partición 48 = 36 + 12,
límites de los períodos y base común de 14 IDs. output/ y las bibliotecas están
ignorados; no los agregues con fuerza al repositorio.

Responde con tus palabras:

1. ¿Qué diferencia hay entre una fecha ausente y otra imposible?
2. ¿Por qué ymd por sí solo no garantiza la forma exigida?
3. ¿Por qué convertir dos fechas correctamente no valida su relación ni la clave?
4. ¿Qué unidad mide dias_desde_alta y qué pregunta no responde?
5. ¿Qué evita usar un fin exclusivo? ¿Por qué comparar solo el número de mes puede fallar?
6. ¿Por qué 18 registros en ambos cortes no significa que sean comparables uno a uno?

Puedes avanzar cuando reconstruyas y expliques fechas, motivos, unidades y
población comparable. Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md);
disponer del material no acredita aprendizaje. No hay checkpoint integrador
implementado asociado.

Siguiente: [07.10 — Primera figura y cierre del análisis](../../../curriculum/07_tidyverse/10_first_plot_closure/README.md).
Volver a la [lección 07.09](../../../curriculum/07_tidyverse/09_dates_cutoffs/README.md).

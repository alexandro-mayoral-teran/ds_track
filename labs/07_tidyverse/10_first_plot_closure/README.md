# Lab 07.10 — Primera figura y cierre del análisis

## Propósito y entradas

Reconstruir desde el CSV original un análisis con rechazos conservados y entregar
una figura cuyo saldo y población puedas explicar. Lee primero la
[lección 07.10](../../../curriculum/07_tidyverse/10_first_plot_closure/README.md).
Requiere 07.09 y el mismo proyecto preparado/restaurado según esa lección.
No inicialices otro renv ni sustituyas datos/cartera_texto.csv por otra muestra.

Trabaja en RStudio o tu IDE: abre el proyecto, mantén su raíz como directorio,
crea output/mi_cierre_lab.R y ejecuta por bloques con Run. Usa Console de R,
no Terminal del sistema. Las exportaciones van en un script aparte para que
la reconstrucción no intente sobrescribir entregas.

## Actividad y resultados esperados

1. Escribe la pregunta, unidad (crédito/corte), fechas exactas y reglas de aceptación.
   Reconstruye desde las 48 entradas. Inspecciona 36 aceptados, 12 rechazos y
   sus motivos. Justifica por qué 81400 MXN no representa saldo a una fecha única.
2. Reconstruye pares por ID. Conserva ocho registros aceptados sin pareja y
   verifica 14 IDs comunes. Compara los 39900/41500 MXN de todos los aceptados
   por corte con 29000/31800 MXN de la base común. Explica qué pregunta responde cada par.
3. Dibuja desde datos_figura con ggplot, aes y geom_col. Identifica qué representa
   cada fila de la tabla y cada barra. Contrasta geom_bar sin peso sobre esa misma
   tabla: anticipa sus valores antes de ejecutar.
4. Añade título, MXN, fechas, tamaño/cobertura de la población y un límite de
   interpretación. Conserva base cero y un color fijo fuera de aes. Usa
   crear_figura_cierre como referencia después de intentar tu explicación.
5. Exporta una entrega nueva a output/entrega_lab_0710. Abre el PNG y compara
   etiquetas y alturas con el CSV. Relee y comprueba la entrega. No publiques
   sesion.txt sin revisar sus rutas locales.
6. Guarda y reinicia R con Session > Restart R. Ejecuta tu script completo y
   verifica la entrega sin cargar un workspace. Registra el procedimiento y una
   conclusión con cambio absoluto, denominador, cobertura y límites.

## Comprobación y solución razonada

<details>
<summary>Ver una reconstrucción de referencia después de intentarlo</summary>

Guarda estos bloques en mi_cierre_lab.R, salvo la exportación indicada aparte:

```r
source(".Rprofile")
stopifnot(isTRUE(renv::status()$synchronized))
source("R/funciones_calidad.R", encoding = "UTF-8")
source("R/funciones_texto.R", encoding = "UTF-8")
source("R/funciones_fechas.R", encoding = "UTF-8")
source("R/funciones_cierre.R", encoding = "UTF-8")
fuente <- leer_texto_segmentos("datos/cartera_texto.csv")
huella <- tools::md5sum("datos/cartera_texto.csv")
cierre <- construir_cierre(fuente)
comprobar_cierre(fuente, cierre)
stopifnot(identical(cierre$resultado$controles$registros, c(48L, 36L, 12L)),
          identical(cierre$resumen_cortes$saldo_observado_mxn, c(39900, 41500)),
          nrow(cierre$comunes) == 14L,
          identical(cierre$datos_figura$saldo_mxn, c(29000, 31800)),
          nrow(cierre$sin_pareja) == 8L,
          sum(cierre$comunes$diferencia_mxn) == 2800,
          identical(huella, tools::md5sum("datos/cartera_texto.csv")))
print(cierre$datos_figura)
figura <- crear_figura_cierre(cierre)
print(figura)
```

Las advertencias de calendario se conservan y pueden repetirse al reconstruir.
Inspecciona los motivos, no corrijas el CSV para lograr que desaparezcan.
El 9.66% usa (31800 − 29000) / 29000 × 100; la cobertura usa 14/18.
No confundir porcentaje de variación del saldo con porcentaje de créditos.
Las barras son dos sumas verificadas. geom_bar sin peso contaría 1 y 1.

Ejecuta aparte una sola vez, eligiendo una ruta nueva si ya existe:

```r
exportar_cierre(cierre, "output/entrega_lab_0710")
comprobar_entrega(fuente, "output/entrega_lab_0710")
```

La entrega conserva también la fuente, banderas y originales en analisis.rds.
Los CSV permiten inspeccionar tablas; no preservan por sí solos clases Date ni
la diferencia entre texto vacío y NA. El verificador compara las tablas, no la
correspondencia de los píxeles con ellas: la revisión visual sigue siendo necesaria.

Después de reiniciar R, ejecuta en Console:

```r
source("output/mi_cierre_lab.R", encoding = "UTF-8")
source("verificar_cierre.R", encoding = "UTF-8")
verificar_entrega_cierre("output/entrega_lab_0710")
```

Esperado: datos idénticos y entrega conciliada, sin reexportar. No se pide
igualdad binaria del PNG entre equipos. No hay evidencia de causas del cambio
ni de representatividad de los 14 IDs para los demás créditos.

</details>

## Fronteras y errores que debes poder explicar

<details>
<summary>Ver comprobaciones de ausencia de pares y alteración</summary>

Con una selección de solo septiembre desaparecen los pares. Se conservan las
tablas, pero no se fabrican dos barras de cero:

```r
solo_septiembre <- fuente |> dplyr::filter(fecha_corte == "2026-09-30")
sin_base <- construir_cierre(solo_septiembre)
stopifnot(nrow(sin_base$comunes) == 0L,
          all(is.na(sin_base$datos_figura$saldo_mxn)))
```

Ejecuta el error esperado por separado; no lo dejes en tu script de reconstrucción:

```r
# ERROR ESPERADO: no hay base comun para graficar.
crear_figura_cierre(sin_base)
```

Alterar valores compensados puede conservar una suma y seguir siendo incorrecto:

```r
alterado <- cierre
alterado$comunes$saldo_sep[1:2] <- alterado$comunes$saldo_sep[1:2] + c(10L, -10L)
stopifnot(sum(alterado$comunes$saldo_sep) == sum(cierre$comunes$saldo_sep))
```

Ejecuta aparte:

```r
# ERROR ESPERADO: conservar el total no conserva los datos de cada ID.
comprobar_cierre(fuente, alterado)
```

</details>

## Evidencia, reflexión y salida

Conserva script propio, entrega, comprobación desde sesión nueva y explicación
de tres a cinco frases. Incluye una duda o corrección encontrada. Anota evidencia
y lo que aún necesitas practicar en [PROGRESS.md](../../../PROGRESS.md) sin
marcar por adelantado competencias como adquiridas. Los archivos de práctica
permanecen locales; el proyecto integrador no tiene carpeta ni checkpoint activo.

- ¿Qué cambia si comparas todos los aceptados en vez de los mismos IDs?
- ¿Por qué dos filas resumidas producirían barras de altura uno con geom_bar?
- ¿Qué representa el eje cero y qué perderías si lo recortaras?
- ¿Por qué una base vacía y un saldo observado igual a cero son distintos?
- ¿Qué comprueba la relectura y qué requiere inspeccionar el PNG?
- ¿Qué necesitarías para hablar de causas o generalizar el cambio?

Cierra cuando puedas reconstruir y justificar esos puntos. Revisa los
[pendientes del módulo](../../../docs/tidyverse-closure.md).
Siguiente: [08.01 — Pregunta y gramática de gráficos](../../../curriculum/08_visualization_r/01_question_grammar/README.md),
ya disponible. Volver a la [lección 07.10](../../../curriculum/07_tidyverse/10_first_plot_closure/README.md).

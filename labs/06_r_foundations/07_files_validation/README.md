# Lab 06.07 — Leer, separar y comprobar una entrega CSV

**Tiempo orientativo:** 90–120 minutos, repartibles entre sesiones.

## Propósito, entradas y preparación

Aplica la [lección 06.07](../../../curriculum/06_r_foundations/07_files_validation/README.md).
Necesitas tablas, funciones, condiciones y ciclos de 06.05–06.06. La entrada es
[ventas_entrada.csv](../../../curriculum/06_r_foundations/07_files_validation/ventas_entrada.csv),
con 14 registros ficticios. No requiere paquetes externos ni proyecto/checkpoint
implementado asociado.

Trabaja desde la raíz en una sesión nueva. Carga solo las definiciones y
elige rutas para tu práctica; conserva intactas las muestras del curso:

```r
source("curriculum/06_r_foundations/06_functions_control/funciones_ventas.R", encoding = "UTF-8")
source("curriculum/06_r_foundations/07_files_validation/funciones_archivos.R", encoding = "UTF-8")
entrada_lab <- file.path("curriculum", "06_r_foundations", "07_files_validation", "ventas_entrada.csv")
destino_lab <- file.path("labs", "06_r_foundations", "07_files_validation", "output", "revision_original")
```

Las soluciones forman un recorrido secuencial; guárdalo en un script personal
bajo `output/` de este lab, ignorado por Git. Cambia el destino por una carpeta
nueva si ya lo usaste. No borres entregas anteriores para repetir la práctica.

## 1. Leer el contrato antes que los números

Predice los nombres, dimensiones y tipos que obtendrás con `leer_ventas`.
Identifica separador, decimal y codificación. Recupera la nota de V007, las
unidades de V005 y el texto de unidades de V008. Explica por qué las tres
lecturas son texto y cómo distinguirás un faltante de un error.

<details>
<summary>Solución razonada: conservar campos antes de convertir</summary>

```r
print(getwd())
print(file.exists(entrada_lab)) # TRUE desde la raiz.
crudos_lab <- leer_ventas(entrada_lab)
print(names(crudos_lab)) # id_venta unidades precio_mxn nota
print(dim(crudos_lab)) # 14 4
str(crudos_lab) # Cuatro columnas character.
print(crudos_lab$nota[crudos_lab$id_venta == "V007"]) # "México, mostrador"
print(crudos_lab$unidades[5]) # "", campo vacio conservado.
print(crudos_lab$unidades[8]) # "dos", texto invalido conservado.
```

La coma dentro de las comillas de V007 pertenece a una nota. UTF-8 conserva
el acento; elegir otra codificación no se arregla cambiando el separador.
`""` es faltante permitido solo según las reglas de cada columna; `dos` no es
un número de este contrato. Un `NA` generado al convertir sin registro del
origen no permitiría distinguir ambas situaciones.

</details>

## 2. Separar registros y explicar todos los duplicados

Antes de ejecutar, identifica los seis registros que deben rechazarse y sus
motivos. Valida y muestra `fila_origen`, identificador, texto y motivo.
Explica por qué se rechazan las dos apariciones de V010 y por qué V005/V006
se aceptan aunque no tengan importe conocido. Concilia los conteos.

<details>
<summary>Solución razonada: 14 entradas = 8 aceptados + 6 rechazos</summary>

```r
revision_lab <- validar_registros(crudos_lab)
print(revision_lab$controles) # 14 8 6
print(revision_lab$rechazos)
# Filas 8, 9, 10, 11, 12 y 13, en el orden de entrada.
print(revision_lab$aceptados$id_venta) # V001 V002 V003 V004 V005 V006 V007 V014
print(revision_lab$controles$n_aceptados + revision_lab$controles$n_rechazados) # 14
```

Los motivos son unidades inválidas en 8/9, identificador repetido en 10/11,
identificador inválido en 12 y precio inválido en 13. V005/V006 cumplen el
contrato de faltantes permitidos. No sabemos qué aparición de V010 es la
correcta: elegir la primera ocultaría una decisión no respaldada por datos.

</details>

## 3. Resumir con dos denominadores

Calcula conocidos, faltantes, cobertura y suma/media observadas de los
aceptados. Explica por qué «75% de los datos» es ambiguo y por qué 765.5 MXN
no es el total de las 14 entradas. Comprueba grupos con umbral 200.

<details>
<summary>Solución razonada: aceptación y cobertura son preguntas diferentes</summary>

```r
resumen_lab <- resumir_importes(revision_lab$aceptados$importe_mxn)
print(resumen_lab) # 8 registros, 6 conocidos, 2 faltantes; cobertura 75.
print(resumen_lab$suma_observada_mxn) # 765.5
print(resumen_lab$media_observada_mxn) # 127.5833 aproximadamente.
print(resumen_lab$total_mxn) # NA
print(c(resumen_lab$n_cumplen, resumen_lab$n_no_cumplen, resumen_lab$n_pendientes)) # 2 4 2
```

«Se aceptaron 8 de 14 registros; se conocen 6 de sus 8 importes, con cobertura
75%. Los importes observados suman 765.5 MXN y su media es 127.5833 MXN
aproximadamente; el total de los aceptados sigue desconocido». Los seis
rechazos se informan aparte y no entran en ese resumen.

</details>

## 4. Revisar variantes sin modificar la fuente

En una copia textual confirma precio `"60"` para V006 y vuelve a validar y
resumir. Debes conservar 8 aceptados/6 rechazos, pero conocer 7 importes:
cobertura 87.5%, suma 885.5 y media 126.5. Demuestra que la tabla original
sigue igual. En otra copia agrega `"dos"` a unidades de la primera V010:
¿se conserva tanto el motivo de duplicado como el numérico?, ¿se cuenta dos veces?

<details>
<summary>Solución razonada: cobertura nueva y motivos acumulados</summary>

```r
confirmadas_lab <- crudos_lab
confirmadas_lab$precio_mxn[confirmadas_lab$id_venta == "V006"] <- "60"
revision_confirmada_lab <- validar_registros(confirmadas_lab)
resumen_confirmado_lab <- resumir_importes(revision_confirmada_lab$aceptados$importe_mxn)
print(resumen_confirmado_lab) # 8/7/1; cobertura 87.5; suma 885.5; media 126.5.
print(crudos_lab$precio_mxn[6]) # "": la tabla original no cambio.
variante_lab <- crudos_lab
variante_lab$unidades[10] <- "dos"
revision_multiple_lab <- validar_registros(variante_lab)
print(revision_multiple_lab$rechazos$motivo[revision_multiple_lab$rechazos$fila_origen == 10])
# "id_repetido;unidades_invalidas"
print(revision_multiple_lab$controles) # Sigue 14 8 6, no siete rechazos.
```

Dos problemas en una fila no equivalen a dos registros rechazados. Guardamos
la evidencia en la copia; no reescribimos el CSV fuente con la confirmación
ficticia ni imputamos precios a las ventas que siguen incompletas.

</details>

## 5. Exportar y comprobar archivos reales

Exporta la revisión **original** en una carpeta nueva del lab. Relee los
aceptados y rechazos como texto y los controles como enteros. Comprueba
nombres de columnas, cantidad de filas, nota con acento/coma, texto inválido
de V008 y sus motivos. Confirma que no apareció una columna extra de índice.

<details>
<summary>Solución razonada: comprobar más que la presencia de archivos</summary>

```r
carpeta_lab <- exportar_revision(revision_lab, resumen_lab, destino_lab)
print(list.files(carpeta_lab))
aceptados_releidos_lab <- read.csv(file.path(carpeta_lab, "aceptados.csv"),
  colClasses = "character", na.strings = character(0),
  check.names = FALSE, fileEncoding = "UTF-8")
rechazos_releidos_lab <- read.csv(file.path(carpeta_lab, "rechazos.csv"),
  colClasses = "character", na.strings = character(0),
  check.names = FALSE, fileEncoding = "UTF-8")
controles_releidos_lab <- read.csv(file.path(carpeta_lab, "controles.csv"), colClasses = "integer")
print(names(aceptados_releidos_lab)) # fila_origen id_venta unidades precio_mxn importe_mxn nota
print(dim(aceptados_releidos_lab)) # 8 6
print(dim(rechazos_releidos_lab)) # 6 6
print(aceptados_releidos_lab$nota[aceptados_releidos_lab$id_venta == "V007"])
print(rechazos_releidos_lab$unidades[rechazos_releidos_lab$id_venta == "V008"]) # "dos"
print(identical(rechazos_releidos_lab$motivo, revision_lab$rechazos$motivo)) # TRUE
print(controles_releidos_lab) # 14 8 6
importe_texto_lab <- aceptados_releidos_lab$importe_mxn
importe_texto_lab[importe_texto_lab == "NA"] <- NA_character_
importes_releidos_lab <- as.double(importe_texto_lab)
print(isTRUE(all.equal(importes_releidos_lab, revision_lab$aceptados$importe_mxn, tolerance = 1e-12))) # TRUE
print(resumir_importes(importes_releidos_lab)$suma_observada_mxn) # 765.5
```

Aquí releemos una entrega que acabamos de generar; no ignoramos avisos de
conversión. El script completo transforma esos avisos en error. Las notas se
mantienen como texto para no reinterpretar una nota literal `NA` como faltante.
`fila_origen` es trazabilidad deliberada, no una columna accidental de nombres
de fila. La relectura numérica comprueba los importes guardados con tolerancia.

</details>

## 6. Vacío, todos rechazados y estructura incompatible

Dentro de la carpeta nueva del ejercicio anterior crea un CSV con **solo
cabecera** usando `writeLines`. Léelo, valida y resume. Contrasta con una tabla
que contenga únicamente los registros 8/9, ambos rechazados. Después crea
otro archivo de práctica con un registro de solo tres campos y prueba su
lectura **por separado**: debe fallar, no aparecer como venta con un campo rellenado.

<details>
<summary>Solución razonada: ausencia de filas frente a problemas de datos</summary>

```r
solo_cabecera_lab <- file.path(carpeta_lab, "solo_cabecera.csv")
writeLines("id_venta,unidades,precio_mxn,nota", solo_cabecera_lab, useBytes = TRUE)
vacios_lab <- leer_ventas(solo_cabecera_lab)
revision_vacia_lab <- validar_registros(vacios_lab)
print(dim(vacios_lab)) # 0 4
print(revision_vacia_lab$controles) # 0 0 0
print(resumir_importes(revision_vacia_lab$aceptados$importe_mxn)) # Sin base: indicadores NA.
revision_rechazada_lab <- validar_registros(crudos_lab[c(8, 9), , drop = FALSE])
print(revision_rechazada_lab$controles) # 2 0 2
```

`writeLines` escribe líneas de texto con salto final. Se usa para una muestra
pequeña controlada; para tablas usamos `write.csv`. Al validar la selección
8/9 como otra entrada en memoria, `fila_origen` empieza de nuevo en 1: esa
columna es posición **en la entrada recibida**, no una clave global.

Ejecuta el siguiente bloque por separado del script correcto:

```r
# Error deliberado: la fila de datos tiene tres campos, no cuatro.
estructura_mala_lab <- file.path(carpeta_lab, "estructura_mala.csv")
writeLines(c("id_venta,unidades,precio_mxn,nota", "V001,4,75"), estructura_mala_lab, useBytes = TRUE)
leer_ventas(estructura_mala_lab)
```

</details>

## 7. Conservar fuentes y entregas anteriores

Intenta volver a exportar al mismo destino **por separado**. Debe fallar sin
reescribir los cuatro archivos. Relee el CSV fuente y compara con la tabla
textual inicial. Para ejecutar otra variante, elige una carpeta nueva y usa
el recorrido con argumentos de la lección.

<details>
<summary>Solución razonada: rechazo de sobrescritura y fuente conservada</summary>

```r
print(identical(leer_ventas(entrada_lab), crudos_lab)) # TRUE
```

```r
# Error deliberado: esta entrega ya existe.
exportar_revision(revision_lab, resumen_lab, destino_lab)
```

La igualdad textual no compara los bytes originales; también conserva el
archivo fuente sin editarlo. Una falla de escritura puede dejar una carpeta
parcial: no la borres ni la presentes como comprobada. Esta práctica no promete
atomicidad de una entrega de varios archivos.

</details>

## Evidencia, comprobación y reflexión

Conserva script, versión/sesión, las cuatro tablas exportadas y una nota con
14 = 8 + 6, grupos 2/4/2, cobertura 6/8 y suma observada 765.5. Añade la
variante 885.5/126.5, el caso con motivos múltiples, vacío 0/0/0 frente a
todos rechazados 2/0/2 y los errores separados. Reinicia R y ejecuta tu copia
correcta con Rscript desde la raíz; usa un destino nuevo para que termine
con código 0. No publiques `output/` ni cambies el estado del estudiante sin
revisar su evidencia.

Explica con tus palabras:

1. ¿Qué información perderías al convertir `dos` directamente a un faltante?
2. ¿Por qué leer sin errores no acredita calidad de los registros?
3. ¿Qué reglas hacen aceptables a V005/V006 pero rechazan ambas V010?
4. ¿Qué denominador utiliza cada porcentaje que informaste?
5. ¿Cómo sabes que el CSV conserva campos y resultados, aunque no clases R?

Registra evidencia real y dudas en tu bitácora personal junto a la práctica.
Después sigue el [06.08 — Proyectos y dependencias con renv](../../../curriculum/06_r_foundations/08_projects_renv/README.md). Volver a la [lección 06.07](../../../curriculum/06_r_foundations/07_files_validation/README.md).

# Lab 09.04 — Escribir y recuperar una tabla desde R

## Propósito y entradas

Practicar [09.04 — Leer y escribir desde R](../../../curriculum/09_arrow_parquet/04_r_read_write/README.md).
Prepara el proyecto y restaura su biblioteca como indica la lección. Trabaja
desde su raíz en el IDE, con Console de R. No necesitas una entrega Python ni
reconstruir ejemplos de cartera de otros módulos.

Tienes `R/contrato_0902.R`, `R/intercambio_parquet.R`, `ejecutar_parquet.R` y
`datos/base_comun_0904.csv`. El CSV contiene 28 filas, 14 IDs en dos fechas;
clave ID/fecha, texto de tres dígitos, fecha entre 1900–2100 y saldo entero
no negativo hasta 2 147 483 647. No admite ausencias. Saldos esperados:
29 000 MXN en septiembre de 2026 y 31 800 en octubre. Usa carpetas nuevas;
no edites las entradas ni reemplaces entregas anteriores.

## Actividad

1. En un script propio define una muestra de **dos créditos** (`"201"`, `"202"`)
   al 31 de octubre de 2026 con saldos `0L` y `1500L`. Declara el esquema no
   anulable `string/date32/int32`, escribe a `output/lab_09_04_mini/` y relee.
   Comprueba tipos, esquema y ambos valores. Explica por qué el cero se conserva.
2. Carga la base común y crea una entrega en `output/lab_09_04_base/` mediante
   las funciones de la lección. Reinicia R y verifica el Parquet contra el CSV.
3. Crea **en memoria** otra tabla con las mismas filas en orden inverso. ¿Debe
   ser aceptada como equivalente? Compruébalo por clave.
4. En otra copia intercambia los saldos de las dos primeras filas de septiembre.
   El total de ese corte sigue siendo el mismo: comprueba que la comparación
   completa detecta el cambio. Guarda la alteración solo en otra carpeta de lab
   si quieres probar también el verificador de archivos.
5. Lee los 23 casos de `datos/casos_contrato_0904.csv`, aplica las reglas a sus
   tres columnas y compara motivos esperados. Explica por qué no se puede
   convertir/exportar todo el lote como si fuera una base válida.

## Resultado y comprobación

- Muestra propia con dos filas, suma 1500 y esquema no anulable.
- Entrega común con 28 filas y esquema real comprobado; cada clave/valor coincide.
- Orden invertido aceptado; saldos intercambiados rechazados con sumas conservadas.
- Casos separados: cinco aceptados, dieciocho rechazados y motivos conservados.
- Verificación desde sesión nueva sin recrear la carpeta de la entrega.

<details>
<summary>Una solución razonada</summary>

Primero, en la raíz del proyecto de práctica, carga las funciones y construye
la muestra propia. Se valida antes de convertir y se comprueba otra vez al leer:

```r
source("R/contrato_0902.R", encoding = "UTF-8")
source("R/intercambio_parquet.R", encoding = "UTF-8")
propia <- data.frame(id_credito = c("201", "202"),
  fecha_corte = as.Date(c("2026-10-31", "2026-10-31")),
  saldo_mxn = c(0L, 1500L))
propia_arrow <- crear_tabla_cartera(propia)
carpeta <- "output/lab_09_04_mini"
stopifnot(!file.exists(carpeta), dir.create(carpeta, recursive = TRUE))
archivo <- file.path(carpeta, "propia.parquet")
arrow::write_parquet(propia_arrow, archivo, version = "2.6", compression = "snappy")
vuelta <- arrow::read_parquet(archivo, as_data_frame = FALSE)
comparar_carteras(propia_arrow, vuelta)
stopifnot(identical(as.data.frame(vuelta)$saldo_mxn, c(0L, 1500L)))

base <- cargar_cartera()
esperada <- crear_tabla_cartera(base)
print(crear_entrega_r("output/lab_09_04_base"))
invertida <- crear_tabla_cartera(base[nrow(base):1L, , drop = FALSE])
comparar_carteras(esperada, invertida)
```

Las filas se comparan tras ordenar por clave; cambiar el orden no cambia qué
saldo corresponde a cada crédito. En cambio, intercambiar importes sí cambia
el contenido aunque se conserve la suma del corte:

```r
alterada <- base
posiciones <- which(alterada$fecha_corte == as.Date("2026-09-30"))[1:2]
stopifnot(length(unique(alterada$saldo_mxn[posiciones])) == 2L)
alterada$saldo_mxn[posiciones] <- rev(alterada$saldo_mxn[posiciones])
alterada_arrow <- crear_tabla_cartera(alterada)
stopifnot(identical(resumir_cartera(esperada), resumir_cartera(alterada_arrow)))
error <- tryCatch({
  comparar_carteras(esperada, alterada_arrow)
  NULL
}, error = function(e) e)
stopifnot(inherits(error, "error"))
print(conditionMessage(error))

casos <- leer_textos_contrato("datos/casos_contrato_0904.csv",
  c("caso", columnas_contrato, "motivos_esperados"))
evaluados <- evaluar_contrato(casos[columnas_contrato])
stopifnot(sum(evaluados$diagnostico$aceptado) == 5L,
  sum(!evaluados$diagnostico$aceptado) == 18L,
  identical(evaluados$diagnostico$motivos, casos$motivos_esperados))
```

`tryCatch()` captura aquí el fallo **esperado** para inspeccionarlo; no convierte
la tabla alterada en válida. No se ocultan errores del lector o de la entrega.
Los casos ilustran ausencias, calendario, rango y claves: las reglas preceden
a cualquier conversión. No se imputa cero ni se truncan fracciones.

Ahora guarda tu script, reinicia R y verifica desde archivos, sin depender
de `base`, `esperada` u otros objetos de la sesión anterior:

```r
source("R/contrato_0902.R", encoding = "UTF-8")
source("R/intercambio_parquet.R", encoding = "UTF-8")
resultado <- verificar_parquet_r("output/lab_09_04_base/base_comun.parquet")
stopifnot(identical(resultado$registros, c(14L, 14L)),
  identical(resultado$saldo_mxn, c(29000, 31800)))
print(resultado)
```

</details>

## Evidencia y reflexión

Conserva el script, las entregas y una explicación de los tipos observados,
el rechazo esperado y la verificación tras reiniciar. Registra qué pudiste
comprobar y qué sigue pendiente; una salida impresa no acredita comprensión.

- ¿Qué información del esquema se pierde si solo miras `str()` de la tabla R?
- ¿Por qué cero, ausencia y entero fuera de rango requieren decisiones diferentes?
- ¿Qué comprueba la comparación por clave que no prueban los dos totales?
- ¿Por qué no vuelves a crear la carpeta al verificar después del reinicio?

No hay proyecto/checkpoint implementado asociado. Después de comprobar y
explicar el lab, continúa con [09.05 — Intercambio Python y R](../../../curriculum/09_arrow_parquet/README.md#05-intercambio-python-y-r),
todavía planificada. Consulta los [pendientes de cierre](../../../docs/storage-closure.md).

# Funciones sin lecturas ni escrituras al hacer source().
# Cargar primero R/contrato_0902.R; se reutilizan sus reglas sin duplicarlas.
esquema_cartera <- function() {
  arrow::schema(
    arrow::field("id_credito", arrow::utf8(), nullable = FALSE),
    arrow::field("fecha_corte", arrow::date32(), nullable = FALSE),
    arrow::field("saldo_mxn", arrow::int32(), nullable = FALSE)
  )
}

exigir_textos <- function(textos) {
  resultado <- evaluar_contrato(textos)
  fallos <- resultado$diagnostico[!resultado$diagnostico$aceptado, , drop = FALSE]
  if (nrow(fallos)) {
    stop("Contrato incumplido (registro: motivos): ",
      paste(paste(fallos$numero_registro, fallos$motivos, sep = ": "), collapse = "; "))
  }
  resultado$tipados
}

cargar_cartera <- function(ruta = "datos/base_comun_0904.csv") {
  exigir_textos(leer_textos_contrato(ruta, columnas_contrato))
}

validar_cartera_r <- function(x) {
  if (!is.data.frame(x) || !identical(names(x), columnas_contrato) ||
      !identical(class(x$id_credito), "character") ||
      !identical(class(x$fecha_corte), "Date") ||
      !identical(class(x$saldo_mxn), "integer") || anyNA(x)) {
    stop("Se exige character/Date/integer, tres columnas en orden y sin NA")
  }
  dias <- as.numeric(x$fecha_corte)
  if (any(!is.finite(dias) | dias != floor(dias))) {
    stop("Date debe contener dias enteros finitos, sin fracciones ocultas")
  }
  # Conversion textual solo despues de comprobar tipos y presencia.
  textos <- data.frame(id_credito = x$id_credito,
    fecha_corte = format(x$fecha_corte, "%Y-%m-%d"),
    saldo_mxn = as.character(x$saldo_mxn), stringsAsFactors = FALSE)
  exigir_textos(textos)
  invisible(x)
}

validar_tabla_cartera <- function(tabla) {
  if (!inherits(tabla, "Table") ||
      !tabla$schema$Equals(esquema_cartera(), check_metadata = FALSE)) {
    stop("Esquema distinto: string/date32/int32 no anulables")
  }
  # Un esquema no prueba presencia, dominio ni unicidad: revisar tambien valores.
  x <- as.data.frame(tabla)
  validar_cartera_r(x)
  x
}

crear_tabla_cartera <- function(x) {
  validar_cartera_r(x)
  tabla <- arrow::arrow_table(x, schema = esquema_cartera())
  # El contrato esta en columnas/tipos; no depende de atributos privados de R.
  tabla$metadata <- NULL
  validar_tabla_cartera(tabla)
  tabla
}

comparar_carteras <- function(esperada, observada) {
  a <- validar_tabla_cartera(esperada)
  b <- validar_tabla_cartera(observada)
  ordenar <- function(x) {
    x <- x[order(x$id_credito, x$fecha_corte), , drop = FALSE]
    rownames(x) <- NULL
    x
  }
  if (!identical(ordenar(a), ordenar(b))) {
    stop("Valores o claves distintos de la fuente, aunque coincidan sumas")
  }
  invisible(TRUE)
}

resumir_cartera <- function(tabla) {
  x <- validar_tabla_cartera(tabla)
  fechas <- sort(unique(x$fecha_corte))
  # Sumar en double evita desbordar int32 al agregar; muestra acotada y exacta.
  # No promete enteros exactos por encima de 2^53 en otras bases.
  data.frame(fecha_corte = fechas,
    registros = vapply(seq_along(fechas), function(i) {
      sum(x$fecha_corte == fechas[i])
    }, integer(1)),
    saldo_mxn = vapply(seq_along(fechas), function(i) {
      sum(as.double(x$saldo_mxn[x$fecha_corte == fechas[i]]))
    }, double(1)))
}

verificar_parquet_r <- function(ruta, ruta_csv = "datos/base_comun_0904.csv") {
  if (!is.character(ruta) || length(ruta) != 1L || is.na(ruta) ||
      !file.exists(ruta) || dir.exists(ruta)) {
    stop("Indica un archivo Parquet existente, no una carpeta")
  }
  esperada <- crear_tabla_cartera(cargar_cartera(ruta_csv))
  # No imponer el esquema esperado al lector: primero observar el real.
  observada <- arrow::read_parquet(ruta, as_data_frame = FALSE)
  comparar_carteras(esperada, observada)
  resumir_cartera(observada)
}

crear_entrega_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  tabla <- crear_tabla_cartera(cargar_cartera(ruta_csv))
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino) || dir.exists(destino)) {
    stop("Indica una carpeta NUEVA; no se reutilizan destinos ocupados")
  }
  if (!arrow::codec_is_available("snappy")) stop("Esta instalacion no incluye Snappy")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  ruta <- file.path(destino, "base_comun.parquet")
  arrow::write_parquet(tabla, ruta, version = "2.6", compression = "snappy")
  resumen <- verificar_parquet_r(ruta, ruta_csv)
  utils::write.csv(resumen, file.path(destino, "resumen.csv"), row.names = FALSE,
    fileEncoding = "UTF-8")
  nota <- data.frame(R = as.character(getRversion()),
    arrow = as.character(utils::packageVersion("arrow")),
    registros = nrow(tabla), ids = length(unique(as.data.frame(tabla)$id_credito)),
    esquema = tabla$schema$ToString(), compresion = "snappy", version_parquet = "2.6")
  utils::write.csv(nota, file.path(destino, "sesion.csv"), row.names = FALSE,
    fileEncoding = "UTF-8")
  # Si falla una escritura queda la carpeta parcial para diagnosticar.
  # Las notas no sustituyen volver a decodificar y comparar el Parquet.
  resumen
}

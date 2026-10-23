# Funciones sin lecturas ni escrituras al hacer source().
funciones_particiones <- function() {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  sys.source("R/consultas_dataset_0906.R", envir = e)
  e
}

campo_particion_r <- function(por) {
  if (!is.character(por) || length(por) != 1L || is.na(por) ||
      !por %in% c("corte", "clave")) stop("por debe ser corte o clave")
  por
}

etiquetas_r <- function(tabla, por) {
  campo_particion_r(por)
  f <- funciones_particiones()
  x <- f$validar_tabla_cartera(tabla)
  if (!nrow(x)) return(character())
  fecha <- format(x$fecha_corte, "%Y-%m-%d")
  if (por == "clave") paste0(x$id_credito, "_", fecha) else fecha
}

archivos_particionados_r <- function(carpeta, por = "corte") {
  campo_particion_r(por)
  if (!is.character(carpeta) || length(carpeta) != 1L || is.na(carpeta) ||
      !dir.exists(carpeta)) stop("Indica la carpeta datos del dataset")
  entradas <- sort(list.files(carpeta, full.names = TRUE, all.files = TRUE, no.. = TRUE))
  archivos <- character()
  if (length(entradas) == 1L && basename(entradas) == "vacio.parquet" && !dir.exists(entradas)) {
    archivos <- entradas
  } else for (p in entradas) {
    patron <- if (por == "corte") "^corte=[0-9]{4}-[0-9]{2}-[0-9]{2}$" else
      "^clave=[0-9]{3}_[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    if (!dir.exists(p) || !grepl(patron, basename(p))) stop("Arbol Hive inesperado")
    valor <- substring(basename(p), nchar(por) + 2L)
    texto_fecha <- substring(valor, nchar(valor) - 9L)
    fecha <- as.Date(texto_fecha, format = "%Y-%m-%d")
    if (is.na(fecha) || format(fecha, "%Y-%m-%d") != texto_fecha ||
        fecha < as.Date("1900-01-01") || fecha > as.Date("2100-12-31")) stop("Fecha de carpeta invalida")
    partes <- sort(list.files(p, full.names = TRUE, all.files = TRUE, no.. = TRUE))
    if (!length(partes) || any(dir.exists(partes)) || any(!grepl("\\.parquet$", partes))) {
      stop("Cada particion debe contener solo Parquet")
    }
    archivos <- c(archivos, partes)
  }
  if (!length(archivos)) stop("Dataset sin archivos: falta un esquema comprobable")
  if (anyDuplicated(normalizePath(archivos, winslash = "/", mustWork = TRUE))) stop("Rutas repetidas")
  f <- funciones_particiones()
  for (ruta in archivos) {
    lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
    if (!lector$GetSchema()$Equals(f$esquema_cartera(), check_metadata = FALSE)) stop("Esquema fisico distinto")
    if (basename(ruta) == "vacio.parquet" && dirname(ruta) == carpeta && lector$num_rows != 0) {
      stop("El archivo vacio contiene registros")
    }
  }
  archivos
}

abrir_particionado_r <- function(carpeta, por = "corte") {
  archivos_particionados_r(carpeta, por)
  particion <- do.call(arrow::hive_partition, stats::setNames(list(arrow::utf8()), por))
  arrow::open_dataset(carpeta, format = "parquet", partitioning = particion, unify_schemas = TRUE)
}

inventario_particiones_r <- function(carpeta, por = "corte") {
  archivos <- archivos_particionados_r(carpeta, por)
  filas <- lapply(archivos, function(ruta) {
    lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
    data.frame(archivo = if (basename(ruta) == "vacio.parquet" && dirname(ruta) == carpeta)
      "vacio.parquet" else paste(basename(dirname(ruta)), basename(ruta), sep = "/"),
      registros = lector$num_rows, grupos = lector$num_row_groups,
      bytes_archivo = unname(file.info(ruta)$size))
  })
  do.call(rbind, filas)
}

auditar_particionado_r <- function(carpeta, ruta_csv = "datos/base_comun_0904.csv", por = "corte") {
  f <- funciones_particiones()
  for (ruta in archivos_particionados_r(carpeta, por)) {
    lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
    valores <- etiquetas_r(lector$ReadTable(), por)
    etiqueta <- substring(basename(dirname(ruta)), nchar(por) + 2L)
    if (length(valores) && any(valores != etiqueta)) stop("Etiqueta distinta de los valores fisicos")
  }
  observada <- arrow::as_arrow_table(abrir_particionado_r(carpeta, por))$SelectColumns(0:2)
  esperada <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  f$comparar_carteras(esperada, observada)
  f$resumir_cartera(observada)
}

escribir_particionado_r <- function(tabla, destino, por = "corte") {
  valores <- etiquetas_r(tabla, por)
  if (!arrow::codec_is_available("snappy")) stop("Snappy no disponible")
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino)) stop("Indica una carpeta NUEVA")
  datos <- file.path(destino, "datos")
  if (!dir.create(datos, recursive = TRUE)) stop("No se pudo crear el destino")
  f <- funciones_particiones()
  if (nrow(tabla)) {
    # La columna auxiliar se escribe en carpetas; las tres originales siguen en cada archivo.
    x <- f$validar_tabla_cartera(tabla)
    x[[por]] <- valores
    campos <- c(lapply(f$columnas_contrato, function(n) f$esquema_cartera()$GetFieldByName(n)),
      list(arrow::field(por, arrow::utf8(), nullable = FALSE)))
    ampliada <- arrow::Table$create(x, schema = do.call(arrow::schema, campos))
    arrow::write_dataset(ampliada, datos, format = "parquet", partitioning = por,
      hive_style = TRUE, basename_template = "parte-{i}.parquet",
      existing_data_behavior = "error", compression = "snappy", version = "2.6")
  } else arrow::write_parquet(tabla, file.path(datos, "vacio.parquet"),
    compression = "snappy", version = "2.6")
  observada <- arrow::as_arrow_table(abrir_particionado_r(datos, por))$SelectColumns(0:2)
  f$comparar_carteras(tabla, observada)
  inventario <- inventario_particiones_r(datos, por)
  utils::write.csv(inventario, file.path(destino, "inventario.csv"), row.names = FALSE,
    fileEncoding = "UTF-8")
  inventario
}

preparar_consulta_particion_r <- function(dataset, corte = as.Date("2026-10-31"), minimo = 2000L) {
  f <- funciones_particiones()
  f$parametros_consulta_r(corte, minimo)
  etiqueta <- format(corte, "%Y-%m-%d")
  fecha_objetivo <- corte
  dataset |>
    dplyr::filter(.data$corte == etiqueta, fecha_corte == fecha_objetivo, saldo_mxn >= minimo) |>
    dplyr::select(id_credito, saldo_mxn)
}

candidatos_por_etiqueta_r <- function(carpeta, corte = as.Date("2026-10-31")) {
  f <- funciones_particiones()
  f$parametros_consulta_r(corte, 0L)
  archivos <- archivos_particionados_r(carpeta)
  # Inventario por nombre: no es una traza del motor ni de lecturas fisicas.
  archivos[basename(dirname(archivos)) == paste0("corte=", format(corte, "%Y-%m-%d"))]
}

crear_comparacion_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  f <- funciones_particiones()
  tabla <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino)) stop("Indica una carpeta NUEVA")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  f$escribir_partes_r(tabla, file.path(destino, "plano"), filas_por_archivo = 14L)
  escribir_particionado_r(tabla, file.path(destino, "por_corte"))
  verificar_comparacion_r(destino, ruta_csv)
}

verificar_comparacion_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  f <- funciones_particiones()
  a <- f$verificar_dataset_r(file.path(destino, "plano/datos"), ruta_csv)
  b <- auditar_particionado_r(file.path(destino, "por_corte/datos"), ruta_csv)
  if (!identical(a, b)) stop("Resumenes distintos")
  b
}

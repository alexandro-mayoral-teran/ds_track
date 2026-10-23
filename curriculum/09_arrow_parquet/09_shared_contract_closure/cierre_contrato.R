# source() solo define funciones; no instala ni reconstruye entregas.
funciones_cierre <- function() {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  sys.source("R/consultas_cierre_0909.R", envir = e)
  e
}

contrato_cierre_r <- function() {
  data.frame(regla = c("columnas", "tipos_arrow", "nulabilidad", "clave", "id", "fechas", "saldo", "duplicados"),
    valor = c("id_credito|fecha_corte|saldo_mxn", "string|date32|int32", "false|false|false",
      "id_credito|fecha_corte", "tres digitos textuales", "1900-01-01 a 2100-12-31; calendario valido",
      "MXN; entero entre 0 y 2147483647", "rechazar; no deduplicar"), stringsAsFactors = FALSE)
}

notas_fijas_cierre <- function() {
  c(version_parquet = "2.6", compresion = "snappy", fecha_consulta = "2026-10-31", minimo_mxn = "2000")
}

escribir_csv_cierre <- function(x, ruta) {
  if (file.exists(ruta)) stop("Archivo ocupado: conservarlo")
  utils::write.csv(x, ruta, row.names = FALSE, fileEncoding = "UTF-8")
}

leer_csv_cierre <- function(ruta, columnas) {
  x <- utils::read.csv(ruta, colClasses = "character", check.names = FALSE,
    na.strings = NULL, stringsAsFactors = FALSE, row.names = NULL,
    fill = FALSE, fileEncoding = "UTF-8")
  if (!identical(names(x), columnas) || anyNA(x)) stop("Columnas/campos CSV distintos")
  x
}

comparar_csv_cierre <- function(ruta, esperada) {
  observada <- leer_csv_cierre(ruta, names(esperada))
  normalizar <- function(x) {
    x[] <- lapply(x, as.character)
    if (nrow(x)) x <- x[do.call(order, x), , drop = FALSE]
    rownames(x) <- NULL
    x
  }
  if (!identical(normalizar(observada), normalizar(esperada))) {
    stop("Valores CSV distintos en ", basename(ruta))
  }
  invisible(TRUE)
}

huellas_cierre_r <- function(destino) {
  # MD5 para cambios accidentales, no autenticidad. R base no exige paquetes nuevos.
  rutas <- sort(list.files(destino, recursive = TRUE, full.names = TRUE, all.files = TRUE))
  relativas <- substring(rutas, nchar(destino) + 2L)
  incluir <- relativas != "huellas.csv"
  rutas <- rutas[incluir]
  data.frame(archivo = gsub("\\\\", "/", relativas[incluir]),
    bytes = unname(file.info(rutas)$size), md5 = unname(tools::md5sum(rutas)), stringsAsFactors = FALSE)
}

verificar_entrega_cierre_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !dir.exists(destino)) stop("Indica una carpeta de entrega existente")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  f <- funciones_cierre()
  esperada <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  nombres <- c("entrada.csv", "tabla.parquet", "dataset", "resumen.csv", "seleccion.csv",
    "contrato.csv", "sesion.csv", "huellas.csv")
  if (!setequal(list.files(destino, all.files = TRUE, no.. = TRUE), nombres) ||
      !setequal(list.files(file.path(destino, "dataset"), all.files = TRUE, no.. = TRUE),
        c("datos", "inventario.csv"))) stop("Entrega incompleta o con entradas adicionales")
  comparar_csv_cierre(file.path(destino, "huellas.csv"), huellas_cierre_r(destino))
  # La fuente externa no se reemplaza por la copia de la propia entrega.
  bytes <- function(p) readBin(p, what = "raw", n = file.info(p)$size)
  if (!identical(bytes(file.path(destino, "entrada.csv")), bytes(ruta_csv))) stop("Copia de entrada distinta")
  comparar_csv_cierre(file.path(destino, "contrato.csv"), contrato_cierre_r())
  notas <- leer_csv_cierre(file.path(destino, "sesion.csv"), c("campo", "valor"))
  sesion <- stats::setNames(notas$valor, notas$campo)
  fijas <- notas_fijas_cierre()
  if (anyDuplicated(notas$campo) || !setequal(names(sesion), c(names(fijas),
      "escritor", "version_lenguaje", "version_arrow")) ||
      !sesion["escritor"] %in% c("Python", "R") || !nzchar(sesion["version_lenguaje"]) ||
      !nzchar(sesion["version_arrow"]) || any(sesion[names(fijas)] != fijas)) stop("Notas de sesion inconsistentes")
  lector <- arrow::ParquetFileReader$create(file.path(destino, "tabla.parquet"), mmap = FALSE)
  f$comparar_carteras(esperada, lector$ReadTable())
  datos <- file.path(destino, "dataset/datos")
  f$verificar_dataset_r(datos, ruta_csv)
  partes <- f$archivos_dataset_r(datos)
  cantidad <- max(1L, ceiling(nrow(esperada) / 14L))
  if (!identical(basename(partes), sprintf("parte_%03d.parquet", seq_len(cantidad)))) stop("Partes distintas del plan")
  inventario <- data.frame(archivo = basename(partes), registros = vapply(partes,
    function(p) as.numeric(arrow::ParquetFileReader$create(p, mmap = FALSE)$num_rows), numeric(1)))
  if (any(inventario$registros > 14)) stop("Una parte supera las 14 filas del plan")
  comparar_csv_cierre(file.path(destino, "dataset/inventario.csv"), inventario)
  comparar_csv_cierre(file.path(destino, "resumen.csv"), f$resumir_cartera(esperada))
  seleccion <- dplyr::collect(f$preparar_consulta_r(f$abrir_dataset_r(datos), as.Date("2026-10-31"), 2000L))
  control <- f$comprobar_consulta_r(seleccion, as.Date("2026-10-31"), 2000L, ruta_csv)
  comparar_csv_cierre(file.path(destino, "seleccion.csv"),
    f$referencia_consulta_r(as.Date("2026-10-31"), 2000L, ruta_csv))
  list(cartera = f$resumir_cartera(esperada), seleccion = control)
}

crear_entrega_cierre_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv") {
  f <- funciones_cierre()
  tabla <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  if (!arrow::codec_is_available("snappy")) stop("Snappy no disponible")
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino)) stop("Indica una carpeta NUEVA")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  destino <- normalizePath(destino, winslash = "/", mustWork = TRUE)
  if (!file.copy(ruta_csv, file.path(destino, "entrada.csv"))) stop("No se pudo copiar la fuente")
  arrow::write_parquet(tabla, file.path(destino, "tabla.parquet"), version = "2.6", compression = "snappy")
  f$escribir_partes_r(tabla, file.path(destino, "dataset"), filas_por_archivo = 14L)
  escribir_csv_cierre(f$resumir_cartera(tabla), file.path(destino, "resumen.csv"))
  seleccion <- dplyr::collect(f$preparar_consulta_r(f$abrir_dataset_r(file.path(destino, "dataset/datos")),
    as.Date("2026-10-31"), 2000L))
  f$comprobar_consulta_r(seleccion, as.Date("2026-10-31"), 2000L, ruta_csv)
  escribir_csv_cierre(as.data.frame(dplyr::arrange(seleccion, id_credito)), file.path(destino, "seleccion.csv"))
  escribir_csv_cierre(contrato_cierre_r(), file.path(destino, "contrato.csv"))
  sesion <- c(escritor = "R", version_lenguaje = as.character(getRversion()),
    version_arrow = as.character(utils::packageVersion("arrow")), notas_fijas_cierre())
  escribir_csv_cierre(data.frame(campo = names(sesion), valor = unname(sesion)), file.path(destino, "sesion.csv"))
  escribir_csv_cierre(huellas_cierre_r(destino), file.path(destino, "huellas.csv"))
  verificar_entrega_cierre_r(destino, ruta_csv)
}

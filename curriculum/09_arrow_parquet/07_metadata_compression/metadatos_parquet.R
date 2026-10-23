# source() solo define funciones. Reutiliza el contrato del proyecto preparado.
funciones_cartera_metadatos <- function() {
  e <- new.env(parent = globalenv())
  sys.source("R/contrato_0902.R", envir = e)
  sys.source("R/intercambio_parquet.R", envir = e)
  e
}

configuraciones_metadatos <- function() {
  data.frame(configuracion = c("base", "snappy", "diccionario", "grupos7"),
    codec = c("uncompressed", "snappy", "uncompressed", "uncompressed"),
    diccionario = c(FALSE, FALSE, TRUE, FALSE), filas_por_grupo = c(14L, 14L, 14L, 7L))
}

inspeccionar_metadatos_r <- function(ruta) {
  # Solo esquema y conteos: esta API R no expone estadisticas/codificaciones por chunk.
  if (!is.character(ruta) || length(ruta) != 1L || is.na(ruta) ||
      !file.exists(ruta) || dir.exists(ruta)) stop("Indica un archivo Parquet existente")
  lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
  list(archivo = basename(ruta), bytes_archivo = unname(file.info(ruta)$size),
    filas = lector$num_rows, columnas = lector$num_columns,
    grupos = lector$num_row_groups, esquema = lector$GetSchema()$ToString())
}

crear_experimento_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv",
    repeticiones = 3L) {
  if (!is.integer(repeticiones) || length(repeticiones) != 1L ||
      is.na(repeticiones) || repeticiones < 1L) stop("repeticiones debe ser entero positivo con L")
  if (!arrow::codec_is_available("snappy")) stop("Snappy no disponible; no sustituir el codec")
  f <- funciones_cartera_metadatos()
  tabla <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) ||
      !nzchar(destino) || file.exists(destino)) stop("Indica una carpeta NUEVA")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  configs <- configuraciones_metadatos()
  medidas <- list()
  reloj <- function() unname(proc.time()["elapsed"])
  for (repeticion in seq_len(repeticiones)) {
    desplazamiento <- (repeticion - 1L) %% nrow(configs)
    orden <- ((seq_len(nrow(configs)) - 1L + desplazamiento) %% nrow(configs)) + 1L
    for (posicion in seq_along(orden)) {
      config <- configs[orden[posicion], , drop = FALSE]
      nombre <- sprintf("%s_%02d.parquet", config$configuracion, repeticion)
      ruta <- file.path(destino, nombre)
      inicio <- reloj()
      arrow::write_parquet(tabla, ruta, version = "2.6", compression = config$codec,
        use_dictionary = config$diccionario, chunk_size = config$filas_por_grupo,
        write_statistics = TRUE)
      escritura <- reloj() - inicio
      inicio <- reloj()
      lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
      observada <- lector$ReadTable()
      lector <- NULL
      lectura <- reloj() - inicio
      f$comparar_carteras(tabla, observada) # Fuera del intervalo de lectura.
      detalle <- inspeccionar_metadatos_r(ruta)
      medidas[[length(medidas) + 1L]] <- data.frame(configuracion = config$configuracion,
        repeticion = repeticion, orden = posicion, archivo = nombre, codec = config$codec,
        diccionario = config$diccionario, filas_por_grupo = config$filas_por_grupo,
        filas = nrow(tabla), grupos = detalle$grupos, bytes_archivo = detalle$bytes_archivo,
        escritura_s = escritura, lectura_s = lectura)
    }
  }
  medidas <- do.call(rbind, medidas)
  utils::write.csv(medidas, file.path(destino, "mediciones.csv"), row.names = FALSE,
    fileEncoding = "UTF-8")
  utils::write.csv(f$resumir_cartera(tabla), file.path(destino, "resumen.csv"),
    row.names = FALSE, fileEncoding = "UTF-8")
  writeLines(c(paste("R:", getRversion()),
    paste("arrow:", utils::packageVersion("arrow")), paste("plataforma:", R.version$platform),
    paste("repeticiones:", repeticiones), "Parquet: 2.6; write_statistics=TRUE",
    "reloj: proc.time elapsed, segundos; resolucion limitada, puede dar cero",
    "lectura: ReadTable completo, mmap=FALSE; paralelismo predeterminado de R Arrow",
    "fuente/conversion/validacion/inspeccion fuera del intervalo; cache no controlada",
    "lectura inmediatamente despues de escribir; sin fsync ni garantia de persistencia fisica",
    "codec/diccionario son parametros solicitados: inspeccionar detalle real con PyArrow"),
    file.path(destino, "sesion.txt"), useBytes = TRUE)
  medidas
}

verificar_experimento_r <- function(destino, ruta_csv = "datos/base_comun_0904.csv",
    repeticiones = 3L) {
  if (!is.integer(repeticiones) || length(repeticiones) != 1L ||
      is.na(repeticiones) || repeticiones < 1L) stop("repeticiones debe ser entero positivo con L")
  configs <- configuraciones_metadatos()
  esperados <- as.vector(outer(configs$configuracion, seq_len(repeticiones),
    function(n, r) sprintf("%s_%02d.parquet", n, r)))
  entradas <- list.files(destino, all.files = TRUE, no.. = TRUE, full.names = TRUE)
  if (!dir.exists(destino) || any(dir.exists(entradas)) ||
      !setequal(basename(entradas), c(esperados, "mediciones.csv", "resumen.csv", "sesion.txt"))) {
    stop("Archivos ausentes o adicionales en el experimento")
  }
  f <- funciones_cartera_metadatos()
  tabla <- f$crear_tabla_cartera(f$cargar_cartera(ruta_csv))
  m <- utils::read.csv(file.path(destino, "mediciones.csv"), stringsAsFactors = FALSE)
  if (nrow(m) != length(esperados) || !setequal(m$archivo, esperados) || anyDuplicated(m$archivo)) {
    stop("Inventario de mediciones distinto")
  }
  for (i in seq_len(nrow(m))) {
    config <- configs[match(m$configuracion[i], configs$configuracion), , drop = FALSE]
    if (anyNA(config)) stop("Configuracion desconocida")
    ruta <- file.path(destino, m$archivo[i])
    lector <- arrow::ParquetFileReader$create(ruta, mmap = FALSE)
    f$comparar_carteras(tabla, lector$ReadTable())
    detalle <- inspeccionar_metadatos_r(ruta)
    # En la tabla vacia no exigimos una convencion de numero de grupos del escritor.
    grupos <- if (nrow(tabla)) ceiling(nrow(tabla) / config$filas_por_grupo) else detalle$grupos
    if (m$archivo[i] != sprintf("%s_%02d.parquet", m$configuracion[i], m$repeticion[i]) ||
        m$bytes_archivo[i] != detalle$bytes_archivo || m$filas[i] != nrow(tabla) ||
        m$grupos[i] != detalle$grupos || detalle$grupos != grupos ||
        m$codec[i] != config$codec || m$diccionario[i] != config$diccionario ||
        m$filas_por_grupo[i] != config$filas_por_grupo) stop("Metadatos/configuracion distintos")
    tiempos <- c(m$escritura_s[i], m$lectura_s[i])
    if (anyNA(tiempos) || any(!is.finite(tiempos) | tiempos < 0)) stop("Tiempo invalido")
  }
  # No autentica tiempos historicos ni codecs efectivos: vease inspector Python.
  f$resumir_cartera(tabla)
}

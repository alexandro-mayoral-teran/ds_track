# Funciones de solo lectura; R base. source() no ejecuta ni inicializa renv.
columnas_contrato <- c("id_credito", "fecha_corte", "saldo_mxn")

leer_textos_contrato <- function(ruta, columnas) {
  x <- utils::read.csv(ruta, colClasses = "character", check.names = FALSE,
    na.strings = NULL, strip.white = FALSE, blank.lines.skip = FALSE,
    fill = FALSE, fileEncoding = "UTF-8", stringsAsFactors = FALSE,
    comment.char = "", row.names = NULL)
  if (!identical(names(x), columnas) || anyNA(x)) {
    stop("Nombres, orden o cantidad de campos distintos")
  }
  x
}

evaluar_contrato <- function(x) {
  if (!is.data.frame(x) || !identical(names(x), columnas_contrato) ||
      !all(vapply(x, is.character, logical(1))) || anyNA(x)) {
    stop("Se requieren las tres columnas textuales en orden, sin NA nativo")
  }
  n <- nrow(x)
  fechas <- as.Date(rep(NA_character_, n))
  saldos <- rep(NA_integer_, n)
  motivos <- rep(list(character()), n)
  id_valido <- grepl("^[0-9]{3}$", x$id_credito)
  for (i in seq_len(n)) {
    m <- character()
    id <- x$id_credito[i]
    texto_fecha <- x$fecha_corte[i]
    texto_saldo <- x$saldo_mxn[i]
    if (id == "\\N") m <- c(m, "id_ausente") else if (!id_valido[i]) m <- c(m, "id_forma")
    if (texto_fecha == "\\N") {
      m <- c(m, "fecha_ausente")
    } else if (!grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", texto_fecha)) {
      m <- c(m, "fecha_forma")
    } else {
      # Python date no admite anio cero; conservar ese calendario compartido.
      fecha <- if (substr(texto_fecha, 1, 4) == "0000") as.Date(NA_character_) else
        as.Date(texto_fecha, format = "%Y-%m-%d")
      # Relectura exacta: no aceptar una fecha normalizada por el lector.
      if (is.na(fecha) || format(fecha, "%Y-%m-%d") != texto_fecha) {
        m <- c(m, "fecha_calendario")
      } else {
        fechas[i] <- fecha
        anio <- as.integer(substr(texto_fecha, 1, 4))
        if (anio < 1900L || anio > 2100L) m <- c(m, "fecha_rango")
      }
    }
    if (texto_saldo == "\\N") {
      m <- c(m, "saldo_ausente")
    } else if (!grepl("^-?[0-9]+$", texto_saldo)) {
      m <- c(m, "saldo_forma")
    } else {
      negativo <- startsWith(texto_saldo, "-")
      digitos <- sub("^0+", "", sub("^-", "", texto_saldo))
      if (digitos == "") digitos <- "0"
      # Con <= 10 digitos, double conserva estos enteros exactamente.
      if (nchar(digitos) > 10L || as.double(digitos) > .Machine$integer.max) {
        m <- c(m, "saldo_rango")
      } else {
        saldos[i] <- as.integer(as.double(digitos) * if (negativo) -1 else 1)
      }
      if (negativo && digitos != "0") m <- c(m, "saldo_negativo")
    }
    motivos[[i]] <- m
  }
  # Detectar TODAS las apariciones, incluso con saldo invalido.
  completa <- id_valido & !is.na(fechas)
  clave <- data.frame(id_credito = x$id_credito, fecha_corte = fechas)
  repetida <- completa & (duplicated(clave) | duplicated(clave, fromLast = TRUE))
  for (i in which(repetida)) motivos[[i]] <- c(motivos[[i]], "clave_repetida")
  diagnostico <- data.frame(numero_registro = seq_len(n), x,
    aceptado = lengths(motivos) == 0L,
    motivos = vapply(motivos, paste, collapse = "|", character(1)),
    check.names = FALSE, stringsAsFactors = FALSE)
  tipados <- data.frame(id_credito = x$id_credito, fecha_corte = fechas, saldo_mxn = saldos)
  # tipados es trabajo intermedio: usar aceptados para analisis del contrato.
  list(diagnostico = diagnostico, tipados = tipados,
       aceptados = tipados[diagnostico$aceptado, , drop = FALSE])
}

comprobar_contrato <- function(carpeta = "curriculum/09_arrow_parquet/02_schemas_types") {
  ruta <- file.path(dirname(carpeta), "01_csv_parquet_arrow", "datos", "base_comun.csv")
  base <- evaluar_contrato(leer_textos_contrato(ruta, columnas_contrato))
  stopifnot(nrow(base$aceptados) == 28L, all(base$diagnostico$aceptado),
    length(unique(base$aceptados$id_credito)) == 14L)
  cortes <- as.Date(c("2026-09-30", "2026-10-31"))
  cantidades <- vapply(seq_along(cortes), function(i) {
    sum(base$aceptados$fecha_corte == cortes[i])
  }, integer(1))
  saldos <- vapply(seq_along(cortes), function(i) {
    sum(as.double(base$aceptados$saldo_mxn[base$aceptados$fecha_corte == cortes[i]]))
  }, double(1))
  stopifnot(identical(cantidades, c(14L, 14L)), identical(saldos, c(29000, 31800)))
  casos <- leer_textos_contrato(file.path(carpeta, "casos_contrato.csv"),
    c("caso", columnas_contrato, "motivos_esperados"))
  evaluados <- evaluar_contrato(casos[columnas_contrato])
  stopifnot(identical(evaluados$diagnostico$motivos, casos$motivos_esperados))
  list(base = base, saldos_mxn = saldos, casos = casos, evaluados = evaluados)
}

# Preparación editorial 11.01 con R base. Cargar este archivo no crea salidas.
preparar_reporte <- function(origen, destino) {
  columnas <- c("credito_id", "fecha_corte", "saldo_mxn")
  fechas <- c("2026-09-30", "2026-10-31")
  ids <- c("001", "002", "003")
  datos <- read.csv(origen, colClasses = "character", check.names = FALSE,
                    na.strings = NULL, strip.white = FALSE)
  if (!identical(names(datos), columnas) || nrow(datos) != 6L || anyNA(datos)) {
    stop("Se requieren tres columnas y seis filas completas del contrato")
  }
  claves <- paste(datos$credito_id, datos$fecha_corte, sep = "|")
  esperadas <- as.vector(outer(ids, fechas, paste, sep = "|"))
  if (anyDuplicated(claves) || !setequal(claves, esperadas) ||
      any(!grepl("^(0|[1-9][0-9]{0,6})$", datos$saldo_mxn))) {
    stop("Clave inválida/repetida o saldo fuera del contrato")
  }
  saldo <- as.integer(datos$saldo_mxn)
  if (any(saldo > 1000000L)) stop("El saldo excede 1000000 MXN")
  # match conserva el orden de IDs al formar los pares por clave.
  septiembre <- saldo[match(paste(ids, fechas[1], sep = "|"), claves)]
  octubre <- saldo[match(paste(ids, fechas[2], sep = "|"), claves)]
  totales <- c(sum(septiembre), sum(octubre))
  diferencia <- totales[2] - totales[1]
  porcentaje <- if (totales[1] == 0) "no definido (base inicial cero)" else
    paste0(formatC(100 * diferencia / totales[1], format = "f", digits = 2,
                  decimal.mark = "."), "%")
  direccion <- if (diferencia > 0) "aumentó" else if (diferencia < 0) "disminuyó" else "no cambió"
  resumen <- data.frame(fecha_corte = fechas, creditos = 3L, saldo_mxn = totales)
  pares <- data.frame(credito_id = ids, septiembre_mxn = septiembre,
                      octubre_mxn = octubre, diferencia_mxn = octubre - septiembre)
  borrador <- c(
    "# Saldo observado de tres créditos ficticios", "",
    "Documento de preparación editorial generado con R; todavía no es un reporte Quarto.", "",
    "## Pregunta y público", "",
    "Para una persona que revisa la cartera: ¿cómo cambió el saldo observado de los",
    "mismos tres créditos entre 2026-09-30 y 2026-10-31?", "",
    "## Hallazgo", "",
    sprintf("El saldo total %s: pasó de %d a %d MXN.", direccion, totales[1], totales[2]),
    sprintf("La diferencia octubre menos septiembre es %d MXN; la variación sobre", diferencia),
    sprintf("septiembre es %s. La base común contiene %d créditos.", porcentaje, length(ids)), "",
    "## Evidencia y método", "",
    "| Corte | Créditos | Saldo (MXN) |", "| --- | --- | --- |",
    sprintf("| %s | 3 | %d |", fechas, totales), "",
    "Fuente: fuente.csv, copia de la entrada sintética de esta preparación.",
    "Una fila representa un crédito en un corte. Se comprobaron las seis claves",
    "esperadas, sin ausencias ni duplicados, y saldos enteros entre 0 y 1000000 MXN.",
    "Se sumó por fecha sobre los mismos IDs. pares.csv permite revisar cada cambio;",
    "resumen.csv conserva los totales. La tasa se presenta con dos decimales.", "",
    "## Límites y revisión", "",
    "Son saldos observados de una muestra ficticia, no desembolsos ni pagos del mes.",
    "No se conoce la causa del cambio ni se describe una cartera real completa.",
    "Revisar las tablas y la claridad del texto antes de preparar el documento Quarto."
  )
  if (file.exists(destino)) stop("El destino ya existe: elige una carpeta nueva")
  if (!dir.create(destino, recursive = TRUE)) stop("No se pudo crear el destino")
  if (!file.copy(origen, file.path(destino, "fuente.csv"), overwrite = FALSE)) {
    stop("No se pudo copiar la fuente")
  }
  write.csv(resumen, file.path(destino, "resumen.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  write.csv(pares, file.path(destino, "pares.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  writeLines(enc2utf8(borrador), file.path(destino, "borrador.md"), useBytes = TRUE)
  invisible(list(resumen = resumen, pares = pares, porcentaje = porcentaje))
}

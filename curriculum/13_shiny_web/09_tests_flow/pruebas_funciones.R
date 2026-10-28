# El ejecutor carga las funciones. Oraculos literales, no el resultado probado.
esperar_error <- function(expresion) {
  resultado <- tryCatch({ force(expresion); NULL }, error = function(e) e)
  stopifnot("Se esperaba un error" = inherits(resultado, "error"))
}
fuente <- leer_cartera("cartera.csv")
referencia <- data.frame(id_credito = rep(c("001", "002", "003"), 2),
  segmento = rep(c("comercio", "servicios", "comercio"), 2),
  fecha_corte = rep(c("2026-09-30", "2026-10-31"), each = 3),
  saldo_mxn = c(0, 2000, 2500, 100, 1900, 2600), stringsAsFactors = FALSE)
stopifnot("Fuente completa conocida" = identical(fuente, referencia))

# Cada fila del plan tiene IDs, valores y denominador esperados independientes.
casos <- list(
  list("2026-09-30", c("comercio", "servicios"), "2000", c("002", "003"), c(2000, 2500), 4500),
  list("2026-10-31", c("comercio", "servicios"), "2000", "003", 2600, 2600),
  list("2026-09-30", "comercio", "0", c("001", "003"), c(0, 2500), 2500),
  list("2026-09-30", "comercio", "1", "003", 2500, 2500),
  list("2026-10-31", "servicios", "1900", "002", 1900, 1900),
  list("2026-10-31", "servicios", "1901", character(), numeric(), 0),
  list("2026-09-30", character(), "0", character(), numeric(), 0))
for (caso in casos) {
  filtros <- revisar_filtros(caso[[1]], caso[[2]], caso[[3]])
  stopifnot(isTRUE(filtros$ok))
  consulta <- crear_consulta(fuente, filtros$filtros)
  stopifnot("IDs y frontera" = identical(consulta$seleccion$id_credito, caso[[4]]),
    "Saldos por credito" = identical(consulta$seleccion$saldo_mxn, caso[[5]]),
    "Suma esperada" = identical(consulta$indicadores$saldo_mxn, caso[[6]]),
    "Denominador completo" = identical(nrow(consulta$universo), 3L),
    "Porcentaje" = isTRUE(all.equal(consulta$indicadores$porcentaje_creditos, 100 * length(caso[[4]]) / 3)))
  # Comprobar por credito evita aceptar dos errores que se compensan en la suma.
  local({
    seleccion_csv <- tempfile(fileext = ".csv"); contexto_csv <- tempfile(fileext = ".csv")
    on.exit(unlink(c(seleccion_csv, contexto_csv)))
    escribir_seleccion(consulta, seleccion_csv); escribir_contexto(consulta, contexto_csv)
    releida <- leer_cartera(seleccion_csv)
    esperada <- referencia[referencia$fecha_corte == caso[[1]] & referencia$id_credito %in% caso[[4]], , drop = FALSE]
    rownames(esperada) <- NULL
    contexto <- read.csv(contexto_csv, colClasses = "character", check.names = FALSE)
    stopifnot("Columnas de contexto" = identical(names(contexto), c("corte", "segmentos", "minimo_mxn", "regla",
      "creditos_universo", "saldo_universo_mxn", "creditos_seleccion", "saldo_seleccion_mxn", "porcentaje_creditos")),
      "CSV por clave/campo" = identical(releida, esperada), nrow(contexto) == 1L,
      identical(contexto$corte, caso[[1]]),
      identical(contexto$segmentos, if (length(caso[[2]]) == 0L) "ninguno" else paste(sort(caso[[2]]), collapse = "|")),
      as.numeric(contexto$minimo_mxn) == as.numeric(caso[[3]]),
      contexto$regla == "saldo_mxn >= minimo_mxn", as.numeric(contexto$creditos_universo) == 3,
      as.numeric(contexto$saldo_universo_mxn) == if (caso[[1]] == "2026-09-30") 4500 else 4600,
      as.numeric(contexto$creditos_seleccion) == length(caso[[4]]),
      as.numeric(contexto$saldo_seleccion_mxn) == caso[[6]],
      isTRUE(all.equal(as.numeric(contexto$porcentaje_creditos), 100 * length(caso[[4]]) / 3)))
    if (length(caso[[4]]) > 0L) {
      capas <- ggplot2::ggplot_build(crear_grafica(consulta))$data
      stopifnot("Alturas" = identical(capas[[1]]$y, caso[[5]]),
        "Etiquetas" = identical(capas[[2]]$label, format(caso[[5]], scientific = FALSE, trim = TRUE)))
    } else esperar_error(crear_grafica(consulta))
  })
}
sin_universo <- crear_consulta(fuente, list(corte = "2026-11-30", segmentos = "comercio", minimo_mxn = 0))
stopifnot(nrow(sin_universo$universo) == 0L, is.na(sin_universo$indicadores$porcentaje_creditos))
esperar_error(crear_contexto(sin_universo))
for (texto in c("", "-1", "+1", " 0", "0 ", "01", "1.5", "1e3", "1000001")) {
  stopifnot("Rechazar texto sin corregirlo" = identical(revisar_filtros("2026-09-30", "comercio", texto)$ok, FALSE))
}
stopifnot(revisar_filtros("2026-09-30", NULL, "0")$ok,
  revisar_filtros("2026-09-30", "comercio", "1000000")$ok,
  !revisar_filtros("2026-02-30", "comercio", "0")$ok)
esperar_error(validar_cartera(rbind(fuente, fuente[6, , drop = FALSE])))
invalida <- fuente; invalida$saldo_mxn[6] <- NA_real_
esperar_error(seleccionar_corte(invalida, "2026-09-30")) # Incidencia fuera del corte.
esperar_error(resumir_seleccion(fuente[1:2, ], 1))
cat("OK funciones: fuente, siete consultas, catorce CSV, capas, fronteras y rechazos.\n")

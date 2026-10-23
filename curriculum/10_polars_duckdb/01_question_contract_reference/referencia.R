# R base; source() solo define funciones. No inicializa renv ni carga paquetes.
reglas_referencia <- function() {
  e <- new.env(parent = globalenv())
  sys.source("curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R", envir = e)
  e
}

fuente_referencia <- function() {
  "curriculum/10_polars_duckdb/01_question_contract_reference/muestra.csv"
}

cargar_filas_referencia <- function(ruta = fuente_referencia()) {
  reglas <- reglas_referencia()
  evaluadas <- reglas$evaluar_contrato(reglas$leer_textos_contrato(ruta, reglas$columnas_contrato))
  fallos <- evaluadas$diagnostico[!evaluadas$diagnostico$aceptado, , drop = FALSE]
  if (nrow(fallos)) stop("Fuente fuera del contrato (fila: motivos): ",
    paste(paste(fallos$numero_registro, fallos$motivos, sep = ": "), collapse = "; "))
  evaluadas$tipados
}

validar_parametros_referencia <- function(corte, minimo) {
  dias <- if (identical(class(corte), "Date")) as.numeric(corte) else NA_real_
  if (length(dias) != 1L || is.na(dias) || !is.finite(dias) || dias != floor(dias) ||
      corte < as.Date("1900-01-01") || corte > as.Date("2100-12-31")) stop("corte debe ser Date valido entre 1900 y 2100")
  if (!is.integer(minimo) || length(minimo) != 1L || is.na(minimo) || minimo < 0L) {
    stop("minimo debe ser entero no negativo con L dentro de int32")
  }
  invisible(TRUE)
}

construir_referencia_r <- function(ruta = fuente_referencia(), corte = as.Date("2026-10-31"), minimo = 2000L) {
  validar_parametros_referencia(corte, minimo)
  filas <- cargar_filas_referencia(ruta)
  # Indexacion R base: no se reutiliza un filtro Arrow, dplyr o SQL.
  seleccion <- filas[filas$fecha_corte == corte & filas$saldo_mxn >= minimo,
    c("id_credito", "saldo_mxn"), drop = FALSE]
  seleccion <- seleccion[order(seleccion$id_credito), , drop = FALSE]
  rownames(seleccion) <- NULL
  # Cota conservadora para suma exacta con double en R; muestras del capitulo muy inferiores.
  if (nrow(seleccion) > floor(2^53 / 2147483647)) stop("Referencia R fuera de la cota exacta documentada")
  list(seleccion = seleccion,
    control = list(corte = format(corte, "%Y-%m-%d"), minimo_mxn = minimo,
      registros = nrow(seleccion), saldo_mxn = sum(as.double(seleccion$saldo_mxn))),
    fuente = list(registros = nrow(filas), ids = length(unique(filas$id_credito))))
}

comprobar_seleccion_r <- function(observada, ruta = fuente_referencia(),
    corte = as.Date("2026-10-31"), minimo = 2000L) {
  if (!is.data.frame(observada) || !identical(names(observada), c("id_credito", "saldo_mxn")) ||
      !identical(class(observada$id_credito), "character") ||
      !identical(class(observada$saldo_mxn), "integer") || anyNA(observada)) {
    stop("Se exige tabla character/integer sin NA; inspecciona el esquema antes de adaptar")
  }
  referencia <- construir_referencia_r(ruta, corte, minimo)
  x <- as.data.frame(observada[order(observada$id_credito), , drop = FALSE])
  rownames(x) <- NULL
  if (!identical(x, referencia$seleccion)) stop("Pares ID/importe distintos aunque coincidan sumas")
  referencia$control
}

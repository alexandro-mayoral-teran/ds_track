# R base: source() solo define. Desde la raiz de DS Track en el IDE elegido.
referencia_cierre <- function(
    fuente = "curriculum/10_polars_duckdb/10_closure_tool_choice/muestra.csv",
    corte = as.Date("2026-10-31"), minimo = 2000L) {
  dias <- if (identical(class(corte), "Date")) as.numeric(corte) else NA_real_
  if (length(dias) != 1L || is.na(dias) || !is.finite(dias) || dias != floor(dias) ||
      corte < as.Date("1900-01-01") || corte > as.Date("2100-12-31")) stop("corte debe ser Date valido")
  if (!is.integer(minimo) || length(minimo) != 1L || is.na(minimo) || minimo < 0L) stop("minimo debe ser integer no negativo")
  e <- new.env(parent = globalenv())
  sys.source("curriculum/09_arrow_parquet/02_schemas_types/contrato_tabla.R", envir = e)
  x <- e$evaluar_contrato(e$leer_textos_contrato(fuente, e$columnas_contrato))
  if (any(!x$diagnostico$aceptado) || nrow(x$tipados) > 1998L) stop("Fuente fuera del contrato de cierre")
  filas <- x$tipados
  seleccion <- filas[filas$fecha_corte == corte & filas$saldo_mxn >= minimo,
    c("id_credito", "saldo_mxn"), drop = FALSE]
  seleccion <- seleccion[order(seleccion$id_credito), , drop = FALSE]
  rownames(seleccion) <- NULL
  cortes <- sort(unique(filas$fecha_corte))
  resumen <- data.frame(fecha_corte = cortes,
    registros = vapply(seq_along(cortes), function(i) sum(filas$fecha_corte == cortes[i]), integer(1)),
    saldo_mxn = vapply(seq_along(cortes), function(i) sum(as.double(filas$saldo_mxn[filas$fecha_corte == cortes[i]])), double(1)))
  # <=1998 saldos Int32: suma exacta por debajo de 2^53; no regla universal de R.
  list(seleccion = seleccion, resumen = resumen,
    control = c(registros = nrow(seleccion), saldo_mxn = sum(as.double(seleccion$saldo_mxn))))
}

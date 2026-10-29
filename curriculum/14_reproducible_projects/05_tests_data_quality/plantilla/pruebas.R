# Pruebas R base; cargar define, probar_proyecto ejecuta en biblioteca local.
probar_proyecto <- function(raiz = ".") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  e <- new.env(parent = globalenv())
  for (p in c("ejecutar.R", "codigo/modelo.R", "pipeline.R")) source(file.path(raiz, p), local = e, encoding = "UTF-8")
  e$verificar_entorno(raiz)
  if (!dir.exists(file.path(raiz, "ensayos"))) dir.create(file.path(raiz, "ensayos"))
  ensayo <- tempfile("pruebas-", tmpdir = file.path(raiz, "ensayos"))
  stopifnot(dir.create(ensayo)); nombre <- basename(ensayo)
  for (base in c("config", "datos/entrada")) stopifnot(dir.create(file.path(raiz, base, nombre)))
  cat("Fixtures conservadas:", ensayo, "\n")
  original <- e$leer_contrato(file.path(raiz, "datos/entrada/cartera.csv"))
  huella_original <- e$huella_1404(file.path(raiz, "datos/entrada/cartera.csv"))
  escribir <- function(ruta, tabla) {
    if (file.exists(ruta)) stop("Fixture ocupada.")
    write.csv(tabla, ruta, row.names = FALSE, fileEncoding = "UTF-8")
  }
  foto <- function(carpeta) {
    p <- sort(list.files(carpeta, full.names = TRUE, all.files = TRUE, no.. = TRUE))
    list(nombres = basename(p), bytes = lapply(p, function(x) readBin(x, "raw", n = file.info(x)$size)), mtime = unname(as.numeric(file.info(p)$mtime)))
  }
  esperar_error <- function(expr, patron = NULL) {
    error <- tryCatch({ force(expr); NULL }, error = function(e) e)
    if (!inherits(error, "error")) stop("Se esperaba un error y no ocurrio.")
    if (!is.null(patron) && !grepl(patron, conditionMessage(error))) stop("Error distinto del esperado: ", conditionMessage(error))
    invisible(TRUE)
  }
  configurar <- function(n, cambios = list(), filas = original) {
    entrada <- paste0("datos/entrada/", nombre, "/", n, ".csv")
    escribir(file.path(raiz, entrada), filas)
    cfg <- e$leer_contrato(file.path(raiz, "config/consulta.csv"))
    valores <- as.list(setNames(cfg$valor, cfg$clave))
    valores$entrada <- entrada; valores$salida <- paste0("salidas/", nombre, "_", n)
    for (k in names(cambios)) valores[[k]] <- cambios[[k]]
    archivo <- paste0("config/", nombre, "/", n, ".csv")
    escribir(file.path(raiz, archivo), data.frame(clave = names(valores), valor = unname(unlist(valores))))
    list(archivo = archivo, destino = file.path(raiz, valores$salida))
  }
  fallas <- character(); grupos <- 0L
  caso <- function(nombre, expr) {
    grupos <<- grupos + 1L
    tryCatch({ force(expr); cat("PASA:", nombre, "\n") }, error = function(e) {
      fallas <<- c(fallas, nombre); cat("FALLA:", nombre, "-", conditionMessage(e), "\n")
    })
  }
  caso("01 nueve criterios literales", {
    datos <- e$leer_fuente_modelo(file.path(raiz, "datos/entrada/cartera.csv"))
    casos <- e$leer_contrato(file.path(raiz, "referencia/criterios.csv")); stopifnot(nrow(casos) == 9L)
    for (i in seq_len(nrow(casos))) {
      c <- casos[i, ]; r <- e$resolver_contrato(datos, c$corte, c$segmentos, c$minimo_texto)
      for (k in names(r)) {
        if (k == "porcentaje_creditos" && nzchar(r[[k]])) stopifnot(abs(as.numeric(r[[k]]) - as.numeric(c[[k]])) < 1e-10)
        else if (!identical(r[[k]], c[[k]])) stop("Criterio distinto: ", c$caso, "/", k)
      }
    }
  })
  caso("02 catorce fuentes invalidas", {
    casos <- e$leer_contrato(file.path(raiz, "referencia/calidad.csv")); stopifnot(nrow(casos) == 14L)
    for (i in seq_len(nrow(casos))) {
      c <- casos[i, ]; filas <- original
      if (c$accion == "valor") filas[1, c$campo] <- c$valor
      else if (c$accion == "duplicar") filas <- rbind(filas, filas[1, , drop = FALSE])
      else if (c$accion == "quitar_columna") filas[[c$campo]] <- NULL
      else if (c$accion == "columna_extra") filas[[c$campo]] <- c$valor
      else stop("Accion desconocida en calidad.csv.")
      ruta <- file.path(ensayo, paste0(c$caso, ".csv")); escribir(ruta, filas)
      esperar_error(e$leer_fuente_modelo(ruta))
    }
  })
  caso("03 orden independiente y cero valido", {
    datos <- e$leer_fuente_modelo(file.path(raiz, "datos/entrada/cartera.csv"))
    r <- e$resolver_contrato(datos[nrow(datos):1, ], "2026-09-30", "comercio", "0")
    stopifnot(r[["ids"]] == "001|003", r[["saldos_mxn"]] == "0|2500")
  })
  caso("04 integracion y repeticion", {
    for (n in c("oct", "sep")) {
      corte <- if (n == "oct") "2026-10-31" else "2026-09-30"
      cfg <- configurar(n, list(corte = corte))
      stopifnot(e$pipeline_proyecto(raiz, cfg$archivo) == "creada")
      filas <- e$leer_contrato(file.path(cfg$destino, "seleccion.csv"))
      ctx <- e$leer_contrato(file.path(cfg$destino, "contexto.csv"))
      stopifnot(paste(filas$id_credito, collapse = "|") == if (n == "oct") "003" else "002|003",
        ctx$saldo_seleccion_mxn == if (n == "oct") "2600" else "4500",
        sum(as.numeric(filas$saldo_mxn)) == as.numeric(ctx$saldo_seleccion_mxn))
      stopifnot(identical(filas$saldo_mxn, if (n == "oct") "2600" else c("2000", "2500")),
        ctx$creditos_universo == "3", ctx$saldo_universo_mxn == if (n == "oct") "4600" else "4500",
        ctx$creditos_seleccion == if (n == "oct") "1" else "2",
        abs(as.numeric(ctx$porcentaje_creditos) - if (n == "oct") 100/3 else 200/3) < 1e-10)
      antes <- foto(cfg$destino)
      stopifnot(e$pipeline_proyecto(raiz, cfg$archivo) == "reutilizada", identical(foto(cfg$destino), antes))
    }
  })
  caso("05 vacio y sin universo", {
    cfg <- configurar("vacio", list(segmentos = "servicios", minimo_texto = "1901"))
    e$pipeline_proyecto(raiz, cfg$archivo)
    filas <- e$leer_contrato(file.path(cfg$destino, "seleccion.csv"))
    ctx <- e$leer_contrato(file.path(cfg$destino, "contexto.csv"))
    stopifnot(identical(names(filas), names(original)), nrow(filas) == 0L,
      ctx$estado == "vacio", ctx$creditos_universo == "3", ctx$porcentaje_creditos == "0")
    cfg <- configurar("sinuniverso", list(corte = "2026-11-30"))
    esperar_error(e$pipeline_proyecto(raiz, cfg$archivo), "sin universo")
    stopifnot(!file.exists(cfg$destino))
  })
  caso("06 duplicado fuera del corte bloquea", {
    cfg <- configurar("duplicado", filas = rbind(original, original[1, , drop = FALSE]))
    esperar_error(e$pipeline_proyecto(raiz, cfg$archivo), "anyDuplicated")
    stopifnot(!file.exists(cfg$destino))
  })
  caso("07 compensacion no engana", {
    cfg <- configurar("alterado", list(corte = "2026-09-30"))
    e$pipeline_proyecto(raiz, cfg$archivo)
    ruta <- file.path(cfg$destino, "seleccion.csv"); filas <- e$leer_contrato(ruta)
    filas$saldo_mxn <- c("1999", "2501")
    # Solo los resultados de este ensayo se modifican deliberadamente.
    write.csv(filas, ruta, row.names = FALSE)
    rutas <- c("seleccion.csv", "contexto.csv", "insumos.csv")
    marca <- data.frame(archivo = rutas, md5 = vapply(file.path(cfg$destino, rutas), e$huella_1404, character(1)))
    write.csv(marca, file.path(cfg$destino, "COMPLETO.csv"), row.names = FALSE)
    antes <- foto(cfg$destino)
    esperar_error(e$pipeline_proyecto(raiz, cfg$archivo), "calculo actual")
    stopifnot(identical(foto(cfg$destino), antes))
  })
  stopifnot(identical(e$huella_1404(file.path(raiz, "datos/entrada/cartera.csv")), huella_original))
  cat(grupos, "grupos;", length(fallas), "fallas.\n")
  if (length(fallas)) stop("Pruebas fallidas: ", paste(fallas, collapse = ", "))
  invisible(TRUE)
}

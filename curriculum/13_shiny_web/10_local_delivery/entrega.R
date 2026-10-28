# source() solo define funciones. Crear ejecuta codigo revisado; verificar solo lee.
plan_cierre <- function() {
  data.frame(caso = c("septiembre", "octubre", "cero", "frontera", "vacio", "sin_universo"),
    corte = c("2026-09-30", "2026-10-31", "2026-09-30", "2026-09-30", "2026-09-30", "2026-11-30"),
    segmentos = c("comercio|servicios", "comercio|servicios", "comercio", "comercio", "ninguno", "comercio|servicios"),
    minimo_mxn = c("2000", "2000", "0", "1", "0", "2000"), stringsAsFactors = FALSE)
}

archivos_cierre <- function() c("app.R", "consulta_module.R", "cartera.R", "consulta.R",
  "validacion.R", "presentacion.R", "cartera.csv", "DESCRIPTION", "renv.lock",
  "shiny_1310.Rproj", "restaurar.R", "iniciar.R", ".Rprofile", "renv/activate.R", "renv/settings.json",
  "minimo.R", "pruebas_minimo.R", "pruebas_funciones.R", "pruebas_servidor.R", "ejecutar_pruebas.R",
  "entrega.R", "LEEME.md", "CONTRATO.md", "casos.csv")

leer_textos_cierre <- function(ruta) {
  utils::read.csv(ruta, colClasses = "character", check.names = FALSE, row.names = NULL,
    na.strings = NULL, fileEncoding = "UTF-8", fill = FALSE, blank.lines.skip = FALSE)
}

# Referencia R base independiente: no carga funciones ni ejecuta codigo de la entrega.
referencia_cierre <- function(ruta) {
  x <- leer_textos_cierre(ruta)
  if (!identical(names(x), c("id_credito", "segmento", "fecha_corte", "saldo_mxn")) ||
      nrow(x) > 10000L || anyNA(x)) stop("Referencia: estructura o ausencias invalidas.")
  if (any(!grepl("^[0-9]{3}$", x$id_credito)) || any(!x$segmento %in% c("comercio", "servicios")) ||
      any(!grepl("^(0|[1-9][0-9]*)$", x$saldo_mxn))) stop("Referencia: ID, segmento o saldo invalido.")
  saldos <- as.numeric(x$saldo_mxn)
  if (any(!is.finite(saldos) | saldos > 1000000)) stop("Referencia: saldo fuera del contrato.")
  for (fecha in unique(x$fecha_corte)) {
    valor <- tryCatch(as.Date(fecha, "%Y-%m-%d"), error = function(e) as.Date(NA))
    if (!grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha) || is.na(valor) ||
        format(valor, "%Y-%m-%d") != fecha || fecha < "1900-01-01" || fecha > "2100-12-31") stop("Referencia: fecha invalida.")
  }
  if (anyDuplicated(x[c("id_credito", "fecha_corte")])) stop("Referencia: clave repetida.")
  x$saldo_mxn <- saldos
  x <- x[order(x$fecha_corte, x$id_credito), , drop = FALSE]; rownames(x) <- NULL
  x
}

resultados_referencia <- function(datos) {
  plan <- plan_cierre(); seleccion <- contexto <- vector("list", nrow(plan)); resumen <- list()
  for (i in seq_len(nrow(plan))) {
    p <- plan[i, ]; u <- datos[datos$fecha_corte == p$corte, , drop = FALSE]
    segmentos <- if (p$segmentos == "ninguno") character() else strsplit(p$segmentos, "|", fixed = TRUE)[[1]]
    s <- u[u$segmento %in% segmentos & u$saldo_mxn >= as.numeric(p$minimo_mxn), , drop = FALSE]
    rownames(s) <- NULL; seleccion[[i]] <- s
    hay <- nrow(u) > 0L; cantidad <- nrow(s); saldo <- sum(s$saldo_mxn)
    porcentaje <- if (hay) 100 * cantidad / nrow(u) else NA_real_
    resumen[[i]] <- data.frame(caso = p$caso, tipo = if (!hay) "sin_universo" else if (cantidad == 0L) "vacio" else "ok",
      creditos_universo = nrow(u), creditos_seleccion = if (hay) cantidad else NA_integer_,
      saldo_seleccion_mxn = if (hay) saldo else NA_real_, porcentaje_creditos = porcentaje)
    contexto[[i]] <- data.frame(corte = p$corte, segmentos = p$segmentos, minimo_mxn = as.numeric(p$minimo_mxn),
      regla = "saldo_mxn >= minimo_mxn", creditos_universo = nrow(u), saldo_universo_mxn = sum(u$saldo_mxn),
      creditos_seleccion = cantidad, saldo_seleccion_mxn = saldo, porcentaje_creditos = porcentaje)
  }
  list(seleccion = seleccion, contexto = contexto, resumen = do.call(rbind, resumen))
}

comparar_tabla_cierre <- function(ruta, esperada, numericas = character()) {
  x <- leer_textos_cierre(ruta)
  if (!identical(names(x), names(esperada)) || nrow(x) != nrow(esperada) || anyNA(x)) stop("Tabla incompatible: ", basename(ruta))
  for (columna in names(x)) {
    if (columna %in% numericas) {
      vacias <- is.na(esperada[[columna]])
      texto <- x[[columna]]
      if (!identical(texto == "", vacias)) stop("Ausencias distintas: ", columna)
      valores <- suppressWarnings(as.numeric(texto[!vacias]))
      if (any(!is.finite(valores)) || !isTRUE(all.equal(valores, as.numeric(esperada[[columna]][!vacias]),
          tolerance = if (columna == "porcentaje_creditos") 1e-12 else 0))) stop("Valores distintos: ", columna)
    } else if (!identical(x[[columna]], as.character(esperada[[columna]]))) stop("Textos distintos: ", columna)
  }
  invisible(TRUE)
}

archivos_resultados <- function(resumen) {
  salida <- c("resumen.csv", "INFORME.md")
  for (i in seq_len(nrow(resumen))) {
    if (resumen$tipo[i] == "sin_universo") next
    prefijo <- paste0("resultados/", resumen$caso[i])
    salida <- c(salida, paste0(prefijo, c("_seleccion.csv", "_contexto.csv")))
    if (resumen$tipo[i] == "ok") salida <- c(salida, paste0(prefijo, ".png"))
  }
  salida
}

verificar_entrega <- function(entrega, referencia) {
  raiz <- normalizePath(entrega, winslash = "/", mustWork = TRUE)
  externa <- normalizePath(referencia, winslash = "/", mustWork = TRUE)
  if (startsWith(tolower(externa), paste0(tolower(raiz), "/"))) stop("Elige referencia externa a la entrega.")
  datos <- referencia_cierre(externa)
  if (!identical(referencia_cierre(file.path(raiz, "cartera.csv")), datos)) stop("Fuente distinta por clave/campo.")
  comparar_tabla_cierre(file.path(raiz, "casos.csv"), plan_cierre())
  r <- resultados_referencia(datos)
  comparar_tabla_cierre(file.path(raiz, "resumen.csv"), r$resumen,
    c("creditos_universo", "creditos_seleccion", "saldo_seleccion_mxn", "porcentaje_creditos"))
  for (i in seq_len(nrow(r$resumen))) {
    if (r$resumen$tipo[i] == "sin_universo") next
    prefijo <- file.path(raiz, "resultados", plan_cierre()$caso[i])
    comparar_tabla_cierre(paste0(prefijo, "_seleccion.csv"), r$seleccion[[i]], "saldo_mxn")
    comparar_tabla_cierre(paste0(prefijo, "_contexto.csv"), r$contexto[[i]],
      c("minimo_mxn", "creditos_universo", "saldo_universo_mxn", "creditos_seleccion", "saldo_seleccion_mxn", "porcentaje_creditos"))
    if (r$resumen$tipo[i] == "ok") {
      con <- file(paste0(prefijo, ".png"), "rb"); cabecera <- tryCatch(readBin(con, "raw", 24), finally = close(con))
      if (length(cabecera) != 24L || !identical(as.integer(cabecera[1:8]), c(137L,80L,78L,71L,13L,10L,26L,10L)) ||
          !identical(as.integer(cabecera[17:24]), c(0L,0L,3L,192L,0L,0L,2L,88L))) stop("PNG: firma o dimensiones distintas.")
    }
  }
  esperados <- sort(c(archivos_cierre(), archivos_resultados(r$resumen)))
  huellas <- leer_textos_cierre(file.path(raiz, "huellas.csv"))
  if (!identical(names(huellas), c("archivo", "md5")) || anyNA(huellas) ||
      !identical(huellas$archivo, esperados) || any(!grepl("^[a-f0-9]{32}$", huellas$md5))) stop("Inventario de huellas incompatible.")
  rutas <- file.path(raiz, esperados)
  if (any(!file.exists(rutas)) || any(dir.exists(rutas)) ||
      !identical(unname(as.character(tools::md5sum(rutas))), huellas$md5)) stop("Archivos ausentes o huellas distintas.")
  # El inventario de resultados es cerrado; no admite exportaciones de sin universo.
  if (!identical(sort(list.files(file.path(raiz, "resultados"))),
      sort(sub("^resultados/", "", esperados[startsWith(esperados, "resultados/")])))) stop("Resultados no previstos.")
  cat("OK entrega: referencia externa, seis casos, tablas, PNG e inventario. No ejecuta la app.\n")
  invisible(r$resumen)
}

crear_entrega <- function(destino, origen = ".") {
  if (!is.character(destino) || length(destino) != 1L || is.na(destino) || !nzchar(destino)) stop("Indica un destino nuevo.")
  if (file.exists(destino) || dir.exists(destino)) stop("El destino existe; conservarlo y elegir otro.")
  fuente <- normalizePath(origen, winslash = "/", mustWork = TRUE)
  padre <- normalizePath(dirname(destino), winslash = "/", mustWork = TRUE)
  nueva <- paste0(padre, "/", basename(destino))
  if (tolower(nueva) == tolower(fuente) || startsWith(tolower(nueva), paste0(tolower(fuente), "/"))) stop("Destino fuera de la carpeta fuente.")
  archivos <- archivos_cierre()
  if (!all(file.exists(file.path(fuente, archivos)))) stop("Faltan fuentes de la practica.")
  anterior <- getwd(); on.exit(setwd(anterior)); setwd(fuente)
  entorno <- new.env(parent = globalenv())
  for (a in c("cartera.R", "consulta.R", "validacion.R", "presentacion.R")) source(a, local = entorno, encoding = "UTF-8")
  datos <- entorno$leer_cartera("cartera.csv")
  comparar_tabla_cierre("casos.csv", plan_cierre())
  if (!dir.create(nueva)) stop("No se pudo crear destino.")
  dir.create(file.path(nueva, "renv")); dir.create(file.path(nueva, "resultados"))
  for (a in archivos) if (!file.copy(a, file.path(nueva, a), overwrite = FALSE)) stop("Copia parcial: conservar y revisar.")
  plan <- plan_cierre(); filas <- list()
  for (i in seq_len(nrow(plan))) {
    p <- plan[i, ]; segmentos <- if (p$segmentos == "ninguno") character() else strsplit(p$segmentos, "|", fixed = TRUE)[[1]]
    q <- entorno$crear_consulta(datos, list(corte = p$corte, segmentos = segmentos, minimo_mxn = as.numeric(p$minimo_mxn)))
    hay <- nrow(q$universo) > 0L; m <- q$indicadores
    tipo <- if (!hay) "sin_universo" else if (m$cantidad == 0L) "vacio" else "ok"
    filas[[i]] <- data.frame(caso = p$caso, tipo = tipo, creditos_universo = nrow(q$universo),
      creditos_seleccion = if (hay) m$cantidad else NA_integer_, saldo_seleccion_mxn = if (hay) m$saldo_mxn else NA_real_,
      porcentaje_creditos = if (hay) m$porcentaje_creditos else NA_real_)
    if (!hay) next
    prefijo <- file.path(nueva, "resultados", p$caso)
    entorno$escribir_seleccion(q, paste0(prefijo, "_seleccion.csv"))
    entorno$escribir_contexto(q, paste0(prefijo, "_contexto.csv"))
    if (tipo == "ok") ggplot2::ggsave(paste0(prefijo, ".png"), plot = entorno$crear_grafica(q), width = 8, height = 5, units = "in", dpi = 120)
  }
  resumen <- do.call(rbind, filas)
  utils::write.csv(resumen, file.path(nueva, "resumen.csv"), row.names = FALSE, na = "")
  writeLines(c("# Evidencia generada de cierre", "", "Seis casos recalculados con las funciones incluidas; ver resumen.csv.",
    "PNG 960 x 600; vacio sin figura; sin universo sin exportaciones.",
    "R de esta generacion:", R.version.string, "", "Pendiente: demostracion humana, navegador y reconstruccion en otra carpeta.",
    "Este archivo no autentica ejecuciones pasadas ni certifica aprendizaje."), file.path(nueva, "INFORME.md"), useBytes = TRUE)
  rutas <- sort(c(archivos, archivos_resultados(resumen)))
  utils::write.csv(data.frame(archivo = rutas, md5 = unname(as.character(tools::md5sum(file.path(nueva, rutas))))),
    file.path(nueva, "huellas.csv"), row.names = FALSE)
  verificar_entrega(nueva, file.path(fuente, "cartera.csv"))
  cat("Entrega nueva creada en ", nueva, ". No incluye paquetes instalados.\n", sep = "")
  invisible(nueva)
}

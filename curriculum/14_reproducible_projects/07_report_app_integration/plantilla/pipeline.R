# Cargar define funciones; ejecutar exige la biblioteca local restaurada.
huella_1404 <- function(ruta) unname(as.character(tools::md5sum(ruta)))
escribir_1404 <- function(ruta, tabla) {
  if (file.exists(ruta)) stop("Archivo ocupado.")
  con <- file(ruta, open = "wb"); on.exit(close(con))
  write.table(tabla, con, sep = ",", row.names = FALSE, col.names = TRUE,
    quote = TRUE, eol = "\n", na = "")
}
comprobar_1404 <- function(carpeta, tablas, lector) {
  if (!dir.exists(carpeta) || !setequal(list.files(carpeta, all.files = TRUE, no.. = TRUE), c(names(tablas), "COMPLETO.csv"))) stop("Entrega incompleta o con archivos extra.")
  for (nombre in c(names(tablas), "COMPLETO.csv")) {
    ruta <- file.path(carpeta, nombre); enlace <- Sys.readlink(ruta)
    if (dir.exists(ruta) || (!is.na(enlace) && nzchar(enlace))) stop("Archivo no regular.")
  }
  for (nombre in names(tablas)) {
    actual <- lector(file.path(carpeta, nombre)); esperado <- tablas[[nombre]]
    rownames(actual) <- rownames(esperado) <- NULL
    if (!identical(actual, esperado)) stop(paste("Entrega distinta del calculo actual:", nombre))
  }
  marca <- lector(file.path(carpeta, "COMPLETO.csv"))
  esperado <- data.frame(archivo = names(tablas), md5 = vapply(file.path(carpeta, names(tablas)), huella_1404, character(1)), stringsAsFactors = FALSE, row.names = NULL)
  if (!identical(marca, esperado)) stop("Marca o huellas incorrectas.")
  invisible(TRUE)
}
tablas_esperadas <- function(raiz, archivo = "config/consulta.csv") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  e <- new.env(parent = globalenv())
  for (p in c("ejecutar.R", "codigo/modelo.R", "codigo/configuracion.R")) source(file.path(raiz, p), local = e, encoding = "UTF-8")
  cfg <- e$leer_configuracion(raiz, archivo, permitir_existente = TRUE)
  destino <- cfg$salida_resuelta
  if (file.exists(destino) && normalizePath(destino, winslash = "/", mustWork = TRUE) != destino) stop("Destino enlazado.")
  datos <- e$leer_fuente_modelo(cfg$entrada_resuelta)
  resultado <- e$resolver_contrato(datos, cfg$corte, cfg$segmentos, cfg$minimo_texto)
  if (!resultado[["estado"]] %in% c("ok", "vacio")) stop("Consulta sin universo o invalida: no se publica entrega.")
  ids <- if (nzchar(resultado[["ids"]])) strsplit(resultado[["ids"]], "|", fixed = TRUE)[[1]] else character()
  seleccion <- datos[datos$fecha_corte == cfg$corte & datos$id_credito %in% ids, , drop = FALSE]
  seleccion <- seleccion[order(seleccion$id_credito), , drop = FALSE]
  seleccion$saldo_mxn <- if (nrow(seleccion)) format(seleccion$saldo_mxn, scientific = FALSE, trim = TRUE) else character()
  rownames(seleccion) <- NULL
  contexto <- c(unlist(cfg[c("version_reglas", "corte", "segmentos", "minimo_texto", "app")]), resultado[!names(resultado) %in% c("ids", "saldos_mxn")])
  contexto[["porcentaje_creditos"]] <- format(100 * as.numeric(resultado[["creditos_seleccion"]]) / as.numeric(resultado[["creditos_universo"]]), digits = 15, scientific = FALSE, trim = TRUE)
  insumos <- c(esquema = "1404-v1", motor = "r", version_reglas = cfg$version_reglas)
  rutas <- c(entrada = cfg$entrada_resuelta, config = file.path(raiz, archivo), modelo = file.path(raiz, "codigo/modelo.R"), pipeline = file.path(raiz, "pipeline.R"), configuracion = file.path(raiz, "codigo/configuracion.R"))
  insumos <- c(insumos, setNames(vapply(rutas, huella_1404, character(1)), paste0("md5.", names(rutas))))
  tablas <- list(seleccion.csv = seleccion,
    contexto.csv = as.data.frame(as.list(contexto), stringsAsFactors = FALSE),
    insumos.csv = data.frame(clave = names(insumos), valor = unname(insumos), stringsAsFactors = FALSE))
  list(cfg = cfg, tablas = tablas, lector = e$leer_contrato)
}
pipeline_proyecto <- function(raiz, archivo = "config/consulta.csv", simular_fallo = FALSE) {
  e <- new.env(parent = globalenv())
  source(file.path(raiz, "ejecutar.R"), local = e, encoding = "UTF-8")
  e$verificar_entorno(raiz)
  preparado <- tablas_esperadas(raiz, archivo)
  cfg <- preparado$cfg; tablas <- preparado$tablas; destino <- cfg$salida_resuelta
  if (file.exists(destino)) {
    comprobar_1404(destino, tablas, preparado$lector)
    cat("Reutilizada y comprobada:", destino, "\n"); return(invisible("reutilizada"))
  }
  temporal <- tempfile(pattern = ".pendiente-", tmpdir = dirname(destino))
  if (!dir.create(temporal)) stop("No se pudo crear temporal.")
  cat("Preparando:", temporal, "\n")
  escribir_1404(file.path(temporal, "seleccion.csv"), tablas$seleccion.csv)
  if (simular_fallo) stop("Fallo didactico: temporal conservado, sin entrega final.")
  for (nombre in c("contexto.csv", "insumos.csv")) escribir_1404(file.path(temporal, nombre), tablas[[nombre]])
  marca <- data.frame(archivo = names(tablas), md5 = vapply(file.path(temporal, names(tablas)), huella_1404, character(1)), stringsAsFactors = FALSE, row.names = NULL)
  escribir_1404(file.path(temporal, "COMPLETO.csv"), marca)
  comprobar_1404(temporal, tablas, preparado$lector)
  if (file.exists(destino) || !file.rename(temporal, destino)) stop("No se publico; temporal conservado. Revisa destino.")
  cat("Creada y comprobada:", destino, "\n")
  invisible("creada")
}

# Lector de solo lectura; source define funciones y no produce salidas.
cargar_integracion <- function(raiz, archivo = "config/octubre.csv", app = "shiny") {
  e <- new.env(parent = globalenv())
  source(file.path(raiz, "pipeline.R"), local = e, encoding = "UTF-8")
  preparado <- e$tablas_esperadas(raiz, archivo)
  cfg <- preparado$cfg
  if (!app %in% c("streamlit", "shiny") || cfg$app != app) stop("La app no coincide con la configuracion.")
  e$comprobar_1404(cfg$salida_resuelta, preparado$tablas, preparado$lector)
  list(config = archivo, entrega = cfg$salida,
    revision = e$huella_1404(file.path(cfg$salida_resuelta, "COMPLETO.csv")),
    comprobado_utc = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ", tz = "UTC"),
    contexto = as.list(preparado$tablas$contexto.csv[1, , drop = FALSE]),
    seleccion = preparado$tablas$seleccion.csv)
}

escapar_1407 <- function(x) {
  x <- gsub("&", "&amp;", as.character(x), fixed = TRUE)
  x <- gsub("<", "&lt;", x, fixed = TRUE)
  x <- gsub(">", "&gt;", x, fixed = TRUE)
  x <- gsub('"', "&quot;", x, fixed = TRUE)
  gsub("'", "&#x27;", x, fixed = TRUE)
}

vista_integracion <- function(p) {
  c <- p$contexto
  valores <- c(c$corte, c$segmentos, c$minimo_texto, c$version_reglas, c$app,
    p$config, p$entrega, p$revision, p$comprobado_utc)
  etiquetas <- c("Corte", "Segmentos", "Mínimo MXN", "Reglas", "App", "Configuración", "Entrega", "Revisión MD5", "Comprobado UTC")
  encabezado <- paste0('<p><strong>', escapar_1407(etiquetas), ':</strong> ', escapar_1407(valores), '</p>', collapse = "")
  claves <- c("estado", "creditos_universo", "saldo_universo_mxn", "creditos_seleccion", "saldo_seleccion_mxn", "porcentaje_creditos")
  etiquetas <- c("Estado", "Créditos del universo", "Saldo del universo MXN", "Créditos seleccionados", "Saldo seleccionado MXN", "Cobertura de créditos %")
  valores <- escapar_1407(unlist(c[claves]))
  medidas <- paste0('<p data-medida="', claves, '" data-valor="', valores, '">', etiquetas, ': ', valores, '</p>', collapse = "")
  filas <- p$seleccion
  tabla <- '<div style="overflow-x:auto"><table><caption>Selección comprobada, saldos en MXN</caption><thead><tr><th scope="col">ID</th><th scope="col">Segmento</th><th scope="col">Corte</th><th scope="col">Saldo MXN</th></tr></thead><tbody>'
  for (i in seq_len(nrow(filas))) tabla <- paste0(tabla, '<tr>', paste0('<td>', escapar_1407(unlist(filas[i, ])), '</td>', collapse = ""), '</tr>')
  tabla <- paste0(tabla, '</tbody></table></div>')
  if (!nrow(filas)) {
    figura <- '<p>Selección vacía sobre universo válido: no hay barras.</p>'
  } else {
    maximo <- max(1, as.numeric(filas$saldo_mxn)); barras <- character()
    for (i in seq_len(nrow(filas))) {
      ancho <- floor(100 * as.numeric(filas$saldo_mxn[i]) / maximo)
      barras <- c(barras, paste0('<p>', filas$id_credito[i], ': ', filas$saldo_mxn[i], ' MXN</p><div data-id="', filas$id_credito[i], '" data-saldo="', filas$saldo_mxn[i], '" style="width:', ancho, '%;height:24px;background:#225ea8"></div>'))
    }
    figura <- paste0('<div role="img" aria-label="Saldo seleccionado por crédito en MXN; valores en la tabla" style="width:100%;max-width:600px">', paste0(barras, collapse = ""), '</div>')
  }
  paste0('<!-- inicio-vista-1407 -->\n<section><h2>Consulta aplicada</h2>', encabezado, medidas, figura, tabla, '</section>\n<!-- fin-vista-1407 -->')
}

carpeta_reporte <- function(raiz, nombre) {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  if (length(nombre) != 1L || is.na(nombre) || !grepl("^[a-z][a-z0-9_-]{0,39}$", nombre)) stop("Reporte: nombre simple nuevo.")
  padre <- file.path(raiz, "reportes"); ruta <- file.path(padre, nombre)
  for (p in c(padre, ruta)) {
    enlace <- Sys.readlink(p)
    if ((!is.na(enlace) && nzchar(enlace)) || (dir.exists(p) && normalizePath(p, winslash = "/") != p)) stop("Reporte enlazado.")
  }
  ruta
}

documento_integracion <- function(p) paste0('---
title: "Consulta de cartera: reporte integrado"
format:
  html:
    embed-resources: true
execute:
  enabled: false
  freeze: false
  cache: false
---

Fotografía de una entrega comprobada. Cambiar datos o filtros exige preparar
otra entrega y otro reporte. La fecha de comprobación no es la fecha del corte.

', '```{=html}\n', vista_integracion(p), '\n```\n\nMD5 compara bytes; no autentica la entrega ni la sesión.\n')

generar_reporte <- function(raiz, nombre, archivo = "config/octubre.csv", app = "shiny") {
  e <- new.env(parent = globalenv()); source(file.path(raiz, "ejecutar.R"), local = e, encoding = "UTF-8")
  e$verificar_entorno(raiz)
  p <- cargar_integracion(raiz, archivo, app)
  carpeta <- carpeta_reporte(raiz, nombre)
  if (!dir.exists(dirname(carpeta)) && !dir.create(dirname(carpeta))) stop("No se pudo crear reportes.")
  if (!dir.create(carpeta, showWarnings = FALSE)) stop("Reporte ocupado; conservar y usar otro nombre.")
  claves <- c("config", "entrega", "revision", "comprobado_utc")
  write.csv(data.frame(clave = claves, valor = unlist(p[claves])), file.path(carpeta, "producto.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  for (n in c("seleccion.csv", "contexto.csv")) {
    if (!file.copy(file.path(raiz, p$entrega, n), file.path(carpeta, n), overwrite = FALSE)) stop("Copia parcial: conservar.")
  }
  con <- file(file.path(carpeta, "reporte.qmd"), open = "wb"); on.exit(close(con))
  writeBin(charToRaw(enc2utf8(documento_integracion(p))), con)
  cat("Reporte preparado, falta renderizar:", carpeta, "\n")
  invisible(carpeta)
}

normalizar_html <- function(texto) {
  for (a in c(' class="anchored"', ' class="caption-top table"', ' class="caption-top"', ' class="header"', ' class="odd"', ' class="even"', ' data-quarto-table-cell-role="th"')) texto <- gsub(a, "", texto, fixed = TRUE)
  texto <- gsub("viewBox=", "viewbox=", texto, fixed = TRUE)
  texto <- gsub("[[:space:]]+/>", "/>", texto)
  texto <- gsub(">[[:space:]]+", ">", texto)
  gsub("[[:space:]]+<", "<", texto)
}

verificar_reporte <- function(raiz, nombre, archivo = "config/octubre.csv", app = "shiny", exigir_html = TRUE) {
  p <- cargar_integracion(raiz, archivo, app)
  carpeta <- carpeta_reporte(raiz, nombre)
  leer <- function(n) utils::read.csv(file.path(carpeta, n), colClasses = "character", na.strings = NULL, check.names = FALSE)
  meta <- leer("producto.csv"); claves <- c("config", "entrega", "revision", "comprobado_utc")
  if (!identical(names(meta), c("clave", "valor")) || !identical(meta$clave, claves)) stop("Metadatos invalidos.")
  valores <- setNames(meta$valor, meta$clave)
  hora <- valores[["comprobado_utc"]]
  if (!grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$", hora) || as.integer(substr(hora, 1, 4)) < 1L) stop("Fecha invalida.")
  instante <- as.POSIXct(hora, format = "%Y-%m-%dT%H:%M:%SZ", tz = "UTC")
  if (is.na(instante) || format(instante, "%Y-%m-%dT%H:%M:%SZ", tz = "UTC") != hora) stop("Fecha invalida.")
  if (!identical(unname(unlist(p[claves[1:3]])), unname(valores[claves[1:3]]))) stop("Reporte de otra entrega/configuracion; conservar como historico.")
  p$comprobado_utc <- valores[["comprobado_utc"]]
  for (n in c("seleccion.csv", "contexto.csv")) {
    referencia <- utils::read.csv(file.path(raiz, p$entrega, n), colClasses = "character", na.strings = NULL, check.names = FALSE)
    if (!identical(leer(n), referencia)) stop("Tabla del reporte distinta.")
  }
  texto <- function(n) {
    con <- file(file.path(carpeta, n), "rb"); on.exit(close(con))
    rawToChar(readBin(con, "raw", n = file.info(file.path(carpeta, n))$size))
  }
  if (texto("reporte.qmd") != enc2utf8(documento_integracion(p))) stop("Fuente del reporte alterada.")
  if (exigir_html) {
    html <- texto("reporte.html")
    inicio <- gregexpr("<!-- inicio-vista-1407 -->", html, fixed = TRUE)[[1]]
    fin <- gregexpr("<!-- fin-vista-1407 -->", html, fixed = TRUE)[[1]]
    if (inicio[1] < 0L || fin[1] < inicio[1] || length(inicio) != 1L || length(fin) != 1L) stop("Marcadores HTML invalidos.")
    fragmento <- substr(html, inicio[1], fin[1] + nchar("<!-- fin-vista-1407 -->") - 1L)
    if (normalizar_html(fragmento) != normalizar_html(enc2utf8(vista_integracion(p)))) stop("HTML sin la vista esperada.")
  }
  invisible(p)
}

renderizar_reporte <- function(raiz, nombre, archivo = "config/octubre.csv", app = "shiny", quarto = Sys.which("quarto")) {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  verificar_reporte(raiz, nombre, archivo, app, exigir_html = FALSE)
  carpeta <- carpeta_reporte(raiz, nombre)
  if (file.exists(file.path(carpeta, "reporte.html"))) stop("HTML ocupado; conserva y usa otro reporte.")
  if (!nzchar(quarto)) {
    candidato <- "C:/Program Files/RStudio/resources/app/bin/quarto/bin/quarto.exe"
    if (file.exists(candidato)) quarto <- candidato else stop("Quarto ausente; indicar ruta, no se instala.")
  }
  anterior <- getwd(); on.exit(setwd(anterior)); setwd(carpeta)
  estado <- system2(quarto, c("render", "reporte.qmd"))
  if (estado != 0L) stop("Render fallido; conserva la carpeta parcial.")
  verificar_reporte(raiz, nombre, archivo, app)
  cat("HTML renderizado y conciliado:", file.path(carpeta, "reporte.html"), "\n")
  invisible(carpeta)
}

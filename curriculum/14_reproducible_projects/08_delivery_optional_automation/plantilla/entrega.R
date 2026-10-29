# Verificar carga herramientas locales revisadas, nunca codigo de la entrega.
herramientas_entrega <- function(raiz) {
  e <- new.env(parent = globalenv())
  for (p in c("ejecutar.R", "codigo/modelo.R", "codigo/configuracion.R", "pipeline.R", "integracion.R")) source(file.path(raiz, p), local = e, encoding = "UTF-8")
  e
}

catalogo_entrega <- function(raiz) {
  x <- utils::read.csv(file.path(raiz, "catalogo.csv"), colClasses = "character", na.strings = NULL)
  if (!identical(names(x), "archivo") || nrow(x) != 60L || anyNA(x) || anyDuplicated(x$archivo) || !identical(x$archivo, sort(x$archivo, method = "radix"))) stop("Catalogo local incompatible.")
  if (any(!grepl("^[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*$", x$archivo)) || any(vapply(strsplit(x$archivo, "/", fixed = TRUE), function(p) any(p %in% c(".", "..")), logical(1)))) stop("Ruta no admitida en catalogo local.")
  x$archivo
}

inventario_entrega <- function(raiz) {
  enlace <- Sys.readlink(raiz)
  if ((!is.na(enlace) && nzchar(enlace)) || !dir.exists(raiz)) stop("Carpeta ausente o enlazada.")
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  visitar <- function(carpeta) {
    salida <- character()
    for (p in list.files(carpeta, full.names = TRUE, all.files = TRUE, no.. = TRUE)) {
      enlace <- Sys.readlink(p); canon <- normalizePath(p, winslash = "/", mustWork = TRUE)
      distinto <- if (.Platform$OS.type == "windows") tolower(canon) != tolower(p) else canon != p
      if ((!is.na(enlace) && nzchar(enlace)) || distinto) stop("Enlace no admitido.")
      if (dir.exists(p)) salida <- c(salida, visitar(p))
      else if (file_test("-f", p)) salida <- c(salida, substring(p, nchar(raiz) + 2L))
      else stop("Archivo no regular.")
    }
    salida
  }
  sort(visitar(raiz), method = "radix")
}

nombres_paquete <- function(raiz_revisor) {
  nombres <- c("LEEME.md", "ENTREGA.csv", "MANIFIESTO.csv", paste0("fuentes/", catalogo_entrega(raiz_revisor)))
  for (caso in c("octubre", "septiembre", "vacio")) {
    nombres <- c(nombres, paste0("muestra/salidas/", caso, "_integrado/", c("seleccion.csv", "contexto.csv", "insumos.csv", "COMPLETO.csv")),
      paste0("muestra/reportes/", caso, "/", c("seleccion.csv", "contexto.csv", "producto.csv", "reporte.qmd", "reporte.html")))
  }
  sort(nombres, method = "radix")
}

verificar_entrega <- function(entrega, referencia, raiz_revisor = ".") {
  raiz_revisor <- normalizePath(raiz_revisor, winslash = "/", mustWork = TRUE)
  actuales <- inventario_entrega(entrega)
  entrega <- normalizePath(entrega, winslash = "/", mustWork = TRUE)
  revisor_comparado <- if (.Platform$OS.type == "windows") tolower(raiz_revisor) else raiz_revisor
  entrega_comparada <- if (.Platform$OS.type == "windows") tolower(entrega) else entrega
  if (revisor_comparado == entrega_comparada || startsWith(revisor_comparado, paste0(entrega_comparada, "/"))) stop("Usar herramientas revisadas fuera de la entrega.")
  if (!identical(actuales, nombres_paquete(raiz_revisor))) stop("Inventario incompatible: faltan archivos o hay extras.")
  e <- herramientas_entrega(raiz_revisor)
  leer <- function(n) e$leer_contrato(file.path(entrega, n))
  meta <- data.frame(clave = c("esquema", "app"), valor = c("1408-v1", "shiny"), stringsAsFactors = FALSE)
  if (!identical(leer("ENTREGA.csv"), meta)) stop("Esquema o ruta distinta; usar revisor R para Shiny.")
  nombres <- actuales[actuales != "MANIFIESTO.csv"]
  esperado <- data.frame(archivo = nombres, md5 = unname(as.character(tools::md5sum(file.path(entrega, nombres)))), stringsAsFactors = FALSE)
  if (!identical(leer("MANIFIESTO.csv"), esperado)) stop("Manifiesto incompatible o huellas distintas.")
  if (!identical(leer("fuentes/catalogo.csv"), e$leer_contrato(file.path(raiz_revisor, "catalogo.csv")))) stop("Catalogo recibido distinto del catalogo local revisado.")
  externa <- normalizePath(referencia, winslash = "/", mustWork = TRUE)
  if (e$dentro_proyecto(externa, entrega)) stop("La referencia debe estar fuera de la entrega.")
  datos <- e$leer_fuente_modelo(externa)
  recibidos <- e$leer_fuente_modelo(file.path(entrega, "fuentes/datos/entrada/cartera.csv"))
  ordenar <- function(x) { x <- x[order(x$id_credito, x$fecha_corte), , drop = FALSE]; rownames(x) <- NULL; x }
  if (!identical(ordenar(datos), ordenar(recibidos))) stop("Fuente distinta de la referencia externa por clave/campo.")
  fuente <- file.path(entrega, "fuentes")
  for (caso in c("octubre", "septiembre", "vacio")) {
    archivo <- paste0("config/", caso, ".csv")
    preparado <- e$tablas_esperadas(fuente, archivo, funciones = e)
    cfg <- preparado$cfg; tablas <- preparado$tablas
    esperado <- list(version_reglas = "1401-v1", entrada = "datos/entrada/cartera.csv", corte = if (caso == "septiembre") "2026-09-30" else "2026-10-31",
      segmentos = if (caso == "vacio") "servicios" else "comercio|servicios", minimo_texto = if (caso == "vacio") "1901" else "2000", app = "shiny", salida = paste0("salidas/", caso, "_integrado"))
    if (!identical(cfg[names(esperado)], esperado)) stop("Configuracion distinta del plan de entrega.")
    salida <- file.path(entrega, "muestra", cfg$salida)
    e$comprobar_1404(salida, tablas, e$leer_contrato)
    reporte <- paste0("muestra/reportes/", caso, "/")
    for (n in c("seleccion.csv", "contexto.csv")) if (!identical(leer(paste0(reporte, n)), tablas[[n]])) stop("Tabla del reporte distinta del calculo revisado.")
    producto <- leer(paste0(reporte, "producto.csv")); claves <- c("config", "entrega", "revision", "comprobado_utc")
    if (!identical(names(producto), c("clave", "valor")) || !identical(producto$clave, claves)) stop("Metadatos del reporte incompatibles.")
    valores <- setNames(producto$valor, producto$clave)
    esperado <- c(config = archivo, entrega = cfg$salida, revision = e$huella_1404(file.path(salida, "COMPLETO.csv")))
    if (!identical(unname(valores[1:3]), unname(esperado))) stop("Reporte de otra entrega/configuracion.")
    hora <- valores[["comprobado_utc"]]
    if (!grepl("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$", hora) || as.integer(substr(hora, 1, 4)) < 1L) stop("Hora UTC invalida.")
    instante <- as.POSIXct(hora, format = "%Y-%m-%dT%H:%M:%SZ", tz = "UTC")
    if (is.na(instante) || format(instante, "%Y-%m-%dT%H:%M:%SZ", tz = "UTC") != hora) stop("Hora UTC invalida.")
    p <- c(as.list(valores), list(contexto = as.list(tablas$contexto.csv[1, , drop = FALSE]), seleccion = tablas$seleccion.csv))
    texto <- function(n) { ruta <- file.path(entrega, reporte, n); con <- file(ruta, "rb"); on.exit(close(con)); rawToChar(readBin(con, "raw", n = file.info(ruta)$size)) }
    if (texto("reporte.qmd") != enc2utf8(e$documento_integracion(p))) stop("Fuente del reporte distinta.")
    html <- texto("reporte.html")
    inicio <- gregexpr("<!-- inicio-vista-1407 -->", html, fixed = TRUE)[[1]]
    fin <- gregexpr("<!-- fin-vista-1407 -->", html, fixed = TRUE)[[1]]
    if (inicio[1] < 0L || fin[1] < inicio[1] || length(inicio) != 1L || length(fin) != 1L) stop("Marcadores HTML invalidos.")
    fragmento <- substr(html, inicio[1], fin[1] + nchar("<!-- fin-vista-1407 -->") - 1L)
    if (e$normalizar_html(fragmento) != e$normalizar_html(enc2utf8(e$vista_integracion(p)))) stop("HTML sin la vista conciliada.")
  }
  cat("Entrega conciliada con referencia externa. No autentica ni aprueba el codigo recibido.\n")
  invisible(entrega)
}

destino_nuevo <- function(destino, origen, e) {
  enlace <- Sys.readlink(destino)
  if (file.exists(destino) || dir.exists(destino) || (!is.na(enlace) && nzchar(enlace))) stop("Destino ocupado; conservar y elegir otro.")
  padre <- dirname(destino)
  if (!dir.exists(padre)) stop("Crear primero la carpeta contenedora del destino.")
  ruta <- file.path(normalizePath(padre, winslash = "/", mustWork = TRUE), basename(destino))
  if (e$dentro_proyecto(ruta, normalizePath(origen, winslash = "/", mustWork = TRUE))) stop("El destino debe estar fuera del origen.")
  ruta
}

crear_entrega <- function(destino, referencia, raiz = ".") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  e <- herramientas_entrega(raiz); e$verificar_entorno(raiz)
  destino <- destino_nuevo(destino, raiz, e)
  for (caso in c("octubre", "septiembre", "vacio")) e$verificar_reporte(raiz, caso, paste0("config/", caso, ".csv"), "shiny")
  relativas <- c(paste0("fuentes/", catalogo_entrega(raiz)), nombres_paquete(raiz)[startsWith(nombres_paquete(raiz), "muestra/")])
  origenes <- ifelse(startsWith(relativas, "fuentes/"), sub("^fuentes/", "", relativas), sub("^muestra/", "", relativas))
  for (n in origenes) {
    ruta <- file.path(raiz, n); enlace <- Sys.readlink(ruta)
    if (!file_test("-f", ruta) || (!is.na(enlace) && nzchar(enlace)) || !e$dentro_proyecto(normalizePath(ruta, winslash = "/", mustWork = TRUE), raiz)) stop("Origen ausente, enlazado o fuera del proyecto.")
  }
  if (!dir.create(destino)) stop("No se pudo crear destino.")
  for (i in seq_along(relativas)) {
    final <- file.path(destino, relativas[i]); if (!dir.exists(dirname(final))) dir.create(dirname(final), recursive = TRUE)
    if (!file.copy(file.path(raiz, origenes[i]), final, overwrite = FALSE)) stop("Copia parcial: conservar.")
  }
  if (!file.copy(file.path(raiz, "LEEME_ENTREGA.md"), file.path(destino, "LEEME.md"), overwrite = FALSE)) stop("Copia parcial.")
  escribir <- function(nombre, tabla) { con <- file(file.path(destino, nombre), "wb"); on.exit(close(con)); write.table(tabla, con, sep = ",", quote = TRUE, row.names = FALSE, eol = "\n") }
  escribir("ENTREGA.csv", data.frame(clave = c("esquema", "app"), valor = c("1408-v1", "shiny")))
  nombres <- inventario_entrega(destino)
  escribir("MANIFIESTO.csv", data.frame(archivo = nombres, md5 = unname(as.character(tools::md5sum(file.path(destino, nombres))))))
  verificar_entrega(destino, referencia, raiz)
  cat("Entrega nueva creada y verificada:", destino, "\n")
  invisible(destino)
}

copiar_fuentes <- function(entrega, destino, referencia, raiz_revisor = ".") {
  raiz_revisor <- normalizePath(raiz_revisor, winslash = "/", mustWork = TRUE)
  entrega <- verificar_entrega(entrega, referencia, raiz_revisor)
  e <- herramientas_entrega(raiz_revisor)
  destino <- destino_nuevo(destino, entrega, e)
  if (!dir.create(destino)) stop("No se pudo crear destino.")
  for (n in catalogo_entrega(raiz_revisor)) {
    final <- file.path(destino, n); if (!dir.exists(dirname(final))) dir.create(dirname(final), recursive = TRUE)
    if (!file.copy(file.path(entrega, "fuentes", n), final, overwrite = FALSE)) stop("Copia parcial: conservar.")
  }
  cat("Solo fuentes copiadas. Revisarlas antes de restaurar y ejecutar:", destino, "\n")
  invisible(destino)
}

# Requiere las funciones de modelo.R; definir no lee archivos.
ruta_relativa <- function(texto) {
  partes <- strsplit(texto, "/", fixed = TRUE)[[1]]
  if (!grepl("^[A-Za-z0-9_-]+(/[A-Za-z0-9_. -]+)+$", texto) ||
      any(partes %in% c(".", "..")) || any(grepl("[. ]$", partes))) stop("Ruta relativa invalida.")
  texto
}
dentro_proyecto <- function(ruta, raiz) {
  if (.Platform$OS.type == "windows") { ruta <- tolower(ruta); raiz <- tolower(raiz) }
  startsWith(ruta, paste0(raiz, "/"))
}
archivo_proyecto <- function(raiz, texto) {
  ruta <- normalizePath(file.path(raiz, ruta_relativa(texto)), winslash = "/", mustWork = TRUE)
  if (!dentro_proyecto(ruta, raiz) || dir.exists(ruta)) stop("Archivo fuera del proyecto o no regular.")
  ruta
}
leer_configuracion <- function(raiz, archivo = "config/consulta.csv") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  if (!dir.exists(raiz)) stop("Indica una carpeta de proyecto.")
  if (!startsWith(archivo, "config/") || !endsWith(archivo, ".csv")) stop("Configuracion: CSV dentro de config/.")
  tabla <- leer_contrato(archivo_proyecto(raiz, archivo))
  claves <- c("version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida")
  if (!identical(names(tabla), c("clave", "valor")) || anyNA(tabla) || nrow(tabla) != length(claves) ||
      anyDuplicated(tabla$clave) || !setequal(tabla$clave, claves)) stop("Configuracion: claves exactas sin repetir.")
  config <- as.list(setNames(tabla$valor, tabla$clave))
  if (config$version_reglas != "1401-v1") stop("Version de reglas no implementada.")
  if (!fecha_contrato(config$corte) || !config$segmentos %in% c("ninguno", "comercio", "servicios", "comercio|servicios", "servicios|comercio")) stop("Corte o segmentos invalidos.")
  if (!grepl("^(0|[1-9][0-9]{0,6})$", config$minimo_texto) || as.numeric(config$minimo_texto) > 1000000) stop("Minimo: entero canonico 0..1000000.")
  if (!config$app %in% c("streamlit", "shiny")) stop("Elige una app: streamlit o shiny.")
  if (!startsWith(config$entrada, "datos/entrada/") || !endsWith(config$entrada, ".csv")) stop("Entrada: CSV dentro de datos/entrada/.")
  entrada <- archivo_proyecto(raiz, config$entrada)
  if (!grepl("^salidas/[a-z][a-z0-9_-]{0,39}$", config$salida)) stop("Salida: salidas/nombre_simple.")
  padre <- normalizePath(file.path(raiz, "salidas"), winslash = "/", mustWork = TRUE)
  if (!dentro_proyecto(padre, raiz) || !dir.exists(padre)) stop("Carpeta salidas fuera del proyecto o ausente.")
  salida <- file.path(padre, sub("^salidas/", "", config$salida))
  enlace <- Sys.readlink(salida)
  if (file.exists(salida) || dir.exists(salida) || (!is.na(enlace) && nzchar(enlace))) stop("Salida ocupada: elige otro nombre.")
  c(config, list(raiz = raiz, entrada_resuelta = entrada, salida_resuelta = salida))
}

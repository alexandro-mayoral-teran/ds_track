# Cargar define; ejecutar requiere biblioteca renv ya activada/restaurada de la copia.
ejecutar_reconstruible <- function(raiz, evidencia, archivo = "config/consulta.csv") {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  declarado <- utils::read.csv(file.path(raiz, "entorno.csv"), colClasses = "character", na.strings = NULL)
  claves <- c("esquema", "python", "r", "dependencias_python", "dependencias_r")
  if (!identical(names(declarado), c("clave", "valor")) || nrow(declarado) != 5L || anyDuplicated(declarado$clave) ||
      !setequal(declarado$clave, claves) || anyNA(declarado)) stop("Declaracion de entorno incompatible.")
  d <- setNames(declarado$valor, declarado$clave)
  if (d[["esquema"]] != "1403-v1" || d[["dependencias_r"]] != "distribucion_R_y_renv") stop("Esquema/dependencias no implementados.")
  if (as.character(getRversion()) != d[["r"]]) stop("Version R distinta de la declarada.")
  biblioteca <- normalizePath(.libPaths()[1], winslash = "/", mustWork = TRUE)
  prefijo <- paste0(raiz, "/renv/library/")
  if (!startsWith(tolower(biblioteca), tolower(prefijo)) || !requireNamespace("renv", quietly = TRUE)) stop("Activa/restaura la biblioteca local de esta copia.")
  if (as.character(utils::packageVersion("renv")) != "1.3.1" ||
      normalizePath(renv::project(), winslash = "/", mustWork = TRUE) != raiz || !isTRUE(renv::status(project = raiz)$synchronized)) stop("Proyecto/biblioteca/lockfile no sincronizados.")
  if (!grepl("^evidencia/[a-z][a-z0-9_-]{0,39}\\.csv$", evidencia)) stop("Evidencia: evidencia/nombre_nuevo.csv.")
  destino <- file.path(raiz, evidencia); padre <- dirname(destino)
  enlace <- Sys.readlink(destino)
  if (file.exists(destino) || dir.exists(destino) || (!is.na(enlace) && nzchar(enlace))) stop("La evidencia existe; elige otro nombre.")
  if (dir.exists(padre) && normalizePath(padre, winslash = "/", mustWork = TRUE) != file.path(raiz, "evidencia")) stop("Carpeta de evidencia enlazada a otro lugar.")
  entorno <- new.env(parent = globalenv())
  source(file.path(raiz, "revisar.R"), local = entorno, encoding = "UTF-8")
  resultado <- entorno$revisar_proyecto(raiz, archivo)
  config <- utils::read.csv(file.path(raiz, archivo), colClasses = "character", na.strings = NULL)
  registro <- c(esquema = "1403-v1", fecha_utc = format(Sys.time(), tz = "UTC", usetz = TRUE),
    runtime = "r", version = as.character(getRversion()), ejecutable = commandArgs()[1],
    raiz = raiz, entorno_local = biblioteca, sistema = paste(Sys.info()[c("sysname", "release", "machine")], collapse = " / "),
    dependencias_calculo = "distribucion_R", bibliotecas = paste(.libPaths(), collapse = "|"))
  quarto <- unname(Sys.which("quarto"))
  registro <- c(registro, quarto_ruta = if (nzchar(quarto)) quarto else "no_disponible_en_PATH",
    quarto_version = if (nzchar(quarto)) paste(tryCatch(system2(quarto, "--version", stdout = TRUE, stderr = TRUE), error = function(e) "error_al_consultar"), collapse = " ") else "no_consultada")
  registro <- c(registro, setNames(config$valor, paste0("config.", config$clave)), setNames(resultado, paste0("resultado.", names(resultado))))
  entrada <- config$valor[config$clave == "entrada"]
  rutas <- c(entrada = file.path(raiz, entrada), config = file.path(raiz, archivo), declaracion = file.path(raiz, "entorno.csv"), lockfile = file.path(raiz, "renv.lock"))
  registro <- c(registro, setNames(unname(as.character(tools::md5sum(rutas))), paste0("md5.", names(rutas))))
  if (!dir.exists(padre) && !dir.create(padre)) stop("No se pudo crear carpeta evidencia.")
  utils::write.csv(data.frame(clave = names(registro), valor = unname(registro)), destino, row.names = FALSE, fileEncoding = "UTF-8")
  cat("Evidencia nueva: ", destino, ". No autentica sesiones pasadas.\n", sep = "")
  invisible(resultado)
}

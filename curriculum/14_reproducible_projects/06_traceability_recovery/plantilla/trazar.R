# Cargar define funciones; no ejecuta el pipeline ni escribe registros.
trazar_proyecto <- function(raiz, intento, archivo = "config/consulta.csv",
                            simular_fallo = FALSE, simular_fallo_final = FALSE) {
  raiz <- normalizePath(raiz, winslash = "/", mustWork = TRUE)
  if (length(intento) != 1L || is.na(intento) || !grepl("^[a-z][a-z0-9_-]{0,39}$", intento)) stop("Intento: nombre simple de hasta 40 caracteres.")
  if (!is.logical(simular_fallo) || length(simular_fallo) != 1L || is.na(simular_fallo) ||
      !is.logical(simular_fallo_final) || length(simular_fallo_final) != 1L || is.na(simular_fallo_final) ||
      (simular_fallo && simular_fallo_final)) stop("Elige una sola falla didactica logica.")
  padre <- file.path(raiz, "intentos")
  enlace <- Sys.readlink(padre)
  if ((!is.na(enlace) && nzchar(enlace)) || (dir.exists(padre) && normalizePath(padre, winslash = "/") != padre)) stop("Carpeta intentos enlazada.")
  if (!dir.exists(padre) && !dir.create(padre)) stop("No se pudo crear intentos.")
  carpeta <- file.path(padre, intento)
  if (!dir.create(carpeta, showWarnings = FALSE)) stop("Intento ocupado; conservar y elegir otro.")
  escribir <- function(nombre, tabla) {
    ruta <- file.path(carpeta, nombre)
    if (file.exists(ruta)) stop("Registro ocupado.")
    con <- file(ruta, open = "wt", encoding = "UTF-8"); on.exit(close(con))
    write.table(tabla, con, sep = ",", quote = TRUE, row.names = FALSE, eol = "\n", na = "")
  }
  secuencia <- 0L
  etapa <- "entorno"
  eventos <- file.path(carpeta, "eventos.csv")
  escribir("eventos.csv", data.frame(secuencia = integer(), fecha_utc = character(), intento = character(), etapa = character(), evento = character(), detalle = character()))
  evento <- function(tipo, detalle) {
    secuencia <<- secuencia + 1L
    fila <- data.frame(secuencia = secuencia, fecha_utc = format(Sys.time(), "%Y-%m-%dT%H:%M:%OS3Z", tz = "UTC"), intento = intento, etapa = etapa, evento = tipo, detalle = detalle)
    con <- file(eventos, open = "at", encoding = "UTF-8"); on.exit(close(con))
    write.table(fila, con, sep = ",", quote = TRUE, row.names = FALSE, col.names = FALSE, eol = "\n")
  }
  evento("INICIO", paste("1406-v1; r", getRversion()))
  tryCatch({
    e <- new.env(parent = globalenv())
    for (p in c("ejecutar.R", "codigo/modelo.R", "codigo/configuracion.R", "pipeline.R")) source(file.path(raiz, p), local = e, encoding = "UTF-8")
    e$verificar_entorno(raiz)
    evento("OK", "Entorno local comprobado")
    etapa <- "configuracion"
    cfg <- e$leer_configuracion(raiz, archivo, permitir_existente = TRUE)
    contexto <- c(unlist(cfg[c("version_reglas", "entrada", "corte", "segmentos", "minimo_texto", "app", "salida")]),
      config = archivo, raiz = raiz, ejecutable = commandArgs()[1], simular_fallo = as.character(simular_fallo), simular_fallo_final = as.character(simular_fallo_final))
    escribir("consulta.csv", data.frame(clave = names(contexto), valor = unname(contexto)))
    evento("OK", cfg$salida)
    etapa <- "huellas"
    rutas <- c(archivo, cfg$entrada, "entorno.csv", "renv.lock", "DESCRIPTION", ".Rprofile", "renv/activate.R", "renv/settings.json",
      "ejecutar.R", "revisar.R", "codigo/modelo.R", "codigo/configuracion.R", "pipeline.R", "trazar.R")
    huellas <- function() {
      valores <- unname(as.character(tools::md5sum(file.path(raiz, rutas))))
      if (anyNA(valores)) stop("No se pudo leer un insumo para su huella.")
      data.frame(archivo = rutas, md5 = valores, stringsAsFactors = FALSE)
    }
    antes <- huellas()
    escribir("huellas.csv", antes)
    evento("OK", "Huellas de fuente, configuracion, codigo y metadatos")
    etapa <- "fuente"
    datos <- e$leer_fuente_modelo(cfg$entrada_resuelta)
    resultado <- e$resolver_contrato(datos, cfg$corte, cfg$segmentos, cfg$minimo_texto)
    evento("OK", paste0("estado_consulta=", resultado[["estado"]]))
    etapa <- "pipeline"
    evento("ENTRADA", "Ver consola.txt; la etapa agrupa escritura y comprobacion")
    # on.exit restaura la salida tambien si el pipeline lanza un error.
    ejecutar_con_salida <- function() {
      con <- file(file.path(carpeta, "consola.txt"), open = "wt", encoding = "UTF-8")
      on.exit(close(con))
      sink(con)
      on.exit(sink(), add = TRUE, after = FALSE)
      e$pipeline_proyecto(raiz, archivo, simular_fallo)
    }
    accion <- ejecutar_con_salida()
    evento("OK", accion)
    etapa <- "cierre"
    if (simular_fallo_final) stop("Fallo didactico despues de publicar/comprobar; revisar la entrega.")
    if (!identical(antes, huellas())) stop("Insumos cambiaron durante el intento; revisar entrega en otro intento.")
    evento("TERMINADO", accion)
    cat("Intento terminado:", carpeta, "; entrega", accion, "\n")
    invisible(accion)
  }, error = function(error) {
    # El manejador recibe la condicion cuando la pila ya se ha desenrollado.
    # Se conserva clase/mensaje/llamada; no se presenta como traceback completo.
    llamada <- paste(deparse(conditionCall(error)), collapse = " ")
    escribir("error.csv", data.frame(clase = paste(class(error), collapse = "|"), mensaje = conditionMessage(error), llamada = llamada))
    evento("FALLO", conditionMessage(error))
    stop(error)
  })
}

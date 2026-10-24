# Cargar desde la raíz del repositorio; no requiere paquetes externos.
preparar_documento <- function(origen, destino, raiz = ".") {
  carpeta <- file.path(raiz, "curriculum/11_reporting_quarto/02_first_document")
  referencia <- new.env(parent = baseenv())
  sys.source(file.path(raiz, "curriculum/11_reporting_quarto/01_report_source_render/preparar.R"),
             envir = referencia)
  # read.csv/write.csv del preparador pertenecen a utils (R base distribuido).
  referencia$read.csv <- utils::read.csv
  referencia$write.csv <- utils::write.csv
  inicio <- readLines(file.path(carpeta, "inicio.qmd"), encoding = "UTF-8", warn = FALSE)
  resultado <- referencia$preparar_reporte(origen, destino)
  borrador <- readLines(file.path(destino, "borrador.md"), encoding = "UTF-8")
  posicion <- match("## Pregunta y público", borrador)
  if (is.na(posicion)) stop("Falta el inicio del contenido editorial")
  contenido <- borrador[seq.int(posicion, length(borrador))]
  writeLines(enc2utf8(c(inicio, "", contenido)), file.path(destino, "reporte.qmd"), useBytes = TRUE)
  invisible(resultado)
}

# Desde la raiz de DS Track: copia solo fuentes y metadatos, sin instalar paquetes.
argumentos <- commandArgs(trailingOnly = TRUE)
if (length(argumentos) > 1L) { stop("Indica como maximo una carpeta nueva.") }
destino <- "curriculum/06_r_foundations/09_known_result/output/cierre_ventas"
if (length(argumentos) == 1L) { destino <- argumentos[1] }
if (file.exists(destino) || dir.exists(destino)) { stop("El destino ya existe; elige otro.") }
base <- "curriculum/06_r_foundations"
plantilla <- file.path(base, "08_projects_renv", "plantilla")
cierre <- file.path(base, "09_known_result")
origenes <- c(
  file.path(plantilla, c(".Rprofile", ".gitignore", "DESCRIPTION", "renv.lock", "restaurar.R")),
  file.path(plantilla, "renv", c("activate.R", "settings.json")),
  file.path(base, "06_functions_control", "funciones_ventas.R"),
  file.path(base, "07_files_validation", c("funciones_archivos.R", "ventas_entrada.csv")),
  file.path(cierre, c("referencia_python.py", "ejecutar_cierre.R", "verificar_cierre.R",
                      "comparar_resultados.R", "README_copia.md"))
)
relativas <- c(".Rprofile", ".gitignore", "DESCRIPTION", "renv.lock", "restaurar.R",
               "renv/activate.R", "renv/settings.json", "R/funciones_ventas.R",
               "R/funciones_archivos.R", "datos/ventas_entrada.csv", "referencia_python.py",
               "ejecutar_cierre.R", "verificar_cierre.R", "R/comparar_resultados.R", "README.md")
if (!all(file.exists(origenes))) { stop("Faltan fuentes; ejecuta desde la raiz de DS Track.") }
if (!dir.create(destino, recursive = TRUE)) { stop("No se pudo crear el destino.") }
for (carpeta in c("R", "datos", "renv")) {
  if (!dir.create(file.path(destino, carpeta))) { stop("No se pudo crear una subcarpeta.") }
}
for (i in seq_along(origenes)) {
  if (!file.copy(origenes[i], file.path(destino, relativas[i]), overwrite = FALSE)) {
    stop("La copia quedo parcial; conserva la carpeta y revisa el error.")
  }
}
cat("Copia de cierre preparada sin instalar paquetes:\n")
print(destino)

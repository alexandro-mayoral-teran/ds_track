# Requiere las funciones de cartera.R; definir no lee ni modifica la fuente.
crear_consulta <- function(cartera, filtros) {
  universo <- seleccionar_corte(cartera, filtros$corte)
  seleccion <- filtrar_seleccion(universo, filtros$segmentos, filtros$minimo_mxn)
  list(filtros = filtros, universo = universo, seleccion = seleccion,
       indicadores = resumir_seleccion(seleccion, nrow(universo)))
}

# 06.03: las mismas cuatro ventas de 06.02, sin depender de aquella sesion.
id_venta <- c("V001", "V002", "V003", "V004")
unidades <- c(4L, 2L, 0L, 3L)
precio_mxn <- c(75, 120, 50, 40)
importe_mxn <- unidades * precio_mxn

# [ selecciona un subconjunto y respeta el orden del indice solicitado.
posiciones <- c(4L, 1L)
print("Ventas pedidas por posicion, en orden 4 y 1:")
print(id_venta[posiciones])       # V004 V001
print(importe_mxn[posiciones])    # 120 300
print("Importes excluyendo posiciones 2 y 4:")
print(importe_mxn[-c(2L, 4L)])    # 300 0

# Los nombres son etiquetas del vector; no hacen una union de datos.
importes_por_venta <- importe_mxn
names(importes_por_venta) <- id_venta
print("Seleccion por nombre, con nombres conservados:")
print(importes_por_venta[c("V004", "V001")])
print("Un valor extraido de vector atomico, sin su etiqueta:")
print(importes_por_venta[["V004"]]) # 120, longitud 1 y sin names.

# Una mascara debe corresponder a las mismas posiciones de todos los vectores.
elegidas <- c(TRUE, FALSE, FALSE, TRUE)
ids_elegidos <- id_venta[elegidas]
importes_elegidos <- importe_mxn[elegidas]
print("Mascara: primera y cuarta venta, en orden original:")
print(ids_elegidos)               # V001 V004
print(importes_elegidos)          # 300 120
print(sum(importes_elegidos))     # 420

# > produce un TRUE/FALSE por cantidad; reglas logicas completas en 06.04.
con_unidades <- unidades > 0L
print("Ventas con unidades positivas:")
print(id_venta[con_unidades])      # V001 V002 V004
print(length(id_venta[con_unidades])) # 3; la fuente aun contiene 4 ventas.
print(sum(importe_mxn[con_unidades])) # 660: el total no revela el cambio de conteo.

# Vista minima de listas para contrastar contenedor y contenido (detalle en 06.05).
paquete_ventas <- list(importes = importes_por_venta, moneda = "MXN")
print("[ devuelve una lista de un componente:")
print(typeof(paquete_ventas["importes"]))  # list
print(length(paquete_ventas["importes"]))  # 1
print("[[ y $ extraen el vector que contiene ese componente:")
print(paquete_ventas[["importes"]])
print(paquete_ventas$importes)
campo <- "importes"
print(paquete_ventas[[campo]])    # Nombre calculado, coincidencia exacta por defecto.

# Modificar una copia conserva los precios usados por el analisis anterior.
precios_variante <- precio_mxn
precios_variante[4] <- 60
print("Total de una variante con cuarto precio 60:")
print(sum(unidades * precios_variante)) # 720; precio_mxn sigue 75,120,50,40.
print(R.version.string)
print(utils::sessionInfo())

# 06.01: una venta ficticia, definida completa dentro de este archivo.
# Ejecutar desde el principio debe reconstruir el resultado sin objetos previos.
unidades <- 4
precio_mxn <- 75
total_mxn <- unidades * precio_mxn

# print hace visible el resultado tanto al usar source como desde Rscript.
print("Total de la venta (MXN):")
print(total_mxn)

# Estas salidas describen la sesión; no se esperan rutas idénticas entre equipos.
print("Version de R:")
print(R.version.string)
print("Directorio de trabajo:")
print(getwd())
print("Instalacion de R en uso:")
print(R.home())
print("Bibliotecas de paquetes consultadas:")
print(.libPaths())
print("Version del paquete utils incluido con R:")
print(utils::packageVersion("utils"))
print("Informacion de la sesion:")
print(utils::sessionInfo())

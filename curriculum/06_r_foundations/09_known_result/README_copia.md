# Copia de cierre de R fundamental

Desde esta carpeta, con Python y R ya elegidos:

1. `Rscript --vanilla restaurar.R` activa y restaura renv/withr localmente.
2. `python referencia_python.py datos/ventas_entrada.csv output/referencia_python`
   genera las tablas Python y su contexto sobre esta misma fuente.
3. `Rscript --vanilla ejecutar_cierre.R` calcula en R, compara con Python,
   exporta y relee los CSV; escribe la conciliación al final.
4. `Rscript --vanilla verificar_cierre.R` recalcula y comprueba sin escribir.

En Windows adapta Rscript a la ruta de tu instalación. La lección y el lab
06.09 de DS Track contienen los recorridos completos por shell y la explicación.
Python usa solo biblioteca estándar; se conserva el lockfile de 06.08 para R.
No se instalan paquetes al preparar la copia ni al ejecutar el verificador.

Se esperan 14 entradas, 8 aceptados, 6 rechazos; 6 importes conocidos de 8,
cobertura 75%, suma observada 765.5 MXN y total completo desconocido.
El informe tiene 72 controles: 36 sobre cálculo y 36 sobre CSV guardados.
Comparar con Python no acredita aprendizaje ni garantiza que el contrato elegido
sea el adecuado para otro dominio.

Los scripts admiten otras muestras del mismo contrato. Python recibe entrada
y destino nuevo; ejecutar_cierre.R/verificar_cierre.R reciben entrada, referencia
y entrega juntos. El umbral de este cierre es 200 MXN en ambos lenguajes.
Conserva fuentes y entregas anteriores; una carpeta existente se rechaza.
Las escrituras pueden dejar una carpeta parcial ante un error.

Transfiere fuentes, datos sintéticos, DESCRIPTION, renv.lock, .Rprofile y los
archivos de activación/configuración renv. No transfieras bibliotecas, cachés,
output/, .RData ni .Rhistory como si fueran fuentes. Las rutas son relativas
a esta copia; no depende de otras carpetas de DS Track después de prepararla.

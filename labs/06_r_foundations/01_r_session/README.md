# Lab 06.01 — Ejecutar un script e identificar su sesión

## Propósito, entradas y resultado

Esta práctica acompaña [06.01 — R, editor, scripts y paquetes](../../../curriculum/06_r_foundations/01_r_session/README.md).
Usa el recorrido completo de tu shell de esa lección o la consola de R/RStudio.
Recibes [primer_script.R](../../../curriculum/06_r_foundations/01_r_session/primer_script.R),
una venta ficticia de cuatro unidades a 75 MXN y funciones incluidas con R.
No necesitas instalar paquetes externos ni modificar el entorno Python.

Conserva una nota personal con comando, resultado, versión, instalación y sesión;
además, una variante propia del script y explicación de un error. Guarda tu
práctica en una carpeta personal output ignorada por Git, conservando el original.
Una sesión puede cubrir solo parte del lab. No hay proyecto/checkpoint
implementado asociado.

## A. Identificar dónde se ejecuta cada instrucción

Explica dónde escribes Rscript --version y dónde ejecutas R.version.string.
Comprueba tu instalación antes de instalar otra. Si utilizas RStudio y terminal,
compara versión y R.home() en ambos. Registra diferencias, aunque ambos programas
parezcan abrir R correctamente.

<details>
<summary>Orientación</summary>

Rscript --version se ejecuta en la terminal. R.version.string se evalúa en una
consola de R o dentro de un script. RStudio es el editor/entorno de desarrollo;
no es una versión del intérprete R. Dos interfaces pueden usar instalaciones
distintas. La salida de R.home() permite reconocer esa diferencia sin cambiar PATH
ni reinstalar por ensayo. En PowerShell, r puede ser un alias del historial.

</details>

## B. Predecir, ejecutar y comprobar

Antes de ejecutar, explica cómo las tres asignaciones producen total_mxn.
Ejecuta el archivo completo con el recorrido de tu shell, dos veces. Comprueba
total 300 y código 0 inmediatamente después de cada ejecución. Si usas source
en RStudio, reinicia R y ejecuta el archivo completo, no solo la última línea.

Registra getwd(), R.home(), .libPaths() y sessionInfo(). Distingue qué valores
deben permanecer iguales y cuáles dependen del equipo. Copia la evidencia a
output/sesion_01.md con tu editor, usando otro nombre si ya existe.

<details>
<summary>Comprobación esperada</summary>

4 × 75 = 300 MXN. El prefijo [1] acompaña la impresión y no modifica ese importe.
El total debe coincidir en las dos ejecuciones; las rutas no tienen por qué
coincidir entre equipos. getwd() ubica el trabajo, R.home() la instalación y
.libPaths() las bibliotecas de paquetes. sessionInfo() describe el contexto;
no guarda una receta de instalación ni sustituye el código.

</details>

## C. Preparar una variante reconstruible

Copia el script en output/mi_venta.R usando el editor. Cambia la entrada a seis
unidades y conserva precio_mxn en 75. Antes de ejecutar, predice el resultado.
Vuelve a usar el recorrido completo de tu shell con la ruta de esa copia en lugar
de primer_script.R. No edites solo total_mxn para forzar la respuesta.

Explica si necesitas volver a ejecutar la multiplicación después de cambiar
unidades en una consola ya abierta. Comprueba tu variante desde una sesión nueva.

<details>
<summary>Una solución razonada</summary>

Las líneas del cálculo en tu copia quedan así; conserva debajo el diagnóstico
de sesión del archivo original:

```r
unidades <- 6
precio_mxn <- 75
total_mxn <- unidades * precio_mxn
print(total_mxn)
```

El resultado esperado es 450. total_mxn contiene el valor que se calculó cuando
se ejecutó su asignación; no es una fórmula que se actualice automáticamente al
cambiar unidades. Ejecutar el archivo completo vuelve a definir entradas y cálculo.
Esta práctica no necesita una tabla ni un bucle.

</details>

## D. Reconocer una dependencia escondida y corregirla

Crea con tu editor output/solo_resultado.R que contenga únicamente
`print(total_mxn)`. En una consola de R donde ya ejecutaste el script completo,
usa source con la ruta de esa copia. Después ejecútala desde Rscript --vanilla
siguiendo el recorrido de tu shell y cambiando solo la ruta del archivo.

Registra qué sucede, el mensaje y el código de salida. Corrige esa copia para
que defina sus entradas y cálculo. No restaures .RData para ocultar el problema;
conserva el archivo original del curso.

<details>
<summary>Por qué falla y cómo comprobar la corrección</summary>

source utiliza la sesión existente y puede encontrar total_mxn en memoria.
El proceso nuevo de Rscript --vanilla no tiene ese objeto: informa un error de
objeto no encontrado y devuelve un código distinto de cero. El texto puede variar
por idioma. La corrección es incluir las asignaciones antes de print y volver a
ejecutar desde cero. Reiniciar la consola es una comprobación útil; limpiar su
pantalla no quita los objetos.

</details>

## E. Consultar ayuda y distinguir paquetes

En R, consulta help("print", package = "base") y
help("sessionInfo", package = "utils"). Identifica para qué sirve cada función
y un argumento documentado. Después consulta utils::packageVersion("stats") y
ejecuta library(stats), un paquete ya incluido.

Explica qué haría instalar un paquete, qué hace library y por qué usar :: no
descarga archivos. No ejecutes install.packages en esta práctica. Si hay una
diferencia con un libro, anota versión y contrasta con la ayuda instalada.

<details>
<summary>Interpretación posible</summary>

Instalar guarda archivos en una biblioteca; library adjunta un paquete instalado
para buscar sus nombres sin prefijo. paquete::funcion identifica una función
exportada y puede cargar su namespace sin adjuntarlo. Ni library ni :: instalan.
La versión de stats corresponde a tu instalación, no al número de versión de
RStudio. La práctica usa paquetes ya incluidos; la gestión del proyecto con
renv llegará en 06.08.

</details>

## Evidencia, reflexión y continuidad

Conserva nota de sesión, variante de 450 MXN, error observado y explicación de
la corrección. Las rutas pueden contener datos personales: revisa qué compartes.

- ¿Qué partes de tu resultado reconstruye el archivo y cuáles describen el equipo?
- ¿Por qué guardar un archivo no equivale a ejecutarlo?
- ¿Por qué source en una sesión usada no basta para probar independencia?
- ¿Qué diferencia hay entre biblioteca de paquetes y objetos de tu sesión?

Puedes cerrar la práctica cuando ejecutes y expliques el resultado desde una
sesión nueva. Registra evidencia real y dudas en PROGRESS.md; tener esta lección
no acredita haberla completado.

Continúa con la siguiente lección prevista:
[plan 06.02 — Objetos, vectores y tipos](../../../curriculum/06_r_foundations/README.md#02-objetos-vectores-y-tipos),
todavía pendiente. Volver a la [lección 06.01](../../../curriculum/06_r_foundations/01_r_session/README.md).

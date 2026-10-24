# Lab 11.03 — Recalcular el reporte en el entorno correcto

Módulo: 11 — Reportes con Quarto. Tiempo orientativo: 60–90 minutos, aparte
de descargas/restauración si preparas un entorno por primera vez.

## Entrada y objetivo

Lee la [lección 11.03](../../../curriculum/11_reporting_quarto/03_execution_python_r/README.md)
y elige **un** recorrido: Python/Jupyter o R/knitr. Usa sus preparadores y
lockfiles; no necesitas carpetas de práctica de 11.01/11.02. El objetivo es
demostrar que el render lee datos y ejecuta funciones guardadas desde cero.

La [entrada completa](../../../curriculum/11_reporting_quarto/03_execution_python_r/cartera.csv)
contiene seis filas: IDs 001/002/003 en 2026-09-30 y 2026-10-31; saldos
septiembre 1000/2000/3000 y octubre 1200/1800/3300 MXN. Cada clave ID/fecha
aparece una vez. Saldo entero entre 0 y 1000000, sin ausencias. Esta comparación
no necesita recordar otra base de cartera.

## Actividad esencial

1. Prepara el entorno y la carpeta de práctica con el recorrido completo de la
   lección. Anota versión de Quarto, Python/R y paquetes de ejecución. Distingue
   instalar/restaurar dependencias de copiar fuentes y de ejecutar un reporte.
2. Crea y renderiza el documento mínimo del lenguaje elegido: debe producir
   6300 desde sus tres valores. Después renderiza el reporte completo de la
   práctica, no el template del curriculum. Revisa el mensaje de comprobación
   del entorno y cada par, además de los totales.
3. Conserva una copia del primer HTML y del CSV en una carpeta de evidencia.
   Cambia **en tu práctica** 003/octubre de 3300 a 3600. No modifiques archivos
   del curriculum. Renderiza el mismo `.qmd` **sin volver a usar el preparador**.
   Predice y comprueba octubre, diferencia, tasa y el par de 003.
4. Reinicia la sesión del IDE o utiliza una terminal nueva, selecciona de nuevo
   el entorno y renderiza todo. No ejecutes previamente una asignación a
   `resultado` en la consola. El reporte debe reconstruirse desde sus archivos.
5. En tu práctica renombra temporalmente `cartera.csv` (Python) o
   `datos/cartera_1103.csv` (R). Intenta renderizar y guarda el error. Comprueba
   que el intento no se presenta como éxito nuevo aunque un HTML anterior siga
   en disco. Restaura el nombre y comprueba recuperación con otro render.
6. Repite el diagnóstico con el archivo de funciones (`analisis.py` o
   `R/analisis_1103.R`) temporalmente ausente. No copies resultados a mano ni
   cambies `error: false`. Restaura el archivo y renderiza de nuevo.

No cambies o elimines paquetes de un entorno que ya funciona para provocar un
error. La ausencia temporal de archivos permite practicar el diagnóstico y
recuperar la práctica sin modificar sus dependencias.

## Repetir el render

Estos bloques presuponen preparación ya completada. Si Quarto requiere ruta
completa, sustituye el valor de la variable como indica la lección.

### Python — PowerShell

Desde la raíz de DS Track, usando el entorno uv local del recorrido:

```powershell
$quarto1103 = "quarto"
$env:QUARTO_PYTHON = (Resolve-Path "output/1103_entorno/Scripts/python.exe").Path
& $quarto1103 render output/1103_python/reporte_python.qmd --to html
```

### Python — Bash/Zsh

Desde la raíz:

```bash
quarto1103="quarto"
export QUARTO_PYTHON="$PWD/output/1103_entorno/bin/python"
"$quarto1103" render output/1103_python/reporte_python.qmd --to html
```

### R — IDE y terminal opcional

Abre `ejecucion_1103.Rproj` en el proyecto preparado, reinicia la sesión R y
renderiza el `.qmd` completo. En la consola R, `renv::status()` debe indicar
sincronización. No escribas comandos del sistema en esa consola.

Para comprobar desde otra ejecución, en la terminal del sistema situada en
la carpeta del proyecto R preparado:

**PowerShell:**

```powershell
$quarto1103 = "quarto"
$env:QUARTO_R = "C:/Program Files/R/R-4.6.1/bin"
& $quarto1103 render reporte_1103.qmd --to html
```

**Bash/Zsh:**

```bash
quarto1103="quarto"
export QUARTO_R="$(dirname "$(command -v Rscript)")"
"$quarto1103" render reporte_1103.qmd --to html
```

Usa tu ruta real de R; la primera es la del equipo de autoría. No hace falta
instalar otro motor si elegiste el recorrido Python.

## Resultado, comprobación y evidencia

Entrega los fuentes y CSV de tu práctica, las dos versiones conservadas del
HTML y unas notas sobre entorno elegido, cambio de datos y errores recuperados.
Mantén cada copia de entrada junto a la evidencia que describe; no atribuyas
el primer HTML al CSV modificado. No incluyas bibliotecas, entornos ni cachés
en Git. La lectura del HTML no necesita los motores, pero reconstruirlo sí.

<details>
<summary>Solución razonada</summary>

La primera respuesta es septiembre 6000 MXN, octubre 6300, diferencia +300 y
5.00% sobre septiembre. Pares: 001 +200, 002 -200 y 003 +300. La comprobación
Python ocurre dentro del kernel; en R se comprueba proyecto/biblioteca. Que la
consola interactiva funcionara antes no sustituye estos controles.

Tras cambiar solo el saldo indicado, el mismo `.qmd` produce octubre 6600,
diferencia +600 y 10.00%; el par 003 cambia a +600. Los otros pares y septiembre
no cambian. A diferencia de 11.02, no hay que regenerar texto con el preparador:
el bloque ejecutable lee el CSV durante cada render.

Una entrada ausente y una función ausente deben detener la ejecución. Conservar
un HTML previo en disco no demuestra que el intento haya funcionado. La
recuperación consiste en restituir el archivo correcto y renderizar desde cero,
sin editar la salida ni ocultar el error. Una terminal nueva necesita volver
a seleccionar intérprete y, para R, entrar en la raíz del proyecto preparado.

La suma crece, pero no todos los créditos crecen. No se puede atribuir el cambio
a cobranza ni extrapolarlo a una cartera real. La comprobación de pares evita
ocultar dos cambios compensados detrás de una suma idéntica.

</details>

## Ampliaciones opcionales

- En otra copia deja septiembre entero en cero. La diferencia sigue calculándose,
  pero la tasa debe quedar no definida. Un cero de base no es una tasa de 0%.
- Repite una clave o elimina una fila en una copia: el render debe detenerse.
  No se permite fingir cobertura completa imputando o eliminando registros.
- Cambia dos saldos de octubre, uno +100 y otro -100. La suma no cambia, pero sí
  los pares. Explica por qué comparar solo totales no detecta toda diferencia.
- Ejecuta el otro lenguaje con su propio entorno y compara por clave, no por
  bytes del HTML ni por formato de impresión.

## Reflexión y siguiente paso

En [PROGRESS.md](../../../PROGRESS.md) registra evidencia y responde: ¿qué
proceso ejecutó los cálculos?, ¿qué archivos necesita una sesión nueva?, ¿cómo
distingues un render fallido de un HTML anterior?, ¿qué cambió frente a 11.02?

Puedes avanzar cuando reconstruyes sin objetos ocultos, justificas cada cifra
y reconoces fallos del entorno o de entradas. El proyecto `05_monthly_report`
y sus checkpoints siguen pendientes en [proyectos](../../../projects/README.md).
Material disponible no acredita práctica del estudiante.
Siguiente: [11.04 — Tablas, figuras y referencias](../../../curriculum/11_reporting_quarto/04_tables_figures_references/README.md),
ya disponible.

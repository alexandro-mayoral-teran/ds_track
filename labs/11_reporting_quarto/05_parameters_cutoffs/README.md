# Lab 11.05 — Dos cortes desde el mismo documento

Módulo: 11 — Reportes con Quarto. Tiempo orientativo: 75–100 minutos;
separa preparación del entorno y revisión de evidencia si lo necesitas.

## Entrada y objetivo

Lee la [lección 11.05](../../../curriculum/11_reporting_quarto/05_parameters_cutoffs/README.md).
Elige Python/Jupyter o R/knitr y prepara el entorno con sus requisitos actuales.
Python necesita Papermill para sustituir parámetros; R reutiliza su biblioteca
renv. No hacen falta tus entregas anteriores ni ejecutar ambos lenguajes.

La [muestra propia](../../../curriculum/11_reporting_quarto/05_parameters_cutoffs/cartera.csv)
tiene siete filas: septiembre 001/002/003 con 1000/2000/3000 MXN; octubre
001/002/003/004 con 1200/1800/3300/700 MXN. Una fila es un crédito en un corte.
Las siete claves ID/fecha deben existir una vez; saldos enteros entre 0 y
1000000, sin ausencias. El contrato no inventa una fila de 004 en septiembre.

## Actividad esencial

1. Prepara los archivos con el recorrido completo de la lección. Identifica el
   lugar donde se declaran los valores predeterminados en tu motor y dónde se
   calculan los resultados después de recibirlos. Anota versiones de herramientas.
2. Ejecuta el mínimo completo de tu motor con mínimo 2000 y luego 3000. Debe
   pasar de un saldo seleccionado a ninguno. No cambies los datos ni el código
   del filtro para producir esa variante.
3. Genera los reportes de septiembre y octubre con sus archivos YAML y nombres
   de HTML distintos. Utiliza **el mismo `.qmd` y CSV**. Antes del segundo render,
   predice universo, selección, IDs y proporción. Conserva ambas salidas.
4. Abre los dos HTML y revisa los parámetros visibles, cada fila, las dos barras
   y las notas. Reconstruye conteos/saldos desde la entrada; no compruebes solo
   que el nombre del archivo diga el mes esperado.
5. Crea un **tercer YAML** para octubre con mínimo 4000. Renderiza hacia un nombre
   nuevo y explica la diferencia entre selección vacía y universo vacío. No edites
   manualmente el párrafo o una fila de la tabla para presentar el caso.
6. En otro YAML pide noviembre de 2026. Guarda el error y explica por qué la
   ausencia de ese corte no autoriza a reportar cero créditos. Recupera el caso
   válido con su YAML correcto; no cambies `error: false` para ocultar el fallo.

## Comandos para la variante vacía

Los siguientes bloques presuponen preparación completada y terminal situada
en la **carpeta del documento**. El YAML nuevo contiene directamente:

```yaml
fecha_corte: "2026-10-31"
minimo_mxn: 4000
```

Guárdalo como `octubre_4000.yml`. No añadas un nivel `params:`. Si Quarto requiere
ruta completa, asigna a la variable la ubicación comprobada del programa.

### Python — PowerShell

Antes de entrar en la práctica, desde la raíz de DS Track selecciona el intérprete
del entorno del recorrido. Después cambia de carpeta:

```powershell
$quarto1105 = "quarto"
$env:QUARTO_PYTHON = (Resolve-Path "output/1105_entorno/Scripts/python.exe").Path
Push-Location output/1105_python
& $quarto1105 render reporte_python.qmd --execute-params octubre_4000.yml --output reporte_octubre_4000.html
Pop-Location
```

### Python — Bash/Zsh

Desde la raíz:

```bash
quarto1105="quarto"
export QUARTO_PYTHON="$PWD/output/1105_entorno/bin/python"
raiz1105="$PWD"
cd output/1105_python
"$quarto1105" render reporte_python.qmd --execute-params octubre_4000.yml --output reporte_octubre_4000.html
cd "$raiz1105"
```

### R — proyecto preparado

Abre el proyecto en RStudio o tu IDE y reinicia R. Para estas variantes se usa
la terminal del sistema desde la carpeta del proyecto; es distinta de la consola R.
Guarda `octubre_4000.yml` allí, junto a `reporte_1105.qmd`.

**PowerShell:**

```powershell
$quarto1105 = "quarto"
$env:QUARTO_R = "C:/Program Files/R/R-4.6.1/bin"
& $quarto1105 render reporte_1105.qmd --execute-params octubre_4000.yml --output reporte_1105_octubre_4000.html
```

**Bash/Zsh:**

```bash
quarto1105="quarto"
export QUARTO_R="$(dirname "$(command -v Rscript)")"
"$quarto1105" render reporte_1105.qmd --execute-params octubre_4000.yml --output reporte_1105_octubre_4000.html
```

Usa la ruta real de R y comprueba que `Rscript` sea el elegido en Bash. Si ya
generaste un HTML con ese nombre, conserva la evidencia y utiliza otro nombre
o una práctica nueva antes de repetir: el CLI puede reemplazar salidas.

## Resultado, comprobación y evidencia

Conserva fuente `.qmd`, funciones, CSV, los tres YAML válidos, tres HTML y el
registro del corte no disponible. Anota parámetros usados y resultados esperados,
y explica por qué no es una comparación de población fija entre septiembre
y octubre. Las entradas deben ser las mismas para la serie de reportes.
No incluyas entornos, bibliotecas o cachés en Git.

<details>
<summary>Solución razonada</summary>

Con mínimo 2000, septiembre tiene universo 3/6000 MXN y selección 002/003,
2/5000 MXN. El saldo exactamente en el umbral se incluye. La proporción de
créditos es 2/3, 66.67%, no 5000/6000 ni 2/7.

Octubre tiene universo 4/7000 MXN y selección 003, 1/3300 MXN; proporción
1/4, 25.00%. El crédito 002 ahora tiene 1800 y sale de la selección. El 004
se observa en el universo de octubre y no cumple el mínimo. Las variaciones
mezclan cambios de saldos, de población y del subconjunto que cumple la regla;
no permiten atribuir un efecto a los mismos créditos ni a cobranza.

Con octubre/4000 se conserva universo 4/7000, selección 0/0, proporción 0.00%
e IDs «ninguno». La tabla conserva las cuatro filas con «no» y la barra de
selección tiene altura cero. No se inventa un crédito con saldo cero.
Noviembre falla porque no está disponible; no es una selección vacía válida.

La etiqueta `parameters` en Python define valores iniciales que se sustituyen
antes del siguiente bloque; R utiliza el YAML `params` y su lista. Los cálculos
derivados se hacen después. Un nombre de HTML no sustituye esos mecanismos.

</details>

## Ampliaciones opcionales

- Septiembre con mínimo 2001: solo 003, 1/3000 MXN y 33.33%. Explica el efecto
  de cambiar de una frontera inclusiva a otra sin modificar el operador `>=`.
- Prueba un mínimo escrito como texto `"2000"`, un booleano `true`, un negativo
  o un decimal con parte fraccionaria: deben rechazarse. Un número 2000.0 sí
  representa un entero y se normaliza en esta práctica.
- Escribe `corte` en vez de `fecha_corte` en una copia del YAML. Observa la
  conducta del motor y los parámetros visibles; no asumas que terminar sin error
  demuestra que el nombre equivocado fue utilizado.
- En otra copia repite una clave de octubre e intenta generar septiembre.
  Debe fallar por la validación completa de la fuente, aun fuera del corte elegido.
- Conserva el mismo `.qmd` y genera otra variante con `-P minimo_mxn:2001`.
  Explica qué fecha predeterminada se usa si no se sustituye también la fecha.

## Reflexión, criterio de salida y siguiente paso

Registra evidencia en tu bitácora personal junto a la práctica. Responde: ¿qué es
parámetro y qué es resultado?, ¿por qué el denominador cambia entre reportes?,
¿qué distingue un corte ausente de una selección vacía?, ¿qué archivos y
valores tendría que conocer otra persona para repetir exactamente tu ejecución?

Puedes avanzar cuando las dos variantes conservadas concuerdan con sus parámetros
y universos, y puedes justificar fronteras y límites. `05_monthly_report` y sus
checkpoints siguen pendientes en [proyectos](../../../projects/README.md).
El material disponible no acredita práctica del estudiante.
Siguiente: [11.06 — Proyectos, caché y freeze](../../../curriculum/11_reporting_quarto/06_projects_cache_freeze/README.md),
ya disponible.

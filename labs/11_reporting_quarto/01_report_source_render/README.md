# Lab 11.01 — Preparar una narrativa y reconocer sus archivos

Módulo: 11 — Reportes con Quarto. Tiempo orientativo: 45–60 minutos;
puedes separar la lectura, la preparación y la explicación en sesiones distintas.

## Entrada y objetivo

Lee la [lección 11.01](../../../curriculum/11_reporting_quarto/01_report_source_render/README.md).
Usa su CSV propio de seis registros y **uno** de sus preparadores: Python estándar
o R base. No necesitas Quarto, Jupyter, knitr ni entregas de módulos anteriores.
La actividad consiste en relacionar pregunta, evidencia y texto, y comprobar
qué ocurre cuando cambia una entrada.

Pregunta: ¿cómo cambió el saldo de los mismos tres créditos ficticios entre
2026-09-30 y 2026-10-31? Cada ID 001/002/003 aparece una vez por fecha;
los saldos son pesos enteros entre 0 y 1000000, sin ausencias. La clave es ID/fecha.
La [entrada completa](../../../curriculum/11_reporting_quarto/01_report_source_render/cartera.csv)
contiene septiembre 1000/2000/3000 y octubre 1200/1800/3300 para esos IDs.

## Actividad esencial

1. Elige el recorrido Python o R de la lección. Genera una preparación en una
   carpeta nueva y abre los cuatro archivos. Explica quién necesita la respuesta
   y qué decisión todavía no permiten tomar estos datos.
2. Revisa `pares.csv`, `resumen.csv` y `borrador.md`. Reconstruye la diferencia
   total desde los tres cambios individuales. Identifica el denominador de la tasa.
3. Crea una copia de la entrada en `output/1101_cambio.csv` y cambia **solo** el
   saldo de 003/2026-10-31: de 3300 a 3600. No cambies el CSV del curriculum.
   Puedes hacerlo con el editor de texto conservando ceros iniciales y encabezado.
4. Antes de ejecutar nada, abre el borrador anterior. Registra qué cifra conserva
   y predice cuál debería aparecer tras recalcular. Genera otra carpeta usando
   la copia; comprueba pares, resumen y texto, no solo el mensaje de éxito.
5. Clasifica `cartera.csv`, `preparar.py`/`preparar.R`, `borrador.md`, un futuro
   `reporte.qmd` y su `reporte.html`: entrada, código, preparación, fuente y salida.
   Indica qué necesitarías conservar para reconstruir y qué abriría quien recibe
   el reporte. Los dos últimos archivos son hipotéticos: aquí no se crean.
6. Propón una mejora de redacción para el público elegido. En tus notas identifica
   las cifras mediante sus campos de origen, por ejemplo «saldo de octubre de
   resumen.csv»; no mantengas otro total escrito a mano como fuente de verdad.
   Si editas el texto del preparador, conserva la inserción desde variables y
   genera una tercera carpeta. No se exige aprender la sintaxis `.qmd` todavía.

### Repetir con la copia — Python

Con el entorno ya activado, desde la raíz del repositorio, en **PowerShell**:

```powershell
python curriculum/11_reporting_quarto/01_report_source_render/preparar.py output/1101_cambio_python --fuente output/1101_cambio.csv
```

En **Bash/Zsh**, desde la raíz y con el entorno ya activado:

```bash
python curriculum/11_reporting_quarto/01_report_source_render/preparar.py output/1101_cambio_python --fuente output/1101_cambio.csv
```

### Repetir con la copia — R

En RStudio o tu IDE, usa un script y una sesión nueva, con la raíz como directorio
de trabajo. Ejecuta en R, no en la terminal del sistema:

```r
source("curriculum/11_reporting_quarto/01_report_source_render/preparar.R", encoding = "UTF-8")
r <- preparar_reporte("output/1101_cambio.csv", "output/1101_cambio_r")
print(r$resumen)
print(r$pares)
stopifnot(identical(as.numeric(r$resumen$saldo_mxn), c(6000, 6600)),
          identical(r$porcentaje, "10.00%"))
```

## Resultado y comprobación

Entrega las dos preparaciones conservadas, la copia modificada y unas notas
breves con pregunta/público, clasificación, explicación del cambio y límites.
No hay HTML requerido. Comprueba que la primera `fuente.csv` conserva 3300,
la segunda contiene 3600 y el CSV original del curriculum permanece intacto.
La primera narrativa debe continuar describiendo su propia copia, no fingir
que se actualizó por abrirla de nuevo.

<details>
<summary>Solución razonada y cifras esperadas</summary>

La primera preparación tiene tres créditos por corte, 6000 y 6300 MXN. Los
cambios +200, -200 y +300 suman +300; `300 / 6000 × 100 = 5%`. Es correcto
decir que el saldo agregado aumentó. No es correcto decir que todos aumentaron
o que la causa fue una caída de la cobranza.

En la copia, octubre suma 6600, diferencia +600 y variación 10% sobre septiembre.
El par 003 cambia de +300 a +600; los otros pares y septiembre no cambian.
Los preparadores insertan esos resultados en tabla y texto. Abrir el Markdown
anterior solo lee un archivo ya guardado: no conoce el cambio en otra entrada.

El CSV es fuente de datos; el script contiene cálculos y la preparación editorial;
el Markdown generado es un borrador. Posteriormente el `.qmd` será el documento
fuente Quarto y el HTML la salida renderizada. Para reconstruir cálculos hace
falta conservar datos, código, fuente del documento, configuración y dependencias
necesarias. Quien recibe una entrega HTML necesita también sus recursos si los
hay; comprobar esa distribución se desarrollará después.

Una mejora posible es abrir con el hallazgo y sus fechas, dejando el detalle de
validación en método. Conserva la referencia a muestra ficticia y base común.
La calidad de esta redacción requiere revisión humana; cifras iguales no la certifican.

</details>

## Ampliaciones que no bloquean avanzar

- En otra copia pon todos los saldos de septiembre en cero. Octubre sigue en
  6300 y la diferencia es 6300; la tasa debe quedar no definida, nunca 0%.
- En una copia distinta elimina una fila o repite una clave. El preparador debe
  rechazar antes de crear el destino; no convierte una ausencia en cero.
- Si ejecutas el otro lenguaje, compara cada par y grupo por clave. No se exige
  que los archivos tengan idénticos bytes ni que los textos mencionen el mismo lenguaje.

## Evidencia, reflexión y siguiente paso

En tu bitácora personal junto a la práctica registra enlaces a tus archivos locales,
lenguaje elegido y qué comprobaste. Responde: ¿qué puede quedar desactualizado
aunque el archivo se vea bien?, ¿qué significa «fuente» en cada caso?, ¿qué
afirmación no permiten sostener estos datos?

Puedes avanzar cuando otra persona localice la evidencia de cada cifra, entienda
la comparación y distinga leer una salida de regenerarla. El proyecto
`05_monthly_report` y sus checkpoints siguen pendientes en
[proyectos](../../../projects/README.md).
Siguiente: [11.02 — Primer documento Quarto](../../../curriculum/11_reporting_quarto/02_first_document/README.md),
ya disponible; el material de esta práctica no acredita haberla completado.

# 08.08 — Exportación reproducible

## Propósito, prerrequisitos y objetivos

**Esencial.** Producir un archivo legible desde código y poder reconstruirlo
desde una sesión nueva. Guardar una captura del panel Plots no conserva las
decisiones necesarias para repetir la figura: objeto, datos, tamaño y formato.

Completa [08.06 — Etiquetas, temas y accesibilidad](../06_labels_themes_accessibility/README.md)
y [08.07 — Componer figuras](../07_compose_figures/README.md). Retoma la
[entrega comprobada de 07.10](../../07_tidyverse/10_first_plot_closure/README.md).
Usa el mismo proyecto renv en RStudio o tu IDE; referencias: R 4.6.1 y ggplot2
4.0.3. No hay dependencias nuevas, preparador ni cambios de lockfile.

Al terminar podrás:

- Elegir un formato según el destino de lectura.
- Distinguir tamaño físico, número de píxeles y resolución.
- Guardar un objeto explícito con `ggsave`, sin depender del último gráfico.
- Conservar tabla fuente, configuración, descripción y diagnóstico de sesión.
- Separar comprobación de valores e integridad de la revisión de legibilidad.
- Reconstruir y comprobar la entrega desde una sesión nueva.

**Recorrido esencial:** PNG, tablas, configuración y comprobación. **Ampliación:**
SVG/PDF y doble resolución. No se exige publicación, Quarto, impresión profesional
ni que todos los equipos generen archivos idénticos byte por byte.

## 1. Empezar por el lugar donde se leerá

Antes de guardar, decide dónde se insertará la figura y cuánto espacio tendrá.
Una imagen amplia que se reduce a una columna estrecha también reduce sus letras.
Un título correcto en Plots puede quedar cortado o ilegible en el documento final.

| Destino | Formato posible | Qué revisar |
| --- | --- | --- |
| Imagen para un documento o pantalla | PNG | Píxeles suficientes para el tamaño de uso, letras y fondo |
| Página web o edición vectorial compatible | SVG | Compatibilidad del visor y de las formas/textos |
| Documento o impresión | PDF | Tamaño de página, fuentes y lectura al tamaño previsto |

PNG guarda una cuadrícula de píxeles. SVG y PDF pueden guardar trazos vectoriales
que mantienen contornos nítidos al ampliar. Eso no significa que toda imagen
dentro de un SVG/PDF sea vectorial: una capa rasterizada sigue teniendo píxeles.
Tampoco garantiza texto seleccionable o accesibilidad; algunos dispositivos
convierten letras a trazos, y las fuentes pueden variar entre equipos.

Para la práctica basta un PNG. Incluimos SVG/PDF como alternativas verificadas,
no como formatos obligatorios adicionales ni como motivo para instalar paquetes.

## 2. Tres medidas que conviene separar

El tamaño físico se expresa aquí en pulgadas (`units = "in"`). Una pulgada
equivale a 2.54 cm. La resolución indica cuántos píxeles corresponden a cada
pulgada al producir la imagen rasterizada; `ggsave` usa el argumento `dpi`.

**Píxeles de ancho = pulgadas de ancho × dpi**, y lo mismo para el alto.

| Configuración PNG | Ancho × alto en píxeles | Qué cambia |
| --- | --- | --- |
| 9 × 6 pulgadas, 144 dpi | 1296 × 864 | Referencia de esta práctica |
| 9 × 6 pulgadas, 288 dpi | 2592 × 1728 | Doble en cada dimensión; cuatro veces tantos píxeles |
| 6 × 4 pulgadas, 144 dpi | 864 × 576 | Menos espacio físico para distribuir texto y paneles |

Duplicar dpi no crea más espacio físico para títulos y notas. Manteniendo el
tamaño en pulgadas, el texto conserva su tamaño en puntos y se dibuja con más
píxeles. El tamaño del archivo puede aumentar, pero no necesariamente por un
factor exacto, porque PNG aplica compresión.

Cambiar de 9 × 6 a 6 × 4 pulgadas reduce el lienzo. Los tamaños de letra definidos
en el tema no se reducen automáticamente en la misma proporción; puede aparecer
solapamiento. Para resolverlo, ajusta disposición, texto o tamaño de destino y
vuelve a revisar. Subir dpi no arregla ese problema de espacio.

En una página web, el tamaño mostrado también depende de su configuración de
presentación. Un archivo de 1296 píxeles puede mostrarse con otros anchos; no
deduzcas su tamaño físico solo por cómo lo presenta el visor. En SVG/PDF, dpi no
controla la nitidez de los trazos vectoriales como lo hace con un PNG.

## 3. Elegir el objeto que se guarda

`ggsave` puede tomar por defecto el último gráfico mostrado y las dimensiones
del dispositivo actual. Esos valores dependen de lo que hiciste antes en la
sesión. Especificamos `plot`, tamaño, unidad, dispositivo y fondo.

Esta es la función breve utilizada en el [script de referencia](exportar_figuras.R).
Puedes leerla y definirla en Console de R; definir una función todavía no guarda
un archivo. Retoma [funciones en R](../../06_r_foundations/06_functions_control/README.md)
si necesitas repasar argumentos y valores por defecto.

```r
guardar_png_visual <- function(figura, ruta, ancho = 9, alto = 6, dpi = 144) {
  if (file.exists(ruta)) { stop("El archivo ya existe; elige otro nombre.") }
  ggplot2::ggsave(ruta, plot = figura, device = grDevices::png,
    width = ancho, height = alto, units = "in", dpi = dpi,
    bg = "white", limitsize = TRUE)
}
```

| Argumento | Decisión que hace explícita |
| --- | --- |
| `ruta` | Nombre y carpeta del archivo; la carpeta debe existir |
| `plot = figura` | Objeto que se guarda, aunque después hayas mostrado otro |
| `device = grDevices::png` | Dispositivo PNG incluido en R |
| `width`, `height`, `units` | Lienzo de 9 × 6 pulgadas en esta configuración |
| `dpi` | Resolución del PNG |
| `bg = "white"` | Fondo blanco, sin depender del fondo del visor |
| `limitsize = TRUE` | Conserva la comprobación de tamaño de ggplot2 |

El guardado de un archivo existente puede reemplazarlo en `ggsave`. El pequeño
control anterior lo impide; la entrega completa también exige una **carpeta
nueva**. Si cambias solo la extensión de un PNG a `.pdf`, no conviertes el
contenido: el dispositivo debe generar el formato correcto.

Usamos `grDevices::png` explícitamente, sin depender de qué dispositivo adicional
encuentre ggplot2. En la ampliación se usan `grDevices::svg` y
`grDevices::cairo_pdf`, también incluidos en R. El guardado de una composición
patchwork acepta igualmente un objeto explícito; aquí retomamos una figura
simple para concentrarnos en la exportación y sus comprobaciones.

## 4. Preparar y exportar desde el IDE

Abre el mismo proyecto de práctica, guarda tu trabajo y reinicia R. Desde el
editor abre [exportar_figuras.R](exportar_figuras.R) y guarda una copia propia
como `output/mi_exportacion.R`, con otro nombre si ya existe. Mantén la raíz
de la práctica como directorio de trabajo. Ejecuta en **Console de R**, no en
Terminal; no hace falta Rscript para esta actividad.

```r
source("output/mi_exportacion.R", encoding = "UTF-8")
preparado <- preparar_visual()
print(preparado$cierre$datos_figura)
print(preparado$figura)
exportar_visual("output/exportacion_0808")
```

El script carga las funciones de 07.10 y define las nuevas; no guarda nada al
cargarlo. `preparar_visual` reconstruye la fuente original, sus reglas y los
14 pares. `exportar_visual` vuelve a reconstruirlos antes de escribir: no toma
los datos de un objeto modificado en la sesión.

Se conserva la misma pregunta: los mismos 14 IDs aceptados entre septiembre
y octubre de 2026, 29000/31800 MXN y cobertura 14/18 por fecha. Los ocho aceptados
sin pareja y los rechazos permanecen en el análisis reconstruido; esta entrega
visual conserva el resumen y los pares. No reemplaza la entrega completa de
07.10 ni presenta todos los aceptados como si fueran la base común.

Las advertencias sobre fechas imposibles proceden de la fuente de práctica.
Revisa sus motivos en el análisis; no las ocultes para dar apariencia de éxito.

### Qué se conserva

| Archivo | Para qué sirve |
| --- | --- |
| `saldo_comun.png` | Figura para revisar e insertar |
| `datos_figura.csv` | Dos filas resumidas que alimentan las barras |
| `base_comun.csv` | Los 14 IDs y sus dos saldos, con diferencias |
| `configuracion.csv` | Pulgadas, dpi, ampliación vectorial y huella de la fuente |
| `descripcion.txt` | Lectura textual del hallazgo, población y límites |
| `sesion.txt` | Diagnóstico de R, plataforma y paquetes cargados |
| `manifiesto.csv` | Nombres y huellas MD5 de los seis archivos anteriores |

Una **huella** resume los bytes de un archivo. Sirve aquí para detectar cambios
accidentales respecto a la entrega creada; no demuestra que los datos sean
correctos ni es una garantía frente a alguien que edite también el manifiesto.
Por eso el verificador reconstruye las tablas desde la fuente además de comparar
huellas. El manifiesto no se incluye a sí mismo.

`sesion.txt` ayuda a diagnosticar diferencias, pero no sustituye a `renv.lock`.
Conserva tu script y el proyecto renv existente junto con esta evidencia. Revisa
el diagnóstico antes de compartirlo: puede contener rutas locales de la sesión.
No se versionan las salidas personales de práctica en el repositorio del curso.

![PNG de referencia: 1296 por 864 píxeles](assets/saldo_exportado.png)

Sin imagen: dos barras desde cero muestran 29000 y 31800 MXN. Se indican fechas,
unidad, base común de 14 IDs y cobertura 14/18. La nota limita la interpretación
a una comparación descriptiva de datos sintéticos.

## 5. Comprobar el archivo que realmente se usará

La función termina llamando a `verificar_exportacion`. Puedes repetir la
comprobación sin escribir archivos:

```r
verificar_exportacion("output/exportacion_0808")
```

Debes obtener `ancho_px = 1296` y `alto_px = 864`. El verificador:

1. Lee y valida la configuración y la huella del CSV original.
2. Comprueba nombres y huellas de los archivos esperados.
3. Reconstruye desde la fuente y compara todas las columnas de resumen y pares.
4. Contrasta la descripción textual con la población reconstruida.
5. Lee la cabecera PNG y comprueba sus dimensiones en píxeles.

No decodifica el dibujo del PNG ni comprueba que cada píxel corresponda a las
tablas. En los vectoriales comprueba presencia y marca de formato, además de
huellas; no certifica fuentes, accesibilidad o apariencia. Esas comprobaciones
automáticas se complementan con **abrir el archivo final**.

Desde Files del IDE o tu explorador de archivos abre `output/exportacion_0808/saldo_comun.png`.
Después insértalo al tamaño previsto en tu documento o visor de destino:

- Comprueba título, cortes, etiquetas y nota completos, sin recortes.
- Lee ejes y unidades sin ampliar continuamente el visor.
- Verifica base común, cobertura y que las barras parten de cero.
- Comprueba que la nota y la descripción textual acompañen la figura.

Una huella correcta puede corresponder a una imagen mal diseñada. Una imagen
bonita puede representar datos equivocados. Necesitamos revisar ambas cosas.

## 6. Reconstruir sin estado oculto

Guarda tu script y reinicia R. En una sesión nueva, desde la misma raíz:

```r
source("output/mi_exportacion.R", encoding = "UTF-8")
verificar_exportacion("output/exportacion_0808")
exportar_visual("output/exportacion_0808_reconstruida")
```

Compara los dos `datos_figura.csv` y `base_comun.csv`, su configuración y las
dimensiones del PNG. Deben coincidir. No se exige que el diagnóstico de sesión,
metadatos del PDF o todas las huellas coincidan entre ejecuciones o plataformas.
Una fuente o un dispositivo diferente puede cambiar la apariencia sin cambiar
los saldos; aun así requiere revisión. La reproducibilidad de los indicadores
no elimina la necesidad de conservar configuración y entorno.

Si un destino ya existe, se rechaza sin reemplazarlo. Si falta la carpeta madre,
se pide una ruta válida. Si una escritura falla, puede quedar una entrega parcial:
inspecciónala y usa otro nombre después de resolver la causa. No cambies las
huellas para hacer pasar una entrega que no has reconstruido.

## 7. Ampliaciones: resolución y vectoriales

Estas actividades no bloquean el cierre esencial. Para duplicar la resolución
sin cambiar el tamaño físico:

```r
exportar_visual("output/exportacion_0808_doble_dpi", dpi = 288)
```

El PNG mide 2592 × 1728 píxeles. Comprueba que los datos y las pulgadas sean
iguales; mira ambos archivos al mismo tamaño de uso. La función admite tamaños
positivos menores de 50 pulgadas y un límite didáctico de 600 dpi; conserva
`limitsize`, sin desactivarlo para ocultar una confusión entre píxeles y pulgadas.

Para conservar además SVG y PDF, primero consulta la capacidad de tu R:

```r
capabilities("cairo")
if (isTRUE(capabilities("cairo"))) {
  exportar_visual("output/exportacion_0808_vectoriales", vectoriales = TRUE)
}
```

Si Cairo no está disponible, conserva el PNG esencial; no es necesario cambiar
tu instalación para avanzar. La función comprueba esa capacidad antes de crear
la carpeta cuando pides vectoriales. Usa los dispositivos completos, no solo
`device = "svg"`, para no introducir la dependencia adicional svglite.

Abre SVG/PDF en un visor compatible. Verifica ancho, alto, acentos, cifras y notas,
y amplía los trazos. En esta configuración el PDF tiene una página de 9 × 6
pulgadas, equivalentes a 648 × 432 puntos PDF, con 72 puntos por pulgada. Revisa
el resultado en el programa donde lo utilizarás; convertir el texto a trazos
o variar las fuentes puede cambiar su selección y presentación.

## Errores habituales, práctica y criterio de salida

| Síntoma | Qué revisar |
| --- | --- |
| Se guardó otro gráfico | Pasar `plot = figura` en lugar de depender del último mostrado |
| Archivo enorme o error de tamaño | Confirmar `units`, ancho/alto y dpi antes de cambiar límites |
| Más dpi, pero título sigue recortado | Ajustar espacio físico, disposición o texto |
| Archivo con extensión engañosa | Generar el formato con el dispositivo correspondiente |
| PNG correcto en Plots, ilegible en documento | Revisar el archivo exportado al tamaño final |
| El verificador detecta cambios | Revisar fuente/archivos y reconstruir en otro destino |

Realiza el [lab 08.08](../../../labs/08_visualization_r/08_reproducible_export/README.md).
Puedes avanzar cuando expliques tu elección de formato, predigas los píxeles,
reconstruyas desde una sesión nueva y compruebes datos y lectura final.
Conserva evidencia propia; material disponible no equivale a práctica completada.

Siguiente: [08.09 — Cierre visual y comparación con Python](../09_visual_comparison/README.md).
Volver al [índice de 08](../README.md). El proyecto y los checkpoints integradores
siguen pendientes; no se acreditan por exportar esta figura.

## Referencias primarias

- [ggsave: objeto, dispositivos, dimensiones y resolución](https://ggplot2.tidyverse.org/reference/ggsave.html).
- [R: dispositivos PNG](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/png.html).
- [R: dispositivos SVG y PDF basados en Cairo](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/cairo.html).
- [R: dispositivo PDF y unidades](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/pdf.html).
- [R: huellas con tools::md5sum](https://stat.ethz.ch/R-manual/R-devel/library/tools/html/md5sum.html).

Las páginas de R-devel pueden describir otra versión. APIs y exportaciones
contrastadas con R 4.6.1 y ggplot2 4.0.3; ejemplos propios del track.

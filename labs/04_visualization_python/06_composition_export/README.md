# Lab 04.06 — Composición y exportación

## Propósito, entradas y preparación

Lee la [lección 04.06](../../../curriculum/04_visualization_python/06_composition_export/README.md)
y completa 04.05 con sus prerrequisitos. Prepararás una figura que otra persona
pueda leer, comprobar y abrir fuera de tu sesión.

**Entradas:** composition.py y los CSV sintéticos de SQL. **Resultado:** una
composición con medidas comprobadas, exportaciones PNG/SVG, tablas y comentario
de lectura. Conserva las fuentes, SQLite y las entregas anteriores.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D. E es ampliación.
Puedes detenerte después de una actividad y registrar preguntas. Usa el entorno
elegido y el recorrido de tu shell indicado en la lección. Desde la raíz ejecuta
composition.py con `--cut 2026-10-31 --dpi 160` y una carpeta nueva
`curriculum/04_visualization_python/06_composition_export/output/lab_06`.

Recibes corte.csv, resumen.csv, comparacion.csv, formatos.csv, lectura.md,
entrega_160.png, entrega_320.png, entrega.svg y comparacion.png. No se requiere
un notebook, una presentación ni una aplicación.

## A. Explicar qué relación tienen los paneles

Abre comparacion.png y comparacion.csv. Antes de mirar la solución:

1. Escribe una pregunta para cada panel y nombra la medida, unidad y fecha.
2. Coteja las medianas y sus coberturas con los saldos originales: no te bases
   únicamente en la longitud de las barras.
3. Verifica el mismo orden de segmentos y rango horizontal en ambos paneles.
4. Explica qué podría confundirse si cada panel se ordenara por su valor o
   usara un máximo diferente.
5. Explica por qué educación no debe tener una barra de cero en octubre.
6. Redacta una frase de comparación que no afirme movimientos individuales.

**Resultado:** ficha de comparación y valores comprobados. **Comprobación:**
los dos paneles muestran medianas conocidas en MXN con rango 0–5000. Conservan
5/5, 8/10, 2/3, 6/6 en septiembre y 5/5, 10/10, 0/3, 6/6 en octubre.

<details>
<summary>Ver solución razonada de A</summary>

Preguntas: «¿Cuál era la mediana del saldo conocido por segmento al 30 de
septiembre?» y «¿Cuál es al 31 de octubre?». La unidad es MXN, no porcentaje
ni suma. Medianas: comercio 2900/3100, consumo 1500/1750, educación 3250/sin
mediana y servicios 2350/2550. El mismo orden alinea categorías y los límites
comunes permiten comparar longitudes desde cero. Con máximos distintos una
barra igual podría significar valores distintos. Educación tiene tres registros
sin saldo conocido: no una mediana de cero. Una frase válida: «La mediana
conocida de consumo es 1750 en octubre y 1500 en septiembre; sus bases conocidas
son 10/10 y 8/10, por lo que no describe necesariamente el cambio de los mismos créditos».

</details>

## B. Conservar unidades y comprobar la anotación

Abre entrega_160.png y resumen.csv.

1. Nombra qué comparten los paneles A y B y qué no deben compartir.
2. Calcula cobertura de cada grupo y global a partir de conteos. ¿Por qué
   el promedio simple de los cuatro porcentajes no da la cobertura global?
3. Describe qué dato señala la flecha y qué parte es solo posición de texto.
4. Distingue saldo cero, ningún saldo conocido y ningún registro.
5. Explica si colocar ambos paneles lado a lado demuestra una relación causal.

**Resultado:** cálculos, lectura de la flecha y tres casos bien distinguidos.
**Comprobación:** 21/24 = 87,5 % global; educación tiene cobertura 0 % y mediana
ausente. No cambiar `sharey=True` a `sharex=True` para emparejar MXN con porcentaje.

<details>
<summary>Ver solución razonada de B</summary>

Se comparten categorías verticales; x mide MXN en A y porcentaje en B. Comercio,
consumo y servicios tienen 100 %; educación, 0 %. El promedio sin ponderación
es 75 %, que da igual peso a cada grupo. La cobertura global usa 21 conocidos
entre 24 registros y da 87,5 %. La flecha señala (0, 2): cobertura cero de
educación. El texto se desplaza en puntos tipográficos; no cambia el porcentaje.
El crédito 004 tiene saldo cero válido, educación tiene registros sin saldos
conocidos y una fecha fuera de la fuente no tiene registros. Estas situaciones
requieren mensajes distintos. La composición explica medida y cobertura, no causa.

</details>

## C. Preparar una versión propia legible

Copia composition.py como `composition_lab.py` **en la misma carpeta que el
original**, para que conserve la reutilización del lector de 04.04. No cambies
las fuentes ni el script original. En tu copia:

1. Escribe un título general propio que incluya medida, fecha y origen sintético.
2. Revisa la nota común. Si la acortas, conserva fuente, base y límite en la
   figura o en una nota de lectura que entregarás junto a ella.
3. En `delivery_figure`, mueve la explicación de educación cambiando `xytext`
   y deja `xy` intacto. Evita tapar el punto, 0/3 o el nombre del segmento.
4. Conserva trama de barras, formas, unidades y datos. No reduzcas la letra
   para meter un párrafo completo dentro del panel.
5. Ejecuta tu copia hacia otra carpeta nueva y revisa el PNG en el tamaño
   en que lo compartirías. Pide a quien te acompaña que explique la figura
   con tus tablas y texto, sin recibir instrucciones orales adicionales.

**Resultado:** código propio, PNG, tablas y nota de cambios. **Comprobación:**
las medianas, porcentajes y flecha al dato deben seguir coincidiendo con B.
No basta con que Python termine sin error.

<details>
<summary>Ver solución razonada de C</summary>

Un título posible: «Octubre de 2026: mediana conocida y cobertura · muestra
sintética». Una nota posible: «Fuente: SQL 03.01; 21/24 saldos conocidos. La
mediana describe los valores disponibles». El resto de los límites se conserva
en lectura.md. Puedes probar `xytext=(35, -48)` en la anotación de educación,
manteniendo `xy=(0, GROUPS.index("educacion"))`. No existe un desplazamiento
universal: revisa la imagen. Comprueba que no haya recortes, superposiciones
ni inferencias nuevas. Escribe por qué moviste el texto y qué permaneció intacto.

</details>

## D. Comparar archivos y elegir qué compartir

Abre los dos PNG y el SVG en un visor compatible. Consulta formatos.csv y las
dimensiones del PNG mediante propiedades o información del visor.

1. Calcula dimensiones esperadas para 12 × 5,5 pulgadas a 160 y 320 dpi.
2. Calcula la razón del número de píxeles. Compara después bytes reales;
   explica por qué no necesitas encontrar la misma razón en los archivos.
3. Muestra los PNG con el mismo ancho de lectura, y luego amplíalos. Describe
   qué cambió en el dibujo y qué no cambió en los datos.
4. Amplía el SVG y revisa flecha, texto, tramas y colores. No lo renombres
   como PNG para insertarlo en un destino que no lo admita.
5. Elige un formato para compartir con quien te acompaña, considerando su
   visor. Incluye CSV y lectura textual; explica la elección.

**Resultado:** comparación de formatos y entrega elegida. **Comprobación:**
1920 × 880 y 3840 × 1760 píxeles; 4 veces el número total de píxeles. Los
valores analíticos son iguales en todas las versiones.

<details>
<summary>Ver solución razonada de D</summary>

12 × 160 = 1920 y 5,5 × 160 = 880; a 320 resultan 3840 y 1760. Cada
dimensión se duplica, por lo que el área en píxeles se cuadruplica. Los bytes
dependen también de compresión y contenido. A igual ancho de presentación,
320 dpi ofrece más detalle raster, no textos proporcionalmente más grandes
ni saldos más precisos. SVG conserva trazados escalables de esta figura;
no implica interactividad ni datos accesibles por sí solos. PNG es una elección
razonable para un visor compatible solo con imágenes raster; SVG si el destino
lo admite y interesa ampliar. Ambas elecciones requieren revisar la entrega real.

</details>

## E. Ampliaciones: composición estrecha y selección vacía

Elige una o ambas, sin bloquear el cierre principal:

- Para un destino estrecho, prueba dos paneles apilados en otra copia del código:
  usa `plt.subplots(2, 1, figsize=(8, 9), layout="constrained")` en
  `delivery_figure`. Establece explícitamente los segmentos y su orden también
  en el panel de cobertura con `set_yticks` y `set_ylim`, pues ya no comparte y.
  Revisa y acorta el título y la nota común; compara legibilidad al ancho final.
- Ejecuta el original con `--cut 2026-11-30` y otra carpeta nueva. Coteja los
  mensajes y los CSV. No interpretes 0/0 como cobertura 0 %. Recuerda que
  comparacion.png sigue usando las fechas originales de las fuentes.

<details>
<summary>Ver solución razonada de E</summary>

Apilar paneles da más ancho útil a cada uno, pero exige revisar altura, nombres,
notas y recorrido de lectura. En el panel B, puedes usar
`axes[1].set_yticks(range(len(GROUPS)), GROUPS)` y
`axes[1].set_ylim(len(GROUPS) - .6, -.6)`. No compartir x: las unidades siguen
siendo distintas. SIZE permanece como tamaño de comparación; cambia también
el tamaño predeterminado de delivery_figure si quieres que export lo utilice.
Para noviembre hay cero registros: medianas y porcentajes están ausentes, no
son ceros observados. Las tablas conservan las categorías y los mensajes lo explican.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código propio, tablas, PNG o SVG revisado, registro de tamaños y
comentario de lectura. Escribe fuente, fecha, unidad, base conocida y límites;
registra evidencia y preguntas en PROGRESS.md. La disponibilidad de esta sección
no acredita que hayas terminado su práctica.

Reflexiona: ¿por qué ver juntas esas dos vistas ayuda? ¿Cuándo sería incorrecto
compartir un eje? ¿Qué error no arregla aumentar dpi? ¿Qué necesita alguien
que recibe solo el archivo de imagen? ¿Cómo comprobarías que exportaste la
Figure correcta si tu sesión tuviera varias abiertas?

No hay checkpoint de proyecto implementado. Continúa con el
[plan de 04.07 — Altair: visualización declarativa](../../../curriculum/04_visualization_python/README.md#07-altair-visualizacion-declarativa),
todavía pendiente de desarrollo.

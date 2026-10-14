# Lab 04.07 — Altair: visualización declarativa

## Propósito, entradas y preparación

Lee la [lección 04.07](../../../curriculum/04_visualization_python/07_altair_declarative/README.md)
y completa 04.06 con sus prerrequisitos. Vas a expresar un análisis conocido
mediante datos, marcas y canales, y comprobar que cambiar de herramienta
conserva la pregunta, población y medida.

**Entradas:** declarative.py, los CSV sintéticos de SQL 03.01 y la tabla de
medianas de 04.06. **Resultado:** cuatro vistas HTML con sus JSON y tablas,
una variación propia y una explicación de datos, tipos y ausencias.
Conserva fuentes, scripts originales, SQLite y entregas previas.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D. E es ampliación.
Usa el gestor y el recorrido completo de tu shell en la lección. Desde la raíz,
ejecuta declarative.py con `--cut 2026-10-31` y una carpeta nueva
`curriculum/04_visualization_python/07_altair_declarative/output/lab_07`.
Abre los HTML con conexión en un navegador compatible. Si eliges `--bundle`,
prepara antes chart-export y usa otra carpeta; PNG/SVG y apertura sin conexión
son opcionales. No necesitas notebook ni escribir JavaScript.

## A. Leer una especificación antes de cambiarla

Abre tramos.html y tramos.json con un editor de texto. Consulta tramos.csv.

1. Identifica los datos de entrada, la marca de barras y la capa de etiquetas.
2. Localiza en `encoding` qué campos reciben x e y, sus tipos y el orden.
3. Explica qué representa una fila de tramos.csv y qué representa una barra.
4. Justifica O para tramo_atraso y Q para creditos. ¿Las distancias entre
   categorías representan intervalos iguales de días?
5. Busca los datos incorporados en `datasets`. No necesitas interpretar cada
   opción del archivo para comprobar campos, tipos y valores.
6. Clasifica segmento, id_credito, saldo_mxn y fecha_corte usando N/O/Q/T.

**Resultado:** ficha de campos y canales. **Comprobación:** tres categorías en
orden Sin atraso → 1–29 días → 30 días o más; conteos 4, 8 y 9.

<details>
<summary>Ver solución razonada de A</summary>

Una fila resume créditos con atraso conocido de un tramo en octubre. La capa
de barras usa x = tramo_atraso, ordinal; y = creditos, cuantitativo. La capa
de texto muestra ese conteo sin volver a calcularlo. Los tres tramos tienen
orden, pero no igual anchura temporal: el último no tiene límite superior.
Las barras no forman un histograma de intervalos iguales.

segmento e id_credito son nominales: distinguir el crédito 004 del 005 no
convierte su diferencia en una medida. saldo_mxn es cuantitativo y fecha_corte
es temporal una vez validada. `datasets` conserva filas; las referencias por
nombre dentro de `data` indican cuál utiliza cada vista. Validar el esquema
no comprueba por sí solo que esos conteos sean correctos.

</details>

## B. Conciliar la vista con el análisis anterior

Abre medianas.html, resumen.csv y lectura.md. Revisa los saldos de octubre
en los CSV originales y los resultados de 04.06.

1. Calcula la mediana de los saldos conocidos de cada segmento. Incluye el
   saldo cero válido; no reemplaces ausencias por cero.
2. Comprueba registros, conocidos y cobertura de cada segmento y del corte.
3. Explica por qué educación tiene mensaje sin mediana y cobertura cero.
4. Identifica `layer`, `hconcat` y la resolución de escalas en medianas.json.
   ¿Qué comparten las vistas y qué unidades deben permanecer separadas?
5. Localiza el campo mediana_mxn y comprueba que no solicita una agregación.
6. Describe qué cambió visualmente frente a Matplotlib y qué cifras conservó.

**Resultado:** tabla conciliada y comentario de comparación. **Comprobación:**
24 registros y 21 saldos conocidos; cobertura global 21/24 = 87,5 %.

<details>
<summary>Ver solución razonada de B</summary>

| Segmento | Mediana conocida (MXN) | Conocidos/registros | Cobertura |
| --- | ---: | ---: | ---: |
| comercio | 3100 | 5/5 | 100 % |
| consumo | 1750 | 10/10 | 100 % |
| educacion | Sin mediana | 0/3 | 0 % |
| servicios | 2550 | 6/6 | 100 % |

Educación tiene tres registros, ningún saldo conocido y ninguna mediana
calculable. No tiene mediana cero. El crédito 004 sí conserva saldo cero y
participa en la mediana de consumo. El promedio simple de coberturas es 75 %,
pero no usa la base de 24 registros; la cobertura global es 87,5 %.

`layer` superpone barras y textos; `hconcat` coloca mediana y cobertura lado
a lado. Se comparten categorías verticales y se conservan escalas x
independientes para MXN y porcentaje. La tabla ya tiene una fila por segmento:
`mediana_mxn:Q` representa el valor preparado. Los motores pueden variar
tipografía o marcas; no deben cambiar la mediana ni su denominador.

</details>

## C. Comprobar detalle, categorías y fechas

Consulta pares.csv, excluidos_pares.csv, tramos.csv, excluidos_atraso.csv y
comparacion.csv junto a sus figuras.

1. Concilia pares aceptados y exclusiones con los 24 registros del corte.
   Busca el crédito 004 y coteja sus coordenadas con la fila original.
2. Comprueba los motivos de las cinco exclusiones. ¿Sería correcto filtrar
   saldos y atrasos por separado y unirlos después por posición?
3. Cuenta atrasos originales: cero; entre 1 y 29; desde 30. Aparta ausentes
   y explica dónde entrarían los valores 1, 29 y 30.
4. Compara fechas y medianas entre comparacion.csv y fechas.html. ¿Por qué
   hay ocho grupos en la tabla y siete puntos?
5. Explica qué aportan color y forma, y por qué una categoría en la leyenda
   no demuestra que tenga puntos. Redacta una lectura sin afirmar causalidad.

**Resultado:** conciliación de pares/tramos y lectura temporal con límites.
**Comprobación:** 19 pares + 5 exclusiones = 24; 4 + 8 + 9 atrasos conocidos
+ 3 ausentes = 24. El crédito 004 está en (0 MXN, 40 días).

<details>
<summary>Ver solución razonada de C</summary>

Un par conserva saldo y atraso de la misma fila crédito/corte. Filtrar cada
columna por separado puede desalinear observaciones. Las banderas de exclusión
permiten ver si falta saldo, atraso o ambos; contar motivos puede superar
cinco porque una fila puede tener dos motivos.

Cero corresponde a Sin atraso; 1 y 29 al tramo intermedio; 30 al último.
Los ausentes no corresponden a ninguno. El conteo cero de un tramo vacío
sería conocido, mientras que un atraso ausente sigue desconocido.

En septiembre las medianas son 2900, 1500, 3250 y 2350; en octubre 3100,
1750, ausente y 2550, en el orden común. Educación no tiene punto en octubre;
no se sustituye por cero. La escala temporal UTC conserva las fechas de corte
de esta muestra sin horas. Color y forma ayudan a distinguir segmentos,
pero educación puede permanecer en la leyenda sin pares conocidos de octubre.

Lectura posible: «La mediana conocida de consumo es 1750 MXN en octubre
y 1500 en septiembre, sobre bases 10/10 y 8/10. La comparación describe
disponibles por fecha; no demuestra el cambio de los mismos créditos ni
una causa». La dispersión muestra asociación sobre 19 pares sintéticos.

</details>

## D. Crear una variación y revisar un caso vacío

Copia declarative.py como `declarative_lab.py` **en la misma carpeta del
original**, para conservar sus importaciones de 04.06. En la copia:

1. Cambia el título de la dispersión conservando medida, fecha, población
   conocida y fuente sintética. Mantén columnas, tipos, unidades y exclusiones.
2. Cambia una forma o el tamaño de punto; conserva una señal además del color.
3. Ejecuta tu copia con octubre y una carpeta nueva. Compara pares.csv y
   resumen.csv con la entrega original; comprueba que los valores no cambiaron.
4. Ejecuta otra entrega con `--cut 2026-11-30`, fecha que no existe en la fuente.
   Revisa medianas, pares y tramos. ¿Qué porcentaje corresponde a 0/0?
5. Comprueba por qué fechas.html sigue mostrando septiembre/octubre aunque
   `--cut` elija noviembre. No afirmes que representa el corte vacío.
6. Intenta repetir una salida ya existente: debe rechazarse conservándola.

**Resultado:** variación propia y explicación del corte vacío. **Comprobación:**
la variación conserva las cifras de B/C; noviembre tiene cero registros y
ninguna mediana ni cobertura definida. Las fuentes permanecen intactas.

<details>
<summary>Ver solución razonada de D</summary>

Un título posible: «Saldo y atraso conocidos · octubre 2026 · 19/24 pares
de la muestra sintética SQL 03.01». Ajustar tamaño de marca no altera datos;
revisar la tabla confirma que no se cambió accidentalmente el filtro.

Con noviembre, resumen.csv conserva los cuatro segmentos con registros y
conocidos en cero, medianas y coberturas ausentes. 0/0 no es cobertura 0 %.
La dispersión indica Sin registros; tramos tiene tres conteos cero y mensaje
Sin registros. Es distinto de octubre, donde sí existen registros sin valores
conocidos en educación. La comparación temporal usa las dos fechas fijas
de la fuente y sigue mostrando sus siete medianas conocidas.

El script exige una carpeta nueva mediante `exist_ok=False`; el rechazo de
una carpeta existente protege resultados anteriores. Una exportación que
se interrumpa puede dejar una carpeta parcial: revisa todos los archivos
antes de considerar completa la entrega.

</details>

## E. Agregación y entrega sin conexión — ampliación

1. Reconstruye el fragmento `median(saldo_mxn):Q` de la lección usando corte,
   no resumen. Compara las tres medianas conocidas con B.
2. Explica por qué la agregación ocurre al interpretar la especificación y
   por qué esa vista todavía necesita cobertura y mensaje de educación.
3. Con chart-export preparado, genera una entrega nueva con `--bundle`.
   Desconecta la red y abre cada HTML; revisa PNG/SVG y las fechas.
4. Compara tamaños de JSON y HTML. Explica qué pierde una imagen estática
   y qué podría faltar si los datos se referenciaran mediante una URL.

<details>
<summary>Ver solución razonada de E</summary>

El detalle permite calcular medianas por segmento: 3100, 1750 y 2550 MXN.
La especificación solicita agregación; no agrega una columna al DataFrame.
Sumar medianas preparadas no reconstruye la mediana de todos los créditos.
Aunque las barras coincidan, sin cobertura ni mensaje queda incompleta la
explicación de educación.

El HTML básico usa bibliotecas desde CDN; la entrega con `--bundle` incorpora
bibliotecas y estos datos. El HTML pesa más y mantiene tooltip en el navegador.
PNG/SVG permiten lectura estática y no mantienen tooltip. Bibliotecas
incorporadas no garantizan una entrega sin red si sus datos todavía usan URL.

</details>

## Evidencia, reflexión y siguiente paso

Conserva código propio, tablas, JSON, HTML y comentario de lectura para las
cuatro vistas. Registra gestor, versiones y cómo abrirlas; PNG/SVG y la prueba
sin conexión son ampliaciones. Explica pregunta, unidad, base, ausencias y
qué se comprobó frente a los CSV y Matplotlib. Registra tu evidencia y dudas
en PROGRESS.md; disponer de este material no acredita completar el lab.

Reflexiona: ¿qué sabe el esquema sobre la corrección de una mediana? ¿Por qué
un ID numérico puede ser nominal? ¿Qué cambia al añadir una agregación?
¿Cómo distingues fallo del visor de ausencia real de datos?

No hay checkpoint de proyecto implementado. Continúa con el
[plan de 04.08 — Interacción con Altair](../../../curriculum/04_visualization_python/README.md#08-interaccion-con-altair),
pendiente y opcional. Si omites esa ampliación, consulta el
[plan de 04.09 — Cierre visual del análisis](../../../curriculum/04_visualization_python/README.md#09-cierre-visual-del-analisis),
también pendiente. Las referencias primarias están en la lección.

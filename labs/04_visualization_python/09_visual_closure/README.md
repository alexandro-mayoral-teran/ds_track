# Lab 04.09 — Cierre visual del análisis

## Propósito, entradas y preparación

Lee la [lección 04.09](../../../curriculum/04_visualization_python/09_visual_closure/README.md)
y completa 04.01–04.07 con sus labs y prerrequisitos. 04.08 es opcional.
Prepararás una entrega que otra persona pueda revisar y reconstruir sin
depender de tu sesión original.

**Entradas:** closure.py y los CSV sintéticos de SQL 03.01. **Resultado:**
tablas conciliadas, figura Matplotlib, vista Altair, interpretación propia
e instrucciones comprobadas. Conserva fuentes, scripts, SQLite y entregas
previas. No necesitas Quarto, notebook, aplicación ni publicación en línea.

Tiempo orientativo: dos sesiones de 60–90 minutos para A–D; E es extensión.
Usa el gestor y recorrido de tu shell indicado en la lección. Desde la raíz,
ejecuta closure.py con `--cut 2026-10-31` y una carpeta nueva
`curriculum/04_visualization_python/09_visual_closure/output/lab_09`.
Abre altair.html en un navegador compatible con conexión. --bundle y
--interactive son opcionales y no se necesitan para A–D.

## A. Definir la ficha y conciliar indicadores

1. Escribe la pregunta, público, fecha, fuente, población, unidad y medida
   antes de describir las figuras. Explica qué representa una fila de corte.csv.
2. Calcula las cuatro medianas desde los saldos originales. Conserva el
   cero del crédito 004 y aparta ausencias sin imputarlas.
3. Comprueba conteos/cobertura por segmento y global en indicadores.csv.
   Calcula la mediana global desde el detalle, no desde medianas de grupos.
4. Revisa referencia_csv.csv y conciliacion.csv: cuenta comprobaciones y
   distingue coincidencia de ausencias de un valor numérico cero.
5. Explica qué comprobaron los cálculos y qué todavía requiere revisión visual.

**Resultado:** ficha y cálculos propios. **Comprobación:** 24 registros,
21 saldos conocidos, mediana global 2300 y cobertura 87,5 %; 20 coincidencias.

<details>
<summary>Ver solución razonada de A</summary>

La pregunta compara medianas conocidas por segmento y cobertura en octubre.
Una fila es un crédito/corte; saldo se mide en MXN y cobertura en conocidos
entre registros. Medianas: comercio 3100 (5/5), consumo 1750 (10/10),
educación ausente (0/3), servicios 2550 (6/6).

Los 21 saldos conocidos del detalle producen mediana 2300. La cobertura
es 21/24 = 87,5 %; promediar 100, 100, 0 y 100 daría 75 %, otra base.
Educación no tiene mediana, pero sí registros y cobertura 0 %. El saldo
cero del crédito 004 es conocido y participa en la mediana de consumo.

Se comparan cuatro campos por cinco grupos, incluido Todos: 20 filas.
Una ausencia de mediana debe coincidir con ausencia en la referencia,
nunca con cero. El cálculo independiente revisa números/bases; todavía
hay que cotejar qué campo dibuja cada figura, unidades y legibilidad.

</details>

## B. Comparar las figuras y redactar una interpretación

Abre matplotlib.png/svg y altair.html junto a resumen.csv.

1. Identifica marca, medida, unidad, orden y escala de cada panel.
2. Comprueba que ambas herramientas representan las mismas medianas
   y coberturas; explica cualquier diferencia de apariencia.
3. Revisa educación y la anotación de cobertura. Distingue mediana ausente,
   cobertura cero y saldo cero válido.
4. Crea interpretacion_propia.md en tu entrega con ficha, un hallazgo,
   valores/bases que lo sostienen y dos límites. No copies informe.md completo.
5. Revisa si tu texto afirma totales, riesgo, causalidad o cambios entre cortes
   que estas figuras no demuestran.

**Resultado:** interpretación propia y revisión de figuras.

<details>
<summary>Ver solución razonada de B</summary>

Ambas figuras usan barras de medianas conocidas en MXN y puntos de cobertura
en porcentaje, con categorías comunes y unidades horizontales separadas.
Los textos y formatos pueden diferir; los valores deben conservarse.
El mensaje de educación evita dibujar una mediana cero inventada.

Una interpretación posible: «Entre los segmentos con saldo conocido,
comercio tiene la mayor mediana en octubre: 3100 MXN sobre 5/5 registros.
Consumo tiene 1750 sobre 10/10 y servicios 2550 sobre 6/6. Educación conserva
tres registros sin saldo conocido; no podemos ordenar su mediana. Esta
muestra ficticia describe disponibles por segmento, no riesgo real ni causa».

El límite de cobertura explica qué falta, pero no estima su saldo. No
presentar 3100 como saldo total ni atribuir una variación individual a una
comparación que solo contiene un corte.

</details>

## C. Reconstruir desde las copias y revisar un corte vacío

1. Lee RECONSTRUIR.md y entrega.json. Comprueba corte, opciones, versiones
   y que la revisión visual no se acredita automáticamente.
2. Ejecuta closure.py en otra carpeta nueva usando --source con la ruta
   de fuentes/ de tu entrega. Usa el mismo corte y dpi.
3. Compara por filas, valores, ausencias y bases corte.csv, resumen.csv,
   indicadores.csv y referencia_csv.csv de ambas entregas.
4. Abre de nuevo PNG y HTML. ¿Es necesario que dos PNG tengan exactamente
   los mismos bytes para comunicar los mismos datos?
5. Genera otra entrega con `--cut 2026-11-30`. Revisa informe, tabla y figuras:
   ¿qué cambia entre educación sin saldo en octubre y un corte sin registros?
6. Intenta repetir una carpeta existente y comprueba que se conserva.

**Resultado:** reconstrucción comprobada y explicación del caso vacío.

<details>
<summary>Ver solución razonada de C</summary>

fuentes/ contiene creditos.csv y cortes.csv completos, incluidos septiembre
y octubre; corte.csv solo contiene la fecha elegida. Las copias permiten
reconstruir sin sustituirlas por el resumen. El repositorio y el entorno
siguen siendo necesarios: la salida no incorpora todo el código.

Con mismas entradas/reglas/corte, las tablas y ausencias coinciden. Una
diferencia de motor o metadatos de imagen puede cambiar bytes sin cambiar
los valores; de todos modos hay que revisar legibilidad y posiciones.

Noviembre tiene cero registros, cero conocidos, mediana y cobertura ausentes
en todos los grupos. No hay segmento ganador ni cobertura 0 %. Educación
en octubre sí tiene tres registros, ninguna mediana y cobertura 0/3 = 0 %.
Las 20 comprobaciones también deben conciliar ausencias en el corte vacío.

La carpeta existente se rechaza; usa otra en lugar de borrar o reiniciar
una entrega. Una ejecución interrumpida puede dejar salidas parciales.
entrega.json no sustituye abrir todos los archivos esperados.

</details>

## D. Revisión acompañada y cierre con evidencia

Entrega la carpeta completa, la interpretación propia y acceso al código
del repositorio a quien te acompaña. Antes de explicar verbalmente:

1. Pídele localizar pregunta, fecha, unidad, población y medida en los archivos.
2. Pídele cotejar una mediana y una ausencia con las fuentes.
3. Sigue las instrucciones de reconstrucción en una sesión nueva del entorno
   elegido; no dependas de variables de notebook o memoria de una sesión previa.
4. Registra dudas, correcciones, entorno/visor, comandos usados y archivos
   revisados en revision.md dentro de la entrega.
5. Explica por qué cada panel existe y qué afirmación no podrías sostener.
6. Registra la evidencia en tu bitácora personal junto a la práctica sin marcar aprendizaje completado
   solo por haber generado archivos.

**Criterio de salida:** puedes reconstruir, conciliar, justificar figuras
y explicar un hallazgo con base y límites. Si algo esencial falla, corrige
y vuelve a revisar. La revisión puede cubrir una parte del lab por sesión.

<details>
<summary>Ver orientación razonada de D</summary>

Una revisión útil deja evidencia específica: «Mediana de consumo contrastada
con diez saldos; ausencia de educación comprobada con tres filas; PNG/SVG
y HTML cotejados; reconstrucción desde fuentes/ en carpeta nueva; texto
corregido para no afirmar riesgo». No basta «todo funciona».

Quien acompaña revisa y pregunta; quien aprende calcula, ejecuta y explica.
Si la entrega solo se entiende con explicaciones verbales, completa ficha,
texto o instrucciones. No hay que publicar datos, crear un proyecto nuevo
ni completar interacción avanzada para alcanzar este criterio.

</details>

## E. HTML sin conexión e interacción — extensión

Con el convertidor de 04.07 preparado, genera otra entrega con --bundle.
Si completaste 04.08 y lo deseas, añade --interactive.

1. Abre altair.html sin red y compara PNG/SVG Altair con resumen.csv.
2. Si incluiste explorador, elige consumo y educación. Explica por qué
   consumo tiene nueve puntos y mediana calculada sobre diez saldos.
3. Guarda una captura con estado y base explícitos; revisa que no reescriba CSV.
4. Comprueba que la figura principal sigue mostrando el corte completo.

<details>
<summary>Ver solución razonada de E</summary>

--bundle incorpora bibliotecas y estos datos, por lo que la vista se abre
sin red; PNG/SVG conservan lectura estática. El explorador empieza en Todos
y reutiliza las reglas de 04.08. Consumo tiene nueve pares porque al crédito
006 le falta atraso, pero su saldo entra en la mediana sobre diez conocidos.
Educación tiene registros sin pares; no mediana cero. Los controles no
alteran archivos ni filtran la figura principal del informe.

</details>

## Evidencia, reflexión y siguiente paso

Conserva fuentes, tablas conciliadas, figuras, informe, interpretación propia,
instrucciones y registro de revisión/reconstrucción. Explica qué se comprobó
y qué sigue limitado por la cobertura. Anota dudas y evidencias en tu bitácora personal junto a la práctica.

Reflexiona: ¿por qué una referencia independiente ayuda? ¿Qué no garantiza
una conciliación correcta? ¿Qué se pierde al enviar solo un PNG? ¿Qué
cambio de la fuente obligaría a reconstruir y revisar toda la entrega?

No hay proyecto/checkpoint implementado asociado. Continúa con el
[05.01 — Del notebook a módulos](../../../curriculum/05_python_applied/01_notebook_to_modules/README.md),
reutilizando este análisis. El material del módulo 04
está disponible; el aprendizaje requiere evidencia de sus criterios.

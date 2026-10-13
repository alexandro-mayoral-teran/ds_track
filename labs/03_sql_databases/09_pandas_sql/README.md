# Lab 03.09 — Integración pandas y SQL

## Entrada, actividad y resultado

Lee la [lección 03.09](../../../curriculum/03_sql_databases/09_pandas_sql/README.md)
y completa sus prerrequisitos. Recibes los CSV originales de 03.01, el esquema,
el preparador de 03.03 y [integration.py](../../../curriculum/03_sql_databases/09_pandas_sql/integration.py)
con detail.sql y summary.sql. Produce una base reconstruida, comparación entre
pandas/SQL, tabla exportada, figura y explicación de resultados con cobertura.

Las consultas se hacen en lectura; conserva las fuentes y las copias de 03.08.
No publiques las bases ni los resultados de output. Sigue los recorridos de
tu shell y entorno en la lección. Puedes estudiar A–B, C–D y E–F en tres sesiones;
la extensión G es opcional. Usa una carpeta de entrega nueva en cada exportación.

## A — Reconstruir y explicar las entradas

1. Ejecuta el preparador de 03.03 con la ruta de base de esta lección.
2. Comprueba 16 clientes, 24 créditos y 48 cortes, sus claves y relaciones.
3. Repite el preparador: debe verificar sin recargar.
4. Reconstruye otra base con una ruta nueva y consulta usando --database.
5. Explica por qué la copia modificada de 03.08 no tiene los resultados originales.

<details>
<summary>Ver solución razonada de A</summary>

La base se reconstruye desde los mismos tres CSV y esquema. No requiere copiar
un archivo personal ni compartir un entorno. La segunda reconstrucción debe
tener el mismo contenido y restricciones; no exigimos identidad de bytes.
La repetición sobre el archivo existente lo conserva y compara con las fuentes.

03.08 conserva un estado de práctica con 49 cortes y 1350 en 001/octubre;
la muestra original tiene 48 y 1300. No reinicies esa copia para que coincida.
Reproduce el cierre en una base separada con sus propias entradas y rutas.

</details>

## B — Leer con parámetros y tipos

1. Revisa detail.sql y declara la unidad del resultado.
2. Ejecuta read_sql_query con params y dtype, como en la lección.
3. Comprueba 24 filas, siete columnas y clave crédito/fecha única en octubre.
4. Inspecciona 001, 004 y 024. Identifica texto, cero y ausencias.
5. Convierte fecha a datetime en una copia si quieres explorarla; explica cómo
   mantendrías el mismo contrato en ambos recorridos.

<details>
<summary>Ver solución razonada de B</summary>

detail.sql relaciona cortes con créditos y clientes por claves. 001 conserva
su texto con ceros y saldo 1300; 004 tiene saldo 0 conocido; 024 tiene saldo y
atraso NA. La lectura declara string para IDs/fecha y Int64 para medidas.
NULL no equivale a cero, y el índice pandas no es la clave del crédito.

```python
assert not detalle.duplicated(["id_credito", "fecha_corte"]).any()
assert detalle["saldo_mxn"].count() == 21
```

Las tasas usan Float64 y conservan ausencias. Si conviertes fecha en solo una
versión, una diferencia de tipos no demuestra necesariamente diferencia de
observaciones; acuerda la representación y vuelve a comparar sin ocultar valores.

</details>

## C — Conciliar el detalle antes de resumir

1. Lee los CSV mediante read_sources y calcula reference_detail para octubre.
2. Explica validate='many_to_one' y la revisión de _merge.
3. Compara con el detalle SQL usando claves, tipos y todas las columnas.
4. En una copia del DataFrame de referencia, cambia un saldo o duplica una fila
   y comprueba que la comparación lo detecta. Conserva el original.

<details>
<summary>Ver solución razonada de C</summary>

La referencia parte de los CSV, filtra octubre y usa merge por ID, no por
posición. validate verifica unicidad del lado de referencia; _merge demuestra
que cada observación tiene crédito y cada crédito cliente. Ambas rutas conservan
24 filas con los mismos valores y atributos.

```python
pd.testing.assert_frame_equal(detalle_sql, detalle_pandas, check_exact=True)
```

Antes ordena por crédito/fecha y normaliza índice/columnas con el contrato
declarado. No conviertas a set ni desactives comprobación de tipos. Cambiar
una fila o duplicarla debe fallar, aunque manipularas otro saldo para conservar
la suma total. Esa prueba se hace solo en memoria, sin escribir sobre la base.

</details>

## D — Indicadores equivalentes

1. Compara summary.sql con reference_summary: identifica conteos, suma, tasa y cobertura.
2. Predice educacion en octubre y septiembre antes de ejecutar.
3. Concilia grupos con el corte completo y anota numerador/denominador de la tasa.
4. Explica qué cambiaría con sum sin min_count=1 o rellenando NULL con cero.

<details>
<summary>Ver solución razonada de D</summary>

Octubre conserva cuatro grupos y 24 observaciones. Sus sumas conocidas son
comercio 15 500, consumo 15 900, servicios 15 300 y educacion NA. Total conocido
46 700 MXN sobre 21 saldos conocidos. Atrasos: 9 confirmados entre 21 conocidos,
tasa ≈ 42.86 % y cobertura 21/24 = 87.5 %.

Educacion en octubre tiene tres saldos ausentes, dos atrasos conocidos y uno
confirmado: tasa 50 %, cobertura ≈ 66.67 %. En septiembre tiene dos saldos
conocidos, pero ningún atraso conocido: tasa NA, cobertura 0 %. No mezcles la
cobertura de una medida con la de otra.

SUM de SQL conserva NULL cuando no hay conocidos; pandas requiere min_count=1.
La ausencia no se corrige para que una figura tenga cuatro barras.
compare_summary compara campos enteros y NA exactamente y tasas con tolerancia.
No promedies tasas de segmentos para obtener la del corte.

</details>

## E — Exportar e interpretar la gráfica

1. Ejecuta --output con una carpeta nueva. Revisa los dos CSV, figura y evidencia.
2. Recarga con los tipos del script y comprueba que 001 y las ausencias se conservan.
3. Explica unidades, fecha y conocidas/observaciones de cada segmento.
4. Redacta un hallazgo y una limitación; añade tu explicación a la evidencia.
5. Repite sin --output y comprueba que se conservan los archivos de entrega.

<details>
<summary>Ver solución razonada de E</summary>

El script exporta sin índice y recarga CSV con dtype y reglas de ausencia
explícitos. La gráfica utiliza el resumen conciliado; muestra comercio 15 500,
consumo 15 900 y servicios 15 300 MXN conocidos. educacion se conserva en el
eje con el mensaje «Sin saldo conocido · 0/3».

Hallazgo posible: consumo tiene la mayor suma conocida entre segmentos con
saldo observado en octubre. Limitación: no podemos ubicar educacion por saldo
porque faltan sus tres importes; tampoco inferimos causalidad ni una tasa de
atraso desde barras de saldo. La tabla conserva ese indicador por separado.

Una carpeta existente se rechaza para no sobrescribir tu evidencia. Para
repetir cálculos, omite --output; para otra entrega, elige otra carpeta nueva.

</details>

## F — Vacíos y cambios de parámetros

1. Ejecuta septiembre, fecha inexistente y umbral 100, en ambas rutas.
2. Exporta una fecha vacía a otra carpeta nueva y revisa el mensaje de la figura.
3. Comprueba columnas y tipos del detalle/resumen vacío y su recarga CSV.
4. Explica qué representa una tasa 0 % con atrasos conocidos frente a una tasa NA.

<details>
<summary>Ver solución razonada de F</summary>

Septiembre tiene 24 observaciones, cuatro grupos y 47 200 MXN conocidos.
Una fecha inexistente entrega cero filas y grupos con el mismo esquema; la
figura informa ausencia de observaciones. No aparecen créditos con saldo cero.

En octubre, umbral 100 da cero confirmados, pero conserva conocidos y grupos;
tasas 0 % entre los conocidos. La tasa NA de educacion en septiembre significa
que no existe base conocida para calcularla; no demuestra ausencia de atrasos.
El umbral de atraso no cambia la suma conocida de saldo.

</details>

## G — Extensión: división de trabajo

Propón qué operaciones ejecutarías en SQL y cuáles en pandas para un reporte
que consulte otro corte. Explica entradas, parámetros, claves, transferencia
de filas y comprobaciones. chunksize y to_sql no son requisitos para cerrar.

<details>
<summary>Ver una decisión razonada</summary>

SQL puede filtrar/unir/agregar cerca de los datos; pandas permite revisar
resultados, conciliar otra referencia y preparar la figura. Leer toda la base
en cada lenguaje no es siempre necesario, pero una consulta ya agregada no
sustituye comprobar cardinalidad y cobertura. Menos filas transferidas tampoco
demuestra por sí solo mayor rendimiento; habría que medir el recorrido.

to_sql con replace no conserva automáticamente el contrato relacional y append
no resuelve repetición. Para estas entradas reutilizamos la carga explícita;
los límites de transacción permanecen visibles como en 03.08.

</details>

## Evidencia, criterio de cierre y siguiente paso

Entrega SQL, script, parámetros y tu explicación de la conciliación y figura.
Debes poder reconstruir otra base, explicar las claves y relaciones, conservar
datos desconocidos y resolver casos vacíos. Incluye la evidencia de escrituras
controladas de 03.08: este análisis de lectura no sustituye esa habilidad.

Registra evidencia y dudas en PROGRESS.md. El módulo puede cerrarse como
aprendizaje solo cuando demuestres sus criterios, no porque haya nueve lecciones
disponibles. No hay checkpoint de 02_credit_database implementado.
Continúa con el [plan de 04 — Visualización en Python](../../../curriculum/04_visualization_python/README.md),
cuya primera lección todavía está pendiente de desarrollo.

# Lab 02.09 — Cambiar largo y ancho conservando observaciones

## Relación, entrada y resultado

- Lección: [Cambiar la forma de una tabla](../../../curriculum/02_pandas/09_reshape_tables/README.md).
- Entrada: cartera_resumen.csv de 07 y reshape_tables.py de 09.
- Resultado: saldos en ambas formas, marcas de presencia y una vuelta comprobada.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 70 a 100 minutos o dos sesiones. Predice antes de ejecutar y consultar
soluciones. Añade exploraciones a main después de leer detalle; modifica copias
y escribe solo en output. No rellenes desconocidos para hacer coincidir resultados.

## Parte A — Interpretar cada celda

1. Ejecuta el script y localiza 001, 004 y 005 en saldo_ancho.csv.
2. Comprueba cuántas filas y columnas tiene cada formato.
3. Explica por qué la celda NA de 005/septiembre no debe convertirse en cero.
4. Verifica la vuelta: 48 filas, seis saldos desconocidos y 93900 MXN conocidos.

<details>
<summary>Ver solución de la parte A</summary>

001: 1100/1300 en septiembre/octubre. 004: 1400/0, con cero conocido en octubre.
005: NA/1700; la observación de septiembre existe, pero su importe es desconocido.
El largo tiene 48 filas y tres columnas; el ancho 24 filas y tres columnas, ID y
dos cortes. El número de observaciones no se deduce contando solo filas del ancho.
Las marcas de presencia son True en las 48 celdas de esta muestra completa.

</details>

## Parte B — Cambiar un valor, conservar la forma

1. En una copia del detalle, cambia el saldo de 005/septiembre de NA a 1500.
2. Proyecta, crea ancho, reconstruye y ejecuta comprobar_vuelta.
3. Predice saldos conocidos/desconocidos y nuevo total; revisa la celda modificada.

<details>
<summary>Ver solución de la parte B</summary>

```python
otra = detalle.copy()
mascara = (otra["id_credito"] == "005") & (otra["fecha_corte"] == pd.Timestamp("2026-09-30"))
otra.loc[mascara, "saldo_mxn"] = 1500
largo2 = proyectar(otra)
ancho2, marcas2 = crear_ancho(largo2)
recuperado2 = reconstruir(ancho2, marcas2)
comprobar_vuelta(largo2, recuperado2)
```

Siguen 48 observaciones, 24 IDs y dos cortes; ahora 43 saldos conocidos, cinco
desconocidos y total **95400 MXN**. La marca de presencia ya era True y permanece
True. La sustitución es una propuesta de ejercicio, no una imputación automática.

</details>

## Parte C — Una observación ausente

1. Desde la muestra original, retira 001/octubre en una copia.
2. Predice cómo queda el ancho y qué produce un melt sin consultar marcas.
3. Reconstruye con las marcas y comprueba que recuperas 47 observaciones.
4. Explica por qué dropna sobre saldo borraría información adicional.

<details>
<summary>Ver solución de la parte C</summary>

```python
retirar = (detalle["id_credito"] == "001") & (detalle["fecha_corte"] == pd.Timestamp("2026-10-31"))
otra = detalle.loc[~retirar].copy()
largo2 = proyectar(otra)
ancho2, marcas2 = crear_ancho(largo2)
recuperado2 = reconstruir(ancho2, marcas2)
comprobar_vuelta(largo2, recuperado2)
```

El ancho sigue con 24 IDs y dos cortes. 001/octubre tiene NA y presencia False.
Un melt simple crea 48 combinaciones, una de las cuales no existía en la copia.
La reconstrucción con marcas conserva 47 observaciones, seis saldos desconocidos
y **92600 MXN** conocidos: 93900 − 1300.
Si haces dropna sobre saldo, conservas solo 41 importes conocidos y pierdes las
seis observaciones reales con importe desconocido. La ausencia de importe y de
observación no son equivalentes.

</details>

## Parte D — Una celda repetida

1. Concatena a una copia del detalle el registro 001/septiembre una segunda vez.
2. Comprueba que proyectar o pivot directo detienen la reorganización.
3. Solo como diagnóstico, usa pivot_table con suma sobre ID/corte y revisa 001/septiembre.
4. Explica por qué no aceptas esa suma como solución al duplicado accidental.

<details>
<summary>Ver solución de la parte D</summary>

```python
mascara = (detalle["id_credito"] == "001") & (detalle["fecha_corte"] == pd.Timestamp("2026-09-30"))
duplicado = pd.concat([detalle, detalle.loc[mascara]], ignore_index=True)
diagnostico = duplicado.pivot_table(
    index="id_credito", columns="fecha_corte", values="saldo_mxn",
    aggfunc=sumar_conocidos, dropna=False, observed=True,
)
print(diagnostico.loc["001", pd.Timestamp("2026-09-30")])  # 2200
```

La celda requería una observación y ahora hay dos. Proyectar detecta la clave
repetida; pivot directo también falla. pivot_table suma 1100 + 1100 = 2200 y
oculta la repetición en un solo valor. Es una agregación, no recuperación del dato
correcto. Hay que investigar el duplicado, no cambiar de función para evitar el error.

</details>

## Parte E — Resumen ancho y pérdida de detalle

1. Revisa saldo_segmento_corte.csv y concilia los dos cortes con la lección 7.
2. Explica por qué educación/octubre queda NA.
3. Haz melt del resumen y predice si puedes reconstruir los 48 IDs originales.

<details>
<summary>Ver solución de la parte E</summary>

El resumen tiene cinco filas, segmento y dos columnas de corte. Sus sumas conocidas
son 47200 y 46700. Educación/octubre tenía tres observaciones pero ningún importe
conocido; sumar_conocidos conserva NA, no cero.
Melt produce diez indicadores segmento/corte, no 48 observaciones ni la identidad
de cada crédito. Una suma por segmento no conserva todos los valores individuales
que la produjeron. No afirmar que pivot_table es reversible como el pivot del detalle.

</details>

## Ampliación opcional — Un solo corte o entrada vacía

Filtra solo septiembre y repite la vuelta. El esquema ancho mantiene ambos cortes,
pero las marcas de octubre son False: se recuperan 24 observaciones, no 48.
Repite con detalle.iloc[:0].copy(): se obtienen cero IDs y cero observaciones con
columnas conservadas. Exporta a otras rutas dentro de output.

## Evidencia, reflexión y siguiente paso

- Conserva código/notas con unidad de fila, claves de celda, medidas, marcas de
  presencia y comprobaciones de filas, valores y desconocidos.
- ¿Qué campos del detalle no recupera nuestra proyección?
- ¿Cuándo una celda vacía describe un valor desconocido y cuándo una combinación ausente?
- ¿Qué evidencia necesitarías para interpretar un cero rellenado automáticamente?
- Si usas Git, revisa diff y registra código/notas. output está ignorado;
  publicar resultados no es requisito para completar el lab.

Continúa con el [alcance de 10 — Análisis y primera gráfica](../../../curriculum/02_pandas/README.md#10-analisis-y-primera-grafica),
pendiente de desarrollo, antes de su futuro lab.

# Lab 02.07 — Conciliar indicadores por grupo

## Relación, entrada y resultado

- Lección: [Agrupar y resumir](../../../curriculum/02_pandas/07_group_summarize/README.md).
- Entrada: cartera_resumen.csv (48 observaciones) y group_summarize.py de la lección.
- Resultado: resumen comprobado y una nota con grupos, indicadores y bases.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 70 a 100 minutos o dos sesiones. Predice antes de ejecutar y desplegar
soluciones. Puedes añadir exploraciones dentro de main después de leer el detalle.
Trabaja con copias; conserva la fuente. No rellenes cantidades desconocidas para
hacer que una comprobación coincida.

## Parte A — Reconstruir un grupo

1. Ejecuta el script y filtra consumo en septiembre en el detalle.
2. Comprueba filas, saldos conocidos y atrasos conocidos.
3. Recalcula saldo, promedio, cobertura y tasa ≥ 30 entre conocidos.
4. Explica por qué no usas necesariamente el mismo denominador en cada indicador.

<details>
<summary>Ver solución de la parte A</summary>

```python
mascara = (detalle["fecha_corte"] == pd.Timestamp("2026-09-30")) & (detalle["segmento"] == "consumo")
grupo = detalle.loc[mascara.fillna(False)]
print(len(grupo), grupo["saldo_mxn"].count(), grupo["dias_atraso"].count())  # 9, 7, 7
print(grupo["saldo_mxn"].sum(min_count=1))  # 10400
```

Promedio de saldo conocido: 10400/7 ≈ 1485.71. Hay dos casos confirmados ≥ 30,
cobertura 7/9 ≈ 77.78 % y tasa entre conocidos 2/7 ≈ 28.57 %.
Los siete saldos y los siete atrasos conocidos no corresponden exactamente a
las mismas filas. Se necesita la base específica de cada indicador.

</details>

## Parte B — Grupos con información desconocida

1. Revisa educación en septiembre y octubre.
2. Predice qué indicadores quedan NA y cuáles sí se pueden calcular.
3. Compara la suma predeterminada con sumar_conocidos para saldo de educación/octubre.
4. Explica qué perderías al agrupar con dropna=True.

<details>
<summary>Ver solución de la parte B</summary>

Septiembre: educación tiene tres filas, dos saldos conocidos (6500 MXN), pero
ningún atraso conocido. Cobertura cero y tasa NA. Octubre: tres filas, ningún
saldo conocido; suma/promedio NA. Tiene dos atrasos conocidos y un caso ≥ 30,
por tanto cobertura ≈ 66.67 % y tasa 50 %.

La suma predeterminada de los tres saldos ausentes puede dar cero; min_count=1
mantiene ausencia de observaciones. Con dropna=True se excluyen las dos filas
sin segmento, saldos 1700 y 2300: el resumen contabiliza 46 filas y 89900 MXN,
en lugar de 48 y 93900. No desaparecieron de la fuente, pero sí de ese resumen.

</details>

## Parte C — Una categoría corregida, totales conservados

1. En una copia, asigna consumo al segmento ausente del registro 7.
2. Resume y predice número de grupos, saldo y tasa de consumo/septiembre.
3. Comprueba que el total conocido de la tabla no cambia.

<details>
<summary>Ver solución de la parte C</summary>

```python
otra = detalle.copy()
otra.loc[otra.index[6], "segmento"] = "consumo"
resumen2 = resumir(otra)
```

El grupo sin segmento de septiembre desaparece al quedar vacío. Hay nueve grupos.
Consumo/septiembre pasa a diez filas, ocho saldos conocidos, saldo **12100 MXN**
y ocho atrasos conocidos. El caso añadido tiene 20 días: los confirmados ≥ 30
siguen siendo dos. Cobertura 80 %, tasa entre conocidos **25 %**.
El total sigue siendo 93900: solo cambió la clasificación de 1700 MXN.
La corrección es una propuesta didáctica, no una regla para inventar segmentos.

</details>

## Parte D — Una base diferente responde otra pregunta

1. Para consumo/septiembre, compara casos ≥ 30 entre conocidos y entre todas las filas.
2. Reconstruye promedio de saldo y tasa global desde numeradores y denominadores.
3. Explica por qué no sumas porcentajes ni IDs distintos de los grupos para obtener
   automáticamente tasas o créditos únicos de toda la tabla.

<details>
<summary>Ver solución de la parte D</summary>

Consumo/septiembre: 2/7 ≈ 28.57 % entre atrasos conocidos; 2/9 ≈ 22.22 % de
casos confirmados entre todas las observaciones. La segunda medida no demuestra
que las dos desconocidas tengan atraso menor a 30.

Toda la tabla tiene 42 saldos conocidos: promedio **93900/42 ≈ 2235.71 MXN**.
Tiene 40 atrasos conocidos y 15 confirmados ≥ 30: tasa **37.5 %**. Son indicadores
sobre observaciones de dos cortes, no sobre 24 créditos únicos en una fecha.
Los grupos tienen diferentes bases y algunos indicadores NA. Sus tasas y promedios
necesitan ponderaciones adecuadas; sus conteos de IDs pueden contar el mismo ID
en dos fechas. detalle.id_credito.nunique() da 24, mientras size del detalle da 48.

</details>

## Parte E — Otro nivel de agrupación

1. Llama resumir con claves=["fecha_corte"].
2. Predice grupos, filas por corte y saldos conocidos.
3. Comprueba que las conciliaciones siguen pasando.
4. Filtra diciembre, resume la tabla vacía y exporta a otra ruta en output.

<details>
<summary>Ver solución de la parte E</summary>

```python
por_corte = resumir(detalle, claves=["fecha_corte"])
print(por_corte[["fecha_corte", "registros", "saldo_conocido_mxn"]])
vacio = detalle.loc[detalle["fecha_corte"] == pd.Timestamp("2026-12-31")].copy()
resumen_vacio = resumir(vacio)
exportar(resumen_vacio, entrada, carpeta / "output" / "resumen_vacio.csv")
```

Dos grupos: 24 observaciones en septiembre, saldo conocido **47200**; 24 en
octubre, **46700**. Los dos suman 93900, con 21 saldos conocidos cada uno.
La tabla vacía produce cero grupos con columnas conservadas; el CSV contiene
encabezados. No consultar una primera fila inexistente ni presentar su suma
con min_count=1 como un saldo cero medido.

</details>

## Ampliación opcional — transform frente a agg

Reproduce el transform de la lección. Comprueba que devuelve una Series de 48
valores alineados con el detalle y que el porcentaje de las filas con saldo
ausente queda desconocido. Explica por qué el total usado describe saldo conocido,
y por qué agg devuelve menos filas que transform en este caso.

## Evidencia, reflexión y siguiente paso

- Conserva código/notas con claves de grupo, numeradores, denominadores, cobertura
  y conciliaciones contra el detalle; identifica qué faltantes permanecen.
- ¿Qué implica cambiar de corte/segmento a solo corte o solo segmento?
- ¿Qué parte del saldo no puedes conocer aunque el resumen concilie?
- ¿Qué diferencia hay entre ausencia de casos conocidos y cero casos en una base conocida?
- Si usas Git, revisa diff y registra código/notas. output está ignorado; publicar
  resultados no es requisito para completar el lab.

Continúa con la [lección 08 — Combinar tablas](../../../curriculum/02_pandas/08_combine_tables/README.md)
antes de realizar su lab.

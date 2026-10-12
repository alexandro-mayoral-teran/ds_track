# Lab 02.08 — Combinar sin inflar registros

## Relación, entrada y resultado

- Lección: [Combinar tablas](../../../curriculum/02_pandas/08_combine_tables/README.md).
- Entradas: cartera_resumen.csv de 07, catálogo y combine_tables.py de 08.
- Resultado: tablas combinadas comprobadas y una nota con claves y cardinalidad.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 70 a 100 minutos o dos sesiones. Predice antes de ejecutar y desplegar
soluciones. Los fragmentos pueden añadirse a main después de crear detalle y
catalogo; modifica copias en memoria o en output, conservando las fuentes.

## Parte A — Seguir los diagramas con datos

1. Ejecuta el ejemplo y comprueba 24 + 24 = 48.
2. Explica por qué el left conserva 48 filas y un saldo conocido de 93900.
3. Identifica las ocho filas sin catálogo y qué significa su equipo ausente.
4. Compara con los diagramas: ¿qué clave relaciona cada operación?

<details>
<summary>Ver solución de la parte A</summary>

concat apila observaciones y después verifica ID/corte. El left relaciona segmento
con un catálogo único por segmento. Hay 40 coincidencias y ocho left_only: seis
observaciones de educación y dos con segmento ausente. Su saldo conocido suma
10500; los demás suman 83400. Los equipos ausentes no autorizan borrar esos registros.
La comparación entre cortes utiliza ID, después de delimitar cada fecha.

</details>

## Parte B — Comparar los tipos de unión

1. En memoria, realiza inner, right y outer sobre detalle/catalogo.
2. Usa validate="many_to_one" e indicator=True.
3. Comprueba conteos y saldos de la tabla de la lección.
4. Localiza agricultura en el outer y explica por qué no es un crédito observado.

<details>
<summary>Ver solución de la parte B</summary>

```python
for tipo in ["inner", "right", "outer"]:
    prueba = detalle.merge(catalogo, on="segmento", how=tipo,
                            validate="many_to_one", indicator=True)
    print(tipo, len(prueba), prueba["saldo_mxn"].sum(min_count=1))
```

inner: 40/83400; right: 41/83400; outer: 49/93900. Agricultura es right_only
y tiene ID, corte y saldo ausentes. Solo representa una fila del catálogo sin
observación relacionada. Un left no mostraría esa fila exclusiva del catálogo.

</details>

## Parte C — Un catálogo repetido

1. Añade a una copia del catálogo otra fila de consumo con equipo_Z.
2. Intenta unir_catalogo y comprueba que detiene la operación.
3. Solo como diagnóstico en memoria, une sin validate y compara filas/saldo.
4. Explica por qué many_to_many o drop_duplicates no resuelven automáticamente el conflicto.

<details>
<summary>Ver solución de la parte C</summary>

```python
extra = pd.DataFrame({"segmento": ["consumo"], "equipo": ["equipo_Z"]}, dtype="string")
catalogo_mal = pd.concat([catalogo, extra], ignore_index=True)
try:
    unir_catalogo(detalle, catalogo_mal)
except pd.errors.MergeError:
    print("El catalogo incumple many_to_one")
diagnostico = detalle.merge(catalogo_mal, on="segmento", how="left")
print(len(diagnostico), diagnostico["saldo_mxn"].sum(min_count=1))  # 67, 120200
```

Las 19 observaciones de consumo se relacionan dos veces; se repiten 26300 MXN
conocidos. 48 + 19 = 67 y 93900 + 26300 = 120200. Elegir un equipo exige evidencia;
la cardinalidad declarada detecta el problema, pero no sabe cuál versión es correcta.

</details>

## Parte D — Completar cobertura sin cambiar importes

1. En otra copia del catálogo válido, agrega educacion con equipo_E.
2. Ejecuta unir_catalogo y predice coincidencias/faltantes.
3. Comprueba que se conservan las 48 filas y los 93900 MXN conocidos.

<details>
<summary>Ver solución de la parte D</summary>

```python
extra = pd.DataFrame({"segmento": ["educacion"], "equipo": ["equipo_E"]}, dtype="string")
completo = pd.concat([catalogo, extra], ignore_index=True)
prueba = unir_catalogo(detalle, completo)
print(prueba["estado_union"].value_counts())
```

46 both y dos left_only, correspondientes a segmentos ausentes. Las seis
observaciones de educación ahora tienen equipo, pero sus saldos desconocidos
siguen desconocidos. Cobertura de catálogo y cobertura de cantidades son distintas.

</details>

## Parte E — Comparar los mismos IDs

1. Revisa comparacion_cortes.csv: cuenta IDs y cambios evaluables.
2. Comprueba el cambio de 001 y 004.
3. Explica por qué la suma de cambios evaluables es 2200 y no −500.
4. En una copia del detalle, retira solo 001 de octubre y vuelve a comparar.

<details>
<summary>Ver solución de la parte E</summary>

24 IDs aparecen en ambos cortes; 19 tienen ambos saldos conocidos. 001 cambia
de 1100 a 1300: +200. 004 cambia de 1400 a cero: −1400, un cero conocido.
La suma sobre los mismos 19 IDs es 2200. La resta −500 usa todos los saldos
conocidos de cada corte, con bases distintas por ausencias.

```python
retirar = (detalle["id_credito"] == "001") & (detalle["fecha_corte"] == pd.Timestamp("2026-10-31"))
otra = detalle.loc[~retirar].copy()
prueba = comparar_cortes(otra)
print(prueba.loc[prueba["id_credito"] == "001"])
```

El outer sigue mostrando 24 IDs: 001 queda left_only, saldo de octubre NA y
cambio NA. Hay 18 cambios evaluables, que suman 2000. No inferir saldo cero ni
cierre del crédito solo por ausencia en la copia.

</details>

## Ampliación opcional — Vacíos y claves ausentes

Prueba un detalle vacío con el catálogo válido: el left produce cero observaciones
y conserva columnas. Exporta a output/vacio. Un catálogo vacío con las columnas
y tipos correctos deja todas las observaciones left_only, sin cambiar sus importes.
Intenta añadir un segmento NA al catálogo: la función debe detenerlo antes del
merge, porque pandas podría relacionarlo con segmentos ausentes del detalle.

## Evidencia, reflexión y siguiente paso

- Conserva código/notas con unidad de fila, claves, tipo de unión, validate,
  conteos antes/después, saldos conocidos y coincidencias faltantes.
- ¿Qué diagrama describe una unión que multiplicó filas?
- ¿Qué reglas necesitarías para un catálogo cuya asignación cambia por corte?
- ¿Por qué verificar una suma no sustituye comparar observaciones?
- Si usas Git, revisa diff y registra código/notas. output está ignorado;
  publicar resultados no es requisito para completar el lab.

Continúa con el [alcance de 09 — Cambiar la forma de una tabla](../../../curriculum/02_pandas/README.md#09-cambiar-la-forma-de-una-tabla),
pendiente de desarrollo, antes de su futuro lab.

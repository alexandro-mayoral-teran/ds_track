# Lab 02.06 — Normalizar y comparar cortes con fechas

## Relación, entrada y resultado

- Lección: [Texto y fechas](../../../curriculum/02_pandas/06_text_dates/README.md).
- Entrada: cartera_texto_fechas.csv (48 registros) y text_dates.py de la lección.
- Resultado: exportaciones comprobadas y una nota con reglas y límites del análisis.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 70 a 100 minutos o dos sesiones. Predice antes de ejecutar y consultar
soluciones. Puedes añadir exploraciones dentro de main después de preparar.
Conserva la fuente original; las correcciones se hacen en memoria o sobre una copia en output.

## Parte A — Seguir el recorrido de un texto

1. Revisa categorías originales y normalizadas de los registros 1, 2, 4, 5 y 9.
2. Explica por qué quitar espacios no resuelve todos los problemas de catálogo.
3. Busca el fragmento literal "com" sobre el segmento normalizado de aceptados.
4. Comprueba la partición: 48 = 36 + 12, y 112800 = 81400 + 31400.

<details>
<summary>Ver solución de la parte A</summary>

1 pasa de " Consumo " a consumo; 2 de "SERVICIOS" a servicios; 4 de "Educación"
a educacion por el alias declarado. 5 tiene solo espacios, que pasan a ausencia.
9 conserva microcredito y queda fuera del catálogo. No se adivina una categoría.

```python
mascara = aceptados["segmento"].str.contains("com", regex=False, na=False)
print(aceptados.loc[mascara, ["numero_registro", "segmento"]])
```

La búsqueda selecciona comercio en esta muestra. Su objetivo es buscar un fragmento;
la validación de categoría utiliza pertenencia exacta al catálogo.

</details>

## Parte B — Ausencia, formato y calendario

1. Revisa los registros 14, 18, 23, 33, 38 y 47.
2. Predice cuáles terminan en NaT y cuáles se consideran ausentes o inválidos.
3. Comprueba que 38 se interpreta pese a sus espacios exteriores.
4. Interpreta "03/04/2026" con ambos formatos explícitos de la lección y explica la diferencia.

<details>
<summary>Ver solución de la parte B</summary>

14 contiene 2026-09-31: forma correcta, calendario imposible. 23 contiene
30/09/2026 y 33 contiene 2026-10-3: no cumplen la forma requerida.
Los tres terminan en NaT con fecha_corte_invalida. 18 está vacío y 47 tiene solo
espacios: fecha_corte_ausente. 38 se interpreta como 2026-10-31 tras strip.

```python
print(pd.to_datetime("03/04/2026", format="%d/%m/%Y"))  # 3 de abril
print(pd.to_datetime("03/04/2026", format="%m/%d/%Y"))  # 4 de marzo
```

El formato procede del contrato de la fuente, no de elegir una de estas salidas
por intuición. El texto original debe conservarse para justificar la interpretación.

</details>

## Parte C — Una corrección cambia el corte disponible

1. Copia fuente en memoria y corrige solo fecha_corte del registro 14 a 2026-09-30.
2. Ejecuta preparar con la copia y selecciona septiembre.
3. Predice aceptados/rechazados y nuevo saldo de septiembre.
4. Comprueba que el CSV original conserva la fecha imposible.

<details>
<summary>Ver solución de la parte C</summary>

```python
otra = fuente.copy()
otra.loc[otra.index[13], "fecha_corte"] = "2026-09-30"
trabajo2, aceptados2, rechazados2, banderas2 = preparar(otra)
septiembre2 = seleccionar_periodo(aceptados2, "2026-09-01", "2026-10-01")
print(len(aceptados2), len(rechazados2))  # 37, 11
print(len(septiembre2), septiembre2["saldo_mxn"].sum(min_count=1))  # 19, 42300
```

El saldo de 014 es 2400; septiembre pasa de 39900 a 42300. No cambió el saldo
de entrada, sino la posibilidad de aceptar ese registro. La fuente permanece intacta.
La corrección se propone solo como ejercicio: en una fuente real necesitaría evidencia.

</details>

## Parte D — La clave después de normalizar

1. Compara repeticiones de ID/corte en fuente y en trabajo.
2. Explica por qué los registros 43 y 44 se apartan.
3. En otra copia de la fuente, corrige el ID del registro 44 a 020.
4. Predice cambios en aceptados y en octubre; evalúa sin modificar otras filas.

<details>
<summary>Ver solución de la parte D</summary>

En fuente no coinciden literalmente "019" y " 019 ". En trabajo ambas filas
tienen ID 019 y fecha_corte 2026-10-31. Las dos se apartan por clave_repetida.

```python
otra = fuente.copy()
otra.loc[otra.index[43], "id_credito"] = "020"
trabajo2, aceptados2, rechazados2, banderas2 = preparar(otra)
octubre2 = seleccionar_periodo(aceptados2, "2026-10-01", "2026-11-01")
print(len(aceptados2), len(rechazados2))  # 38, 10
print(len(octubre2), octubre2["saldo_mxn"].sum(min_count=1))  # 20, 47800
```

Al resolver el conflicto se recuperan las dos filas, saldos 3100 y 3200, porque
ninguna incumplía otra regla. Octubre aumenta en 6300. Elegir arbitrariamente la
primera de la clave repetida recuperaría solo una fila y ocultaría la discrepancia.

</details>

## Parte E — Fechas de evento y límites del período

1. Selecciona ID 001 en aceptados y comprueba 60 y 91 días desde el alta.
2. Revisa el registro 12: ¿por qué se rechaza aunque ambas fechas se interpretaron?
3. Selecciona diciembre con un intervalo [2026-12-01, 2027-01-01).
4. Explica por qué 18 filas en ambos meses no prueba que se comparen los mismos créditos.

<details>
<summary>Ver solución de la parte E</summary>

001 tiene alta 2026-08-01, corte 2026-09-30 (60 días) y 2026-10-31 (91).
Son días desde alta, no días de atraso. El registro 12 tiene alta un día después
del corte y diferencia −1: incumple alta_posterior_corte.

```python
diciembre = seleccionar_periodo(aceptados, "2026-12-01", "2027-01-01")
print(diciembre.empty)  # True
print(diciembre["saldo_mxn"].sum(min_count=1))  # NA
```

No hay observaciones aceptadas de diciembre. La igualdad de conteos de septiembre
y octubre no asegura igualdad de IDs; sus rechazos son distintos. La diferencia
de totales describe dos conjuntos disponibles y necesita una comparación de
poblaciones antes de interpretarse como cambio de los mismos créditos.

</details>

## Ampliación opcional — Archivo vacío

Evalúa fuente.iloc[:0].copy() y exporta sus tres tablas a output/vacio. Deben
conservar columnas y tipos; los CSV solo contienen encabezados y la suma con
min_count=1 es NA. No depende de que existan 48 filas ni una primera fila que consultar.

## Evidencia, reflexión y siguiente paso

- Conserva código y notas con catálogo, formato temporal, ejemplos originales,
  motivos y conteos/totales antes y después de una corrección.
- ¿Qué normalizaciones puedes justificar y cuáles requieren información externa?
- ¿Por qué una fecha interpretable todavía puede incumplir una regla?
- ¿Qué cambiaría si la fuente incluyera horas o zonas horarias?
- Si usas Git, revisa diff y registra código/notas. output está ignorado; publicar
  los resultados no es requisito para completar el lab.

Continúa con la [lección 07 — Agrupar y resumir](../../../curriculum/02_pandas/07_group_summarize/README.md)
antes de realizar su lab.

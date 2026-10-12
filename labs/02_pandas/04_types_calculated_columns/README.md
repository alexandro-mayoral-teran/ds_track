# Lab 02.04 — Convertir y explicar columnas calculadas

## Relación, entrada y resultado

- Lección: [Tipos y columnas calculadas](../../../curriculum/02_pandas/04_types_calculated_columns/README.md).
- Entrada: su cartera_conversion.csv, con 40 registros ficticios, y types_calculated_columns.py.
- Resultado: tabla calculada comprobada y una nota con decisiones, casos y conciliación.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 60 a 90 minutos o dos sesiones. Predice antes de ejecutar y desplegar
soluciones. Trabaja con el entorno existente; conserva la fuente original.
Los fragmentos siguientes se pueden añadir dentro de main después de transformar.

## Parte A — Interpretar, no solo cambiar el formato

1. Ejecuta el script y compara dtypes de tabla y resultado.
2. Revisa 005, 014 y 023: ¿qué había en origen y qué quedó convertido?
3. Cuenta por columna ausentes e incompatibles; explica por qué no son lo mismo.
4. Comprueba que el ID 001 sigue siendo texto con ceros iniciales.

<details>
<summary>Ver solución de la parte A</summary>

La entrada tiene seis columnas string; la salida tiene 40 filas y 15 columnas.
Los tres campos numéricos pasan a Int64 y porcentaje_pago a Float64.
005 tiene saldo ausente y marca incompatible False; 014 tenía "error" y marca
True. 023 tenía "3.5": se interpreta como número, pero no como entero de días,
por eso queda NA y marcado True, sin truncar.

Conteos: saldo 1 ausente/1 incompatible; pago 1/1; días 1/2. Para explorar:

```python
casos = resultado["id_credito"].isin(["005", "014", "023"])
print(resultado.loc[casos, [
    "id_credito", "saldo_mxn_texto", "saldo_mxn", "saldo_mxn_incompatible",
    "dias_atraso_texto", "dias_atraso", "dias_atraso_incompatible",
]])
```

ID es string en ambas tablas: no es un importe al que haya que aplicar to_numeric.

</details>

## Parte B — Calcular y conciliar

1. Comprueba a mano la resta y el porcentaje de 001, 002 y 028.
2. Identifica qué registros no permiten restar saldo y pago.
3. Reproduce la conciliación sobre las 36 filas evaluables usando un ciclo de
   Python, para compararla con el cálculo por columnas.
4. Explica por qué sumar cada columna sobre todas sus cifras conocidas puede
   producir una comparación que no utiliza la misma base.

<details>
<summary>Ver solución de la parte B</summary>

001: resta 1150, porcentaje 8. 002: resta 1300, porcentaje aproximadamente
13.333333. 028: resta cero, porcentaje NA porque el denominador no es positivo.
Sin resta: 005, 009, 014 y 033. Faltar atraso no impide por sí solo una resta.

```python
base = resultado.loc[resultado["saldo_despues_pago_mxn"].notna()]
total_python = 0
for registro in base.to_dict("records"):
    total_python += registro["saldo_mxn"] - registro["pago_mxn"]
print(total_python)  # 211150
print(base["saldo_despues_pago_mxn"].sum(min_count=1))  # 211150
```

to_dict("records") produce la lista de diccionarios que ya conoces. El ciclo
sirve como comprobación didáctica; la transformación principal sigue vectorizada.
Sobre la misma base, 217750 − 6600 = 211150. Si se suman columnas con faltantes
independientemente, unas filas aportan saldo pero no pago y otras a la inversa.

</details>

## Parte C — Una modificación controlada

1. Copia el CSV a output/cartera_practica.csv y cambia solo esa copia.
2. Sustituye "pendiente" en el pago de 009 por 450.
3. En main cambia entrada a esa copia y salida a output/calculada_practica.csv.
4. Predice filas evaluables, marca incompatible, resta y nuevo total; ejecuta.

<details>
<summary>Ver solución de la parte C</summary>

En main, carpeta sigue apuntando a la carpeta de la lección:

```python
entrada = carpeta / "output" / "cartera_practica.csv"
salida = carpeta / "output" / "calculada_practica.csv"
```

009 tiene saldo 3250 y nuevo pago 450: resta 2800, porcentaje aproximadamente
13.846154. Su pago_incompatible pasa a False. Hay 37 restas evaluables y el total
es 211150 + 2800 = **213950**. Siguen siendo 40 filas en la salida; no se acumuló
otra tabla. La fuente original continúa con "pendiente".

</details>

## Parte D — Asignación y alineación

1. Vuelve a la muestra original. Clasifica una copia con un umbral de 40 días
   usando loc; conserva "sin dato evaluable" donde corresponda.
2. Predice y comprueba cuántos registros tienen al menos 40 días y qué ocurre con 023.
3. Reproduce el ejemplo de índices A/B de la lección y explica 90/180.
4. Comprueba que modificar esa copia no cambia resultado ni tabla.

<details>
<summary>Ver solución de la parte D</summary>

```python
practica = resultado.copy()
practica["estado_atraso"] = pd.Series("sin dato evaluable", index=practica.index, dtype="string")
practica.loc[practica["dias_atraso"].notna(), "estado_atraso"] = "menos de 40 dias"
mascara = (practica["dias_atraso"] >= 40).fillna(False)
practica.loc[mascara, "estado_atraso"] = "40 dias o mas"
print(mascara.sum())  # 16
```

Son 16 filas: 004, 005, 006, 011, 012, 013, 019, 020, 025, 026, 027,
032, 033, 034, 039 y 040. 023 permanece sin dato evaluable, no en el grupo menor.
005 puede clasificarse por atraso aunque no permita calcular saldo − pago.
La copia tiene categorías propias; resultado conserva el umbral de 30.
En A/B se restan valores de la misma etiqueta, aunque tengan posiciones distintas.

</details>

## Parte E — Sin observaciones (ampliación opcional)

Prueba transformar(tabla.iloc[:0].copy()) y su exportación a otra ruta dentro
de output. Predice forma y suma con min_count=1. No reemplaces la fuente.

<details>
<summary>Ver solución de la parte E</summary>

El resultado tiene forma (0, 15), con tipos y columnas conservados. El CSV contiene
solo encabezados. La suma con min_count=1 es NA; no es un total cero observado.
No hay primera fila que consultar. El cálculo no debe depender de que existan
40 filas: esa cantidad describe la muestra, no es un requisito de la función.

</details>

## Evidencia, reflexión y siguiente paso

- Conserva el código y una nota con origen, tipos, casos incompatibles, base de
  conciliación y totales antes/después de la modificación.
- ¿Por qué coerce requiere conservar el valor original?
- ¿Qué diferencia hay entre una conversión numérica y una regla de negocio?
- ¿Por qué Int64 y Float64 cumplen funciones distintas aquí?
- ¿Cuándo NA en una columna impide un cálculo y cuándo no?
- Si utilizas Git, revisa diff y registra cambios de código y notas. output está
  ignorado; publicar en el repo compartido no es requisito para completar el lab.

Continúa con el [alcance de la lección 05 — Faltantes, duplicados y reglas](../../../curriculum/02_pandas/README.md#05-faltantes-duplicados-y-reglas),
pendiente de desarrollo, antes de su futuro lab.

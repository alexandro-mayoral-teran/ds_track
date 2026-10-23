# Lab 10.02 — Seleccionar, transformar y resumir con Polars

## Propósito y entradas

Practicar las expresiones de la
[lección 10.02](../../../curriculum/10_polars_duckdb/02_polars_tables_expressions/README.md)
y comprobar resultados sin depender de ejemplos personales anteriores.
Necesitas el entorno Python con Polars 2.0.0 de sus
[recorridos](../../../curriculum/10_polars_duckdb/02_polars_tables_expressions/recorridos.md).
Elige una sesión; puedes repartir la práctica en varios momentos.

Fuente completa: tres créditos, dos cortes y seis observaciones.

| ID textual | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

El [CSV incluido](../../../curriculum/10_polars_duckdb/02_polars_tables_expressions/muestra.csv)
no se modifica. Clave ID/corte única, IDs de tres dígitos, fechas válidas
1900–2100, saldos enteros 0–2147483647, sin ausencias. Se valida toda la fuente,
incluidas las filas que no saldrán en la selección. No requiere entregas de 09
ni de 10.01; reutiliza funciones presentes en el repositorio.

## Actividad

1. Escribe la respuesta manual para **septiembre ≥ 2000 MXN** y para
   **octubre ≥ 0 MXN**, con IDs, importes, conteo y suma.
2. Carga el CSV con `cargar_tabla`, inspecciona forma y esquema. Usa `select`
   para obtener ID/saldo y `with_columns` para añadir `saldo_miles_mxn`.
   Explica cómo cambian las columnas y si cambia la fuente.
3. Selecciona ambos escenarios con `seleccionar` y llama a
   `comprobar_seleccion` con sus parámetros correspondientes. Repite septiembre
   con umbral **2001** y explica la fila que desaparece.
4. Resume **toda la fuente** por corte con `resumir_por_corte` y
   `comprobar_resumen`. Explica por qué no representa la suma de la selección.
5. Consulta noviembre, que no existe. Comprueba la forma, tipos y control.
   Compara una selección vacía con agrupar una entrada vacía de esquema explícito.
6. Construye la salida incorrecta septiembre `002/2100`, `003/2400` y muestra
   que la conciliación la rechaza aunque su suma y conteo coincidan.
7. Reinicia la sesión o ejecuta el script completo desde otro proceso y explica
   una diferencia entre `Series` y expresión. Conserva tu evidencia en una
   carpeta nueva bajo `output/`; no publiques entornos ni salidas de práctica.

## Resultado esperado y comprobación

| Escenario | Pares ID/saldo MXN | Registros | Suma MXN |
| --- | --- | ---: | ---: |
| Septiembre ≥ 2000 | 002/2000, 003/2500 | 2 | 4500 |
| Septiembre ≥ 2001 | 003/2500 | 1 | 2500 |
| Octubre ≥ 0 | 001/100, 002/1900, 003/2600 | 3 | 4600 |
| Noviembre ≥ 2000 | Ninguno | 0 | 0 |

Fuente: `(6, 3)`; vista ID/saldo: `(6, 2)`; tabla con una derivada: `(6, 4)`.
Resumen completo: septiembre tres/4500 y octubre tres/4600, suma Int64.
Conserva los pesos enteros para conciliar; los miles Float64 son aproximados.

<details>
<summary>Solución razonada: recorrido esencial completo</summary>

Ejecuta desde la raíz en Python, con el intérprete correcto. Solo lee fuentes:

```python
from datetime import date
from pathlib import Path
import sys
import polars as pl

carpeta = Path("curriculum/10_polars_duckdb/02_polars_tables_expressions").resolve()
sys.path.insert(0, str(carpeta))
from tablas_polars import (
    ESQUEMA, SELECCION, cargar_tabla, transformar, seleccionar,
    resumir_por_corte, comprobar_seleccion, comprobar_resumen,
)

tabla = cargar_tabla()
original = tabla.clone()
print(tabla.shape, dict(tabla.schema))
vista = tabla.select("id_credito", "saldo_mxn")
ampliada = transformar(tabla)
assert vista.shape == (6, 2)
assert ampliada.shape == (6, 4)
assert tabla.equals(original)

for corte, minimo in [
    (date(2026, 9, 30), 2000),
    (date(2026, 9, 30), 2001),
    (date(2026, 10, 31), 0),
    (date(2026, 11, 30), 2000),
]:
    salida = seleccionar(tabla, corte, minimo)
    print(salida.to_dicts())
    print(comprobar_seleccion(salida, corte=corte, minimo=minimo))
    assert dict(salida.schema) == SELECCION

resumen = resumir_por_corte(tabla)
print(comprobar_resumen(resumen))
vacia = pl.DataFrame(schema=ESQUEMA)
assert seleccionar(vacia).shape == (0, 2)
assert resumir_por_corte(vacia).shape == (0, 3)

incorrecta = pl.DataFrame(
    {"id_credito": ["002", "003"], "saldo_mxn": [2100, 2400]}, schema=SELECCION
)
try:
    comprobar_seleccion(incorrecta, corte=date(2026, 9, 30), minimo=2000)
except ValueError as error:
    print("Rechazo esperado:", error)
else:
    raise AssertionError("Debia detectar pares alterados")
```

`clone` conserva una referencia de comparación de valores; `equals` comprueba
que no cambiaron. No exige copiar todos los buffers. `assert` sirve aquí para
evidencia de práctica; los validadores reutilizables lanzan errores explícitos.
No pases la tabla vacía al comprobador que espera resultados del CSV de seis
filas: representarían fuentes distintas.

La selección de noviembre conserva columnas con cero filas. La agrupación
vacía no produce grupos. En cambio una reducción global de cero filas puede
producir una fila con conteo/suma cero: la forma depende del contexto.

</details>

## Extensión opcional: 40 filas con claves nuevas

Genera una fuente nueva y concíliala sin imponerle los resultados de seis filas.
Cada fila sigue siendo un crédito/corte. Hay 20 créditos, dos cortes y 40 filas.
La fórmula determina los saldos; no hay azar ni necesidad de otro archivo propio.

<details>
<summary>Solución razonada: crear una carpeta nueva y comparar</summary>

Este bloque es autónomo; ejecútalo desde la raíz. Cambia el nombre de destino
si ya existe; no borres evidencia anterior para reutilizarlo.

```python
from pathlib import Path
import sys

carpeta = Path("curriculum/10_polars_duckdb/02_polars_tables_expressions").resolve()
sys.path.insert(0, str(carpeta))
from tablas_polars import (
    referencia, cargar_tabla, seleccionar, resumir_por_corte,
    comprobar_seleccion, comprobar_resumen,
)

destino = Path("output/lab_10_02_escala")
destino.mkdir(parents=True, exist_ok=False)
fuente = destino / "escala.csv"
referencia.generar_escala(fuente, creditos=20)
tabla = cargar_tabla(fuente)
assert tabla.shape == (40, 3)
print(comprobar_seleccion(seleccionar(tabla), ruta=fuente))
print(comprobar_resumen(resumir_por_corte(tabla), ruta=fuente))
```

Septiembre suma 26030 y octubre 27690 MXN, 20 observaciones en cada corte.
Octubre ≥ 2000 elige seis IDs (`015`–`020`) y suma 14061 MXN.
La referencia se vuelve a construir desde **esta fuente**, no desde la muestra
predeterminada. La fórmula es `(j * 137 + mes * 83) % 5001`, con `j=0..19`
y `mes=0/1`; los IDs van de `001` a `020` en ambos cortes.
Duplicar filas enteras violaría la clave; generar IDs distintos conserva el contrato.
Esta escala enseña exploración, no sustenta una conclusión de rendimiento.

</details>

## Evidencia, reflexión y salida

Conserva tu script, versión/intérprete, escenarios conciliados, rechazo observado
y una explicación breve de los tipos. No basta una captura del total correcto.

- ¿Qué cambia en las filas/columnas con `select`, `with_columns`, `filter` y `agg`?
- ¿Por qué el resumen debe partir de toda la tabla y no de octubre ya filtrado?
- ¿Por qué convertir a Int64 después de sumar podría llegar demasiado tarde?
- ¿Qué pierde una comprobación que solo mira el total? ¿Qué prueba un vacío?
- ¿Por qué `saldo_miles_mxn` no sustituye los pesos enteros para conciliar dinero?

Criterio de salida: explicas contextos, unidades y esquema, ejecutas desde sesión
nueva y detectas el error compensado sin alterar entradas. La extensión no bloquea
avanzar. No existe proyecto/checkpoint implementado asociado; el material no
acredita aprendizaje sin tu evidencia.

Siguiente: [10.03 — Polars lazy y planes de consulta](../../../curriculum/10_polars_duckdb/03_polars_lazy_plans/README.md).
Vuelve a la
[lección 10.02](../../../curriculum/10_polars_duckdb/02_polars_tables_expressions/README.md)
para referencias y explicaciones.

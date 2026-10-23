# Lab 10.05 — Lotes, sink y memoria observada

## Propósito y entradas

Extensión **opcional** de la
[lección 10.05](../../../curriculum/10_polars_duckdb/05_streaming_memory/README.md).
Aprender a distinguir procesamiento por lotes, salida materializada, escritura
y memoria observada. No necesitas entregas de otras lecciones ni provocar falta
de RAM. Python con Polars 2.0.0 basta; revisa los
[recorridos](../../../curriculum/10_polars_duckdb/05_streaming_memory/recorridos.md).

El [CSV propio](../../../curriculum/10_polars_duckdb/05_streaming_memory/muestra.csv)
contiene todos estos datos:

| ID textual | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Unidad crédito/corte; clave ID/fecha única. ID de tres dígitos, fecha válida
1900–2100, saldo entero 0–2147483647 MXN, sin ausencias. Se valida la fuente
entera antes del filtro. Conserva los originales y elige carpetas nuevas bajo
`output/`. Los conteos y sumas son controles adicionales a comparar cada par.

## Actividad

1. Predice pares, conteos y sumas de octubre ≥ 2000, octubre ≥ 0, septiembre
   ≥ 2000 y noviembre ≥ 2000. Distingue la unidad de un lote de la de un corte.
2. Prepara tu propio Parquet. Para octubre ≥ 0, consume todos los lotes con
   tamaños pedidos de una y dos filas; no los guardes en una lista. Comprueba
   total de registros y saldo, anotando tamaños reales recibidos.
3. Escribe esa selección con sink en una carpeta nueva. Relee desde otro
   proceso y comprueba tipos y cada par contra la referencia CSV externa.
   Repite septiembre y noviembre, con sus propios destinos.
4. Lee plan lógico y DOT físico. Señala scan, filtro, proyección y flujo hacia
   la salida. Añade una ordenación al plan y revisa su nodo; no concluyas RAM
   acotada ni fallback solo por el nombre de una operación.
5. En una copia, duplica una fila de septiembre. La consulta selectiva de
   octubre puede seguir dando los mismos valores; demuestra que la auditoría
   completa la rechaza. Altera después los dos saldos de una salida de
   septiembre a 2100/2400 y comprueba que la misma suma no supera la verificación.
6. Si eliges observar memoria, usa procesos nuevos para collect+escritura y
   sink. Lee métrica, bytes, alcance y controles; revisa sus trazas. Explica
   por qué no puedes atribuir el pico solo a la consulta ni inferir un ganador.
7. Guarda script, versiones, planes anotados y comprobaciones. El registro de
   memoria puede marcar no disponible en una plataforma no contemplada; no lo
   interpretes como consumo cero. No necesitas generar grandes volúmenes.

## Resultado esperado y comprobación

| Consulta | Pares ID/saldo | Registros | Suma MXN |
| --- | --- | ---: | ---: |
| Octubre ≥ 2000 | 003/2600 | 1 | 2600 |
| Octubre ≥ 0 | 001/100, 002/1900, 003/2600 | 3 | 4600 |
| Septiembre ≥ 2000 | 002/2000, 003/2500 | 2 | 4500 |
| Noviembre ≥ 2000 | Ninguno | 0 | 0 |

Selección String/Int32, incluso vacía `(0, 2)`. Cambiar el tamaño pedido de
lote no debe cambiar los pares finales ni su suma. No se exige un texto DOT
literal, un número fijo de lotes para cualquier versión ni un pico universal
de memoria. Las cuatro consultas se concilian con todos los valores esperados.

<details>
<summary>Solución razonada: lotes, sink y errores detectados</summary>

Desde la raíz, en un script Python con el entorno seleccionado:

```python
from datetime import date
from pathlib import Path
import sys
import polars as pl

modulos = Path("curriculum/10_polars_duckdb/05_streaming_memory").resolve()
sys.path.insert(0, str(modulos))
import streaming_polars as m

carpeta = Path("output/streaming_1005_lab")
carpeta.mkdir(parents=True, exist_ok=False)
entrada = m.preparar(carpeta / "entrada")
consulta = m.consultar(entrada, minimo=0)
for filas_lote in [1, 2]:
    control = m.recorrer_lotes(consulta, filas_lote)
    print("Tamano pedido y control:", filas_lote, control)
    assert control["registros"] == 3
    assert control["saldo_mxn"] == 4600

for nombre, corte, minimo, pares in [
    ("octubre", date(2026, 10, 31), 2000, [("003", 2600)]),
    ("octubre_todos", date(2026, 10, 31), 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    ("septiembre", date(2026, 9, 30), 2000, [("002", 2000), ("003", 2500)]),
    ("noviembre", date(2026, 11, 30), 2000, []),
]:
    entrega = m.ejecutar(entrada, carpeta / nombre, corte=corte, minimo=minimo)
    tabla = pl.read_parquet(entrega["salida"])
    assert tabla.sort("id_credito").rows() == pares
    assert dict(tabla.schema) == {"id_credito": pl.String, "saldo_mxn": pl.Int32}
    m.verificar(entrega["salida"], entrada, corte=corte, minimo=minimo)

ordenada = consulta.sort("id_credito")
dot = ordenada.show_graph(engine="streaming", plan_stage="physical", raw_output=True, show=False)
(carpeta / "plan_ordenacion.dot").write_text(dot, encoding="utf-8")
print(dot)

original = pl.read_parquet(entrada)
entrada_error = carpeta / "entrada_duplicada.parquet"
pl.concat([original, original.head(1)]).write_parquet(entrada_error)
assert m.consultar(entrada_error).collect(engine="streaming").rows() == [("003", 2600)]
try:
    m.ejecutar(entrada_error, carpeta / "no_entrega")
except ValueError:
    print("Rechazo esperado: clave repetida fuera del filtro")
else:
    raise AssertionError("Debio rechazar la fuente")
assert not (carpeta / "no_entrega").exists()

compensada = carpeta / "septiembre_compensado.parquet"
pl.DataFrame({"id_credito": ["002", "003"], "saldo_mxn": [2100, 2400]},
             schema={"id_credito": pl.String, "saldo_mxn": pl.Int32}).write_parquet(compensada)
try:
    m.verificar(compensada, entrada, corte=date(2026, 9, 30))
except ValueError:
    print("Rechazo esperado: pares distintos con igual suma")
else:
    raise AssertionError("Debio rechazar la salida")
assert pl.read_parquet(entrada).equals(original)
```

Se ejecuta varias veces para comparar formas de consumo y errores; no es una
medición de un pipeline único. El control por lotes no conserva todos los IDs,
pero la verificación externa compara cada par. La auditoría completa sí
materializa datos, por lo que no acredita memoria acotada para todo el recorrido.

Para verificar desde un proceso nuevo con tu entorno activo, en la terminal:

```text
python -X utf8 curriculum/10_polars_duckdb/05_streaming_memory/streaming_polars.py verificar output/streaming_1005_lab/octubre_todos/seleccion.parquet output/streaming_1005_lab/entrada/muestra.parquet --minimo 0
```

Con uv usa `uv run --locked python -X utf8` en lugar de `python -X utf8`.
Solo lee; no reescribe el archivo para «arreglarlo».

</details>

<details>
<summary>Solución razonada: observación de memoria y otra escala opcional</summary>

Continuación del script anterior:

```python
from observar_memoria import observar

registros = observar(entrada, carpeta / "memoria", minimo=0)
for registro in registros:
    print(registro)
    assert registro["control"]["saldo_mxn"] == 4600
    assert registro["control"]["registros"] == 3
```

Se crean procesos nuevos y archivos collect/sink: JSON con métrica/alcance,
log de ejecución y Parquet conciliado. En Windows, `PeakWorkingSetSize` informa
bytes de máximo residente del proceso. No es la memoria privada ni la memoria
exclusiva del filtro. La auditoría está en el padre; la escritura está en ambos
trabajadores. Una diferencia entre dos picos no prueba ahorro general.

No se activa `POLARS_VERBOSE` globalmente. Una línea `total memory` del log
puede referirse a memoria disponible para el motor; usa la métrica del JSON
para el pico observado del proceso y explica qué incluye.

Para otra escala, sin repetir claves ni modificar muestras:

```python
fuente_40 = carpeta / "escala_40.csv"
m.referencia.generar_escala(fuente_40, creditos=20)
entrada_40 = m.preparar(carpeta / "entrada_40", fuente_40)
escala = m.ejecutar(entrada_40, carpeta / "salida_40", fuente_40)
assert escala["control"]["registros"] == 6
assert escala["control"]["saldo_mxn"] == 14061
```

Son 20 créditos × dos cortes, no 40 créditos. El generador está incluido y
es determinista; la referencia externa se reconstruye desde este nuevo CSV.
No requiere que hayas realizado su lección original. Puedes elegir 200
créditos para 400 filas, conservando destinos nuevos. No se demuestra con estas
escalas que un archivo mayor que la RAM se procese con recursos suficientes.

</details>

## Evidencia y reflexión

Conserva script, versiones, planes anotados, controles y relectura. Si observaste
memoria, añade JSON/log y una interpretación de unidad/alcance, sin un ranking.

- ¿Por qué collect sigue materializando toda la salida si el motor es streaming?
- ¿Qué cambiaría al guardar todos los lotes en una lista?
- ¿Qué estado crece al agrupar por más claves distintas?
- ¿Por qué sink no elimina los requisitos de una ordenación anterior?
- ¿Qué diferencia hay entre plan físico, traza y pico residente?
- ¿Qué parte de nuestro verificador sí materializa toda la entrada?

Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md).
El proyecto `04_large_credit_dataset` y sus checkpoints siguen pendientes.

Siguiente: [10.06 — DuckDB: SQL sobre Parquet](../../../curriculum/10_polars_duckdb/06_duckdb_parquet/README.md).
Vuelve a la
[lección 10.05](../../../curriculum/10_polars_duckdb/05_streaming_memory/README.md)
para revisar conceptos; esta extensión no bloquea esa continuación esencial.

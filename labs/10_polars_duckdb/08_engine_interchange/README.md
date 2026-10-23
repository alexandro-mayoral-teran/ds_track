# Lab 10.08 — Comprobar cada frontera

## Propósito y entradas

Intercambiar una tabla entre pandas, Arrow, Polars y DuckDB conservando claves,
tipos lógicos y valores. La [lección](../../../curriculum/10_polars_duckdb/08_engine_interchange/README.md)
incluye preparación de entorno y todos los conceptos. No necesitas entregas
anteriores: el CSV incluido tiene los siguientes registros de una financiera ficticia.

| ID | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

ID textual de tres dígitos, Date 1900–2100, saldo entero 0–2147483647,
sin ausencias y clave ID/corte única. Una incidencia rechaza la fuente completa.
Por corte hay tres registros y 4500/4600 MXN; no sumes cortes para presentar
saldo a una fecha única. Usa Python desde la raíz del repositorio.

## Actividad

1. Predice los pares de los cuatro casos de abajo. Ejecuta el recorrido integrado
   y registra esquema/ausencias de cada etapa, además del resultado filtrado.
2. Localiza en el código el registro de fuente, la relación SQL y las
   materializaciones a Arrow/Polars/pandas. Marca qué objetos dependen de una
   conexión abierta y cuáles ya contienen los resultados.
3. Explica por qué se acepta string/large_string y por qué el verificador
   rechaza float64 para el saldo, aun con valores que parecen enteros.
4. Ejecuta la muestra anulable independiente: IDs 001/002/003, importes
   0/ausencia/10 y etiquetas vacío/ausencia/café. Comprueba suma observada 10,
   cobertura 2/3 y conservación del vacío frente a ausencia.
5. Cierra Python, abre otra sesión y ejecuta el script completo. No uses un
   objeto que quedó en memoria para reconstruir la referencia externa.

| Corte | Umbral | Pares esperados |
| --- | ---: | --- |
| 2026-10-31 | 2000 | 003/2600 |
| 2026-09-30 | 2001 | 003/2500 |
| 2026-10-31 | 0 | 001/100, 002/1900, 003/2600 |
| 2026-11-30 | 2000 | ninguno |

## Comprobación y solución razonada

<details>
<summary>Recorrido completo y salida vacía</summary>

```python
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/08_engine_interchange").resolve()))
import intercambio

casos = [
    ("2026-10-31", 2000, [("003", 2600)]),
    ("2026-09-30", 2001, [("003", 2500)]),
    ("2026-10-31", 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    ("2026-11-30", 2000, []),
]
for corte, minimo, pares in casos:
    x = intercambio.ejecutar(corte=date.fromisoformat(corte), minimo=minimo)
    assert [(f["id_credito"], f["saldo_mxn"]) for f in x["seleccion"]] == pares
    assert [f[2] for f in x["resumen"]] == ["4500", "4600"]
    assert x["etapas"]["seleccion_arrow"]["filas"] == len(pares)
    print(corte, x["control"], x["dtypes_pandas"])

anulable = intercambio.ejemplo_anulable()
assert (anulable["suma_observada"], anulable["observados"], anulable["registros"]) == (10, 2, 3)
assert anulable["valores"][0]["etiqueta"] == ""
assert anulable["valores"][1]["etiqueta"] is None
print(anulable)
```

Noviembre conserva columnas tipadas en Arrow/Polars aunque no tenga filas.
El resumen sigue calculándose sobre toda la fuente. Los tipos y la comparación
por clave se revisan antes de reducir la respuesta a conteo y suma.

</details>

<details>
<summary>Detectar una alteración sin cambiar la suma</summary>

En una sesión Python nueva, desde la raíz:

```python
from pathlib import Path
import sys
import pyarrow as pa
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/08_engine_interchange").resolve()))
import intercambio

esperadas = intercambio.referencia.cargar_filas(intercambio.FUENTE)
tabla = pa.Table.from_pylist(esperadas, schema=intercambio.ESQUEMA)
alteradas = tabla.to_pylist()
alteradas[1]["saldo_mxn"] += 1
alteradas[2]["saldo_mxn"] -= 1
copia = pa.Table.from_pylist(alteradas, schema=intercambio.ESQUEMA)
assert sum(f["saldo_mxn"] for f in alteradas) == sum(f["saldo_mxn"] for f in esperadas)
try:
    intercambio.comprobar_arrow(copia, esperadas)
except ValueError as error:
    print("Alteración detectada:", error)
else:
    raise AssertionError("La comprobación debió rechazar valores distintos")
```

Solo cambió septiembre, fuera del filtro de octubre. La suma coincide, pero
los importes individuales no. Convertir a una lista facilita comparar estos
datos pequeños; materializa valores y no es un método para medir rendimiento.

</details>

## Ampliaciones opcionales

- Repite la demostración del lector de la lección. Explica por qué lote de dos
  filas no garantiza RAM acotada. Cambia su tamaño sin cambiar conteo/valores.
- Comprueba el entero 9007199254740993 con una ausencia en el ejemplo separado;
  explica por qué convertir a entero un float ya aproximado no lo recupera.
- En R, prepara la extensión sin cambiar dependencias y ejecuta el script
  completo desde una sesión nueva. Después de `source("ejecutar_intercambio.R")`,
  ejecuta `ejecutar_1008_r(corte=as.Date("2026-11-30"))`: selección vacía y
  resumen 4500/4600. Identifica dónde DBI recupera un data.frame y dónde vuelve
  a Arrow. No necesitas instalar Polars en R para esta ampliación.

## Evidencia, reflexión y criterio de salida

Conserva script, versiones, tabla de etapas/tipos, pares de los cuatro casos y
resultado de la muestra anulable. Registra reinicio de sesión, incidencia
compensada y explicación de índice, string/large_string y materializaciones.

¿Un DataFrame pandas implica el mismo respaldo de memoria en todas sus columnas?
¿Igualdad de valores implica igualdad de metadatos? ¿Qué tendría que cambiar
en el contrato para aceptar timestamps, categorías o dinero decimal?
¿Qué trabajo vuelve a ocurrir al pedir otra materialización de una relación?

Avanza cuando puedas comprobar tipos y valores de cada frontera y señalar
qué no prueban esas comparaciones sobre copias, RAM o tiempo. No hay checkpoint
activo: el proyecto integrador sigue previsto y el material no acredita práctica.
Siguiente: [10.09 — Comparar tiempo y memoria](../../../curriculum/10_polars_duckdb/README.md#09-comparar-tiempo-y-memoria),
todavía planificada.

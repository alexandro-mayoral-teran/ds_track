# Lab 10.07 — La misma consulta desde Python y R

## Propósito y entradas

Vuelve a la [lección 10.07](../../../curriculum/10_polars_duckdb/07_duckdb_python_r/README.md)
para conceptos y preparación de ambos entornos. Elige primero un cliente y
después contrasta el otro. No necesitas entregas previas: el CSV incluido contiene
estas seis filas y cada recorrido prepara su propio Parquet en carpeta nueva.

| ID | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Clave ID/corte única; ID textual de tres dígitos, Date 1900–2100 y saldo entero
0–2147483647, sin ausencias. Audita la fuente completa antes de filtrar.
Python usa la raíz del repositorio; R usa la copia renv preparada.

## Actividad

1. Escribe los resultados esperados de la tabla de comprobación antes de ejecutar.
2. Abre `seleccion.sql`; identifica los tres parámetros y conserva el mismo SQL
   en los dos clientes. Cambia valores mediante parámetros.
3. Prepara un Parquet propio por cliente, consulta los cuatro casos y compara
   cada par ID/saldo, también cuando no haya filas. Inspecciona clases y versión.
4. Revisa el resumen por fecha: tres filas/4500 y tres/4600. Explica por qué
   `registros_texto` y `saldo_texto` son texto exacto, aunque se calcularon en SQL.
5. Reinicia cada sesión y vuelve a leer su Parquet sin prepararlo de nuevo.
   Comprueba que las salidas coinciden y las fuentes permanecen intactas.

| Corte | Umbral | Pares esperados | Control |
| --- | ---: | --- | --- |
| 2026-09-30 | 2000 | 002/2000, 003/2500 | dos/4500 |
| 2026-09-30 | 2001 | 003/2500 | uno/2500 |
| 2026-10-31 | 0 | 001/100, 002/1900, 003/2600 | tres/4600 |
| 2026-11-30 | 2000 | ninguno | cero/cero |

Octubre ≥ 2000, caso de la lección, debe seguir dejando `003/2600`.
No sumes cortes para presentar saldo a una fecha única.

## Comprobación y solución razonada

<details>
<summary>Python: preparación y todos los pares</summary>

Con el entorno elegido, desde la raíz, en una sesión Python nueva:

```python
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/07_duckdb_python_r").resolve()))
import clientes

archivo = clientes.preparar("output/lab_1007_python")
casos = [
    ("2026-09-30", 2000, [("002", 2000), ("003", 2500)]),
    ("2026-09-30", 2001, [("003", 2500)]),
    ("2026-10-31", 0, [("001", 100), ("002", 1900), ("003", 2600)]),
    ("2026-11-30", 2000, []),
]
for corte, minimo, esperado in casos:
    x = clientes.ejecutar(archivo, corte=date.fromisoformat(corte), minimo=minimo, pagina=1)
    assert x["seleccion"] == esperado
    assert [f[2] for f in x["resumen"]] == ["4500", "4600"]
    print(corte, x["control"], x["version"])
```

En sesión nueva repite los imports y asigna `archivo` a la ruta conservada,
sin llamar a preparar. Ejecuta de nuevo el bucle. El umbral inclusivo conserva
2000; cambiarlo a 2001 excluye ese par. Un vacío válido no es un error de lectura.

</details>

<details>
<summary>R: recorrido completo en el proyecto preparado</summary>

En un script nuevo del proyecto R, después de reiniciar la sesión:

```r
source("R/clientes_1007.R", encoding = "UTF-8")
archivo <- preparar_1007("output/lab_1007_r")
cortes <- as.Date(c("2026-09-30", "2026-09-30", "2026-10-31", "2026-11-30"))
minimos <- c(2000L, 2001L, 0L, 2000L)
ids <- list(c("002", "003"), "003", c("001", "002", "003"), character())
saldos <- list(c(2000L, 2500L), 2500L, c(100L, 1900L, 2600L), integer())
for (i in seq_along(cortes)) {
  x <- ejecutar_1007(archivo, corte = cortes[i], minimo = minimos[i], pagina = 1L)
  stopifnot(identical(x$seleccion$id_credito, ids[[i]]),
    identical(x$seleccion$saldo_mxn, saldos[[i]]),
    identical(x$resumen$saldo_texto, c("4500", "4600")))
  print(x$control)
}
str(x$seleccion)
```

La salida vacía conserva columnas character/integer. En otra sesión ejecuta
el bloque con `archivo` asignado al Parquet existente en vez de preparar otra vez.
La función protege resultado y conexión con `on.exit`; inspecciona ese orden
en el código antes de adaptar sus llamadas.

</details>

## Ampliación: cruzar archivos y comprobar errores

Sin cambiar el archivo SQL, pasa el Parquet escrito por R a `clientes.ejecutar`
en Python y el escrito por Python a `ejecutar_1007` en R. Usa rutas absolutas
con `/`, porque las carpetas de trabajo son distintas. Ambos CSV originales
representan la misma fuente. Comprueba `003/2600` y el resumen exacto.
No compartas una base DuckDB persistente entre versiones diferentes.

En copias nuevas, intenta pasar fecha textual a la función R, umbral negativo
o página cero: deben rechazarse. Si una copia de Parquet cambia dos saldos
compensándose, o añade un duplicado de septiembre, la auditoría debe fallar
aunque la selección de octubre o la suma total sigan iguales. Nunca edites
la fuente externa para ocultar una alteración. Cambiar SQL para solicitar una
columna inexistente debe fallar; liberar recursos también pertenece al caso de error.

Recuperar páginas y acumularlas en una lista/data.frame no acredita memoria
acotada. No conviertas un tiempo aislado en comparación de rendimiento.

## Evidencia, reflexión y criterio de salida

Conserva consulta, versiones efectivas, rutas relativas de tus entregas,
pares de los cuatro casos, tipos SQL/clases nativas y resumen. Registra cómo
reiniciaste las sesiones y cómo se cierran resultados/conexiones. Si realizaste
la ampliación, añade las lecturas cruzadas y el error detectado.

Explica: ¿qué pertenece al motor y qué al cliente?, ¿por qué parámetros en vez
de concatenación?, ¿qué perderías al convertir HUGEINT a numeric antes de texto?,
¿por qué las páginas no bastan para afirmar RAM acotada?

Avanza cuando puedas recuperar la misma respuesta desde ambos clientes,
explicar las representaciones y demostrar el vacío tipado. No hay checkpoint
activo; desarrollar el material no acredita que hayas realizado la práctica.
Siguiente: [10.08 — Intercambio entre motores](../../../curriculum/10_polars_duckdb/README.md#08-intercambio-entre-motores),
todavía planificada.

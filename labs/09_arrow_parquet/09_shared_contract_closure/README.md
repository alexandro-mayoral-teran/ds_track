# Lab 09.09 — Entregar y comprobar el contrato compartido

## Propósito y entradas

Cerrar [09.09 — Contrato compartido](../../../curriculum/09_arrow_parquet/09_shared_contract_closure/README.md)
con evidencia propia. No requiere entregas personales de otras secciones ni
particiones de 09.08. Necesita los entornos y el preparador indicados en la
lección; no instala bibliotecas.

La fuente incluida tiene 28 registros, 14 IDs, dos cortes y columnas físicas
`string/date32/int32` no anulables. Clave ID/fecha, pesos enteros no negativos;
septiembre: 14/29 000 MXN; octubre: 14/31 800. Consulta octubre ≥ 2000:
nueve pares ID/importe, 24 100 MXN. Los datos y reglas están completos en la
lección. Puedes comenzar por su muestra autónoma de cuatro filas antes de
construir la entrega común.

## Actividad 1 — Reconstrucción y lectura cruzada

1. Crea `python_lab/` y `r_lab/` con las funciones del capítulo, cada una
   reconstruida desde el CSV incluido, sin copiar la entrega del otro lenguaje.
2. Inspecciona contrato, resumen, selección y lista de archivos/huellas.
3. Reinicia ambas sesiones. Verifica ambas carpetas desde Python y ambas desde R.
4. Explica qué comparación comprueba bytes y cuál comprueba cada clave/valor.
5. Intenta crear otra vez en el mismo destino: debe rechazarse conservando la entrega.
6. Reconstruye otra vez en carpetas nuevas con sufijo `_reconstruido` y comprueba
   sus valores. No exijas iguales huellas entre archivos escritos por distintos
   lenguajes ni una versión de escritor idéntica para aceptar el contrato.

<details>
<summary>Una solución razonada: crear, reiniciar y verificar</summary>

**Python**, desde la raíz de DS Track y el intérprete elegido:

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/09_arrow_parquet/09_shared_contract_closure").resolve()))
import cierre_contrato as curso

compartida = Path("output/09_09_cierre").resolve()
print(curso.crear_entrega(compartida / "python_lab"))
print(curso.crear_entrega(compartida / "python_lab_reconstruido"))
try:
    curso.crear_entrega(compartida / "python_lab")
except FileExistsError:
    print("Entrega original conservada")
else:
    raise AssertionError("Se acepto un destino ocupado")
```

**R**, desde la raíz del proyecto preparado:

```r
source("cierre_contrato.R", encoding = "UTF-8")
compartida <- readLines("ruta_cierre_0909.txt", encoding = "UTF-8")
print(crear_entrega_cierre_r(file.path(compartida, "r_lab")))
print(crear_entrega_cierre_r(file.path(compartida, "r_lab_reconstruido")))
error <- tryCatch({crear_entrega_cierre_r(file.path(compartida, "r_lab")); NULL},
  error = function(e) e)
stopifnot(inherits(error, "error"))
```

Ahora reinicia Python, carga los mismos imports/módulo y define `compartida`.
Sin crear ni copiar carpetas:

```python
for nombre in ["python_lab", "r_lab", "python_lab_reconstruido", "r_lab_reconstruido"]:
    resultado = curso.verificar_entrega(compartida / nombre)
    assert resultado["cartera"]["registros"] == 28
    assert resultado["seleccion"] == {"registros": 9, "saldo_mxn": 24100}
    print(nombre, resultado)
```

Reinicia R, carga `cierre_contrato.R` y lee la ruta local del TXT. Solo lectura:

```r
for (nombre in c("r_lab", "python_lab", "r_lab_reconstruido", "python_lab_reconstruido")) {
  resultado <- verificar_entrega_cierre_r(file.path(compartida, nombre))
  stopifnot(identical(resultado$cartera$saldo_mxn, c(29000, 31800)),
    resultado$seleccion$registros == 9L, resultado$seleccion$saldo_mxn == 24100)
  print(resultado)
}
```

Cada lector reconstruye su referencia desde la fuente incluida. No usa el
resumen escrito por el otro como única prueba. Los scripts y funciones se
pueden volver a cargar sin crear archivos al importar/hacer `source()`.

</details>

## Actividad 2 — Detectar una exportación incorrecta

1. Copia una entrega completa en otra carpeta nueva, `copia_error_python/` o
   `copia_error_r/`. No edites las originales.
2. En la copia, cambia los dos primeros saldos de `seleccion.csv` en +1 y −1.
   Conserva número de filas, IDs y suma total; verifica que los importes sigan
   siendo no negativos. Los Parquet permanecen intactos.
3. Ejecuta el verificador: debe detectar que el archivo cambió frente a sus huellas.
4. Solo en esa copia de diagnóstico, vuelve a registrar las huellas actuales.
   Ejecuta otra vez: debe rechazar los valores de la selección aunque las
   huellas coincidan y la suma siga dando 24 100.
5. Comprueba también esa copia desde el otro lenguaje. El rechazo no depende
   de que el escritor original y el lector usen la misma API.
6. Verifica de nuevo ambas entregas originales. Deben seguir válidas.

<details>
<summary>Una solución razonada: dos capas de comprobación</summary>

**Python**, con los imports y la ruta de la actividad 1:

```python
import csv
import shutil

copia = compartida / "copia_error_python"
shutil.copytree(compartida / "python_lab", copia)
ruta = copia / "seleccion.csv"
filas = curso.leer_csv(ruta, ["id_credito", "saldo_mxn"])
filas[0]["saldo_mxn"] = str(int(filas[0]["saldo_mxn"]) + 1)
filas[1]["saldo_mxn"] = str(int(filas[1]["saldo_mxn"]) - 1)
with ruta.open("w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["id_credito", "saldo_mxn"])
    escritor.writeheader()
    escritor.writerows(filas)

for actualizar in [False, True]:
    if actualizar:
        # Solo para el experimento sobre la copia; no forma parte del verificador.
        with (copia / "huellas.csv").open("w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["archivo", "bytes", "md5"])
            escritor.writeheader()
            escritor.writerows(curso.huellas(copia))
    try:
        curso.verificar_entrega(copia)
    except ValueError as error:
        print(error)
    else:
        raise AssertionError("La copia alterada fue aceptada")
print(curso.verificar_entrega(compartida / "python_lab"))
```

El primer rechazo pertenece al registro de archivos; el segundo, al contenido
de `seleccion.csv` frente a la referencia independiente. La reescritura de
huellas se limita al experimento: no «repara» la entrega.

**R**, sin depender de la copia alterada Python:

```r
copia <- file.path(compartida, "copia_error_r")
if (file.exists(copia)) stop("Elige una copia nueva")
stopifnot(dir.create(copia))
original <- file.path(compartida, "r_lab")
stopifnot(all(file.copy(list.files(original, full.names = TRUE, all.files = TRUE,
  no.. = TRUE), copia, recursive = TRUE)))
ruta <- file.path(copia, "seleccion.csv")
filas <- leer_csv_cierre(ruta, c("id_credito", "saldo_mxn"))
filas$saldo_mxn[1:2] <- as.character(as.integer(filas$saldo_mxn[1:2]) + c(1L, -1L))
utils::write.csv(filas, ruta, row.names = FALSE, fileEncoding = "UTF-8")
for (actualizar in c(FALSE, TRUE)) {
  if (actualizar) {
    # Solo en la copia del experimento; verificar_entrega_cierre_r nunca escribe.
    utils::write.csv(huellas_cierre_r(copia), file.path(copia, "huellas.csv"),
      row.names = FALSE, fileEncoding = "UTF-8")
  }
  error <- tryCatch({verificar_entrega_cierre_r(copia); NULL}, error = function(e) e)
  stopifnot(inherits(error, "error"))
  print(conditionMessage(error))
}
print(verificar_entrega_cierre_r(original))
```

Después, desde cada lector verifica también la copia creada por el otro y
comprueba su rechazo. No uses `crear_entrega()` para verificar una carpeta
existente ni edites el código del contrato para aceptar el error.

</details>

## Evidencia y criterio de salida

Conserva scripts, carpetas nuevas, versiones, resultados de ambos lectores y
mensajes de rechazo. No publiques salidas de práctica en el repositorio del
curso. Entrega una explicación de cinco a ocho frases que responda:

- ¿Qué significan una fila, la clave y la unidad del saldo?
- ¿Cómo sabes que ambos lenguajes recuperaron los mismos valores y tipos?
- ¿Qué papel cumplen fuente externa, resumen, consulta y huellas?
- ¿Por qué una huella distinta entre Python y R no demuestra una diferencia de datos?
- ¿Por qué conservar la suma no basta y actualizar huellas no corrige valores?
- ¿Qué recuperaste desde archivos después de reiniciar? ¿Qué quedó fuera de alcance?

Criterio de salida: reconstrucción propia, cuatro combinaciones escritor/lector
comprobadas desde sesiones nuevas, copia alterada rechazada y originales
intactos. Eso acredita esta práctica cuando aportes su evidencia; disponer de
las nueve lecciones no acredita haberlas cursado.

No hay proyecto/checkpoint activo asociado: `04_large_credit_dataset` sigue
planificado. Siguiente: [10.01 — Pregunta, contrato y referencia](../../../curriculum/10_polars_duckdb/README.md#01-pregunta-contrato-y-referencia),
todavía planificada. Consulta los [pendientes de integración](../../../docs/storage-closure.md).

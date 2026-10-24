# 10.10 — Cierre y elección de herramienta

## Propósito y prerrequisitos

Resolver una pregunta con pandas, Polars y DuckDB, reconstruir las respuestas
desde archivos y justificar una elección con evidencia y límites. Elegir exige
relacionar la herramienta con quien revisará el trabajo, el entorno y los costos
observados; una mediana menor no decide por sí sola.

Necesitas reconocer tablas, tipos, filtros, agrupaciones y ejecución diferida.
Puedes profundizar en [contratos](../01_question_contract_reference/README.md),
[tipos/uniones](../04_types_missing_joins/README.md),
[clientes](../07_duckdb_python_r/README.md),
[conversiones](../08_engine_interchange/README.md) y
[mediciones](../09_time_memory/README.md). Aquí se presentan contexto, datos,
reglas y resultados completos. Reutilizamos funciones incluidas, sin pedir
entregas personales anteriores ni instalar herramientas para el siguiente módulo.

**Práctica de cierre:** entrega técnica y decisión explicada. R base ofrece
una referencia independiente opcional; streaming y Polars en R no bloquean
este cierre. No hay proyecto/checkpoint activo ni acreditación automática.

## Objetivos

- Resolver la misma selección y resumen con tres motores.
- Conservar claves, fechas, pesos enteros y resultados al escribir/releer.
- Reconstruir la referencia externa y detectar errores aun con sumas iguales.
- Justificar una herramienta por claridad, entorno y costos de alcance conocido.
- Distinguir evidencia técnica, revisión humana y desarrollo del material.

## 1. Contexto y diccionario completos

Una financiera ficticia registra veinte créditos en dos cortes. La persona que
revisará la entrega quiere **los créditos con saldo ≥ 2000 MXN el 31 de octubre
de 2026**, el importe seleccionado y un resumen de **cada corte completo**.
Necesita tablas verificables y una nota que explique cómo se producirían otra vez.

| Columna | Significado y contrato |
| --- | --- |
| id_credito | Texto de tres dígitos; conserva ceros iniciales |
| fecha_corte | Date válido, 1900–2100; fecha sin hora ni zona |
| saldo_mxn | Saldo a ese corte, entero 0–2147483647 MXN |

Unidad crédito/corte y clave compuesta ID/fecha única. No se admiten ausencias,
negativos ni claves repetidas. Una incidencia rechaza la fuente completa, incluso
fuera del filtro; no se imputan ceros ni se elimina una aparición duplicada.
Esta entrega didáctica admite hasta 1998 filas para mantener las cotas de sus
agregados. No demuestra grandes volúmenes o procesamiento mayor que memoria.

### Muestra mínima para entender la frontera

Estas seis observaciones son un ejemplo completo por sí mismas, antes de pasar
a la muestra de veinte créditos:

| ID | Corte | Saldo MXN |
| --- | --- | ---: |
| 014 | 2026-09-30 | 1781 |
| 015 | 2026-09-30 | 1918 |
| 016 | 2026-09-30 | 2055 |
| 014 | 2026-10-31 | 1864 |
| 015 | 2026-10-31 | 2001 |
| 016 | 2026-10-31 | 2138 |

Octubre ≥ 2000 deja 015/2001 y 016/2138: dos/4139. Si subes el umbral a
2002, queda 016/2138. El resumen completo de esta mini muestra es tres/5754
en septiembre y tres/6003 en octubre. El resumen usa todos los registros del
corte; no confundirlo con el subtotal seleccionado.

Ejemplo Python autónomo, sin motores ni archivos de otra sección:

```python
from datetime import date
filas = [
    ("014", date(2026, 9, 30), 1781), ("015", date(2026, 9, 30), 1918),
    ("016", date(2026, 9, 30), 2055), ("014", date(2026, 10, 31), 1864),
    ("015", date(2026, 10, 31), 2001), ("016", date(2026, 10, 31), 2138),
]
pares = sorted((id_, saldo) for id_, corte, saldo in filas
               if corte == date(2026, 10, 31) and saldo >= 2000)
assert pares == [("015", 2001), ("016", 2138)]
assert sum(saldo for _, saldo in pares) == 4139
```

### Muestra propia de cierre: todos sus valores

[muestra.csv](muestra.csv) contiene las cuarenta filas en formato largo. Esta
tabla muestra exactamente sus valores en formato ancho, uno por crédito:

| ID | Saldo 2026-09-30 | Saldo 2026-10-31 |
| --- | ---: | ---: |
| 001 | 0 | 83 |
| 002 | 137 | 220 |
| 003 | 274 | 357 |
| 004 | 411 | 494 |
| 005 | 548 | 631 |
| 006 | 685 | 768 |
| 007 | 822 | 905 |
| 008 | 959 | 1042 |
| 009 | 1096 | 1179 |
| 010 | 1233 | 1316 |
| 011 | 1370 | 1453 |
| 012 | 1507 | 1590 |
| 013 | 1644 | 1727 |
| 014 | 1781 | 1864 |
| 015 | 1918 | 2001 |
| 016 | 2055 | 2138 |
| 017 | 2192 | 2275 |
| 018 | 2329 | 2412 |
| 019 | 2466 | 2549 |
| 020 | 2603 | 2686 |

Son valores sintéticos deterministas: para j=0..19, ID=j+1 con tres dígitos,
saldo `137*j + 83*mes`, mes 0/1. No son observaciones reales ni una muestra
estadística de clientes.

**Respuesta de cierre:** octubre ≥ 2000 deja 015/2001, 016/2138, 017/2275,
018/2412, 019/2549 y 020/2686: **seis créditos/14061 MXN**.
Septiembre ≥ 2000 deja 016–020: cinco/11645. Octubre ≥ 2002 excluye 015:
cinco/12060. Octubre ≥ 0 deja veinte/27690; noviembre no tiene registros.

| Corte completo | Registros | Saldo MXN |
| --- | ---: | ---: |
| 2026-09-30 | 20 | 26030 |
| 2026-10-31 | 20 | 27690 |

Sumar fechas distintas no produce saldo a una fecha única. El incremento de
1660 MXN en esta muestra describe sus dos totales; no prueba causalidad.

## 2. Qué debe entregar cada alternativa

Todos reciben el mismo Parquet generado del CSV validado. Producen selección
ordenada por ID y resumen por fecha, sin índice artificial en columnas:

| Resultado | Tipos lógicos exigidos |
| --- | --- |
| Selección | ID textual; saldo individual Int32 |
| Resumen | Date; conteo Int64; suma Int64 |

pandas usa tipos Arrow y amplía saldo a Int64 **antes** de agrupar/sumar.
Polars hace scan, expresiones y collect; también amplía antes de agregar.
DuckDB usa SQL parametrizado y recupera Arrow, con SUM en el motor y adaptación
a BIGINT. La cota de 1998 saldos Int32 suma como máximo 4290672326706 MXN,
por debajo de Int64 y de 2^53: justifica la conversión para esta entrega.
No sería una política universal para otras bases.

Se inspeccionan tipos antes de convertir a registros para comparar. string y
large_string se admiten como representación textual de los mismos IDs;
no se aceptan float en lugar de entero, timestamps en lugar de Date o saldos
intercambiados que preserven la suma. La marca de anulabilidad/metadatos puede
diferir entre motores; se comprueba también que no haya ausencias reales.

La lectura completa se audita contra CSV externo antes de filtrar. Después
de escribir, se releen **ambos Parquet por motor** y se comparan cada par y cada
grupo con Python estándar. La fuente puede llegar en otro orden; la selección
guardada debe quedar por ID y el resumen por fecha, como exige esta entrega.
Esto comprueba los archivos guardados, no solo objetos
de una sesión. Conserva fuentes sin cambios durante el recorrido; no ofrece
instantánea frente a modificaciones concurrentes ni RAM acotada para la auditoría.

## 3. Preparar una entrega independiente

Versiones ejecutadas: Python 3.12.12, pandas 2.3.3, PyArrow 21.0.0,
Polars 2.0.0 y DuckDB 2.0.0, ya declarados en
[pyproject.toml](../../../pyproject.toml)/[uv.lock](../../../uv.lock).
No hay dependencias nuevas. Comprueba el entorno en los [recorridos](recorridos.md).
Prepararlo es distinto de necesitar resultados personales de lecciones previas.

Desde la raíz de DS Track en un script/consola Python:

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/10_closure_tool_choice").resolve()))
import cierre

entrega = Path("output/cierre_1010")
x = cierre.generar(entrega, nota="Anotar disco, carga y energia conocidos del equipo")
assert (x["control"]["registros"], x["control"]["saldo_mxn"]) == (6, 14061)
assert [f["saldo_mxn"] for f in x["resumen"]] == [26030, 27690]
assert x["decision"] == "borrador"
print(x)
```

[cierre.py](cierre.py) crea una carpeta exclusiva. Si existe, se detiene;
repetir requiere otro nombre, sin borrar la entrega anterior. Si falla un paso,
conserva carpeta parcial/logs para revisar. La decisión empieza en borrador
porque generar evidencia técnica no redacta ni aprueba tu argumento.

```text
cierre_1010/
  fuente.csv, contrato.json, manifiesto.json
  datos/entrada.parquet
  pandas/seleccion.parquet, resumen.parquet
  polars/seleccion.parquet, resumen.parquet
  duckdb/seleccion.parquet, resumen.parquet
  comparacion.json
  mediciones/                 # crudas, informe, logs y exportaciones
  decision.json              # completar por quien realiza la practica
```

## 4. Costos: evidencia nueva y alcance acotado

La generación ejecuta tres repeticiones por motor, nueve procesos nuevos y
orden rotado, usando el protocolo incluido de 10.09 sobre **este Parquet y
esta pregunta**. No copia mediciones de otra lección. Conserva versiones,
configuración, equipo/notas, caché sin vaciar, fases y pico residente disponible.
La fuente se leyó durante la auditoría previa; proceso nuevo no significa disco frío.

**Los tiempos miden selección ordenada/adaptación/exportación JSON del protocolo
10.09.** No miden el resumen por corte ni la escritura de todos los Parquet,
la auditoría o la construcción completa de esta entrega. Las funciones de cierre
comprueban más resultados; no les atribuyas los tiempos de otro alcance.
Lee consulta_ns, intervalo_ns y proceso_ns con sus definiciones, y conserva
mediana/rango. El pico es del proceso hasta el contador, no memoria exclusiva
del motor; no acredita I/O físico, disco frío o procesamiento mayor que memoria.

Para depurar resultados puedes generar con `con_mediciones=False`; esa variante
no completa la evidencia de costos y no puede pasar `exigir_decision=True`.
La entrega esencial usa mediciones nuevas. Para medir el flujo completo haría
falta otro experimento con fronteras equivalentes y controles nuevos.

## 5. Elegir: requisitos, alternativas y decisión revisable

Primero define restricciones reales. Luego compara alternativas que ya
conciliaron. Elige con razones que otra persona pueda revisar:

| Criterio | Pregunta concreta |
| --- | --- |
| Claridad | ¿Quien mantendrá el análisis puede explicar y revisar este código? |
| Entorno | ¿Qué versiones y clientes están disponibles en su entorno elegido? |
| Costos | ¿Qué trabajo se midió y qué rango tuvo con esta entrada/configuración? |
| Escala y forma | ¿Cabe la tarea observada? ¿Necesita SQL, expresiones o conversiones? |
| Límites | ¿Qué no se probó y qué cambio obligaría a medir/revisar otra vez? |

Ejemplo razonado con **contexto ficticio explícito**: una persona ya revisa pandas,
trabaja con estas cuarenta filas y necesita tablas para un reporte local. Puede
elegir pandas por legibilidad y continuidad del entorno, aceptando el costo de
esa lectura pequeña. Debe citar el rango observado en su corrida y explicar que
el resumen completo no fue medido. No necesita declarar que pandas fue más rápido.

Si el equipo revisa principalmente SQL sobre archivos, DuckDB puede hacer más
clara la entrega. Si mantiene un flujo de expresiones/planes Polars, conservarlo
puede reducir conversiones. Son razones condicionales: aquí no probamos un
servicio concurrente, una base mayor que RAM ni los costos de otro despliegue.
La evidencia de tiempo ayuda a decidir; no reemplaza requisitos o mantenibilidad.

Abre `decision.json` en tu editor. Completa motor_elegido, contexto, claridad,
entorno, costos, limites y cuando_cambiaria; conserva el alcance escrito por
el programa y cambia estado a documentada cuando redactes la explicación.
El [lab](../../../labs/10_polars_duckdb/10_closure_tool_choice/README.md) contiene
una solución cerrada que incorpora cifras de la corrida recién ejecutada.

## 6. Reconstruir desde otra sesión

Reinicia Python y ejecuta este bloque completo desde la raíz, sin generar de nuevo:

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/10_closure_tool_choice").resolve()))
import cierre

revision = cierre.verificar("output/cierre_1010")
assert revision["control"]["saldo_mxn"] == 14061
print(revision)
```

El verificador solo lee: reconstruye fuente, contrato, esquema/valores guardados,
comparación y mediciones. No acepta una selección alterada solo porque coincida
su suma; tampoco basta actualizar las huellas. SHA-256 identifica contenido,
no autentica quién escribió los archivos o duraciones pasadas.

Después de completar la decisión, usa `cierre.verificar(entrega, exigir_decision=True)`.
Exige mediciones verificadas, motor válido, estado documentada y campos no vacíos.
Eso verifica **estructura y evidencia técnica**, no que el argumento sea bueno:
una persona debe discutir la pregunta, los costos y los límites contigo.

`decision.json` no se incluye en las huellas del manifiesto porque se completa
después; su estructura y alcance sí se revisan. Las mediciones tienen comprobación
propia de crudas/pares/fases; no certifican autenticidad histórica.

### Ampliación R base independiente

No requiere nuevas bibliotecas ni un proyecto renv ampliado. En RStudio/IDE,
con la raíz de DS Track como carpeta de trabajo, abre un script nuevo y ejecuta:

```r
source("curriculum/10_polars_duckdb/10_closure_tool_choice/referencia.R", encoding = "UTF-8")
r <- referencia_cierre()
stopifnot(identical(r$seleccion$id_credito, sprintf("%03d", 15:20)),
          identical(unname(r$control), c(6, 14061)),
          identical(r$resumen$saldo_mxn, c(26030, 27690)))
print(r)
```

[referencia.R](referencia.R) lee el CSV como texto, reutiliza reglas R base incluidas
y calcula selección/resumen independientemente de pandas/Polars/DuckDB. Los saldos
individuales siguen siendo integer; suma en double con la cota de 1998 filas
ya justificada, sin extrapolar exactitud a cualquier entero. Reinicia R y ejecuta
el script completo. Autoría comprueba R 4.6.1 desde procesos nuevos; no afirma
haber probado la interfaz del IDE. La consola R es distinta de la terminal.

## 7. Qué queda cerrado y qué se entrega después

Las diez secciones de este módulo tienen material; 10.05 sigue siendo extensión
opcional. Para cerrar **tu práctica**, presenta tablas reconstruidas, decisión,
evidencia y explicación; el estado del material no acredita aprendizaje.

El proyecto previsto `04_large_credit_dataset` no se crea ni activa con este lab.
Siguen pendientes producto, fuentes, rúbrica y checkpoints de esa integración,
según [proyectos](../../../projects/README.md) y
[pendientes de almacenamiento](../../../docs/storage-closure.md).

El siguiente módulo es [11 — Reportes con Quarto](../../11_reporting_quarto/README.md),
con [11.01 — Reporte, fuente y renderizado](../../11_reporting_quarto/01_report_source_render/README.md)
ya disponible. Esta entrega aporta pregunta, tablas, método, decisión y
límites para una narrativa; no exige instalar Quarto ni copiar cifras manualmente.
Registra evidencia y dudas en [PROGRESS.md](../../../PROGRESS.md).

## Práctica y criterio de salida

Realiza el [lab 10.10](../../../labs/10_polars_duckdb/10_closure_tool_choice/README.md).
Puedes reconstruir cada resultado desde la fuente, explicar el agregado entero,
detectar cambios que preservan sumas y defender tu elección con límites explícitos.
La revisión humana de esa explicación pertenece al cierre de la práctica.

## Referencias primarias

Consultadas el 2026-10-23; datos/ejemplos propios y APIs ejecutadas con las
versiones fijadas. La documentación web Polars puede describir otra serie.

- [pandas 2.3.3: lectura Parquet y tipos](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_parquet.html).
- [Polars: collect y materialización](https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.collect.html).
- [DuckDB 2.0: conversiones y salida Arrow](https://duckdb.org/docs/2.0/clients/python/conversion).
- Los [relojes, contadores y límites de las mediciones](../09_time_memory/README.md#referencias-primarias)
  tienen sus fuentes primarias en 10.09.

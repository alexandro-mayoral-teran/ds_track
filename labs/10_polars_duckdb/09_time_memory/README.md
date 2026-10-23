# Lab 10.09 — Medir una pregunta definida

## Propósito y entradas

Conservar mediciones repetidas cuya respuesta, unidades y alcance puedas explicar.
La [lección](../../../curriculum/10_polars_duckdb/09_time_memory/README.md)
incluye entorno, conceptos y todos los datos; no exige entregas previas.
Una financiera ficticia tiene estos registros, en el CSV propio de la sección:

| ID | Corte | Saldo MXN |
| --- | --- | ---: |
| 001 | 2026-09-30 | 0 |
| 002 | 2026-09-30 | 2000 |
| 003 | 2026-09-30 | 2500 |
| 001 | 2026-10-31 | 100 |
| 002 | 2026-10-31 | 1900 |
| 003 | 2026-10-31 | 2600 |

Clave ID/corte única, ID textual de tres dígitos, Date 1900–2100 y saldo
entero 0–2147483647 MXN, sin ausencias. Audita toda la fuente antes del filtro.
Por corte hay tres filas y 4500/4600; no sumes cortes para presentar un saldo
a una fecha única.

## Actividad

1. Escribe pregunta, entrada, salida y predicción: octubre ≥ 2000 debe dar
   `003/2600`. Dibuja qué incluye consulta_ns, intervalo_ns y proceso_ns.
2. Prepara un Parquet nuevo y una corrida nueva con tres repeticiones por motor.
   Anota equipo/disco/carga/energía conocidos. No supongas caché fría.
3. Conserva los nueve registros crudos y exportaciones. Comprueba la respuesta
   de cada variante antes de mirar cuál tiene menor mediana.
4. Reconstruye una mediana y su rango desde crudas; convierte ns a ms y bytes
   a MiB. Explica si el pico incluye importaciones y qué no mide tracemalloc.
5. Reinicia Python y verifica la corrida sin medirla otra vez ni modificar archivos.
6. Redacta una conclusión local, con política de caché, fases y métrica de memoria.
   No generalices a grandes datos ni descartes automáticamente la corrida lenta.

## Resultado esperado

Nueve respuestas `003/2600`, tres observaciones por motor con orden rotado,
fases que concilian y resumen reconstruible. No hay un tiempo ni consumo exactos
que deban coincidir entre equipos. El contador no disponible es ausencia, no cero.

Puedes realizarlo por partes: preparación/medición en una sesión y análisis/
verificación en otra. No se necesita repetir mediciones solo para recuperar el informe.

## Comprobación y solución razonada

<details>
<summary>Recorrido completo y mediana reconstruida</summary>

Desde la raíz en Python con el entorno elegido:

```python
from pathlib import Path
import json
from statistics import median
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/09_time_memory").resolve()))
import comparar

entrada = comparar.preparar("output/lab_1009_datos")
destino = Path("output/lab_1009_corrida")
informe = comparar.medir(entrada, destino, nota="Registrar condiciones conocidas")
resumen = comparar.verificar(destino, entrada)
archivos = sorted(p for p in destino.glob("*.json") if p.name != "informe.json")
crudas = [json.loads(p.read_text(encoding="utf-8")) for p in archivos]
assert len(crudas) == 9
for motor in comparar.MOTORES:
    grupo = [r for r in crudas if r["motor"] == motor]
    assert len(grupo) == 3
    assert all(r["seleccion"] == [{"id_credito": "003", "saldo_mxn": 2600}] for r in grupo)
    ns = [r["consulta_ns"] for r in grupo]
    fila = next(r for r in resumen if r["motor"] == motor)
    assert fila["consulta_ns"]["mediana"] == median(ns)
    print(motor, "min/mediana/max ms:", min(ns)/1e6, median(ns)/1e6, max(ns)/1e6)
```

En otra sesión repite imports, asigna entrada/destino a esas rutas y llama solo
a verificar. La mediana de tres es el valor central ordenado; conservar rango
y crudas evita ocultar variación. Un valor grande no se elimina sin una regla
de exclusión justificada previamente.

</details>

<details>
<summary>Cómo redactar el alcance de la conclusión</summary>

Completa con tus valores, sin copiar cifras de otra máquina:

«Para seis registros en este Parquet y selección octubre ≥ 2000, concilié
003/2600 en tres observaciones por motor. Usé procesos nuevos, orden rotado,
entrada ya leída en auditoría y caché del SO sin vaciar. Registré versiones y
pools configurados a uno. Consulta abarca entrada/plan, ejecución/recuperación
y adaptación; la exportación se midió aparte. La mediana y rango de [recorrido]
fueron […]. El pico [métrica] abarca el proceso hasta después de exportar y
no representa RAM adicional de la consulta. No medí I/O físico ni sostengo
que este resultado se mantenga al cambiar volumen, filtros o hilos».

Si falta información de hardware/carga, dilo. Si dos rangos se superponen,
no conviertas una diferencia de medianas pequeñas en una regla general.

</details>

## Ampliaciones opcionales

- Mide septiembre ≥ 2001 en otra carpeta: debe dar 003/2500. Noviembre debe
  exportar una lista vacía conservando el esquema int32 de la selección.
- Cambia solo el tamaño con el generador determinista de abajo, conservando
  contrato/filtro/configuración. No llames grandes datos a 40/400 filas.
- Ejecuta el ejemplo R completo de la lección y explica por qué sus tiempos
  de tabla en memoria/DBI no se mezclan con los procesos Python/Parquet/JSON.

<details>
<summary>Preparar 40 filas sin repetir claves</summary>

Desde una sesión Python nueva en la raíz:

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("curriculum/10_polars_duckdb/09_time_memory").resolve()))
import comparar

carpeta = Path("output/lab_1009_escala")
carpeta.mkdir(parents=True, exist_ok=False)
fuente = carpeta / "fuente_40.csv"
comparar.referencia.generar_escala(fuente, creditos=20)
entrada_40 = comparar.preparar(carpeta / "datos", fuente)
assert comparar.auditar(entrada_40, fuente) == 40
# Para medir esta entrada, usa otra carpeta nueva y pasa fuente=fuente.
```

El generador usa dos cortes y IDs nuevos; no concatena copias que romperían
la clave ID/corte. Para 400 filas elige 200 créditos en otra carpeta y conserva
el archivo previo. La referencia calcula los pares de cada muestra; no asumas
que 40 filas deben conservar la selección 003/2600 de la muestra de seis.

</details>

## Evidencia y criterio de salida

Conserva contrato/pregunta, fuentes, crudas/exportaciones, informe, notas del
equipo y una conclusión cuyo alcance coincida con las métricas. Explica:
¿por qué un plan lazy pequeño no es una consulta ya ejecutada?, ¿por qué un
pico histórico no se resta como si fuese memoria exclusiva?, ¿qué cambia si
una aplicación ya importó bibliotecas o retiene tablas?, ¿qué no autentican las huellas?

Avanza cuando puedas conciliar la respuesta, reconstruir el resumen y detectar
comparaciones con fases distintas. No hay checkpoint activo; proyecto y práctica
del estudiante siguen pendientes aunque el material exista.
Siguiente: [10.10 — Cierre y elección de herramienta](../../../curriculum/10_polars_duckdb/10_closure_tool_choice/README.md).

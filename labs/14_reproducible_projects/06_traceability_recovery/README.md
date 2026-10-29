# Lab 14.06 — Recuperar y explicar un intento fallido

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.06**

## Relación y objetivo

Refuerza [14.06 — Trazabilidad y recuperación de fallas](../../../curriculum/14_reproducible_projects/06_traceability_recovery/README.md).
Objetivo: decidir cómo continuar a partir de registros y archivos comprobados.
No hay proyecto asociado ni checkpoint implementado.

## Entrada

Usa las 33 fuentes reunidas por el [preparador y recorrido elegido](../../../curriculum/14_reproducible_projects/06_traceability_recovery/recorridos.md).
No necesitas entregas anteriores ni paquetes nuevos. Elige un lenguaje, conserva
las copias y trabaja con un escritor. La entrada es sintética: tres créditos por
corte, saldos MXN enteros y clave ID/fecha. Con ambos segmentos y mínimo 2000:
octubre selecciona 003/2600 sobre universo 3/4600; septiembre 002/2000 y 003/2500
sobre universo 3/4500. La cobertura usa número de créditos del corte.

## 1. Predecir antes de ejecutar

Sin abrir todavía la solución, escribe una tabla con estas columnas:
intento, falla solicitada, última etapa esperada, existencia del destino final,
acción siguiente. Completa filas para a01/a02/a03 y b01/b02 de los recorridos.

Tu acompañante elige una predicción para preguntarte por qué. No alcanza con
afirmar que «si falla no hay resultado»: identifica cuándo ocurre cada error.

## 2. Fallar, conservar y recuperar

Realiza el recorrido esencial: a01 falla antes del contexto; a02 crea y a03
reutiliza. Antes de a02, localiza el temporal exacto en consola.txt y describe
sus archivos. No borres el temporal, cambies la marca COMPLETO ni lo renombres.

Comprueba en la entrega recuperada:

- Una fila seleccionada: ID 003 y saldo 2600.
- Contexto de octubre, mínimo 2000, ambos segmentos y reglas 1401-v1.
- Universo de tres créditos/4600 MXN y cobertura 1/3, con tolerancia de 1e-10
  puntos porcentuales si comparas su representación decimal.
- Registro separado para cada intento y último evento coherente.

Antes y después de a03, compara las huellas de los cuatro archivos finales:
deben coincidir. Que los bytes coincidan no prueba por sí solo ausencia de
reescritura; para sostenerla revisa también la rama de reutilización del pipeline.
Los nuevos eventos viven fuera de la entrega, en intentos/a03.

<details>
<summary><strong>Pista: qué comparar</strong></summary>

Revisa seleccion.csv, contexto.csv, insumos.csv y COMPLETO.csv. Puedes usar
`Get-FileHash` en PowerShell, `md5sum` si existe en tu shell o `tools::md5sum`
en R. No modifiques los archivos para hacer coincidir las huellas.

</details>

## 3. Explicar el fallo final

En la segunda copia nueva realiza b01 con simulación final y b02 sin ella.
Localiza en b01 el OK de pipeline y el FALLO de cierre. Revisa la entrega
existente y el resultado de b02. Explica por qué conservar el error es compatible
con reutilizar después una entrega que sí supera todas las comprobaciones.

Después considera esta variación **sin terminar procesos a la fuerza**: recibes
solo un registro cuyo último evento es ENTRADA en pipeline. Escribe qué puedes
afirmar, qué desconoces y cómo comprobarías el destino con un intento nuevo.
No conviertas la ausencia de final en una afirmación de éxito o de fallo seguro.

## 4. Otra consulta exige otro destino

Regresa a la primera copia y conserva config/consulta.csv. Crea config/septiembre.csv
como una copia nueva, sin reemplazar archivos existentes. En el editor cambia
solo corte a `2026-09-30` y salida a `salidas/septiembre`. Mantén los otros valores.

En R, consola de la primera copia:

```r
if (file.exists("config/septiembre.csv")) stop("Configuracion ocupada.")
stopifnot(file.copy("config/consulta.csv", "config/septiembre.csv", overwrite = FALSE))
# Edita y guarda los dos valores indicados antes de ejecutar.
```

En PowerShell, desde esa copia:

```powershell
if (Test-Path config/septiembre.csv) { throw "Configuracion ocupada." }
Copy-Item -LiteralPath config/consulta.csv -Destination config/septiembre.csv -ErrorAction Stop
```

En Bash, alternativa completa de copia:

```bash
test ! -e config/septiembre.csv || exit 1
cp config/consulta.csv config/septiembre.csv || exit 1
```

Tras editar, ejecuta según tu ruta:

```r
source("trazar.R")
trazar_proyecto(".", "sept01", "config/septiembre.csv")
```

```powershell
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sept01 --config config/septiembre.csv
if ($LASTEXITCODE -ne 0) { throw "Revisar consulta de septiembre." }
```

```bash
uv run --locked --no-python-downloads --cache-dir .uv-cache python trazar.py sept01 --config config/septiembre.csv || exit 1
```

Comprueba dos filas 002/2000 y 003/2500, total seleccionado 4500 y cobertura 2/3.
La entrega de octubre y sus registros deben permanecer. Relaciona septiembre
con su consulta.csv y huellas.csv. No basta cambiar el nombre del intento:
este no modifica el corte ni autoriza sobrescribir la salida anterior.

## Resultado esperado y solución razonada

<details>
<summary><strong>Ver solución después de comprobar</strong></summary>

| Intento | Último evento | Destino y decisión |
| --- | --- | --- |
| a01 | FALLO en pipeline | Sin final en copia nueva; conservar parcial y corregir causa simulada |
| a02 | TERMINADO / creada | Final comprobado; parcial anterior permanece |
| a03 | TERMINADO / reutilizada | Recalcula y compara; mantiene entrega |
| b01 | FALLO en cierre | Entrega ya creada; revisar, sin asumir ausencia |
| b02 | TERMINADO / reutilizada | Recalcula y confirma la entrega existente |
| sept01 | TERMINADO / creada | Otro corte/configuración en salida nueva |

El error a01 se corrige quitando la simulación en otro intento; no manipulando
el parcial. El fallo b01 sucede después de que el pipeline comprobó y publicó.
Si los insumos se mantienen, b02 puede confirmar esa entrega. Sin evento terminal,
el estado histórico queda indeterminado; una nueva comprobación aporta evidencia
actual, no reconstruye mágicamente cada instrucción del proceso anterior.

Septiembre selecciona 002 justo en la frontera 2000 y 003/2500. Octubre conserva
003/2600. Ambos universos tienen tres créditos, con 4500 y 4600 MXN. Las coberturas
son 2/3 y 1/3 respectivamente, calculadas sobre créditos y no sobre saldos.

</details>

## Evidencia y reflexión

Conserva predicciones, registros, diagnósticos, parciales y entregas en tu copia
personal, junto con una nota: causa, etapa alcanzada, acción, comprobación por ID,
resultado y límites. No registres tu práctica en PROGRESS.md compartido.
Tu acompañante debe poder localizar un fallo y comprobar tu decisión.

Explica qué distingue reintentar, reutilizar y reanudar; qué no permite recuperar
una huella; y por qué un log editable o una fecha no autentican una ejecución.
No hay recuperación automática, integración reporte/app ni garantía de concurrencia.

Siguiente lección: [14.07 — Integración de reporte y app](../../../curriculum/14_reproducible_projects/07_report_app_integration/README.md),
disponible con su lab. [Volver a 14.06](../../../curriculum/14_reproducible_projects/06_traceability_recovery/README.md).

# 14.04 — Pipeline y reprocesamiento

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **14.04**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Repetir una consulta y separar cortes sin duplicar resultados |
| **Necesitas** | Contrato/configuración de 14.01–14.02 y un entorno de 14.03 |
| **Evidencia** | Entregas conciliadas, repetición sin cambios y fallo explicado |

[**Hacer el lab 14.04 →**](../../../labs/14_reproducible_projects/04_pipeline_reprocessing/README.md) · [Recorridos de ejecución](recorridos.md)

## Propósito y prerrequisitos

Un pipeline es una secuencia de pasos con dependencias: cada paso recibe algo
que el anterior preparó y comprobó. Aquí una persona elige la configuración y
lanza la ejecución local. No hace falta un servicio de orquestación.

Revisa [14.01, contrato](../01_product_question_contract/README.md),
[14.02, estructura](../02_structure_configuration/README.md) y
[14.03, entornos](../03_reconstructible_environments/README.md).
Los preparadores incluyen todas las fuentes; no necesitas entregas anteriores.
Elige R/renv o Python/uv. El entorno y sus lockfiles se conservan, sin paquetes nuevos.

## Objetivos

- Explicar qué pasos dependen de la fuente, la configuración y el código.
- Ejecutar dos veces una consulta sin agregar filas ni reemplazar archivos.
- Procesar otro corte en otro destino y conciliar filas, contexto e indicadores.
- Distinguir una entrega comprobada de un intento parcial.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Recorridos](recorridos.md) | Preparar y ejecutar en R/IDE, PowerShell o Bash | Elegir uno |
| [Preparador R](preparar.R) / [Python](preparar.py) | Copiar 28 fuentes a una carpeta nueva | Según ruta |
| [Pipeline R](plantilla/pipeline.R) / [Python](plantilla/pipeline.py) | Seguir las fases y sus comprobaciones | Consulta de código |
| [LEEME de la copia](plantilla/LEEME.md) | Restaurar el entorno y reconocer la entrega | Leer antes de ejecutar |
| [Fuente](../01_product_question_contract/cartera.csv) y [criterios](../01_product_question_contract/criterios.csv) | Inspeccionar las seis filas y los nueve casos conocidos | Comparar con resultados |

## Datos y pregunta, completos en esta sección

La fuente sintética usa pesos mexicanos enteros; cada fila es un crédito en un
corte. La clave es **id_credito + fecha_corte**; el ID conserva sus ceros.

| id_credito | segmento | fecha_corte | saldo_mxn |
| --- | --- | --- | ---: |
| 001 | comercio | 2026-09-30 | 0 |
| 002 | servicios | 2026-09-30 | 2000 |
| 003 | comercio | 2026-09-30 | 2500 |
| 001 | comercio | 2026-10-31 | 100 |
| 002 | servicios | 2026-10-31 | 1900 |
| 003 | comercio | 2026-10-31 | 2600 |

Pregunta: dentro de un corte, ¿qué créditos cumplen los segmentos elegidos y
un saldo **mayor o igual** al mínimo? El universo incluye todos los créditos
del corte, antes de esos dos filtros. Porcentaje = 100 × seleccionados / universo.
No se suman cortes como si fueran créditos diferentes de una sola fecha.

Con ambos segmentos y mínimo 2000:

| Corte | IDs seleccionados | Saldo seleccionado | Universo | Saldo del universo | % de créditos |
| --- | --- | ---: | ---: | ---: | ---: |
| Septiembre | 002, 003 | 4500 | 3 | 4500 | 66.666… |
| Octubre | 003 | 2600 | 3 | 4600 | 33.333… |

La fuente completa se valida antes de filtrar: columnas exactas, IDs de tres
cifras, fechas reales 1900–2100, segmentos del catálogo, saldo entero 0..1000000,
clave única y hasta 10000 filas. Un duplicado de septiembre también impide
publicar octubre. Reglas detalladas en la
[especificación](../01_product_question_contract/ESPECIFICACION.md).

## Un orden que se puede explicar

```text
entorno local → configuración → fuente completa válida → consulta
                                                        ↓
                         tablas esperadas ← selección + contexto
                                  ↓
             destino existente: releer y comparar → reutilizar o rechazar
             destino nuevo: temporal → escribir → marcar → comprobar → renombrar
```

1. **Entorno:** comprobar versiones y aislamiento antes de producir resultados.
2. **Configuración:** leer corte, segmentos, mínimo y destino. Rutas relativas
   a la raíz; ni el directorio de trabajo accidental ni un valor escondido deciden el corte.
3. **Fuente:** validar todos los registros. Un filtro no corrige datos inválidos.
4. **Cálculo:** obtener selección y denominador desde la misma fuente.
5. **Entrega:** construir tablas esperadas y comprobar archivos antes de anunciar éxito.

`revisar.py/R` conserva su papel de consulta sin exportar: exige un destino
libre. `pipeline.py/R` admite uno existente para comprobarlo. `ejecutar.py/R`
conserva la evidencia de entorno de 14.03 y expone su comprobación para el pipeline.
No ejecuta Quarto ni inicia Streamlit/Shiny; el campo app registra la decisión prevista.

## Repetir: qué significa aquí

Una operación es **idempotente** si repetirla deja el mismo estado relevante.
Aquí, la segunda ejecución vuelve a validar y calcular; después compara con la
entrega existente y la reutiliza **sin escribir**. No es una caché que omita
validaciones. Tampoco agrega resultados al CSV con append.

El corte por sí solo no identifica todo el cálculo. También importan los bytes
de fuente/configuración, versión de reglas y código registrado. Se incluyen
huellas del modelo, configuración y pipeline, y el motor Python/R. Un cambio
incluso fuera del corte impide reutilizar esa entrega. Reordenar la fuente o
editar un comentario del código registrado también puede cambiar su huella:
es una política conservadora y fácil de comprobar, no equivalencia semántica general.

Si cambia algo, **conserva el destino anterior y usa otro nombre**. Para comparar
Python y R usa copias/destinos distintos: sus insumos registran motores diferentes.
Las tablas de selección/contexto deben describir los mismos resultados.

## Los cuatro archivos de una entrega

| Archivo | Contenido | Comprobación |
| --- | --- | --- |
| seleccion.csv | Cuatro columnas de la fuente, solo filas seleccionadas, orden por ID | Cada valor coincide con la selección recién calculada |
| contexto.csv | Una fila: parámetros, estado, universo, selección, saldos y porcentaje | Numerador y denominador corresponden al mismo corte |
| insumos.csv | Esquema 1404-v1, motor, reglas y huellas de fuente/configuración/código | Los insumos registrados coinciden con los actuales |
| COMPLETO.csv | Nombres y MD5 de los tres CSV anteriores | Inventario exacto, huellas y tablas comprobadas |

MD5 sirve aquí para detectar cambios accidentales; no acredita autenticidad.
Un archivo con la palabra COMPLETO no prueba que el cálculo sea correcto.
El pipeline reconstruye las tablas esperadas: alterar dos saldos conservando la
suma y actualizar las huellas sigue fallando al comparar cada registro.
La comprobación usa la fuente/configuración **actuales**; no es un auditor
independiente de entregas históricas cuyos insumos ya no están disponibles.

## Vacío, ausencia de universo y fallo

- **vacio:** existe universo, pero no seleccionados. Se publica seleccion.csv
  con encabezados y cero filas; contexto conserva universo y muestra selección/saldo cero.
- **sin_universo:** el corte no tiene registros. Se detiene antes de crear temporal;
  un denominador ausente no se convierte en porcentaje cero.
- **rechazo:** datos/configuración inválidos. No se publica una entrega nueva.
- **fallo durante escritura:** queda `.pendiente-*`, sin destino final. Se conserva
  para revisión y el reintento construye otra carpeta; no incorpora archivos del intento fallido.

La opción de simulación falla después de escribir seleccion.csv en el temporal.
No representa todas las fallas posibles ni se activa al reutilizar un destino válido.

## Escritura temporal y límites

Se escribe en un hermano temporal del destino, dentro de salidas. COMPLETO.csv
se escribe al final; después se relee la carpeta y se compara. Solo entonces se
renombra al destino libre. El renombrado usa el mismo directorio padre para no
mover entre sistemas de archivos. No se reemplaza una entrega anterior.

Esto reduce la exposición de resultados parciales; **no garantiza una transacción
de todo el pipeline**, durabilidad frente a un apagón ni exclusión de escritores
simultáneos. Ejecuta una persona/proceso por destino. No hay bloqueo distribuido,
programación periódica ni limpieza automática. La recuperación y trazabilidad más
amplias se desarrollarán en 14.06. La documentación de
[Python os.rename](https://docs.python.org/3.12/library/os.html#os.rename) y
[R file.rename](https://stat.ethz.ch/R-manual/R-devel/library/base/html/files.html)
explica restricciones y diferencias entre plataformas; no generalices las pruebas de Windows.

## Ejecución y práctica

Sigue el [recorrido completo](recorridos.md): preparar copia nueva, restaurar una
ruta, ejecutar/repetir octubre, crear configuración de septiembre y simular un fallo.
Después realiza el [lab](../../../labs/14_reproducible_projects/04_pipeline_reprocessing/README.md).

## Criterio de salida y siguiente paso

Explica cada dependencia y demuestra: repetición sin cambios en archivos;
septiembre/octubre separados con cifras conciliadas; vacío distinguido de
sin universo; fallo sin entrega final; rechazo de un destino alterado.
Guarda evidencia de tu propia práctica; el material disponible no acredita haberla realizado.
No hay proyecto asociado ni checkpoint implementado.

Puedes detener la sesión aquí después de revisar esa evidencia. La siguiente
sección es [14.05 — Pruebas y calidad de datos](../README.md#05-pruebas-y-calidad-de-datos),
aún planificada.

## Referencias primarias

- [Python 3.12: csv](https://docs.python.org/3.12/library/csv.html): encabezados y filas al leer/escribir.
- [Python 3.12: tempfile.mkdtemp](https://docs.python.org/3.12/library/tempfile.html#tempfile.mkdtemp): directorios temporales únicos, limpieza a cargo del programa.
- [R: write.table](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/write.table.html): escritura tabular y opciones explícitas.

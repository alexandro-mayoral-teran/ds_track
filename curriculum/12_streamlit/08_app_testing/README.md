# 12.08 — Pruebas de la aplicación

[Inicio](../../../README.md) / [Módulo 12](../README.md) / **12.08**

**Una app que abre sin errores todavía puede mostrar una cifra equivocada.**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Detectar errores en cálculos y transiciones de la app con casos conocidos |
| **Necesitas** | Funciones, formularios, mensajes y descargas de 12.03–12.07 |
| **Evidencia** | Pruebas, un fallo explicado y un registro de revisión en navegador |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Lab 12.08](../../../labs/12_streamlit/08_app_testing/README.md) · [Criterio de salida](#evidencia-y-criterio-de-salida)

## Propósito

Probar significa preparar una situación, ejecutar una acción y contrastar el
resultado con una expectativa justificada. Hasta ahora comprobabas filtros y
descargas manualmente. Aquí conviertes parte de esas comprobaciones en programas
que puedes repetir después de cambiar la app.

Las pruebas ayudan a detectar una **regresión**: algo que funcionaba y deja de
hacerlo después de una modificación. Una prueba aprobada cubre los casos y
propiedades que escribiste; no demuestra que toda interacción futura sea correcta.

## Antes de empezar

- Revisa [12.03 — Modelo e interfaz](../03_data_interface/README.md),
  [12.04 — Formularios](../04_session_state_forms/README.md) y
  [12.07 — Tabla, gráfico y descarga](../07_tables_charts_download/README.md).
- Retoma [05.04 — Pruebas](../../05_python_applied/README.md#orden-de-desarrollo)
  si necesitas recordar `unittest`, métodos de prueba y aserciones. Esta lección
  explica las herramientas nuevas de AppTest y el aislamiento que usa el ejemplo.
- Usa el entorno local de 12.01: Python 3.12.12, Streamlit 1.66.1 y Altair 6.3.0
  son las versiones de referencia comprobadas. `unittest` viene con Python;
  AppTest viene con Streamlit. No necesitas instalar pytest ni cambiar lockfiles.
- Sigue los [recorridos completos](recorridos.md) para preparar una carpeta
  nueva. No necesitas una entrega anterior. No ejecutes la app fuente de 12.07
  directamente: el preparador reúne sus módulos y datos.
- Las pruebas se ejecutan con **Python en la terminal**, sin servidor ni pestaña.
  Para la revisión del navegador sí arrancarás Streamlit desde tu copia.

## Qué vas a aprender

- Elegir un resultado esperado a partir de datos y reglas explícitos.
- Probar funciones, cambios de widgets y estado de sesión en niveles separados.
- Comprobar frontera, vacío, errores tratados, recuperación y sesión nueva.
- Detectar una regresión sin cambiar la prueba para aceptar el error.
- Distinguir datos preparados de una descarga real y de su presentación visual.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Preparador](preparar_practica.py) y [recorridos](recorridos.md) | Reunir fuentes y ejecutar en una copia nueva | Esencial |
| [Mínimo](minimo.py) y [su prueba](minimo_pruebas.py) | Dos ventas, tres situaciones y una primera interacción AppTest | Esencial: empezar aquí |
| [Pruebas del modelo](pruebas_modelo.py) | Contrastar reglas, CSV y contexto con expectativas explícitas | Esencial: leer y ejecutar |
| [Pruebas de la app](pruebas_app.py) | Comprobar indicadores, filas y transiciones aisladas | Esencial; la inspección del protocolo del gráfico es ampliación |
| [Modelo](../03_data_interface/cartera.py) y [CSV](../03_data_interface/cartera.csv) | Reglas y seis registros sintéticos | Reutilizados sin cambios |
| [App](../07_tables_charts_download/app.py), [gráfico](../07_tables_charts_download/graficos.py), [salidas](../07_tables_charts_download/salidas.py) y [revisor](../07_tables_charts_download/revisar_descarga.py) | Misma interfaz y archivos de 12.07 | Copiados sin cambios |
| [Configuración](../03_data_interface/configuracion.py), [ejecutor](../03_data_interface/ejecutar.py), [caché](../05_data_resource_cache/cache_analisis.py) y [entradas](../06_messages_empty_cases/entradas.py) | Conservar rutas, referencia JSON, caché y validación textual | Copiados sin cambios |

## 1. Tres niveles para preguntas distintas

| Nivel | Pregunta | Ejemplo y límite |
| --- | --- | --- |
| Función | ¿Las reglas producen los registros e indicadores esperados? | `analizar(...)` incluye un saldo igual al mínimo; no comprueba widgets |
| Integración con AppTest | ¿La app conecta controles, estado y resultados? | Enviar septiembre cambia filas e indicadores; no abre un navegador |
| Navegador | ¿La persona puede operar la interfaz y recuperar los archivos? | Editar sin enviar, usar teclado, leer barras y guardar CSV/JSON reales |

Una prueba necesita una **referencia esperada**: datos o resultados obtenidos
de una regla que puedas explicar. Si calculas el esperado volviendo a llamar a
la misma función, ambos lados pueden repetir el mismo error. Tampoco basta
comparar dos totales: intercambiar saldos entre créditos conserva la suma.
Por eso comprobaremos también ID, segmento, corte e importe de cada fila.

## 2. Primera prueba: dos ventas y un límite

El [mínimo](minimo.py) es autónomo. Contiene dos ventas ficticias, de 100 y 200 MXN.
Cada número representa una venta; elegimos importes **mayores o iguales** al
mínimo, sin faltantes ni conversiones. Los resultados se obtienen a mano:

| Mínimo MXN | Ventas seleccionadas | Importe seleccionado MXN |
| ---: | ---: | ---: |
| 100 | 2 | 300 |
| 200 | 1 | 200 |
| 201 | 0 | 0 |

Abre [minimo_pruebas.py](minimo_pruebas.py). Estas son sus operaciones principales:

```python
from pathlib import Path
from streamlit.testing.v1 import AppTest

app = AppTest.from_file(str(Path(__file__).with_name("minimo.py")), default_timeout=20).run()
assert not app.exception
assert [m.value for m in app.metric] == ["2", "300"]
app.number_input(key="minimo").set_value(200).run()
assert not app.exception
assert [m.value for m in app.metric] == ["1", "200"]
```

Este fragmento se ejecuta junto a `minimo.py` en la copia preparada. El archivo
completo lo envuelve en `unittest.TestCase`; `assertEqual` ofrece diferencias
legibles al fallar y `assertFalse` exige una condición falsa.

- `Path(__file__)` ubica el archivo de prueba; `with_name` busca su vecino.
  Evita depender de la carpeta desde la que abriste la terminal.
- `from_file` crea una app simulada; el primer `run()` ejecuta su script.
  `default_timeout=20` es un límite de espera en segundos, no una pausa artificial.
- `app.exception` reúne excepciones sin tratar de esa pasada. Debe estar vacío.
- `app.metric` reúne las métricas en orden; `value` contiene su texto mostrado.
  Por eso el esperado usa cadenas como `"300"`.
- `number_input(key="minimo")` localiza el widget por su clave, ya definida en
  la app. `set_value(200)` prepara su valor; **`run()` ejecuta otra pasada**.

Predice qué debería pasar con 201 y encuentra esa tercera comprobación en el
archivo. Desde la raíz, con Python de tu entorno activado:

```text
python output/practica_1208/minimo_pruebas.py
```

Con uv usa el prefijo de tus [recorridos](recorridos.md). Debe aparecer
`Ran 1 test` y `OK`: un método contiene varias acciones y aserciones.
`FAIL` significa que una expectativa no coincidió; `ERROR` puede indicar que
el propio código de prueba no logró continuar. Lee el nombre y la diferencia,
no solo el último renglón. Un aviso de `ScriptRunContext` en modo de prueba no
sustituye el resultado de `unittest` ni autoriza ignorar excepciones de la app.

**Pausa posible:** conserva tu predicción de 201 y explica el papel de `run()`
antes de pasar a la cartera.

## 3. Funciones: datos pequeños y resultados independientes

[pruebas_modelo.py](pruebas_modelo.py) empieza con dos registros completos:

| ID | Segmento | Corte | Saldo MXN |
| --- | --- | --- | ---: |
| 001 | comercio | 2026-09-30 | 0 |
| 002 | servicios | 2026-09-30 | 2000 |

Unidad: crédito en un corte; clave ID/corte. IDs de tres dígitos, fecha ISO
real entre 1900 y 2100, segmento del catálogo y saldo entero de 0 a 1000000 MXN.
No se aceptan faltantes, duplicados ni booleanos como saldos. Cero es observado.
La fuente completa se valida antes de filtrar, aunque una fila no aparezca
en la selección. Son reglas del ejemplo reutilizado, no de toda cartera real.

Elige septiembre, servicios y mínimo 2000. Esperamos la fila 002 completa,
universo de dos créditos/2000 MXN y selección de uno/2000, equivalente al 50%.
La prueba escribe esos valores explícitamente; no pide al modelo que fabrique
su propia respuesta esperada.

```python
resultado = analizar(self.filas, "2026-09-30", ["servicios"], 2000)
self.assertEqual(resultado["seleccion"], [self.filas[1]])
self.assertEqual(resultado["indicadores"],
                 {"cantidad": 1, "saldo_mxn": 2000, "porcentaje_creditos": 50.0})
```

`setUp` prepara esas dos filas antes de cada prueba. `self` permite guardarlas
para el método; cada método `test_...` recibe una preparación independiente.
La prueba también verifica que cambiar el resultado no modifique la entrada.
Para un error esperado se usa `with self.assertRaises(ValueError):`: el bloque
debe lanzar esa excepción. Si no la lanza, la prueba falla.

Contrasta tres situaciones que comparten saldo seleccionado cero:

| Situación | Cantidad seleccionada | Porcentaje |
| --- | ---: | --- |
| Septiembre, comercio, mínimo 0 | 1 | 50%: el crédito tiene saldo cero conocido |
| Septiembre, ningún segmento | 0 | 0%: existe universo válido |
| Noviembre sin registros | 0 | `None`: falta el denominador |

La función representa estas situaciones con datos; la app decide qué mensaje
y métricas presentar. Una entrada inválida debe lanzar un error; una selección
vacía válida devuelve un resultado. No convertir ambos casos en la misma lista
vacía para hacer pasar una prueba.

Ejecuta `python output/practica_1208/pruebas_modelo.py`. Sus siete métodos
incluyen frontera, validación fuera del filtro, mínimo textual, copias, CSV y
contexto. `subTest` identifica variantes dentro de un método sin ocultar cuál falló.

## 4. La base común y una transición de formulario

La app completa reutiliza las seis filas sintéticas de 12.03, que el preparador
incluye sin pedir entregas previas:

| ID | Segmento | Corte | Saldo MXN |
| --- | --- | --- | ---: |
| 001 | comercio | 2026-09-30 | 0 |
| 002 | servicios | 2026-09-30 | 2000 |
| 003 | comercio | 2026-09-30 | 2500 |
| 001 | comercio | 2026-10-31 | 100 |
| 002 | servicios | 2026-10-31 | 1900 |
| 003 | comercio | 2026-10-31 | 2600 |

Se pregunta qué créditos de un corte cumplen segmentos y saldo mínimo. El
universo es **todo el corte antes de esos dos filtros**. Octubre tiene 3/4600 MXN;
septiembre, 3/4500 MXN. El inicio usa octubre, ambos segmentos y mínimo 2000:
003/2600, uno de tres y 33.33%.

Abre [pruebas_app.py](pruebas_app.py). La transición principal equivale a:

```python
app.selectbox(key="corte_borrador").set_value("2026-09-30")
app.multiselect(key="segmentos_borrador").set_value(["comercio", "servicios"])
app.text_input(key="minimo_borrador").set_value("2000")
app.button(key="aplicar").click().run()
```

Las primeras tres operaciones preparan valores; el botón del formulario provoca
el envío simulado al ejecutar `run()`. Esperamos 002/2000 y 003/2500, dos créditos,
4500 MXN y 66.67%. La prueba contrasta las cuatro columnas de ambas filas y los
tres textos de métricas. Subir el mínimo a 2001 deja solamente 003/2500.

`nueva`, `aplicar` y `comprobar_metricas` son métodos auxiliares de nuestra clase:
evitan repetir preparación, interacción y comparación. **No son API de AppTest.**
El orden de las métricas es parte del contrato de esta interfaz; si cambias ese
orden deliberadamente, revisa la prueba junto con la especificación del resultado.

`app.table[0].value` permite recuperar la tabla como DataFrame. Convertirla con
`to_dict(orient="records")` produce registros comparables, incluidos los ceros
iniciales de los IDs. No hace falta generar otra tabla con el mismo algoritmo
para obtener el esperado.

## 5. Errores, sesiones y pruebas que no se contaminan

| Caso de la suite | Qué debe demostrar |
| --- | --- |
| Mínimo `2.5` enviado | Mensaje de rechazo, filtros previos y contador conservados, descargas bloqueadas; un envío válido recupera la app |
| Ningún segmento | Métricas 0/0/0%, sin tabla ni barras, botones de descarga habilitados |
| Noviembre | Aviso, sin métricas ni descargas de cartera |
| Un crédito con saldo cero | 1/0/100%, fila y gráfico presentes |
| Duplicado de septiembre al consultar octubre | Fuente completa rechazada, sin resultados anteriores, aun con caché |
| Archivo ausente o encabezado solo | Mensaje correspondiente, sin indicadores ni descargas |
| 2600 cambiado a 2800 | Otra lectura actualiza selección sin aumentar envíos |
| Otra pasada y nueva AppTest | La primera conserva filtros; la nueva comienza con octubre y contador 0 |

**Un error tratado no tiene por qué aparecer en `app.exception`.** La app
captura errores esperados y usa `st.error`/`st.stop`. Comprueba a la vez que no
hay excepciones sin tratar, que sí aparece el mensaje y que desaparecen las
salidas inapropiadas. `assert not app.exception` por sí solo aceptaría muchas
apps incorrectas.

Las pruebas de integración copian el CSV a `TemporaryDirectory`, una carpeta
temporal propia. `patch.object(configuracion, "RUTA_DATOS", ...)` cambia la ruta
que importará la app durante la prueba; **el lector y el análisis reales siguen
ejecutándose**. No simulamos sus respuestas.

`addCleanup` registra limpiezas que se ejecutan incluso al fallar una aserción:
vaciar la caché del análisis, restaurar la configuración y liberar la carpeta,
en orden inverso al registro. Antes de cada caso se vuelve a limpiar esa caché.
Una AppTest nueva tiene estado de sesión propio, pero la caché puede compartirse
en el proceso: son problemas distintos. Ejecuta la suite como proceso separado,
sin importarla dentro de un servidor de estudio que quieras conservar.

Los cambios de fuente solo afectan al CSV temporal. Tu CSV preparado y las
fuentes del repositorio permanecen intactos. No ejecutes pruebas paralelas que
compartan esta configuración de proceso; el recorrido usa ejecución secuencial.

Ejecuta `python output/practica_1208/pruebas_app.py`. Deben pasar once métodos.
Puedes concentrarte en uno con:

```text
python output/practica_1208/pruebas_app.py PruebasApp.test_inicio
```

## 6. Un fallo útil: la app abre y el saldo está mal

Una comprobación que nunca has visto fallar puede estar mirando algo irrelevante.
Prepara **otra copia**, por ejemplo `output/regresion_1208`, con el mismo preparador
y ejecútala primero sin cambios. En su `app.py`, localiza esta línea:

```python
col_saldo.metric("Saldo seleccionado (MXN)", indicadores["saldo_mxn"])
```

Cambia solamente el valor presentado:

```python
col_saldo.metric("Saldo seleccionado (MXN)", universo["saldo_mxn"])
```

La modificación muestra 4600 como saldo seleccionado inicial, cuando corresponde
2600. La tabla todavía contiene 003/2600; la app puede abrir sin excepción.
Ejecuta `pruebas_app.py PruebasApp.test_inicio` **de esa copia**: debe fallar al
comparar la métrica 4600 con el esperado 2600.

Lee la diferencia, explica universo frente a selección y restaura la línea.
Repite la prueba y luego toda la suite. No cambies 2600 por 4600 en el esperado
para ocultar el fallo. Este experimento no requiere modificar las fuentes educativas.

**Ampliación:** intercambia 2000 y 2500 entre los créditos de septiembre solo
en una copia de experimento. La suma sigue siendo 4500; las expectativas por
clave deben detectar el intercambio. Una suma conciliada no identifica las filas.

## 7. Gráfico y descarga: hasta dónde llega la automatización

`pruebas_modelo.py` relee los bytes CSV producidos por `preparar_descargas` y
compara cada campo con las dos filas esperadas de septiembre. También comprueba
filtros, universo, indicadores y huella del contexto. Esto prueba la función
de preparación de archivos; no demuestra que el navegador haya recibido esos bytes.

La última prueba de la app es una **ampliación dependiente de versión**. Con
Streamlit 1.66.1, `app.get("vega_lite_chart")` y `app.get("download_button")`
permiten inspeccionar elementos y sus `proto`. Los registros del gráfico viajan
en Arrow separados de su especificación; PyArrow, ya declarado, permite releerlos.
Se comprueban filas explícitas y botones habilitados/con `ignore_rerun`.
Estos detalles de protocolo pueden cambiar: no son una API de negocio propia
ni una comprobación visual de las barras. No enseñamos un `.click()` de descarga
que AppTest no ofrece para ese elemento en la versión comprobada.

Completa la revisión **en un navegador**, siguiendo los [comandos](recorridos.md):

| Acción | Resultado que debes comprobar y registrar |
| --- | --- |
| Inicio y descarga CSV/JSON | Octubre, 003/2600; universo 3/4600; campos y huella del par releídos |
| Editar septiembre sin enviar | Vista y descarga aún de octubre; Enter no envía en esta app |
| Confirmar septiembre/2000 | Dos filas y dos barras identificables, 4500/66.67%; archivos con 002/2000 y 003/2500 |
| Ocultar detalle | CSV conserva ambas filas; ocultar tabla no cambia selección |
| Enviar mínimo inválido y corregir | Botones bloqueados durante rechazo; recuperación con filtros válidos |
| Ningún segmento | Descarga CSV con encabezado y JSON con selección cero/universo válido |
| Recargar o abrir otra sesión | Filtros iniciales de octubre y contador 0 |
| Ventana estrecha y teclado | Etiquetas, filtros, soluciones y botones legibles y alcanzables; anotar problemas |

Usa `revisar_descarga.py` para releer cada par y contrasta además los valores
por ID/corte con la tabla de seis filas. La huella relaciona archivos, no
autentica la fuente ni valida por sí misma los importes. Conserva navegador,
ancho aproximado, filtros, predicción, resultado y limitaciones de tu revisión.
Si no verificaste una fila del protocolo, márcala pendiente. No declares probados
descarga real, accesibilidad completa o comportamiento de otros navegadores
por obtener `OK` en AppTest.

## Práctica

Realiza el [lab 12.08](../../../labs/12_streamlit/08_app_testing/README.md): añade
un caso de segmento, provoca y corrige la regresión, y contrasta dos descargas
reales. Puedes separar la sesión de pruebas de la revisión en navegador.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Prueba mínima y predicciones | 100/200/201 producen los tres resultados manuales | Qué ejecuta `run()` |
| Caso propio de función y AppTest | Filas completas e indicadores esperados | Por qué el esperado no repite el algoritmo |
| Diferencia del fallo y corrección | 4600 incorrecto detectado; 2600 restaurado y suites aprobadas | Universo frente a selección |
| CSV/JSON reales y nota de navegador | Claves, campos, filtros, huella y casos de formulario | Qué cubre cada nivel y qué queda pendiente |

Puedes continuar cuando justifiques una frontera, un error tratado y la
independencia de las sesiones, y puedas provocar, localizar y corregir el fallo.
Pide a tu compañero una variación que no conozcas de antemano. Conserva ayudas,
dudas y siguiente paso en tu bitácora personal; PROGRESS.md registra autoría.
No hay proyecto integrador ni checkpoints implementados por añadir esta sección.

## Referencias

Fuentes oficiales consultadas el 2026-10-28; ejemplos propios comprobados con
Python 3.12.12, Streamlit 1.66.1 y Altair 6.3.0. La documentación web puede mostrar
otra versión; la referencia de AppTest consultada presenta v1.66.0.

- [Streamlit: introducción a pruebas](https://docs.streamlit.io/develop/concepts/app-testing/get-started)
  y [AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest).
- [Python 3.12: unittest](https://docs.python.org/3.12/library/unittest.html),
  [patch.object](https://docs.python.org/3.12/library/unittest.mock.html#patch-object)
  y [TemporaryDirectory](https://docs.python.org/3.12/library/tempfile.html#tempfile.TemporaryDirectory).
- [Arrow: lectura de streams IPC](https://arrow.apache.org/docs/python/ipc.html),
  para la ampliación de inspección del gráfico.

## Siguiente paso

Después del lab, consulta [12.09 — Cierre y entrega local](../README.md#09-cierre-y-entrega-local),
todavía planificado. El [estado y reanudación](../../../docs/streamlit-closure.md)
reúne los criterios pendientes sin dar por terminado el módulo.

---

[← 12.07](../07_tables_charts_download/README.md) · [Módulo 12](../README.md) · [Lab 12.08 →](../../../labs/12_streamlit/08_app_testing/README.md)

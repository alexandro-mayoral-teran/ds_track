# 12.09 — Cierre y entrega local

[Inicio](../../../README.md) / [Módulo 12](../README.md) / **12.09**

**Otra persona debe poder reconstruir, comprobar y explicar la app que entregas.**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Entregar un explorador local con fuentes, entorno, casos y límites recuperables |
| **Necesitas** | Modelo, estado, caché, descargas y pruebas de 12.03–12.08 |
| **Evidencia** | Carpeta reconstruida, contraste externo y demostración documentada |

[Preparación](#antes-de-empezar) · [Material de apoyo](#material-de-apoyo) · [Lab 12.09](../../../labs/12_streamlit/09_local_delivery/README.md) · [Criterio de salida](#evidencia-y-criterio-de-salida)

## Propósito

Una app que funciona en tu equipo puede depender de un archivo que olvidaste,
una ruta personal o un entorno que solo existe en tu sesión. El cierre convierte
el trabajo conocido en una carpeta que otra persona puede revisar y reconstruir.
Reutilizaremos la interfaz de 12.07 y las pruebas de 12.08; la capacidad nueva
es preparar y revisar una entrega local completa.

Como ejemplo pequeño, imagina que seleccionaste una venta de 200 MXN entre
ventas de 100 y 200. Entregar solo el CSV de 200 conserva la selección, pero
pierde el universo de dos ventas/300 MXN y la regla del filtro. Una entrega
reconstruible necesita fuente, reglas, código, entorno e instrucciones para
obtener de nuevo ese resultado. La misma distinción se aplica a la cartera.

Este cierre completa el **material de las nueve secciones de Streamlit**.
La práctica personal y los proyectos/checkpoints requieren sus propias evidencias;
no se completan por disponer de esta lección. Publicar en Internet es opcional.

## Antes de empezar

- Revisa [12.03 — Modelo e interfaz](../03_data_interface/README.md),
  [12.04 — Estado](../04_session_state_forms/README.md),
  [12.05 — Caché](../05_data_resource_cache/README.md),
  [12.07 — Descargas](../07_tables_charts_download/README.md) y
  [12.08 — Pruebas](../08_app_testing/README.md).
- Usa el entorno local que elegiste en 12.01. Referencias: Python 3.12.12,
  Streamlit 1.66.1 y Altair 6.3.0. No hay dependencias nuevas ni cambios del
  lockfile. El preparador copia los metadatos completos del curso.
- Sigue los [recorridos](recorridos.md): primero una práctica nueva, después
  una entrega nueva y finalmente otra reconstrucción. No necesitas conservar
  entregas anteriores del recorrido.
- Todo se ejecuta en tu copia personal. No modifiques las fuentes educativas
  para simular un fallo. Guarda notas y descargas fuera de la carpeta entregable.

## Qué vas a aprender

- Distinguir descarga de una vista, carpeta de trabajo y entrega reconstruible.
- Conservar contrato, fuentes, código, versiones y casos de referencia.
- Verificar valores por clave contra una referencia externa, además de huellas.
- Reconstruir desde otra carpeta sin depender del repositorio original.
- Demostrar funcionamiento y explicar los límites de sesión, caché y descarga.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Preparador](preparar_practica.py) y [recorridos](recorridos.md) | Reunir fuentes y separar práctica/entrega/reconstrucción | Esencial |
| [Constructor y verificador](entrega.py) | Crear un destino nuevo o revisar otro sin modificarlo | Esencial, ejecutar la copia preparada |
| [Instrucciones de la entrega](LEEME.md) | README autocontenido que recibe la otra persona | Esencial: leer antes de entregar |
| [App](../07_tables_charts_download/app.py), [modelo](../03_data_interface/cartera.py) y [CSV](../03_data_interface/cartera.csv) | Conservar lógica, interfaz y muestra | Reutilizados sin cambios |
| [Configuración](../03_data_interface/configuracion.py), [ejecutor](../03_data_interface/ejecutar.py), [caché](../05_data_resource_cache/cache_analisis.py) y [entradas](../06_messages_empty_cases/entradas.py) | Rutas, referencia JSON y reglas de aplicación | Copiados sin cambios |
| [Gráfico](../07_tables_charts_download/graficos.py), [salidas](../07_tables_charts_download/salidas.py) y [revisor](../07_tables_charts_download/revisar_descarga.py) | Vistas y relectura de descargas reales | Copiados sin cambios |
| [Pruebas del modelo](../08_app_testing/pruebas_modelo.py), [AppTest](../08_app_testing/pruebas_app.py), [mínimo](../08_app_testing/minimo.py) y [su prueba](../08_app_testing/minimo_pruebas.py) | Repetir comprobaciones en la reconstrucción | Esencial: modelo y AppTest; mínimo como repaso |
| [pyproject.toml](../../../pyproject.toml) y [uv.lock](../../../uv.lock) | Reconstruir el entorno bloqueado | Copiados sin cambios, no incluyen paquetes instalados |
| [Controles de autoría](comprobar_entrega.py) | Comprobar reconstrucción, fronteras y alteraciones | Opcional, separado del lab |

## 1. Qué se entrega y qué se reconstruye

| Elemento | Qué conserva | Qué falta por demostrar |
| --- | --- | --- |
| Captura o URL local | Apariencia o ubicación de una sesión temporal | Fuentes, entorno y ejecución futura |
| CSV/contexto descargados | Selección y filtros de una vista calculada | App, fuente completa y reconstrucción |
| Carpeta entregable | Código, datos sintéticos, metadatos, instrucciones y casos | Ejecución en otra copia y explicación de la persona |
| Reconstrucción revisada | Capacidad de recalcular desde los archivos incluidos | Aprendizaje, autoría y comportamiento no probado |

El preparador de esta lección crea una práctica con 18 archivos. Reúne las
fuentes de 12.08 y añade `entrega.py`, el README y los metadatos del entorno.
No instala paquetes, no ejecuta pruebas ni inicia la app.

Dentro de esa práctica, `entrega.py crear` calcula seis casos y genera una
carpeta de 36 archivos. Solo copia una lista explícita: no incorpora tu entorno,
otras salidas, caché, notas o credenciales por copiar todo el directorio.
El destino debe ser nuevo y estar fuera de la carpeta fuente. Una carpeta
parcial tras un fallo debe conservarse y revisarse; no se reutiliza.

## 2. Fuente, contrato y resultados que deben conservarse

Usamos seis registros sintéticos, incluidos por el preparador:

| ID | Segmento | Corte | Saldo MXN |
| --- | --- | --- | ---: |
| 001 | comercio | 2026-09-30 | 0 |
| 002 | servicios | 2026-09-30 | 2000 |
| 003 | comercio | 2026-09-30 | 2500 |
| 001 | comercio | 2026-10-31 | 100 |
| 002 | servicios | 2026-10-31 | 1900 |
| 003 | comercio | 2026-10-31 | 2600 |

Una fila es un crédito/corte; esa combinación es única. El ID conserva tres
dígitos como texto; segmento admite comercio/servicios; fecha ISO real entre
1900 y 2100; saldo entero entre 0 y 1000000 MXN. No se admiten ausencias,
duplicados, signos o decimales en el CSV. Cero es un importe conocido.
Se valida la fuente completa antes de filtrar.

Universo: todos los créditos del corte, antes de segmento y mínimo. Selección:
los que cumplen segmento y `saldo_mxn >= minimo_mxn`. Predice estos seis casos:

| Caso | Corte / segmento / mínimo | Selección por ID y saldo MXN | Universo | Métricas mostradas |
| --- | --- | --- | --- | --- |
| octubre | Octubre / ambos / 2000 | 003/2600 | 3/4600 | 1, 2600, 33.33% |
| septiembre | Septiembre / ambos / 2000 | 002/2000 y 003/2500 | 3/4500 | 2, 4500, 66.67% |
| frontera | Septiembre / ambos / 2001 | 003/2500 | 3/4500 | 1, 2500, 33.33% |
| servicios | Octubre / servicios / 1900 | 002/1900 | 3/4600 | 1, 1900, 33.33% |
| vacio | Octubre / ninguno / 0 | Sin filas | 3/4600 | 0, 0, 0.00% |
| sin_corte | Noviembre / ambos / 0 | Sin universo | Ausente | Sin métricas ni archivos de descarga |

El porcentaje usa **cantidad de créditos**, no proporción del saldo. El JSON del
modelo conserva precisión numérica; la interfaz redondea a dos decimales. Los
archivos se ordenan por ID; el contraste de la fuente usa ID/corte, sin depender
del orden original del CSV.

El contrato de esta entrega exige septiembre y octubre presentes y noviembre
sin registros. Una fuente vacía o sin esos cortes se rechaza antes de crear la
entrega. No se inventa una carpeta de cierre exitosa con datos inválidos. La app
y las pruebas de 12.08 siguen permitiendo explicar esos errores y recuperar la fuente.

## 3. Crear la entrega y entender sus archivos

Desde la raíz, con Python de tu entorno activado:

```text
python curriculum/12_streamlit/09_local_delivery/preparar_practica.py output/practica_1209
python output/practica_1209/entrega.py crear output/entrega_1209
```

Si usas uv, emplea los prefijos de tus [recorridos](recorridos.md). No ejecutes
el `entrega.py` fuente: los archivos reutilizados se reúnen en la práctica.

En [entrega.py](entrega.py), `crear` reutiliza `analizar` y `preparar_descargas`.
No vuelve a implementar la lógica de la app. La estructura resultante es:

```text
entrega_1209/
  README.md                 instrucciones para la persona receptora
  app.py, cartera.py, ...   código y pruebas reutilizados
  cartera.csv               fuente completa
  pyproject.toml, uv.lock   metadatos del entorno
  contrato.json             reglas, claves y seis filtros efectivos
  resultados/
    octubre/                analisis.json, seleccion.csv, contexto.json
    septiembre/             analisis.json, seleccion.csv, contexto.json
    frontera/               analisis.json, seleccion.csv, contexto.json
    servicios/              analisis.json, seleccion.csv, contexto.json
    vacio/                  analisis.json, seleccion.csv, contexto.json
    sin_corte/              solo analisis.json
  manifiesto.json           inventario y huellas SHA-256
```

Los pares de `resultados/` son archivos **calculados en terminal** con las
mismas funciones de salida; no prueban que alguien haya pulsado un botón de
descarga. En `vacio`, CSV conserva encabezado y JSON conserva universo válido.
En `sin_corte`, el análisis registra porcentaje `null`; no se ofrecen CSV/contexto
como descarga de cartera, porque la app tampoco los ofrece sin universo.

`manifiesto.json` identifica los archivos y sus huellas, salvo a sí mismo.
Una huella cambia al cambiar los bytes; no demuestra quién los creó ni qué
programa se ejecutó. La entrega no incluye registros que aparenten pruebas
aprobadas o una revisión humana ya realizada.

## 4. Verificar contra una referencia externa

Conserva una copia del CSV original separada de la entrega. Para el ejemplo,
puedes usar la fuente del repositorio. Ejecuta el revisor desde la práctica:

```text
python output/practica_1209/entrega.py verificar output/entrega_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

`verificar` solo lee. No importa ni ejecuta el código de la carpeta revisada.
Utiliza Python estándar para revisar el contrato y calcular una referencia
independiente del modelo de la app. Comprueba:

1. Inventario exacto y huellas de rutas conocidas. Rechaza faltantes o archivos
   extra; ignora `.venv` y `__pycache__`, que no se distribuyen.
2. Fuente completa frente al CSV externo por ID/corte y por todos sus valores.
   También valida registros fuera de la selección.
3. Los seis filtros y cada resultado: universo, filas completas, indicadores y
   ausencia de denominador. Booleanos no sustituyen cantidades enteras.
4. Campos, orden y valores de cada CSV, y filtros/universo/indicadores/huella
   de su contexto JSON. Los IDs deben conservar sus ceros iniciales.

El resultado base informa seis casos, seis filas de fuente y 36 archivos.
Un rechazo termina con código 2 y diagnóstico. No reescribe resultados ni
actualiza huellas para hacerlos pasar. `crear` y `verificar` son acciones
exclusivas: `--referencia` pertenece solo a `verificar`.

La referencia debe estar **fuera de la entrega**. Si usas el propio CSV alterado
como referencia y ajustas todo a él, pierdes el contraste. El revisor tampoco
autentica esa referencia externa; la persona revisora debe conservarla y conocer
su procedencia. Usa una copia de confianza de `entrega.py` al revisar otra carpeta:
un revisor que alguien modificó puede mentir.

**Predicción:** si intercambias 2000 y 2500 entre 002 y 003 de septiembre, el
total continúa en 4500. Aunque recalcules huellas, el contraste por clave debe
rechazar la fuente o los resultados alterados. El
[lab](../../../labs/12_streamlit/09_local_delivery/README.md) propone este experimento
en una copia separada; no modifiques la referencia que conserva tu compañero.

## 5. Reconstruir desde otra ubicación

Abre el README de la entrega. Debe bastar para operar sin consultar carpetas
anteriores del curso. Desde una terminal **dentro de `output/entrega_1209`**,
con el mismo entorno activado:

```text
python entrega.py crear ../reconstruida_1209
```

El constructor copia sus fuentes y recalcula resultados desde el CSV; no toma
los JSON de `resultados/` como entrada. El destino nuevo queda al lado, sin
copiar `.venv`, caché ni estado de sesión. Desde la raíz, compara esta nueva
carpeta con la misma referencia externa:

```text
python output/practica_1209/entrega.py verificar output/reconstruida_1209 --referencia curriculum/12_streamlit/03_data_interface/cartera.csv
```

Para comprobar también el entorno desde cero, el README explica uv y `.venv`
local con `uv sync --locked --group streamlit --python 3.12`. Conserva el lockfile
completo: contiene dependencias de otros módulos, no una lista mínima de Streamlit.
Sincronizar no significa instalar globalmente. Una primera sincronización puede
requerir red; disponer de la carpeta no garantiza reconstruir sin conexión.

Con Conda o venv/pip, reutiliza el entorno elegido si ya es compatible; consulta
los [recorridos iniciales](../01_first_app_execution/recorridos.md) si necesitas
prepararlo. Basta un gestor. No mezcles gestores sobre el mismo entorno.

Desde la raíz, con Python de tu entorno, ejecuta en la reconstrucción:

```text
python output/reconstruida_1209/pruebas_modelo.py
python output/reconstruida_1209/pruebas_app.py
```

La muestra base debe aprobar siete métodos de modelo y once AppTest. Como
repaso, `minimo_pruebas.py` añade un método. Las pruebas tienen expectativas
de las seis filas del curso; una variante legítima requiere revisar y justificar
sus propios casos, sin cambiar expectativas para ocultar errores.

**Pausa posible:** guarda la ubicación, el resultado del contraste y qué entorno
usaste. Para retomar no vuelvas a preparar sobre ninguna de esas carpetas.

## 6. Demostrar la app, no solo la carpeta

Inicia el `app.py` de la reconstrucción siguiendo los [recorridos](recorridos.md).
Abre la URL local; detén tu servidor con Ctrl+C al terminar. La URL y el estado
de la sesión son temporales. Entregar esta carpeta no publica un servicio ni
crea un archivo HTML autónomo.

Tu compañero elige casos y contrasta datos recuperables:

| Acción | Evidencia que debe poder revisar |
| --- | --- |
| Inicio octubre y envío septiembre | 003/2600 pasa a 002/2000 y 003/2500; tabla, barras y métricas coinciden |
| Borrador sin enviar y tabla oculta | No cambia la selección aplicada ni el contenido descargable |
| Servicios/1900 y luego 1901 | Frontera incluida y vacío válido; el universo sigue en 3/4600 |
| Mínimo decimal y corrección | Rechazo conserva filtros válidos, bloquea descarga y después recupera |
| Noviembre y regreso a octubre | Aviso sin métricas/descargas; recuperación al aplicar filtros válidos |
| Dos descargas reales | CSV/JSON guardados fuera de la entrega, releídos y contrastados por clave |
| Recarga o reinicio | Inicio de octubre y contador 0; no conserva una bitácora de aprendizaje |
| Teclado y ventana estrecha | Controles alcanzables, etiquetas legibles y problemas registrados |

El [revisor de pares](../07_tables_charts_download/revisar_descarga.py) comprueba
coherencia de CSV/contexto; no reemplaza la referencia externa por fila. Guarda
una nota fuera de la entrega: entorno, fecha, filtros, predicción, resultado,
ayudas y dudas. No afirmes que la revisión humana está completa por aprobar
AppTest o el verificador de archivos.

## 7. Límites que deben acompañar la entrega

- **Estado:** los filtros válidos pertenecen a una sesión; no son almacenamiento
  permanente. No se promete recuperar borradores sin enviar tras otras interacciones.
- **Caché:** clave con filas/filtros/versión, TTL 60, ocho entradas y sin disco.
  Lectura y validación ocurren antes; no acredita evitar lectura ni rendimiento.
- **Descarga:** bytes de la vista calculada, `on_click="ignore"`. Si cambió el
  CSV, relee y revisa antes de descargar. El clic no valida la fuente otra vez.
- **Verificación:** datos y estructura frente a referencia externa; no certifica
  autoría, sesiones pasadas, código correcto para todos los casos ni accesibilidad.
- **Alcance:** entrega local sin cuentas ni despliegue. Multipágina, fragments,
  autenticación y publicación son ampliaciones que requieren una necesidad propia.

## Práctica

Realiza el [lab 12.09](../../../labs/12_streamlit/09_local_delivery/README.md):
crea y reconstruye la entrega, detecta una alteración con total conservado y
demuestra casos elegidos por otra persona. Las fuentes incluidas bastan.

## Evidencia y criterio de salida

| Conserva | Comprueba | Explica |
| --- | --- | --- |
| Entrega y reconstrucción nuevas | Fuentes y seis casos conciliados contra referencia externa | Qué necesita la persona receptora |
| Resultados de pruebas y un rechazo deliberado | Valores por ID/corte, frontera y recuperación | Por qué suma/huella no bastan |
| Dos pares descargados y nota de demostración | Coinciden con filtros aplicados y datos por clave | Diferencia entre resultado preparado y descarga real |
| Entorno y límites documentados | Reinicio y ejecución desde otra carpeta | Sesión, caché, lectura y alcance local |

El cierre de tu práctica requiere reconstruir, demostrar y justificar esas
decisiones con tu compañero. Disponer de los nueve labs no acredita aprendizaje.
No hay proyecto integrador ni checkpoints de Streamlit implementados por este cierre;
el catálogo de [proyectos](../../../projects/README.md) conserva su estado propio.

## Referencias

Fuentes oficiales consultadas el 2026-10-28; ejemplos propios con Python 3.12.12,
Streamlit 1.66.1 y Altair 6.3.0. La documentación web puede mostrar versiones distintas.

- [Streamlit: estado de sesión](https://docs.streamlit.io/develop/concepts/architecture/session-state)
  y [caché](https://docs.streamlit.io/develop/concepts/architecture/caching).
- [uv: trabajar con proyectos](https://docs.astral.sh/uv/guides/projects/),
  para metadatos, lockfile y entornos locales.
- [Python 3.12: hashlib](https://docs.python.org/3.12/library/hashlib.html),
  [CSV](https://docs.python.org/3.12/library/csv.html) y
  [JSON](https://docs.python.org/3.12/library/json.html).

## Siguiente paso

Revisa el [cierre del módulo](../README.md#criterio-de-salida) y conserva tus
pendientes personales. Streamlit y [Shiny (13)](../../13_shiny_web/README.md)
son alternativas; no necesitas ambas aplicaciones. El siguiente tramo de
integración es [14.01 — Pregunta y contrato del producto](../../14_reproducible_projects/01_product_question_contract/README.md),
disponible con lección y lab; 14.02–14.08 también tienen lecciones/labs y 14.09 sigue planificada. Distingue los ocho labs disponibles de las secciones aún planificadas.

---

[← 12.08](../08_app_testing/README.md) · [Módulo 12](../README.md) · [Lab 12.09 →](../../../labs/12_streamlit/09_local_delivery/README.md)

# Explorador local — entrega de Streamlit 12.09

Esta carpeta contiene la app, sus fuentes sintéticas, pruebas, seis casos de
terminal y los metadatos bloqueados del curso. No contiene un entorno instalado,
un servidor activo, credenciales ni historial de sesiones del navegador.

## Datos y contrato

Cada fila de cartera.csv representa un crédito en un corte. La clave es
id_credito/fecha_corte. ID: tres dígitos conservados como texto; segmento:
comercio o servicios; fecha ISO real, años 1900–2100; saldo: pesos enteros de
0 a 1000000, incluidos ceros conocidos. No se admiten ausencias ni claves
repetidas. Se valida la fuente completa antes de filtrar.

El cierre requiere registros en septiembre y octubre de 2026 y noviembre sin
registros. La referencia del curso tiene seis filas. Si recibes otra variante,
conserva su referencia externa y documenta los valores esperados antes de usarla.

## Qué contienen los archivos

| Archivo o grupo | Función |
| --- | --- |
| app.py | Interfaz local: formulario, métricas, gráfico, tabla y descargas |
| cartera.py, configuracion.py, ejecutar.py | Contrato, lectura, análisis y consumidor JSON |
| cache_analisis.py, entradas.py | Caché de análisis y mínimo textual validado |
| graficos.py, salidas.py, revisar_descarga.py | Gráfico, bytes CSV/JSON y relectura de un par |
| minimo.py, minimo_pruebas.py, pruebas_modelo.py, pruebas_app.py | Mínimo y suites de 12.08 |
| entrega.py, contrato.json | Crear otra entrega y verificar esta con una referencia externa |
| pyproject.toml, uv.lock | Metadatos completos del curso, copiados sin cambios |
| resultados/ | Seis análisis JSON y cinco pares CSV/JSON calculados en terminal |
| manifiesto.json | Inventario de archivos con SHA-256, excepto el propio manifiesto |

Los archivos de resultados/ fueron preparados por Python en terminal: no son
descargas del navegador ni acreditan que alguien haya ejecutado las pruebas.
El mínimo es autónomo; la app completa usa cartera.csv. No ejecutes app.py
con `python app.py`: inicia Streamlit como se indica abajo.

## Entorno y reconstrucción

Referencia comprobada: Python 3.12.12, Streamlit 1.66.1, Altair 6.3.0. Para la
inspección opcional del gráfico en AppTest se usa PyArrow 21.0.0, ya declarado.
El lockfile incluye herramientas de otros módulos; no se recortó ni recalculó
para esta entrega. No implica que toda dependencia del curso sea necesaria
para diseñar una app Streamlit.

Conserva juntos los archivos y abre la terminal **dentro de esta carpeta**.
Si ya tienes un entorno compatible, actívalo y usa los comandos Python del
apartado siguiente. Para una reconstrucción local con uv, elige un solo shell.
Esto crea .venv en esta copia; no modifica entornos globales. La primera
sincronización puede necesitar conexión para obtener paquetes bloqueados.

### PowerShell

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".venv"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python minimo_pruebas.py
uv run --locked --group streamlit python pruebas_modelo.py
uv run --locked --group streamlit python pruebas_app.py
uv run --locked --group streamlit python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### Bash/Zsh

```bash
export UV_PROJECT_ENVIRONMENT=".venv"
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python minimo_pruebas.py
uv run --locked --group streamlit python pruebas_modelo.py
uv run --locked --group streamlit python pruebas_app.py
uv run --locked --group streamlit python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

### CMD / Anaconda Prompt

```bat
set UV_PROJECT_ENVIRONMENT=.venv
uv sync --locked --group streamlit --python 3.12
uv run --locked --group streamlit python minimo_pruebas.py
uv run --locked --group streamlit python pruebas_modelo.py
uv run --locked --group streamlit python pruebas_app.py
uv run --locked --group streamlit python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

## Si ya tienes Conda o venv/pip activado

Comandos iguales en PowerShell, Bash/Zsh y Anaconda Prompt, desde esta carpeta:

```text
python minimo_pruebas.py
python pruebas_modelo.py
python pruebas_app.py
python ejecutar.py --corte 2026-09-30 --minimo 2000
python -m streamlit run app.py --server.address 127.0.0.1 --browser.gatherUsageStats false
```

Las suites originales esperan la muestra de seis filas del curso: 1, 7 y 11
métodos aprobados. Si preparaste una variante de datos, esas expectativas no
cambian solas; revísalas y justifícalas en una copia de trabajo antes de emitir
otra entrega. El verificador de datos usa la referencia externa que indiques.

Abre la URL local mostrada. El servidor ocupa esa terminal hasta Ctrl+C. Si el
puerto está ocupado, añade `--server.port 8509`; no cierres procesos ajenos.
Para reiniciar, repite solo streamlit run. Una persona receptora necesita
Python, dependencias y capacidad de ejecutar archivos locales; enviar esta
carpeta no convierte la app en un HTML que funcione sin servidor.

## Casos de referencia del curso

El universo es todo el corte antes de segmento y mínimo. En septiembre hay
3 créditos/4500 MXN; en octubre, 3/4600 MXN. Ambos segmentos salvo donde se indica:

| Caso | Filtros | Selección | Cantidad / saldo MXN / porcentaje |
| --- | --- | --- | --- |
| octubre | 2026-10-31, mínimo 2000 | 003/2600 | 1 / 2600 / 33.33% |
| septiembre | 2026-09-30, mínimo 2000 | 002/2000 y 003/2500 | 2 / 4500 / 66.67% |
| frontera | 2026-09-30, mínimo 2001 | 003/2500 | 1 / 2500 / 33.33% |
| servicios | 2026-10-31, servicios, mínimo 1900 | 002/1900 | 1 / 1900 / 33.33% |
| vacio | 2026-10-31, ningún segmento, mínimo 0 | Sin filas | 0 / 0 / 0.00% |
| sin_corte | 2026-11-30, mínimo 0 | Sin universo | Sin métricas ni descargas en app |

resultados/sin_corte/analisis.json conserva cantidad/saldo de selección cero y
porcentaje null del modelo; la interfaz explica la falta de universo y no
presenta ese corte como saldo observado cero. No se generan CSV/contexto para
este caso. En vacio sí hay universo válido: se genera CSV con encabezado y contexto.

## Verificar la entrega sin ejecutarla

Conserva una copia de referencia del CSV **fuera** de esta carpeta y fuera de
sus reconstrucciones. Desde esta carpeta, sustituye la ruta de ejemplo por
ese archivo que la persona revisora conserva:

```text
python entrega.py verificar . --referencia "../referencia_cartera.csv"
```

Con uv antepón `uv run --locked --group streamlit`. El verificador también
funciona con Python estándar y no instala paquetes. Revisa inventario,
contrato, huellas, fuente completa por ID/corte, filtros y todos los valores
de cada análisis/CSV/contexto contra una referencia calculada sin importar el
modelo de la app. No ejecuta código de la entrega que recibe.

La propia copia de entrega.py puede modificarse. Para revisar una carpeta de
procedencia incierta, utiliza una copia conservada del revisor y del CSV fuera
de ella. Ni el SHA-256 ni una copia que se comprueba a sí misma autentican el
origen. Un verificador aprobado tampoco demuestra el comportamiento actual de
la app: ejecuta sus pruebas y completa la revisión del navegador por separado.

Si falta un archivo, una huella no coincide o cambia un valor, no regeneres
el manifiesto para ocultarlo. Conserva el diagnóstico, corrige la copia de
trabajo y genera otra entrega. La verificación solo lee y termina con código 2
ante un rechazo. Una entrega parcial tras un fallo de escritura debe conservarse
y revisarse; no reutilices ese destino.

## Reconstruir otra entrega

Desde esta carpeta, con el mismo Python, elige un destino nuevo situado fuera
de ella, por ejemplo un hermano que todavía no exista:

```text
python entrega.py crear ../entrega_reconstruida
python entrega.py verificar ../entrega_reconstruida --referencia ../referencia_cartera.csv
```

No necesitas el repositorio original para estos comandos. La reconstrucción
recalcula resultados desde fuentes y archivos incluidos; no copia una sesión
ni reutiliza los JSON calculados como verdad. No transporta .venv, caché ni
bytecode; crea el entorno en cada copia cuando haga falta. El verificador ignora
.venv y __pycache__, no los distribuyas con la entrega. Los demás archivos extra
se rechazan: guarda descargas y notas personales en otra carpeta.

## Demostración y límites

Contrasta octubre, septiembre, servicios, vacío y corte ausente. Rechaza un
mínimo decimal, confirma filtros válidos y comprueba recuperación. Editar sin
enviar no aplica filtros; ocultar tabla no cambia los bytes descargados.
Guarda dos pares CSV/JSON reales en una carpeta personal externa y relee:

```text
python revisar_descarga.py "ruta/seleccion.csv" "ruta/contexto.json"
```

Ese revisor comprueba coherencia del par; compara además las cuatro columnas
con tu referencia por ID/corte. La huella no sustituye ese contraste.

La lectura y validación ocurren antes de caché. La clave incluye filas completas,
filtros y versión; TTL 60 segundos, máximo ocho entradas, sin disco. No acredita
evitar lectura ni rendimiento. Session State conserva filtros válidos de una
sesión, no una bitácora: recargar o reiniciar vuelve al inicio. Descargas usan
bytes de la vista calculada; si cambió la fuente, relee antes de descargar.
Rechazo de filtros bloquea descargas hasta confirmar filtros válidos.

Conserva fuera de la entrega una nota con fecha, entorno, filtros, predicción,
resultado, ayudas, problemas observados y siguiente paso. Registra teclado,
ventana estrecha y navegador revisados. Una demostración, prueba o carpeta
generada no acredita por sí sola aprendizaje, accesibilidad completa ni
autenticidad. No hay despliegue, autenticación ni progreso sincronizado.

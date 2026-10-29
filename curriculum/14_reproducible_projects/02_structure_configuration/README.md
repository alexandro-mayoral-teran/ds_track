# 14.02 — Estructura y configuración

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **Lección 14.02**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Localizar responsabilidades y ejecutar una consulta con parámetros explícitos |
| **Necesitas** | Contrato 14.01, archivos/rutas y funciones; elige Python o R |
| **Evidencia** | Copia organizada, dos configuraciones y resultados conciliados desde otra carpeta |

[Empezar](#antes-de-empezar) · [Ir al lab](../../../labs/14_reproducible_projects/02_structure_configuration/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

El contrato de 14.01 define qué queremos responder. Ahora necesitamos localizar
la entrada, el cálculo y los parámetros sin buscar valores repartidos por scripts
ni depender de un objeto que quedó en la consola. Organizar es asignar
responsabilidades; crear muchas carpetas no garantiza esa separación.

Un cambio de corte debe poder declararse como configuración. Un cambio de
denominador altera el contrato y necesita revisar código/criterios. Esta distinción
permite variar una consulta conservando el significado de sus resultados.

## Antes de empezar

- Revisa [14.01 — Pregunta y contrato](../01_product_question_contract/README.md)
  y su especificación. No necesitas conservar tu entrega anterior: el preparador
  copia contrato, muestra y criterios conocidos.
- Para rutas consulta [00.02](../../00_getting_started/02_terminal_paths/README.md);
  para separación de funciones, [05 — Python aplicado](../../05_python_applied/README.md)
  o [06.06 — Funciones R](../../06_r_foundations/06_functions_control/README.md).
- Sigue [recorridos.md](recorridos.md) en un destino nuevo. Python estándar o
  R base bastan; no hay paquetes, lockfiles, entornos, reporte/app o pipeline nuevos.
  La reconstrucción de entornos se practica en [14.03](../03_reconstructible_environments/README.md), ya disponible.

## Qué vas a aprender

- Distinguir entrada preservada, contrato, parámetros, código y salidas regenerables.
- Resolver rutas respecto a una raíz explícita, no a la carpeta actual por accidente.
- Validar nombres, valores y destinos de una configuración antes de calcular.
- Cambiar preguntas mediante archivos de parámetros sin cambiar las reglas.
- Explicar qué se conserva al mover una carpeta y qué requiere revisión posterior.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [preparar.py](preparar.py), [preparar.R](preparar.R), [recorridos.md](recorridos.md) | Crear una copia de trece archivos útiles | Elige una alternativa |
| [LEEME de la copia](plantilla/LEEME.md) | Responsabilidades, ejecución y formato de configuración | Esencial |
| [consulta.csv](plantilla/config/consulta.csv) | Siete parámetros/rutas declarados | Esencial |
| [Modelo Python](plantilla/codigo/modelo.py), [modelo R](plantilla/codigo/modelo.R) | Lectura/contrato/cálculo separados del punto de entrada | Elige un lenguaje |
| [Configuración Python](plantilla/codigo/configuracion.py), [configuración R](plantilla/codigo/configuracion.R) | Leer y validar claves, valores y rutas | Elige un lenguaje |
| [revisar.py](plantilla/revisar.py), [revisar.R](plantilla/revisar.R) | Coordinar una consulta, sin generar productos | Punto de entrada |
| [Contrato](../01_product_question_contract/ESPECIFICACION.md), [CSV](../01_product_question_contract/cartera.csv), [criterios](../01_product_question_contract/criterios.csv) | Pregunta, fuente y expectativas conservadas | Se copian automáticamente |
| [Salidas](plantilla/salidas/LEEME.md) | Diferenciar destino declarado de resultado generado | Esencial |

## 1. Una muestra pequeña para separar responsabilidades

Imagina dos ventas V01=100 y V02=200 MXN. La entrada contiene las dos ventas;
la regla selecciona importe >= mínimo; la configuración establece mínimo=200;
el resultado es V02/200. Cambiar mínimo a 100 es otra consulta. Cambiar >= por >
es otra regla: V02 ya no cumpliría mínimo=200.

Guardar el mínimo dentro de la función de sumar mezcla una elección con el
cálculo. Guardar la selección encima del CSV fuente destruye el universo para
la siguiente consulta. Separaremos ambas cosas antes de conectar productos.

## 2. Una estructura con archivos que cumplen una función

El preparador reúne esta copia, sin instalar ni calcular:

```text
practica_1402/
  LEEME.md
  revisar.py / revisar.R
  config/consulta.csv
  codigo/modelo.py / modelo.R
  codigo/configuracion.py / configuracion.R
  docs/ESPECIFICACION.md
  docs/plantilla_contrato.md
  datos/entrada/cartera.csv
  referencia/criterios.csv
  salidas/LEEME.md
```

Las parejas Python/R son alternativas, no una obligación de hacer dos proyectos.
Tampoco son los módulos Shiny de interfaz de 13.08: aquí módulo se refiere a
código reutilizable que define funciones. Importar/cargar modelo o configuración
no lee la fuente ni crea resultados; el punto de entrada coordina esas acciones.

datos/entrada conserva el CSV. docs define lo acordado; referencia conserva
expectativas, que no se usan como datos para producir la consulta. config cambia
elecciones permitidas. codigo define cómo validar/calcular. salidas está destinada
a resultados regenerables, sin convertirse en otra fuente escondida.

No hay carpetas de reporte/app vacías para simular avances. El LEEME de salidas
explica por qué en esta sección no se genera nada ahí. projects/ y sus checkpoints
siguen pendientes; esta es una copia didáctica útil, no el producto final integrado.

## 3. Raíz del proyecto frente a directorio actual

Una ruta relativa como datos/entrada/cartera.csv necesita un punto de partida.
El directorio actual es donde está trabajando el proceso; puede ser la raíz,
otra práctica o una terminal abierta en otro lugar. No se vuelve la carpeta del
script por el simple hecho de ejecutarlo.

Python obtiene la raíz desde `Path(__file__).resolve().parent` en revisar.py.
Luego carga los módulos locales y resuelve la configuración/entrada respecto
a esa raíz. En R la función recibe `raiz` explícitamente; puedes cargar revisar.R
por su ruta y pasar la carpeta del proyecto sin cambiar getwd().

```r
source("output/practica_1402/revisar.R")
revisar_proyecto("output/practica_1402")
```

Estas rutas iniciales son relativas a la consola que lanza la acción. Una vez
identificada la raíz, las rutas de config se interpretan respecto al proyecto,
no respecto a config/ ni al lugar desde donde se abrió la terminal. Por eso
puedes mover la copia completa; no necesitas editar una ruta personal dentro
de la configuración. Debes seguir indicando dónde encontrar el punto de entrada.

## 4. Configuración explícita y validada

config/consulta.csv es CSV UTF-8, dos columnas clave/valor y siete claves únicas:

| Clave | Inicial | Qué controla |
| --- | --- | --- |
| version_reglas | 1401-v1 | Contrato conocido; una versión desconocida se rechaza |
| entrada | datos/entrada/cartera.csv | Fuente preservada existente dentro del proyecto |
| corte | 2026-10-31 | Universo solicitado |
| segmentos | comercio\|servicios | Categorías elegidas; ninguno significa selección vacía |
| minimo_texto | 2000 | Saldo >= mínimo, pesos enteros canónicos |
| app | shiny | Alternativa prevista, no instalación/arranque |
| salida | salidas/octubre | Destino nuevo previsto, no generado ni reservado |

Los lectores leen todos los valores como texto antes de validar. CSV no aporta
por sí solo tipos o reglas: 2000.0, espacios, etiquetas desconocidas y claves
duplicadas no se corrigen silenciosamente. Falta de clave, extra o repetición
detiene la revisión. No se mezcla archivo con variables de entorno o defaults
que puedan esconder la consulta efectiva; se muestra todo lo utilizado.

La raíz y los nombres de código no se guardan como rutas personales. Las rutas
de entrada/configuración usan /, componentes relativos y archivos existentes
dentro de la raíz, sin .. ni unidades Windows. El destino usa salidas/nombre_simple
libre; si existe, se rechaza aunque esta revisión no escriba en él. Consulta el
LEEME para el formato exacto. Estas restricciones didácticas no son una garantía
de aislamiento ante código no confiable o cambios concurrentes del sistema.

## 5. Reorganizar sin alterar indicadores

Conservamos las seis observaciones de 14.01: tres créditos en septiembre con
saldos 0/2000/2500 y los mismos tres en octubre con 100/1900/2600; segmentos
comercio/servicios/comercio. Clave ID/corte, pesos enteros conocidos y fuente
completa validada antes de filtrar. El denominador son los créditos del corte.

El caso inicial octubre/ambos/2000 da **003=2600 MXN**, universo tres/4600 y
cobertura 100/3≈33.33%. Copia la configuración a config/septiembre.csv y cambia
corte a 2026-09-30 y salida a salidas/septiembre: obtendrás 002=2000 y 003=2500,
4500 MXN y 2/3≈66.67%. El código y la fuente permanecen iguales.

En comercio/mínimos 0 y 1 cambia la cantidad pero no la suma de 2500 MXN:
001 tiene cero conocido. Ninguno produce selección vacía sobre universo; noviembre
no publica medidas. Una configuración inválida se rechaza antes de calcular,
sin simular las políticas de una sesión de app anterior.

Los modelos reorganizan las funciones de referencia de 14.01: separar lectura,
validación y cálculo no autoriza a cambiar >=, claves o denominador. Los nueve
criterios originales siguen en referencia/ para contrastar; la aceptación de
reporte/app aún requiere implementación y revisión futura.

## 6. Qué demuestra la revisión y qué falta

revisar.py y revisar.R leen configuración/fuente y muestran parámetros y resultado.
No escriben CSV, HTML, figuras ni registros de ejecución. Python evita cachés
de bytecode desde su punto de entrada. Repetir la revisión no genera dos entregas
ni reserva una ruta para el futuro: otra operación podría ocuparla después.

Un archivo de configuración no es un historial de lo que ocurrió, ni contiene
las dependencias del entorno. Las siguientes secciones desarrollarán entornos,
reprocesamiento, pruebas y trazabilidad. CI, publicación y autenticación continúan
como ampliaciones; no hacen falta para comprender la estructura.

## Práctica

Continúa con el [lab 14.02](../../../labs/14_reproducible_projects/02_structure_configuration/README.md):
preparar una copia, modificar una consulta y revisar resultados desde otra carpeta.

## Evidencia y criterio de salida

Conserva las dos configuraciones, predicciones y resultados por crédito, un
rechazo explicado y una nota de ejecución desde otra carpeta. Otra persona
debe localizar dónde cambiar un corte, dónde validar datos y dónde conservar
entrada/resultados sin adivinar rutas ni modificar reglas para cada consulta.

## Siguiente paso

Continúa con [14.03 — Entornos y ejecución reconstruible](../03_reconstructible_environments/README.md),
disponible con lección y lab. Tener estructura/configuración no acredita haber integrado
el producto, restaurado entornos nuevos o completado proyectos/checkpoints.

## Referencias primarias

Ejemplos propios; APIs contrastadas con Python 3.12 y R base:

- [Python: pathlib](https://docs.python.org/3.12/library/pathlib.html): rutas relativas y resolución explícita.
- [Python: csv](https://docs.python.org/3.12/library/csv.html): lectura textual y dialectos; validar es una responsabilidad adicional.
- [R: normalizePath](https://stat.ethz.ch/R-manual/R-devel/library/base/html/normalizePath.html): rutas existentes en forma canónica y límites por plataforma.

# 13.10 — Cierre y entrega local

[Inicio](../../../README.md) / [Módulo 13](../README.md) / **Lección 13.10**

**Otra persona debe poder abrir, reconstruir y comprobar el explorador que recibe.**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Entregar fuentes, reglas, entorno e indicadores recuperables |
| **Necesitas** | Consulta aplicada, validación, salidas, módulos y pruebas de 13.04–13.09 |
| **Evidencia** | Entrega verificada, reconstrucción en otra carpeta y demostración documentada |

[Preparación](#antes-de-empezar) · [Lab 13.10](../../../labs/13_shiny_web/10_local_delivery/README.md) · [Comprobar](#evidencia-y-criterio-de-salida)

## Propósito

Si una app funciona gracias a un objeto que quedó en tu consola o una ruta
personal, copiar app.R no basta para compartirla. Este cierre reúne lo que
otra persona necesita para recalcular y revisar los resultados desde cero.
Conservamos la app modular de 13.08 y las pruebas de 13.09; la capacidad nueva
es construir, verificar y reconstruir una entrega local completa.

Ejemplo pequeño: de dos ventas de 100 y 200 MXN seleccionas la de 200. Un CSV
con esa venta no conserva el universo de dos ventas/300 MXN, la regla del
filtro ni el código que la produjo. Para reconstruir necesitas fuente, contrato,
reglas, entorno e instrucciones, además de evidencia de resultados.

Con esta sección quedan disponibles las **diez lecciones y labs de Shiny**.
Esto describe material educativo: la práctica personal y los proyectos/checkpoints
requieren evidencia propia. 14.01–14.05 ofrecen diseño, configuración, entornos,
pipeline y pruebas; 14.06–14.09 y la integración final siguen planificadas. Publicar un servidor en Internet es una ampliación.

## Antes de empezar

- Revisa [13.04 — Filtros](../04_shared_filters/README.md),
  [13.05 — Estado](../05_events_session/README.md),
  [13.06 — Mensajes](../06_validation_messages/README.md),
  [13.07 — Salidas](../07_outputs_downloads/README.md),
  [13.08 — Módulos](../08_organization_modules/README.md) y
  [13.09 — Pruebas](../09_tests_flow/README.md).
- Sigue [recorridos.md](recorridos.md): primero una práctica nueva, después
  una entrega nueva y finalmente otra reconstrucción. No se exigen archivos
  producidos en labs anteriores; el preparador reúne las fuentes necesarias.
- R 4.6.1, Shiny 1.14.0, ggplot2 4.0.3 y renv 1.3.1 son las referencias
  comprobadas. Se conservan los 42 registros del lockfile de 13.07. No hay
  dependencias nuevas ni cambios de bibliotecas globales.
- Revisa el código antes de ejecutarlo. Conserva las notas humanas, capturas
  y descargas personales fuera de la carpeta que entregarás.

## Qué vas a aprender

- Distinguir descarga de una vista, carpeta de trabajo y entrega reconstruible.
- Conservar fuente, contrato, código, versiones y preguntas de referencia.
- Verificar valores por clave contra una referencia externa, además de huellas.
- Restaurar el entorno y recalcular en otra carpeta sin depender del repositorio.
- Demostrar la app y explicar los límites de sesiones, descargas y evidencia.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [preparar_app.R](preparar_app.R), [recorridos.md](recorridos.md) | Preparar práctica y separar entrega/reconstrucción | Esencial; elige IDE o terminal |
| [entrega.R](entrega.R) | Constructor y verificador de solo lectura | Esencial |
| [LEEME.md](LEEME.md) | Instrucciones autocontenidas que recibe otra persona | Incluido en la entrega |
| [CONTRATO.md](CONTRATO.md), [casos.csv](casos.csv) | Fuente, unidades, claves y seis preguntas | Incluidos en la entrega |
| [App](../08_organization_modules/app.R), [módulo](../08_organization_modules/consulta_module.R) | Explorador de dos consultas | Reutilizados sin cambios |
| [Funciones](../04_shared_filters/cartera.R), [consulta](../05_events_session/consulta.R), [validación](../06_validation_messages/validacion.R), [presentación](../07_outputs_downloads/presentacion.R) | Transformación, estado y salidas | Reutilizados sin cambios |
| [Pruebas](../09_tests_flow/ejecutar_pruebas.R) y [mínimo](../09_tests_flow/minimo.R) | Comprobar cálculo/transiciones y repasar dependencias | Se copian con los tres archivos de pruebas |
| [CSV](../../12_streamlit/03_data_interface/cartera.csv), [DESCRIPTION](../07_outputs_downloads/DESCRIPTION), [lockfile](../07_outputs_downloads/renv.lock) | Fuente/entorno conocidos | Se copian sin cambios |

## 1. Qué conservar en cada carpeta

| Elemento | Conserva | Comprobación necesaria |
| --- | --- | --- |
| Descarga selección/contexto | Una consulta aplicada, filtro y medidas | Releer ambos antes de aplicar otra consulta |
| Carpeta de práctica | Fuentes y entorno de trabajo local | Pruebas y observación personal |
| Entrega | Fuentes, contrato, entorno declarado y resultados de referencia | Contraste externo e inventario |
| Reconstrucción | Nueva biblioteca y nuevos resultados desde lo recibido | Sesión limpia, pruebas y navegador |

El preparador reúne **24 fuentes** en un destino nuevo. No instala ni ejecuta
la app. El constructor copia una lista explícita, sin arrastrar renv/library,
.renv-local, .RData, cachés o tus otros archivos de trabajo. Una entrega base
terminada contiene **41 archivos**: las 24 fuentes, resumen.csv, INFORME.md,
huellas.csv y 14 resultados de casos.

Una URL local no sustituye esta carpeta. `127.0.0.1` es el propio equipo;
la persona receptora debe iniciar su proceso R. Guardar la página del navegador
no conserva el servidor ni sus futuras interacciones.

## 2. Fuente y resultados conocidos

La fuente es sintética. Cada fila identifica un crédito en un corte, clave
ID/fecha; el saldo está en pesos enteros. No se admiten ausencias ni duplicados.

| Crédito / segmento | Septiembre 2026-09-30 | Octubre 2026-10-31 |
| --- | ---: | ---: |
| 001 / comercio | 0 | 100 |
| 002 / servicios | 2000 | 1900 |
| 003 / comercio | 2500 | 2600 |

Son seis observaciones, tres créditos por fecha y universos 4500/4600 MXN.
Se valida toda la fuente antes de seleccionar un corte. El filtro combina
segmentos elegidos con saldo >= mínimo; ninguno significa selección vacía.
La cobertura usa todos los créditos del corte como denominador.

| Caso | Filtros | IDs | Saldo seleccionado | Cobertura |
| --- | --- | --- | ---: | ---: |
| septiembre | Septiembre / ambos / 2000 | 002, 003 | 4500 | 2/3 |
| octubre | Octubre / ambos / 2000 | 003 | 2600 | 1/3 |
| cero | Septiembre / comercio / 0 | 001, 003 | 2500 | 2/3 |
| frontera | Septiembre / comercio / 1 | 003 | 2500 | 1/3 |
| vacio | Septiembre / ninguno / 0 | Ninguno | 0 | 0/3 |
| sin_universo | Noviembre / ambos / 2000 | Sin corte | Ausente | Sin denominador |

Cero y frontera tienen la misma suma y distinta cantidad de créditos. Comparar
solo totales no basta. En resumen.csv, sin_universo conserva universo 0 y deja
vacías las medidas de selección/porcentaje, como ausencia explícita de indicador
publicable. No lo presenta como 0%. CONTRATO.md detalla estas decisiones.

## 3. Crear la entrega después de comprobar la práctica

Desde la consola R de la copia preparada/restaurada, detén tu servidor antes
de trabajar con archivos. Ejecuta las pruebas y luego el constructor:

```r
source("ejecutar_pruebas.R")
source("entrega.R")
crear_entrega("../entrega_1310")
```

El padre del destino debe existir; la carpeta final debe ser nueva y estar
fuera de origen. Si falla y deja una copia parcial, consérvala para revisar
y elige otro nombre; no sobrescribas trabajo anterior. El constructor:

1. Comprueba las fuentes y las seis preguntas fijadas por el cierre.
2. Copia las 24 fuentes, incluyendo .Rprofile, activador/configuración renv y lockfile.
3. Recalcula los seis casos con las funciones de la app.
4. Escribe cinco selecciones y cinco contextos CSV, más cuatro PNG de 960 × 600.
5. Guarda resumen/nota de generación/huellas y verifica contra la fuente externa de la práctica.

Vacío tiene CSV selección con encabezado y contexto con una fila, sin figura.
Sin universo no genera CSV de vista ni PNG. Las cuatro figuras usan el mismo
creador ggplot que la app, con objeto explícito y dimensiones fijas.

Los resultados del lote **no son descargas de una sesión web pasada**. Representan
preguntas fijas recalculadas al construir. La interacción en navegador debe
demostrarse por separado; no se deduce de estos archivos.

## 4. Verificar con una referencia externa

Una **huella** resume bytes para detectar cambios. huellas.csv declara MD5 de
los archivos incluidos, salvo ella misma. Detecta pérdidas/cambios accidentales
respecto a ese inventario, pero no aporta una firma: puede modificarse junto
con un archivo erróneo. No acredita autenticidad ni ejecución histórica.

Desde la práctica, usando entrega.R revisado:

```r
verificar_entrega("../entrega_1310", referencia = "cartera.csv")
```

La referencia debe estar fuera de la carpeta verificada y ser una fuente que
hayas revisado. El verificador usa R base, reconstruye resultados con una ruta
independiente y no llama a las funciones recibidas para decidir qué es correcto.
Compara todos los valores de la fuente por clave y las tablas de resultados;
un par de errores que conserve la suma debe rechazarse. También revisa nombres,
ausencias, seis preguntas, inventario, huellas y cabecera/dimensiones PNG.

Solo lee. No inicia la app, ejecuta .Rprofile, instala paquetes ni escribe en
la entrega. Para revisar una carpeta alterada, usa un verificador de confianza
fuera de ella: un programa que también fue modificado no puede ser su propia
garantía. La independencia depende de la referencia y el código elegidos.

**Límites:** una cabecera PNG correcta no demuestra que su gráfico sea correcto;
revisar las figuras y reconstruir sigue siendo necesario. Las huellas de código
no prueban que su lógica esté bien. INFORME.md es texto generado, con revisión
humana pendiente; no autentica una demostración anterior. El inventario tampoco
certifica que cualquier archivo añadido por ti sea apropiado para compartir.

## 5. Reconstruir desde lo recibido

Conserva la entrega original. Crea otra carpeta y copia solo sus 24 fuentes
declaradas en archivos_cierre(), incluyendo los archivos ocultos. No copies
la biblioteca instalada ni los resultados: queremos volver a obtenerlos.
Los [recorridos](recorridos.md) incluyen el bloque exacto de copia.

Abre shiny_1310.Rproj de la reconstrucción, reinicia R, restaura y ejecuta las
pruebas completas. Debe poder funcionar sin leer el repositorio original.
Después crea otra entrega en un destino nuevo y verifícala con el CSV de la
entrega recibida como referencia externa. La comparación de PNG entre sistemas
no exige bytes idénticos: fuentes/dispositivos pueden variar; revisa datos,
dimensiones, etiquetas y aspecto.

El lockfile declara versiones de paquetes R; no incluye el intérprete, sistema,
navegador, fuentes ni disponibilidad futura de repositorios. renv::restore
reconstruye la biblioteca local cuando esas versiones están disponibles.
Si falla, registra el diagnóstico y resuelve la causa; no sustituyas versiones
silenciosamente para afirmar que reprodujiste el entorno bloqueado.

## 6. Demostración de cierre

Con la reconstrucción, inicia app.R siguiendo LEEME.md. A debe mostrar
septiembre/ambos/2000 → 002/003, 4500 MXN y 66.67%; B octubre/ambos/2000 →
003, 2600 MXN y 33.33%. Explica la unidad y el denominador antes de mirar barras.
Las figuras de cada panel tienen escala propia: compara importes/etiquetas.

Edita A sin aplicar: conserva la consulta anterior identificada. Oculta su
tabla, descarga selección/contexto, prueba rechazo 1.5, cero, vacío y noviembre.
Completa ambas descargas antes de aplicar otra consulta; son solicitudes
independientes. B conserva su estado. Recarga o abre una sesión nueva: se
pierden las consultas, sin persistencia ni autenticación implementadas.

La app relee y valida la fuente al aplicar cada panel; no vigila el archivo ni
recalcula instantáneas anteriores al cambiarlo. Fuente inválida/ausente retira
las cifras al aplicar, mientras una entrada rechazada conserva una consulta
anterior válida. Estas políticas ya se prueban en 13.09.

## Práctica

Continúa con el [lab 13.10](../../../labs/13_shiny_web/10_local_delivery/README.md):
preparar, verificar, reconstruir y explicar con otra persona que revise la entrega.

## Evidencia y criterio de salida

Conserva entrega y reconstrucción, resultados comparados y una nota personal
fuera de ellas: entorno real, pruebas, casos demostrados, descargas releídas,
ayudas, dudas y siguiente paso. Explica las diferencias entre cero, vacío,
ausencia de universo, rechazo y bloqueo; entre archivo generado y sesión observada.

El cierre requiere ejecución desde otra carpeta, pruebas completas y revisión
humana de la app/resultados. Material disponible, OK técnico y aprendizaje
son estados distintos; no se marca automáticamente un proyecto/checkpoint.

## Siguiente paso

Revisa el [cierre de Shiny](../../../docs/shiny-closure.md). Cuando completes
la práctica, consulta [14.01 — Pregunta y contrato del producto](../../14_reproducible_projects/01_product_question_contract/README.md),
disponible con lección y lab; 14.02–14.05 también tienen lecciones/labs y 14.06–14.09 siguen planificadas. Streamlit es una alternativa; no es obligatorio construir
ambas apps antes de avanzar. Las diez secciones de Shiny tienen material.

## Referencias primarias

Ejemplos propios, contrastados con las versiones declaradas:

- [Posit: runApp](https://shiny.posit.co/r/reference/shiny/latest/runapp.html): carpeta/app, proceso activo y escucha local.
- [renv: restore](https://rstudio.github.io/renv/reference/restore.html): reconstrucción de la biblioteca desde lockfile.
- [renv: colaboración](https://pkgs.rstudio.com/renv/articles/collaborating.html): fuentes, lockfile y activadores compartidos.
- [R: md5sum](https://stat.ethz.ch/R-manual/R-devel/library/tools/html/md5sum.html): huellas de archivos.
- [Posit: testServer](https://shiny.posit.co/r/reference/shiny/latest/testserver.html): alcance de las pruebas de servidor.

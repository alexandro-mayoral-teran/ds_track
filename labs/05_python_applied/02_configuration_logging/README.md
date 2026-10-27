# Lab 05.02 — Configuración y registro de ejecución

## Propósito, entradas y preparación

Lee la [lección 05.02](../../../curriculum/05_python_applied/02_configuration_logging/README.md)
y completa 05.01 con su lab. Ejecutarás el mismo análisis con parámetros externos
y explicarás el contexto que produjo cada entrega.

**Entradas:** consumidor ejecutar_configurado.py, paquete de 05.01,
septiembre.json/octubre.json y CSV sintéticos de SQL 03.01.
**Resultado:** dos cortes conciliados, una ejecución con opciones explícitas,
registros y explicación de rutas/niveles/errores. No hay proyecto/checkpoint
implementado asociado todavía. Dos o tres sesiones de 45–75 minutos bastan
para dividir A/B, C/D y E; no necesitas otro notebook.

Trabaja desde la raíz, con el entorno elegido activado. Sigue el recorrido
completo de tu shell en la lección. Usa carpetas nuevas dentro de
curriculum/05_python_applied/02_configuration_logging/output; conserva
fuentes, configuraciones curadas y entregas previas. Crea variantes del JSON
solo en tu carpeta de práctica y ajusta sus rutas al moverlas.

## A. Interpretar argumentos antes de exportar

1. Ejecuta argumentos_demo.py con --help y con --cut 2026-09-30 --dpi 120.
2. Prueba --dpi alto. Explica dónde se detiene y qué significa type=int.
3. Prueba --dpi 0 en la demostración y en el consumidor completo con un
   --output nuevo. Explica por qué no es suficiente convertir a entero.
4. Consulta --help de ejecutar_configurado.py y describe cada opción.
5. Explica cómo --log-level llega al atributo log_level y por qué --output
   se exige aquí o dentro del JSON, en vez de marcarlo required=True sin más.

**Comprobación:** --help no exporta; --dpi alto falla al interpretar;
el consumidor completo rechaza 0 antes de crear salida. **Evidencia:**
explicación de conversión/validación y opciones que cambian resultados o presentación.

<details>
<summary>Ver solución razonada de A</summary>

La demostración convierte dpi a int y muestra 120 como entero. No tiene la
regla de resolución positiva del consumidor completo; por eso 0 puede
convertirse sin servir para exportar. Un texto como alto falla en argparse.
--log-level usa un nombre con guion en terminal y guion bajo en Namespace.

source/output eligen archivos; cut selecciona datos; dpi cambia la cuadrícula
PNG; log_level filtra mensajes. La salida puede venir del archivo JSON: exigir
siempre --output en argparse impediría ese recorrido. Se comprueba después de
combinar fuentes de configuración. --help termina antes de esa validación.

</details>

## B. Ejecutar septiembre y octubre

1. Ejecuta los dos JSON desde la raíz siguiendo la lección. Si el destino
   existe, pasa --output con otro nombre; no borres la entrega anterior.
2. Lee el código de salida inmediatamente después de cada comando.
3. Coteja indicadores.csv, referencia_csv.csv y conciliacion.csv.
4. Abre las figuras con sus tablas. Redacta un hallazgo y un límite por corte.
5. Explica por qué ambos tienen cobertura global 87,5 % pero distribuciones
   de ausencias diferentes. Evita atribuir causas a esta comparación.

**Resultado:** dos entregas y una tabla comparativa.
**Comprobación:** 24 registros, 21 conocidos, mediana global 2300 y veinte
conciliaciones por corte. Educación tiene mediana 3250 con 2/3 en septiembre;
en octubre conserva 3 registros sin mediana y cobertura 0 %.

<details>
<summary>Ver solución razonada de B</summary>

Medianas de septiembre: comercio 2900 (5/5), consumo 1500 (8/10),
educación 3250 (2/3), servicios 2350 (6/6). Octubre: 3100 (5/5),
1750 (10/10), ausente (0/3) y 2550 (6/6), respectivamente.
La referencia calcula esos valores desde CSV/statistics antes de entregar.

Las tres ausencias de cada corte se distribuyen de distinta manera. La
igualdad de mediana/cobertura global no prueba que el detalle sea idéntico.
WARNING sobre cobertura parcial informa un límite; no impide código 0 ni
implica que las ausencias se reemplazaron por ceros. Revisa las figuras:
las conciliaciones no acreditan automáticamente legibilidad o interpretación.

</details>

## C. Demostrar precedencia y bases de rutas

1. Usa octubre.json con --cut 2026-09-30, --dpi 120, --log-level WARNING
   y --output nuevo, como en los recorridos de la lección.
2. Antes de ejecutar, predice los valores efectivos y su procedencia por campo.
3. Lee ejecucion.json y contrasta tu predicción. Compara indicadores.csv
   con septiembre: cambiar dpi/nivel no debe alterar valores ni ausencias.
4. Comprueba el PNG de 1440 × 660 píxeles y las unidades de las figuras.
5. Ejecuta desde otra carpeta con rutas absolutas al consumidor y al JSON,
   y --output con otra ubicación nueva. Explica qué base usa cada ruta.
6. Reconstruye desde fuentes/ de una entrega, con misma fecha/dpi y otro destino.

**Evidencia:** valores predichos/registrados, comparación y reconstrucción.

<details>
<summary>Ver solución razonada de C</summary>

source viene del archivo y se resuelve respecto de su carpeta. cut, dpi,
log_level y output vienen de la terminal; output relativo parte del directorio
de trabajo. Debe ejecutarse septiembre, aunque el archivo se llame octubre.

La comparación de indicadores conserva septiembre. El número de píxeles
cambia por dpi, mientras los datos y el SVG conservan su medida. Con rutas
absolutas al consumidor/configuración, cambiar la carpeta de trabajo no cambia
source del JSON. Una opción de ruta relativa en terminal sí depende de esa
carpeta. Al copiar el JSON debes revisar la base de sus rutas internas.

Para reconstruir, usa las copias de creditos.csv/cortes.csv conservadas dentro
de fuentes/. No se reconstruye desde una captura ni desde los mensajes.

</details>

## D. Separar mensajes y registro persistente

1. Ejecuta el mismo corte en destinos nuevos con INFO y WARNING. Compara
   lo visible, los códigos de salida y las tablas.
2. Usa DEBUG en una tercera carpeta. Localiza la procedencia de parámetros.
3. Revisa ejecucion.json en todas: configura valores, reglas y versiones
   aunque algunos mensajes estén ocultos. Reconoce qué campos sí varían.
4. Explica por qué stderr no significa necesariamente error y por qué un
   mensaje final no reemplaza abrir las figuras o verificar conteos.

**Comprobación:** INFO muestra etapas; WARNING conserva la advertencia de
cobertura y oculta INFO. Ambos terminan con 0 y los mismos indicadores.
El registro persiste con independencia del umbral.

<details>
<summary>Ver solución razonada de D</summary>

Logging emite diagnóstico por stderr y clasifica niveles. WARNING es un
umbral: no vuelve incorrecto el dato ni detiene el cálculo. DEBUG añade
procedencia; no requiere alterar las transformaciones.

ejecucion.json registra los niveles elegidos y destinos distintos, además de
valores efectivos/versión. Las rutas son de tu ejecución local: no publiques
el registro sin revisar ese contexto. El JSON y el mensaje final acreditan
que se alcanzaron ciertas etapas, no aprendizaje ni revisión visual completa.

</details>

## E. Comprobar errores sin confundir salidas anteriores

1. Prueba --cut 2026-02-30, --dpi 0, --log-level VERBOSE y una fuente
   inexistente, siempre con destinos nuevos de prueba.
2. Ejecuta sin --output ni JSON que lo declare. Describe la condición faltante.
3. Repite una entrega con el mismo destino; comprueba que conserva sus archivos.
4. En una copia del JSON incluye una clave mal escrita como dpI. Revisa
   el mensaje y confirma que no se crea una entrega.
5. Usa el corte válido sin registros 2026-11-30 en un destino nuevo.
   Distingue esa advertencia de la fecha imposible del primer paso.

**Comprobación:** configuración inválida termina con 2 antes de exportar;
el corte vacío permite 0 con bases no definidas. Conserva fuentes y salidas.
El manejo de fallas durante la escritura se profundizará en 05.03.

<details>
<summary>Ver solución razonada de E</summary>

argparse comprueba conversión/opciones permitidas; load_settings comprueba
valores efectivos, fuentes y destino. No reconoce dpI como dpi ni corrige
silenciosamente una clave. Ningún error de configuración debe crear esa salida.

2026-02-30 no es una fecha posible. 2026-11-30 es válida, pero no tiene
registros en estas fuentes: cada segmento conserva 0 registros/conocidos,
mediana y cobertura no definidas. Es un resultado vacío, no saldo cero.

Un destino existente se rechaza antes de escribirlo. Una falla durante una
exportación puede dejar archivos parciales: entrega.json y ejecucion.json
representan etapas distintas. Aun con un registro final, revisa los archivos.

</details>

## Reflexión, evidencia y continuidad

- ¿Qué valor se utilizó finalmente y de dónde vino cada campo?
- ¿Qué ruta depende de la terminal y cuál del archivo JSON?
- ¿Qué queda oculto con WARNING y qué sigue guardándose?
- ¿Por qué una cobertura global igual no prueba análisis idénticos?
- ¿Qué falta comprobar después de un código 0?

Registra tus tablas comparadas, explicación, revisión visual y dudas en
tu bitácora personal junto a la práctica. Puedes avanzar cuando cambies corte/destino sin editar el cálculo,
justifiques la precedencia y distingas advertencias, configuración inválida y
una entrega incompleta.

Continúa con [05.03 — Errores y gestión de recursos](../../../curriculum/05_python_applied/03_errors_resources/README.md).
Volver a la [lección 05.02](../../../curriculum/05_python_applied/02_configuration_logging/README.md).

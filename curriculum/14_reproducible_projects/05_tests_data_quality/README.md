# 14.05 — Pruebas y calidad de datos

[Inicio](../../../README.md) / [Módulo 14](../README.md) / **Lección 14.05**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Detectar fallas relevantes antes de entregar una consulta |
| **Necesitas** | Contrato de 14.01, configuración/entorno y pipeline de 14.02–14.04 |
| **Evidencia** | Suite aprobada, falla controlada detectada y explicación del control |

[**Hacer el lab 14.05 →**](../../../labs/14_reproducible_projects/05_tests_data_quality/README.md) · [Recorridos completos](recorridos.md)

## Propósito

Una consulta puede terminar sin error y producir una respuesta equivocada.
También puede detenerse correctamente porque la fuente incumple el contrato.
Esta sección permite distinguir ambas situaciones mediante ejemplos pequeños,
resultados esperados conocidos y comprobaciones automáticas.

Una **suite** es un conjunto de pruebas que ejecutamos juntas.
No basta con comprobar que un archivo existe ni con comparar una suma. Vamos a
comprobar filas, claves, estados, denominadores y la relación entre cálculo y entrega.

## Antes de empezar

Revisa [14.01 — Contrato](../01_product_question_contract/README.md),
[14.02 — Configuración](../02_structure_configuration/README.md),
[14.03 — Entornos](../03_reconstructible_environments/README.md) y
[14.04 — Pipeline](../04_pipeline_reprocessing/README.md).
Los preparadores incluyen 31 fuentes; no necesitas entregas anteriores.
Elige R/renv o Python/uv. Conservamos modelos, datos, pipeline y lockfiles;
no instalamos paquetes nuevos. En Python se reutiliza
[unittest de 05.04](../../05_python_applied/04_testing/README.md).

## Qué vas a aprender

- Traducir una regla del contrato a entrada, resultado esperado y comprobación.
- Separar pruebas de una función, pruebas de integración y controles de datos actuales.
- Probar fronteras, ausencias, duplicados y estados vacíos con una razón explícita.
- Introducir un defecto controlado, observar la falla y recuperar una suite aprobada.
- Explicar qué cubren las pruebas y qué necesita revisión humana o casos adicionales.

## Material de apoyo

| Recurso | Para qué sirve | Uso |
| --- | --- | --- |
| [Recorridos](recorridos.md) | Preparar/restaurar y ejecutar sin mezclar shells | Elegir una ruta |
| [Preparador R](preparar.R) / [Python](preparar.py) | Crear una copia nueva de 31 fuentes | Según ruta |
| [Pruebas R](plantilla/pruebas.R) / [Python](plantilla/pruebas.py) | Inspeccionar los siete grupos y ejecutar la suite | Esencial |
| [Casos de calidad](plantilla/referencia/calidad.csv) | Catorce alteraciones de fuente que deben rechazarse | Inspeccionar |
| [Criterios literales](../01_product_question_contract/criterios.csv) | Nueve preguntas y resultados esperados del contrato | Referencia independiente del cálculo |
| [LEEME](plantilla/LEEME.md) | Entorno y archivos que deja cada ensayo | Leer antes de ejecutar |

## 1. Un ejemplo pequeño antes de la suite

La fuente es sintética, el saldo está en pesos mexicanos enteros y la clave es
id_credito + fecha_corte. El ID conserva ceros. En este ejemplo hay un solo corte:

| id_credito | segmento | fecha_corte | saldo_mxn |
| --- | --- | --- | ---: |
| 001 | comercio | 2026-09-30 | 0 |
| 002 | servicios | 2026-09-30 | 2000 |
| 003 | comercio | 2026-09-30 | 2500 |

Con ambos segmentos y mínimo 2000, la regla **saldo ≥ mínimo** selecciona
002 y 003. Saldo seleccionado: 2000 + 2500 = 4500. Universo: tres créditos,
saldo 4500; porcentaje: 100 × 2 / 3. El saldo cero de 001 es válido, aunque
no supera ese filtro. Con mínimo cero y comercio, sí aparece junto a 003.

Una prueba tiene tres partes:

1. **Preparar:** una entrada conocida, sin depender del resultado de otra prueba.
2. **Actuar:** llamar la función o ejecutar los pasos que queremos comprobar.
3. **Comparar:** contrastar el resultado con una expectativa declarada de antemano.

Si calculas el valor esperado llamando a la misma función, un defecto compartido
puede hacer que la prueba pase. Aquí las cifras e IDs esperados están escritos
en el contrato y pueden comprobarse a mano.

### Python: una prueba de frontera

En la copia preparada, crea un archivo nuevo minimo.py con este ejemplo completo.
Ejecútalo con el Python local según los recorridos:

```python
import sys
import unittest
sys.path.insert(0, "codigo")
from modelo import resolver

class Frontera(unittest.TestCase):
    def test_incluye_el_minimo(self):
        filas = [
            dict(id_credito="001", segmento="comercio", fecha_corte="2026-09-30", saldo_mxn="0"),
            dict(id_credito="002", segmento="servicios", fecha_corte="2026-09-30", saldo_mxn="2000"),
            dict(id_credito="003", segmento="comercio", fecha_corte="2026-09-30", saldo_mxn="2500"),
        ]
        resultado = resolver(filas, "2026-09-30", "comercio|servicios", "2000")
        self.assertEqual(resultado["ids"], "002|003")
        self.assertEqual(resultado["saldo_seleccion_mxn"], "4500")

if __name__ == "__main__":
    unittest.main()
```

TestCase agrupa pruebas; los métodos test_* se descubren al ejecutar unittest.
assertEqual informa una falla si los valores difieren. unittest.main ejecuta y
resume; un fallo hace que el proceso termine con código distinto de cero.
Esta prueba usa datos válidos definidos en memoria: no acredita la lectura del CSV.

### R: comprobar el mismo caso

Desde la raíz de la copia, en consola R:

```r
source("codigo/modelo.R")
mini <- data.frame(
  id_credito = c("001", "002", "003"),
  segmento = c("comercio", "servicios", "comercio"),
  fecha_corte = rep("2026-09-30", 3),
  saldo_mxn = c(0, 2000, 2500)
)
resultado <- resolver_contrato(mini, "2026-09-30", "comercio|servicios", "2000")
stopifnot(resultado[["ids"]] == "002|003",
          resultado[["saldo_seleccion_mxn"]] == "4500")
```

stopifnot detiene la ejecución si una condición no es verdadera. R base basta
para esta práctica; no se exige instalar testthat. En pruebas.R se capturan las
fallas por grupo para mostrar el conjunto y detenerse al final si alguna falló.

## 2. Tres comprobaciones con responsabilidades distintas

| Tipo | Pregunta | Ejemplo de esta sección |
| --- | --- | --- |
| Unitaria | ¿La función cumple una regla con una entrada pequeña? | Incluye saldo igual al mínimo; conserva cero y estados |
| Integración | ¿Las piezas se conectan correctamente? | Configuración → CSV válido → selección/contexto → archivos releídos |
| Control de datos actuales | ¿Esta fuente concreta cumple el contrato al ejecutar? | Clave única y calendario válido en todos los registros antes del filtro |

Una suite aprobada con fixtures —muestras preparadas para probar— no demuestra
que otro CSV recibido mañana sea válido. Por eso el pipeline valida **cada fuente
completa** cuando se ejecuta. Las pruebas comprueban que esos controles rechazan
ejemplos inválidos y aceptan ejemplos conocidos.

Tampoco reemplazan la revisión de la pregunta: una fórmula puede estar bien
programada y responder a un objetivo distinto del que necesita la persona.

## 3. Calidad de datos como reglas verificables

En esta muestra no se aceptan campos ausentes. No rellenamos saldos con cero ni
eliminamos duplicados para conseguir que una prueba pase.

| Dimensión | Regla del contrato | Caso que debe hacer fallar la validación |
| --- | --- | --- |
| Esquema | Cuatro columnas exactas | Falta segmento o aparece una columna extra |
| Identidad | ID textual de tres cifras | 1 o ID vacío |
| Unicidad | Una fila por ID/corte | Duplicar una fila completa |
| Categorías | comercio o servicios | salud |
| Calendario | ISO real, años 1900–2100 | 2026-02-30, fecha local o 1899 |
| Presencia | Los cuatro campos necesarios tienen valor | Saldo vacío |
| Unidad/rango | Pesos enteros 0..1000000 | -1, 1.5, 1000001 o texto NA |
| Coherencia | Filas e indicadores corresponden a la misma selección | IDs correctos con saldos cambiados |

Esas dimensiones no miden por sí solas si el dato refleja el mundo real. Un saldo
ficticio de 1900 puede cumplir todos los formatos y seguir siendo falso en una
fuente real. Procedencia, conciliación externa, frescura y significado requieren
controles adecuados a cada producto. Aquí conocemos el origen sintético y las reglas.

**Error habitual:** filtrar octubre primero y validar después. Un duplicado de
septiembre desaparecería del control. La integración introduce ese duplicado
fuera del corte consultado y exige que no se publique ningún destino final.

## 4. Qué comprueban los siete grupos

Abre [pruebas.py](plantilla/pruebas.py) o [pruebas.R](plantilla/pruebas.R) junto con
[calidad.csv](plantilla/referencia/calidad.csv). No necesitas memorizar el ejecutor:
localiza la entrada preparada, la llamada y la comparación de un caso.

| Grupo | Comprobación |
| --- | --- |
| 01 | Nueve criterios literales: IDs, saldos por registro, estados, conteos, sumas y porcentajes |
| 02 | Catorce fuentes inválidas: una alteración por fixture, rechazo esperado |
| 03 | Invertir el orden de entrada conserva IDs ordenados; cero sigue siendo un valor válido |
| 04 | Octubre y septiembre se exportan por separado; valores por ID/contexto y repetición sin cambios |
| 05 | Selección vacía conserva encabezados/universo; corte sin universo no publica |
| 06 | Duplicado fuera del corte bloquea la entrega |
| 07 | Alteración compensada y huellas actualizadas no engañan la comprobación por valor |

Python ejecuta siete métodos, algunos con subTest para distinguir casos dentro
del grupo; la cifra de métodos no equivale al número de entradas contrastadas.
R ejecuta siete grupos y acumula sus fallas; dentro de cada grupo se detiene en
la primera condición que falla. No se afirma cobertura total de ramas o líneas.

Los enteros y los IDs se comparan exactamente. Para porcentajes calculados en
punto flotante usamos tolerancia absoluta 1e-10 puntos porcentuales; por ejemplo,
66.666… no tiene representación decimal finita. No trasladar esa tolerancia a
claves o saldos enteros, donde podría ocultar errores.

## 5. Un rechazo esperado debe comprobarse

En Python, assertRaises exige que la llamada produzca el tipo de excepción
esperado; assertRaisesRegex añade una señal del motivo. Si la llamada acepta el
dato inválido, falla la prueba. En R, esperar_error captura el error y verifica
que ocurrió; cuando se indica un patrón, también compara el motivo.
No convertir cualquier resultado en «PASA» usando un catch vacío.

Los casos de fuente se rechazan con ValueError en Python y errores de contrato
en R. Las pruebas positivas impiden que un validador que rechaza todo parezca
correcto. Los errores esperados pertenecen a **fixtures de ensayo**, no se
presentan como entregas válidas.

## 6. Demostrar que las pruebas detectan un defecto

En **otra copia de práctica**, conserva el modelo original como respaldo y cambia
solo el comparador del filtro de saldo: ≥ pasa a >. Con mínimo 2000, desaparece
002 de septiembre aunque su saldo cumple la regla original. La prueba de frontera
y los criterios deben fallar. Revisa el valor obtenido frente al esperado;
restaura el código desde el respaldo y exige una suite nuevamente aprobada.

Esto es un ensayo manual de modificación de código, no una herramienta de
mutation testing ni una medición de cobertura. Un defecto detectado demuestra
sensibilidad a ese defecto; no a todos los posibles. El
[lab](../../../labs/14_reproducible_projects/05_tests_data_quality/README.md) guía la evidencia.

## 7. Qué queda después de ejecutar

Cada tanda crea fixtures nuevas bajo ensayos/pruebas-*, config/pruebas-* y
datos/entrada/pruebas-*. Sus entregas van a salidas/pruebas-*. No borra archivos
ni modifica datos/configuración iniciales; la alteración deliberada afecta solo
su entrega de ensayo y se conserva para revisarla. Repetir crea otra tanda.
Los ensayos no se deben mezclar con una entrega al público.

El entorno se comprueba antes de la suite y durante el pipeline. Las pruebas de
integración usan su propia configuración: para entregar tu consulta debes además
ejecutar el pipeline con **tu configuración real** y revisar sus resultados.
No hay CI, reporte/app integrados ni garantía frente a escrituras simultáneas.

## Práctica, evidencia y criterio de salida

Sigue los [recorridos](recorridos.md) y realiza el
[lab 14.05](../../../labs/14_reproducible_projects/05_tests_data_quality/README.md).
Conserva comando, versiones, resumen aprobado, falla controlada y nueva aprobación.
Explica qué regla protegió cada prueba elegida y qué datos podrían seguir mal
sin que esa prueba lo detecte. Material disponible no acredita tu práctica.
No hay proyecto asociado ni checkpoint implementado.

Siguiente: [14.06 — Trazabilidad y recuperación de fallas](../06_traceability_recovery/README.md),
disponible con su lab.

## Referencias primarias

- [Python 3.12: unittest](https://docs.python.org/3.12/library/unittest.html): casos, fixtures, subTest y aserciones.
- [R: stopifnot](https://stat.ethz.ch/R-manual/R-devel/library/base/html/stopifnot.html): detener ante condiciones incumplidas.
- [R: condiciones y tryCatch](https://stat.ethz.ch/R-manual/R-devel/library/base/html/conditions.html): capturar errores y distinguirlos de una ejecución correcta.

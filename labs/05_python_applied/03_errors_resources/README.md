# Lab 05.03 — Errores y gestión de recursos

## Propósito, entradas y preparación

Lee la [lección 05.03](../../../curriculum/05_python_applied/03_errors_resources/README.md)
y completa 05.02 con sus prerrequisitos. Vas a provocar fallas controladas,
conservar evidencia y explicar qué se completó antes de detenerse.

**Entradas:** ejecutar_seguro.py, paquete de 05.01, fuentes sintéticas de SQL
y recursos_demo.py. **Resultado:** entrega normal, carpetas parciales,
reconstrucción y comprobaciones de recursos/JSON. No hay proyecto/checkpoint
implementado asociado; no necesitas otra instalación, notebook ni base persistente.

Divide la práctica en dos o tres sesiones de 45–75 minutos. Sigue el recorrido
completo de tu shell desde la raíz, con el entorno elegido. Los destinos de
03_errors_resources/output deben ser nuevos. Conserva fuentes y entregas anteriores;
las simulaciones no requieren cambiar permisos, borrar datos ni llenar el disco.

## A. Identificar y comunicar una excepción

1. Prueba int("pendiente") en Python y describe tipo, mensaje y operación fallida.
2. Ejecuta el ejemplo convertir_saldo de la lección. Explica qué añade
   raise ... from exc y cómo conserva la causa.
3. Distingue saldo ausente, corte vacío, clave sin correspondencia y variable
   mal escrita. Decide qué situación admite un resultado y cuál debe detenerse.
4. Localiza el except de cli_segura y el finally de export. Explica por qué
   el mensaje final no pertenece a finally.

**Evidencia:** clasificación y explicación del recorrido. No devuelvas cero
ni una lista vacía para ocultar la falla de conversión.

<details>
<summary>Ver solución razonada de A</summary>

int no puede convertir ese texto: ValueError. La función de ejemplo añade
el contexto del saldo y conserva la excepción original como causa. Un raise
sin argumento dentro del except propagaría la misma excepción.

Un saldo ausente se conserva y afecta cobertura; un corte vacío permite
mediana/cobertura no definidas. Una relación inválida impide calcular la
pregunta sobre una base fiable. NameError por una variable mal escrita exige
corregir el código, no devolver una tabla vacía.

finally limpia recursos al terminar o fallar. Un éxito allí sería falso en
el segundo caso. La entrada responde OSError/ValueError previstos con código
1 y diagnóstico; deja propagar otras excepciones para corregirlas.

</details>

## B. Comprobar recursos después de una falla

1. Ejecuta recursos_demo.py con --output nuevo según la lección.
2. Describe dónde se abre/cierra el archivo y qué falla dentro del bloque.
3. Explica qué hace cada with de la conexión SQLite en memoria.
4. Comprueba los mensajes de archivo cerrado, conexión cerrada y temporal retirado.
5. Localiza el try/finally de Matplotlib en export. Indica qué Figure cierra
   y por qué no debe cerrar figuras ajenas.

**Comprobación:** archivo cerrado después de ValueError, consulta rechazada
por conexión cerrada y temporal propio retirado. **Evidencia:** salida y mapa
de adquisición/liberación, diferenciando transacción de cierre.

<details>
<summary>Ver solución razonada de B</summary>

El gestor del archivo llama a su cierre al salir del bloque. El ValueError
proviene de la conversión, no de una supuesta falta de saldo en el análisis.
La conexión usa with connection para la transacción y closing para cerrar;
el primer gestor por sí solo no cierra la conexión.

La demostración comprueba cierre mediante ProgrammingError al intentar otra
consulta. Temporal y SQLite se crean para el ejercicio; las fuentes y bases
del curso no se reinician. Matplotlib cierra la Figure concreta creada por
export, incluso si falla el guardado protegido por ese bloque.

</details>

## C. Conservar un JSON anterior

1. En una sesión iniciada en 01_notebook_to_modules, ejecuta la demostración
   write_json_atomic de la lección dentro de output/json_demo nuevo.
2. Después de simulate_failure=True, vuelve a leer estado.json.
3. Comprueba que el temporal propio se retiró y que la versión anterior sigue siendo 1.
4. Ejecuta sin simulación y comprueba versión 2.
5. Explica por qué se serializa antes de abrir, se cierra antes de replace
   y se usa un temporal en la misma carpeta.

**Resultado:** archivo propio antes/después y explicación de sus límites.
**Comprobación:** la falla no trunca versión 1; el reemplazo normal publica 2.

<details>
<summary>Ver solución razonada de C</summary>

La falla controlada sucede después de escribir/cerrar el temporal, pero antes
de reemplazar el destino. El original sigue intacto y finally retira ese
temporal si el sistema lo permite. En el camino normal os.replace cambia
el destino al JSON completo de versión 2.

Cerrar antes evita mantener el temporal abierto al reemplazar en Windows.
Serializar antes evita abrir archivos si el objeto no puede representarse.
La misma carpeta evita un movimiento entre sistemas de archivos. No se
garantiza una transacción sobre varios archivos, persistencia total ante
pérdida de energía ni limpieza después de matar abruptamente el proceso.

</details>

## D. Distinguir etapas de entrega y reintentar

1. Ejecuta la entrega normal y las simulaciones record/before-close de la
   lección. Lee el código de salida inmediatamente después de cada comando.
2. Compara presencia de entrega.json, ejecucion.json y cierre.json.
3. Desde una sesión en 01_notebook_to_modules, inspecciona tus rutas reales:

```python
from analisis_cartera.cierre import inspect_delivery

print(inspect_delivery("../03_errors_resources/output/normal"))
print(inspect_delivery("../03_errors_resources/output/falla_registro"))
print(inspect_delivery("../03_errors_resources/output/falla_cierre"))
```

4. Explica por qué entrega.json puede estar presente en las tres carpetas
   sin acreditar cierre de 05.03. Conserva las parciales; no agregues marcadores.
5. Reconstruye desde normal/fuentes hacia otra carpeta nueva sin simulación.
   Compara los indicadores y las veinte conciliaciones.
6. Abre las figuras de normal/reconstrucción y coteja unidades, bases y ausencias.

**Comprobación:** normal/reconstrucción terminan con 0 y cierre válido;
simulaciones con 1 y estado incompleta. Las fuentes y carpetas previas se conservan.
**Evidencia:** tabla de etapas, causa identificada y resultados reconstruidos.

<details>
<summary>Ver solución razonada de D</summary>

| Caso | entrega.json | ejecucion.json | cierre.json | Código |
| --- | --- | --- | --- | ---: |
| Normal | Sí | Sí | Sí | 0 |
| record | Sí | No | No | 1 |
| before-close | Sí | Sí | No | 1 |

El export heredado escribe entrega.json al terminar su parte; el consumidor
nuevo registra y cierra después. Fallar en esas etapas conserva la parte
exportada. No hay mensaje final de cierre ante esas fallas. DEBUG permite
examinar la causa y su recorrido.

La reconstrucción conserva 24 registros, 21 conocidos, mediana global 2300,
cobertura 87,5 % y veinte coincidencias. Educación sigue sin mediana con
cobertura 0 %. Revisar figuras y explicación continúa siendo necesario aun
cuando inspect_delivery diga completada: solo comprueba etapa y presencia.

</details>

## Extensión opcional

Ejecuta after-export en otro destino nuevo. Predice los archivos presentes
antes de abrir la carpeta. Describe cómo diseñarías una excepción de dominio
para distinguir falla de contrato de otros errores, sin exigir implementarla.
Excepciones propias/gestores personalizados no bloquean este cierre.

## Reflexión, evidencia y continuidad

- ¿Qué excepción se atendió y qué información de la causa se conservó?
- ¿Qué recurso cierra with y cuál requiere otro responsable?
- ¿Qué archivo anterior se protegió y cuándo se permite reemplazarlo?
- ¿Por qué guardar cierre.json no convierte una carpeta en transacción?
- ¿Qué harías con una carpeta parcial antes de volver a intentar?

Registra resultados, revisión visual, dudas y siguiente paso en tu bitácora personal junto a la práctica.
Puedes avanzar cuando demuestres conservación y cierre de recursos, interpretes
las etapas y no confundas una falla con un resultado válido vacío.

Continúa con [05.04 — Pruebas de código y datos](../../../curriculum/05_python_applied/04_testing/README.md). Volver a la [lección 05.03](../../../curriculum/05_python_applied/03_errors_resources/README.md).

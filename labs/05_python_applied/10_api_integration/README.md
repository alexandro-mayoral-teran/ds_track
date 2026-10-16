# Lab 05.10 — Incorporar páginas de una API con controles

## Propósito, entradas y resultado

Esta práctica de **extensión** acompaña
[05.10 — Integración con APIs](../../../curriculum/05_python_applied/10_api_integration/README.md).
Usa su recorrido completo de PowerShell, Bash/Zsh o CMD en el entorno ya elegido.
No necesitas conexión, credenciales, servidor ni instalaciones nuevas.

Recibes [configuración y muestras](../../../curriculum/05_python_applied/10_api_integration/muestras/README.md),
[api.py](../../../curriculum/05_python_applied/01_notebook_to_modules/analisis_cartera/api.py),
[ejecutar_api.py](../../../curriculum/05_python_applied/01_notebook_to_modules/ejecutar_api.py)
y [18 pruebas locales](../../../curriculum/05_python_applied/01_notebook_to_modules/pruebas_0510/test_api.py).
Las muestras representan los mismos 48 cortes de los CSV conocidos, en tres páginas.

Entrega evidencia de los dos escenarios exitosos, explicación de las fallas y
una prueba propia. Conserva fuentes y corridas anteriores; usa destinos nuevos.
Una sesión puede cubrir solo parte del lab. No hay proyecto/checkpoint
implementado asociado.

## A. Seguir una solicitud y su contrato

Localiza método, endpoint, consulta y cabeceras en el ejemplo de la lección.
Después abre pagina_01.json y correcto.json: ¿cuál contiene registros y cuál
describe una secuencia de respuestas? Explica qué significa total=48 frente a
16 elementos en items. No consultes el dominio de ejemplo.

Predice qué ocurriría con 200 y HTML, 200 y JSON sin total, 204 y cuerpo vacío,
y 200 con items=[], total=0, next_page=null. Distingue JSON legible de datos válidos.

<details>
<summary>Orientación y comprobación</summary>

GET solicita lectura; page indica la página. Accept solicita JSON y Content-Type
describe la respuesta, pero ninguno valida las reglas del contenido. correcto.json
ordena pasos del simulador; pagina_01.json es el cuerpo de una respuesta.
total cuenta la extracción completa; items solo contiene esta página.

El cliente rechaza HTML, esquema incompleto y 204 porque no cumplen su contrato.
La página vacía con total cero y final explícito sí es válida y produce columnas
tipadas vacías. Eso no equivale a devolver [] ante una falla: el estado de éxito
debe haberse comprobado antes. Un vacío inesperado todavía puede incumplir una
regla posterior del análisis o la comparación con una fuente conocida.

</details>

## B. Completar y conciliar los escenarios exitosos

Ejecuta correcto y recuperable hacia carpetas nuevas con los comandos de la
lección. Registra inmediatamente sus códigos de salida. Revisa detalle_api.csv,
indicadores_api.csv, conciliacion.csv y ejecucion.json. Cuenta filas y solicitudes;
no confundas reintentos con nuevas páginas.

Explica cómo compruebas que el escenario recuperable no duplicó página 1 ni
descartó página 2. Compara los indicadores de ambas ejecuciones y con el resultado
conocido. Justifica por qué no debes concatenar este detalle con el CSV original.

<details>
<summary>Comprobaciones esperadas</summary>

Ambos terminan con código 0 y estado completo. Hay 48 observaciones, cinco filas
de indicadores y 20 controles. correcto solicita 1, 2, 3; recuperable solicita
1, 1, 2, 2, 3, con dos pausas simuladas de 0,25 segundos. El simulador no duerme.

El cliente acumula registros solo después del 200 y su validación. Reintentar la
misma página no añade otro lote por un 503/timeout. Las claves se comprueban
globalmente y el detalle se compara exactamente con la lectura CSV.
Todos conserva 24/21/2300/87,5 para registros/conocidos/mediana/cobertura. Educación
conserva ausencia de mediana. API y CSV representan las mismas observaciones;
concatenarlos duplicaría datos. La finalidad es comprobar una entrada alternativa.

</details>

## C. Fallar sin anunciar éxito parcial

Ejecuta error_tardio y json_invalido hacia destinos nuevos. Espera código 1 y
ausencia de carpetas de resultados. Explica por qué tener una primera página
válida no basta para producir indicadores de toda la extracción.

Revisa las pruebas de agotamiento, Retry-After, claves repetidas y total cambiante.
Explica qué casos se reintentan, cuántas veces y por qué el reintento de la misma
solicitud no corrige una incompatibilidad de esquema. El registro muestra página,
intento y estado; no debería mostrar cuerpos ni credenciales.

<details>
<summary>Interpretación razonada</summary>

error_tardio recibe 401 en página 2. La lógica no devuelve la tabla de página 1
ni crea resultados parciales de éxito. json_invalido tiene 200, pero el texto no
se puede interpretar como JSON. Ninguna falla se transforma en una extracción vacía.

La política repite solo timeout y 503 sin Retry-After, con dos intentos por página
en la configuración incluida. Tras el último no duerme ni solicita otra vez.
401/429 y 503 con Retry-After se detienen para revisar acceso/límites/espera.
Un error de esquema o clave implica revisar datos/contrato, no repetir por costumbre.
La extracción puede fallar después de varios intentos correctos: los mensajes
anteriores no acreditan cierre.

</details>

## D. Probar un límite sin cambiar las fuentes

Copia config.json a una carpeta personal de output y cambia max_pages a 1.
Ejecuta correcto con --config seguido de la ruta de esa copia y --output hacia
otro destino nuevo. El resto del comando conserva la estructura de tu recorrido.
No modifiques el archivo original ni aumentes límites para ocultar una falla.

Predice si se solicitará página 2. Después explica la diferencia entre límite
de páginas, cantidad de intentos, máximo de filas y timeout. Si quisieras una
fecha límite total de descarga, ¿qué control adicional faltaría?

<details>
<summary>Resultado esperado y límites del mecanismo</summary>

El cliente valida página 1 y detecta que necesita otra. Con max_pages=1 falla
antes de solicitar página 2, sin carpeta de resultados. Un límite de páginas
no incluye por sí solo el número de reintentos: una página puede tener varios.
max_rows controla el total declarado; timeout limita operaciones bloqueantes
del transporte, no la suma de todas las páginas/lecturas/pausas.
Una fecha límite global exigiría seguir el tiempo restante durante el recorrido
y que el transporte pudiera respetarlo. No está implementada en este ejercicio.

</details>

## E. Prueba propia: JSON incompatible no provoca reintentos

Añade un método a PruebasExtraccion en test_api.py. Prepara un sobre con 200 y
Content-Type JSON cuyo body sea "{". Registra llamadas y pausas; exige ApiError,
una única solicitud y ninguna pausa incluso con max_attempts=3.
Usa los ayudantes response y transport que ya contiene ese archivo.

Ejecuta pruebas nuevas y combinadas con los comandos de la lección. Deben terminar
con OK y código 0. Antes del ejercicio hay 18/105 métodos; la solución añade uno.

<details>
<summary>Una solución y por qué distingue el error</summary>

Inserta el método dentro de PruebasExtraccion con la misma indentación:

```python
    def test_json_incompatible_no_reintenta(self):
        calls, waits = [], []
        envelope = response()
        envelope["body"] = "{"
        with self.assertRaises(ApiError):
            fetch_detail(transport([envelope], calls), max_attempts=3, wait=waits.append)
        self.assertEqual(calls, [(1, 5.0)])
        self.assertEqual(waits, [])
```

No hay una segunda respuesta disponible. Una implementación que intentara
repetir sin criterio agotaría la secuencia o alteraría llamadas/pausas. El error
ocurre después de recibir la respuesta, al interpretar el cuerpo; no pertenece
a los errores transitorios de la política. La solución aislada deja 19 métodos
nuevos y 106 combinados; otros ejercicios personales pueden añadir más.

</details>

## Evidencia, reflexión y continuidad

Conserva carpetas exitosas, comandos/códigos de salida de fallas, configuración
personal y prueba propia. Añade una nota breve con contrato, política de reintento,
conteos conciliados y límites de la simulación.

- ¿Qué demuestra un 200 y qué comprobaciones siguen pendientes?
- ¿Por qué null, cero y una extracción fallida deben distinguirse?
- ¿Qué detectan las claves globales que no detecta contar filas por página?
- ¿Por qué un total estable no garantiza una instantánea de un servicio cambiante?
- ¿Qué parte del adaptador HTTPS se comprobó y qué requeriría un proveedor real?

Puedes cerrar esta extensión cuando expliques esas decisiones y compruebes
éxito/falla con tus palabras. Registra evidencia y dudas en PROGRESS.md; el
desarrollo del material no acredita aprendizaje del estudiante.

Continúa con la siguiente lección prevista:
[plan 05.11 — Cierre del proyecto Python](../../../curriculum/05_python_applied/README.md#11-cierre-del-proyecto-python),
todavía pendiente. Las ampliaciones no obligan a usar una API real para cerrar.
Volver a la [lección 05.10](../../../curriculum/05_python_applied/10_api_integration/README.md).

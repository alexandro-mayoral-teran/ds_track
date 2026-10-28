# Lab 12.08 — Detectar y explicar una regresión

[Inicio](../../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.08**

| Tu práctica | Qué debes producir |
| --- | --- |
| **Meta** | Una prueba propia y una regresión detectada, corregida y explicada |
| **Necesitas** | [Lección 12.08](../../../curriculum/12_streamlit/08_app_testing/README.md) y su copia preparada |
| **Evidencia** | Pruebas, fallo/corrección, CSV/JSON reales y nota de revisión |

## Antes de empezar

Sigue los [recorridos](../../../curriculum/12_streamlit/08_app_testing/recorridos.md)
desde la raíz del repositorio. Elige un entorno y un shell; prepara destinos nuevos.
No necesitas entregas anteriores ni instalar paquetes nuevos. Trabaja en tus copias,
sin cambiar las fuentes del curso ni la práctica que quieras conservar.

## Entradas y resultado esperado

Recibes un mínimo con ventas de 100/200 MXN, las funciones y la app de 12.07,
seis registros sintéticos y tres archivos de pruebas. La
[lección](../../../curriculum/12_streamlit/08_app_testing/README.md#4-la-base-común-y-una-transición-de-formulario)
incluye la tabla completa y sus reglas. Cada fila es un crédito/corte; saldos
enteros conocidos, claves únicas y validación completa antes de filtrar.

Tu caso nuevo será **octubre, servicios, mínimo 1900**. Debe mostrar solamente
002/1900, universo 3/4600, cantidad 1 y porcentaje mostrado 33.33%. Con mínimo
1901 la selección queda vacía, conservando el universo. Justifica estos resultados
antes de escribir código.

## Actividades

1. **Predice y ejecuta el mínimo.** Anota las salidas con mínimos 100, 200 y 201.
   Ejecuta `minimo_pruebas.py` y explica por qué tres situaciones están dentro
   de un método de prueba. Ejecuta después `pruebas_modelo.py` y `pruebas_app.py`.
2. **Escribe un caso de función.** Añade a tu copia de `pruebas_modelo.py` un
   método `test_servicios_octubre`. Lee el CSV y comprueba los cuatro campos de
   la fila 002, universo e indicadores con 1900. Repite con 1901. No obtengas
   el esperado volviendo a llamar al análisis.
3. **Conecta la interfaz.** En tu copia de `pruebas_app.py`, añade un método con
   el mismo caso. Usa `nueva()` y `aplicar(...)` y verifica métricas y la fila
   completa. Después aplica 1901 y exige ausencia de tabla y métricas 0/0/0%.
4. **Detecta la regresión.** Prepara otra copia `output/regresion_1208`.
   Comprueba su inicio correcto; cambia solo la métrica de saldo para presentar
   `universo["saldo_mxn"]` como explica la lección. Ejecuta `test_inicio`,
   conserva la diferencia 4600/2600, identifica la causa y restaura el valor.
   Ejecuta de nuevo la prueba y las suites completas. No modifiques expectativas
   para aprobar un comportamiento incorrecto.
5. **Comprueba en navegador.** Inicia la app de tu copia correcta. Descarga el
   par CSV/JSON inicial y el del caso servicios/1900. Antes de aplicar servicios,
   deja un borrador sin enviar: la vista sigue siendo octubre/ambos/2000.
   Relee los pares con el revisor y compara todas las columnas con la fuente.
   Oculta el detalle y confirma que los archivos conservan la misma selección.
   Ensaya rechazo/corrección y vacío/recuperación; repite con ventana estrecha y
   teclado. Detén únicamente tu servidor al terminar.

Puedes pausar después del paso 3. Para retomar conserva la carpeta y ejecuta
las pruebas de esa copia; no prepares otra vez encima de ella.

## Comprobación

| Caso | Resultado exigido |
| --- | --- |
| Suites originales | 1 método mínimo, 7 de modelo y 11 de app aprobados |
| Tus dos métodos nuevos | Un método adicional en cada suite; no cambian las pruebas originales |
| Servicios/1900 | 002, servicios, 2026-10-31, 1900; universo 3/4600 y 33.33% |
| Servicios/1901 | Selección vacía válida, 0/0/0%; conserva universo |
| Regresión de métrica | `FAIL`, sin necesidad de una excepción de la app; al corregir vuelve a `OK` |
| Navegador | Dos pares recuperados y releídos, filtros efectivos y valores por clave correctos |

El método nuevo de función suma a los siete originales; el de interfaz, a los
once. Cuenta métodos, no subcasos ni aserciones. Si algo falla, conserva el
mensaje y revisa datos, acción y esperado antes de editar.

<details>
<summary><strong>Pista: localiza el caso y luego el resultado</strong></summary>

Para la función, importa lo ya disponible y usa
`leer_cartera(Path(__file__).with_name("cartera.csv"))`. En la clase AppTest,
`self.aplicar(app, corte="2026-10-31", segmentos=["servicios"], minimo="1900")`
envía los tres filtros juntos. El porcentaje del modelo es numérico; usa
`assertAlmostEqual` para compararlo con `100 / 3`. La app presenta `"33.33%"`.

</details>

<details>
<summary><strong>Solución razonada: un método para cada nivel</strong></summary>

Añade este método dentro de `PruebasModelo`, antes del bloque final
`if __name__ == "__main__"`:

```python
def test_servicios_octubre(self):
    filas = leer_cartera(Path(__file__).with_name("cartera.csv"))
    resultado = analizar(filas, "2026-10-31", ["servicios"], 1900)
    self.assertEqual(resultado["seleccion"], [
        {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-10-31", "saldo_mxn": 1900},
    ])
    self.assertEqual(resultado["universo"], {"cantidad": 3, "saldo_mxn": 4600})
    self.assertEqual(resultado["indicadores"]["cantidad"], 1)
    self.assertEqual(resultado["indicadores"]["saldo_mxn"], 1900)
    self.assertAlmostEqual(resultado["indicadores"]["porcentaje_creditos"], 100 / 3)
    vacio = analizar(filas, "2026-10-31", ["servicios"], 1901)
    self.assertEqual(vacio["seleccion"], [])
    self.assertEqual(vacio["indicadores"], {"cantidad": 0, "saldo_mxn": 0, "porcentaje_creditos": 0.0})
    self.assertEqual(vacio["universo"], {"cantidad": 3, "saldo_mxn": 4600})
```

Dentro de `PruebasApp`:

```python
def test_servicios_octubre(self):
    app = self.nueva()
    self.aplicar(app, corte="2026-10-31", segmentos=["servicios"], minimo="1900")
    self.comprobar_metricas(app, ["1", "1900", "33.33%"])
    self.assertEqual(app.table[0].value.to_dict(orient="records"), [
        {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-10-31", "saldo_mxn": 1900},
    ])
    self.aplicar(app, corte="2026-10-31", segmentos=["servicios"], minimo="1901")
    self.comprobar_metricas(app, ["0", "0", "0.00%"])
    self.assertEqual(len(app.table), 0)
```

El límite incluye 1900 por la regla `>=`. Subirlo a 1901 elimina al único crédito
de servicios de ese corte; los otros dos registros siguen en el universo. El
primer método verifica ese universo; el segundo verifica la conexión de widgets
y presentación. Ninguno sustituye pulsar una descarga real ni inspeccionar su archivo.

La regresión muestra el saldo de todo el corte, 4600, en el espacio de la
selección, 2600. Restaurar `indicadores["saldo_mxn"]` corrige la presentación;
cambiar el esperado para aceptar 4600 ocultaría el error.

</details>

## Evidencia y reflexión

Conserva los métodos añadidos, el fallo deliberado y su corrección, resultados
de ejecución y dos pares CSV/JSON reales. En tu nota personal identifica
navegador, ancho aproximado, filtros, claves comprobadas, ayudas y pendientes.

- ¿Qué detecta la prueba por fila que no detectaría una suma?
- ¿Por qué `app.exception` vacío no basta para aprobar la app?
- ¿Qué cambia al crear una AppTest nueva y qué puede seguir compartido?
- ¿Qué comprobaste en navegador que las pruebas de Python no cubren?

Tu compañero revisa una expectativa y propone otra frontera. Esta práctica
no activa un proyecto/checkpoint; PROGRESS.md registra autoría del material,
no el aprendizaje ni los resultados personales.

## Siguiente paso

Revisa el [criterio de salida](../../../curriculum/12_streamlit/08_app_testing/README.md#evidencia-y-criterio-de-salida)
y continúa con [12.09 — Cierre y entrega local](../../../curriculum/12_streamlit/README.md#09-cierre-y-entrega-local),
todavía planificado.

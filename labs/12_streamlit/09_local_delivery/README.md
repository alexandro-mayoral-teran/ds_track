# Lab 12.09 — Reconstruir y demostrar una entrega local

[Inicio](../../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.09**

| Tu práctica | Qué debes producir |
| --- | --- |
| **Meta** | Una entrega que otra persona reconstruya y contraste con una referencia |
| **Necesitas** | [Lección 12.09](../../../curriculum/12_streamlit/09_local_delivery/README.md) y entorno de Streamlit |
| **Evidencia** | Entrega, reconstrucción, rechazo explicado y demostración documentada |

## Antes de empezar

Sigue los [recorridos](../../../curriculum/12_streamlit/09_local_delivery/recorridos.md)
desde la raíz del repositorio. Cada destino debe ser nuevo. No necesitas
entregas anteriores; el preparador reúne fuentes y metadatos. Usa un entorno
local y un gestor; no instales en base ni modifiques el lockfile del curso.

Puedes separar preparación/verificación, reconstrucción y demostración en
sesiones distintas. Para retomar conserva las carpetas y repite solo las
comprobaciones o el arranque, sin preparar encima de lo existente.

## Entradas y resultado esperado

Recibes la app de 12.07, pruebas de 12.08, seis filas sintéticas y un constructor/
verificador. La [lección](../../../curriculum/12_streamlit/09_local_delivery/README.md#2-fuente-contrato-y-resultados-que-deben-conservarse)
presenta todos los datos y reglas: clave ID/corte, saldos enteros conocidos,
validación completa antes de filtrar. El cierre usa septiembre y octubre
con registros y noviembre ausente.

Debes producir una entrega y otra reconstrucción de 36 archivos cada una,
con seis análisis y cinco pares CSV/JSON calculados en terminal. La demostración
añadirá dos pares **descargados realmente** y notas personales en otra carpeta.
Ninguna salida de terminal prueba por sí sola aprendizaje o uso del navegador.

## Actividades

1. **Predice dos casos.** Escribe filtros, filas completas, universo e indicadores
   para octubre/ambos/2000 y septiembre/ambos/2000. Explica el denominador del
   porcentaje. No ejecutes todavía para copiar la respuesta.
2. **Prepara y crea.** Genera `output/practica_1209` y `output/entrega_1209` con
   los comandos de los recorridos. Lee su README y ubica código, fuente,
   contrato, entorno y resultados. Comprueba por qué `vacio` tiene CSV y
   `sin_corte` solamente análisis JSON.
3. **Contrasta desde fuera.** Ejecuta el verificador de tu práctica con la fuente
   original del repositorio como referencia externa. Relee los análisis y CSV
   de los dos casos predichos: ID, segmento, corte e importe deben coincidir.
   Guarda el diagnóstico y explica qué no demuestra el SHA-256.
4. **Reconstruye con tu compañero.** Desde la carpeta entregada, usando su README,
   crea `output/reconstruida_1209` como carpeta hermana. No abras fuentes de
   lecciones anteriores para completar archivos que faltan. Contrasta la nueva
   carpeta contra la misma referencia y ejecuta las pruebas de modelo/AppTest.
   Si también reconstruyes el entorno, usa una biblioteca local nueva y el
   lockfile incluido; registra cómo lo hiciste.
5. **Detecta una alteración compensada.** Desde la práctica correcta crea otra
   entrega `output/alterada_1209`. Solo en su
   `resultados/septiembre/analisis.json`, intercambia los saldos de los dos
   seleccionados: 002 queda con 2500 y 003 con 2000. Conserva cantidad 2 y suma
   4500. Revisa contra la referencia: debe fallar por huella. Como experimento,
   actualiza únicamente la huella de ese archivo en su manifiesto y repite:
   debe seguir fallando, ahora por valores del análisis. No cambies la referencia,
   el revisor ni el resto de la entrega para aceptar la alteración.
6. **Demuestra la reconstrucción.** Arranca su app. Tu compañero elige septiembre,
   servicios/1900, servicios/1901 y noviembre; recupera octubre después. Envía
   un mínimo decimal y corrígelo. Ensaya un borrador sin enviar y ocultar tabla.
   Guarda dos pares descargados reales fuera de la entrega y contrasta todas
   sus columnas con la fuente, además de releer huellas/contextos. Repite con
   ventana estrecha y teclado. Recarga y explica qué estado se perdió.

La carpeta alterada es un experimento rechazado, no la entrega final. Conserva
el diagnóstico en tu nota externa y presenta la copia correcta. No publiques
datos personales, entornos, notas privadas ni carpetas generadas en el repositorio.

## Comprobación

| Revisión | Resultado exigido con la muestra del curso |
| --- | --- |
| Entrega y reconstrucción | Seis casos, seis filas, 36 archivos; datos conciliados por ID/corte |
| Octubre/ambos/2000 | 003, comercio, 2026-10-31, 2600; universo 3/4600, 33.33% |
| Septiembre/ambos/2000 | 002/servicios/2000 y 003/comercio/2500 del 2026-09-30; universo 3/4500, 66.67% |
| Servicios/1900 y /1901 | 002/1900 y después selección vacía válida con universo 3/4600 |
| Pruebas de reconstrucción | Siete métodos de modelo y once AppTest aprobados; mínimo opcional: uno |
| Alteración inicial y con huella actualizada | Ambos rechazos; el segundo detecta los valores por clave pese al total conservado |
| Navegador | Dos pares reales recuperados y releídos; rechazo/vacío/recuperación, recarga, teclado y ancho anotados |

No cambies un esperado correcto para hacer pasar una cifra errónea. Si el
problema es de entorno, archivo o permisos, registra el diagnóstico y corrige
esa causa en una copia de trabajo. Una revisión de archivos no sustituye las
pruebas de comportamiento ni la explicación de la persona.

<details>
<summary><strong>Pista: compara capas distintas</strong></summary>

La huella compara bytes con una declaración. La referencia externa permite
comparar el significado de esos bytes. Una suma de 4500 acepta muchas parejas
de importes; solamente una corresponde a 002/2000 y 003/2500 de septiembre.
Usa el revisor conservado en la práctica, no otro que cambiaste con el experimento.

</details>

<details>
<summary><strong>Solución razonada: alteración con total conservado</strong></summary>

Primero crea la entrega experimental con el constructor de tu práctica correcta.
Desde la raíz, guarda este fragmento como `output/alterar_1209.py`, fuera de la
carpeta entregable. Ejecútalo con tu Python activado:

```python
from pathlib import Path
from hashlib import sha256
import json

carpeta = Path("output/alterada_1209")
nombre = "resultados/septiembre/analisis.json"
archivo = carpeta / nombre
resultado = json.loads(archivo.read_text(encoding="utf-8"))
assert [f["id_credito"] for f in resultado["seleccion"]] == ["002", "003"]
resultado["seleccion"][0]["saldo_mxn"] = 2500
resultado["seleccion"][1]["saldo_mxn"] = 2000
archivo.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

Verifica ahora y conserva el rechazo de huella. Para el segundo experimento,
añade al archivo externo y vuelve a ejecutarlo:

```python
manifiesto = carpeta / "manifiesto.json"
datos = json.loads(manifiesto.read_text(encoding="utf-8"))
datos["sha256"][nombre] = sha256(archivo.read_bytes()).hexdigest()
manifiesto.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

Repite la verificación con el comando de los recorridos, cambiando solo la
carpeta revisada por `output/alterada_1209`. La huella vuelve a coincidir, pero
el análisis de septiembre ya no coincide con la referencia por ID/corte.
El revisor no ejecuta el código de la carpeta alterada ni modifica archivos.

Para corregir no necesitas reparar esta copia experimental: genera otra entrega
nueva desde la práctica correcta y repite la reconstrucción/contraste. La
evidencia personal conserva tanto el rechazo como la explicación del fallo.

</details>

## Evidencia y reflexión

Conserva la entrega correcta, su reconstrucción, diagnósticos, resultados de
pruebas y dos pares descargados con una nota externa: entorno, filtros,
predicción, valores por clave, navegador/ancho, ayudas, dudas y siguiente paso.

- ¿Qué información perdió un CSV seleccionado que recupera la entrega completa?
- ¿Por qué no basta actualizar las huellas después de un cambio compensado?
- ¿Qué reconstruiste realmente: archivos, entorno, resultados o una sesión?
- ¿Qué observó tu compañero y qué falta todavía comprobar?
- ¿Qué cambia al reiniciar, y qué debes guardar antes para retomar?

El material del módulo tiene nueve lecciones/labs; tu cierre requiere demostrar
y explicar la práctica. No hay proyecto integrador ni checkpoints implementados
por esta actividad. PROGRESS.md conserva autoría, no tu bitácora personal.

## Siguiente paso

Revisa el [criterio de salida](../../../curriculum/12_streamlit/09_local_delivery/README.md#evidencia-y-criterio-de-salida).
El siguiente tramo es [14.01 — Pregunta y contrato del producto](../../../curriculum/14_reproducible_projects/01_product_question_contract/README.md),
disponible con lección y lab; 14.02–14.07 también tienen lecciones/labs y 14.08–14.09 siguen planificadas. [13 — Shiny](../../../curriculum/13_shiny_web/README.md) es
una alternativa a Streamlit, no un requisito adicional para continuar.

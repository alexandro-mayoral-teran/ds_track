# Lab 05.11 — Reconstruir y explicar una entrega Python

## Propósito, entradas y resultado

Esta práctica de cierre acompaña
[05.11 — Cierre del proyecto Python](../../../curriculum/05_python_applied/11_project_closure/README.md).
Integra organización, configuración, errores, pruebas y contratos. Las ampliaciones
05.06–05.10 no son obligatorias. Una sesión puede cubrir parte de la actividad.

Recibes el paquete existente, [config.json](../../../curriculum/05_python_applied/11_project_closure/config.json),
el script ejecutar_seguro.py y
[verificar_entrega.py](../../../curriculum/05_python_applied/01_notebook_to_modules/verificar_entrega.py).
Las fuentes tienen 48 observaciones en dos cortes. No se cambia la base de SQL ni
se consulta una API. Usa el entorno elegido y los recorridos completos de tu shell
en la lección; no necesitas instalaciones nuevas.

Entrega dos carpetas equivalentes, una explicación de resultados, evidencia de
una falla controlada y una prueba propia. Conserva entradas y resultados previos;
todos los destinos deben ser nuevos. No hay proyecto/checkpoint implementado
asociado: esta práctica integra el paquete educativo disponible.

## A. Preparar instrucciones que otra persona pueda seguir

Antes de ejecutar, identifica directorio inicial, entorno, comando, configuración,
fuentes, fecha, salida y código de éxito. Explica la prioridad de --source sobre
el JSON y la diferencia entre rutas del archivo y rutas de terminal.

Predice los valores de Todos y el tratamiento de educación. Localiza tu evidencia
anterior de pandas/SQL y visualización para contrastarla después. No cambies una
regla para conseguir las cifras: comprueba primero la unidad y las entradas.

<details>
<summary>Orientación</summary>

Para 2026-10-31 esperamos 24 registros, 21 saldos conocidos, mediana 2300 MXN y
cobertura 87,5 %. Educación tiene tres registros sin saldo conocido: mediana
ausente y cobertura 0 %, no una mediana de cero. El JSON resuelve source respecto
de su carpeta; una ruta de --source se resuelve desde donde ejecutas el comando
y reemplaza ese valor. Mantener esta diferencia explícita permite reconstruir
desde las copias de la entrega.

</details>

## B. Producir y verificar la entrega

Sigue el recorrido de la lección hasta la primera verificación. Comprueba código
0, cierre.json, cinco tablas y 20 conciliaciones. La colección combinada debe
tener 115 métodos antes de tus ejercicios. Revisa también configuración efectiva,
versiones y las copias de fuentes.

Abre informe.md y matplotlib.png o matplotlib.svg. Revisa títulos, fecha, unidad,
escala, etiquetas, cobertura y ausencia de mediana. Relaciona cada marca con una
fila de resumen.csv; no basta con que el archivo abra. El HTML es opcional para
esta revisión y puede necesitar red.

<details>
<summary>Comprobaciones esperadas</summary>

Con dpi=160, el PNG mide 1920 × 880. Comercio muestra mediana 3100 y 5/5;
consumo 1750 y 10/10; servicios 2550 y 6/6. Educación comunica «Sin mediana · 0/3»
y cobertura cero. El pie debe distinguir las dos medidas y sus limitaciones.
El aviso de cobertura parcial 21/24 describe una condición conocida del dato;
no impide cerrar una entrega válida.

El verificador recalcula desde fuentes/ de la entrega y comprueba tablas y
especificación Altair. Solo comprueba algunas propiedades de PNG/SVG. Por eso
su resultado conserva revision_visual pendiente: la revisión humana se registra
con la evidencia de la práctica, sin modificar el marcador para aparentarla.

</details>

## C. Reconstruir desde las copias

Continúa el recorrido hacia reconstruccion_01 usando --source con fuentes/ de
la primera entrega. No apuntes otra vez a los CSV originales. Compara ambas
carpetas con --compare y abre sus figuras. Explica qué se comparó exactamente
y qué puede variar sin cambiar el resultado del análisis.

Pide a quien te acompaña que siga tus instrucciones desde la raíz con su entorno
compatible. Si no hubo esa segunda revisión, registra que está pendiente, sin
afirmar que otra persona ya pudo reconstruir.

<details>
<summary>Resultado e interpretación</summary>

Se espera reconstruccion_equivalente, mismo corte y hashes de fuentes, cinco
tablas equivalentes y especificación Altair igual. La ruta de ejecución cambia,
pero los datos usados son los de la entrega. Una nueva carpeta conserva la anterior.
No se exige igualdad de bytes de imágenes; metadatos y renderizado pueden variar.
Revisa que ambas representen los mismos valores y mensajes. Una diferencia en
fuentes o corte requiere otra comparación; no es la misma reconstrucción.

</details>

## D. Observar una falla sin confundir archivos con cierre

Completa el comando con --simulate-failure before-close hacia parcial_01 y
verifica esa carpeta. Registra ambos códigos 1. Comprueba que pueden existir
tablas y figuras sin un cierre válido. Conserva la carpeta parcial para explicar
en qué etapa falló; vuelve a ejecutar normalmente hacia otra carpeta nueva.

Lee test_tabla_editada_con_marcador_existente en
[las pruebas](../../../curriculum/05_python_applied/01_notebook_to_modules/pruebas_0511/test_auditoria.py).
Explica por qué inspect_delivery puede informar completada y verify_delivery
detectar una tabla alterada después. No edites tu entrega de referencia para probarlo.

<details>
<summary>Interpretación razonada</summary>

El marcador final se escribe después de las etapas. La falla simulada ocurre
antes: los archivos anteriores pueden estar completos, pero no se declara la
ejecución cerrada. El verificador no corrige esa carpeta ni crea un marcador.

inspect_delivery revisa presencia y estructura de cierre; no recalcula todos los
archivos. Las pruebas alteran copias temporales de indicadores.csv y conservan
el marcador. verify_delivery vuelve a calcular y encuentra el cambio. Esa
distinción evita confundir existencia de archivos con coherencia de resultados.

</details>

## E. Prueba propia: detectar una columna renombrada

Añade a PruebasAuditoria un método que cambie, **en su copia temporal**, la
columna id_credito de corte.csv por credito. Conserva los valores y exige que
verify_delivery rechace la tabla. Ejecuta nuevamente pruebas nuevas y combinadas.
No cambies la fuente ni el contrato para hacer pasar la prueba.

<details>
<summary>Una solución y su explicación</summary>

En test_auditoria.py, dentro de PruebasAuditoria, los nombres ya están importados
y self.output apunta a una copia temporal preparada por cada prueba:

```python
    def test_columna_renombrada_se_detecta(self):
        path = self.output / "corte.csv"
        table = pd.read_csv(path, dtype={"id_credito": "string"})
        table = table.rename(columns={"id_credito": "credito"})
        table.to_csv(path, index=False)
        with self.assertRaisesRegex(ValueError, "corte.csv"):
            verify_delivery(self.output)
```

Conservar números de filas y valores no basta si cambia la estructura esperada.
La comparación detecta nombres de columnas además del contenido. La solución
aislada deja 11 métodos nuevos y 116 combinados; tus ejercicios pueden añadir más.
El setUp copia la entrega base y cada prueba modifica solo su propia carpeta.

</details>

## Evidencia, reflexión y continuidad

Conserva instrucciones, configuración, dos entregas, informe de comparación,
comandos/códigos de la falla y prueba propia. Añade una explicación breve de la
revisión visual y de lo que aún falta comprobar con otra persona.

- ¿Qué entradas/reglas permiten interpretar la mediana y su cobertura?
- ¿Qué hace reconstruible la entrega además de guardar una imagen?
- ¿Qué protege una prueba de estructura que no protege contar filas?
- ¿Qué demuestra el cierre, qué recalcula el verificador y qué revisa una persona?

Registra en PROGRESS.md evidencia real y dudas. Puedes cerrar el módulo cuando
la entrega se reconstruya, los resultados concilien, la figura sea legible y
expliques una prueba que detecta una falla relevante. El material completo no
acredita automáticamente haber completado estas prácticas.

Continúa con [06 — R fundamental](../../../curriculum/06_r_foundations/README.md),
cuyas lecciones siguen planificadas. Su
[primera sección prevista](../../../curriculum/06_r_foundations/README.md#01-r-editor-scripts-y-paquetes)
introducirá el entorno y modelo propio de R. No hay que completar todas las
ampliaciones de Python para avanzar. Volver a la
[lección 05.11](../../../curriculum/05_python_applied/11_project_closure/README.md).

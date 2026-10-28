# Lab 12.03 — Un análisis, dos consumidores

[Inicio](../../../README.md) / [Labs](../../README.md) / [Módulo 12](../../../curriculum/12_streamlit/README.md) / **Lab 12.03**

## Propósito

Comprobar que la interfaz y la terminal reutilizan la misma transformación,
sin duplicar reglas y conservando registros verificables.

## Entradas y preparación

- [Lección 12.03](../../../curriculum/12_streamlit/03_data_interface/README.md),
  [datos](../../../curriculum/12_streamlit/03_data_interface/cartera.csv) y
  [recorridos por shell](../../../curriculum/12_streamlit/03_data_interface/recorridos.md).
- Python estándar para el ejecutor; el entorno local de 12.01 para Streamlit.
- Copia **la carpeta completa** `03_data_interface` a una carpeta personal nueva.
  No basta copiar app.py: necesita módulos hermanos y CSV. No alteres originales.
  No se requieren entregas de labs anteriores.

## Antes de ejecutar: predice

1. Octubre, ambos segmentos, mínimo 2000: escribe IDs, saldo y universo.
2. Septiembre, mínimo 2001: ¿qué registro deja de cumplir?
3. Si vacías segmentos, ¿cambia el denominador del corte?
4. Cambiarás el saldo de 003 en octubre de 2600 a 2800. ¿Qué cambia y qué permanece?

## Actividad

1. Ejecuta el script y arranca la app de tu copia siguiendo los recorridos.
   Compara octubre ≥ 2000 y septiembre ≥ 2001. Usa parámetros iguales: por
   ejemplo `--corte 2026-09-30 --minimo 2001` en el ejecutor.
2. Sigue una llamada a `analizar` en ambos archivos. Señala dónde se lee el CSV,
   dónde se calcula y dónde se imprime o dibuja. No agregues otra suma a la app.
3. Detén la app. En el CSV de tu copia cambia **solo** el saldo de 003 en octubre:
   `2600` → `2800`. Reinicia y ejecuta nuevamente el script. Contrasta detalle,
   universo, cantidad, saldo y porcentaje con tu predicción.
4. Cambia la carpeta actual de la terminal. Ejecuta el script mediante su ruta
   absoluta, entre comillas si tiene espacios. El CSV predeterminado debe seguir
   siendo el que acompaña al script, no uno de la carpeta actual.
5. Ejecuta con `--segmentos` sin valores, y luego con `--corte 2026-11-30`.
   Contrasta lista vacía/0% frente a universo vacío/`null`.
6. En la copia agrega de nuevo la fila de 001 en septiembre. Pregunta por octubre.
   Debe rechazarse el conjunto por clave repetida aunque esa fila no cumpla el
   filtro. La app debe detenerse con un mensaje y el ejecutor no producir JSON
   de éxito. Retira **solo la fila agregada en tu copia** y comprueba recuperación.

Si editaste Python o configuración, reinicia el servidor. No dependas de que
los módulos importados se vuelvan a cargar con cada cambio de widget.

## Resultado y comprobación

Anota parámetros efectivos y parejas ID/importe en ambos consumidores. Compara
también segmento y fecha; un total igual por sí solo no garantiza filas iguales.

| Caso | Qué debes comprobar |
| --- | --- |
| Base octubre ≥ 2000 | Un registro, 003/2600; universo 3/4600; 33.33% |
| Base septiembre ≥ 2001 | Un registro, 003/2500; universo 3/4500; 33.33% |
| Variante octubre ≥ 2000 | Un registro, 003/2800; universo 3/4800; 33.33% |
| Variante, ningún segmento | Cero elegidos; universo 3/4800; 0% |
| Noviembre | Universo cero, porcentaje no definido: JSON null |
| Duplicado fuera del filtro | Rechazo completo; ninguna selección presentada como válida |

<details>
<summary><strong>Ver solución razonada</strong></summary>

El cambio afecta al saldo de 003, que sigue cumpliendo el mínimo. Por eso aumentan
saldo seleccionado y saldo del universo en 200 MXN, pero la cantidad continúa
siendo uno de tres. El porcentaje de créditos no cambia. Septiembre permanece
intacto porque se modificó otro corte. `analizar` hace este cálculo una sola vez
en el código; cada consumidor lo llama con sus entradas.

Vaciar segmentos deja de seleccionar registros sin borrar el universo: 0/3 es
0%. Noviembre no existe en esta muestra: 0/0 no está definido, por lo que no se
presenta como 0%. El duplicado de septiembre se detecta porque la validación
antecede al filtro de octubre.

La ruta predeterminada nace de `__file__` en configuracion.py. Al usar `--fuente`
con una ruta relativa estás dando otra regla: esa ruta pertenece a la carpeta
actual de la terminal. En ambos casos, `cartera.py` recibe la ruta explícitamente.

</details>

## Evidencia y reflexión

Conserva tu carpeta, predicciones, dos salidas conciliadas y una nota del rechazo
y recuperación. No necesitas capturas de cada combinación; el detalle y los
parámetros deben poder reconstruirse. Tu compañero puede revisar la app mientras
tú justificas el JSON.

- ¿Qué código cambiarías para presentar el saldo en miles sin alterar pesos enteros?
- ¿Qué función puedes llamar sin Streamlit y por qué?
- ¿Por qué importar el modelo no debería leer inmediatamente el archivo?
- ¿Qué detecta comparar ambos consumidores y qué requiere una referencia manual?

Guarda esta evidencia y las ayudas recibidas en tu bitácora personal. PROGRESS.md
registra autoría del material, no tu avance. No hay proyecto/checkpoint asociado.

## Siguiente paso

Vuelve a la [lección](../../../curriculum/12_streamlit/03_data_interface/README.md)
y revisa el criterio de salida. Después consulta
[12.04 — Estado de sesión y formularios](../../../curriculum/12_streamlit/README.md#04-estado-de-sesion-y-formularios),
todavía planificado.

# Lab 11.09 — Reconstruir, conciliar y entregar

## Entrada y objetivo

Lee la [lección 11.09](../../../curriculum/11_reporting_quarto/09_reproducible_report_closure/README.md).
Usa su preparador Python o R: siete filas propias, contrato completo y entorno
local. No se requieren entregas anteriores ni dashboard/PDF. Basta un motor.

Una persona construye; su compañero conserva la referencia y revisa. Después
intercambien papeles. Dividan la práctica en sesiones si hace falta.

## Actividad

1. Antes de ejecutar, anota pregunta, unidad por fila, claves, mínimo y
   denominador. Predice septiembre con mínimo 2000.
2. Prepara una carpeta nueva, inspecciona sus fuentes y construye siguiendo
   el recorrido de tu motor. Conserva HTML, salidas, comando, registro y huellas.
3. Tu compañero comprueba contra el CSV original externo y los parámetros
   esperados. En R puede usar el mismo verificador Python estándar o documentar
   la conciliación manual de las siete claves y las salidas del corte.
4. Abre el HTML sin conexión. Revisa navegación, ambas tablas, etiquetas y
   barras en ventana amplia y estrecha; usa teclado en el detalle.
5. Copia solo fuentes a otra carpeta con `copiar_fuentes.py`. Comprueba que
   no existen HTML, salida, cachés ni biblioteca instalada. Reconstruye desde
   esa copia con una sesión nueva y vuelve a conciliar.
6. En una tercera copia cambia parámetros a octubre, mínimo 4000. Verifica
   selección vacía sin perder el universo. No edites resultados a mano.
7. Conserva otra referencia externa y cambia 003/septiembre a 3600; construye
   otra copia desde ella y explica cómo cambian texto, tablas y figura.
8. En una copia de prueba duplica una clave de octubre y solicita septiembre.
   Explica por qué el error debe bloquear la entrega aunque esté fuera del filtro.
9. Entrega a tu compañero las fuentes y las instrucciones. Pídele que explique
   qué archivo permite leer, cuál reconstruir y qué no prueba una huella MD5.

## Resultado y comprobación

La carpeta completa y la reconstruida deben concordar por clave, indicadores,
texto y datos de barras. Es normal que algunos bytes del HTML o PNG varíen
entre plataformas: no sustituyas la comparación de valores por igualdad binaria.
El verificador comprueba la igualdad del PNG entregado con el incluido en su
propio HTML, no la equivalencia visual de dos renderizados distintos.

<details>
<summary>Resultados esperados y explicación</summary>

Septiembre: tres créditos, 6000 MXN; 002 y 003 cumplen, suman 5000 y representan
2/3 = 66.67% de los créditos. No es 5000/6000: esa sería una proporción de saldo.

Octubre con mínimo 4000: universo cuatro/7000; selección cero/0 y 0.00%.
Los cuatro registros continúan en el detalle. Cero seleccionados no significa
que falte el corte.

Al cambiar 003/septiembre a 3600: universo 6600, selección 5600; se mantienen
dos seleccionados y 66.67%. Hay cambios de pesos sin cambiar el porcentaje
de créditos. Deben regenerarse narrativa, resumen y barras desde la nueva fuente.

Una clave duplicada invalida la fuente completa aunque se solicite otro corte.
Rechazarla antes de seleccionar evita esconder errores detrás de un filtro.
Las huellas actualizadas por la misma persona que altera un archivo no son una
garantía independiente. La referencia externa y la reconstrucción aportan otras
comprobaciones; no certifican por sí solas el significado editorial.

</details>

## Evidencia y reflexión

Conserva rutas de las copias, parámetros, comando y versiones; resultado del
verificador o conciliación manual; captura del HTML final y nota de teclado;
predicciones frente a resultados; error deliberado y diagnóstico. Anota quién
reconstruyó y qué necesitó aclarar. No publiques datos privados ni entornos.

Explica: ¿por qué reconstruir sin HTML anterior?, ¿qué detecta comparar claves
que no detecta sumar?, ¿qué falta revisar después de un verificador exitoso?

## Criterio de salida y siguiente paso

Otra persona reconstruye el reporte con las mismas entradas, obtiene cifras
conciliadas y puede explicar el resultado y sus límites. Si solo tú puedes
reproducirlo, registra qué parte de las instrucciones debe mejorar.

Consulta [cierre del módulo](../../../docs/reporting-closure.md): el proyecto y
checkpoints siguen pendientes; completar material no acredita práctica personal.
La siguiente ruta numerada es [12 — Streamlit](../../../curriculum/12_streamlit/README.md)
o [13 — Shiny](../../../curriculum/13_shiny_web/README.md). Ambas tienen
lecciones, labs y entrega local disponibles; basta una aplicación. Consulta
su cierre de [Streamlit](../../../docs/streamlit-closure.md) o
[Shiny](../../../docs/shiny-closure.md). El módulo 14 sigue planificado.

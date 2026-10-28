# Streamlit — estado, comprobación y reanudación

## Alcance vigente

El [módulo 12](../curriculum/12_streamlit/README.md) dispone de **12.01–12.07**
con lecciones y labs. 12.08 y 12.09 conservan planes. Este documento define el
punto de reanudación y criterios pendientes; la bitácora de autoría vive en
[PROGRESS.md](../PROGRESS.md). Material disponible no acredita práctica del estudiante.

| Tramo disponible | Qué permite practicar |
| --- | --- |
| 12.01–12.02 | Arrancar/detener, observar reejecuciones y filtrar una muestra verificable |
| 12.03 | Reutilizar lectura, contrato y análisis desde app y ejecutor JSON |
| 12.04 | Separar borrador y filtros aplicados; conservar elecciones por sesión |
| 12.05 | Clave con registros/filtros/versión, TTL, limpieza y copias frente a recursos |
| 12.06 | Rechazar intentos, explicar vacíos y recuperar fuentes sin cifras engañosas |
| 12.07 | Conciliar tabla/gráfico/CSV/contexto y conservar archivos de la misma vista |

No hay proyecto integrador ni checkpoints Streamlit implementados. El cierre
local del recorrido completo sigue pendiente; desplegar en Internet no es requisito.
El portal es otro trabajo y no integra estas apps por disponer de fuentes nuevas.

## Cómo retomar la práctica

1. Abre la [lección 12.07](../curriculum/12_streamlit/07_tables_charts_download/README.md)
   y sus [recorridos](../curriculum/12_streamlit/07_tables_charts_download/recorridos.md).
2. Reutiliza el entorno local elegido en 12.01. Versiones comprobadas: Python
   3.12.12, Streamlit 1.66.1 y Altair 6.3.0 declarados en el proyecto. No reinstales
   globalmente ni cambies Conda/base o el entorno raíz para retomar.
3. Si conservas tu carpeta preparada, arranca su app; no vuelvas a preparar encima.
   Si necesitas una copia nueva, elige otro destino. Las fuentes incluidas bastan;
   no se exigen entregas anteriores.
4. Restaura la muestra de seis filas si hiciste variantes. Caso de referencia:
   octubre/ambos/2000 → 003/2600 MXN, universo 3/4600 y 33.33%.
5. Comprueba también septiembre/ambos/2000 → 002/2000 y 003/2500, universo
   3/4500 y 66.67%; relee CSV y contexto, no solo la captura.
6. Conserva datos de tu variante, CSV/contexto, predicción, resultado, ayudas y
   dudas en tu evidencia personal. La sesión y la caché no sustituyen esa bitácora.

Los servidores y URLs de una sesión de autoría son temporales. Los comandos de
arranque de la lección permiten reconstruir la práctica; un enlace local activo
no constituye alojamiento permanente.

## Decisiones que deben conservar las siguientes secciones

- Funciones de negocio de 12.03, capa de caché de 12.05 y entradas de 12.06 se
  reutilizan como fuentes; cada práctica se prepara en destino nuevo.
- Fuente completa validada antes de caché, claves ID/corte únicas y saldos enteros
  conocidos. No imputar ceros ni esconder duplicados fuera del filtro.
- Caché del análisis con registros completos, filtros y versión; TTL 60 segundos,
  máximo ocho entradas, sin disco. No evita la lectura ni acredita rendimiento o RAM acotada.
- Filtros aplicados por formulario y estado por sesión. Borradores sin enviar no
  cambian el análisis. Intentos rechazados se identifican y conservan filtros válidos.
- Fuente inválida, fuente sin filas o corte ausente no ofrecen métricas ni archivos
  de cartera. Selección vacía con universo válido puede descargar encabezado y contexto.
- Tabla, datos del gráfico y CSV consumen la misma selección. Gráfico con IDs
  nominales, pesos, cero inicial, etiquetas y alternativa textual; altura explícita
  comprobada en navegador para que las barras no queden comprimidas.
- Descarga de bytes preparados, `on_click="ignore"`, nombres con filtros y JSON
  con universo/indicadores/huella. Tras cambiar fuente se requiere otra pasada.
  Un intento rechazado deshabilita descargas hasta confirmar filtros válidos.
- La huella relaciona un CSV con su contexto; no autentica al autor ni prueba que
  todos los valores sean correctos frente a una fuente histórica. Revisar por clave.

## Siguiente desarrollo: 12.08

Convertir los controles de autoría en una explicación gradual de pruebas de app:

- Distinguir prueba de funciones, integración AppTest y revisión real de navegador.
- Enseñar primero un caso pequeño y después indicadores, valores por clave,
  transiciones de formulario, errores, vacío, recuperación y sesión nueva.
- Verificar descarga real además de datos preparados. En Streamlit 1.66.1,
  AppTest expone gráfico/descarga como elementos sin una API de interacción
  equivalente a todos los widgets; los datos del gráfico viajan en Arrow aparte
  de su especificación. Son detalles de la versión comprobada, no una API estable propia.
- Mostrar una regresión concreta que una comprobación detecte, sin limitarse
  a comparar una función con otra llamada a sí misma.

Los archivos comprobar_app.py existentes son apoyos opcionales de autoría;
su existencia no da por impartida ni implementada la lección 12.08.

## Después: 12.09 y cierre real

12.09 deberá reunir fuente/contrato, instrucciones y versiones, reconstrucción en
carpeta nueva, ejemplos comprobables y una entrega local. Tendrá que conciliar
los valores con una referencia, conservar contexto de filtros y justificar
límites de estado/caché/descarga. No marcar proyecto/checkpoints completos por
tener nueve labs; sus archivos y criterios deben implementarse explícitamente.

La revisión humana deberá comprobar explicación, decisiones, ayudas recibidas y
capacidad de recuperar la práctica. Desarrollar y ejecutar material no demuestra
que una persona ya aprendió o completó el recorrido.

## Comprobación disponible al cerrar 12.07

Se ejecutaron controles de 12.07 en dos entornos locales existentes, con las
versiones indicadas, sin nuevas dependencias. Incluyen datos del gráfico frente
a tabla, CSV releído, contexto/huella, vacío, cero, rechazo, recuperación y fuentes
previas conservadas. En navegador se descargaron archivos reales de varios casos,
incluido borrador sin enviar, tabla oculta, variante de datos y móvil. La revisión
visual comprobó barras separadas, etiquetas y valores recuperables.

Esto describe la evidencia de autoría de esa sección. No certifica todos los
navegadores, sistemas operativos, accesibilidad completa, autenticidad de entregas
ni una ejecución futura. Los detalles y resultados concretos quedan en PROGRESS.md.

# Streamlit — estado, comprobación y reanudación

## Alcance vigente

El [módulo 12](../curriculum/12_streamlit/README.md) dispone de **12.01–12.09**
con lecciones y labs. Las nueve secciones tienen material de cierre local. Este documento define el
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
| 12.08 | Probar funciones y AppTest con expectativas explícitas, detectar una regresión y revisar límites en navegador |
| 12.09 | Crear una entrega, contrastarla contra referencia externa y reconstruirla desde sus fuentes |

No hay proyecto integrador ni checkpoints Streamlit implementados. La práctica de cierre
local debe demostrarse individualmente; desplegar en Internet no es requisito.
El portal es otro trabajo y no integra estas apps por disponer de fuentes nuevas.

## Cómo retomar la práctica

1. Abre la [lección 12.09](../curriculum/12_streamlit/09_local_delivery/README.md)
   y sus [recorridos](../curriculum/12_streamlit/09_local_delivery/recorridos.md).
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

## Pruebas disponibles: 12.08

La sección distingue prueba de funciones, integración AppTest y revisión real
de navegador. Incluye mínimo de dos ventas, suites con expectativas por clave,
frontera, errores tratados, vacío, recuperación y sesión nueva. Un experimento
independiente cambia saldo seleccionado por saldo del universo para observar
un fallo aunque la app abra sin excepciones. El lab añade servicios/1900–1901.

Cada caso de integración usa CSV temporal y ruta configurada durante la prueba;
limpia la caché y restaura configuración aun al fallar. AppTest nuevo no implica
caché independiente. Las suites se ejecutan secuencialmente y en procesos propios.

En Streamlit 1.66.1, gráfico/descarga se inspeccionan como elementos de protocolo;
la lectura Arrow del gráfico es ampliación de versión. Datos preparados y botones
habilitados no demuestran una descarga en navegador. La lección incluye un
protocolo de descarga real, borrador sin enviar, rechazo, vacío, teclado y ventana
estrecha. Los comprobar_app.py previos siguen como apoyos opcionales de autoría.

## Entrega disponible y práctica de cierre: 12.09

El preparador reúne las fuentes de 12.08 y añade constructor/verificador,
instrucciones autocontenidas y copias de pyproject.toml/uv.lock sin cambios.
La entrega tiene 36 archivos: fuente/contrato, código/pruebas, seis análisis,
cinco pares CSV/JSON calculados en terminal y manifiesto SHA-256. Noviembre
conserva diagnóstico sin descarga; vacío válido conserva encabezado/contexto.

El constructor exige destino nuevo fuera de su fuente y recalcula desde el CSV;
no utiliza resultados anteriores como entrada ni transporta entornos/caché.
El verificador solo lee y no importa código de la carpeta revisada: valida
inventario/huellas, fuente completa por ID/corte, filtros y todos los valores
contra una referencia CSV externa. La referencia y el revisor deben conservarse
fuera de la entrega; el contraste no autentica su procedencia. La muestra de
cierre requiere septiembre y octubre presentes y noviembre sin registros.

La reconstrucción funciona desde los archivos entregados, sin el repositorio
original; el README explica reconstruir el entorno local con el lockfile completo.
Las suites de 12.08 conservan expectativas de las seis filas del curso. Para una
variante legítima se revisan casos y documentación en una copia de trabajo;
el verificador de valores usa la referencia externa elegida.

Retomar la práctica exige otra carpeta, pruebas actuales, demostración de filtros/
vacíos/rechazo/recuperación y dos pares descargados realmente. Resultados de
terminal, huellas o AppTest no acreditan una descarga ni revisión humana.
Conservar entorno, filtros, claves, ayudas, navegador/ancho y pendientes en
la evidencia personal. La sesión y la caché no guardan aprendizaje.

El material de Streamlit está desarrollado; práctica personal y proyectos/
checkpoints siguen pendientes. Shiny es una alternativa. Continúa con
[14 — Proyecto reproducible](../curriculum/14_reproducible_projects/README.md) y
su [revisión final disponible](reproducible-projects-closure.md). No se requiere
una segunda app, despliegue ni ampliación del portal para este cierre local.

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

## Comprobación disponible al cerrar 12.08

Las suites de referencia y las soluciones del lab se comprobaron en dos entornos
locales existentes. Se detectaron la métrica de universo usada como selección y
un intercambio de saldos con total conservado. En Chrome headless se recuperaron
nueve pares CSV/JSON reales, incluidos servicios/1900–1901, y se releyeron con el
revisor estándar y referencias por clave. Borrador/Enter, rechazo, recuperación,
recarga, móvil y recorrido con teclado se comprobaron por separado de AppTest.
Las páginas nuevas se revisaron como GFM a dos anchos. Detalles en PROGRESS.md;
no acredita aprendizaje, accesibilidad completa ni otros navegadores.

## Comprobación disponible al cerrar 12.09

Doce controles de entrega pasaron en los dos entornos existentes. Se reconstruyó
desde los archivos entregados y se restauraron dos entornos locales nuevos con
el lockfile, desde caché y sin red; las 19 pruebas de referencia pasaron en cada
copia. Se conciliaron los seis casos con referencia externa y se rechazaron
alteraciones compensadas aun con huellas actualizadas. Verificación de solo
lectura y programas/metadatos anteriores preservados.

La app reconstruida se revisó en Chrome headless a 1440/390: nueve pares reales
recuperados, relectura estándar y contraste por clave; estados, recuperación,
recarga y teclado comprobados. Se revisaron seis páginas como GFM a dos anchos.
Esto describe evidencia de autoría: no certifica aprendizaje, accesibilidad
completa ni otros navegadores. Detalles en PROGRESS.md.

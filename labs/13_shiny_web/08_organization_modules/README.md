# Lab 13.08 — Organización y módulos

[Inicio](../../../README.md) / [Módulo 13](../../../curriculum/13_shiny_web/README.md) / **Lab 13.08**

| Tu sesión | Qué prepararás o comprobarás |
| --- | --- |
| **Meta** | Reutilizar UI/servidor y demostrar independencia por instancia |
| **Entrada** | Copia nueva, dos módulos de número y dos consultas con la fuente de seis filas |
| **Evidencia** | Predicciones A/B, parejas de IDs, API del padre y CSV por instancia |

[Lección 13.08](../../../curriculum/13_shiny_web/08_organization_modules/README.md) · [Actividad](#actividad) · [Comprobación](#resultado-y-comprobación)

## Relación y preparación

Refuerza [13.08](../../../curriculum/13_shiny_web/08_organization_modules/README.md).
Sigue [los recorridos](../../../curriculum/13_shiny_web/08_organization_modules/recorridos.md)
en una carpeta nueva. No exige entregas anteriores ni tiene proyecto/checkpoint
implementado. Conserva las fuentes del curso; trabaja sobre tu copia.

La cartera conserva 001/002/003 con septiembre 0/2000/2500 y octubre 100/1900/2600
MXN. Una fila por ID/corte; el mínimo es inclusivo y la cobertura usa tres
créditos del corte antes de filtrar. No cambies estas reglas al organizar código.

## Actividad

### 1. Reconocer instancias en el mínimo

Abre minimo.R e inicia con iniciar_app desde la consola R. Antes de probar,
predice resultado de A, B y texto del padre para cada paso:

1. Inicio con ambos controles en 2, sin guardar.
2. Guarda 3 en A.
3. Guarda 7 en B.
4. Edita 0 en A, sin guardar.
5. Guarda A y luego guarda otra vez sin cambios.

Anota IDs externos uno/dos y nombres locales numero/guardar/resultado. Escribe
qué ID genera NS("uno")("guardar") y qué nombre lee el servidor dentro del
módulo. Explica por qué repetir las etiquetas visibles no es repetir los IDs.

### 2. Dos consultas con las mismas funciones

Detén el mínimo e inicia app.R. A y B deben empezar sin consulta aplicada.
Aplica septiembre/ambos/2000 en A y octubre/ambos/2000 en B. Contrasta en cada panel:

| Panel | IDs | Saldo MXN | Cantidad / cobertura |
| --- | --- | --- | --- |
| A | 002, 003 | 2000, 2500 | 2 / 66.67% |
| B | 003 | 2600 | 1 / 33.33% |

Revisa tabla, barras, alt y texto del padre. Descarga selección/contexto de A
y B a carpetas distintas; relee cada par siguiendo 13.07. Los nombres pueden
coincidir si consultas el mismo corte con filtros distintos; NS no nombra archivos.

Edita octubre en A sin aplicar: A conserva septiembre y B conserva octubre.
Oculta la tabla de A: B no debe cambiar. Aplica septiembre/comercio/0 en A:
001/0 y 003/2500, dos créditos/2500/66.67%; B sigue 003/2600. Descarga de nuevo
A y confirma que 001 se conserva en las filas.

### 3. Verificar la UI dinámica

Localiza consultaUI, moduleServer y renderUI en consulta_module.R. Identifica:

- NS(id) al crear los controles y contenedores estáticos.
- input$corte/output$resumen como nombres locales del servidor.
- session$ns("csv_seleccion") al crear un botón después de aplicar.
- La lectura reactiva estado que se devuelve al padre.

Con ambos paneles aplicados comprueba sus descargas por separado. Usar un solo
panel no bastaría para detectar una colisión dinámica. Quien acompaña puede
ayudar a inspeccionar los IDs en el navegador; no necesitas editar el DOM ni
usar JavaScript para completar la práctica.

### 4. Cambiar un ID sin reescribir el módulo

Detén el servidor. En app.R cambia solo el ID de la instancia A de izquierda
a principal, **en sus dos llamadas**: consultaUI y consultaServer. Conserva
los nombres de variables a/b y el ID de B. No cambies input, output ni los
botones dinámicos dentro del módulo.

Guarda, reinicia R, carga iniciar.R e inicia app.R. A debe seguir aplicando y
descargando septiembre y B octubre. El padre sigue leyendo a$estado()/b$estado().
Explica qué nombres de UI genera ahora el módulo y por qué no fue necesario
buscar izquierda dentro de sus renders. Restaura el ID original al terminar.

**Ampliación opcional:** escribe la pareja de llamadas que añadiría una tercera
instancia con ID revision. Explica qué colocarías en la UI padre y qué llamarías
en su servidor. No es necesario crear otro archivo con una copia del módulo.

### 5. Instancias frente a sesiones y fuente

Aplica vacío en A desmarcando segmentos: A conserva 0 seleccionados sobre tres,
CSV con encabezado y contexto; B no cambia. Prueba mínimo inválido en A y
comprueba que solo conserva su consulta anterior. Aplica noviembre en A: sin
universo ni descargas, mientras B sigue disponible.

Abre otra pestaña: tiene otras dos instancias sin consulta. Recargar la primera
también reinicia sus dos estados. Son sesiones, no usuarios autenticados.

**Ampliación opcional de fuente:** conserva un respaldo y renombra cartera.csv
de tu copia, manteniendo el servidor. Aplica solo A: A se bloquea y B conserva
su instantánea. Al aplicar B también detecta la ausencia. Restaura el nombre y
aplica cada panel para recuperarlo. No hay monitor ni duplicación física del CSV.

<details>
<summary>Ver una pista</summary>

El ID externo conecta UI y moduleServer. Dentro se usan nombres locales.
El padre recibe una función reactiva de lectura, no un control del módulo.
La fuente puede ser compartida como archivo aunque los estados no lo sean.

</details>

## Resultado y comprobación

Debes demostrar que dos instancias funcionan juntas, que el ID renombrado
sigue conectando controles/descargas y que las cifras de 13.07 no cambiaron.
Una app que solo abre sin errores no prueba independencia ni equivalencia.

<details>
<summary>Ver solución razonada</summary>

El mínimo mantiene 3/6 en A y 7/14 en B; editar 0 no aplica y guardarlo produce
0/0 solo en A. El padre lee los valores devueltos, sin reconstruirlos de inputs.
En las consultas A=septiembre 002/003/4500 y B=octubre 003/2600; cada porcentaje
usa tres créditos de su propio corte. Cambiar A no escribe estado de B.

Al renombrar A, NS produce principal-corte y principal-csv_seleccion, entre
otros. El servidor sigue usando input$corte y output$csv_seleccion locales.
Hay una sola definición del módulo, invocada con dos IDs. La ruta es un parámetro
explícito; ambas instancias pueden leer el mismo archivo al aplicar sin compartir
sus reactiveVal. Recargar crea una nueva sesión, sin persistencia.

</details>

## Evidencia y reflexión

Conserva mapa de archivos, predicciones, pares CSV por panel y nota del ID
renombrado en tu copia personal. Registra ayudas/dudas fuera de PROGRESS.md.
Quien acompaña propone un cambio de un panel y pide explicar el otro antes de probar.

- ¿Por qué separar un archivo no resuelve por sí solo la colisión de IDs?
- ¿Por qué poner estado fuera de moduleServer mezclaría instancias?
- ¿Qué lee el padre y qué no necesita conocer de los controles internos?
- ¿Por qué NS no renombra CSV ni ofrece autenticación?

## Siguiente paso

Consulta [13.09 — Pruebas y observación del flujo](../../../curriculum/13_shiny_web/README.md#09-pruebas-y-observacion-del-flujo), todavía planificado.

[← Lección 13.08](../../../curriculum/13_shiny_web/08_organization_modules/README.md) · [Módulo 13](../../../curriculum/13_shiny_web/README.md)

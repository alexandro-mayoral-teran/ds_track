# Lab 14.08 — Entregar y reconstruir sin copiar el entorno

[Inicio](../../../README.md) / [Módulo 14](../../../curriculum/14_reproducible_projects/README.md) / **Lab 14.08**

> **Opcional:** permite practicar la entrega local. CI es una ampliación dentro
> de esta práctica. No hay proyecto ni checkpoint implementado.

## Relación y objetivo

Refuerza [14.08 — Entrega y automatización opcional](../../../curriculum/14_reproducible_projects/08_delivery_optional_automation/README.md).
Objetivo: compartir un paquete comprobable y reconstruirlo desde sus fuentes,
explicando qué demuestra cada operación. Elige Python/Streamlit o R/Shiny.

## Entrada

Usa las 60 fuentes de los [recorridos](../../../curriculum/14_reproducible_projects/08_delivery_optional_automation/recorridos.md)
y un CSV de referencia conservado fuera del paquete. No necesitas entregas
personales previas. Conserva copias nuevas y usa un escritor.

La muestra sintética tiene tres créditos por corte, saldos MXN enteros y clave
ID/fecha. Octubre selecciona 003/2600 sobre universo 3/4600; septiembre 002/2000
y 003/2500 sobre 3/4500; vacío da cero seleccionados sobre universo 3/4600.
Coberturas: 1/3, 2/3 y 0%, respectivamente. La referencia debe permitir revisar
también los registros no seleccionados.

## 1. Predecir qué se compartirá

Antes de ejecutar, clasifica estos elementos como fuente, muestra o archivo
local que no debe copiarse: cartera.csv, pyproject.toml, renv.lock, .venv,
renv/library, un intento fallido, reporte.html, pruebas.py, .Rprofile,
una bitácora personal y CI_EJEMPLO.yml.

Contrasta tu decisión con catalogo.csv. Explica por qué .Rprofile se revisa como
código y por qué el lockfile no sustituye Python/R/Quarto ni contiene todos sus
instaladores. Tu acompañante elige dos elementos para que justifiques la decisión.

## 2. Producir y verificar el paquete

Completa el recorrido elegido: preparación, restauración del cálculo,
reconstrucción de tres casos y creación del paquete. Comprueba:

- 60 archivos en fuentes/ y 27 en muestra/.
- LEEME.md, ENTREGA.csv y MANIFIESTO.csv: 90 archivos totales.
- 89 filas de huellas; el manifiesto no se incluye a sí mismo.
- Ausencia de bibliotecas instaladas, cachés y bitácoras personales del autor.
- Aprobación del revisor local con referencia fuera del paquete.

Guarda el comando exacto y el resultado. No ejecutes automáticamente entrega.py/R
del paquete recibido como sustituto de herramientas revisadas. Si eliges R,
verificar no activa renv; construir y reconstruir sí exigen el entorno declarado.

<details>
<summary><strong>Pista: qué significa «externa»</strong></summary>

Usar paquete/fuentes/datos/entrada/cartera.csv como referencia de ese mismo
paquete se rechaza. Conserva el original por separado. Una ubicación externa
no autentica el archivo: explica de dónde procede y por qué lo elegiste.

</details>

## 3. Observar una alteración sin modificar el original

Conserva el paquete válido y crea **otra copia de ensayo**. En el editor cambia
solo el saldo seleccionado de 003 de octubre de 2600 a 2700 en
muestra/salidas/octubre_integrado/seleccion.csv. No toques la referencia externa.

Ejecuta el revisor desde las herramientas originales: debe rechazar. Anota
qué control lo detectó; no interpretes cualquier fallo de entorno/ruta como
evidencia de que detectó el saldo alterado. El paquete válido debe seguir aprobando.

Después responde sin renovar manualmente huellas para forzar aprobación:
¿bastaría cambiar el manifiesto? ¿Y si alguien cambia 2000/2500 a 2001/2499,
mantiene el total y actualiza todas las huellas? Explica qué comparación por
clave y referencia debe seguir rechazando el error.

## 4. Reconstruir solo desde fuentes

Usa la operación copiar/copiar_fuentes indicada en el recorrido para crear otra
carpeta con 60 fuentes. Antes de ejecutar, revisa código y metadatos, incluido
.Rprofile. Restaura el entorno local elegido y ejecuta el reconstruidor completo.
No copies muestra/, una biblioteca ni las salidas del autor.

Compara en cada caso:

1. Corte, segmentos, mínimo y reglas.
2. IDs, fechas, segmentos y saldos por crédito.
3. Universo, suma seleccionada y cobertura; tolerancia de 1e-10 puntos
   porcentuales al comparar las representaciones decimales.
4. Texto, etiquetas y barras en los nuevos HTML.
5. La app local elegida, después de restaurar su interfaz: mismo caso aplicado,
   borrador identificado y rechazo sin cifras anteriores.

Las horas de comprobación no necesitan coincidir con las de la muestra. Si
cambian bytes, las huellas pueden diferir: identifica la causa y no las uses
como sustituto de comparar valores. Con los mismos archivos que originan las
marcas y el mismo motor, esas revisiones pueden conservarse entre carpetas.

## 5. Explicar una automatización acotada

Lee CI_EJEMPLO.yml sin activarlo. Identifica disparador, permisos, dos acciones
fijadas, versión Python y comando ejecutado. Separa lo que aprobaría esa tarea
de lo que aún faltaría para comprobar el producto completo.

Como ampliación puedes ejecutar su comando en otra copia nueva sin .venv,
siguiendo el recorrido PowerShell. Una ejecución local correcta no demuestra
que el servicio hospedado se haya ejecutado. No habilites Actions ni publiques
una app como requisito de este lab.

## Resultado esperado y solución razonada

<details>
<summary><strong>Ver solución después de comprobar</strong></summary>

Las fuentes contienen receta, datos sintéticos, contratos, código, pruebas y
metadatos. La muestra contiene resultados para comparar. Un entorno instalado,
un intento con rutas locales y una bitácora personal quedan fuera. .Rprofile y
CI_EJEMPLO.yml son código/configuración que se revisa antes de activar o ejecutar.

El paquete tiene 90 archivos y 89 filas de huellas. Un saldo cambiado debe
fallar; renovar huellas no corrige una diferencia con la referencia externa ni
la asignación por crédito. Aun una verificación numérica aprobada no autentica
el código recibido: el revisor usa sus propias funciones y no lo ejecuta.

La copia reconstruida comienza con 60 fuentes y un entorno local nuevo.
Produce resultados que concilian 003/2600, 002/2000 + 003/2500 y vacío válido.
CI solo ejecuta siete grupos Python en un venv; no restaura uv/renv, renderiza,
sirve interfaces ni construye la entrega. La revisión final se realiza en 14.09.

</details>

## Evidencia y criterio de salida

Conserva clasificación inicial, paquete válido, copia alterada, diagnóstico,
referencia externa, copia de fuentes y salidas reconstruidas, comandos/versiones
y nota de comparación. No necesitas publicar ensayos ni rutas personales.
Tu acompañante debe poder seguir las instrucciones sin recibir tu entorno ni
copiar la muestra como si fuera una salida nueva.

Guarda evidencia y dudas en tu copia personal. PROGRESS.md registra material;
este lab no certifica aprendizaje, autenticidad ni un proyecto/checkpoint.

Siguiente lección: [14.09 — Revisión final y defensa de decisiones](../../../curriculum/14_reproducible_projects/09_final_review_defense/README.md),
disponible con su lab. [Volver a 14.08](../../../curriculum/14_reproducible_projects/08_delivery_optional_automation/README.md).

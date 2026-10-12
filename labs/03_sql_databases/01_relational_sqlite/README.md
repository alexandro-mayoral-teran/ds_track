# Lab 03.01 — Explicar tablas y relaciones

## Relación, entrada y resultado

- Lección: [Modelo relacional y SQLite](../../../curriculum/03_sql_databases/01_relational_sqlite/README.md).
- Entrada: script, esquema y tres CSV sintéticos de la lección.
- Resultado: base preparada y una nota o diagrama con unidades, claves y relaciones.
- Proyecto: todavía no aplica; el proyecto de base crediticia sigue previsto.

Reserva 50 a 80 minutos o dos sesiones. No necesitas editar el esquema ni escribir
joins. Conserva fuentes y bases previas; la exploración se hace en solo lectura.

## Parte A — Explicar el mapa

1. Antes de ejecutar, escribe qué representa una fila de cada tabla.
2. Identifica sus claves primarias y foráneas.
3. Sigue C001 → créditos 001/002 → cuatro observaciones de corte.
4. Explica por qué cuatro cortes no significan cuatro clientes.

<details>
<summary>Ver solución de la parte A</summary>

clientes identifica un cliente por id_cliente; creditos un crédito por id_credito;
cortes una observación por ID/fecha. creditos.id_cliente referencia clientes y
cortes.id_credito referencia creditos. C001 tiene dos créditos; ambos aparecen en
dos cortes. Son un cliente, dos créditos y cuatro observaciones temporales.

</details>

## Parte B — Preparar y repetir sin duplicar

1. Ejecuta el script y anota versión de SQLite y cantidades de filas.
2. Repite el comando; comprueba que la base existente se valida sin modificaciones.
3. Usa --database para crear otra base dentro de output y compara sus conteos.
4. Explica qué archivos son entradas y cuál es el resultado generado.

<details>
<summary>Ver comprobaciones de la parte B</summary>

Clientes 16, créditos 24 y cortes 48. La segunda ejecución conserva esos conteos:
no vuelve a insertar registros. La otra ruta crea una base independiente con los
mismos datos. Entradas: schema.sql y data/clientes.csv, creditos.csv y cortes.csv.
Resultado: archivo .sqlite en output, ignorado por Git. No se necesita instalar
una biblioteca adicional para el script de preparación.

</details>

## Parte C — Reconocer una clave compuesta

1. Sobre data/cortes.csv, identifica las dos observaciones de 001.
2. Predice qué pasaría si la clave fuera solo ID, o solo fecha.
3. Explica qué significa repetir exactamente ID 001 y corte 2026-09-30.
4. No cambies el esquema todavía: justifica el diseño con los registros existentes.

<details>
<summary>Ver solución de la parte C</summary>

001 aparece en septiembre con 1100 y en octubre con 1300. Solo ID impediría
guardar ambos cortes; solo fecha impediría guardar varios créditos en esa fecha.
La combinación ID/fecha distingue sus observaciones. Repetir 001/2026-09-30
viola esa clave aunque el saldo sea idéntico. No se resuelve sumando ambas filas.

</details>

## Parte D — Explorar sin escribir

1. Ejecuta el fragmento de lectura de la lección desde la raíz.
2. Comprueba las dos filas de 001 y su orden.
3. Sustituye el parámetro por "004"; observa el saldo cero de octubre.
4. Sobre el CSV fuente, revisa saldo de 005/septiembre: ¿es el mismo caso?

<details>
<summary>Ver solución de la parte D</summary>

001 produce 1100/1300; 004 produce 1400/0. Ese cero es un importe conocido.
005/septiembre tiene campo de saldo vacío en CSV: la base guarda NULL y Python
lo recupera como None. No representa cero. El orden procede de ORDER BY, y
la conexión se cierra al terminar el bloque finally.

</details>

## Parte E — Justificar la separación

1. Imagina que region se repite en cada observación de corte.
2. Describe un problema de modificar solo una de esas copias.
3. Explica qué papel tienen la clave foránea y su activación.
4. Identifica una regla que el esquema no pueda garantizar por sí solo.

<details>
<summary>Ver una explicación de la parte E</summary>

Una actualización parcial dejaría regiones incompatibles para el mismo cliente.
Guardar el atributo en clientes evita esas copias en este modelo estable. Las
claves foráneas habilitadas verifican que exista el padre; no prueban que el
cliente asignado corresponda a una persona real ni que una categoría sea verdadera.
Si región cambia con el tiempo, este esquema necesitaría un diseño de historia.

</details>

## Evidencia y siguiente paso

- Conserva una nota o diagrama que indique unidad, clave primaria y referencias.
- Anota conteos, versión del motor y explicación de NULL frente a cero.
- ¿Qué diferencia hay entre SQL, SQLite, sqlite3 y el archivo de base?
- ¿Qué tabla utilizarías para contar clientes, créditos u observaciones temporales?
- Si usas Git, registra notas/código tras revisar diff. output está ignorado;
  compartir tu base no es requisito para completar el lab.

Continúa con la [lección 03.02 — Primeras consultas](../../../curriculum/03_sql_databases/02_first_queries/README.md)
y después realiza su lab asociado.

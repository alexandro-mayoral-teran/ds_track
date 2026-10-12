# Lab 02.05 — Conservar aceptados y rechazos con motivos

## Relación, entrada y resultado

- Lección: [Faltantes, duplicados y reglas](../../../curriculum/02_pandas/05_missing_duplicates_rules/README.md).
- Entrada: cartera_calidad.csv (44 registros) y quality_rules.py de la lección.
- Resultado: tres CSV comprobados y una nota que justifique la política aplicada.
- Proyecto: todavía no aplica; el proyecto de limpieza sigue previsto.

Reserva 60 a 90 minutos o dos sesiones. Predice antes de consultar soluciones.
Usa el entorno existente y conserva la fuente. Las exploraciones pueden añadirse
dentro de main después de evaluar; las correcciones se hacen sobre una copia en output.

## Parte A — Identificar problemas distintos

1. Ejecuta el script y revisa 005, 014, 023 y 028.
2. Explica qué distingue ausencia, incompatibilidad, cero y regla de rango.
3. Revisa el registro 43: ¿por qué tiene cuatro motivos?
4. Comprueba 44 = 29 + 15. ¿Por qué 19 incumplimientos no significan 19 rechazados?

<details>
<summary>Ver solución de la parte A</summary>

005 carece de saldo; 014 contiene "error"; 023 contiene días "3.5", incompatibles
con el tipo entero requerido. Los tres se rechazan conservando el origen.
028 tiene saldo y pago cero y días cero: pasa las reglas; no falta información.

El registro 43, ID 041, tiene saldo −100, pago −50 y días −1: tres negativos y
además −50 > −100. Sus cuatro motivos se mantienen aunque uno solo baste para
rechazar. El registro 44 tiene dos campos ausentes. Los demás rechazados tienen
uno: 15 filas + 3 motivos adicionales + 1 adicional = 19 incumplimientos.

</details>

## Parte B — Comparar duplicados y claves

1. Sobre fuente, compara duplicated sin subset con duplicated sobre ID y corte.
2. Predice filas marcadas con keep="first" y keep=False.
3. Explica qué perderías al elegir automáticamente el primer registro de 002.
4. En una copia en memoria, cambia solo el corte del registro 42 a 2026-10-31;
   compara de nuevo la repetición de la clave. No necesitas convertir fechas aquí.

<details>
<summary>Ver solución de la parte B</summary>

```python
print(fuente.duplicated(keep=False).sum())  # 2 filas idénticas
print(fuente.duplicated(subset=CLAVE, keep=False).sum())  # 4 filas de claves repetidas
print(fuente.duplicated(subset=CLAVE, keep="first").sum())  # 2 copias posteriores
otra = fuente.copy()
otra.loc[otra.index[41], "fecha_corte"] = "2026-10-31"
print(otra.duplicated(subset=CLAVE, keep=False).sum())  # 2, ambas de 001
```

Los pagos de 002 son 200 y 250. Elegir el primero ocultaría la otra versión sin
evidencia de cuál corresponde. Tras cambiar el corte, las dos filas de 002 ya no
comparten la clave compuesta; eso no acredita que el nuevo corte sea correcto.
La posición 41 de iloc corresponde al registro 42, porque las posiciones empiezan en cero.

</details>

## Parte C — Una corrección verificable

1. Copia la entrada a output/cartera_practica.csv.
2. En esa copia, corrige solo el pago "pendiente" de 009 a 450.
3. Cambia entrada en main a esa copia; exporta a output/practica para distinguir ejecuciones.
4. Predice conteos y saldo aceptado/rechazado. Comprueba que desaparece únicamente su motivo.

<details>
<summary>Ver solución de la parte C</summary>

En main:

```python
entrada = carpeta / "output" / "cartera_practica.csv"
# En la llamada exportar, usar esta carpeta de salida:
# carpeta / "output" / "practica"
```

009 pasa a aceptado: saldo 3250 y pago 450 cumplen las reglas. Hay 30 aceptados,
14 rechazados y 18 incumplimientos. El saldo aceptado pasa a **180500** y el
rechazado a **54400**; el interpretable de entrada sigue siendo 234900.
La corrección de pago no altera el saldo de origen, solo cambia a qué partición pertenece.
Los demás problemas permanecen. La fuente versionada conserva "pendiente".

</details>

## Parte D — Corregir un problema no corrige toda la fila

1. Desde la muestra original, crea una copia en memoria del registro 43 con
   saldo 100, pago −50 y días −1. Evalúa la tabla modificada.
2. Predice cuántos motivos quedan y si cambia de partición.
3. En otra copia, deja pago y días en cero. Vuelve a comprobar.

<details>
<summary>Ver solución de la parte D</summary>

```python
otra = fuente.copy()
otra.loc[otra.index[42], "saldo_mxn"] = "100"
trabajo2, aceptados2, rechazados2, banderas2 = evaluar(otra)
print(rechazados2.loc[rechazados2["numero_registro"] == 43, "motivos"])
otra.loc[otra.index[42], ["pago_mxn", "dias_atraso"]] = ["0", "0"]
trabajo3, aceptados3, rechazados3, banderas3 = evaluar(otra)
```

En la primera corrección quedan pago_mxn_negativo y dias_atraso_negativo; el
registro sigue rechazado. Saldo ya no es negativo y −50 no supera 100.
Hay 17 incumplimientos, pero siguen 29 aceptados/15 rechazados.
Con saldo 100, pago 0 y días 0 pasa las reglas: 30 aceptados/14 rechazados y
15 incumplimientos. Son correcciones didácticas propuestas, no una autorización
para inventar valores en datos reales.

</details>

## Parte E — Vacíos y claves incompletas (ampliación opcional)

1. Evalúa fuente.iloc[:0].copy() y exporta a output/vacio.
2. Evalúa solo los registros 005 y 014, que carecen de saldo interpretable.
3. Evalúa dos copias del último registro, con ID ausente. ¿Se identifica una clave repetida?

<details>
<summary>Ver solución de la parte E</summary>

Sin entrada, aceptados y rechazados tienen cero filas y conservan columnas; las
salidas tienen encabezados. La suma con min_count=1 es NA.
Con 005 y 014 hay dos rechazados y ningún saldo interpretable: no afirmar un total cero.
Dos registros sin ID se rechazan por obligatoriedad, pero clave_repetida es False:
la clave incompleta no identifica un crédito. Duplicated por sí solo puede marcar
combinaciones faltantes repetidas; clave_presente impide asignarles esa identidad.

</details>

## Evidencia, reflexión y siguiente paso

- Conserva código y una nota con reglas, clave, motivos y conciliación antes/después.
- ¿Qué evidencia pedirías para resolver el conflicto de 002?
- ¿Por qué 028 pasa aunque su porcentaje no se pueda calcular?
- ¿Qué cantidades no conocemos aunque el saldo interpretable concilie?
- ¿Qué validaciones faltan antes de afirmar que el archivo está completamente limpio?
- Si usas Git, revisa diff y registra código/notas. output está ignorado; publicar
  resultados en el repo compartido no es requisito para completar el lab.

Continúa con el [alcance de 06 — Texto y fechas](../../../curriculum/02_pandas/README.md#06-texto-y-fechas),
pendiente de desarrollo, antes de su futuro lab.

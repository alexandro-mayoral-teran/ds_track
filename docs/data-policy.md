# Política de datos

El repositorio es público o potencialmente compartible. Todos los ejemplos deben
tratarse como si fueran a publicarse.

## Permitido

- Datos completamente sintéticos.
- Datasets públicos cuya licencia permita redistribución.
- Muestras pequeñas anonimizadas únicamente si existe autorización explícita y
  se ha evaluado el riesgo de reidentificación.
- Generadores deterministas con una semilla documentada.

## No permitido

- Datos reales de clientes o solicitudes de crédito.
- Nombres, teléfonos, correos, domicilios, CURP, RFC o identificadores reales.
- Credenciales, tokens, cadenas de conexión o archivos `.env`.
- Exportaciones internas, incluso si parecen no contener nombres.
- Resultados agregados que revelen información confidencial.

## Reglas del dataset sintético

- Los identificadores deben ser ficticios y no derivarse de datos reales.
- Los importes deben generarse artificialmente.
- El diccionario debe indicar tipo, unidad, nulabilidad y descripción.
- Las reglas de mora y pago deben documentarse para que los resultados puedan
  verificarse.
- Los archivos voluminosos deben generarse localmente, no almacenarse en Git.


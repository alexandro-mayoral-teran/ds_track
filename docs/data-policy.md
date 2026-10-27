# Política de datos

Aunque el repositorio tenga acceso privado, sus ejemplos son potencialmente
compartibles y deben prepararse con ese criterio.

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
- El diccionario debe indicar nombre de campo, tipo, unidad, nulabilidad,
  descripción, valores permitidos y sensibilidad.
- Las reglas de mora y pago deben documentarse para que los resultados puedan
  verificarse.
- Los archivos voluminosos deben generarse localmente, no almacenarse en Git.
- Cada generador debe documentar semilla o regla determinista, cantidad de
  registros, esquema, reglas y destino. No afirmar grandes volúmenes si la
  muestra o el contrato solo cubren una escala didáctica.

Las muestras y sus diccionarios vigentes están junto a las lecciones. Crear una
carpeta compartida de datos o generadores cuando exista material reutilizable;
no mantener carpetas vacías para representar un plan.


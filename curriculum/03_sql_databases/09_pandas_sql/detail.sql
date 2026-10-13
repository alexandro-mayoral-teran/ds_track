SELECT o.id_credito, o.fecha_corte, o.saldo_mxn, o.dias_atraso,
       c.id_cliente, c.segmento, p.region
FROM cortes AS o
INNER JOIN creditos AS c ON c.id_credito = o.id_credito
INNER JOIN clientes AS p ON p.id_cliente = c.id_cliente
WHERE o.fecha_corte = :fecha
ORDER BY o.id_credito;

SELECT c.segmento, COUNT(*) AS registros,
       COUNT(o.saldo_mxn) AS saldos_conocidos,
       SUM(o.saldo_mxn) AS suma_conocida_mxn,
       COUNT(o.dias_atraso) AS atrasos_conocidos,
       COUNT(CASE WHEN o.dias_atraso >= :umbral THEN 1 END) AS confirmados,
       100.0 * COUNT(CASE WHEN o.dias_atraso >= :umbral THEN 1 END)
           / NULLIF(COUNT(o.dias_atraso), 0) AS tasa_conocidos_pct,
       100.0 * COUNT(o.dias_atraso) / NULLIF(COUNT(*), 0) AS cobertura_atraso_pct
FROM cortes AS o
INNER JOIN creditos AS c ON c.id_credito = o.id_credito
WHERE o.fecha_corte = :fecha
GROUP BY c.segmento
ORDER BY c.segmento;

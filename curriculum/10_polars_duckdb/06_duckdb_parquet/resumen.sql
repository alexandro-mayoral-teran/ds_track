SELECT fecha_corte, COUNT(*) AS registros, SUM(saldo_mxn) AS saldo_mxn
FROM read_parquet(?)
GROUP BY fecha_corte
ORDER BY fecha_corte;

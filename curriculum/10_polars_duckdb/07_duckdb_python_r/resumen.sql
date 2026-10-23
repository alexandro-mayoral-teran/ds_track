SELECT fecha_corte, CAST(COUNT(*) AS VARCHAR) AS registros_texto,
       CAST(SUM(saldo_mxn) AS VARCHAR) AS saldo_texto
FROM read_parquet(?)
GROUP BY fecha_corte
ORDER BY fecha_corte;

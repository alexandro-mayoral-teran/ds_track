SELECT id_credito, saldo_mxn
FROM read_parquet(?)
WHERE fecha_corte = ? AND saldo_mxn >= ?
ORDER BY id_credito;

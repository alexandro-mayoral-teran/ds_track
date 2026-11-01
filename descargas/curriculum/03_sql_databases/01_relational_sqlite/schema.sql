-- Esquema preparado. Su construcción se estudia en la lección 03.
CREATE TABLE clientes (
    id_cliente TEXT PRIMARY KEY NOT NULL,
    alias TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE creditos (
    id_credito TEXT PRIMARY KEY NOT NULL,
    id_cliente TEXT NOT NULL,
    segmento TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE cortes (
    id_credito TEXT NOT NULL,
    fecha_corte TEXT NOT NULL,
    saldo_mxn INTEGER CHECK (saldo_mxn IS NULL OR (typeof(saldo_mxn) = 'integer' AND saldo_mxn >= 0)),
    dias_atraso INTEGER CHECK (dias_atraso IS NULL OR (typeof(dias_atraso) = 'integer' AND dias_atraso >= 0)),
    PRIMARY KEY (id_credito, fecha_corte),
    FOREIGN KEY (id_credito) REFERENCES creditos(id_credito)
);

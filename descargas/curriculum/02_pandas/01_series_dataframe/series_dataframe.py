"""Representa ventas ficticias como tablas y distingue etiquetas de posiciones."""

import pandas as pd


def crear_tabla(registros):
    """Mantiene las columnas previstas, incluso con una colección vacía."""
    return pd.DataFrame(
        registros, columns=["producto", "unidades", "precio_unitario_mxn"]
    )


def main():
    # Los datos ya están tipados: leer y convertir CSV se estudiará después.
    registros = [
        {"producto": "cuaderno", "unidades": 2, "precio_unitario_mxn": 40},
        {"producto": "lápiz, azul", "unidades": 5, "precio_unitario_mxn": 10},
        {"producto": "carpeta", "unidades": 1, "precio_unitario_mxn": 35},
    ]
    tabla = crear_tabla(registros)
    unidades = tabla["unidades"]  # Una columna: Series.
    tabla_unidades = tabla[["unidades"]]  # Lista de columnas: DataFrame.

    print(f"pandas: {pd.__version__}")
    print("\nTabla de ventas:")
    print(tabla)
    print(f"\nForma (filas, columnas): {tabla.shape}")
    print(f"Columnas: {list(tabla.columns)}")
    print(f"Índice: {list(tabla.index)}")
    print("Tipos por columna:")
    print(tabla.dtypes)
    print(f"\nUna columna: {type(unidades).__name__}, forma {unidades.shape}")
    print(f"Lista de columnas: {type(tabla_unidades).__name__}, forma {tabla_unidades.shape}")
    print(f"Total de unidades: {unidades.sum()}")

    # Las etiquetas personalizadas hacen visible la diferencia con las posiciones.
    etiquetada = tabla.copy()
    etiquetada.index = ["venta_a", "venta_b", "venta_c"]
    print(f"\nProducto por etiqueta: {etiquetada.loc['venta_b', 'producto']}")
    print(f"Producto por posición: {etiquetada.iloc[1, 0]}")


if __name__ == "__main__":
    main()

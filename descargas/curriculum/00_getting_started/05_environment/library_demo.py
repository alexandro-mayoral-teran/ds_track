"""Comprueba una biblioteca externa con tres ventas ficticias."""

from tabulate import tabulate

ventas = [("cuaderno", 80), ("lapiz", 50), ("carpeta", 35)]
print(tabulate(ventas, headers=["Producto", "Importe MXN"], tablefmt="github"))

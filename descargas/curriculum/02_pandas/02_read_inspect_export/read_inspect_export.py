"""Carga una cartera ficticia, inspecciona y verifica una copia CSV."""

from pathlib import Path

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso"]
TIPOS = {
    "id_credito": "string",
    "segmento": "string",
    "fecha_corte": "string",
    "saldo_mxn": "Int64",
    "dias_atraso": "Int64",
}


def leer_cartera(ruta):
    """Lee la muestra con columnas y tipos acordados; no limpia sus datos."""
    tabla = pd.read_csv(ruta, sep=",", encoding="utf-8-sig", dtype=TIPOS)
    if list(tabla.columns) != COLUMNAS:
        raise ValueError(f"Columnas esperadas, en este orden: {COLUMNAS}")
    return tabla


def guardar_y_comprobar(tabla, ruta_entrada, ruta_salida):
    """Escribe otro archivo y lo vuelve a leer con el mismo contrato."""
    if ruta_entrada.resolve() == ruta_salida.resolve():
        raise ValueError("Entrada y salida deben ser archivos distintos.")
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    tabla.to_csv(ruta_salida, index=False, encoding="utf-8", lineterminator="\n")
    recargada = leer_cartera(ruta_salida)
    if not tabla.equals(recargada):
        raise ValueError("La salida recargada no conserva la tabla original.")
    return recargada


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "cartera_demo.csv"
    salida = carpeta / "output" / "cartera_copia.csv"
    tabla = leer_cartera(entrada)

    print(f"pandas: {pd.__version__}")
    print("\nPrimeras cinco filas (no toda la tabla):")
    print(tabla.head())
    print(f"\nForma completa: {tabla.shape}")
    print("\nEstructura, tipos y valores presentes:")
    tabla.info()  # Imprime su propio informe; no utilizar print(tabla.info()).
    print("\nResumen de columnas numéricas:")
    print(tabla.describe())
    # min_count=1 evita mostrar cero cuando no hay ningún saldo conocido.
    print(f"\nSuma de saldos conocidos: {tabla['saldo_mxn'].sum(min_count=1)} MXN")

    recargada = guardar_y_comprobar(tabla, entrada, salida)
    print(f"\nExportación comprobada: {len(recargada)} filas, {len(recargada.columns)} columnas.")
    print("Se conservaron valores, tipos e identificadores; la entrada no se sobrescribió.")
    print(f"Salida: output/{salida.name} en esta lección")


if __name__ == "__main__":
    main()

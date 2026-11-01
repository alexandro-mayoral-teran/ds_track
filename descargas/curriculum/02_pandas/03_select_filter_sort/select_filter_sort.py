"""Selecciona y ordena una cartera ficticia conservando la tabla de entrada."""

from pathlib import Path

import pandas as pd


COLUMNAS_ENTRADA = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "dias_atraso"]
COLUMNAS_SALIDA = ["id_credito", "segmento", "saldo_mxn", "dias_atraso"]
TIPOS = {
    "id_credito": "string",
    "segmento": "string",
    "fecha_corte": "string",
    "saldo_mxn": "Int64",
    "dias_atraso": "Int64",
}


def leer_cartera(ruta):
    """Reutiliza el contrato de lectura de la lección 02, sin limpiar datos."""
    tabla = pd.read_csv(ruta, encoding="utf-8-sig", dtype=TIPOS)
    if list(tabla.columns) != COLUMNAS_ENTRADA:
        raise ValueError(f"Columnas esperadas: {COLUMNAS_ENTRADA}")
    return tabla


def seleccionar_creditos(tabla, saldo_minimo=500, atraso_minimo=5):
    """Selecciona condiciones confirmadas; un resultado desconocido no se incluye."""
    mascara = ((tabla["saldo_mxn"] >= saldo_minimo)
               & (tabla["dias_atraso"] >= atraso_minimo))
    # Esta política afecta a la máscara; no reemplaza los faltantes de la fuente.
    return tabla.loc[mascara.fillna(False), COLUMNAS_SALIDA].copy()


def seleccionar_atraso_desconocido(tabla):
    """Conserva aparte los registros cuyo atraso no se puede evaluar."""
    return tabla.loc[tabla["dias_atraso"].isna(), COLUMNAS_SALIDA].copy()


def ordenar_creditos(seleccion):
    """Ordena saldo descendente e identificador ascendente como desempate."""
    return seleccion.sort_values(
        by=["saldo_mxn", "id_credito"],
        ascending=[False, True],
        na_position="last",
    )


def guardar_seleccion(seleccion, entrada, salida):
    """Escribe la selección y verifica sus valores y orden al volver a leerla."""
    if entrada.resolve() == salida.resolve():
        raise ValueError("Entrada y salida deben ser archivos distintos.")
    salida.parent.mkdir(parents=True, exist_ok=True)
    seleccion.to_csv(salida, index=False, encoding="utf-8", lineterminator="\n")
    recargada = pd.read_csv(salida, dtype=TIPOS, encoding="utf-8-sig")
    # CSV no conserva las etiquetas de fila cuando index=False.
    if not seleccion.reset_index(drop=True).equals(recargada):
        raise ValueError("La salida no conserva la selección y su orden.")
    return recargada


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta.parent / "02_read_inspect_export" / "cartera_demo.csv"
    salida = carpeta / "output" / "creditos_seleccionados.csv"
    tabla = leer_cartera(entrada)
    original = tabla.copy(deep=True)

    seleccion = seleccionar_creditos(tabla, saldo_minimo=500, atraso_minimo=5)
    ordenada = ordenar_creditos(seleccion)
    desconocidos = seleccionar_atraso_desconocido(tabla)
    guardar_seleccion(ordenada, entrada, salida)
    if not tabla.equals(original):
        raise ValueError("La tabla de entrada fue modificada.")

    print(f"pandas: {pd.__version__}")
    print("Pregunta: saldo >= 500 MXN y atraso conocido >= 5 días.")
    print(f"Filas de entrada: {len(tabla)} | Seleccionadas: {len(ordenada)}")
    print(f"Subtotal de saldos conocidos seleccionados: {ordenada['saldo_mxn'].sum(min_count=1)} MXN")
    print(f"Registros con atraso desconocido: {len(desconocidos)}")
    print("\nSelección ordenada:")
    print(ordenada)
    print("\nAtraso desconocido, conservado aparte para revisión:")
    print(desconocidos)
    if ordenada.empty:
        print("No hay coincidencias; no se consulta una primera fila inexistente.")
    else:
        print(f"Primer ID por posición: {ordenada.iloc[0]['id_credito']}")
    print(f"\nSalida comprobada: output/{salida.name}")


if __name__ == "__main__":
    main()

"""Convertir una muestra didáctica sin perder sus valores de origen."""

from pathlib import Path

import pandas as pd


COLUMNAS_ENTRADA = [
    "id_credito", "segmento", "fecha_corte", "saldo_mxn", "pago_mxn", "dias_atraso"
]
NUMERICAS = ["saldo_mxn", "pago_mxn", "dias_atraso"]


def leer_texto(ruta):
    # Solo el campo vacío significa ausencia; conservar otros textos para revisarlos.
    tabla = pd.read_csv(
        ruta, dtype="string", encoding="utf-8-sig", keep_default_na=False,
        na_values=[""],
    )
    if list(tabla.columns) != COLUMNAS_ENTRADA:
        raise ValueError("Se esperan las seis columnas del diccionario, en ese orden")
    return tabla


def convertir_entero(texto):
    # La muestra exige enteros pequeños: no redondear ni truncar fracciones.
    numero = pd.to_numeric(texto, errors="coerce")
    es_entero = numero.notna() & (numero % 1 == 0)
    incompatible = (texto.notna() & ~es_entero).astype("boolean")
    convertido = numero.where(es_entero).astype("Int64")
    return convertido, incompatible


def transformar(tabla):
    resultado = tabla.copy()
    for columna in NUMERICAS:
        # Este ciclo recorre tres nombres de columna, nunca las filas.
        resultado[columna + "_texto"] = tabla[columna]
        convertido, incompatible = convertir_entero(tabla[columna])
        resultado[columna] = convertido
        resultado[columna + "_incompatible"] = incompatible

    # Operaciones entre Series: pandas alinea sus etiquetas de índice.
    resultado["saldo_despues_pago_mxn"] = resultado["saldo_mxn"] - resultado["pago_mxn"]
    denominador = resultado["saldo_mxn"].where(resultado["saldo_mxn"] > 0)
    resultado["porcentaje_pago"] = (
        resultado["pago_mxn"] / denominador * 100
    ).astype("Float64")

    # Asignación en un solo paso sobre la tabla que queremos modificar.
    resultado["estado_atraso"] = pd.Series("sin dato evaluable", index=tabla.index, dtype="string")
    conocido = resultado["dias_atraso"].notna()
    resultado.loc[conocido, "estado_atraso"] = "menos de 30 dias"
    resultado.loc[(resultado["dias_atraso"] >= 30).fillna(False), "estado_atraso"] = "30 dias o mas"
    return resultado


def guardar_y_comprobar(resultado, entrada, salida):
    if entrada.resolve() == salida.resolve():
        raise ValueError("La salida no puede reemplazar la fuente")
    salida.parent.mkdir(parents=True, exist_ok=True)
    resultado.to_csv(salida, index=False, encoding="utf-8", lineterminator="\n")
    # CSV no almacena tipos: restaurarlos al leer y tolerar redondeo de porcentajes.
    tipos = {columna: str(tipo) for columna, tipo in resultado.dtypes.items()}
    recargada = pd.read_csv(
        salida, dtype=tipos, encoding="utf-8", keep_default_na=False, na_values=[""]
    )
    pd.testing.assert_frame_equal(
        resultado.reset_index(drop=True), recargada, check_exact=False,
        rtol=1e-12, atol=1e-12,
    )


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "cartera_conversion.csv"
    salida = carpeta / "output" / "cartera_calculada.csv"
    tabla = leer_texto(entrada)
    original = tabla.copy()
    resultado = transformar(tabla)
    pd.testing.assert_frame_equal(tabla, original)
    guardar_y_comprobar(resultado, entrada, salida)

    print(f"Entrada: {len(tabla)} filas; salida: {len(resultado)} filas")
    for columna in NUMERICAS:
        print(f"{columna}: ausentes={tabla[columna].isna().sum()}, "
              f"incompatibles={resultado[columna + '_incompatible'].sum()}")
    completas = resultado["saldo_despues_pago_mxn"].notna()
    base = resultado.loc[completas]
    saldo = base["saldo_mxn"].sum(min_count=1)
    pago = base["pago_mxn"].sum(min_count=1)
    restante = base["saldo_despues_pago_mxn"].sum(min_count=1)
    print(f"Filas con resta evaluable: {len(base)}; saldo={saldo}; pago={pago}; restante={restante}")
    if not base.empty and saldo - pago != restante:
        raise ValueError("La conciliacion de la misma base no coincide")
    print(resultado.head(3)[["id_credito", "saldo_despues_pago_mxn", "porcentaje_pago"]].to_string(index=False))
    print(f"Salida comprobada: {salida.name}")


if __name__ == "__main__":
    main()

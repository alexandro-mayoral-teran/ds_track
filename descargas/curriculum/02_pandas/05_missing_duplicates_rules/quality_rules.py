"""Particionar registros por reglas didácticas, conservando evidencia de rechazo."""

from pathlib import Path

import pandas as pd


COLUMNAS = ["id_credito", "segmento", "fecha_corte", "saldo_mxn", "pago_mxn", "dias_atraso"]
NUMERICAS = ["saldo_mxn", "pago_mxn", "dias_atraso"]
CLAVE = ["id_credito", "fecha_corte"]
SEGMENTOS = ["consumo", "servicios", "comercio", "educacion"]


def leer_fuente(ruta):
    tabla = pd.read_csv(ruta, dtype="string", encoding="utf-8-sig",
                        keep_default_na=False, na_values=[""])
    if list(tabla.columns) != COLUMNAS:
        raise ValueError("Las columnas no coinciden con el diccionario")
    return tabla


def evaluar(tabla):
    # El índice de trabajo es único; numero_registro rastrea la posición en la entrada.
    trabajo = tabla.reset_index(drop=True).copy()
    trabajo.insert(0, "numero_registro", pd.Series(range(1, len(tabla) + 1), dtype="Int64"))
    reglas = {}
    for columna in COLUMNAS:
        reglas[columna + "_ausente"] = trabajo[columna].isna()
    for columna in NUMERICAS:
        texto = trabajo[columna].copy()
        numero = pd.to_numeric(texto, errors="coerce")
        entero = numero.notna() & (numero % 1 == 0)
        trabajo[columna + "_texto"] = texto
        trabajo[columna] = numero.where(entero).astype("Int64")
        reglas[columna + "_incompatible"] = texto.notna() & ~entero
        reglas[columna + "_negativo"] = trabajo[columna] < 0

    reglas["segmento_fuera_catalogo"] = trabajo["segmento"].notna() & ~trabajo["segmento"].isin(SEGMENTOS)
    reglas["pago_supera_saldo"] = trabajo["pago_mxn"] > trabajo["saldo_mxn"]
    clave_presente = trabajo[CLAVE].notna().all(axis=1)
    reglas["clave_repetida"] = clave_presente & trabajo.duplicated(subset=CLAVE, keep=False)

    # Cada regla produce una columna lógica: True significa incumplimiento confirmado.
    banderas = pd.DataFrame(reglas, index=trabajo.index).fillna(False).astype("boolean")
    invalido = banderas.any(axis=1)
    motivos = pd.Series("", index=trabajo.index, dtype="string")
    for nombre in banderas.columns:
        mascara = banderas[nombre]
        # Añadir todos los motivos; el separador solo aparece a partir del segundo.
        separador = pd.Series("", index=trabajo.index, dtype="string")
        separador.loc[motivos != ""] = "; "
        motivos.loc[mascara] = motivos.loc[mascara] + separador.loc[mascara] + nombre
    trabajo["motivos"] = motivos
    trabajo["saldo_despues_pago_mxn"] = trabajo["saldo_mxn"] - trabajo["pago_mxn"]
    aceptados = trabajo.loc[~invalido].copy()
    rechazados = trabajo.loc[invalido].copy()
    comprobar_particion(trabajo, aceptados, rechazados)
    return trabajo, aceptados, rechazados, banderas


def comprobar_particion(trabajo, aceptados, rechazados):
    if len(aceptados) + len(rechazados) != len(trabajo):
        raise ValueError("El conteo no concilia")
    juntos = pd.concat([aceptados, rechazados]).sort_values("numero_registro").reset_index(drop=True)
    pd.testing.assert_frame_equal(trabajo.reset_index(drop=True), juntos)
    if not aceptados["motivos"].eq("").all() or rechazados["motivos"].eq("").any():
        raise ValueError("Los motivos no coinciden con la particion")
    if aceptados[CLAVE].isna().any(axis=None) or aceptados.duplicated(subset=CLAVE).any():
        raise ValueError("Las claves aceptadas no son completas y unicas")
    # Comparar saldos interpretables. No afirmar que los NA representan cero.
    total = trabajo["saldo_mxn"].sum(min_count=1)
    if pd.notna(total):
        partes = pd.Series([
            aceptados["saldo_mxn"].sum(min_count=1),
            rechazados["saldo_mxn"].sum(min_count=1),
        ], dtype="Int64")
        if partes.sum(min_count=1) != total:
            raise ValueError("El saldo interpretable no concilia")


def exportar(trabajo, aceptados, rechazados, banderas, entrada, carpeta):
    tablas = {"aceptados.csv": aceptados, "rechazados.csv": rechazados,
              "reglas_por_registro.csv": banderas.copy()}
    tablas["reglas_por_registro.csv"].insert(0, "numero_registro", trabajo["numero_registro"])
    rutas = {nombre: carpeta / nombre for nombre in tablas}
    if any(ruta.resolve() == entrada.resolve() for ruta in rutas.values()):
        raise ValueError("Una salida reemplazaria la fuente")
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, tabla in tablas.items():
        ruta = rutas[nombre]
        tabla.to_csv(ruta, index=False, encoding="utf-8", lineterminator="\n")
        recargada = pd.read_csv(ruta, dtype={c: str(t) for c, t in tabla.dtypes.items()},
                               keep_default_na=False, na_values=[""])
        # Un motivo vacío significa aceptación; restaurar solo ese campo textual.
        if "motivos" in recargada:
            recargada["motivos"] = recargada["motivos"].fillna("")
        pd.testing.assert_frame_equal(tabla.reset_index(drop=True), recargada, check_exact=True)


def main():
    carpeta = Path(__file__).resolve().parent
    entrada = carpeta / "cartera_calidad.csv"
    fuente = leer_fuente(entrada)
    original = fuente.copy()
    trabajo, aceptados, rechazados, banderas = evaluar(fuente)
    pd.testing.assert_frame_equal(fuente, original)
    exportar(trabajo, aceptados, rechazados, banderas, entrada, carpeta / "output")
    print(f"Entrada={len(fuente)}; aceptados={len(aceptados)}; rechazados={len(rechazados)}")
    print(f"Saldo interpretable: entrada={trabajo['saldo_mxn'].sum(min_count=1)}, "
          f"aceptados={aceptados['saldo_mxn'].sum(min_count=1)}, "
          f"rechazados={rechazados['saldo_mxn'].sum(min_count=1)}")
    print(f"Saldo sin interpretar: {trabajo['saldo_mxn'].isna().sum()} registros")
    print(f"Incumplimientos: {banderas.sum().sum()} (una fila puede tener varios)")
    print(rechazados[["numero_registro", "id_credito", "motivos"]].to_string(index=False))
    print("Exportaciones comprobadas; fuente intacta")


if __name__ == "__main__":
    main()

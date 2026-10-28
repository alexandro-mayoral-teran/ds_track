"""Pruebas sin servidor ni AppTest; trabajar en la copia preparada."""

import copy
import csv
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import unittest

from cartera import analizar, leer_cartera
from entradas import preparar_filtros
from salidas import preparar_descargas


class PruebasModelo(unittest.TestCase):
    def setUp(self):
        # Ejemplo independiente: dos créditos, un corte, pesos enteros conocidos.
        self.filas = [
            {"id_credito": "001", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 0},
            {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": 2000},
        ]

    def test_frontera_incluye_igual(self):
        resultado = analizar(self.filas, "2026-09-30", ["servicios"], 2000)
        self.assertEqual(resultado["seleccion"], [self.filas[1]])
        self.assertEqual(resultado["universo"], {"cantidad": 2, "saldo_mxn": 2000})
        self.assertEqual(resultado["indicadores"],
                         {"cantidad": 1, "saldo_mxn": 2000, "porcentaje_creditos": 50.0})

    def test_vacio_cero_y_corte_ausente(self):
        cero = analizar(self.filas, "2026-09-30", ["comercio"], 0)
        vacio = analizar(self.filas, "2026-09-30", [], 0)
        ausente = analizar(self.filas, "2026-11-30", ["comercio"], 0)
        self.assertEqual(cero["indicadores"], {"cantidad": 1, "saldo_mxn": 0, "porcentaje_creditos": 50.0})
        self.assertEqual(vacio["indicadores"], {"cantidad": 0, "saldo_mxn": 0, "porcentaje_creditos": 0.0})
        self.assertEqual(ausente["universo"], {"cantidad": 0, "saldo_mxn": 0})
        self.assertIsNone(ausente["indicadores"]["porcentaje_creditos"])
        self.assertEqual(analizar([], "2026-09-30", [], 0)["seleccion"], [])

    def test_valida_incluso_fuera_del_filtro(self):
        for saldo in (-1, True, None, 1.5, 1_000_001):
            with self.subTest(saldo=saldo):
                filas = copy.deepcopy(self.filas)
                filas[0]["saldo_mxn"] = saldo
                with self.assertRaises(ValueError):
                    analizar(filas, "2026-10-31", ["servicios"], 2000)
        with self.assertRaises(ValueError):
            analizar(self.filas + [dict(self.filas[0])], "2026-10-31", [], 0)

    def test_texto_minimo_y_limites(self):
        for texto, esperado in [("0", 0), (" 2000 ", 2000), ("1000000", 1_000_000)]:
            with self.subTest(texto=texto):
                self.assertEqual(preparar_filtros("2026-09-30", [], texto)["minimo_mxn"], esperado)
        for texto in ("", "-1", "+1", "1.5", "2,000", "1000001"):
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                preparar_filtros("2026-09-30", [], texto)

    def test_no_muta_y_devuelve_copias(self):
        anterior = copy.deepcopy(self.filas)
        resultado = analizar(self.filas, "2026-09-30", ["servicios"], 0)
        resultado["seleccion"][0]["saldo_mxn"] = 999
        self.assertEqual(self.filas, anterior)

    def test_csv_contexto_con_referencia_explicita(self):
        filas = leer_cartera(Path(__file__).with_name("cartera.csv"))
        resultado = analizar(filas, "2026-09-30", ["comercio", "servicios"], 2000)
        anterior = copy.deepcopy(resultado)
        salida = preparar_descargas(resultado, "1205-v1")
        lector = csv.DictReader(StringIO(salida["csv"].decode("utf-8")))
        self.assertEqual(lector.fieldnames, ["id_credito", "segmento", "fecha_corte", "saldo_mxn"])
        self.assertEqual(list(lector), [
            {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": "2000"},
            {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": "2500"},
        ])
        contexto = json.loads(salida["contexto"])
        self.assertEqual(contexto["filtros"], {"corte": "2026-09-30", "segmentos": ["comercio", "servicios"], "minimo_mxn": 2000})
        self.assertEqual(contexto["universo"], {"cantidad": 3, "saldo_mxn": 4500})
        self.assertEqual(contexto["indicadores"]["cantidad"], 2)
        self.assertEqual(contexto["indicadores"]["saldo_mxn"], 4500)
        self.assertAlmostEqual(contexto["indicadores"]["porcentaje_creditos"], 200 / 3)
        self.assertEqual(contexto["filas_csv"], 2)
        self.assertEqual(contexto["sha256_csv"], sha256(salida["csv"]).hexdigest())
        self.assertEqual(resultado, anterior)

    def test_csv_vacio_con_encabezado(self):
        resultado = analizar(self.filas, "2026-09-30", [], 0)
        salida = preparar_descargas(resultado, "1205-v1")
        self.assertEqual(salida["csv"], b"id_credito,segmento,fecha_corte,saldo_mxn\n")
        self.assertEqual(json.loads(salida["contexto"])["filas_csv"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

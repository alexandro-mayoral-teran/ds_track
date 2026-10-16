"""Casos de función: selección, bases, ausencia y conservación de entrada."""

import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.transformacion import summarize
from pruebas_0504.muestras import CUT, detail_fixture


class PruebasResumen(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de CADA método test_: ninguna prueba hereda cambios.
        self.detail = detail_fixture()

    def test_mediana_con_cero_y_medio_peso(self):
        selected, summary = summarize(self.detail, CUT)
        row = summary.set_index("segmento").loc["comercio"]
        self.assertEqual(len(selected), 5)
        self.assertEqual(row["registros"], 3)
        self.assertEqual(row["conocidos"], 2)
        self.assertEqual(row["mediana_mxn"], 0.5)
        self.assertAlmostEqual(row["cobertura_pct"], 200 / 3, places=10)
        self.assertEqual(row["fraccion"], "2/3")

    def test_ausencia_y_segmento_sin_registros(self):
        _, summary = summarize(self.detail, CUT)
        rows = summary.set_index("segmento")
        unknown = rows.loc["educacion"]
        empty = rows.loc["servicios"]
        self.assertEqual(unknown["registros"], 1)
        self.assertEqual(unknown["conocidos"], 0)
        self.assertEqual(unknown["cobertura_pct"], 0)
        self.assertTrue(pd.isna(unknown["mediana_mxn"]))
        self.assertEqual(empty["registros"], 0)
        self.assertTrue(pd.isna(empty["mediana_mxn"]))
        self.assertTrue(pd.isna(empty["cobertura_pct"]))

    def test_corte_sin_filas_y_entrada_vacia(self):
        for detail, cut in [(self.detail, "2027-01-31"), (self.detail.iloc[:0], CUT)]:
            with self.subTest(cut=cut, filas=len(detail)):
                selected, summary = summarize(detail, cut)
                self.assertTrue(selected.empty)
                self.assertEqual(summary["segmento"].tolist(),
                                 ["comercio", "consumo", "educacion", "servicios"])
                self.assertEqual(summary["registros"].tolist(), [0, 0, 0, 0])
                self.assertEqual(summary["conocidos"].tolist(), [0, 0, 0, 0])
                self.assertTrue(summary["mediana_mxn"].isna().all())
                self.assertTrue(summary["cobertura_pct"].isna().all())

    def test_no_modifica_entrada_ni_comparte_seleccion(self):
        before = self.detail.copy(deep=True)
        selected, _ = summarize(self.detail, CUT)
        assert_frame_equal(self.detail, before, check_exact=True)
        selected.loc[selected.index[0], "saldo_mxn"] = 999
        assert_frame_equal(self.detail, before, check_exact=True)

    def test_fecha_invalida_se_rechaza(self):
        for cut in ["2026-02-30", "2026-1-31", "texto"]:
            with self.subTest(cut=cut):
                with self.assertRaises(ValueError):
                    summarize(self.detail, cut)

    def test_un_saldo_y_mediana_impar(self):
        for values, expected in [([0], 0), ([1, 2, 100], 2)]:
            with self.subTest(saldos=values):
                detail = self.detail.iloc[:len(values)].copy(deep=True)
                detail["saldo_mxn"] = pd.Series(values, index=detail.index, dtype="Int64")
                _, summary = summarize(detail, CUT)
                row = summary.set_index("segmento").loc["comercio"]
                self.assertEqual(row["mediana_mxn"], expected)
                self.assertEqual(row["conocidos"], len(values))
                self.assertEqual(row["cobertura_pct"], 100)

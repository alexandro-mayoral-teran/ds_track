"""Validaciones de opciones y conexión con la lectura/conciliación existente."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.flujo import build_analysis
from analisis_cartera.revision import review_summary
from pruebas_0504.muestras import CUT, CREDITS, write_sources


class PruebasRevision(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.source = write_sources(Path(temporary.name) / "fuentes")

    def test_none_conserva_resumen_y_fuentes(self):
        before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        expected = build_analysis(self.source, CUT)["resumen"]
        assert_frame_equal(review_summary(str(self.source)), expected, check_exact=True)
        assert_frame_equal(review_summary(self.source, None, segments=None), expected, check_exact=True)
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, before)

    def test_lista_explicita_define_orden_y_conserva_ausencia(self):
        segments = ["educacion", "comercio"]
        actual = review_summary(self.source, CUT, segments=segments)
        self.assertEqual(actual["segmento"].tolist(), segments)
        self.assertEqual(segments, ["educacion", "comercio"])
        self.assertTrue(pd.isna(actual.iloc[0]["mediana_mxn"]))
        self.assertEqual(actual.iloc[0]["cobertura_pct"], 0)
        self.assertEqual(actual.iloc[1]["mediana_mxn"], 0.5)
        actual.loc[1, "mediana_mxn"] = 999
        fresh = review_summary(self.source, CUT, segments=segments)
        self.assertEqual(fresh.iloc[1]["mediana_mxn"], 0.5)

    def test_lista_vacia_conserva_estructura(self):
        complete = review_summary(self.source)
        empty = review_summary(self.source, segments=[])
        assert_frame_equal(empty, complete.iloc[:0], check_exact=True)

    def test_corte_valido_sin_registros(self):
        empty_cut = review_summary(self.source, "2027-01-31")
        self.assertEqual(empty_cut["registros"].tolist(), [0, 0, 0, 0])
        self.assertTrue(empty_cut["mediana_mxn"].isna().all())
        self.assertTrue(empty_cut["cobertura_pct"].isna().all())

    def test_opciones_invalidas_antes_de_leer(self):
        absent = self.source / "no_existe"
        for segments, error in [("comercio", TypeError), (("comercio",), TypeError),
                                ([1], TypeError), (["otro"], ValueError),
                                (["comercio", "comercio"], ValueError)]:
            with self.subTest(segments=segments):
                with self.assertRaises(error):
                    review_summary(absent, segments=segments)
        with self.assertRaises(TypeError):
            review_summary(3)
        with self.assertRaises(ValueError):
            review_summary("")
        with self.assertRaises(TypeError):
            review_summary(self.source, CUT, ["comercio"])

    def test_lista_vacia_no_omite_validacion_de_datos(self):
        write_sources(self.source, credits=[*CREDITS, CREDITS[0]])
        with self.assertRaisesRegex(ValueError, "Clave de crédito"):
            review_summary(self.source, segments=[])

    def test_fuente_ausente_no_se_convierte_en_tabla_vacia(self):
        with self.assertRaises(FileNotFoundError):
            review_summary(self.source / "no_existe", segments=[])
